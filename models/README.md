# Model Adapters

v1's platform matrix was almost entirely "to verify." v3 replaces it with a method: a capability checklist, a table that says how each answer changes the prompt, and an adapter template that may be filled **only from verified sources or your own test clips**. Nothing here claims what any specific model can do; capabilities change quickly.

## 1. Capability checklist (answer per model, with a date)

| # | Question | How to verify |
|---|---|---|
| 1 | Maximum and typical clip duration | Official docs or the interface |
| 2 | Single shot only, or several shots in one generation | Docs, then a test |
| 3 | Reference inputs accepted (image, video, audio), how many, what each is used for | Docs, then a test |
| 4 | First frame, last frame, or both | Docs |
| 5 | Native audio: ambience/effects, **speech**, **lip sync** (three separate answers) | Docs, then a test |
| 6 | Prompt language(s) that work best | Docs, then an A/B test |
| 7 | Separate negative-prompt field | Interface |
| 8 | Camera control: text only, or real parameters | Interface |
| 9 | Resolution, aspect, frame rate options | Interface |
| 10 | **Prompt length behavior** (truncated, diluted, or fully used) | Test with the length ladder (`evals/cases.md`, case 10) |
| 11 | **Cinematography vocabulary** the model responds to (lens, grain, halation, rim light, handheld) | Test with case 9 |
| 12 | **Fine face control** (gaze, brow, micro-flicker) by shot size | Test with case 12 |

## 2. How each answer changes what you write

| If the model... | Then |
|---|---|
| Accepts long prompts | Extended in full |
| Truncates or dilutes long prompts | Use the largest tier that holds; sacrifice in the order set in `core/pipeline.md` |
| Generates one short single shot | One Tier A chain per clip; self-contained first sentences; seams carry continuity |
| Generates several shots in one pass | Write the look anchor and subject lock once, then cut language (`lens/output-skeletons.md` section 7) |
| Accepts several reference inputs | Say in the control notes what each reference is for; keep text anchors; a face portrait does not stand in for costume or weapon contact angles |
| Takes first and/or last frames | Check the frame against the design; describe the motion between frames |
| Supports native speech | Lines inline with delivery; voice script optional |
| Has native audio but unverified speech | Lines inline for mouth timing plus a voice script; sync untested |
| Has no native audio | Voice script outside the block; ambience as one line |
| Responds well to cinematography vocabulary | Use the optics/light terms freely in the look anchor |
| Ignores cinematography vocabulary | Rely on depiction ("a thin orange edge on his hair"), keep terms minimal |
| Prefers English or Chinese | Write the prompt in that language; keep names consistent |
| Has a negative field | At most two short exclusions there; the body stays positive |
| Has only text camera control | Camera relationships in natural sentences, never pseudo-parameters |
| Renders fine facial detail poorly | Use the fallback order in `lens/face-pass.md` section 7 |

## 3. Adapter file template

Create `models/<model>-<version>.md` (copy `_adapter-template.md`). Fill only what you have verified. An entry without a date and a source is not an entry. When a model updates, mark the old entry "superseded"; do not edit it into the new one.

## 4. Status

One observation is recorded: `observed-wuxia-30s-clip.md` (one clip, model not named). Run `evals/cases.md` on your model and fill in a proper adapter from the results.

## 5. Appendix: v1 decision tree (work method, not a capability score)

Each node first checks that the current mode supports it; previews and pre-vis are not guarantees.

| Primary need | Candidate path | Fallback |
|---|---|---|
| Character consistency | A qualified reference (image-to-video or character reference); with none, strong text anchors or build the asset first | Fix asset angles or costume first; avoid conflicting multi-image references |
| Complex action and contact | Fewer concurrent events; split events; use first/last poses or controllable motion references when supported | Split contact phases, fix the camera, use a white-model or composite; do not demand a last frame |
| Style exploration | Text-to-video, or text-to-image first to compare signatures | Fix the scene, change one dimension at a time, then lock the character |
| Continuous long take | Define the continuous space first, then first/last frames or segment handoff by support | First/last frames do not guarantee the path between; interpolation adds samples, not plot or contact |
| Exact lip sync | A dedicated lip-sync workflow, a qualified audio track, close shots | Split into dedicated dialogue shots, or voice-over; do not demand exact micro-expression in a fight clip |
| Pure atmosphere | Text-to-video, steady camera, one visible change | Reduce detail, use a still with slight motion or post; do not pad with empty shots |

Order: user goal → available assets → interface capability → cost → pilot results. One brand's versions and hosting platforms may differ; unknown capability is internal "to verify", and to the user say "I'll work from the settings you can actually choose." Never silently downgrade a user's explicit goal.
