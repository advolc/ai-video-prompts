# Quality and Regression (Consolidated)

Combines review scoring, controlled comparisons, and regression checks. See [evals/cases.md](../evals/cases.md) for v3 empirical evaluations.

## Review and scoring on request

**Use only when the user explicitly requests review/scoring; never score automatically.** In the editor role, point out requested problems directly without forcing a numerical table. "Not cool enough" is an ordinary revision, not a trigger for a full-library judgment. Score only accessible material; mark unseen/unheard dimensions unassessed, not zero.

The four 1–5 scales are this repository's review convention, not objective certification:

| Dimension | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Visual | Subject/contact difficult to distinguish | Multiple light/color/space conflicts | Main information readable, with local drift | Stable signatures and hierarchy | Visible choices consistently and economically serve intent |
| Narrative | Goal/causality does not work | Key trigger or result missing | Goal and change can be retold | Clear information/reaction rhythm | Choices, costs, and aftermath form a distinct expression |
| Sound | Sync/clarity seriously obstructs understanding | Multiple masking problems or abrupt changes | Dialogue and key events audible | Stable layers/space and breathing room | Audiovisual division of labor consistently adds narrative information |
| Technical | File/playback unusable | Severe flicker, wrong frames, or specifications | Usable with local flaws | Encoding/subtitles/continuity meet this task's requirements | Complete delivery checklist, each item actually rechecked |

An optional originality/personal-signature dimension is for discussion only, not automatic judgment: 1, generic phrasing only; 2, a few personal terms buried by templates; 3, distinct choices can be located; 4, choices run through form and content; 5, multiple mutually supporting personal expressions. Scores do not establish absence of plagiarism or legal originality; discuss actual sources.

An overall score cannot cancel a critical failure in one dimension. Identity, contact, permissions, file usability, and other hard goals retain their original acceptance criteria. Templates and style cards diagnose gaps, not impose a mold; before output, ask whether only the template remains and the user's own material has vanished. See [interaction rules](../ux/interaction.md) for everyday boundaries.

## Controlled comparisons

Create two prompt or generation versions with the same intent. Freeze characters, scene, outcome, duration, and references, preferably changing only one main variable. Record noise when real randomness cannot be fixed; a single difference does not prove causation.

Define acceptance first, such as "retreat begins after shaft and blade cross." A retains the original; B changes only contact wording or camera position. Inspect continuous footage over the same range, recording the earliest difference and failures. If model/assets/runtime all change, list confounders rather than claiming to identify an effective word.

Record: `Intent | Sole variable | Shared conditions | A input/settings/output | B input/settings/output | Observable results | Limits | Choice rationale`. Cover/title tests separately record exposure source, audience, and interval; click-through rate is not work quality. Stop within the user's budget; do not automatically buy a larger sample. Expand quality judgments through [scoring](quality.md) only on explicit review requests; locate failures through the [AI pipeline](../references/ai-pipeline.md).

## Change regression and release checks

After changing a target module, inspect its callers and dependencies, then run structural, data, script, and behavioral walkthroughs. Keep evidence types independent: static checks do not establish model behavior or generation success. Rule tests should catch real conflicts, not merely count keywords.

- Core: retain Tier A event budgets and directorial causality, the six seam categories, separation of generation/control/management, Lens depth, and default self-contained plain prose.
- Files: SKILL.md frontmatter/link targets/file reachability (`scripts/check_skill.py`); no private absolute paths or discarded test drafts in the package.
- Tools: eight-dimensional draws, chosen subclasses, no repeats across historical batches; prompt lint and spatial diagnostics cover valid ordinary language, quoted speech, malformed ledgers and actual per-character changes.
- Interaction: brief directions for ambiguous input; classify references first; no rerouting for small edits; stop when told; role switching; trace back to confirmed versions; score only on explicit review requests.
- Delivery: no G labels or slate notes in final input; self-contained anchors and intact causality; do not withhold complete text, and do not equate internal units with generation counts.
- Release: reconcile file manifests and ZIP integrity, state document-validation and pilot scope, and never upload without authorization.

When a change fails, repair its corresponding batch first rather than rewriting protected parsers. Run [scripts/check_skill.py](../scripts/check_skill.py) for static structure and [scripts/lint_prompt.py](../scripts/lint_prompt.py) for final prompts. Scripts do not simulate human creative understanding; retain actual outputs and limitations for the eight-scenario walkthrough.

### Behavioral cases for creative confirmation and delegated scope

These are validation cases and expected behavior, not completed independent-model test records. Save actual inputs, outputs, and observations, distinguishing rule walkthroughs from independent behavioral validation.

| Input or situation | Expected behavior |
|---|---|
| Only "this visual style, a 30-second fight" | First understand the content idea; do not directly produce a complete plot and prompt |
| Only answers "original swordsman, Seedance" | Update only those two items; plot, setting, and ending remain undecided |
| Borrow only cool-gray grading | Do not inherit the reference's rainy alley, characters, or golden magic |
| Story undecided, model unknown | Handle the creative gap first; "platform draft" does not authorize designing everything |
| "Choose the setting for me" | Propose or draft the setting without extending scope to the whole film's winner |
| Says the previous version was entirely unapproved decisions | Undo unconfirmed decisions and restore the last confirmed state |
| After seeing an outline, says "give me everything based on this" | Treat the current outline as confirmed and deliver all of it without asking again |
| Supplies an existing fight draft and asks for prompts | Preserve core facts, translate visible causality, and deliver directly without a new creative questionnaire |
| Wants only one sentence of inspiration | Give brief Compact candidates; do not require a full plot or outline confirmation |
| "Design the plot, setting, and fight yourself; give me the full draft directly" | Draft within explicit authorization and known constraints without repeated confirmation; creative authority does not authorize paid generation or publishing |

### Behavioral regression for contextual refinements

- An established dialogue scene has a cup and cold weather: refine suitable nonessential grip behavior with a stimulus and readable hand use. New shots do not justify repetitive fidgeting, and no cup is forced into a scene without one; there is no fixed one-gesture allowance.
- Basic contextual treatment does not ask about texture or automatically append module/promotional explanations. New scope such as full character/setting design still follows existing authorization rules.
- An established metal-weapon rain fight: force and a very few existing droplets arise from actual contact. Add no sparks, shockwaves, or second explosion without material/ability sources.
- Sand in eyes or a rain-induced fall that changes the situation is not a silent free addition; if used, it belongs to the original event and carries state. Default candidates may simply be discarded.
- Subjective photography has one main task per shot, not simultaneous shake, hunting focus, push/pull zoom, and blood-obscured contact. With unknown native sound, prose does not claim precise tinnitus mixing is controllable.
- Do not force everyday gestures, wear, or dirty-lens effects when the user specifies stillness, minimalism, or clean assets. Silent polishing preserves the user's creative boundaries and protected targets.
These are prospective behavioral criteria, not independent-model test results. Structural and script verification still follows the original checklist.
