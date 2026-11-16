# Creator & STEM Toolkit

A practical open-source reference shelf for **Venkata Krishna's teaching, educational videos, filmmaking, AI experiments, and robotics**.

[Full directory: 113 projects](docs/github-resource-library.md) · [Import list](docs/github-stars.txt) · [GitHub Stars](https://github.com/VenkataKrishnaYalagala?tab=stars)

## Start with a project

| Goal | First tools to consider | Useful output |
| --- | --- | --- |
| Explain a mathematics concept | [Manim](https://github.com/ManimCommunity/manim), [SymPy](https://github.com/sympy/sympy), [Matplotlib](https://github.com/matplotlib/matplotlib) | Short animation, checked examples, and lesson plots |
| Produce an educational video | [OBS Studio](https://github.com/obsproject/obs-studio), [FFmpeg](https://github.com/FFmpeg/FFmpeg), [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Recording, converted clips, and draft subtitles |
| Create 3D and VFX shots | [Blender](https://github.com/blender/blender) | Storyboard tests, models, animation, and compositing |
| Extend the learning website | [KaTeX](https://github.com/KaTeX/KaTeX), [Playwright](https://github.com/microsoft/playwright), [Puck](https://github.com/puckeditor/puck) | Formula rendering, tested pages, and visual editing experiments |
| Build an Arduino demonstration | [Arduino CLI](https://github.com/arduino/arduino-cli), [PlatformIO](https://github.com/platformio/platformio-core), [ESP32 Arduino](https://github.com/espressif/arduino-esp32) | Reproducible firmware and sensor experiments |
| Explore reusable agent skills | [OpenAI Skills](https://github.com/openai/skills), [Anthropic Skills](https://github.com/anthropics/skills), [Agent Skills](https://github.com/agentskills/agentskills) | Reviewed instructions for a specific task |
| Experiment with local AI | [Ollama](https://github.com/ollama/ollama), [llama.cpp](https://github.com/ggml-org/llama.cpp) | Small-model experiments suited to available memory |

## Using this collection

1. Choose one output you want to make.
2. Open the upstream project's official README and check its requirements and license.
3. Bookmark it with a GitHub Star; fork it when you need to modify its source.
4. Keep your own lesson, film, or firmware source in a separate original project repository.

These are references, not installed dependencies. Start small on an M1 Mac with 8 GB RAM; large AI video models and simulation stacks need separate evaluation.

## Full directory

The [categorized catalog](docs/github-resource-library.md) covers skills and MCP, coding tools, film and audio, mathematics, websites, learning platforms, local AI, robotics, automation, and development quality. Its last upstream availability check was **15 November 2026**; review current requirements before adopting a tool.

## Optional bulk bookmarking

Requires Python 3 and an authenticated GitHub CLI. Preview first:

```bash
git clone https://github.com/VenkataKrishnaYalagala/creator-stem-toolkit.git
cd creator-stem-toolkit
python3 scripts/star_github_resources.py
```

To add the complete catalog to the authenticated account's Stars:

```bash
python3 scripts/star_github_resources.py --apply
```

The helper changes bookmarks only; it does not install tools or enable external services.

## Related projects

- [Aptitude Mind Plus](https://github.com/VenkataKrishnaYalagala/aptitude-mind-plus): website and learning resources.
- [AMP Daily](https://github.com/VenkataKrishnaYalagala/aptitude-mind-plus-daily): educational cards and publishing workflow.
- [Venkata Krishna](https://github.com/VenkataKrishnaYalagala): profile and featured work.
