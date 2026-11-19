# ai-video-prompts v3.5.0-beta2 (English release)

Director-level design translated into self-contained, camera-recordable AI video prompts. Story facts remain the user's; sensory detail is enriched within those facts. Extended is the default; the user can request a shorter tier.

## Entry and routing

Start with `SKILL.md`, then the relevant sections of its routed files. Context selects action mode, dialogue situation, performance and camera behavior. Run design before Lens translation; keep analysis and production tables outside final prose.

- Fights: `references/spatial-tactics.md` supplies space checks and expanded arena/position design for complex scenes, before exchanges and camera coverage.
- Dialogue and silent interaction: `dialogue/spatial-blocking.md` supplies required spatial choices and counterpart responses. Motivated stillness is valid; fight displacement thresholds do not apply.
- Expanded production records: `references/template-contract.md` and its linked template are optional; required spatial/contact/seam checks still apply.
- Request capacity and audio execution: `references/generation-handoff.md` is the shared definition. Rhythm examples are not model limits. Dialogue is inline by default; unknown audio/lip-sync capability is labeled outside the copy block.
- Model evidence classes, dated interface records and evaluation procedures: `models/` and `evals/cases.md`. Text checks are not dynamic generation evidence; no auditable original generation sample is bundled.

## First use

Extract the ZIP and open a terminal inside its `ai-video-prompts` folder. With Python 3.9+ available, these commands use only bundled files and the standard library:

```text
python -X utf8 -B scripts/check_skill.py .
python -X utf8 -B scripts/read_route.py --list
python -X utf8 -B scripts/lint_prompt.py examples/first-prompt.txt --lang en --tier standard --seconds 5 --scene-type action
```

Expect the structure check to print `OK`, the route list to include `action`, and lint to report a nonzero English word count and `0 error(s)`. The bundled sample is deliberately one stationary parry, not a template for every fight. Length ranges are advisory; `BELOW` or `ABOVE` asks for review, not padding or automatic cuts. Exit 0 means no text-pattern errors, not a validated video.

To create your own prompt, ask the assistant to use this skill with your scene, locked facts and desired pace/camera/performance. It reads the relevant route, designs the scene and delivers copyable prose. Save that prose as `prompt.txt`; for a mixed action/dialogue scene it can read `python -X utf8 -B scripts/read_route.py action dialogue`. No route output is a finished prompt. Without Python, the assistant can read the exact files/headings in [routes](assets/routes.json) manually; automatic checks are then unavailable.

## Tools

```text
python scripts/check_skill.py .
python scripts/lint_prompt.py prompt.txt --lang auto --seconds 20 --scene-type dialogue
python scripts/lint_prompt.py prompt.txt --lang auto --seconds 30 --scene-type action
python scripts/check_spatial.py ledger.json
python scripts/analyze_clip.py clip.mp4 --json metrics.json --sheet contact.png
python scripts/draw_inspiration.py --dimension action
```

`check_skill.py` checks links, routing, stale gates and runtime debris. `lint_prompt.py` checks text patterns and scene-specific length guidance; a clean result does not certify acting or blocking. `check_spatial.py` validates design data and reports per-character changes; only explicit project requirements create target failures. `analyze_clip.py` needs FFmpeg/FFprobe and measures cuts and pixel motion, including camera motion; inspect actual frames and listen separately. Inspiration history belongs in project work, not this skill.

The first-use commands run as written. In this larger tool list, `prompt.txt`, `ledger.json` and `clip.mp4` are your own project inputs, not missing package files. For mixed-language text, `--lang auto` is a heuristic; use `--lang en` or `--lang zh` when you intend one counting convention.

For setup, copyable commands, output fields and troubleshooting, read the [video analyzer usage guide](scripts/analyze_clip.md).

## Package boundaries

The active package contains current instructions, useful templates, scripts and routed examples. Legacy patch reports and v1 examples are archived outside the installed runtime. Git metadata remains in the local repository but is excluded from portable ZIPs. Preserve `LICENSE` when copying the package.

The [inspiration compatibility data](assets/inspiration-compatibility.json) is a runtime dependency: it maps legacy draw histories and localized aliases to the English card library. It is not development output. Source prose, templates and filenames in this release are English; escaped multilingual matching data preserves non-English input support.

Extended means relevant richness with no minimum length. Necessary checks survive Compact delivery. Lint supports `--format platform` for verified structured syntax and optional `--density-diagnostic`. No text checker replaces target coverage review.

## Product candidate entry points

Use [loading](core/loading.md) and [routes](assets/routes.json) for exact-section reading, [ownership](core/ownership.md) for rule maintenance, [records](core/records.md) for optional forms, and [capabilities](models/capabilities.md) for dated evidence. Run `python scripts/read_route.py --list`, `python scripts/read_route.py action dialogue --stats`, or omit `--stats` to read source sections. Expanded references remain available in the [index](core/reference-index.md).

This is an engineering beta retaining v3.4.0 as the creative baseline and superseding v3.5.0-rc1's engineering draft. It is available for supervised trials; generated-video non-regression and broad production suitability remain unestablished. Package hashes, issue disposition, diffs and actual test artifacts are delivered separately from runtime instructions.

Runtime tools require Python 3.9+. Run the portable regression suite with `python -B tests/regression.py`. Video analysis additionally needs FFmpeg/FFprobe. No API keys or paid generation are needed for these static/text checks.
