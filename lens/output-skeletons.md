# Output Skeletons

**Extended is the default for every prompt.** Compact and Standard exist only for when the user asks for "short", "lite", "quick", "简版", or when a model's documented prompt limit forces them.

The skeleton is a writing order, not a visible structure. The delivered prompt is plain prose: paragraphs allowed, no headings, no brackets, no labels, no bullet points, no timestamps.

## 1. The seven slots (Extended order)

| # | Slot | Content | Weight |
|---|---|---|---|
| 1 | Look anchor | Medium and format (live-action, 3D, 2D), aspect, lens family and focal length, depth of field, stock or sensor character, grain, grade and contrast, shutter feel, overall light family | 1–3 sentences |
| 2 | Subject lock | Per character: age band, face structure with one asymmetry, skin state, hair state, build, costume materials and wear, weapon or prop with material and wear, one distinctive identifier. Re-state in every clip | 2–4 sentences each |
| 3 | Set and light physics | Space anchors and surfaces, named light sources with direction and color temperature, atmosphere (haze, dust, steam, rain), time of day, temperature cues | 2–5 sentences |
| 4 | Performance timeline | Time-ordered beats: body, hands, gaze, face, prop business, listener, spoken lines with delivery, and any Tier A contact events written as one recordable chain | ~55–65% of the text |
| 5 | Camera behavior | Framing, motivated movement, focus pulls, handheld micro-motion, reframing, always attached to the beat it serves | 1–4 sentences, woven near their beats |
| 6 | Sound and speech | Ambience, foley, room tone, voice quality, breath; native-audio platforms only, otherwise one line of ambience | 1–4 sentences |
| 7 | End state | The final frame: positions, posture, held objects, light, what holds still. Doubles as the seam into the next clip | 1–2 sentences |

## 2. Length

| Tier | English words | Chinese characters | Use |
|---|---|---|---|
| **Extended (default)** | about 320–520 per clip | about 650–1000 | Every prompt unless told otherwise |
| Standard | about 150–250 | about 300–500 | Models with tighter limits; mid-depth requests |
| Compact | about 60–110 | about 120–220 | "short/lite/quick/简版"; fast iteration |

- These are working ranges, not promises. The real ceiling is the target model's documented prompt limit. Check `models/README.md` item 10 (prompt length behavior). If the limit is unknown, deliver Extended and add one line outside the copy block: "If this truncates or the model drifts, try the Standard version."
- A multi-clip piece gets Extended per clip.
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

Same slots, written in natural Chinese: 画面基调（镜头、焦段、景深、胶片颗粒、调色）→ 主体锁定 → 场景与光线 → 表演时间线（含引号对白）→ 运镜 → 声音 → 收束状态. Use the Chinese columns of the pass files. Do not mix English jargon into a Chinese prompt unless the model is known to respond better to it.

## 10. Before delivery

Run `python scripts/lint_prompt.py prompt.txt`. Then confirm the coherence checklist in `lens/lens-layer.md` section 6, the length against the model's limit, and the one-line added-texture note.
