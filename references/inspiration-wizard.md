# Guided Inspiration Incubation

Serve users who have “no inspiration,” “only one word/one image,” or “two ideas they have not chosen between.” Use the vocabulary library and small questions to help ideas grow; do not present a complete plot, storyboard, or prompt in the first round. Users with a clear plan go directly to design/production, without being forced through the wizard again.

Length figures stated in Chinese characters describe the Chinese version's brevity, not a required output language. In another requested language, use comparably concise wording while retaining the same fields.

## Mandatory Preliminary Confirmation (Prevent Scope Reduction and Drift)

When the user says “make a film/feature/series/short film,” or gives only a broad request such as “make a period-style/science-fiction story,” do not immediately generate scene tags, default to a fight/confrontation, or reduce it to one generation segment without authorization. Confirm project scale and broad story category first; this section precedes card drawing, scene recommendations, and generic story-direction menus below.

1. **Confirm scale (prevent scope reduction):** When scale is undecided, first ask: “Is this a complete film/series project, or do you want to test one scene first? If you want to build from scratch, we'll follow preproduction from worldbuilding to characters to outline; if you already have a storyline, we can choose one scene to test.” An existing storyline does not automatically authorize single-scene-only work; the user may still choose full-project planning.
2. **Confirm broad category (prevent drift):** When only background information such as period style or science fiction is available, ask whether they prefer dialogue-driven drama, suspense, political intrigue, everyday life, or another category of their own. Do not narrow period style to drawing swords for revenge or settling scores, or make science fiction automatically mean mecha combat. Do not ask again about an already explicit genre.

Reuse scale, genre, and storyline established earlier, in attachments, or in the current turn; ask only about missing items that would change direction. If both categories remain undecided, ask about scale first and story category in the next round; one question per round, without a long form. If the user explicitly wants only one scene/one inspiration line/a direct trial, follow that scope rather than forcing construction of an entire world. Before confirming a broad request, do not ask about the video platform or produce a five-second draft. If the user chooses whole-film preproduction, organize world rules, characters, and outline first, then select a scene.

Before exploration, you must execute the [Dimension-by-Dimension Assembly Protocol](../ux/interaction.md): by default, one dimension per round in the order world → space → relationship → spectacle/core action. This page retains state and delivery details; do not use old nonlinear descriptions to bypass the order or assemble packages. When the user explicitly changes the workflow, follow the protocol's exceptions.

## Core Interaction Principles

**Strictly distinguish what has been confirmed:** Selecting a character category confirms only that category; selecting a platform confirms only the tool. The AI must not treat creative settings still unconfirmed as approved defaults simply because the user answered other questions.

### 1. State Snapshot

Maintain five core slots backstage within the conversation. Do not ask the user to fill a form, automatically write to long-term memory, or claim to have created an external database:

| Slot | Recorded content | Relevant dependencies |
|---|---|---|
| World | Era/technology and ability rules; mood and visual style may be supplementary descriptions | Weapons, materials, architecture, and ability sources |
| Space | Location, scale, support, retreat routes, and height differences | Effective distance, movement, attack range, consequences of destruction |
| Relationship | Who relates to whom, protection/contested target, motives, and intended situation | Degree of force, attack/defense choices, and ending |
| Spectacle | Weapon/spell appearance, environmental interaction, recognizable memorable beat | Shape consistency, cost, contact/destruction rules |
| Core action | One principal attack/defense and response/outcome, prioritizing clearly readable bodily action | Weapon length, space, support, and momentum |

Attach a source (explicit user choice/AI candidate), status (undecided/candidate/settled/pending review), and branch to every value. Preserve the user's words first; do not assume AI suggestions are user selections. Record target duration, tool information, and delivery preferences separately; they cannot displace the five slots.

In wizard mode, end every reply with a roughly 50-Chinese-character briefing of all five slots; mark undecided items honestly, without adding settings to fill length. With multiple branches, compress using A/B labels while preserving each branch's full values backstage. If the mode continues after prompt delivery, keep attaching snapshots outside the generation body/copyable block as management information. Stop attaching them after the user exits this mode; skill-maintenance conversations do not count as entering incubation.

Briefing form: `Status: World…; Space…; Relationship…; Spectacle…; Action….` If an upstream change remains unresolved, mark related values “pending review,” never still “settled.”

Also record within the conversation the active branch, current focus slot, outline version and each branch's confirmed version, pending linked changes, generation conditions, and text-delivery preference. These are interaction-control state, not a sixth creative slot, and are not displayed individually. State transitions are:

| Current state | Trigger and transition |
|---|---|
| Exploration | First assign all user-provided information to slots, then handle the earliest undecided item under the dimension-by-dimension protocol; four dimensions handled or explicit user request to skip to a proposal → validation |
| Validation | A contradiction affects the principal action → return to the relevant slot; viable → roughly 100-Chinese-character outline and awaiting confirmation |
| Awaiting confirmation | User modifies → update affected branches and validate; user confirms current version → generation handoff; no response never self-approves |
| Generation handoff | Complete platform conditions and unknown delivery preferences; do not re-ask known information; conditions ready or user explicitly chooses a generic assumption-based draft → deliver according to preference |
| Delivery/diagnosis | Deliver all text at once, or deliver in batches awaiting test feedback; failure → local AI-pipeline diagnosis; user switches to all-at-once → deliver the remainder |
| Any state | User overturns a setting → mark ripple effects, invalidate old-outline confirmation for related branches, then revalidate; unaffected branches and slots remain intact |

The state machine records changes and recovery; it does not authorize the AI to skip the default four-dimension order. Do not re-ask settled items; skip only within the scope of an explicit user workflow change. When the user explicitly exits or switches to direct production with an existing plan, end the wizard while preserving established information.

### 2. State Recovery and User-Directed Skips/Branches

The default four-dimension order follows the [Dimension-by-Dimension Assembly Protocol](../ux/interaction.md). Record all information the user volunteers across slots, then handle only the earliest undecided dimension; do not jump across slots to present packages because the model has an idea. Switch only when the user explicitly asks to discuss a dimension first, skip a step, or receive a complete plan directly. Follow the latest explicit intention while preserving undecided status and sources.

Two locations may coexist as current space branches without attaching two sets of characters/plots. If the user says only “show me both,” first provide a short comparison within the current dimension; deliver cross-dimension plans only when they explicitly request “two complete stories.” After selecting or merging branches, archive unselected values rather than silently rewriting settled slots. When an upstream premise is overturned, revisit affected items, then resume from the earliest currently undecided dimension instead of repeating the whole questionnaire.

### 3. Traceable Changes and Ripple Effects

When the user changes an upstream setting, record old and new values, mark related downstream items pending review, and proactively ask whether to adjust them together. Do not automatically clear the whole plan or replace weapons/characters. Common dependencies: world → weapons/materials/location/ability sources; space → weapon length/action radius/blast radius/retreat route; relationship → attack/defense objective and injury outcome; spectacle → force generation/support and core action.

For example, “change modern urban to Eastern fantasy”: update the world; the existing submachine gun, steel elevator, and glass curtain wall become pending-review items. Offer A: change to magical implements and mechanical architecture; B: retain an explained hybrid world; C: change only visual materials first; or accept a custom choice. Proactively ask whether weapons, materials, and locations should change too. Do not treat “ancient settings cannot have guns” as a universal ban; if the user selects a hybrid setting, establish the ability/technology source.

Before the synchronization scope is confirmed, continue exploring unaffected slots such as motives, but do not write pending-review content as an approved final draft. When a confirmed outline changes, reassess only affected portions and update the roughly 100-Chinese-character outline if necessary, without interrogating the user from scratch.

### 4. Stay Open; Do Not Force a Binary Choice

Every set of options must include the open invitation: **“You can choose any item in this batch, or simply tell me whatever word springs to mind—I can work with it.”** Label drawn cards A–E or A–F according to the actual batch size; A/B/C must not imply only three options. Options are stepping stones for inspiration, not limits. Even with only two existing branches, retain “keep both/customize.” When using a question tool, retain free input; its options are not the only legitimate answers.

After a custom response, briefly extract the core elements and assign slots, then ask a concrete question about the next dimension. Do not require free text to be resubmitted as a numbered choice. If the user says “I don't know any of it,” switch to more specific sensory images, still drafting 5–6 per batch; if they actively request fewer, follow that preference without blame or repeating the same questionnaire. If the user authorizes “decide for me/design everything,” select and report only one dimension each round under the dimension-by-dimension protocol. Delegated choice is not authorization to dump a finished product, and silence is not consent. If they also explicitly request skipping exploration and drafting directly, follow the exception.

## Five-Step Wizard Convergence Flow

A typical round uses “receive the user's words → randomly curate 5–6 items → one open question with new-batch/free-input invitations → end-of-reply five-slot snapshot.” Do not request the entire project card, platform parameters, or budget in the opening round; first help the user grasp an image they want to make. Read the dedicated [Large Inspiration Library](inspiration-library.md) by dimension and category, without dumping the entire table or preloading characters and spells from existing examples.

### Card-Draw Presentation and Unlimited New Batches

1. **Show only the tip of the iceberg.** Whenever an inspiration menu is needed for world, space, relationship, or spectacle/core action, show only 5–6 items from the current dimension. Do not show a batch from each of the four dimensions in one round, much less all 270 items. During validation or repair of linked settings, ask only necessary questions; do not add irrelevant menus to meet a card count.
2. **Random and diverse.** Draw randomly across categories within the corresponding dimension, spanning categories and image types where possible, from realism to exaggeration. If the user specifies a category, choose different tags within it rather than forcing other styles. Retain “tag + one image sentence” for each item. Filter incompatible cards against settled slots without silently changing the user's world or weapon rules.
3. **Every batch needs a new-batch invitation.** After presentation, explicitly say: **“This is only the tip of the iceberg. If these don't feel right, say ‘another batch’ and I'll show you other types.”** Also retain: **“If a better word comes to mind, just tell me.”** End with the roughly 50-Chinese-character five-slot snapshot; the open invitation is not a compulsory multiple-choice question.
4. **Unlimited batches, not unlimited repetition.** Record dimensions, active branch, shown tags, and latest batch backstage. “Another batch” replaces only the current menu, without clearing settled slots, automatically advancing, or recording unselected candidates as settings. Prefer unseen items, then avoid the immediately preceding batch when rotating. There is no batch-change limit; do not pressure an unsatisfied user to choose one.
5. **Respond immediately to a specified category.** “Anything period-style?” immediately draws from Traditional Eastern/Cultivation; “I want science fiction” immediately draws from Cyberpunk/Future Science Fiction. Space, relationship, and action can likewise filter by category. If the original world is locked, present the batch as candidates first rather than automatically rewriting it. Use context to distinguish a menu change from a setting change; if unclear, show the batch and add one scope question, then apply ripple handling if settings really change.
6. **Rotate a finite library honestly.** The fixed vocabulary library contains only 270 items; a category of 10 cannot supply six perpetually new items. When too few unseen items remain, mix new and old and disclose revisiting. After the whole category has been seen, rotate old items, change categories, or derive live from user words. Label derived items “new combination,” rather than claiming infinitely many unseen library entries. Tags within each batch never repeat.
7. **Card drawing does not alter the delivery decision.** Once the user selects within a dimension, stop automatically refreshing that dimension. In the next round, handle the earliest undecided dimension in sequence. Only after all four dimensions have been handled individually proceed to logic validation, outline confirmation, and advanced generation handoff. Explicit requests to skip exploration and receive a complete plan follow the exception. Reuse known all-at-once/batched preferences.

For actual random drawing, use the bundled [scripts/draw_inspiration.py](../scripts/draw_inspiration.py), which draws across categories using a standard-library random source. It supports dimension, specified category, batches of 5/6, and optional session history. History files belong only in the project's work directory; never rewrite the vocabulary library or long-term memory. Without history, cross-round deduplication is not guaranteed by default; the wizard should pass the same session history or maintain shown tags itself. Multiple branches may each use a separate history; switching branches must not confuse settled slots.

```text
python -X utf8 ai-video-prompts/scripts/draw_inspiration.py --dimension world --count 6 --history work/inspiration-draws.json
python -X utf8 ai-video-prompts/scripts/draw_inspiration.py --dimension world --category "Traditional Eastern/Cultivation" --count 6 --history work/inspiration-draws.json
```

Run these commands from the project parent containing the ai-video-prompts directory, creating project work first. If the skill is installed elsewhere, use the real absolute script path; history stays in project work, never inside the skill directory. Dimension parameters correspond to: world = world, space = space, relation = relationship, action = spectacle and action, blind = blind mix. Use `--exclude-tags` to exclude tags conflicting with established settings before drawing. Reuse counts and candidate-pool status returned by the tool are for backstage use; do not dump the full history after the user menu. If the tool is unavailable, select cards under the same diverse-rotation rules without pretending the random script ran.

### 1. World and Visual Tone (Broad Divergence)

Draw 5–6 items from the library's first dimension across Traditional Eastern, Cyberpunk Science Fiction, Modern Urban, and Alien Wasteland categories, showing only world and visual characteristics. Explore unusual directions within the current dimension too; cross-dimension blind mixes are used only when the user explicitly requests complete combinations. Mood candidates such as oppressive, light, tragic and heroic, uncanny, or fierce and fast may accompany the image without expanding into another entire menu. Ask “Which feeling would you rather see?” or begin with the user's freely supplied sound, color, or action. World and mood need not both be settled in one round.

### 2. Spatial Constraints

Using the settled world, randomly draw 5–6 items from the library's second dimension across confined, open, special-medium, and high-altitude categories. Explain action differences through each card's image sentence, such as “a narrow space restricts long weapons; a broken bridge makes retreat costly”; accept custom settings. Do not merely change background color while preserving identical movement.

### 3. Motive and Relationship

Draw 5–6 items from the third dimension across rivals, desperate odds, protection, and covert conflict. Clarify what must be protected or changed right now instead of first writing long character biographies. Retain an opening for user-defined objectives rather than forcing one of these motives. The desired ending may remain provisional; do not introduce awakening, sacrifice, or a rescuing character without authorization.

### 4. Visual Spectacle and Core Action

Draw 5–6 items from the fourth dimension across unusual weapons, environmental interaction, and special movement. If the user specifies one category, refresh within it. After selection, assign “spectacle appearance” and “body action” to their respective slots. Drawing a card does not require accepting all its world or relationship premises; established weapon and spell rules take priority.

First find one “memorable action to see clearly,” then establish how the opponent forces it to happen and what changes afterward. Spectacle does not mean endlessly adding effects; fine components stay as fixed structure, while action first satisfies distance, support, contact, and result.

If the selected action/spectacle remains abstract (for example, “dimensional reduction strike” or “wild combo”), use the [Action Reference Card System](action-reference-system.md) within the current dimension to complete applicable paths, support, landing, and force. This is internal choreography, not another module-activation question. Gaps involving new abilities, story, or outcomes still follow the user's decisions; do not force “dimensional reduction” into realistic martial arts.

### 5. Logic Validation and Outline Confirmation

By default, summarize world, space, relationship, spectacle, and core action only after handling all four dimensions in sequence. Check physical/spatial/visual-style consistency and setting dependencies. Explicit user requests to skip exploration follow the exception; identify undecided values as authorized draft assumptions rather than falsely claiming the user selected them.

For “narrow elevator + large explosion,” point out effects on people and car structure, retreat routes, and subsequent scenes. Offer directional impact/small-scale damage, a larger location, explicit magical protection, or other possible adjustments; accept custom user explanations. Do not ban exaggeration on sight; establish workable rules and visible costs.

After resolving conflicts affecting the main action, provide a roughly 100-Chinese-character outline covering the starting point, motive, spatial constraint, one core exchange, and resulting situation, distinguishing user-established facts from AI suggestions. Ask the user to confirm or change one thing and wait; do not immediately append a complete storyboard and prompts after the first question. If the user explicitly skips confirmation and authorizes drafting, follow that latest choice. After seeing the outline, “use this, give me everything” simultaneously confirms it and selects all-at-once delivery, without another question. A prior request for all-at-once text does not approve an outline not yet shown. Each round still ends with a roughly 50-Chinese-character five-slot snapshot.

Before producing the short outline or at confirmation, check the [Dialogue Design](dialogue-engine.md) or [Performance Design](performance-and-psychology.md) needed by the current context. Read only relevant sections without creating extra waits through module recommendations; strong conflict does not require loading an entire library. Both the first and later formal prompts default to self-contained plain text under [Delivery Rules](delivery-and-qa.md). Show engineering tables only on explicit user request; the wizard snapshot stays outside the copyable area.

## Delivery Strategy: After Outline Confirmation, Connect to the Advanced Generation Pipeline

### Generation Handoff Must Intervene First

After the user confirms the outline, read and execute [generation-handoff.md](generation-handoff.md). Before specific prompts, confirm the current platform/mode, available duration per segment, whether reference images/first and last frames are actually used, and native sound-effect/dialogue support. Reuse known information and consolidate questions about missing items that would change delivery. Do not present an unknown version as verified. If the user does not know the features, ask them to describe actual options or verify official materials/UI. While conditions remain unknown, continue with narrative drafts without labeling them ready-to-submit finals. If the user explicitly requests platform-independent prompts, deliver under stated assumptions.

Then connect to [Generation Segments](prompts-and-segments.md), [Consistency](consistency.md), and the [AI Pipeline](ai-pipeline.md); when using reusable templates, also execute the [Structure Contract](template-contract.md). Five-slot snapshots, choice records, and QA are management information and cannot enter the generation body.

### Delivery Choices and Professional Advice

Distinguish two independent decisions: **receive all text at once or in batches**, and **generate once or multiple times on the platform**. Receiving all segmented prompts at once does not mean concatenating the project into one model request; recommending a test first does not authorize withholding later text. If the user already explicitly chose all-at-once or batched delivery, reuse it without asking the same question again.

When no delivery preference exists, use the [Delivery choice in Generation Handoff](generation-handoff.md#10-delivery-choice): deliver all segmented plain text at once, or one test segment first; also accept custom choices such as “revise the outline first.” Recommend testing the highest-risk action first while retaining the user's decision. Do not mix “generate 30 seconds at once” into the text-delivery menu or label all-at-once delivery an unconditional default recommendation.

For a 30-second target, ask concretely: “Would you like all the segmented plain text needed for 30 seconds at once, or one segment to test first?” Replace that duration for other targets; do not default to 30 seconds or force engineering IDs/storyboard tables on the user. This delivery choice comes after card selection, logic validation, and outline confirmation; it cannot replace creative exploration. Execute an existing choice directly.

For complex, unverified multi-event plans of 30 seconds or more, explain risk according to actual event load and suggest grouping; duration alone is not evidence of failure:

> If these 30 seconds contain multiple attack-and-defense exchanges, complex contact, or scene changes, a single generation may lose actions or transitions. We can first group by event: would you like the full prompt set at once, or one segment to test first? Specific segment lengths depend on your platform and test results.

3 × 10 seconds is only one candidate grouping for a 30-second finished piece, not every model's duration limit or a claim that 30 seconds must fail. Actual request length follows this platform and tested capabilities. For other projects, substitute the actual total duration; adapt using successful evidence under the same conditions when available. Options must still include the open invitation.

A candidate 30-second plan may contain three roughly 10-second delivery groups, each with two roughly five-second event units: G01–G06 as an example. Every G still receives a layer A event and principal-interaction load check. A 10-second group need not equal one GEN request; the actual unit count is not fixed at six, and complex contact may require more.

### User Wants Everything: Deliver All at Once Without a Test Gate

Under confirmed conditions, deliver all self-contained plain-language text needed for actual submission in the same round. Do not require running the first segment to unlock the rest. If message capacity is exceeded, provide a complete file in that round rather than requesting the already-given all-at-once authorization again. Follow [Generation Handoff](generation-handoff.md) uniformly for self-containment, six visible continuity elements, and separation of parameters/notes; follow the [Delivery Protocol](delivery-and-qa.md) uniformly for semantic rewriting and engineering-version exceptions.

Keep the wizard-specific five-slot snapshot outside the copyable area; if showing a user-requested engineering version, place the snapshot after its explanation. Use Compact for one inspiration line or an unsegmented request.

### User Accepts Batches: Deliver the First Unit and Advance According to Results

First turn the chosen test unit into a self-contained plain-text body; place necessary references, settings, and a small number of acceptance checks outside the copyable area. The user may also choose the highest-risk segment first; briefly identify its position, and state the initial condition within the body itself rather than pretending it is the opening. Then wait for the user's test result; do not pay to run it yourself.

If the user reports failure, execute [ai-pipeline.md](ai-pipeline.md): obtain actual output, actual input, and settings; identify the earliest failure first, distinguishing action load, space, contact, reference, and platform-execution problems. Change only the principal variable at a time and deliver a revision. Without files or sufficient frames, provide candidate causes with uncertainty rather than inventing conclusions from footage you have not viewed. Do not mechanically reset the five slots or make the user choose the world again; apply ripple rules if a core setting must change. If the user switches to all-at-once at any time, immediately provide the remaining units without continuing compulsory batching.

## Opening-Round Example and Self-Check

At outline confirmation, major setting changes, completed test acceptance, or preparation to switch chats, use the [Continue-Creation State Card](../assets/templates/continuation-state-card.md) to organize a short portable card recording branches, five slots, platform conditions, and current seams. Retain the roughly 50-Chinese-character endnote each round; the full state card need not repeat every turn. Do not claim the platform permanently remembers every branch.

For an uninspired user's first round, actually draw 5–6 world-dimension items and label “tag + one image sentence” A–E or A–F. Then ask only “Which one most makes an image appear in your mind?” Immediately follow with the new-batch invitation, free-input invitation, and five-slot snapshot. Do not reuse a fixed set of three examples or record all current candidates as settled settings.

Interaction self-check: were inputs assigned to slots before asking? Does each batch contain only 5–6 diverse items and permit new batches/specified categories/free input? Does changing batches preserve settled slots and avoid recent repeats? Does the default follow four dimensions, one per round, with no cross-dimension packages; does “you decide everything” still select and report round by round, skipping only after an explicit workflow change? Are current-dimension branches preserved, with linked-change questions proactively asked after upstream changes? Was a complete plan delivered prematurely before outline confirmation? Were generation handoff and delivery preference confirmed before prompts? Does each wizard reply end with the roughly 50-Chinese-character five-slot snapshot? Did an all-at-once request actually receive everything, and did a failed batch follow the AI pipeline?

## Style Diagnosis Branch

When the user provides a reference and says “this kind of feel,” first use [Reference Input Classification](../ux/interaction.md) to establish whether they mean color, composition, action, atmosphere, or the whole; do not re-ask an explicit intent. Then propose style-card candidates under [Style Translation](../visual/style-translation.md). After user confirmation/adjustment, return to space, relationship, or action rather than automatically applying an entire director library.

Only this branch adds “style signature (candidate/settled)” outside the original five slots; do not turn every wizard into six slots. Keep source scope and unverified items internal. Retain the roughly 50-Chinese-character snapshot each round and append a brief signature; after leaving the wizard, restore low-frequency summaries under [Conversation Rules](../ux/interaction.md). Existing card drawing, new batches, free input, and all-at-once/batched choices remain.

Extended card draws may explore mood (mood), visual style (visual), and character archetype (archetype), still only 5–6 items per round, never all dimensions at once.

