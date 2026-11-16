# Filmmaking, 3D, voice and thumbnail GitHub toolkit (16 November 2026)

This is the focused creator-production supplement to [the full GitHub resource library](github-resource-library.md). Each linked repository was checked for existence and non-archived status on 16 November 2026. These are curated recommendations, **not a ranking of six-month star growth**, and a GitHub star is not the same as an installation, working integration or approved commercial license.

**Account status:** This toolkit holds links and optional import lists. Existing personal forks include `manim`, `whisper.cpp`, `skills` and `mcp-for-blender`; preserve and avoid duplicates. No new software has been installed on your Mac through this catalog.

## Five high-profile starting points for 2026

| Repository | What it does | Usage and limits |
|---|---|---|
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Node workflows for generated images, thumbnails and AI video | Established, very popular; large workflows and models require strong GPU/RAM |
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) | Text/image-to-video generation | Very heavy model inference; prefer hosted GPU; check model terms |
| [LTX-2](https://github.com/Lightricks/LTX-2) | Generated video with audio workflows | Code and model-weight licenses differ; advanced GPU workloads |
| [TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | High-quality *image-to-3D* textured assets | Linux + NVIDIA GPU with at least 24 GB VRAM per project README; not local on M1 8 GB |
| [Remotion](https://github.com/remotion-dev/remotion) | Programmatic videos, lower thirds, titles and reusable templates | Very useful for repeatable lesson graphics; evaluate commercial/automation licensing |

These are five notable choices across the crafts, **not five repositories proven to have gained the most GitHub stars in the past six months**. Popularity, date of latest activity, maintainability, licenses and actual task fit all matter.

## Five useful choices for each craft

A project may appear in more than one craft because it can perform several jobs. All GitHub links point to the upstream project rather than unofficial reuploads.

### 1. Editing, automatic rough cuts and batch processing

| Repository | Purpose | Priority |
|---|---|---|
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Audio/video conversion, assembly, filters and delivery | **Now**; also in original catalog |
| [Auto-Editor](https://github.com/WyattBlue/auto-editor) | Rough cuts based on audio/motion; check Final Cut/Resolve interchange | **Now**; protect teaching pauses |
| [LosslessCut](https://github.com/mifi/lossless-cut) | Fast trimming and selecting segments without full re-encode | **Now** |
| [MoviePy](https://github.com/Zulko/moviepy) | Python-scripted clips, overlays and compilations | Explore |
| [CommandPost](https://github.com/CommandPost/CommandPost) | Mac automation, especially Final Cut Pro | Explore; validate with installed Final Cut version |

For the finishing timeline, prefer your existing editor. A repository does **not** install itself or become a plugin automatically.

### 2. Text/image-to-video and generative scenes

| Repository | Purpose | Priority |
|---|---|---|
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Reusable nodes for image/video workflows | Heavy |
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) | Generative video and animation | Heavy |
| [LTX-2](https://github.com/Lightricks/LTX-2) | Video/audio generation and editing pipelines | Heavy; custom model license |
| [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) | Model inference/orchestration research and video workflows | Heavy |
| [Open-Sora](https://github.com/hpcaitech/Open-Sora) | Open video-generation research and training | Later/heavy |

Optional [LTX-Desktop](https://github.com/Lightricks/LTX-Desktop) provides a user-facing video app. On an 8 GB Apple Silicon Mac, it is not an eligible *local generation* machine according to project requirements; any cloud use may cost money.

### 3. Blender, animation and text/image-to-3D

| Repository | Purpose | Priority |
|---|---|---|
| [Blender](https://github.com/blender/blender) | Scene modeling, rigging, keyframes, lighting, rendering and compositing | **Now** |
| [mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | Community Blender bridge for AI-assisted modeling/scene changes | Explore; fork already on account, no official Blender MCP |
| [TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | Image-to-3D textured mesh generation | Heavy: Linux / NVIDIA 24 GB+ |
| [Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | 3D asset generation from images/text pipelines | Heavy; check model license |
| [Shap-E](https://github.com/openai/shap-e) | OpenAI's historical text/image-to-3D research project | Reference/older, not the newest production tool |

Also worth preserving: [TripoSR](https://github.com/VAST-AI-Research/TripoSR), fast single-image reconstruction. Text-to-3D and image-to-3D are different: some workflows first generate a reference image and then reconstruct a 3D asset. Generated meshes often need manual clean-up, rigging and topology work for animation.

### 4. Clean narration, dialogue and sound

| Repository | Purpose | Priority |
|---|---|---|
| [Audacity](https://github.com/audacity/audacity) | Record/edit dialogue, EQ, normalize and manually inspect sound | **Now** |
| [DeepFilterNet](https://github.com/Rikorose/DeepFilterNet) | Speech noise removal from recordings | **Now** as a test; compare before/after |
| [RNNoise](https://github.com/xiph/rnnoise) | Noise suppression for voice | Explore |
| [Resemble Enhance](https://github.com/resemble-ai/resemble-enhance) | Speech enhancement/denoising experiments | Explore; verify hardware and model rights |
| [Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui) | Separation of vocals/instruments and stems | Explore; only use recordings you may process |

**Voice processing order:** retain untouched source WAV → remove obvious hum/noise → edit clicks/pauses → gentle EQ/de-essing/compression → check intelligibility/peaks/loudness → export final audio. Do not overprocess a teacher's voice. Commercial [Adobe Podcast Enhance Speech](https://podcast.adobe.com/en/enhance) is a hosted service, not an open-source Adobe GitHub repo. Confirm current quotas, data terms and cost before uploading student/guest recordings.

### 5. Captions, transcript editing and multilingual speech

| Repository | Purpose | Priority |
|---|---|---|
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Local transcription on Apple Silicon | **Now**; fork already present |
| [OpenAI Whisper](https://github.com/openai/whisper) | Original speech recognition project | Reference |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Alternate optimized Whisper implementation | Explore |
| [WhisperX](https://github.com/m-bain/whisperX) | Word alignment and diarization pipelines | Explore; check hardware |
| [OpenChatCut](https://github.com/0xsline/OpenChatCut) | Transcript-driven editing/AI video workflow | Explore; check AGPL and current functionality |

Manually review timing, Telugu/English code-switching, mathematics symbols, technical terminology, and any personal names. Prefer native captions (SRT/VTT) and keep original audio.

### 6. Thumbnails, images, subject cutouts and graphics

| Repository | Purpose | Priority |
|---|---|---|
| [Krita](https://github.com/KDE/krita) | Draw, composite and paint attention-grabbing thumbnails | **Now** |
| [rembg](https://github.com/danielgatis/rembg) | Remove backgrounds/prepare presenter cutouts | **Now** |
| [ImageMagick](https://github.com/ImageMagick/ImageMagick) | Batch resize, crop, composite and export images | **Now** |
| [Sharp](https://github.com/lovell/sharp) | Node image-processing service for automated thumbnail templates | Explore |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | AI illustration/background generation for graphics | Heavy |

Practical thumbnail method: choose the accurate lesson concept → original title/text → clear visual focus → hand-drawn or teacher-authored asset → high-contrast safe text → export 16:9. Maintain a consistent channel brand. For thumbnails, Adobe Photoshop and Adobe Express are commercial products, not repos to fork.

### 7. Lower thirds, motion graphics, titles, openers

| Repository | Purpose | Priority |
|---|---|---|
| [Remotion](https://github.com/remotion-dev/remotion) | Programmatic branded lower thirds, chapter cards, captions | **Now**, license review |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | TypeScript timeline animations and technical explainers | **Now** |
| [Revideo](https://github.com/midrender/revideo) | Code-first video and animated compositions | Explore |
| [Lottie-web](https://github.com/airbnb/lottie-web) | Play vector animations exported from After Effects | Explore |
| [Snapcn](https://github.com/shadcn-labs/snapcn) | Ready-to-adapt Remotion-style animation components | Explore; check source |

Also see [motion-skills](https://github.com/iart-ai/motion-skills), a **third-party** animation skills collection. Review any agent skill's instructions before enabling automation.

### 8. Advanced VFX, color and postproduction

| Repository | Purpose | Priority |
|---|---|---|
| [Blender](https://github.com/blender/blender) | Compositing, tracking and procedural effects | **Now** |
| [Segment Anything 2](https://github.com/facebookresearch/sam2) | Object/video masks for VFX pipelines | Heavy/experimental |
| [ProPainter](https://github.com/sczhou/ProPainter) | Video inpainting/object removal research | Heavy/experimental |
| [Upscayl](https://github.com/upscayl/upscayl) | Upscale still images; not a full video editor | Explore |
| [OpenColorIO](https://github.com/AcademySoftwareFoundation/OpenColorIO) | Consistent color-space pipeline for compatible apps | Later; not one-click grading |

## Adobe: actual public repositories vs commercial apps

| Official Adobe GitHub repository | What it actually provides |
|---|---|
| [Premiere Pro UXP samples](https://github.com/AdobeDocs/uxp-premiere-pro-samples) | Example source code for **developing** Premiere Pro plugins; requires compatible Premiere Pro |
| [Photoshop UXP plugin samples](https://github.com/AdobeDocs/uxp-photoshop-plugin-samples) | Example plugin projects and API patterns for Photoshop |
| [Adobe Research EditVerse](https://github.com/adobe-research/EditVerse) | Research benchmark/evaluation code; **not** a ready-made consumer video editor or plugin |

Commercial [Adobe Podcast](https://podcast.adobe.com/), [Adobe Express](https://www.adobe.com/express/), Premiere Pro, Photoshop, After Effects and Firefly are separate apps/services. They are not automatically installable from these GitHub repositories. Read licensing and paid-use rules before automation.

## Two practical production workflows

### A. Aptitude Mind Plus and classroom videos (lightweight now)

1. Record iPad handwriting and voice with separate untouched originals if possible.
2. Use Auto-Editor for **reviewable** rough cuts or LosslessCut for fast trims; avoid deleting explanatory pauses.
3. Clean dialogue in Audacity; compare DeepFilterNet/RNNoise only when background noise warrants it.
4. Draft SRT/VTT using whisper.cpp; correct Telugu, English, mathematical notation and sync.
5. Render standard intro, lower third and summary cards from Remotion or Motion Canvas templates.
6. Finish in your current video editor; use FFmpeg only for repeatable media conversion.
7. Make thumbnail in Krita/Photoshop/Canva, optionally rembg cutouts; check readable phone-size preview.
8. Review final loudness, caption timing, 16:9/9:16 crops, upload metadata and rights before publishing.

### B. 3D and cinematic shots (advanced later)

1. Storyboard and plan an original shot.
2. Model in Blender or generate draft 3D geometry via a hosted 3D service/cloud GPU if licensed.
3. Cleanup topology, materials and rigging in Blender. Export manageable render passes.
4. Generate optional AI background/VFX shots using ComfyUI/Wan/LTX through appropriately provisioned GPU.
5. Composite, color-manage and sound-design; export short low-res tests before full final render.

## Apple M1 / 8 GB readiness

- **Suitable to evaluate now:** FFmpeg, LosslessCut, Audacity, whisper.cpp with small multilingual model, Auto-Editor, ImageMagick, Krita, carefully sized Blender scenes, and short Motion Canvas/Remotion renders.
- **Test individually:** DeepFilterNet, rembg, CommandPost and new plugins; check OS/editor release compatibility and disk space first.
- **Keep as references for stronger hardware or cloud:** TRELLIS.2, Hunyuan3D, Wan2.2, LTX-2, Open-Sora, DiffSynth-Studio, SAM2/ProPainter and large ComfyUI pipelines. Do not install them all or claim they will run locally on 8 GB.

## Bookmarking this selection in your GitHub account

The focused [filmmaking-stars.txt](filmmaking-stars.txt) includes the repositories added in this supplement, plus already-listed essential tools. To preview it on **your own authenticated Mac** after cloning this toolkit:

```bash
python3 scripts/star_github_resources.py --file docs/filmmaking-stars.txt
```

After reviewing the exact list, the explicit `--apply` flag bookmarks them using the GitHub CLI session authenticated as your own account:

```bash
python3 scripts/star_github_resources.py --file docs/filmmaking-stars.txt --apply
```

No automatic stars, forks, installation, API subscription, remote execution, editor configuration, downloads or license grants are implied by this GitHub document. Never publish third-party work/voice without permission or expose credentials.
