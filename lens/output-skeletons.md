# Output Skeletons

**Extended is the default level of relevant richness.** It has no minimum word count. Standard and Compact change delivery length, while necessary design checks remain. Choose a shorter expression when the scene is sparse, the user requests brevity or actual model evidence favors it; retain all explicit targets.

The skeleton is a coverage aid, not seven mandatory paragraphs. Deliver plain prose by default. Verified platform syntax or an explicit user format may use headings, tags or timestamps; keep analytical notes outside the copy block.

## 1. The seven slots (Extended order)

| # | Slot | Content | Weight |
|---|---|---|---|
| 1 | Look anchor | Medium and format (live-action, 3D, 2D), aspect ratio, lens family and focal length, depth of field, stock or sensor character, grain, grade and contrast, shutter feel, overall light family | 1–3 sentences |
| 2 | Subject lock | Per character: age band, face structure with one asymmetry, skin state, hair state, build, costume materials and wear, weapon or prop with material and wear, one distinctive identifier. Carry the identifiers needed per clip; reference/first-frame inputs may reduce repeated description | 2–4 sentences each |
| 3 | Set and light physics | Space anchors and surfaces, **the named landmarks and heights the action will use**, named light sources with direction and color temperature, atmosphere (haze, dust, steam, rain), time of day, temperature cues | 2–5 sentences |
| 4 | Performance timeline | Time-ordered beats: body, hands, gaze, face, prop business, listener, spoken lines with delivery, and any Tier A contact events written as one recordable chain | Weight set by scene type (section 11); about 55–65% for dialogue-driven and mixed scenes |
| 5 | Camera behavior | Framing, motivated movement, focus pulls, handheld micro-motion, reframing, always attached to the beat it serves | 1–4 sentences, woven near their beats |
| 6 | Sound and speech | Ambience, foley, room tone, selected speech and brief voice/breath cues; actual native-audio or post-production execution is tracked outside the prose in generation-handoff | 1–4 sentences |
| 7 | End state | The final frame or the handoff state (end modes in section 11): positions, posture, held objects, light. It may hold still or leave motion in progress. Doubles as the seam into the next clip | 1–2 sentences |

## 2. Length

| Tier | English words | Chinese characters | Use |
|---|---|---|---|
| **Extended (default)** | about 320–520 per clip | about 650–1000 | Rich scenes when useful; no minimum |
| Standard | about 150–250 | about 300–500 | Models with tighter limits; mid-depth requests |
| Compact | about 60–110 | about 120–220 | "short/lite/quick"; fast iteration |

- **Do not scale mechanically with duration.** The ranges above fit a single short clip of about 5–10 s. For longer clips, size the text by the actual changes, speech and camera tasks. For planning a dense multi-shot clip, use the provisional range of **about 25–35 English words per second** (about 50–70 Chinese characters per second). Treat this as a hypothesis and test it with `evals/cases.md` case 10. It describes a **dense, multi-event** clip; sparse scenes (stealth, atmosphere, a held look) need fewer words per second, and padding them with invented activity breaks their mode (section 11). Use `scripts/lint_prompt.py --seconds 30 --scene-type action` for this dense-action estimate; other scene types use the section 11 ranges.
- These are working ranges, not promises. The real ceiling is the target model's documented prompt limit. Check `models/README.md` item 10 (prompt length behavior). If the limit is unknown, deliver Extended and add one line outside the copy block: "If this truncates or the model drifts, try the Standard version."
- Each clip is self-contained at the appropriate length; carry identity and seam facts without padding.
- A clip that is mostly dialogue spends its length on the performance timeline and speech (slot 4), not on more adjectives.
- When a limit forces cuts, sacrifice in this order (see `core/pipeline.md`): repeated or secondary optics, secondary ambient texture, secondary Tier B beats. Never Tier A causality, identity anchors, or locked demands.

## 3. Extended template (placeholders, not copy-paste text)

Write as flowing paragraphs. Brackets mark what to fill.

```
[Medium/format], [aspect]. Shot on [lens family/focal length] with [depth of field], [stock or sensor character], [grain], [grade/contrast], [shutter feel].

[Character A]: [age band], [face structure and one asymmetry], [skin state], [hair state], [build], wearing [costume materials and wear], [weapon/prop with material]. [Character B]: ... 

[Set]: [space anchors and surfaces]. [Light]: [named sources, direction, color temperature, falloff], [atmosphere], [time of day, temperature cues].

[Beat 1: posture, hands, gaze, face, prop, listener]. [Speech: "line" with delivery]. [Camera cue tied to the beat]. [Beat 2...] [Tier A event as one chain: approach, contact, reaction, recovery]. ... [Beat n].

[Ambience, foley, room tone, voice quality.] [End state: positions, posture, held objects, light, stillness.]
```

## 4. Standard template

Slots 1, 2, 3 compressed to one sentence each (identity anchors and the key light only), slot 4 at about 4–6 beats, slot 5 as one sentence, slot 7 as one sentence. Skip slot 6 unless speech is present.

## 5. Compact template

```
[Medium + one-line look]. [Character(s): 2–3 anchors and weapon/prop or empty hands]. [Set and one light fact]. [The main event as one connected chain, with the key speech if any]. [One camera fact]. [End state.]
```

Keep identity anchors and the contact chain. Texture shrinks to the light fact and one material cue.

## 6. Continuation clip (opens from a seam)

Start with slot 1 (same look) and slot 2 (same anchors), then open slot 3 and slot 4 **from the previous clip's end state, written as present facts**: "Lin stands in the doorway, her weight on her right leg, her left hand hidden in her sleeve, snow falling between her and Han." Never "continuing from before" or "as in the previous clip".

## 7. Multi-shot inside one prompt (models that support it, verify per model)

Write the look anchor and subject lock once. Then run the shots in prose using cut language: "The scene opens on…", "Cut to a tight close-up of…", "The camera returns to the wide as…". Keep one contact chain per shot. State fixed identity and spatial anchors once, then re-check them in the result; continuity inside one pass is the model's job. If a platform has its own shot syntax (verified in docs or by test), use that syntax in the model adapter and keep this prose form as the fallback.

## 8. Dialogue-bearing clips

Spoken lines are written **inline** as quoted speech inside the timeline, each with a delivery cue and the body beat it rides on. Example form: `Wu says, voice dropping, "Sir, the shipment, it, uh, it didn't clear customs on Tuesday."` Fit line lengths to the clip duration (`dialogue/conversation-units.md`). Provide a separate **voice script** outside the copy block when the platform has no native speech or when you will voice in post (`dialogue/spoken-register.md` section 7).

## 9. Chinese output

Use the same slots in natural Chinese when Chinese is the requested or best-supported output language: look (lens, focal length, depth of field, grain and grade) -> subject lock -> setting and light -> performance timeline with quoted speech -> camera -> sound -> end state. Translate the physical descriptions into the output language. Avoid mixed-language jargon unless verified model behavior warrants it.

## 10. Control parameters stay out of the prose

Set resolution, duration and frame rate in the platform's documented controls when available. Prose such as "1080p", "30s" or "24 fps" is not proof that those output settings were applied. Describe dramatic timing where useful and retain an aspect-ratio composition anchor if relevant; keep export/settings labels in control notes unless the verified interface expects them in text. Inspect delivered stream metadata separately from visual adherence. This is an input-handling rule, not a conclusion from a bundled generation test. `lint_prompt.py` flags control-like prose for review; `--format platform` permits verified structured syntax. See [evidence boundaries](../references/source-scope.md#model-observation-record).

## 11. Scene-type weighting and end-state modes

Slot weights and length follow the **scene type**, set by the Context Profile.

| Scene type | Emphasis | English words per second (planning range) |
|---|---|---|
| Action-dominant (fight, chase) | Slot 4 with the Tier A chain about 60–70%; slot 5 camera 2–5 sentences; slot 6 impact and breath; slot 3 compact | 25–35 for dense multi-shot |
| Dialogue-dominant | Slot 4 beats and speech about 60–70%; slot 2 faces; camera 1–3 sentences | 15–30, by the speech pace |
| Intimate or emotional | Slots 2 (skin, face) and 4 (face beats) heavier; soft light; few words of action | 15–25 |
| Stealth, atmosphere, establishing | Slots 3 and 6 (space, light, sound) about 40–50%; slot 4 sparse; long holds | 10–20 |
| Insert, transition, montage | Compact-leaning; one image per sentence | n/a |

**End-state modes** (pick one; do not end every clip on a still hold):

| Mode | Use | How to write the last sentence |
|---|---|---|
| Hold | A scene that closes, a ritual, a farewell after the departure, an aftermath | Positions and light settle; a held frame |
| Handoff in motion | Last stand, chase, brawl, ambush burst | The last sentence leaves motion in progress with the state that carries into the next clip |
| Cut on action | An impact or an entry | The clip ends at the moment of contact or entry; the next clip opens on the result |
| Reveal | A twist or a discovery | The last image shows the new information |

A still hold at the end of a chase or last stand tells the model the fight has stopped. The examples in this skill end on holds because their profiles are hold-type.

## 12. Before delivery

Run `python scripts/lint_prompt.py prompt.txt --seconds N --scene-type action|dialogue|emotional|atmosphere`, selecting the actual scene type; omit runtime if unknown. Length estimates are guidance, not reasons to invent activity. Then confirm the coherence checklist in `lens/lens-layer.md` section 6, the length against the model's limit, and the one-line added-texture note.
