# Pass 4: The Face

This pass gives faces anatomical, layered, believable behavior. It is **performance for fictional characters**, not a diagnostic tool: a muscle pattern does not prove an inner state, and nothing here reads a real person's psychology. Terms are **confirm per model**; fine facial control varies a lot between models and shot sizes, so the pass includes fallbacks.

The Director's Room decides *what the character is hiding or showing* (`references/performance-and-psychology.md`). This pass decides *what the face visibly does*.

## 1. The layers of a face

Write expression as layers, from the most readable to the finest:

1. **Gaze:** where the eyes go, how long, how they leave. The strongest signal.
2. **Eyelids and brows:** lids lift, narrow, or lower; brows draw, lift, or tilt.
3. **Cheeks and nose:** cheeks lift, the nose wrinkles, the nostrils flare.
4. **Mouth and jaw:** lips press, part, tighten, pull; the jaw sets or loosens; the chin boss rises.
5. **Skin and breath:** flush, a swallow, a pulse, a shallow breath, a blink.
6. **Timing:** how fast it appears, how long it holds, whether it is masked.

## 2. Muscle-informed lexicon (FACS-based, rendered as what you can see)

Action units (AUs) come from the Facial Action Coding System. The prompt carries the **visible effect**, never the AU number or muscle name. The muscle column is for the Director's Room.

| AU | Muscle (design only) | Visible effect | 中文写法 |
|---|---|---|---|
| 1 | Frontalis, medial | Inner brows lift; a small tent of skin above the nose | 眉头上提，眉心微微隆起 |
| 2 | Frontalis, lateral | Outer brows arch | 眉尾上扬 |
| 4 | Corrugator, procerus | Brows pull together and down; vertical lines between them | 双眉下压并拢，眉间出现竖纹 |
| 5 | Levator palpebrae | Upper lids lift, more white shows above the iris | 上眼睑抬起，虹膜上方露出眼白 |
| 6 | Orbicularis oculi, outer | Cheeks rise, skin beside the eyes crinkles, eyes narrow slightly | 脸颊上抬，眼角起褶 |
| 7 | Orbicularis oculi, inner | Lids tighten, a hard narrowed look | 下眼睑绷紧，目光变硬 |
| 9 | Levator labii superioris alaeque nasi | Nose wrinkles, upper lip lifts | 鼻梁起皱，上唇上提 |
| 10 | Levator labii superioris | Upper lip raises, teeth edge shows | 上唇抬起，露出上齿边缘 |
| 12 | Zygomaticus major | Mouth corners pull up and back | 嘴角上扬并向后 |
| 14 | Buccinator | Corners tighten into a small dimple | 嘴角收紧，起一个小窝 |
| 15 | Depressor anguli oris | Mouth corners pull down | 嘴角下压 |
| 17 | Mentalis | Chin pushes up, lower lip lifts, a dimpled chin | 下巴上顶，下唇上抬，下巴皮肤起窝 |
| 20 | Risorius | Lips stretch sideways | 嘴唇向两侧拉平 |
| 23 / 24 | Orbicularis oris | Lips tighten and press into a thin line | 嘴唇收紧，抿成一线 |
| 25 / 26 / 27 | Jaw and lip muscles | Lips part, jaw drops slightly or wide | 双唇微分，下颌微落或大张 |
| 43 / 45 | Orbicularis oculi | Eyes close; a blink | 闭眼；眨眼 |

Unilateral movement (one side only) reads as contempt or irony. Asymmetry is a feature: real expressions are rarely mirrored.

## 3. Reference combinations (design aids, not rules)

The following AU combinations are widely cited associations in the facial-coding literature. Use them to choose a **visible** pattern. They are not proofs, and characters differ; masked or mixed expressions are normal.

| Display | Combination | Rendered as |
|---|---|---|
| Genuine smile | 6 + 12 | The mouth lifts and the skin beside the eyes crinkles |
| Polite smile | 12 without 6 | The mouth lifts; the eyes stay still |
| Sadness | 1 + 4 + 15, often 17 | Inner brows lift and draw; mouth corners down; chin tightens |
| Anger | 4 + 5 + 7 + 23 | Brows lowered and drawn; eyes hard and staring; lips pressed |
| Fear | 1 + 2 + 4 + 5 + 20 (+26) | Brows raised and drawn; upper lids wide; lips stretched back |
| Surprise | 1 + 2 + 5 + 26 | Brows arched; eyes wide; jaw dropped |
| Disgust | 9 / 10 + 15 + 17 | Nose wrinkles; upper lip lifts; chin pushes up |
| Contempt | One-sided 12 (+14) | One corner tightens and lifts |
| Concentration | 4 + 7, steady gaze | Brows slightly lowered, lids narrowed, stillness |
| Pain | 4 + 6 + 7 + 9 + 43 | Brows drawn, lids squeezed, nose wrinkled |

## 4. Micro-expressions and masking

Micro-expressions are brief, often described as lasting well under half a second, and the research on how reliably people read them is mixed. Treat them as a **performance device**.

- Write them as a **flicker followed by recovery**: "for an instant his brows draw and his lips thin, then his face smooths into a patient blank."
- Use a **mask** (the face the character wants to show) over a **leak** (what slips): a polite smile held while the throat swallows; a calm voice while the jaw sets.
- A leak is a small, specific thing. How many a face can hold depends on context: a calm public mask holds one; high arousal, exhaustion, or high stakes make the mask fail in more channels (section 10), but always in an order the viewer can follow, never all at once.
- Fast action and fine micro-expression do not share a moment. Put the flicker in a pause, a listening beat, or a close-up.

## 5. Gaze and eyes

- **Direction and target:** the eyes go to something specific (the other man's hands, the door, the cup), and the shot size must be able to show it.
- **Leaving:** a glance away is information (avoidance, calculation, shame). Write where the eyes land: "his eyes drop to the cup, then return."
- **Blink and moisture:** blinks slow when still and watchful, quicken under stress; a wet rim signals held tears.
- **Steadiness:** a long unblinking gaze is a power move; a darting gaze reads uneasy.
- **Eye-line:** the two people's eye-lines meet, miss, or cross, and the framing keeps that readable.
- Give the eyes a **catchlight** (`physical-light.md` section 5).

## 6. Breath, throat, and skin

A face lives through the throat and breath: a swallow before a hard sentence, a short inhale before speaking, a held breath, a long exhale through the nose. Flush rises along the neck; a pulse shows at the throat. These are Tier B beats and carry no plot.

## 7. Fallbacks (when the model cannot render fine detail)

Order of fallback, from the finest to the broadest: micro-expression → gaze and brow → head and shoulder turn → hand action → distance and position. Choose the first step the shot size can carry. In wide shots, drop face language and let posture and distance carry the beat. If the user demanded a specific face target in a complex fight, **offer options and wait** (separate reaction shot, low-motion close-up, test the long take) before replacing it.

## 8. Writing it into the prompt

- Fold face behavior into the action sentence; never list fields.
- One main face beat per spoken or silent beat; the rest of the face stays still.
- Pair every face change with its **cause** (the line just spoken, a sound, the other person's movement) in time order.
- Avoid labels such as "devilish smile", "pupils quaking", "veins bulging", "lips curl into a sneer" as the only information; unpack them into what moves.

## 9. Examples

- *Contempt and mask:* "As Wu stumbles over the word 'customs', one corner of Chen's mouth tightens and lifts for an instant; his eyes stay half-lidded and still, and the patient blank returns before Wu finishes."
- *Held fear:* "Lin's upper lids lift a hair; she keeps her lips pressed in a thin line and swallows once, her pulse ticking at her throat."
- *Genuine vs polite smile:* "She smiles, the corners lifting, but the skin beside her eyes stays smooth." (polite) vs "...and fine lines gather at the corners of her eyes." (genuine)
- *中文：* "听到那个名字，他眉头微微下压，嘴唇抿成一线，喉结滚了一下，随即眼神平平地移开，落在窗外的雪上。"

## 10. Display rules: who is watching

People manage their faces by context. The same news looks different in a closed car and in a courtroom corridor. Route the face by **audience, relationship, arousal, fatigue, and stakes** (`core/context-routing.md`).

| Context | Mask | Where the leak shows | Recovery | Notes |
|---|---|---|---|---|
| Private, intimate | Low or none | Everywhere; large, unguarded expressions, crying, laughter | Slow | The mask is lowered; closeness allows big expressions |
| Semi-public (colleagues, neighbors) | A professional or social mask | Eyes, hands, voice, breath; small | Moderate | The courtesy smile or flat politeness holds, with a lag |
| Public with an audience (court, ceremony, crowd) | Strong; flat or composed | Jaw, throat, hands, posture; the face stays disciplined | Fast | Wider shots let the body carry it; close shots catch the tight margins |
| Under authority or threat | Deferential or blank | Brows and mouth for an instant, masked at once | Very fast | Gaze lowered; compliance on the surface |
| Among enemies | Stoic composure; contempt may show | Controlled; a flicker of satisfaction or fear | Fast | The mask is a weapon |
| Performing a deception | Over-smooth | The leak is **timing** (a late smile, a too-long pause), not intensity | Moderate | A smooth face can be the tell |

**Modifiers.**
- **Arousal and exhaustion** reduce masking capacity: leaks appear in more channels and recovery slows. A worn face is slack, with heavy lids and slower expression changes.
- **Stakes** scale expression: low stakes, small expressions; high stakes, larger ones or harder suppression.
- **Public and private versions of the same beat:** write the public mask first, then the private after-beat when the door closes (the face drops, the breath breaks). The after-beat suits a close shot.
- **Culture and era:** display rules differ across cultures and periods (whether grief or anger is shown in public, how contempt is signalled). Do not assume. Pick what fits the established world and label the assumption outside the copy block.
- **Do not invent a mask where none is motivated.** If nobody is watching and nothing is at stake, let the face move.

Shot size routing still applies (section 7): a public mask suits wider shots where the body does the work; a private leak suits a close-up.
