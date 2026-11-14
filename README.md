# ai-video-prompts v3.3.1

Dialogue/silent-interaction updates use `dialogue/spatial-blocking.md`: mandatory spatial decisions and listener responses, with motivated stillness preserved; fight thresholds remain fight-specific.

A director-level system for AI video prompts. The deep thinking (choices and contact causality, the four-layer dialogue engine, psychological action, status and power, continuity seams) stays **internal**. What comes out is **pure cinematic execution**: one vivid, camera-recordable **Extended** prompt per clip, with real optics, physical light, skin, face, body language, and spoken-register dialogue.

## Architecture: three rooms

```
Director's Room (design)  ->  Lens (translate + enrich)  ->  Prompt (Extended output + lint)
 v1's deep systems, kept       depiction grammar,             plain prose, 7-slot skeleton,
 internal, never in the        five passes: optics, light,    quoted spoken lines, notes
 prompt                        skin, face, body and status    outside the copy block
```

**Context-Aware Routing:** before anything is written, the Director's Room builds a Context Profile (purpose, power, body state, space, audience, relationship, tools, tone, stakes) that routes to an action mode, a dialogue situation, display rules, a camera stance, and a look. There is no default scene.

Texture Authority: story facts are **locked**; sensory texture is **open**. Budgets are three tiers (A story and contact: strict; B performance: generous; C texture: unlimited but coherent).

## Layout

```
SKILL.md                      Entry: pipeline, defaults, 7 rules, one precedence ladder, routing
core/        pipeline.md      Three rooms, Texture Authority, tiered budgets
             precedence.md    Resolution examples for the single ladder
             context-routing.md  Context Profile and routing to modes, situations, display rules, camera, look
lens/        lens-layer.md            Depiction grammar and the design-to-prompt procedure
             output-skeletons.md      Extended (default), Standard, Compact, multi-shot, continuation
             optics-and-stock.md      Pass 1: lens, depth of field, stock, grain, halation, camera behavior
             physical-light.md        Pass 2: sources, color temperature, falloff, catchlights, atmosphere
             skin-and-material.md     Pass 3: skin, hair, fabric, material, anti-plastic
             face-pass.md             Pass 4: FACS-informed face lexicon, micro-expressions, masking
             body-and-status.md       Pass 5: Status & Proxemics, posture, prop business, listening
dialogue/    spoken-register.md       Real-speech texture, delivery tags, voice script
             conversation-units.md    Multi-turn units, timing math, coverage, seams
             situation-profiles.md    13 situation profiles: movement, pace, silence, camera
references/  action-modes.md  Ten fight modes with pacing, fatigue, reach, terrain, fail-states
             spatial-tactics.md  Arena card, 3D position ledger, path vocabulary, line-break rules, spatial QA gate
             Director's Room systems: choreography, hit-feel, dialogue-engine, performance-and-psychology,
             character-and-performance, consistency, camera-and-rhythm, world-and-style, powers-and-vfx,
             action-reference-system, prompts-and-segments, ai-pipeline, delivery-and-qa, generation-handoff, ...
visual/ narrative/ sound/ production/ post/ quality/ ux/   Domain files (stubs merged)
models/       README.md + adapter template   Capability checklist, how answers change the prompt
evals/        cases.md                       12 cases, rubric, A/B protocol
examples/     context-routing-examples.md    Six routed cases (stealth, last stand, sparring, street argument, farewell, public/private)
              v3-extended-examples.md        Three Extended prompts (EN, ZH, face close-up) + before/after
              legacy-v1/                     v1 examples (design-side illustration; kept for reference)
scripts/      lint_prompt.py                 Lint a final prompt for the Lens grammar
              check_spatial.py               Spatial QA gate on a fight's position ledger (design check)
              check_skill.py                 Lint the package (links, routing, competing authorities)
              draw_inspiration.py            v1 inspiration drawing tool (unchanged)
MIGRATION.md                    What changed from v1 and why
```

## Using it

- Say what you want. The default is full depth and an Extended prompt. Say "short", "lite", or "简版" for the Compact tier.
- Check a prompt: `python scripts/lint_prompt.py prompt.txt` (add `--tier standard|compact` if relevant).
- Check the package after editing: `python scripts/check_skill.py .`
- Measure: run `evals/cases.md` on your model before trusting any rule or any vocabulary.

## Context cost

Extended by default loads more than v1's lean path did. Rough estimates (Chinese counted at ~1.3 characters per token, other text at ~4): the Extended core alone is about 19K tokens; a dialogue scene about 30K; a fight scene about 25K. If your model or plan struggles with that, say "short" or "lite", or trim the passes you do not need for the shot.

## Status

v3 encodes design principles and a vocabulary. It has not been benchmarked on any video model. Optics, light, face, and speech terms are marked "confirm per model". Language note: the v1 depth systems keep their original Chinese; the v3 layers are written in English with Chinese equivalents in the lexicons. Prompts are written in the language the target model handles best.
