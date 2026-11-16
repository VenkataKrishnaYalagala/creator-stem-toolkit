#!/usr/bin/env python3
"""Preview or apply a vetted GitHub Star import; uses existing GitHub CLI auth.

Default is read-only. Run with --apply to star each owner/repo. Never stores tokens.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

LIST_FILE = Path(__file__).resolve().parents[1] / "docs" / "github-stars.txt"
PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def read_repos(path: Path) -> list[str]:
    repos = []
    seen = set()
    for index, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        value = raw.strip()
        if not value or value.startswith("#"):
            continue
        if not PATTERN.fullmatch(value):
            raise ValueError(f"Invalid repository on line {index}: {value!r}")
        if value not in seen:
            repos.append(value)
            seen.add(value)
    return repos


def main() -> int:
    parser = argparse.ArgumentParser(description="Import curated repositories as GitHub Stars")
    parser.add_argument("--apply", action="store_true", help="Star repositories using GitHub CLI (default: preview only)")
    parser.add_argument("--limit", type=int, default=None, help="Optional number of repositories to process")
    parser.add_argument("--pause", type=float, default=1.0, help="Seconds between API writes; default 1.0")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    if args.pause < 0:
        parser.error("--pause cannot be negative")

    try:
        repos = read_repos(LIST_FILE)
    except (OSError, ValueError) as exc:
        print(f"Could not load repository list: {exc}", file=sys.stderr)
        return 2
    if args.limit:
        repos = repos[:args.limit]
    print(f"{len(repos)} unique GitHub repositories from {LIST_FILE.name}.")
    if not args.apply:
        for repo in repos:
            print(f"  DRY RUN  {repo}")
        print("No changes made. Run with --apply after reviewing the source and list.")
        return 0

    if not shutil.which("gh"):
        print("GitHub CLI 'gh' not found. Install it and run 'gh auth login'.", file=sys.stderr)
        return 2
    auth = subprocess.run(["gh", "auth", "status"], text=True, capture_output=True)
    if auth.returncode:
        print("GitHub CLI is not authenticated. Run 'gh auth login'.", file=sys.stderr)
        return 2
    successes = 0
    for index, repo in enumerate(repos, 1):
        result = subprocess.run(
            ["gh", "api", "--method", "PUT", "--silent", f"/user/starred/{repo}"],
            text=True, capture_output=True,
        )
        if result.returncode:
            print(f"Failed at {index}/{len(repos)}: {repo}. Check CLI permissions or rate limits.", file=sys.stderr)
            print(f"Successfully starred {successes} repositories before stopping. Rerun later if throttled.", file=sys.stderr)
            return 1
        successes += 1
        print(f"  Starred {index}/{len(repos)}: {repo}")
        if index < len(repos):
            time.sleep(args.pause)
    print(f"Done. {successes} GitHub Star operations completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
