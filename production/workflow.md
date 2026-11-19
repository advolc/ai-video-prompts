# Production Workflow (Consolidated)

Combines v1 editing grammar, negative constraints, previs, shot lists, storyboards, toolchains, batch generation, and selection. See the [Lens layer](../lens/lens-layer.md) for prompt writing.

## Editing grammar

This file handles narrative rhythm, information selection, and shot connections; [generation segments](../references/prompts-and-segments.md) handles technical seams and opening/closing states. A narrative cut across time/space is not technical seamlessness; technical matching does not prove dramatic progress.

Action cuts may fall on preparation, contact, or outcome while retaining direction and target; contact cannot always hide in cuts. Emotional editing assigns reactions by whose understanding changes rather than using shot/reverse-shot after every line. Music editing selects meaningful beats, not a cut for every sound; environment and silence also create rhythm.

Hard cuts suit clear changes; match cuts connect shapes/actions; sound bridges carry information; dissolves suit elapsed time but can create double figures. Jump cuts must intentionally compress readable time. An establishing shot need not slow the scene. Overcranking/undercranking and speed curves belong in post; actual frame rates and motion samples determine latitude. Interpolation cannot establish new attack/defense actions.

For multi-segment assembly, check the six state categories first, then camera direction, light, and sound tails. Failed matching may use an explicit cut rather than a forced dissolve. Check full playback and the smallest viewing size, not only the schedule. Final generation prose depicts visible movement speed; cut points, retiming, freezes, and transition execution stay in production notes.

## Targeted negative constraints

Internally use at most 2 targeted exclusions: choose the likeliest mistakes that materially affect this segment's goals rather than copying the whole vocabulary below. Final prose defaults to positive visible relationships. Supply a separate adapted negative-field version only when the platform has such a field and official confirmation of its availability; do not assume all models respond to negatives.

| Category | Internal risk examples | Candidate positive rewrite |
|---|---|---|
| Style | Unmotivated shifts between 2D and realism | Retain established line/material language and describe its texture |
| Composition | Duplicated figures, key hands out of frame | Established headcount, hands and contact in readable space |
| Light | Key switches sides, dead-black shadows | Same world-space light direction, cloth detail on the dark side |
| Action | Reaction before contact, floating feet | Displacement follows contact; feet alternate in taking ground support |
| Material | Soft blades, glass becomes water | Rigid straight blade, solid fragments after breakage |
| Platform artifacts | Flicker, random text, fused faces | Simpler repeated textures, one consistent identity, graphics added in post |

Do not use negatives to solve invalid choreography distance, wrong reference grip, contradictory goals, absent model controls, or exceeded information capacity. Repair design and input first; negation cannot create a missing feature. Positive rewrites retain the original object and trigger; examples do not authorize new weapons/explosions. See [prompt engineering](../lens/lens-layer.md) and [generation handoff](../references/generation-handoff.md) for platform differences.

## Low-cost previs

Choose the cheapest method that tests the risk. Static storyboards with scratch audio and a timeline test information/rhythm; 3D white models test scale, occlusion, camera position, and support; actual generated pilots reveal that model's execution. White models do not prove final material, facial detail, identity, or lip-sync stability.

Static previs: import panels → assign duration by read-through/action estimates → add scratch dialogue/footsteps → play continuously → record the earliest ambiguity. 3D white models: ground/entrances/character height → key positions and contact proxies → camera path → pose transitions → continuous playback. Mark scratch audio temporary and use authorized or self-made material, never presenting it as final effects.

Pass criteria: goal and result can be stated; key contact/landings remain visible; reactions have reading time; continuous states do not jump; sound space does not crowd dialogue. Unplayed previs is not viewed; stills alone do not establish motion validation. Fix space/rhythm first instead of hiding problems with white flashes in post.

Gap-management table: what previs confirms, what generation still needs to test, and which final effects belong to post. Establish dynamic support and character orientation before expensive generation. For text-only requests, provide a previs plan without automatically running paid tools. Connect to the [toolchain](workflow.md) and [AI pipeline](../references/ai-pipeline.md).

## Shot script and shooting list

Common production fields: `Shot number | Shot size | Angle | Main camera move | Net duration | Main content and opening/ending | Sound | Notes`. These help departments share information; they are not a claim that every professional production mandates one table. Existing storyboard tables emphasize space/action; this list adds execution, coverage, and sound handoff without replacing them.

### Information hierarchy (optional depth)

Enabled by default; may be omitted for explicit "compact/lite" requests. This is storyboard self-checking; field names stay out of final prompts.

| Field | Design question | Candidate |
|---|---|---|
| Main information | What one thing must be readable? | An established deflection moves the attack line off the target |
| Secondary information | Which one or two items support understanding? | Retreat/recovery in the original action, direction of an existing exit |
| Background information | What can be missed without harming understanding? | Secondary weather, hems, or background detail |
| Attention entry | Where should the first glance land? | Entry side of the original action, contact point, or clear visual distinction |
| Required reading window | How long must contact/choice remain readable? | Based on feasible approach, crossing, and result, not a universal frame count |
| Missable items | What can disappear without breaking the main information? | Background density, nonessential ornament count |

Three acceptance questions: is there only one main information task? Downgrade or reorganize separate primary tasks first; split a shot only when needed, not a tight causal chain mechanically. Is the reading window sufficient? Adjust net duration, framing, or shot size before treating post slow motion as automatic repair. Are missable items truly optional? The sole causal evidence cannot become background/atmosphere. Independent actions in secondary information still count as events; hierarchy does not bypass Tier A checks.

### AI task reduction and handoff

For AI tasks, first retain main content, shot size, main camera movement, opening/ending state, and estimated net duration. List control parameters, asset binding, and model request duration separately; authorization, acceptance, and post notes belong in management. One main camera task per shot; focus pulls and large orbits do not compete with multiple complex contacts.

A SHOT may span multiple GENs, and one GEN may yield several CLIPs. Record the actual mapping and selected intervals; only their net-duration sum is the final runtime. Request duration must be a real platform option, not inferred from storyboard seconds. Cut execution belongs to editing, not invented model parameters.

Acceptance: at least one shot clearly establishes key positions in the same scene; reactions add information; each shot's relation to its neighbors can be explained; sound ownership is assigned. Show the table only when explicitly requested; final copy prose has no shot numbers or schedule. [Storyboards](workflow.md) handle spatial images; [editing grammar](workflow.md) handles selection and connections.

## Storyboards

Show engineering content only when the user requests storyboards/panels; final prompts remain plain prose. Use one aspect ratio per panel and mark ground, exits, figure left/right/depth, gaze/attack lines, and support. Simple figures expose missing space better than attractive illustrations that hide it.

Solid arrows denote character/object displacement, hollow arrows camera paths, dotted lines gaze; explain these in a legend. A still cannot establish timing by itself. Use long/wide/medium/close/extreme-close sizes or clear abbreviations instead of unexplained mixed symbols. Beside each panel, state main information, opening/ending, and sound responsibilities rather than inserting a literary draft.

Panel to prompt: figure placement → opening space; arrows → routes and sequence; contact point → body/weapon response; final pose → next-panel handoff. Multiple panels express shot intentions, not proof that one model request can execute all panels. Manage panels/SHOTs, action events G, requests GEN, and selections CLIP separately. Bind reference control when supported; a nine-panel grid does not automatically lock identity.

Acceptance: even with text hidden, who faces whom, routes, and main contact remain recognizable; left/right, weapon hands, and damage connect across panels. Two opening/ending stills do not prove motion. Test rhythm through the [shot list](workflow.md) and [previs](workflow.md).

## Generation-to-delivery toolchain

Do not bind to brands. Select tool types by handoff artifacts, then verify features using current official material/actual interfaces. Writing this workflow does not mean software is connected or video generated.

| Stage | Tool type/handoff | Check before proceeding | When skippable |
|---|---|---|---|
| Text design | Assistant/drafts, rules, fixed identity | Sound goals/causality, user's request preserved | Qualified draft exists |
| Text-to-image/assets | Image tool/character images, scene images, responsibilities | Recognizable identity, correct held objects and support | User chooses no images or has assets |
| Image/text-to-video | Video generator/actual inputs and raw clips | Readable main action, state, identity, camera | Qualified raw clips exist |
| Editing | Nonlinear editor/timeline and selections | Six-category continuity, information rhythm, net runtime | One clip needs no assembly |
| Post | Grading/compositing/subtitle/sound tools and projects | Unified visuals, readable subtitles, audible synchronization | Corresponding work is unnecessary |
| Output | Encoder/master, delivery copy, subtitles, manifest | Full decoding, playback, metadata, target specifications | Text design only |

Record input version, output path, status, and next department at every step; pilot high-risk passages first. Authorization scope, budget, and attempt count follow the existing AI pipeline; batch tools do not automatically authorize payment or publication. See the [decision tree](../models/README.md) for model choice. Return to the earliest failed stage rather than calling structural documentation proof of dynamic success.

## Batch generation and selection

Before batching, obtain user-authorized boundaries for attempts, money, and time; this module grants no paid-generation or publication authority. First test the most risky representative passage, expanding only after it qualifies. Preserve raw clips per batch rather than overwriting. For text-only users, deliver the complete plan without making a pilot mandatory.

Screen hard vetoes first: identity, contact, six-category states, and explicit user goals. Then consider style and feel. A beautiful clip with a critical error cannot be selected as the next segment's final frame. Suggested labels: ID identity, SP space, CT contact, MO momentum/support, FX effects, CA camera, AU audio, ED seams, PF platform conditions. Distinguish design faults from execution deviations.

Internal record: `Sample ID | Draft/asset/model-mode versions | Request settings | Main variable | Output path | Usable interval | Failure label and location | Retain/discard rationale`. Do not delete unselected samples and lose comparison; when cleanup is requested, limit it to files generated for this task.

Estimate as "planned attempts × currently verified unit price + post-production time." Take the price from the interface and record its date; separate measured queue/generation/review durations. Without prices and samples, give no certain budget or success rate; an experience-based range must state assumptions. Stop when the same failure repeats with no new variable to test, returning to the [AI pipeline](../references/ai-pipeline.md) or a controllable approach.

