# Migration: v1 to v3.0

v3 is a fork of v1, not a rewrite. The depth systems you valued stay. What changed is **where depth is spent** and **how it is turned into text**.

## Diagnosis recap (from the review)

v1 used one conservative gate for two different things. Story facts needed protection; sensory texture needed freedom. v1 put both behind "3+2" (65 mentions in 38 files), 187 prohibitions, opt-in depth ("lean不加载 / 仅full"), and a rule against model-native cinematography vocabulary. All four symptoms (director's-note prose, plastic look, wooden actors, fake dialogue) came from that.

## What changed

| Symptom | Cause in v1 | v3 fix |
|---|---|---|
| Reads like a director's note | Prompt derived from an engineering form; constraints rewritten as conditionals ("only after..."); no translation spec | `lens/lens-layer.md` depiction grammar; prompt-first; `scripts/lint_prompt.py` |
| Plastic look | No optics, skin, or physical-light layer; lens and halation barely mentioned; cinematography terms discouraged | Passes 1–3: `optics-and-stock`, `physical-light`, `skin-and-material` |
| No muscle-level faces | One-signal cap; matrix pessimistic | Pass 4 `face-pass.md` (FACS-informed lexicon, masking, fallbacks) |
| Wooden actors | One life-action per scene; ambient cap of 2; no status or prop-business system | Pass 5 `body-and-status.md`: Status & Proxemics, listener acting, prop business, dyad templates |
| Fake dialogue | Lines routed to notes by default; ten-character trim target; aphoristic cards; one line per 5 s event | `dialogue/spoken-register.md`, `dialogue/conversation-units.md`, inline quoted lines by default |
| Thin default output | Depth opt-in; Compact-like by default | Depth on by default; **Extended** is the default tier |

## Rules replaced

| v1 | v3 |
|---|---|
| "3+2" must-do/ambient/guard budget as law with three exemptions | **Tiers:** A story and contact (about 3 independent interactions per ~5 s), B performance (generous), C texture (coherence only) |
| Locked and unlocked treated alike | **Texture Authority**: locked story facts, open sensory texture, gray cases with a one-line added-texture note |
| Several files claiming supremacy | One precedence ladder in `SKILL.md`; `check_skill.py` fails on any other authority claim |
| Depth behind consent phrases | Depth default on; "short/lite/简版" lowers it |
| Dialogue to production notes | Lines inline with delivery cues; voice script as a second output |

## What was kept (the depth systems)

Choreography and force/support/contact, hit chain and hit-context derivation, state-seam ledger, the four-layer dialogue engine with subtext axes, texture engines, language DNA, the 14 dialogue cards, psychological action, micro-signal matrix and leak formula, character and costume design, consistency, camera and rhythm, powers and VFX, world and style, inspiration wizard and library, cultural research, the Buliangren style study. Where they referred to the 3+2 budget, gating, or supreme authority, the references were patched to the tier model. Their original Chinese text is retained.

## What was merged or removed

- **Merged stubs:** narrative (9 files) → `narrative/story-and-scene.md`; production (8) → `production/workflow.md`; post, distribution, management (13) → `post/finishing-and-release.md`; quality (3) → `quality/quality.md`; sound (2) → `sound/sound-and-voice.md`; style cards (10) → `visual/style-library.md`; ux (7) → `ux/interaction.md`. Camera subjective notes moved into `references/camera-and-rhythm.md`.
- **Removed:** core load-graph, task-router, module-contract, precedence-rules (replaced by `core/pipeline.md`, `core/precedence.md`, and the ladder); `anti-lazy-and-delivery.md` (replaced by `references/delivery-and-qa.md`); `visual/lighting.md` (absorbed into `lens/physical-light.md`); `production/prompt-engineering.md` (replaced by the Lens layer); the generation input template and `export_prompt.py` (prompt-first replaces the form-first workflow); `validate_modules.py` (replaced by `check_skill.py`, which also catches competing authorities and leftover v1 gates); dead `depends_on` metadata.
- **Archived:** v1 worked examples at `examples/legacy-v1/`. They use the old FIXED/EVENT/SEAM design surface and are design-side illustrations only.

## Decisions you made that I implemented as asked

- **Extended is the default for every prompt.** It targets about 320–520 English words (about 650–1000 Chinese characters) per clip, up to the model's limit. This is your call; the risk is that some models truncate, dilute, or contradict themselves on long prompts. `evals/cases.md` case 10 (the length ladder) tests it per model, and `models/` records the result.
- **Dialogue is inline by default**, which means some prompts will include speech the model cannot voice. Lip sync is untested everywhere until you test it.

## Honest caveats

- **Nothing here has been run on a video model.** The cinematography, face, and speech vocabulary is marked "confirm per model". The belief that models respond to cinematography terms is reasonable but unverified.
- **More vocabulary can backfire.** Stacked jargon makes models contradict themselves. That is why coherence rules and the linter exist.
- **I could not verify the newest models** (Seedance 2.5, current Sora, etc.). The model layer is a method, not a database.
- **The patches to v1 files were surgical.** I replaced budget and gating sentences and kept the rest. Run `python scripts/check_skill.py .` to find any leftover gate I missed; it fails on the 3+2 law, "lean不加载", "仅full", and the ten-character cap.
- **Language mix.** v1's deep files are Chinese; the new layers are English with Chinese lexicon columns. The model reading them handles both; if you prefer one language, translate the new layers.
- **v2 failed in your test.** v3 deliberately keeps v1's depth and changes the allocation. Treat each layer as a hypothesis until your A/B says otherwise.
