# Pipeline Contract

This file defines how the three rooms hand off and what each may change. It does not claim priority over anything; precedence lives in `precedence.md`.

## 1. The three rooms

| Room | Input | Does | Output | Never |
|---|---|---|---|---|
| Director's Room | The user's story, constraints, references | **Context Profile and routing** (`context-routing.md`), **arena card and 3D position ledger** (`references/spatial-tactics.md`), choices, contact and support, four-layer dialogue, psychological action, status and power, seams, continuity | A design record (internal) | Writes the final prompt text; invents locked facts |
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

**Gray (check, then usually open):** a new object that a character *uses in a way that affects the scene*; new weather or time-of-day change; a new off-screen sound that implies an event. Open if it is mundane and does not change what happens or what anyone knows. If it does, offer it as a candidate. Weapons, letters, keys, wounds, and secrets are never added.

**Added-texture note.** After the copy block, one line: "Added: porcelain cup and lid business for Chen; tungsten desk lamp; breath fog." The user can veto. This is transparency, not a request for permission.

## 3. Tiered budgets

**Tier A: story and contact events (strict).**
- An event is one exchange of attack/defense/transfer with a clear outcome. Approach, crossing, and forced reaction of one blow count as one.
- Density is **mode-dependent** (`references/action-modes.md`): a duel about 1–3 independent interactions per ~5 s, a last stand 2–4 with overlap, an ambush 3 or more in the first 2 s, a stealth takedown 0–1 per clip, a ritual duel 0–2. These are starting points for short clips; scale after testing on your model and duration.
- Split a clip when it contains a new attack, a changed defensive relationship, a new complex contact, or a second camera task.
- A new persistent state (knockdown, disability, wall crack, weapon break, door closing) is its own event.
- This tier exists to keep action physically readable. It never limits how richly each event is described.

**Tier B: performance and body (generous).**
- Written beat by beat in time order. Guide for a dialogue-heavy 10 s clip: 6 to 12 beats across face, posture, hands, gaze, prop, and listener.
- Each beat is anchored to a line, a cue from the other person, a prop, or a breath. Unanchored fidgeting is noise.
- Readability limits: one primary hand business at a time per person; simultaneous gestures must not contradict (no sip while gesturing with the same hand); fast fighting and fine facial micro-expression do not share a moment (see `references/performance-and-psychology.md`).
- A face close-up the user demanded is protected (precedence tier 2).

**Tier C: texture (open).**
- No count. Limited by **coherence** and the model's prompt length.
- Coherence rules: one lens family per shot; one stock/grade; one light family (sources, direction, color temperature agree); no two wind directions; no object in two states; no jargon pile-ups (anamorphic and fisheye and tilt-shift together is a contradiction).
- Every sentence must add information. Stacked synonyms ("stunning, breathtaking, epic") are removed.
- Order of sacrifice when the model's limit forces cuts: repeated or secondary optics, then secondary ambient texture, then Tier B secondary beats. Never cut Tier A causality, identity anchors, or locked demands.

## 4. Depth is default

All depth systems engage when the scene calls for them. There is no consent state machine. The user can lower depth with "lite", "short", "quick", or "简版". They can request more focus with a plain sentence ("make the face work harder"). Do not announce modules, do not ask whether to "unlock" depth.

Ask at most once, together, for what changes the outcome: the creative core, target model, clip length, which reference inputs exist. Assume and label the rest.

## 5. Design record contents (internal)

Keep it brief and structured, never in the prompt:

`Context Profile and routed modes | Arena card and position ledger | Locked facts | Added texture | Beats and status shifts | Dialogue (intent, subtext, spoken form) | Contact chain and support | Seam state in/out | Shot list with camera tasks | Open risks`

## 6. Clip splitting

Split by Tier A **as set by the action mode** (a stealth approach and its strike stay one unit; a last stand chains clips). Within a clip, B and C are unlimited. Dialogue-heavy scenes split by conversation unit (`dialogue/conversation-units.md`), not by 5 s event count. Multi-shot-capable models can take a short shot list inside one prompt; verify per model (`models/README.md`).
