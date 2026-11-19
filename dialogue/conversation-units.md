# Dialogue v3, Part 2: Conversation Units

v1 built dialogue around 5-second event units, so a clip carried one short line and the actors stood still. v3 builds around the **conversation unit**: a continuous exchange with one dramatic turn, including the listening between lines.

## 1. The unit

A conversation unit has one meaningful change: a status shift, a revelation, a decision, a refusal or an accepted invitation. Three to eight turns is a planning example, not a minimum: a two-line exchange or a silent response can form a complete unit. Do not add speech or gestures to fill a turn quota. Fit the unit to the requested duration and the model's real clip length (`models/README.md`); a longer scene is a chain of units joined by seams.

## 1b. Spatial spine (required design)

Before line-level acting, use [spatial blocking](spatial-blocking.md) to record the unit's opening geometry, cue and goal, choice to maintain/relocate/mix, path or hold reason, counterpart response, and ending geometry/consequence. Revisit it at a meaningful turn, not for every utterance. Stillness, warmth and cooperation can pass; a changing camera and busy hands cannot substitute for this decision. A long scene carries the resulting relations forward across units.

## 2. Unit skeleton

This is the skeleton for a **formal exchange** (situation profiles A and B in `situation-profiles.md`). Other situations (street argument, farewell, confession, interrogation, walking talk, post-exertion) use their own skeletons in `situation-profiles.md` section 3.

| Stage | Purpose | Typical beats |
|---|---|---|
| Opening gambit | Establish who holds status and what the topic is | A greeting, a prop beat, a loaded first line |
| Probe | One side tests | A question, an offer, a silence |
| Evasion or pressure | The other defends or pushes | Deflection, repetition, a posture change |
| Turn | The change happens | A confession, a threat, a concession, a laugh |
| Exit | Aftermath | An echo, a prop beat, a look away, stillness |

It need not fill all five; a short unit can be probe → turn → exit.

## 3. Turn anatomy

Each turn contains, in time order:

1. **Listener beat while the speaker begins** (stillness, a glance, a prop beat)
2. **The line** in spoken form with delivery (`spoken-register.md`)
3. **A body beat riding on the line** (a swallow, a hand moving, a posture change, or a phase of the already-designed path/hold). The unit spatial spine precedes these details; it is not rebuilt or forced to move once per line
4. **The listener's response** (a backchannel, a silence, a micro-reaction)
5. **A camera cue** only where it adds information (a push-in on the pivotal word, a cut to the hands)

Silence is a turn too: a long hold with a visible action in it (a lid ticking on porcelain).

## 4. Timing math

Use the single [speech pace table](situation-profiles.md#2-speech-timing-by-arousal) for state-dependent starting estimates and the selected situation for silence. Count the actual locked words/characters, reserve time for breaths, listener responses and movement, and time a read-through when possible. Do not maintain a separate clip-length word quota here. Estimates are not measured timings. If speech does not fit, preserve its wording and negotiate duration/staging/splitting; do not rush or silently cut a required line.

## 5. Overlap and interruption

Write interruptions as sequence: `Wu starts, "But the—" and Chen speaks over him, "Tuesday."` Some models cannot render overlapping voices; then write the interruption as a cut-off followed by the other's line. Mark which version you used in a note.

## 6. Coverage inside a unit

The table below is for a seated two-person exchange. Other situations route the camera by profile: handheld and participant for a street argument, tracking beside or in front for a walking talk, a long lens and a hold after the departure for a farewell, tight and low-key for a whisper (`situation-profiles.md`).

| Moment | Framing | Why |
|---|---|---|
| Opening geometry | Two-shot, wide or medium | Seating, status, space |
| Pivotal line | Single or over-shoulder, push-in | Isolate the speaker's face |
| The listener's reaction | Single on the listener | Listening is acting |
| The prop beat | Insert (cup, hands) | Detail carries subtext |
| The exit | Two-shot or a slow pull | Aftermath, restored distance |

Choose coverage after blocking. Preserve readable evidence of a key rise, route or change of alignment, then use closer coverage when it serves performance. A seated hold can retain a fixed composition; no camera-axis quota applies to dialogue.

Do not cut to a face for every line. Add camera cues where a change of information or geometry calls for them; a fixed-camera scene may keep one framing throughout. In a multi-shot prompt, use cut language (`lens/output-skeletons.md` section 7). No fixed cue count overrides the user's framing or the unit's blocking.

## 6b. Framing: choose for acting, not for fear of sync

Do not assume that dialogue always requires a close-up or that a wider frame guarantees poor sync. Verify the target model under the actual shot and audio conditions. Choose framing for **performance**: when a line carries a status shift or a face beat, give it a medium or close shot and a listener beat; when the shot is a moving wide, the lines can still ride on it, but expect little face acting. Verify on your target model; a successful clip is still only one data point.

## 7. Chaining units (seams)

At the end of a unit, record: **last line and who held the floor; each person's world anchor, facing, posture/height and distance; routes/access and unresolved spatial invitations; prop states (cup level, lid, paper pile), light, any unresolved silence.** The next unit opens from those facts, written as present: "Chen's cup is half empty on his knee; Wu's palms are still flat."

## 8. Monologue and voice-over

A spoken monologue still has breath groups, false starts, and pauses. Voice-over can be more composed but should still sound like the character. Put the picture to work under VO: hands, objects, small movements. Do not narrate what the audience can see.

## 9. Three or more people

- Floor control: who speaks, who can interrupt, who is ignored.
- Eye-lines map the alliances: who looks at whom while someone speaks.
- Status triangles: two people align against one, or one controls both.
- Side exchanges (a whisper, a glance) are Tier B beats.
- Keep one primary speaker per moment.

## 10. Checklist

- [ ] Is the situation profile named, and do movement, distance, pace, and silence match it (not a default table)?
- [ ] Does the unit have a single turn?
- [ ] Is the unit spatial spine complete and plausible (start, cue/goal, choice, path or hold reason, counterpart response, result)? Has it passed `spatial-blocking.md` section 6?
- [ ] Do world positions, routes, orientation and access survive cuts and seams, with movement evidence or an explicit motivated hold?
- [ ] Is every line in spoken form, with delivery?
- [ ] Does each turn include a listener beat?
- [ ] Do the lines fit the clip length with silence included?
- [ ] Is the status ledger visible in posture, space, tempo, and eye control?
- [ ] Are props consistent and their state tracked?
- [ ] Are locked lines unchanged?
- [ ] Is the end state written for the seam?
