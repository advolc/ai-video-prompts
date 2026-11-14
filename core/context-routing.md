# Context-Aware Routing

v3.0 and v3.1 applied one template to every scene: the same exchange rhythm, the same seated-table dialogue geometry, the same single-leak face, the same length weighting, the same ending on a still hold. Real scenes differ by **why they exist, who holds power, how tired or frightened the people are, how much space they have, who is watching, and what happens if someone fails**. This file adds a routing step in front of every subsystem. **Route first, then write.**

## 1. The Context Profile

In the Director's Room, before any module runs, build a one-line profile from the user's input. Fill what is known; infer the rest; label inferences. Ask only if an axis changes the whole design and cannot be inferred (once, together with the other intake questions).

| Axis | Values (examples, not a closed list) |
|---|---|
| **Purpose** (why this scene exists) | decide an outcome, reveal character, escalate, reverse, release, intimidate, deceive, seduce, mourn, say goodbye, test, comic relief, ritual |
| **Power** | parity, dominance, inversion in progress, information asymmetry (who knows more) |
| **Body and arousal** | calm / agitated / panicked; stamina fresh / winded / spent; injured (where) |
| **Space** | confined, open, vertical, crowded, dark, unstable footing, moving platform (horse, boat, vehicle), weather. For any fight, build an arena card (`references/spatial-tactics.md`) |
| **Privacy and audience** | private, semi-public, public with onlookers, watched by authority, watched by an enemy |
| **Relationship** | intimate, familiar, formal, strangers, enemies, pretending to be something else |
| **Reach and tools** | unarmed, short, long, flexible, ranged, improvised, mixed; size and speed mismatch |
| **Tone and medium** | realist, stylized, comic, horror, ritual or code-bound; live-action or animation |
| **Stakes and fail-state** | lethal, injurious, humiliating, reversible, comic; what failure looks like for each side |
| **Time** | urgency, available runtime, whether the scene continues in the next clip |

**Profile line (design record):** `Purpose: ... | Power: ... | State: ... | Space: ... | Audience: ... | Relationship: ... | Tools: ... | Tone: ... | Fail-state: ...`

## 2. What the profile routes

| Subsystem | Routed by | Where |
|---|---|---|
| Fight pacing, initiative, pause legitimacy, fatigue, reach, terrain, fail-states | Purpose, power, state, space, tools, stakes | `references/action-modes.md` |
| Fighter movement through the arena (3D ledger, footwork, path vocabulary, line-break rule) | Space, mode, tools | `references/spatial-tactics.md` |
| Clip splitting and Tier A density | Action mode | `references/generation-handoff.md` section 3 |
| Dialogue physicality, movement, timing, silence, coverage | Situation (purpose, space, audience, relationship, arousal) | `dialogue/situation-profiles.md` |
| Dialogue/silent-interaction geometry, paths, deliberate holds and listener responses | Purpose, relationship, state, actual routes and access | [Dialogue spatial blocking](../dialogue/spatial-blocking.md) |
| Body language and status behavior | Situation and power | `lens/body-and-status.md` section 13 |
| Facial display (mask strength, leak channels) | Audience, relationship, arousal, fatigue, stakes | `lens/face-pass.md` section 10 |
| Camera behavior (observe, participate, subjective) | Purpose, arousal, space | `references/camera-and-rhythm.md` and `lens/optics-and-stock.md` section 10 |
| Light mood | Privacy, stakes, time | `lens/physical-light.md` section 12 |
| Sound strategy (silence, density, voice) | Mode, arousal, privacy | `sound/sound-and-voice.md` |
| Slot weights, length, end-state mode | Scene type | `lens/output-skeletons.md` section 11 |

## 3. Resolution rules

1. **Purpose picks the primary mode.** A stealth takedown with a panicked character is still a stealth takedown, performed badly.
2. **State modifies tempo, never purpose.** Fatigue, injury, and arousal change speed, precision, guard height, breath, and what a character can hide. They do not change what the scene is for.
3. **Audience modifies the face and the voice before the blocking.** A public setting suppresses expression first; private settings release it. Blocking changes when the audience can interrupt or intervene.
4. **Space constrains moves.** For dialogue, map available anchors, routes, sight/hearing and actual access limits; record the unit spatial spine before fine gestures. A profile tag is not a blocking plan. For fights, the environment limits what the mode can do (a confined corridor removes flanking; an open field removes cover).
5. **Blend, don't average.** When two modes apply (a sparring match turns real), use the first until a **turn** event, then switch. Check a fight transition's actual event under Tier A. A dialogue turn or ordinary change of alignment is not automatically a new Tier A event or a new model request; use the conversation unit and the actual consequence.
6. **Re-route at turning points.** A change in power, arousal, audience, or purpose triggers the router again. A scene may use several profiles in sequence.
7. **Locked facts and user decisions override the router.** If the user says "it must be a back-and-forth duel", it is one.

## 4. When the profile is unknown

- Do not default to a seated table or a back-and-forth exchange. State the assumed profile in the notes and continue.
- If the purpose is missing and would change the design (is this a farewell or a quarrel?), ask once.
- If the user gives only a genre ("a fight scene"), pick the mode that the narrative setup suggests, list one alternative mode, and offer to switch.

## 5. Anti-template rule

Examples in this skill (the tea scene, the canyon duel, the doorway) are illustrations of one profile each. **Never copy an example's posture, rhythm, or ending into a scene whose profile differs.** Every example states its profile so you can check the match.

## 6. Output of routing

Add to the design record:

`Context Profile | Action mode (if any) | Situation profile and unit spatial spine (if dialogue/silent interaction) | Display rules | Camera stance | Look mood | Density and splitting | End-state mode | What a failed generation would look like in this mode`

The last field is deliberate: each mode has a distinct way of going wrong, and knowing it makes triage faster.
