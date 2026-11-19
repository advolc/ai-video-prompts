# AI Production Pipeline, Failure Diagnosis, and Stage Acceptance

## Stage deliverables

| Stage | Handoff deliverables | Conditions for proceeding |
|---|---|---|
| Requirements lock | Project card, landscape specifications, episode change, budget, material permissions ledger | No mixed aspect ratios; clear goals and constraints |
| Art and research | Character consistency cards, scene-anchor map, weapon/power cards, source records | Reference-based or text-only workflow selected; with images, verify angles/structure; without images, specify visible descriptions and reproduction checks still pending |
| Choreography and storyboard | Spatial map, action beats, shot timetable, low-cost previs | Attack/defense paths, effective distance, force production, and consequences hold together |
| Generation planning | Actual operating conditions, SHOT—GEN—CLIP mapping, start/end states, generation prose, control fields, separate production notes | Generation handoff checks complete; correct net duration, per-segment load addressed, pass/fail criteria for key actions; templates also check Tier A event budgets, shell/example separation, and platform fallbacks |
| Test samples | Representative contact, lateral-move, or multi-character segments; actual-output assessment | Tool achieves the principal requirements at the current complexity |
| Batch generation and selection | Raw outputs, versions/parameters, pass/fail tags, selected intervals | Failed end frames are not carried forward as approved references |
| Local repair and editing | Repaired segments, seams, continuous states, consistent framing/grade | Full playback is readable; space and rhythm work |
| Sound and lip sync | Stems, event table, dialogue timing, lip-sync checks | Actual listening and checks of synchronization, masking, and character voice |
| Post-production | Grading/compositing/subtitle/audio projects and revision versions | Action stays visible, visuals are unified, subtitles and sound checked under actual conditions |
| Export and delivery | Master, target delivery version, separate subtitles/stems, dependency list | Record decoding, playback, and actual listening separately; do not imply publication |
| Final film and handoff | Master, subtitles, required stems, asset/permissions records, acceptance notes | Checked on desktop and as a small image on a phone held vertically |

For planning-only work, mark execution stages “pending execution”; do not imply a model was run. Confirm the model name/version, first/last-frame and reference capabilities, segment duration, and current rules through the actual tool interface or official material. Without platform information, deliver a platform-independent plan and experimental hypotheses.

Platform fallbacks must address capabilities that are actually missing. When using templates, see the [structure contract](template-contract.md): text descriptions do not constitute image-based identity locking, and selecting frames in post does not constitute end-frame control. If reducing detailed powers or key actions would change fixed facts, obtain a choice first. When native audio is unconfirmed, preserve the task in production notes; do not infer that the platform lacks audio.

## Define a pass before generating key actions

For every event that changes the situation, record: `event ID | force provider/contact or support surface | start/end posture and direction | critical sequence | visible result | rejection conditions`. Choose the few necessary indicators for the event; do not make every shot fill the same count. Inspect actual continuous footage; sampled frames locate problems and guide denser sampling. Do not infer precise timing from one frame.

| Example event | Relationship that must be visible | Deviation requiring rework |
|---|---|---|
| Diagonal downward hammerfist breaks the guard | Fist travels downward into the guarding forearm; after the guard compresses, the body loses balance toward its established landing point | Replaced by a horizontal chest-level push-punch; body flies away before contact; fragments of light with no readable force direction |
| Both boots land on roof tiles and slide back | Both feet touch tiles first, knees bend to bear weight; for a specified squat, buttocks remain off the tiles; slide direction stays continuous | Replaced by a seated slide; support floats off the roof; long slide marks appear before the feet bear weight |
| Sword blade presses a petal | Blade meets the designated petal before deformation/release; the result establishes both positions and terrain changes | Explosion before contact; contact hidden throughout in intense light; six-petal components or force connections unreadable at the critical point |

These examples serve their particular action intent; a low squat, six petals, or a rooftop is not a standard for every fight. If a key item fails, label it rework/unachieved. An overall score, clear faces, or lavish effects cannot offset it. If the segment genuinely needs a different action result, record a design change first; do not silently lower acceptance and then call the original requirement complete.

## Failure diagnosis tree

First acknowledge frustration under the [interaction rules](../ux/interaction.md), then request only what is necessary to locate the earliest error. Stop when the user says stop; do not continue requesting samples. Do not begin by handing the user a long checklist.

Start at the earliest failed layer, changing only the principal variable each round and retaining comparisons.

First compare the text actually submitted, requested duration, reference inputs, and the scope covered by this delivery, rather than reading only the original storyboard. Distinguish faulty design causality, existing rules not followed in the draft, changes in the user's actual generation conditions, model execution deviation, and editing problems. Several may coexist; one output cannot establish percentage responsibility or a model's hard limits.

1. Person/object identity fails first? Verify whether references were actually uploaded. With images, check responsibilities, versions, angles, and mirroring. Without images, check textual distinguishability and whether identity demands exceed verified scope. Do not blame reference failure when there was no reference.
2. Identity correct but positions jump? Check world/screen left and right, axis, scene anchors, first/last states, and damage versions; restore relationships with a map and stable camera.
3. Space correct but attacks ineffective? Check distance, grip, center of mass, striking surface, and response; simplify the exchange or use controllable previs. Negative words cannot replace choreography.
4. Action works but contact looks wrong? Check collision timing, limb occlusion, handles, and weapon structure; move the segment seam, reduce interactions, or create a separate contact shot.
5. Contact works but lacks force? Check displacement/yielding, recovery, material response, and sound synchronization. Build layer by layer through [hit feel](hit-feel.md), rather than first enlarging the flash.
6. Failure only in lateral moves/frame edges? Check endpoint anchors and repeating textures; reduce edge characters and camera travel, use a stable camera or controllable background.
7. Individual segments work but do not join? Check posture, momentum, lighting, camera speed, and sound tails; if matching fails, use an explicit cut rather than forcing a dissolve.
8. Picture works but dialogue/lip sync fails? Retiming dialogue or repairing local lip sync should follow actual audio timing; do not damage the whole action segment for one line.
9. Works on desktop but unreadable on phone? Recompose contact framing, subject/subtitle areas, and edge information rather than only increasing export resolution.

## Executable comparison samples

Do not automatically run paid generation. Once the user authorizes test clips, select one earliest-failing event within budget. For planning-only delivery, provide the following experiment plan marked unexecuted. Record: `sample ID | model/settings/actual references | sole principal change | original draft/actual input | output | event acceptance result | conclusion and uncertainty`.

1. Retain the original sample as baseline. First reduce only independent attack/defense events, preserving characters, style, camera, requested duration, and other settings as far as possible; check whether the target event becomes more complete. Do not change model, add references, and substantially change camera at the same time.
2. If failure persists, keep the simplified draft and change only the camera to a stable view; inspect contact and support. In a later round, separately try explicit starting-posture text or an actual posture reference. Provide a text branch when no image exists; do not force an upload.
3. If requested duration must be shortened, treat that as another variable and use the real interface. If the user insists on one long segment, test tradeoffs within that method; do not unilaterally switch to segmentation.
4. Change models only when tool comparison is necessary and authorized, keeping inputs/settings as equivalent as possible; list unmatched conditions. A single success or failure is one sample, not a success rate or capability ceiling. Sampling noise remains without fixed random conditions.

Improvement after simplification supports task organization as one bottleneck in this instance. Continued failure establishes only that the requirement was not achieved under these tested conditions. When similar failures repeat within budget and no new variable remains, change shot design, use controllable previs/compositing, or report non-achievement; do not keep adding words.

## Budget and stopping conditions

At project start, agree on sample cost, per-segment attempt limits, and total budget. Without an agreed budget, deliver a plan; do not automatically run paid batch generation. Within existing authorization, test the highest-risk segment before expanding; record each failure's cause and change. When the same failure recurs without a new approach, change storyboard, segment duration, controllable animation/compositing, or provide a reviewable alternative rather than drawing indefinitely.

Expanding after samples is a budget strategy for actual generation, not a lock on text delivery. When the user requests all prompts, deliver every split unit and seam together under [generation handoff](generation-handoff.md). Deliver one segment and await feedback only when the user chooses staged text delivery. If staged tests originating in [idea development](inspiration-wizard.md) fail, preserve the user's established five slots first; inspect actual output/input/settings and diagnose locally. If established facts must change, ask about the scope of linked changes instead of mechanically restarting the entire wizard.

Completion reports separately state: design complete, assets produced, generation run, dynamic previs viewed, audio listened to, phone viewing checked, platform requirements verified. Passing structure/link/duration checks establishes only document reliability, not model success rate, a seamless long take, or publishing compliance.

## Additional cross-layer acceptance

For internal use or user-requested review; do not automatically score routine work:

- [ ] Visuals: dominant color/composition/light direction/material relationships hold; key contact readable; checked in actual video, not only the cover.
- [ ] Narrative: viewers can identify goals and changes; information order, reaction time, and emotional pauses have a basis.
- [ ] Sound: environment/foley/music layering, synchronization, and silence actually heard; leave unchecked if unheard.

See the [toolchain](../production/workflow.md) for post-production and [output specifications](../post/finishing-and-release.md) for export checks. Original action acceptance and rejection conditions remain effective; overall scores do not cancel key failures.
