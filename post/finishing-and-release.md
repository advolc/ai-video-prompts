# Post-production, Release, and Management (Consolidated)

Combines v1 post-production (audio, grading, compositing, output specifications, subtitles, effects compositing), distribution (covers/titles, multiple platforms, release strategy), and project management (collaboration, feedback, templates, versions). All are brief checklists.

## Audio post-production

Confirm separate dialogue, environment, foley, and music tracks first. Prioritize intelligible dialogue; duck music moderately beneath speech and restore it smoothly, without pumping on every word. Preserve spatial continuity in the environmental bed and align contact sounds with visible triggers. Distinguish scratch TTS/effects from final versions.

Clean obvious noise and discontinuities before balancing frequency, dynamics, and space. Mastering checks overall loudness and true peak; verify LUFS against the target platform/program requirements rather than declaring a common number universal. Measurement reports record tool, range, and values; compliant loudness does not replace listening.

For stereo, check centered dialogue, left/right imaging, and mono fold-down. Produce 5.1 only with established requirements and tools, assigning channels correctly rather than duplicating ordinary stereo six times. Spatial sound follows visual distance and occlusion; environmental tails may survive cuts.

Acceptance begins with meters for clipping/true peak/loudness, then actual listening for dialogue clarity, bass, and audiovisual synchronization. State the available headphone and small-speaker checks separately. Complex pause, stress, and subtext cards hand off here to voice/lip-sync tools, not as analysis inside video prose. See [overall sound](../sound/sound-and-voice.md) for design sources and [output specifications](finishing-and-release.md) for release requirements.

## Color grading

Correct exposure, white balance, and color space, then match shots, then stylize. Applying a LUT is not completion. Determine whether material is ordinary display-transformed video or Log/HDR. Match LUT input/output; duplicate transforms may crush blacks or shift color. Without metadata, investigate the project source rather than guessing a curve visually.

Unification order: choose a reference shot → match black/white levels and skin → correct key-light temperature → restore dominant-color proportions between segments → locally protect faces/hands/key contact → play through for jumps. Dominant monochrome uses broad surfaces and atmospheric relationships, not identical tint on every pixel. Separate character and background through value, material, and local temperature.

AI grading can explore candidates but risks framewise color drift and local flicker. Manual work allows more controlled tracking and comparison of key passages. Choose by actual controls, not brand guarantees. Skin protection does not mean forcing everyone onto a template skin-tone line; follow characters, sources, and established style while retaining sufficient differentiation.

Acceptance: no unmotivated hue jump on adjacent faces or white objects; readable shadows/highlights; original dominant-color signature retained; viewing device/display transform recorded. Grading cannot restore cut-off action or nonexistent details. See [output specifications](finishing-and-release.md) for color tags and the [color system](../visual/composition-and-color.md) for design relationships.

## Basic compositing

First decide whether to replace a background, repair locally, or combine live-action/3D/AI layers, then choose the fewest layers needed. Check green-screen spill and edges; without a screen, roto/segmentation still requires framewise checks of hair and fingers. Select planar/point/camera tracking for the actual motion instead of applying two-dimensional translation everywhere.

Order: unify frame geometry/rate and color interpretation → key/mask → geometry and perspective → occlusion and contact shadows → light/color match → depth of field/motion blur/grain match → output. Depth compositing separates foreground/background through depth relationships; erroneous estimated-depth edges need manual repair. Adding a depth map does not make all occlusion correct.

Choose blend modes by purpose. Additive glow protects highlights; smoke/dust primarily follows transmission rather than washing everything white with Screen. A grounded character needs scale, foot contact, and ground reflections/shadows. Match the original blur of AI material to sharp 3D edges instead of blurring everything indiscriminately.

Inspect continuous footage for breathing edges, keying holes, sliding, shadow direction, depth occlusion, and light/color consistency. Record editable projects, asset versions, and color settings in management notes, not generation prose. Specialized effects connect to [effects compositing](finishing-and-release.md).

## Masters and platform delivery

Masters preserve as much image quality, audio, and editable project information as possible. Delivery copies use target-specific compression, aspect, and subtitles. Name them separately; platform transcodes never overwrite masters. Record at least container, video codec/pixel format, bitrate strategy, frame rate, actual dimensions, color space/transfer/matrix, audio codec/sample rate/channels, and subtitle method.

Prefer the project's actual motion sampling for frame rate; upsampling does not prove new motion valid. Verify SDR/HDR source and target before conversion; changing tags alone is not conversion. Resolution means actual dimensions. Stretching/letterboxing needs intent; do not crop characters without permission.

Verified example (2026-10-31, not universal): YouTube officially recommends MP4/H.264 and 48 kHz audio; BT.709 for SDR; 8 Mbps for standard-frame-rate 1080p and 12 Mbps for high frame rates; upload at the recorded frame rate. Source: [official upload encoding recommendations](https://support.google.com/youtube/answer/1722171?hl=en). This was a document check, not a project upload test. Verify other platforms item by item through the [matrix](../models/README.md).

Report three independent acceptance categories: file checks (dimensions/frame rate/duration/audio/full decode), playback checks (beginning/end/seams/subtitles/picture), and actual listening (clarity/synchronization/peaks and volume experience). Correct metadata does not establish playback/listening success. Delivery includes master/target copy/subtitles/necessary stems/project dependencies and instructions. State missing items and actual scope; never imply uploading or publishing occurred.

## Titles and subtitles

Separate on-screen text, explanatory subtitles, and release covers first. Do not force readable long text from generation models; precise text is preferably added in post. Fonts must be available with applicable usage rights. For Chinese, choose clear conventional forms whose fine strokes survive compression.

Segment subtitles semantically against the actual audio rather than mechanically animating every character. Pauses and speaker changes inform breaks. Read through each language's length instead of forcing translations into the same line width. Avoid faces, hands, contact, and platform UI; check safe areas in the actual target preview rather than using one permanent pixel value for all platforms. Reflow after aspect changes rather than merely scaling down.

Animation serves reading: brief fades or slight movement, sparing keyword emphasis. Do not bounce every character while combat competes for attention. The picture carries visible facts; subtitles add speech/explanation rather than redundant narration of readable action.

Acceptance: readable at phone size, no typos/garbling/missing glyphs, timing within the audio, no obscured key information. Choose external SRT/VTT or burned-in versions for the actual platform. State language and version; OCR drafts are not proofread subtitles. See [output specifications](finishing-and-release.md) for delivery checks.

## Effects compositing in post

Ability counts, shapes, and triggers follow established rules. Post particles, light, explosions, and smoke implement existing causality, not a changed winner. Establish subject contact first, then layer effects; a white flash cannot repair incorrect raw contact.

Layers: contact point/core shape → foreground/background occlusion → particle paths → lighting influence → smoke/dust residue → camera/material unification. Explosions specify trigger, expansion, and debris direction; smoke follows space and wind. Light influence on neighboring objects cannot expand without limit. Match raw frame rate, shutter feel, depth of field, and perspective; do not paste high-frame-rate particles over a sparsely sampled subject.

| Failure | Check first |
|---|---|
| Looks like a sticker | Tracking, perspective, occlusion, contact light/shadow |
| White washout | Layer count, brightness, influence range |
| Drifting effect | Lost anchor/tracking; do not conceal it with more particles |
| Explosion before contact | Trigger frame and audiovisual sync |
| Appearing/disappearing smoke | State version, persistence, inheritance in the next shot |

Retain readable windows for hands/blades/support. The main action remains intelligible with effects disabled. Include effect states in ability/damage seams. See [basic compositing](finishing-and-release.md) for the pipeline and [powers and effects](../references/powers-and-vfx.md) for original form layers.

## Covers and titles

Determine whether the user prioritizes clicks or artistic expression, then choose one core promise. A cover has one main focal point, necessary identifying text, and a readable action/relationship. Do not mislead with explosions or characters absent from the film. Check subjects, text, and contrast as phone thumbnails; do not simply shrink a large-screen design.

Title candidates: specific dilemma + change; clear subject + distinct mechanism; question + deliverable content. Avoid empty exaggeration and invented outcomes. Tutorial titles state what can be learned; narrative titles need not reveal the ending. Cover and title divide labor: one shows visual conflict, the other gives a viewing reason, instead of repeating the same long sentence.

Supposed algorithm preferences are experience-based hypotheses. Without official evidence, do not claim fixed platform rewards for colors, word counts, or time slots. Change only the cover or title in A/B tests and record exposure source and observation interval. Different traffic phases cannot be attributed entirely to design. See [controlled comparisons](../quality/quality.md). Style cards fill gaps without overriding the user's personal signature.

## Adapting versions for multiple platforms

Freeze story outcome, identity, key contact, and style signatures first, then separately design horizontal/vertical/square and 15/30/60-second versions. This is general rearrangement, not a specialized vertical-drama or brand-creation system.

An aspect change reconstructs character relationships: a lateral pair may become depth/vertical staging with necessary reactions, not a crop deleting a person or weapon. Preview target framing first; key hands, faces, and paths remain readable. If source material is insufficient, add shots or acknowledge regeneration is needed rather than substituting distorted scaling.

Compress runtime by information causality: preserve goal → essential contact/choice → result, removing repetition rather than triggers. Longer versions add relationship/aftermath information, not only slow motion. Reflow subtitles, covers, and sound entry/exit, not only image crops. Independently check six-category continuity and net runtime for each version, and reverify target output specifications.

Handoff table: source master/selections, retained/changed items, aspect, net runtime, missing assets, subtitle version, audio version, output path. See [version control](finishing-and-release.md). Platform changes do not automatically change story results.

## Release strategy

Plan audience, entry point, main-film/trailer relationship, sustainable update rhythm, and feedback window. No time slot guarantees traffic. Schedule around the actual project rather than automatically expanding one short into a series.

If a series is already requested, teasers promise only real main-film content and clearly identify viewing entry and version. This is general operations guidance, not a specialized serialized-creation system. Ask one concrete feedback question, such as "which contact was clearest?", rather than seeking generic praise. Classify comments as comprehension, production, or preference and return them to [project feedback](finishing-and-release.md); one comment does not overturn the whole design.

Before release, check picture, sound, subtitles, description, and links, using the [platform matrix](../models/README.md) for current specifications. External publication, replacement, and sending require explicit user authorization; a plan does not authorize operation. Record release time, version, and later edits rather than deleting old conclusions to disguise results. Reach and engagement are observations, not automatic work-quality scores.

## Project collaboration and handoff

Responsibilities: writing locks goals/facts; storyboarding locks space/information; generation preserves actual inputs/settings/raw outputs; post handles selections/compositing/grading/subtitles; sound owns tracks/sync/mixing. Solo projects may reuse these responsibilities without inventing a team.

Each handoff includes input version, chosen design, protected facts, output paths, completed scope, unexecuted items, recipient/next step. Acceptance uses observable role-specific facts, not a "cinematic" sign-off. Only qualified generated clips provide final frames; post cannot silently change story or lip-sync goals.

When a team edits concurrently, name the current master and owner, record feedback centrally, and resolve conflicts before overwriting. Continue routine reversible changes already authorized by the user; this workflow grants no external-send/publication authority. See [project shells](finishing-and-release.md) for templates and [version control](finishing-and-release.md) for changes.

## Project-level feedback loop

This file handles implementation ledgers across versions and contributors; [live feedback attribution](../ux/interaction.md) handles fragmentary conversational edits. Revise first and record as needed, without making the user complete a table.

Classify feedback as feeling/content/form/technical, mark source and scope, then prioritize hard user goals/factual errors → comprehension → taste. Client, director, and viewer roles are not factual precedence. Let the user resolve conflicting tradeoffs rather than majority-voting changes to confirmed plot. For vague "looks bad," ask once about a visible distinction, such as "too colorful or too much action?", while accepting free description.

Ledger: `Feedback ID | Source | Version/shot | Original wording | Attributed layer | Proposed change | Retained items | Priority | Owner | Result/evidence | User acceptance`. After implementation, give the result rather than a long process broadcast. Repeated problems suggest changing the wrong layer; do not endlessly add modules. Refusal or stopping is a boundary, not an objection to overcome.

## Project-management shells

These shells support setup and handoff, never final prompts, and do not require user completion. The assistant organizes existing information; real gaps stay blank or provisional. Separate layers according to the [template contract](../references/template-contract.md); rules and tables are internal by default.

```text
General: Project ID______ Version______ Audience/viewing conditions______
Story goal/protected user facts______ Runtime/aspect______ Platform mode______
Established characters/assets______ Budget/authorization/attempt ceiling______
Input/output paths______ Completed scope______ Next handoff______
```

| Type | Specific shell slots | Handoff focus |
|---|---|---|
| Short | One choice______ Cost______ Result______ | Structure → shots → actual inputs → master |
| Promotional video | Experience promise______ Distinction______ Ending entry______ | Teaser promises are deliverable, not unrelated montage |
| Episode | Episode change______ Entry/exit states______ Connecting facts______ | Episode fields, not a claim of a series-management system |
| Advertisement | Featured object______ One main benefit______ Evidence image______ Action entry______ | No invented efficacy; not a brand-specific system |

Per-project delivery list: selected text, actual controls, production notes, raw/selected clips, project/dependencies, master/platform versions, subtitles/stems where applicable. Report file checks, playback, listening, and actual uploads separately. See [version control](finishing-and-release.md) and [collaboration](finishing-and-release.md).

## Versions and rollback

Track design, character/scene assets, prompts, actual generations, and finished-film versions separately; do not name everything final. Suggested naming: `project_type_shot_version_status`, such as `bridge_prompt_G02_v003_candidate`. This is management naming; G numbers stay out of generation prose.

Version table: `Design ID | Version | Parent version | Changed layer/differences | Input assets/model mode | Output path | Selection rationale | Discard reason | Rollback location`. Do not overwrite raw clips or the only qualified version. Copy a draft before editing; use content hashes when needed to confirm identical files. Discarding does not mean deletion; cleanup follows user scope.

Compare one main variable at a time, then update the state summary after selection and keep unused branches. "Use that red version from earlier" should be locatable without making the user repeat it. Rollback synchronizes assets/prompts/seams; restoring only text while leaving new damage images is incomplete. See the [feedback loop](finishing-and-release.md); [consistency](../references/consistency.md) still maintains cross-segment facts.

