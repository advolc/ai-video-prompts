# Consistency Engineering

## Asset versions are the baseline

Characters, settings, weapons, powers, costumes, and voices each have stable IDs and versions. Filenames may use `CHAR_A_v02`; shots and generation segments reference them. An approved image is not overwritten by the next generation. Retain originals, crop purposes, change records, and approval status. When appearance changes, list affected shots to avoid half an episode using a new crown and half the old one.

Consistency includes more than faces: silhouette proportions, black/white hair regions, left/right shoulder armor, pattern locations, handedness, weapon length/grip spacing, power-component count, injuries, energy reserves, and background structure. Fixed seeds and identical prompts are tools, not guarantees across shots.

First verify actual inputs through [generation handoff checks](generation-handoff.md). Without images, use a written appearance card as design baseline. Mark approved images, angle coverage, and image handoff “not provided/not used” rather than pretending they exist. Fixed text does not mean identity is locked. If strict reproduction is requested but material is insufficient, explain the gap and offer optional references or adjusted goals; do not change the character yourself.

## State and spatial ledger

`timepoint/SHOT/GEN | character position/facing/screen region | support and momentum | weapon hand/ownership | costume and damage | ability state | scene anchors/damage version | camera side/height | sound continuity items`.

Dialogue additionally carries each character's anchor, facing, posture/height, distance, available routes/access, and unresolved spatial proposals through [dialogue spatial blocking](../dialogue/spatial-blocking.md). A held position also needs continuity; a camera turn cannot substitute for bodily movement.

For every generation segment, record planned start/end states separately from actually approved states. The next opening inherits the preceding qualified result, or has an explicit ellipsis and reason. Name input frames only when first/last-frame controls are actually used; a written state sheet is not an image lock. Record world and screen coordinates. Camera rotation is not character teleportation; ornaments use character-relative left/right and must not silently switch through mirroring.

## Scene anchors and consistency cards

See [character performance](character-and-performance.md) for character cards and [world/style](world-and-style.md) for setting cards. With reference assets, check complex poses needed here beyond standard views; weapon collisions specifically need hands, handle, and contact surfaces, not merely a face portrait. In text-only workflows, explicitly describe those relationships and pending dynamic checks. A full reference-asset set is not a prerequisite for every creative task.

Compare an asset's standard frame, this shot's start/middle/end, cross-segment seams, and final film. Stylized transient deformation is allowed, but recovered identity/structure should return to baseline. Label a single-frame anomaly separately from sustained identity drift and judge actual viewing impact.

## Changes and local rework

Tag failures as identity, space, action, contact, effects, sound/lip sync. Locate the earliest failure and inspect dependencies: if a broken shield returns intact in the next segment, revise the later state reference. If the preceding end frame is already wrong, do not keep it as the sole identity baseline.

Rework only affected segments/assets; editing and grading must not overwrite original output. Record selection reasons, rejected segments, and versions. After repair, review adjacent seams and related shots; do not regenerate the whole film without reason. Use compositing/image repair within their actual scope; text constraints alone cannot be described as a repaired video.

## Additional version and performance consistency

Version fields: plan ID, version, parent version, differences, selection reason, rejection record. Link assets/prompts/final film through [version control](../post/finishing-and-release.md); rollbacks also restore relevant seam states.

Performance fields: expression baseline, gaze habits, breathing rhythm, subtle-signal variants, applicable stimuli. These preserve character; they do not require every item to appear or add actions in every segment. The main subtle signal and related bodily proxy are Tier B, not additional Tier A events. An explicit facial target cannot silently become distant body acting.

`references/character-and-performance.md` and `references/performance-and-psychology.md` design immediately visible acting: gaze, breath, subtle signals, bodily proxies. This file handles only preservation and handoff across segments; do not redesign acting here or add performance plans inside state cards.
