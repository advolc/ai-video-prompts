# Dialogue v3, Part 1: Spoken Register

`references/dialogue-engine.md` decides **what a line is for**: intent, subtext, speech act, power, language DNA. This file decides **how it is actually said**. v1's lines read as written aphorisms because real speech has a texture the engine never produced. A designed line is raw material; the spoken form is what goes into the prompt.

## 1. The over-tea test

Read every line aloud, imagining two people at a table. If it sounds like a fortune cookie, a proverb, or a screenplay line rather than something a person would say, convert it. Intent and subtext stay; the surface changes.

## 2. The features of real speech

| Feature | Example |
|---|---|
| False start and repair | "The shipment, it, uh, it didn't clear." |
| Filler and hedge | "Well, I mean...", "sort of", "I guess" |
| Trailing off | "If you'd just let me explain, then—" |
| Interruption | "But the—" |
| Overlap | Both start at once; one yields |
| Backchannel | "mm", "right", "go on" |
| Echo and repeat | Chen: "Tuesday." |
| Ellipsis and fragments | "Tuesday?" "Not yet." "Who says?" |
| Contractions and slang | "didn't", "gonna", "what's going on", "give it a rest" |
| Address terms | "Sir", "boss", "Director Chen", "master" |
| Register shift under stress | Formal turns clipped, or the reverse |
| Breath groups | Short bursts split by inhales, never one unbroken paragraph |
| Pauses | A pause is an action beat: a swallow, a cup lifting |
| Laughter, sighs | A short exhale through the nose, "heh", a dry laugh |
| Volume and pitch movement | Dropping to a murmur on the blunt sentence |

## 3. Calibrating disfluency to the character

Over-sprinkled fillers sound like a parody. Choose density from the **status ledger** (`lens/body-and-status.md`) and the **language DNA card** (`references/dialogue-engine.md` section 8):

- **High status, confident:** full sentences, few fillers, long silences, short echoes.
- **Low status, anxious:** hedges, fragments, restarts, trailing off, fast fill.
- **Under stress:** disfluency rises; formal speakers become clipped.
- **Deceiving:** over-precise detail or a suspiciously smooth delivery; a micro-pause before the key word.
- **Formal setting:** fewer fillers; more address terms.
- **Intimate setting:** fragments, shared shorthand, half-finished sentences understood by both.

Every filler or stammer needs a cause. Do not mock dialect or accent. If the character speaks a regional variety, give it through word choice and rhythm, not caricature spelling.

## 4. Length

v1 trimmed threats to about ten characters. v3 removes that target. Line length follows the **character and the situation**: a brusque boss may say five words; a nervous subordinate may need two run-on sentences. A conversation unit (`conversation-units.md`) holds several turns, not one line. Fit the lines to the clip's duration using the pace table there; if the speech will not fit, lengthen the clip request or split by unit, never silently trim the line.

## 5. Delivery tags

Write delivery as a short cue attached to the line, one or two per line, no stack:

| Dimension | Examples |
|---|---|
| Voice quality | low, dry, gravelly, breathy, thin, warm, flat |
| Pace | unhurried, clipped, rushed, halting |
| Volume | murmured, level, raised, swallowed |
| Pitch movement | falling at the end, rising on the question, flat |
| Breath | a short inhale first, an exhale through the nose after |
| Smile in the voice | a faint smile in the voice, a dry half-laugh |

Form: `Chen says, low and unhurried, "Tuesday."`. Keep it attached to a body beat (a swallow, a sip, a glance).

## 6. Converting v1 cards and designed lines

| Designed line (v1 style) | Spoken form | What changed |
|---|---|---|
| "The door isn't shut yet." | "Door's still open. ...Isn't it?" | Contraction, a breath, a tag question that deflects |
| "Button your coat. It's windy out." | "Button up. Wind's picked up, you'll—just button up." | Cut-off, repeat, care carried by the order |
| "I never said he was at the north gate." | "North gate? ...I never said north gate." | Echo, pause, the catch lands as a repeat |
| "Your tea has gone cold. Shall I have it changed, or is the person you're waiting for not coming?" | "Your tea's gone cold. I can have it changed. ...Or, well. Is he not coming?" | Soft menace through the pause and the polite offer |
| "You saved me half a bowl of porridge once. I thought it cold and didn't drink it." | "You saved me half a bowl of porridge once. Remember? ...I thought it'd gone cold. Couldn't drink it. Couldn't throw the bowl out, either." | Specific detail, hesitations, a trailing end |
| "Your sword once cut only falling leaves. At whom is it pointed today?" | "That sword of yours... it used to cut falling leaves. Today—who are you pointing it at?" | A pause, an echo, a colloquial question ending |

## 7. Subtext in speech

Say less than you mean. Answer the question behind the question. Change the subject at the sensitive point. Use the name or title as a weapon ("Mr. Wu." instead of "Wu."). Repeat the other's word back, flatly. Let a sentence fail at the critical word. Subtext is the Director's Room's job; the spoken line only carries its surface.

## 8. Two outputs, both first-class

1. **Native-dialogue prompt (default).** Lines go **inline** in the Extended prompt as quoted speech with delivery cues and body beats. When the platform has native speech, this is the render path. When it does not, the quotes still give the model mouth shapes and timing; whether lips sync is **model-specific**: check the actual model and input conditions (`models/README.md`, item 5). Never promise sync.
2. **Voice script** (outside the copy block): for post, TTS, or a voice actor.

```
Speaker | Line (spoken form) | Delivery | Pause before/after (s, estimated) | On/off camera
Chen | "Tuesday." | low, unhurried, falling | 0.8 before | on
```
Mark pauses and read-through status as estimates until someone has read them aloud. Never invent exact seconds you have not timed.

## 9. Language and names

Write the speech in the character's own language. In a mixed-language scene, keep each speaker's language consistent; add translation only in notes. Keep names and address terms identical across clips.

## 10. Negative checks

- No line that explains the audience's own experience ("As you can see, I am afraid").
- No wisdom aphorism unless the character is the kind of person who speaks in them, and then no more than one per scene.
- No whole plan narrated in one speech.
- No change to the user's locked lines. If the user's line is stilted, keep it and offer a spoken-form alternative as a candidate.
- No line stuffed into a clip where the body is mid-impact or breath-held; move it to a pause or a voice-over.

## 11. Register-sensitive review

Use the over-tea test as a naturalness check only where conversational realism is intended. Ritual, period, poetic and stylized speech may be formal and polished. Preserve established character voice and exact user lines. Fillers, fragments and stammers need a scene-specific cause; they are not universal evidence of natural dialogue.
