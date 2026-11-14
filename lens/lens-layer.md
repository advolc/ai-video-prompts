# The Lens Layer: from design to depiction

A video model does not read your reasoning. It reads a description and renders what the description makes it picture. So the final text must be **what a camera and microphone would record, in time order**, and nothing else. The Director's Room's depth survives by being converted into things you can see and hear.

Test for every sentence: *could a camera operator film this, or a sound recordist capture it?* If not, rewrite it or delete it.

## 1. The depiction grammar

| Do not write | Why it fails | Write instead |
|---|---|---|
| Conditionals and constraints: "only after the palm lands, the shoulders lean away", "must not slide", "should look worn" | Logic, not image. Reads as a specification | A time-ordered statement: "the palm lands; his shoulders and back lean away" |
| Negations: "no flash", "without shaking", "does not step forward" | Models often render the negated thing | State what is there: "the camera holds steady", "he stays planted where he stands" |
| Purpose or explanation: "to show dominance", "because he is nervous", "so the audience sees" | Not recordable | Show the cause as behavior: "his thumbnail picks at the cup's rim" |
| Theory and craft words: subtext, tension, power dynamic, vulnerability, micro-expression, motif, seam, beat | Analytical notes, not images | The body fact the word stands for |
| Emotion labels as the only information: "angry", "devastated", "nervous" | The model draws a stock face | Physical signs: jaw set, breath short, eyes fixed on the other's hands |
| Production scaffolding: clip IDs, time ranges, "must-do", "ambient", "same as previous", "see above" | Leaks the pipeline | Fold the needed carry-over into the visible present: left/right, posture, hand position |
| Empty evaluatives: stunning, epic, masterpiece, flawless, perfect, gorgeous, ultra-detailed, 8K | Adds nothing, and flawless/perfect pull toward the smooth plastic look (a hypothesis to test per model) | Specific material, light, and imperfection |
| Ambiguous pronouns when two similar people are present | The model swaps them | Name or re-describe: "Chen", "the younger man" |
| Stacked synonyms | Dilutes | One strong word |

**Temporal connectives are allowed and encouraged** (as, then, while, a beat later, just before, when X lands, Y). They carry order without turning into a rule. "When the palm lands" is a moment; "only after the palm lands do" is a constraint.

## 2. Sentence craft

- Present tense. Concrete verbs: press, tilt, settle, pinch, drift, set down.
- One sentence is one visual moment, or two tightly coupled ones. Long sentences are for continuous flow (a pan, a breath). Short sentences are for contact and decisions.
- Inside a sentence, order: subject → action → body part or object → what the light or camera does with it.
- A recurring subject keeps one stable descriptor ("Chen", "the white-haired man"). Repeat identity anchors when the subject changes or the shot cuts; do not repeat them every sentence otherwise.
- Pause and silence are written as action: "He lets the question sit; the lid of the cup ticks against porcelain." Never "(pause)".
- Put the most important image early in its sentence.

## 3. Using cinematography vocabulary

Models trained on captioned footage tend to know the words cinematographers and photographers use: focal lengths, depth of field, rim light, key light, handheld, Steadicam, film grain, halation, anamorphic. This is a testable belief, not a verified fact, so every term in the pass files is marked "confirm per model" until you test it.

Rules:
1. Cinematography terms go in the **Look anchor** and the **camera sentences**. Descriptive depiction does the rest.
2. Use a term only if the shot size and situation can show it. (A "50 mm shallow depth of field" tells the model nothing useful in a drone-height wide.)
3. One coherent look: one focal family, one stock/grade, one light logic. See the coherence checklist below.
4. A term plus a depiction beats a term alone: "rim light" plus "a thin orange edge on his hair and the shoulder of his coat".
5. Never write jargon as a command to the model ("set aperture to f/1.8"). Write what the image looks like.

## 4. How design vocabulary becomes depiction (examples)

| Director's note (internal) | Execution (prompt) |
|---|---|
| Superior asserts dominance by calm listening while the subordinate explains; the power gap shows in posture | Chen sits far back in the leather armchair, right ankle over left knee, a cup balanced on his knee. Wu perches on the front third of his chair, palms flat on his thighs, swallowing before each sentence. |
| She conceals the wound; subtext is that she cannot afford to be seen hurt | Her left hand slides deeper into the sleeve while her right keeps the staff planted on the threshold; her breath stays shallow and level. |
| He is afraid but protective | His rear foot gives half a pace; his forearm stays across the child's chest. |
| The strike must not launch the opponent before contact | The palm heel touches the chest; then the white-clad man's shoulders and back lean away and both boots slide back across the ice, scraping two pale lines. |
| Micro-expression of contempt, brief | For a flicker, one corner of his mouth tightens and lifts; then his face returns to a blank, patient look. |
| 他强压怒火 (suppressed fury) | 他下颌的肌肉绷紧又缓缓松开，指节在杯壁上泛白，视线仍落在对方的手上。 |
| 对峙，气氛紧张 (tense standoff) | 两人隔一步站立，雪片落在两人之间；他握剑的拇指在护手上来回压了一下，对面的人没有眨眼。 |

## 5. From design record to prompt: the procedure

1. **Freeze the facts.** List locked facts and user demands (identity, weapon, outcome, named moves, lines, face targets).
2. **Write the beat timeline.** For dialogue or silent interaction, carry the already-designed [unit spatial spine](../dialogue/spatial-blocking.md): cue, path or concrete hold, listener response, resulting relation. Keep body movement in world space distinct from camera movement. Then write time-ordered visible events across all characters, with Tier A events marked. Use the design record's status shifts, subtext, and speech acts as the *reason* for each beat, but write only the beat.
3. **Convert each beat to a recordable statement** using section 1. Replace every emotion and theory word with its physical proxy (`face-pass.md`, `body-and-status.md`).
4. **Run the five passes** (Extended default): optics, light, skin and material, face, body. Each pass adds only what the shot size can show and what is consistent with locked facts.
5. **Order into the skeleton** (`output-skeletons.md`).
6. **Check coherence** (section 6).
7. **Lint** with `scripts/lint_prompt.py`. Fix flags; the linter finds patterns, not meaning.
8. **Write the one-line added-texture note** and any assumptions outside the copy block.

## 6. Coherence checklist (run before delivery)

- One lens family per shot. If two focal looks are needed, they are two shots.
- One stock/grade and one grain level.
- One light logic: sources, direction, color temperature agree; light on the face matches the practical sources named. Time of day matches the window.
- Weather, wind direction, and cloth movement agree.
- Objects: one state at a time (the cup is full, then lighter after the sip; not both).
- Identity anchors do not contradict the locked look or earlier clips.
- Hands and limbs: no two actions on the same limb at once.
- Dialogue: the unit spatial choice is depicted; its path or meaningful hold, counterpart response and resulting anchors are readable. Cuts do not reset positions, and hand business does not replace the macro decision.
- Speech: line lengths fit the shot duration (`dialogue/conversation-units.md`).
- No sentence exists only to sound cinematic.
- Nothing in the prompt names a design concept, a module, a card, or a pass.

## 7. Positive rewrites of design constraints

Design notes often say what must not happen. Convert each to the visible condition that makes it true, preserving the object and the stage:

| Constraint | Visible condition |
|---|---|
| No foot sliding | His boots alternate on the ice, the soles biting before each step |
| The flower core must not be solid | Six curved petals enclose a clearly hollow center |
| No hit flash on a miss | The spearpoint passes the empty space where his chest was, and nothing sparks |
| Face must stay readable | Soft light from the left holds both eyes and the mouth clear throughout |
| Weapon stays in the same hand | His right hand keeps the hilt from the first frame to the last |

When a negation is the clearest way to keep a rare, high-risk artifact out, it may go in a platform's negative-prompt field if that field exists and is verified. It does not go in the body.

## 8. What the Lens never does

- It never adds Tier A events (a new strike, block, fall, or reveal).
- It never changes locked facts to fit richer text.
- It never explains itself in the prompt.
- It never pads. Length is earned by distinct, recordable information.

## 9. Writing movement in space

Fighters move through three dimensions, and the prompt has to say how (`references/spatial-tactics.md`).

- A **path sentence** has three parts: where from (a landmark or an opponent-relative direction), what shape (arc, slip, pass, drop, spring, push-off), where to (a landmark or a relationship to the opponent).
- Prefer opponent-relative and landmark terms: "outside the right blade", "behind his shoulder", "around the boulder", "up the rock step", "with the sun behind him".
- Level changes are depicted, not named: "drops under the sweep and rolls to one knee", "springs onto the low rock, a full pace above him".
- A prompt in which most movement is "steps in", "steps back", "retreats half a step" keeps the fight on one line. `lint_prompt.py` warns on this pattern.
- Camera axis variety is part of the depiction: a fight filmed only in side profile looks linear whatever the ledger says.
