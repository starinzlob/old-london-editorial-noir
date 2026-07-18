# Old London Editorial Noir

An installable Codex Skill for creating images and videos in a restrained interwar British private-press style: old London, editorial film noir, visible halftone, letterpress ink, raw newsprint, fog, rain, gaslight, and modern readability.

Created by [@starinzlob](https://github.com/starinzlob).

![1932 London railway platform rendered as an editorial-noir video style frame](examples/02-railway-styleframe.png)

## What it does

- Directs still images, image edits, posters, covers, advertisements, logos, and keyframes.
- Directs storyboards, motion graphics, collage B-roll, title sequences, finished videos, and bilingual subtitles.
- Converts the style into a concrete production contract: story, hierarchy, material, palette, light, type, motion, and drift guards.
- Includes separate image and video workflows plus a deterministic prompt preflight script.
- Rejects common drift into generic sepia vintage, cyberpunk, glossy 3D, steampunk clutter, or propaganda-emblem aesthetics.

## Install

Use the Codex Skill Installer:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo starinzlob/old-london-editorial-noir \
  --path skills/old-london-editorial-noir
```

The Skill will be available on the next Codex turn.

Manual installation:

```bash
git clone https://github.com/starinzlob/old-london-editorial-noir.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R old-london-editorial-noir/skills/old-london-editorial-noir \
  "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Use

Invoke it explicitly:

```text
Use $old-london-editorial-noir to turn this script into a restrained
15-second editorial-noir video with Chinese and English subtitles.
```

Or ask naturally:

```text
Create a 4:5 poster in our core Old London newspaper style.
```

The Skill can also trigger from requests for interwar London, British newspaper illustration, editorial film noir, halftone newsprint, letterpress, engraving, fog, rain, or gaslight.

## Examples

| Lead image | Video style frame | Commercial illustration |
| --- | --- | --- |
| ![A woman with an umbrella on a rain-dark London street](examples/01-gaslight-street.png) | ![A porter and steam train beneath a London station roof](examples/02-railway-styleframe.png) | ![A 1930s typewriter rendered as a newspaper advertisement](examples/03-typewriter-advert.png) |
| Portrait 4:5 | Landscape 16:9 | Square 1:1 |

The example images were generated with OpenAI image generation using art direction produced from this Skill. Exact copy is intentionally excluded from generated pixels; production typography should remain editable.

## Structure

```text
skills/old-london-editorial-noir/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── canon.md
│   ├── image-workflow.md
│   └── video-workflow.md
└── scripts/check_style_brief.py
```

Run a written prompt through the optional preflight:

```bash
python3 skills/old-london-editorial-noir/scripts/check_style_brief.py \
  path/to/prompt.txt --target image
```

Use `--target video` to add motion and temporal-stability checks. The script is a review aid; approval still requires inspecting the actual visual output.

## License

MIT
