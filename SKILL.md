---
name: ai-video-prompts
description: Director-level design plus cinematic prompt writing for AI video models (Sora, Veo, Kling, Seedance/Jimeng, Runway, Hailuo, Wan, etc.). Use for any request to write, design, upgrade, or storyboard AI video prompts - action and fight choreography, dialogue and power-dynamic scenes, character performance and micro-expressions, multi-clip continuity, or turning a script into generation-ready text. Delivers vivid, camera-recordable Extended prompts by default. 触发词：视频提示词、分镜、打戏、台词、潜台词、微表情、肢体语言、质感、剧本转提示词。
---

# AI Video Prompts v3

Deep director-level thinking stays **internal**. What leaves the skill is **pure cinematic execution**: one vivid, physical, camera-recordable prompt per clip, with real optics, light, skin, face, body, and speech.

## The pipeline: three rooms

1. **Director's Room (design).** Run the deep systems at full depth: choices and contact causality, the four-layer dialogue engine, psychological action, status and power, continuity seams. **First build the Context Profile and route** (`core/context-routing.md`): purpose, power, body state, space, audience, relationship, tools, tone, stakes. The profile picks the action mode, the situation profile, the display rules, the camera stance, and the look. Output is an internal design record. It never appears in the prompt. See `core/pipeline.md`.
2. **Lens (translation).** Convert the design into statements a camera could record, then enrich with five passes: optics, physical light, skin and material, face, body and status. See `lens/lens-layer.md`.
3. **Prompt (output).** Write the **Extended** prompt by default (`lens/output-skeletons.md`), lint it (`scripts/lint_prompt.py`), deliver it. Notes sit outside the copy block.

## Defaults (change only when the user asks)

- **Depth: on.** Every depth system the scene calls for is used. There is no opt-in ladder. "short", "lite", "quick", "简版" lowers depth and length to the Compact tier.
- **Length: Extended.** Fill every slot of the skeleton at full richness, up to the target model's prompt limit. If the model's limit is lower, fit the largest version that fits and say so in one line.
- **Dialogue: spoken, inline.** Lines go into the prompt as quoted speech with delivery cues. See `dialogue/`.
- **Language:** the prompt is written in the language best supported by the target model; if unknown, the user's language. Design notes use the user's language.

## Rules that do not bend

1. **Do not invent the story.** Plot, outcome, who wins, who knows what, character identity and established look, plot-bearing objects, injuries, world rules, and any move, line, or face target the user named are **locked**. If a gap would change them, ask once; if the user delegates ("you decide"), decide inside that scope only.
2. **Texture is yours to enrich.** Anything that changes how a moment looks, sounds, or feels without changing what happens is **open**: lens, grain, light, skin, hair, fabric, breath, posture, prop business with ordinary setting props, ambient motion, speech rhythm. Add it generously. Note notable additions in one line outside the copy block so the user can veto. See `core/pipeline.md` for the full locked/open/gray split.
3. **Depict, never specify.** Every sentence in the prompt describes something a camera or microphone would capture. No conditionals, no negations, no explanation, no theory words, no production labels. See `lens/lens-layer.md`.
4. **Contact before consequence.** A body reacts to a force only after something delivers it. Support, contact, and result are traceable. Fix choreography before adding light, shake, or particles.
5. **Every clip hands over its end state** (position and facing, support and posture, held objects, injury and stamina, ability state, environment state), and the next clip opens from it.
6. **Say what is verified and what is assumed.** A platform feature is "supported" only if the user confirmed it or you checked current official docs. A prompt is "tested" only if a clip was generated. Never promise results.
7. **Protect explicit user targets.** If one competes with something else, offer options and wait; never silently downgrade.
8. **Route by context.** There is no default scene. A fight is a duel, a last stand, a stealth takedown, a sparring match, or another mode; a conversation is a seated exchange, a street argument, a farewell, or another situation. Build the Context Profile first; never copy an example's posture, rhythm, or ending into a scene whose profile differs.
9. **Space is three-dimensional.** Every fight starts with an arena card and a position ledger (x, y, z, facing, anchor per beat). Fighters traverse the arena, answer attacks with displacement (off-line, arc, pass, level change, push-off, terrain funnel), and change anchors. A fight confined to one line is a defect unless the mode calls for it (`references/spatial-tactics.md`).

## Budgets: three tiers, not one count

| Tier | Covers | Rule |
|---|---|---|
| A: story and contact | Attack/defense/transfer events, outcomes, ability use | Strict, and **mode-dependent**: density comes from the action mode (`references/action-modes.md`). A duel may run 1–3 interactions per ~5 s, a last stand 2–4 overlapping, a stealth takedown 0–1 per clip. Split clips beyond the mode's density |
| B: performance and body | Gaze, face, posture, hands, prop business, listening, speech delivery | Generous, written beat by beat; limited by readability, not by count |
| C: texture | Optics, light, skin, fabric, atmosphere, micro-motion, sound bed | No count; limited only by coherence and the model's prompt length |

Details and coherence rules: `core/pipeline.md`.

## Precedence (the only ladder)

When rules conflict, the higher one wins. No other file claims priority; `scripts/check_skill.py` fails if one does.

1. Safety, legal, platform policy
2. The user's explicit decisions and locked story facts
3. Physical and causal integrity of Tier A
4. Continuity of identity and state
5. Lens validity (depiction grammar, coherence)
6. Performance and dialogue depth (Tier B)
7. Texture and style (Tier C)

When Tier A and a richer Tier B or C detail collide, **re-stage** (move the gesture to a free limb or a later moment) rather than delete richness.

## What to read

Read the files whose trigger appears. For an Extended prompt, the Lens files are always read.

| Task has... | Read |
|---|---|
| Any prompt output (always) | `core/pipeline.md`, `core/context-routing.md`, `lens/lens-layer.md`, `lens/output-skeletons.md` |
| Extended (default): the five passes | `lens/optics-and-stock.md`, `lens/physical-light.md`, `lens/skin-and-material.md`, `lens/face-pass.md`, `lens/body-and-status.md` |
| Any spoken line, monologue, negotiation, confrontation | `dialogue/situation-profiles.md`, `dialogue/spoken-register.md`, `dialogue/conversation-units.md`, then `references/dialogue-engine.md` (cards: `references/dialogue-reference-cards.md`) |
| Fight, chase, weapons, multi-clip action | `references/action-modes.md`, `references/spatial-tactics.md`, `references/choreography.md`, `references/hit-feel.md`, `references/action-reference-system.md`, `references/consistency.md` |
| An emotional or psychological beat, close-up, concealment | `references/performance-and-psychology.md`, `references/character-and-performance.md` |
| Camera, rhythm, composition, color | `references/camera-and-rhythm.md`, `visual/composition-and-color.md` |
| Setting, props, environment, weather | `references/world-and-style.md`, `visual/environment-interaction.md`, `narrative/story-and-scene.md` |
| Powers, VFX | `references/powers-and-vfx.md` |
| A style or reference | `visual/style-translation.md`, `visual/style-library.md` |
| Sound or voice | `sound/sound-and-voice.md`, `references/hit-feel.md` |
| Splitting into clips, continuity, platform | `references/prompts-and-segments.md`, `references/generation-handoff.md`, `models/README.md` |
| Final check, delivery | `references/delivery-and-qa.md` |
| Story ideation from nothing | `references/inspiration-wizard.md`, `references/inspiration-library.md` |
| Real periods, objects, sources; compliance | `references/cultural-research.md`, `references/source-scope.md`, `references/framing-and-compliance.md` |
| Planning and tooling a full pipeline | `references/ai-pipeline.md`, `references/template-contract.md` (optional ledgers), `references/delivery-and-example.md` (v1 design example) |
| Workflow, planning, post, release | `production/workflow.md`, `post/finishing-and-release.md`, `quality/quality.md` |
| Tone and interaction rules | `ux/interaction.md` |

## Honesty about this skill

v3 encodes design principles and a vocabulary. It has not been benchmarked against any specific model, and the optics, light, face, and speech vocabulary is flagged "confirm per model" until you test it. `evals/cases.md` is how to find out what works on yours.
