---
name: ai-video-prompts
description: Director-level design plus cinematic prompt writing for AI video models (Sora, Veo, Kling, Seedance/Jimeng, Runway, Hailuo, Wan, etc.). Use for any request to write, design, upgrade, or storyboard AI video prompts - action and fight choreography, dialogue and power-dynamic scenes, character performance and micro-expressions, multi-clip continuity, or turning a script into generation-ready text. Delivers vivid, camera-recordable Extended prompts by default.
---

# AI Video Prompts v3.5.0-beta2

Deep director-level thinking stays **internal**. What leaves the skill is **pure cinematic execution**: one vivid, physical, camera-recordable prompt per clip, with real optics, light, skin, face, body, and speech.

## The pipeline: three rooms

1. **Director's Room (design).** Use the depth needed to resolve this scene: choices and contact causality, the four-layer dialogue engine, psychological action, status and power, continuity seams. **First build the Context Profile and route** (`core/context-routing.md`): purpose, power, body state, space, audience, relationship, tools, tone, stakes. The profile picks the action mode, the situation profile, the display rules, the camera stance, and the look. Output is an internal design record. It never appears in the prompt. See `core/pipeline.md`.
2. **Lens (translation).** Convert the design into statements a camera could record, then select relevant detail from five dimensions: optics, physical light, skin and material, face, body and status. See `lens/lens-layer.md`.
3. **Prompt (output).** Write the **Extended** prompt by default (`lens/output-skeletons.md`), lint it (`scripts/lint_prompt.py`), deliver it. Notes sit outside the copy block.

## Defaults (change only when the user asks)

- **Depth: on.** Every depth system the scene calls for is used. There is no opt-in ladder. A request for "short", "lite", "quick", or a concise version changes delivery length. Story coverage, causality, motivated performance and continuity remain checked at every length; optional exploration may be shorter.
- **Length: Extended.** Extended means richly developed relevant content, not a minimum word count or a requirement to fill every slot. Select detail by dramatic priority, shot size and actual inputs. Stop when the scene is complete. If the model's limit is lower, fit the largest version that fits and say so in one line.
- **Dialogue: spoken, inline.** Lines go into the prompt as quoted speech with delivery cues. See `dialogue/`.
- **Language:** the prompt is written in the language best supported by the target model; if unknown, the user's language. Design notes use the user's language.

## Rules that do not bend

1. **Do not invent the story.** Plot, outcome, who wins, who knows what, character identity and established look, plot-bearing objects, injuries, world rules, and any move, line, or face target the user named are **locked**. If a gap would change them, ask once; if the user delegates ("you decide"), decide inside that scope only.
2. **Texture is yours to enrich.** Anything that changes how a moment looks, sounds, or feels without changing what happens is **open**: lens, grain, light, skin, hair, fabric, breath, posture, prop business with ordinary setting props, ambient motion, speech rhythm. Add it generously. Note notable additions in one line outside the copy block so the user can veto. See `core/pipeline.md` for the full locked/open/gray split.
3. **Depict, never specify.** Every sentence in the prompt describes something a camera or microphone would capture. Prefer direct depiction over analytical scaffolding. Preserve quoted speech, meaningful ordinary words and verified platform syntax; linguistic patterns are review cues, not universal bans. See `lens/lens-layer.md`.
4. **Contact before consequence.** A body reacts to a force only after something delivers it. Support, contact, and result are traceable. Fix choreography before adding light, shake, or particles.
5. **Every clip hands over its end state** (position and facing, support and posture, held objects, injury and stamina, ability state, environment state), and the next clip opens from it.
6. **Say what is verified and what is assumed.** A platform feature is "supported" only if the user confirmed it or you checked current official docs. A prompt is "tested" only if a clip was generated. Never promise results.
7. **Protect explicit user targets.** Resolve unspecified staging within authorization. If a real conflict requires changing a locked detail, offer concrete options and wait for that choice; never silently downgrade.
8. **Route by context.** There is no default scene. A fight is a duel, a last stand, a stealth takedown, a sparring match, or another mode; a conversation is a seated exchange, a street argument, a farewell, or another situation. Build the Context Profile first; never copy an example's posture, rhythm, or ending into a scene whose profile differs.
9. **Space is three-dimensional.** Every fight checks usable space, support, facing and paths. A simple exchange may use a concise spatial record; complex crossings, groups and multi-clip choreography use an arena card and position ledger. Select travel, level changes, holds and camera axes for the actual goal, without universal movement quotas (`references/spatial-tactics.md`).

10. **Dialogue needs spatial decisions.** Before gesture and coverage, plan each conversation unit's starting geometry, motivated movement or deliberate hold, the other person's response, and the resulting geometry. Apply [dialogue spatial blocking](dialogue/spatial-blocking.md), including silent interaction. Deliberate stillness is valid; displacement, height and camera quotas from fights do not apply to dialogue.

## Budgets: three tiers, not one count

| Tier | Covers | Rule |
|---|---|---|
| A: story and contact | Attack/defense/transfer events, outcomes, ability use | Strict causal and capacity check: the action mode suggests rhythm; timing, contact complexity, assets and verified model behavior determine request capacity. Use `references/generation-handoff.md` section 3; counts are planning estimates, not universal quotas |
| B: performance and body | Gaze, face, posture, hands, prop business, listening, speech delivery | Motivated and generous where useful; limited by visibility, runtime and shared attention |
| C: texture | Optics, light, skin, fabric, atmosphere, micro-motion, sound bed | No fixed count; limited by relevance, visibility, shared attention, coherence and actual prompt limits |

Details and coherence rules: `core/pipeline.md`.

## Precedence (the only ladder)

When rules conflict, the higher one wins. No other file claims priority; `scripts/check_skill.py` fails if one does.

1. Safety, legal, platform policy
2. The user's explicit decisions and locked story facts
3. Physical and causal integrity of Tier A within the declared world's mechanics
4. Continuity of identity and state
5. Lens validity (depiction grammar, coherence)
6. Performance and dialogue depth (Tier B)
7. Texture and style (Tier C)

When details compete, protect locked targets and causal readability. Re-stage useful performance if feasible; omit secondary detail that distracts or cannot fit. Richness serves the scene.

Apply [conflict resolution](core/precedence.md): resolve unspecified staging directly; seek a choice when the solution changes a locked detail. An explicit supernatural premise permits flight or hovering; do not invent extra powers or impose realism against the user's world rules.

## Load by the work to be done

Read [loading](core/loading.md), then the primary route in [routes](assets/routes.json). Use `python scripts/read_route.py action` (or dialogue, visual, ideation, review); combine routes for genuinely mixed scenes. The tool returns exact source sections without rewriting them. Without Python, read the manifest's files and headings manually. References inside a selected section are expansion links, not recursive read-all commands; resolve mandatory dependencies through the loading protocol.

Before writing, capture the user's quality targets: intended intensity, camera ambition, performance subtlety, visual richness and continuity. These are delivery obligations, not dispensable ornament. See [pipeline quality preservation](core/pipeline.md#8-quality-preservation). Rich action must not quietly become one cautious exchange; an intimate hold must not become decorative activity. Output brevity never removes necessary design.

Expand when a declared target remains undesigned, an input is missing, a physical/expressive conflict remains, or the current draft is generic. Use the [reference index](core/reference-index.md) to choose the relevant source, then return to writing. Do not stop reading because of a file quota; do not open every library merely because it shares a keyword.

Use [record selection](core/records.md) for optional project cards, [ownership](core/ownership.md) when maintaining rules, and [model evidence](models/capabilities.md) for dated platform facts. Final semantic coverage is checked in the route before text lint. Rich craft remains available through every original reference.

## Honesty about this skill

This engineering beta retains v3.4.0 as its creative baseline. It encodes design principles and a vocabulary, with no auditable original model-generation sample bundled. Structural checks and finite text trials do not establish video-quality non-regression or suitability for broad production. Optics, light, face and speech vocabulary remains a rendering hypothesis until tested under recorded conditions; `evals/cases.md` explains matched comparisons. Useful craft does not depend on unsupported historical clip claims.
