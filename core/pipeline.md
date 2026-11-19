# Pipeline Contract

This file defines how the three rooms hand off and what each may change. It does not claim priority over anything; precedence lives in `precedence.md`.

## 1. The three rooms

| Room | Input | Does | Output | Never |
|---|---|---|---|---|
| Director's Room | The user's story, constraints, references | **Context Profile and routing** (`context-routing.md`), **space check for fights, expanded arena card and 3D position ledger for complex choreography** (`references/spatial-tactics.md`), **unit spatial spine for dialogue or silent interaction** ([dialogue blocking](../dialogue/spatial-blocking.md)), choices, contact and support, four-layer dialogue, psychological action, status and power, seams, continuity | A design record (internal) | Writes the final prompt text; invents locked facts |
| Lens | The design record | Translates to recordable statements; runs five enrichment passes; applies coherence | A texture-rich shot description | Changes locked facts; adds Tier A events |
| Prompt | The shot description | Orders it into the skeleton, writes it in model language, lints it | One clip prompt (Extended by default) + notes outside the copy block | Contains design vocabulary, labels, or explanations |

Each room can send work back. If the Lens cannot depict something, return it to the Director's Room to re-stage; do not cover the gap with adjectives.

## 2. Texture Authority

**Locked (story facts, change only with the user's say-so):** plot and sequence of events; outcome and who wins; who knows what; character identity and established look; plot-bearing objects (a letter, key, weapon); injuries and their consequences; world and ability rules; the user's named moves, lines, and face targets; anything the user set up and expects to persist.

**Open (sensory texture, add freely):**
- Lens, aperture, stock, grain, halation, grade, shutter feel, camera behavior
- Light quality, direction, color temperature, falloff, bounce, haze, as long as the established light sources and time of day stay consistent
- Skin, pores, fine hair, flush, sweat, lips, eyes, hair flyaways, fabric weave and creases, wear
- Face behavior: blink, gaze drift, micro-movements, asymmetry
- Posture, weight, stillness, fidgeting, status behavior, prop business with **ordinary, setting-consistent props** (a cup, a pen, a sleeve, a lamp), listener acting
- Ambient motion: dust, steam, breath fog, fabric drift, water
- Speech rhythm, disfluency, breath, voice quality, room tone

**Dialogue blocking is designed before texture:** ordinary rising, walking, yielding space, changing orientation and deliberate holds are usually Tier B performance. Record their paths or hold reasons and the listener's response. A consequential restriction, forced contact, departure, transfer or reveal is checked under existing story locks and Tier A; never add one as sensory enrichment. See [dialogue spatial blocking](../dialogue/spatial-blocking.md). Fight density rules do not set dialogue movement quotas.

**Gray (check, then usually open):** a new object that a character *uses in a way that affects the scene*; new weather or time-of-day change; a new off-screen sound that implies an event. Open if it is mundane and does not change what happens or what anyone knows. If it does, offer it as a candidate. Weapons, letters, keys, wounds, and secrets are never added.

**Added-texture note.** After the copy block, one line: "Added: porcelain cup and lid business for Chen; tungsten desk lamp; breath fog." The user can veto. This is transparency, not a request for permission.

## 3. Tiered budgets

**Tier A: story and contact events (strict).**
- Use the operational [event boundaries](../references/generation-handoff.md#event-boundaries) in the capacity owner. Distinguish causal interactions from individual verbs, camera shots and model requests.
- The action mode suggests rhythm; numerical density examples are planning hypotheses, not model limits or mandatory targets. The request capacity and splitting check has one definition: [generation handoff](../references/generation-handoff.md) section 3.
- Recheck timing, limb/support compatibility and camera continuity when an attack, defensive relation, complex contact or camera task changes. Split only when re-staging cannot keep those demands readable within the actual model/request constraints; sequential shots are not automatically separate requests.
- Record persistent state changes. A knockdown caused by an already recorded strike is that interaction's result, not a second identical charge; a separate door closure or independent weapon break is a separate transition. Simultaneous independent threats remain distinct.
- This tier exists to keep action physically readable. Description remains subject to shared attention, shot visibility and prompt limits.

**Tier B: performance and body (generous).**
- Written beat by beat in time order. Select motivated beats across face, posture, hands, gaze, prop and listener. No minimum gesture count; a sustained hold may carry the whole turn.
- Each beat is anchored to a line, a cue from the other person, a prop, or a breath. Unanchored fidgeting is noise.
- Readability limits: simultaneous hand tasks need compatible grips and timing. Fast full-body action can make fine facial cues hard to read; design framing, coverage or a suitable beat rather than deleting an explicit expression target (see `references/performance-and-psychology.md` and [conflict examples](precedence.md)).
- A face close-up the user demanded is protected (precedence tier 2).

**Tier C: texture (open).**
- No fixed count. Limited by relevance, shared attention, shot visibility, **coherence** and the model's prompt length.
- Coherence rules: one lens family per shot; one stock/grade; one light family (sources, direction, color temperature agree); no two wind directions; no object in two states; no jargon pile-ups (anamorphic and fisheye and tilt-shift together is a contradiction).
- Every sentence must add information. Stacked synonyms ("stunning, breathtaking, epic") are removed.
- Order of sacrifice when the model's limit forces cuts: repeated or secondary optics, then secondary ambient texture, then Tier B secondary beats. Never cut Tier A causality, identity anchors, or locked demands.

## 4. Depth is default

All depth systems engage when the scene calls for them. There is no consent state machine. The user can request shorter delivery with "lite", "short", "quick", or a localized concise request. Necessary design checks remain; optional elaboration can shrink. They can request more focus with a plain sentence ("make the face work harder"). Do not announce modules, do not ask whether to "unlock" depth.

Ask at most once, together, for what changes the outcome: the creative core, target model, clip length, which reference inputs exist. Assume and label the rest.

## 5. Design record contents (internal)

Keep it brief and structured, never in the prompt:

`Context Profile and routed modes | Fight spatial record (expanded ledger for complex paths) or dialogue unit spatial spine (as applicable) | Locked facts | Added texture | Beats and status shifts | Dialogue (intent, subtext, spoken form) | Contact chain and support | Seam state in/out | Shot list with camera tasks | Open risks`

## 6. Clip splitting

Map distinct Tier A events to requests with the generation-handoff capacity check, preserving the chosen action mode. Within a clip, B and C remain limited by coherence, attention and prompt length rather than a fixed count. Dialogue-heavy scenes split by conversation unit (`dialogue/conversation-units.md`), not by 5 s event count. Multi-shot-capable models can take a short shot list inside one prompt; verify per model (`models/README.md`).

## 7. Shared attention and coverage

Choose the main image/action or conversational turn, then the supporting performance and look. All tiers share runtime and viewer/model attention. A coherent detail can still be irrelevant. Preserve rich description where it clarifies intent; remove repetition and secondary demands before compromising a locked target. Match detail to shot size and reference inputs. An established first frame usually needs motion and changes more than a repeated portrait; retain identifiers needed to prevent swaps.

Before delivery, map each explicit user target to its actual sentence/action/line and end state. Resolve missing or contradictory targets; a lint pass cannot perform this semantic check. Keep this compact coverage record internal unless requested.

Design depth and output length are independent. Simple scenes need concise reasoning records, not incomplete reasoning. Expanded coordinates and tables are useful for complex paths and continuity, not a paperwork quota.

## 8. Quality preservation

Record a brief quality target alongside locked story facts: desired pace and force, complexity of attack/response, camera ambition, emotional development, material/light specificity and continuation. Infer a sensible level from the request, but do not quietly lower explicit ambition to ease generation. A request for relentless action requires designed evolving exchanges and motivated camera participation; a single readable parry is not an equivalent substitute. A requested still scene requires expressive timing, listening and framing rather than compulsory motion.

Develop both causal readability and expressive specificity. For each important action, show the opponent's response and the resulting opportunity; recovery may become the next defense rather than a reset. For dialogue, realize intention through exact/authorized language, delivery and the listener's consequential response. Texture connects to bodies, surfaces, sources and motion; adjectives alone do not replace it. Keep useful detail even when it lengthens the prompt.

Before shortening, identify what the removed text contributes. Compress repeated phrasing; preserve distinct action transitions, listener changes, camera tasks and specific material/light cues. If an actual platform limit makes a protected target impossible, propose a different staging or delivery path while preserving the goal; mark an ambitious untested draft honestly. Unknown capability alone does not justify silently simplifying.

Evaluate revisions against the current approved prompt for each scene, not an average across unrelated scenes. A structural improvement does not establish creative improvement. If a candidate weakens an important dimension, restore the relevant method or retain the prior route. Human review and generated-video comparisons remain necessary for release claims.
