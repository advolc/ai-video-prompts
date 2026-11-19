# Prompt Layers and Generation-Segment Planning

## Separate three units

A narrative shot, SHOT, describes what viewers continuously see. GEN is one tool output. A timeline CLIP is the interval actually selected. Several GENs may form one long take, and only part of a GEN may be used. First confirm actual operating conditions, reference-material branch, and action load through [generation handoff checks](generation-handoff.md), then decide GENs. For complex interactions, 3–5 seconds of motion with one principal contact can be an initial experiment; duration follows user choice and platform tests. The retained six-second example is a candidate budget, not a universal capability ceiling.

Segment table: `SHOT_ID/GEN_ID | timeline start/end and net duration | requested duration/start-end margins | actual input assets | starting pose/composition/state | principal attack/defense/load tradeoff | ending pose/composition/state | camera movement | seam method | audio responsibilities | key pass/fail conditions | acceptance/rework reason`. Start/end states are design requirements, not proof that first/last images were supplied. Margins are not extra story time. Trim duplicated overlap so total net duration equals episode length.

## Internal generation descriptions and the three output boundaries

The [template structure contract](template-contract.md) separates generation prose, control fields, and independent production notes. Fixed prefixes, events, and visible continuity belong to generation. These five categories are planning dimensions of generation content, not permission to mix control/management into five prompt layers.

1. Fixed content: visible identity, weapon hand, weapon/power structure, style. Asset IDs, versions, and reference bindings stay in control/management; actual generation specifications go in parameter fields.
2. Setting: anchors, axis, left/right/depth, damage, lighting state. For segmentation, describe the preceding qualified state; use a first-frame image as a constraint only when actually supplied.
3. Action: one principal attack/defense goal, path, response, contact/miss, result, ending pose. Prioritize subject/main action and select among secondary changes.
4. Camera/performance: framing, one principal camera move, gaze target, breath/dialogue interval, focus task.
5. Effects/limits: trigger, attachment, decay. Prioritize the two or three limits whose failure would break this segment rather than generic negative lists.

Manage fixed content in project files, but include necessary descriptions when the tool lacks cross-segment memory; “same as above” is insufficient. Reference responsibilities/bindings and first/last-frame files go in controls, not a full binding table in prose. If the platform requires inline media markers, insert the minimum using verified syntax. Describe available native sound within its event interval; mixing, post-dubbing, and lip repairs stay in separate production notes.

These are planning layers, not a requirement to paste all five verbatim into every input. Compress through handoff checks, removing references to unuploaded assets and competing tasks. Each segment independently identifies subject, start, main action, and result. Separate storyboard, actual input, and post instructions.

## Conditions for lateral photography in AI

Check background collapse at both sides, edge-character deformation, lateral background drift, and repeated textures as risks; do not claim all models inevitably fail. Test coverage with inexpensive samples first. Establish left/right endpoint keyframes, static anchors, and plausible parallax. Tracking translates the camera and creates parallax; panning rotates near its position. Neither is merely “the background moves sideways.”

First place critical shared-frame encounters within the central safe area. Edge threats may appear partially, but the sole contact cannot live in a distortion zone. Give tracking/panning clear start/end anchors, primary target, and travel amplitude. If a wide, many enemies, dense repeating architecture, and fast lateral travel coexist, reduce one complexity. If drift persists, choose character motion under a stable camera, angular cuts, or a built/layered setting rather than repeatedly adding “stable background.”

Inspect continuous frames at both boundaries and center: doorpost count, roof patterns, ground perspective, pattern phase, and body proportions must not jump. Heavy blur cannot conceal geography that needs explanation.

## Long takes assembled from segments

Joining segments is optional, not mandatory for all long takes. Under the [global protocol](delivery-and-qa.md), around ten seconds of one tightly connected causal chain without complex contact may remain one long event unit; actual input emphasizes “one continuous long-take action.” Split only when complex interaction, support, or tool conditions require it, not mechanically by seconds.

Design the full spatial path and action beats before selecting seams. Favor natural holds after completed actions, brief character occlusion, doorpost cover, or clearly directed passes across the lens. Avoid hard joins during the most complex blade/body crossing or two-hand grip change.

When the user actually uses first-frame/image references, select the preceding qualified end frame or a clear adjacent frame with its state sheet. For end-frame control, use the actual approved image without repeatedly re-encoding and degrading it. For text-only workflows, self-contained prose specifies starting support, grip, momentum, and camera height; mark continuity pending rather than claiming locked frames. Retain modest editing margins and compare silhouette position, velocity direction, lighting, background anchors, and damage. Determine margin length through action tests.

Hidden seams still require spatial/time continuity checks. Brief occlusion, motion matching, and continuous ambience can help; dissolves cannot solve character doubling, bent weapons, or obvious background misalignment. If matching fails, make an intentional cut and reestablish space; call it a continuous exchange, not a seamless long take.

Planning example: a 24-second shot made of four six-second net segments, each GEN requesting net duration plus tool-permitted margins. Seams use recovery after deflection, doorpost occlusion, and framing after entry. Select only timeline intervals 0–6, 6–12, 12–18, 18–24 seconds; duplicated action does not create a longer story. Align phase-specific forms and held objects segment by segment.

Concrete candidate: a door-defense segment without powers, not dynamically validated. Escorting and renewed fighting, and operating the mechanism versus inserting the spear to block the gate, are separated. This is a segment table; actual text still needs preparation for current conditions.

| Segment ID | Net timeline interval | Start/end states and events | Next seam |
|---|---|---|---|
| G01 | 0–6 seconds | A center, B right, door left; B thrusts, A deflects with right-hand staff; both recover at the end without switching hands | Brief post-deflection hold; match staff tip/spearpoint and breath |
| G02 | 6–12 seconds | B retracts spear and follows without another thrust; A escorts C over the threshold with staff guarding, then retreats beside the lever | Join under brief doorpost occlusion; space/light behind the post stays consistent |
| G03 | 12–18 seconds | C inside; A pulls lever with left hand to lower gate, then withdraws inside; B remains outside, spear not yet in the gap | A inside, gate descending; match spearpoint and gate-bottom height |
| G04 | 18–24 seconds | B uses both hands to insert spear into descending gap; gate grips shaft; A/C inside left, B remains right | Tail establishes clamping result; ambience/gate-vibration tails continue |

For image handoff, pass the approved end frame and state sheet forward. For text-only handoff, check actual output matches; a state sheet is not video evidence. Retain seam options and remove duplicated action in editing. If reference first/last-frame capacity is insufficient, post occlusion unstable, or joins still jump, use explicit cuts within the same scene. Continuous 24-second storytelling remains possible; mark a seamless long take unachieved.

## Retry strategy

Change only the principal failure variable each time; retain old outputs, prompts, reference versions, and tags. Test feasibility with one high-risk contact segment before batching. If similar failures repeat within budget, change segmentation/shots or use controllable animation/compositing rather than spending the budget on unchanged draws. See [AI pipeline](ai-pipeline.md).

## Default one-segment/one-event split (duel contexts; see action modes for others)

The “rush—contact—separate—contact again” split applies to duels with unvalidated complex contact. Infiltration, last stands, ambushes, sparring, and melees use [action-mode](action-modes.md) splits instead. Start complex-contact samples at 3–5 seconds of movement with one principal contact. Choose requested duration from the actual interface; if short requests are unsupported, generate longer footage and select an interval. Selecting approximately 1–2 net seconds for a contact insert is a candidate edit choice, not a fabricated API parameter. See generation handoff checks for independent events and a user's one-long-segment choice. Do not disguise several attacks as “one suppression,” claim models can handle only one contact, or assert close-ups are inherently more stable.

| Segment | Event | Relay state |
|---|---|---|
| Rush | Attacker enters effective range from a clear start | Handoff frame retains attack line, support foot, weapon direction; contact has not occurred |
| First contact | Block, deflection, or control becomes valid | Same weapons/limbs; encounter produces specific deflection, displacement, or restriction |
| Separation/repositioning | Release contact, recover, move to a new position | Specify ownership, imbalance, distance, next attack line |
| Second contact | One encounter from a new angle | Choreograph response/consequences separately, not a duplicate first result |

For contact close-ups, fix near hand, weapon/bracer, and contact surface first; reduce simultaneous turning/hand switching. The final frame still shows force direction. A wrist hold needs clear surrounding fingers and arm ownership; a blade pressing a bracer needs material/ability justification for not cutting through. Toe/knee relationships must connect to the same leg/support state in the wide.

Wide—close—wide draft: 0–2 seconds wide shows approach up to impending encounter; 2–3.5 seconds close shows contact/deflection; 3.5–5.5 seconds wide shows retreat/imbalance/new distance. Total net 5.5 seconds, not three complete repetitions of the hit. Adjust times to action; contact result appears clearly in the insert or return wide.

Pillars/shoulder-backs can hide seams. Two to three frames is only an editing experiment: about 0.083–0.125 seconds at 24 fps, 0.067–0.100 at 30 fps. Choose by motion/coverage; revise if too short exposes a jump or too long loses action. Match occlusion entry/exit direction, size, value, and camera speed, then world state across it.

Whips/cuts may omit noncritical recovery but cannot entirely hide a decisive weapon transfer. Establish ownership, transfer direction, and cause before/after. If transfer is the key mechanism, use a readable insert or controllable animation rather than hiding generation failure. If the seam fails, use an explicit cut.

## Technical seams versus narrative editing

This file handles start/end states, generation requests, and shot joins; [editing grammar](../production/workflow.md) handles information/rhythm choices. Technical continuity is not complete narrative; narrative jump cuts are not seamless long takes.

## Executable wording for cinematic qualities

Aspect ratio belongs to controls. Depth/focus, light quality, material texture, and necessary environmental information become visible relationships; post grading and camera-breathing treatment belong to management notes. Select only what this shot's principal information needs, not every style term. If breathing means angle-of-view changes caused by focal-length change, it requires tool/material evidence rather than mystical decoration.

See [targeted negative constraints](../production/workflow.md) for negative-word categories and platform fallbacks. Prohibitions on this page are risk examples, not a universal cross-platform negative list. Final prose still converts them to positive visible relationships.
