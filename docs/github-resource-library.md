# Curated GitHub Repository Library

**Maintainer:** VenkataKrishnaYalagala  
**Catalog checked:** 2026-11-15  
**Purpose:** A practical research shelf for Aptitude Mind Plus, Agastya Academy, Garuda GATE Academy, YouTube production, filmmaking, robotics and future AI projects.

> **This catalog is a list of external repositories, NOT forks, local installations, endorsements, or software integrated into this website.** Repositories were individually checked through GitHub for existence and non-archived status on the date above. Stars, activity, names and licenses can change. Download only from trusted official projects.

## Start here

Use GitHub **Stars** as a personal library. Star useful upstream projects instead of forking or cloning every high-starred repository. Fork only when changing source code for a specific project; create your own original repositories for your platforms and films. A star is a bookmark, not permission to redistribute or commercially exploit the code.

- **Now:** most directly useful to current work.
- **Explore:** compare with alternatives when a real requirement appears.
- **Later:** keep as reference for larger projects.
- **Heavy:** may require substantial RAM/GPU, paid compute, or a separate workstation.

### Bring this collection into GitHub Stars

The import source is [github-stars.txt](github-stars.txt), containing **113 verified repository names**. The safe helper [star_github_resources.py](../scripts/star_github_resources.py) previews by default and only modifies GitHub Stars with `--apply`.

```bash
# Run after cloning this repository to your computer.
# Install GitHub CLI if needed (for macOS: brew install gh), then authenticate:
gh auth login
python3 scripts/star_github_resources.py
# Review the list, then add the stars to the account authenticated in gh:
python3 scripts/star_github_resources.py --apply
```

Re-running the import is safe: GitHub's star API uses an idempotent PUT. A temporary API throttle stops the script with an error; simply re-run later. No credentials are embedded in this repository.

**Do not execute or install all listed projects.** Especially review third-party skills, MCP servers, actions and plugins for permissions, malicious code, untrusted instructions and supply-chain risk. Respect each project's current license and media usage rights. Remotion, n8n, and other source-available/fair-code tools may have commercial-use conditions. For the present small Apple-silicon machine, start with modest local models; heavy AI video-generation models and high-end robot simulation are references for later.

## Most immediately useful

1. [openai/skills](https://github.com/openai/skills)
2. [anthropics/skills](https://github.com/anthropics/skills)
3. [agentskills/agentskills](https://github.com/agentskills/agentskills)
4. [vercel-labs/skills](https://github.com/vercel-labs/skills)
5. [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
6. [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
7. [openai/codex](https://github.com/openai/codex)
8. [blender/blender](https://github.com/blender/blender)
9. [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)
10. [obsproject/obs-studio](https://github.com/obsproject/obs-studio)
11. [remotion-dev/remotion](https://github.com/remotion-dev/remotion)
12. [ManimCommunity/manim](https://github.com/ManimCommunity/manim)
13. [jupyterlab/jupyterlab](https://github.com/jupyterlab/jupyterlab)
14. [sympy/sympy](https://github.com/sympy/sympy)
15. [numpy/numpy](https://github.com/numpy/numpy)
16. [matplotlib/matplotlib](https://github.com/matplotlib/matplotlib)
17. [KaTeX/KaTeX](https://github.com/KaTeX/KaTeX)
18. [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid)
19. [vitejs/vite](https://github.com/vitejs/vite)
20. [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)
21. [shadcn-ui/ui](https://github.com/shadcn-ui/ui)
22. [microsoft/playwright](https://github.com/microsoft/playwright)
23. [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)
24. [puckeditor/puck](https://github.com/puckeditor/puck)
25. [ollama/ollama](https://github.com/ollama/ollama)
26. [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
27. [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)
28. [arduino/arduino-cli](https://github.com/arduino/arduino-cli)
29. [platformio/platformio-core](https://github.com/platformio/platformio-core)
30. [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
31. [microsoft/markitdown](https://github.com/microsoft/markitdown)
32. [github/gitignore](https://github.com/github/gitignore)
33. [actions/starter-workflows](https://github.com/actions/starter-workflows)
34. [astral-sh/ruff](https://github.com/astral-sh/ruff)
35. [astral-sh/uv](https://github.com/astral-sh/uv)
36. [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)

## Complete categorized directory

### Agent Skills, curated skills and MCP

Reusable agent instructions and integration catalogs; inspect each skill before installing it.

| Repository | Use | Stage |
|---|---|---|
| [openai/skills](https://github.com/openai/skills) | Official Codex skills catalog | Now |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's public Agent Skills examples | Now |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | Open Agent Skills specification | Now |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | CLI for managing agent skills | Now |
| [google/skills](https://github.com/google/skills) | Agent skills for Google's technologies | Explore |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Engineering-oriented reusable skills | Explore |
| [obra/superpowers](https://github.com/obra/superpowers) | Skill framework and development workflow | Explore |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Large cross-platform skill directory | Explore |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Curated Claude skill references | Explore |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | Large community skill catalog; review provenance | Explore |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Directory of MCP integrations | Now |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Reference MCP server implementations | Now |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) | Build MCP servers and apps | Explore |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Examples of AI applications and agents | Explore |

### Coding agents and AI application frameworks

Agents, browser automation, research and reusable AI workflows; choose one framework per project rather than install them all.

| Repository | Use | Stage |
|---|---|---|
| [openai/codex](https://github.com/openai/codex) | OpenAI terminal coding agent | Now |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | Claude terminal coding agent | Explore |
| [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Gemini terminal coding agent | Explore |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Browser-agent automation library | Explore |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | LLM application building blocks | Explore |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Stateful agent orchestration | Explore |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Collaborative-agent workflows | Explore |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Multi-agent programming framework | Explore |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Document ingestion and retrieval | Explore |
| [langgenius/dify](https://github.com/langgenius/dify) | Visual AI app and RAG platform | Explore |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | Visual AI agent/workflow builder | Explore |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Unified LLM routing and cost management | Explore |

### Filmmaking, video, VFX and audio workflows

Editing, shooting, motion graphics, color, upscaling and generative workflows for short films and educational YouTube videos.

| Repository | Use | Stage |
|---|---|---|
| [blender/blender](https://github.com/blender/blender) | 3D, simulation, animation and VFX | Now |
| [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | Batch video and audio conversion | Now |
| [obsproject/obs-studio](https://github.com/obsproject/obs-studio) | Screen and camera recording | Now |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | Code-driven video, graphics and subtitles; check licensing | Now |
| [mltframework/mlt](https://github.com/mltframework/mlt) | Video-processing pipeline used by editors | Explore |
| [OpenShot/openshot-qt](https://github.com/OpenShot/openshot-qt) | Desktop video editor | Explore |
| [KDE/kdenlive](https://github.com/KDE/kdenlive) | Multi-track open-source video editor | Explore |
| [AcademySoftwareFoundation/OpenColorIO](https://github.com/AcademySoftwareFoundation/OpenColorIO) | Professional color management | Later |
| [opentoonz/opentoonz](https://github.com/opentoonz/opentoonz) | 2D animation software | Explore |
| [upscayl/upscayl](https://github.com/upscayl/upscayl) | AI image upscaling; GPU capacity matters | Explore |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | Downloading material you own or can lawfully reuse | Explore |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Node-based AI media generation; resource intensive | Heavy |
| [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI) | Visual AI generation workflows; resource intensive | Heavy |

### STEM teaching, mathematics and interactive diagrams

Create polished lessons, mathematics animations, interactive notes and explanatory diagrams.

| Repository | Use | Stage |
|---|---|---|
| [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Maintainable math animations for lessons | Now |
| [3b1b/manim](https://github.com/3b1b/manim) | Reference for mathematical animation techniques | Explore |
| [jupyterlab/jupyterlab](https://github.com/jupyterlab/jupyterlab) | Notebook-based teaching and computation | Now |
| [marimo-team/marimo](https://github.com/marimo-team/marimo) | Interactive and version-controlled Python notebooks | Explore |
| [sympy/sympy](https://github.com/sympy/sympy) | Symbolic algebra and equation solving | Now |
| [numpy/numpy](https://github.com/numpy/numpy) | Numerical arrays | Now |
| [scipy/scipy](https://github.com/scipy/scipy) | Scientific computing | Explore |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | PYQ and question-bank data analysis | Explore |
| [matplotlib/matplotlib](https://github.com/matplotlib/matplotlib) | Plotting educational visuals | Now |
| [KaTeX/KaTeX](https://github.com/KaTeX/KaTeX) | Render formulas on academy websites | Now |
| [mathjax/MathJax](https://github.com/mathjax/MathJax) | Accessible web mathematics rendering | Explore |
| [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | Diagrams from text | Now |

### Website design, drag-and-drop and quality

Aptitude Mind Plus, Agastya Academy, Garuda GATE Academy, responsive components and editors.

| Repository | Use | Stage |
|---|---|---|
| [vercel/next.js](https://github.com/vercel/next.js) | React-based full-stack web framework | Explore |
| [vitejs/vite](https://github.com/vitejs/vite) | Fast frontend development and builds | Now |
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | Design systems and responsive styling | Now |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | Reusable accessible UI patterns | Now |
| [storybookjs/storybook](https://github.com/storybookjs/storybook) | Isolated UI development and review | Explore |
| [microsoft/playwright](https://github.com/microsoft/playwright) | End-to-end browser testing | Now |
| [vitest-dev/vitest](https://github.com/vitest-dev/vitest) | Fast tests for JavaScript/TypeScript | Explore |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | Interactive whiteboard and canvas SDK | Explore |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | Hand-drawn diagrams and collaboration | Now |
| [puckeditor/puck](https://github.com/puckeditor/puck) | Drag-and-drop React editing | Now |
| [GrapesJS/grapesjs](https://github.com/GrapesJS/grapesjs) | Visual page-building framework | Explore |
| [payloadcms/payload](https://github.com/payloadcms/payload) | TypeScript content management | Explore |
| [directus/directus](https://github.com/directus/directus) | Database-backed visual admin/CMS | Explore |

### Courses, online shops and platform backends

Learning management, student login, publishing materials and future commerce; evaluate privacy and licensing before deployment.

| Repository | Use | Stage |
|---|---|---|
| [strapi/strapi](https://github.com/strapi/strapi) | Headless CMS alternative | Explore |
| [supabase/supabase](https://github.com/supabase/supabase) | Managed Postgres, authentication and storage | Explore |
| [appwrite/appwrite](https://github.com/appwrite/appwrite) | Backend and authentication alternative | Explore |
| [medusajs/medusa](https://github.com/medusajs/medusa) | Commerce architecture for study-material shops | Explore |
| [saleor/saleor](https://github.com/saleor/saleor) | Composable e-commerce alternative | Later |
| [WordPress/wordpress-develop](https://github.com/WordPress/wordpress-develop) | WordPress core reference, not a ready-made site | Explore |
| [moodle/moodle](https://github.com/moodle/moodle) | Full learning management system | Explore |

### Local AI, transcription and model experimentation

Start with compact models on Apple silicon; large diffusion and video systems may exceed an 8 GB machine's comfortable capacity.

| Repository | Use | Stage |
|---|---|---|
| [ollama/ollama](https://github.com/ollama/ollama) | Easy local model runner | Now |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Efficient local LLM inference | Now |
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Local speech-to-text for video captions | Now |
| [ml-explore/mlx](https://github.com/ml-explore/mlx) | Apple-silicon machine learning | Explore |
| [ml-explore/mlx-examples](https://github.com/ml-explore/mlx-examples) | Examples for MLX | Explore |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Model loading and experimentation | Explore |
| [huggingface/diffusers](https://github.com/huggingface/diffusers) | Diffusion model toolkit; often hardware intensive | Heavy |
| [openai/whisper](https://github.com/openai/whisper) | Whisper speech recognition reference | Explore |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Alternative optimized transcription runtime | Explore |
| [m-bain/whisperX](https://github.com/m-bain/whisperX) | Word timing and diarization workflows | Explore |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | Browser interface to local models | Explore |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | High-throughput model serving; generally server-class hardware | Heavy |

### Robotics, Arduino and hardware projects

Build sensor, microcontroller and portfolio projects now; introduce ROS and drone stacks as projects grow.

| Repository | Use | Stage |
|---|---|---|
| [arduino/arduino-cli](https://github.com/arduino/arduino-cli) | Arduino builds and uploads from terminal | Now |
| [platformio/platformio-core](https://github.com/platformio/platformio-core) | Cross-board firmware build and libraries | Now |
| [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32) | ESP32 Arduino support | Now |
| [espressif/esp-idf](https://github.com/espressif/esp-idf) | Advanced ESP32 firmware platform | Explore |
| [ros2/ros2](https://github.com/ros2/ros2) | Robot Operating System framework | Later |
| [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim) | Robot simulation; resource intensive | Heavy |
| [ArduPilot/ardupilot](https://github.com/ArduPilot/ardupilot) | Autonomous vehicle stack | Later |
| [PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot) | Flight-controller firmware | Later |
| [opencv/opencv](https://github.com/opencv/opencv) | Machine vision for robots and lessons | Explore |
| [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | Object detection; check AGPL/commercial terms | Later |
| [micropython/micropython](https://github.com/micropython/micropython) | Python on microcontrollers | Explore |
| [micro-ROS/micro_ros_arduino](https://github.com/micro-ROS/micro_ros_arduino) | ROS integrations for microcontrollers | Later |

### Workflow automation and document processing

Automate publishing, content pipelines and internal work; do not turn on production posting without review.

| Repository | Use | Stage |
|---|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Visual workflow automation; check license terms | Explore |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | Visual automation platform | Explore |
| [windmill-labs/windmill](https://github.com/windmill-labs/windmill) | Code-based workflow orchestration | Explore |
| [kestra-io/kestra](https://github.com/kestra-io/kestra) | Event-driven workflows and orchestration | Later |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | Convert documents and office files to Markdown | Now |
| [docker/compose](https://github.com/docker/compose) | Multi-service local development | Explore |
| [docker/awesome-compose](https://github.com/docker/awesome-compose) | Sample deployment setups | Explore |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | Public API directory; check each service's terms | Explore |

### Engineering quality and security

Professional repository maintenance, reproducible builds, testing and secret scanning.

| Repository | Use | Stage |
|---|---|---|
| [github/gitignore](https://github.com/github/gitignore) | Safe repository ignore templates | Now |
| [actions/starter-workflows](https://github.com/actions/starter-workflows) | GitHub Actions CI examples | Now |
| [pre-commit/pre-commit](https://github.com/pre-commit/pre-commit) | Local pre-commit quality checks | Explore |
| [astral-sh/ruff](https://github.com/astral-sh/ruff) | Fast Python linting and formatting | Now |
| [astral-sh/uv](https://github.com/astral-sh/uv) | Fast Python dependencies and environments | Now |
| [renovatebot/renovate](https://github.com/renovatebot/renovate) | Dependency update automation alternative | Explore |
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | Scan for accidentally committed secrets | Now |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | Dependency and configuration security scans | Explore |

### Career and reference libraries

Useful educational resources rather than software to deploy.

| Repository | Use | Stage |
|---|---|---|
| [ossu/computer-science](https://github.com/ossu/computer-science) | Self-study computer science curriculum | Explore |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | Collection of freely available programming books | Explore |

## Project selection guidelines

- **Aptitude Mind Plus:** Manim, SymPy, KaTeX, Playwright, Puck or GrapesJS, then the existing site stack. Prefer verified official previous-year papers and original explanations.
- **Agastya Academy / Garuda GATE Academy:** share components and visual patterns, but keep branding, syllabi, licensing and data separated across products. Consider a CMS only when manual updates become the bottleneck.
- **YouTube and cinema:** OBS for recording, FFmpeg for batch assembly, Remotion or Manim for controlled effects, Blender for VFX and Whisper for transcripts. Check license terms, including commercially distributed output.
- **Robotics:** Arduino CLI, PlatformIO, ESP32 and MicroPython first; OpenCV, ROS and simulation only when needed for an actual prototype.
- **Personal AI:** begin with Ollama or llama.cpp and whisper.cpp; do not run huge generative video models on a memory-constrained Mac.
- **Security and account maintenance:** never paste tokens into commits, copy third-party automation blindly or auto-enable publishing/deployment. Keep backups and use pull requests for runtime code changes.

## Curation policy

This is a **focused library, not a ranking of all of GitHub**. Importance, popularity and usefulness are distinct. A project with fewer stars can be the correct choice for your work. Every repo in this catalog existed and was non-archived at the verification date, but no complete source-code security or license audit was performed. Evaluate dependencies and maintenance again before installation. This directory is maintained in the dedicated Creator & STEM Toolkit repository.
