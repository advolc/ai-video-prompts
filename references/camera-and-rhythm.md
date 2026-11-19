# Camera Movement, Storyboarding, and Rhythm

See [composition](../visual/composition-and-color.md) for composition-layer rules. This file handles camera movement and timing; existing composition examples explain photography rather than establish a second set of composition thresholds.

## Each shot delivers one primary piece of information

Write “what the audience needs to know now” before choosing framing and movement. Full-body action, contact detail, a character's judgment, and the resulting situation are different tasks. A shot may carry secondary information, but do not combine rapid orbiting, zooming, rolling, and concealment of the principal contact.

| Method | Suitable task | Execution limits |
|---|---|---|
| Stable wide / medium-wide | Initial distance, continuous exchanges, differences in ability | Do not reduce characters to unreadable dots; separate silhouettes from the background |
| Lateral move / parallel tracking | Pursuit, advance/retreat, lateral movement | Background anchors demonstrate travel; pace it to leave room for the next threat |
| Dolly in / out | Enter psychological pressure or reveal environmental results | Camera translation changes perspective and cannot be described as pure zooming |
| Pan / whip-follow | Redirect attention, sudden attack | Identifiable endpoint; whip blur cannot hide all critical action |
| Short arc / orbit | Flanking, exchanges of attack/defense, control of the situation | Readable terrain and main axis; update screen left/right after the turn |
| Low / high camera | Weight, pressure, elevation, route | Camera height alone does not establish character strength; action and composition must support it |
| Contact close-up | Decisive grip, jam, break, guard breach | Reconnect to the body before/after; a close-up cannot invent an extra hand |
| Eyeline / POV | Threat recognition, misjudgment, target acquisition | Specify the gaze target; impaired awareness may justify instability but requires later reorientation |
| Distant / overhead view | Scale, group-fight relationships, landings, environmental damage | Preserve direction and height when returning closer |
| Fixed camera allowing exit from frame | Sudden speed, aftermath, suspense | Establish necessary results afterward; going offscreen is not a permanent escape from action design |

Without measured focal length, a wide-angle feel, normal perspective, or compressed feel suffices. For 3D camera parameters, state sensor/format conditions and label them previs suggestions; precise lens millimeters cannot be reverse-engineered from the final film. See [framing and compliance](framing-and-compliance.md) for aspect ratio, safe areas, and small-screen acceptance; see [generation segments](prompts-and-segments.md) for AI lateral/panning conditions and edge-distortion checks.

## Shot continuity

Record opening/closing composition, character screen positions, gaze targets, movement direction, and entry/exit edges. Usually preserve relationships across the main axis. For deliberate axis crossings, reorient through continuous movement, a neutral-axis shot, or a clear new wide. Multidirectional group fights can redefine local axes; one axis cannot mechanically explain the entire scene.

Group fights also map current/approaching/flanking/exit-blocking threats to screen-left/right regions and depth layers. Update after characters cross or the camera changes sides; see [group choreography](choreography.md).

Cuts at initiation, contact, reaction, or landing have different effects. Showing danger before reaction creates suspense; showing the startle before revealing danger creates surprise. Do not always repeat “eyes—fist—flash.” Even across shots, a key attack's path and result must connect.

A very short action phase may be repeated moderately to emphasize impact, but do not make characters inexplicably reverse and repeat. Deliberate disorientation suits subjective dizziness or fear; restore geography afterward. It is a design choice, not a continuity-error patch.

## Control four timelines separately

1. Action time: initiation, acceleration, meeting, recovery, consequences.
2. Camera time: when the camera starts, follows, passes the subject, and settles.
3. Editing time: when a cut occurs and whether the information has been read.
4. Animation time: spacing between key poses, holds, and in-between density. Output frame rate is not the number of independently drawn poses per second; a 30 fps file does not mean every part updates thirty times each second.

Speed can come from continuous exchanges in a longer shot; slowness can come from observation and an unresolved threat. Quiet around a burst, pose amplitude, and spatial change often matter more than adding cuts.

## Planning rhythm

The rhythm curve follows context and action mode ([context routing](../core/context-routing.md), [action modes](action-modes.md)): duels may rise, fall, and pause; last stands sustain pressure; infiltration has a long approach and one contact; sparring allows correction pauses; ritual duels pause under their rules. The following are a menu, not one universal curve.

Write information beats first, for example “probe—recognize—redirect—local failure—escape through the environment,” then assign seconds. An opening climax, sustained pressure, or comic pauses are equally possible; no single curve is mandatory.

A standoff pause needs an information change: weight shift, redirected attention, reduced exit access, or a decision. Slow motion emphasizes recognition difficulty or subjective experience; a freeze can provide stylized emphasis. Neither is a default rule of the source work. Follow fast exchanges with force response, breathing, goal progress, or a new distance so the peak has consequences.

Check both shot duration and action feasibility. If suggesting a two-frame emphasis at 24 fps, label it approximately 0.083 seconds and only an experimental starting point. Recalculate for other rates; “three frames of screen shake” is not a hard rule for every style. Simultaneous actions across shots use one timeline and are not counted twice toward total duration.

## Camera stance: observer, participant, subjective (context-routed)

Camera stance follows the Context Profile rather than a universal setting.

| Stance | Context | Method | Avoid |
|---|---|---|---|
| Observer | Ritual duel, infiltration, overwhelming advantage, formal talk, solemn farewell | Fixed/slow movement, longer lens or symmetrical wide, few framing changes; action happens within frame | Remaining an observer throughout and staging the entire fight as a side-view cross-section |
| Participant | Last stand, ambush, melee, street argument, escape | Close handheld, movement with force, low dives, pushes, whip around shoulders; attention follows danger and retreats from the blade | Unmotivated shaking; hidden critical contact |
| Subjective | Fear, injury, intoxication, dizziness, near death | Character eyeline, narrowed focus, defocus, breathing motion express state | Blurring failed action; returning to an objective view without explanation |

Switch stance at a **turn**, such as observer to participant when sparring becomes real; provide a trigger such as a blood-drawing strike or a shout. Choose cuts or continuous movement for the requested dramatic and spatial goal. If an actual output misses a requested cut, inspect that output and its inputs before choosing another attempt, a documented storyboard control, or separate shots joined in editing. A continuous retreat, low dive, push or shoulder arc is an alternative only when it preserves the user's shot intent. Missing evidence does not establish that a model cannot cut; one successful cut does not establish reliable execution. See [evidence boundaries](source-scope.md#model-observation-record).

**Choose the camera axis for the action.** Follow the spatial requirements in [spatial tactics](spatial-tactics.md), section 5. A fixed side view may preserve clear geography; it is valid when it serves the scene or is explicitly requested. When travel, depth or height needs another view, use a motivated three-quarter, over-shoulder, high/low view or continuous arc. Keep landings and contact readable, and preserve the user's requested camera ambition. Foreground, parallax and landmarks can clarify depth; do not add a second axis merely to meet a quota.

## Sound and dialogue timing

Sound can include warning, air movement, contact, bodily/mechanical response, environmental tail, and breath. Choose a primary sound rather than maximizing every layer. Briefly reducing ambience before a strong impact can be subjective treatment, not a template for every punch. Music beats can help; do not cut action causality merely to hit a beat.

Read dialogue in the character's delivery first, then check fit, allowing inhalation and response. Without listening to the track, propose new design only; do not evaluate the reference audio. Even low-cost previs needs at least one continuous playback check; static storyboards alone do not prove rhythm.

## Turn prompts into a shooting plan

Fill checkable fields first, then connect them into concise prose. “Cinematic,” “stunning,” “wild camera,” and “blockbuster feel” are not shooting instructions.

| Field | Content | Assessment |
|---|---|---|
| Camera position/height | Low, eye-level, behind shoulder/pillar; ground reference and suggested height | First-frame relationship to the specified subject agrees; height is a design target, not guaranteed AI precision |
| Composition | Character left/right/depth, frame share, visible feet/tiles, contact safe area | Key bodies/weapons have room; close shots reconnect to the whole |
| Movement | One of push/pull/pan/track, direction, start/end anchors, travel during the interval, start/stop behavior | Background parallax agrees with travel; “high speed” does not replace a path |
| Main action | Who starts where, attack line, responder, one principal contact and consequence | Hands, blade, target, support align; end state carries into the next segment |
| Lighting | Key direction/softness, shadow detail, power-generated fill; rain/fog/wet ground only if established | Light direction and ground state agree across segments; silhouettes remain readable |
| Time | Net duration, key-event interval, request margin, edit interval | Duration fits action volume; repeated margins are not story time |

Example shooting plan: 16:9, net four seconds; camera south of the passage, suggested height 0.6 m, slight upward angle, medium-wide retaining both feet, ground around the lower third; A left, B right. B steps left with a spear thrust. A's right-hand short staff deflects north, with one shaft contact. After contact A steps half a pace left, B retracts the spear. Camera tracks left around half a pace, slows before contact and settles at contact; doorpost stays rear left. Cool light enters upper right, shadow folds remain readable; no added weather or broad flash. Both weapons remain in their original hands at the end.

Height, ground proportion, and lateral travel must all pass first-frame/previs composition checks together. Do not submit contradictory numbers to the generation tool. Approved references supply exact identity, clothing, and weapon proportions.

## Motivated framing and psychological staging (avoid routine surveillance coverage)

- **Reject uninformative flattening:** ordinary dialogue uses medium/two-person wides to establish relationship and position, but that does not mean skipping lived processes. Favor close-ups for psychological turns, clues, weapon draws, or other critical contacts requiring clarity. A close-up is visual emphasis and adds information; do not cut to a face every line or silently remove explicitly requested expression/object close-ups.
- **Over-shoulder and occlusion:** dialogue may retain the partner's shoulder or use existing doorframes, pillars, or loose hair as foreground layers. Occlusion must not cover the current critical eyeline, hands, or contact. Camera/eyeline axes reconnect to shared geography; do not add foreground objects solely for a cinematic look.
- **Motion transitions:** use a match cut when similar actions already exist in both scenes, such as an established cup lift followed by a blade lift. This is a post-production connection between two shots; the cup does not transform into a blade within one shot, and no weapon is added just to make a match. A sound bridge brings existing sound from the next scene into the current picture early, handled in actual audio/editing layers.

Each segment still has one principal camera task. Match cuts, sound bridges, speed changes, and edit execution stay in management notes, not disguised as platform controls or new combat actions. Framing follows the psychological attention target; camera suggestions add no Tier A events.

## Subjective camera extension interface

Basic camera position, framing, axes, path, and one-shot task remain on this page. The user-mentioned production/camera-and-rhythm.md now connects to [subjective emotional camera language](camera-and-rhythm.md), extending only state-driven photography, perspective choice, and physical lens media, without copying or replacing this page. Subjective camera is a basic context choice for the segment; it does not require enabling deep psychology/dialogue systems, and defocus/dirt cannot conceal failed action.

## Appendix: Subjective emotional camera language (merged from production/camera-and-rhythm)

This is the subjective-camera extension, ID `subjective-camera-and-rhythm`. [Original camera and rhythm](../references/camera-and-rhythm.md) still maintains basic framing, axes, and movement. Preserve the old path without duplicating rules into another primary definition. Silently choose it by default only when current perspective genuinely relates to character state; do not force an objective wide into an eye POV.

### State → attention target → camera choice

Read the established stimulus for fear, serious injury, or tension, body support, and current attention target before choosing one camera response. Fear may be a steady stare; serious injury may involve controlled breathing. Do not hard-code “fear = shaky handheld” or “injury = defocus.” Options include a slow approach to the attention target, slight instability preserving readable contact, or one motivated focus transfer. Camera breathing means subtle starting/stopping or rhythm, not frame-accurate focus control.

Keep one principal camera task per segment rather than stacking shake, rack focus, orbit, dizziness, and dolly movement. Preserve a visible window at critical contact. If focus briefly leaves the target, new information must take over; an entirely blurred segment is not psychological expression.

### Narrative functions of visual language (optional depth)

Enabled by default; omit for an explicit “brief/lite” request. This addresses function without duplicating [composition methods](../visual/composition-and-color.md) or [basic camera movement](../references/camera-and-rhythm.md). The following are not mandatory shooting rules.

#### Narrative function of shot size

| Framing | Function | Common misuse |
|---|---|---|
| Distant / wide | Establish position and character/environment scale | Characters reduced to dots while subtle judgments are still demanded |
| Medium | Read distance, action relationships, contact | Excessively fine facial detail; key contact at frame edges |
| Medium close-up | Read judgment, choice, correspondence between hands and gaze | Complex combat and precise subtle facial acting together |
| Close / extreme close-up | Read grip, contact surface, decisive small action | Cutting to a face every line with no new information |

#### Narrative function of angle

| Angle | Possible function | Boundary |
|---|---|---|
| Eye-level | Neutral observation, equality, viewer judgment | Composition may still be biased; not automatically objective |
| Low | Pressure, weight, being looked down upon | Not automatically stronger; current action must support it |
| High | Confinement, observation, overview map | Not automatically weaker |
| Canted | Imbalance, anomaly, subjective unease | Not every shot; continuous emphasis fatigues |
| Over-shoulder / occluded | Relationship distance and depth placement | Preserve critical contact and gaze targets |

#### Rules for recurring visual motifs

| Stage | Internal check | Candidate change |
|---|---|---|
| Introduction | What relationship did this framing, angle, or camera change establish? | The same observing relationship first establishes confrontation |
| Recurrence | After the relationship changes, what more does repetition say? | The same device shows a former opponent beginning to yield |
| Ending | Can keeping/removing the device embody a choice? | The established rupture or approach changes the viewing relationship |

Remove repetition without added meaning; do not mechanically reuse for uniformity. This handles recurring visual devices; [narrative motifs](../narrative/story-and-scene.md) handles how objects, sounds, and colors gain meaning. Do not invent separate plots for each. Terms/function tables remain backstage. Translate through [on-set camera reasoning](delivery-and-qa.md) into natural language supported by spatial constraints, character paths, and emotional tension; complex photography remains anchored to action.

### Feasibility of visual illusion

For extreme pressure, consider a dolly zoom: camera translation and zoom coordinated so subject size stays roughly stable as background perspective changes. First check camera path, subject support, and tool control; do not claim precise platform parameters without verification. If uncontrollable, choose a stable close shot or separate post/controllable previs rather than merely feeding the term to the model.

Telephoto compression requires corresponding camera distance and spatial arrangement; changing focus in place does not change physical distance. Use it only when that relationship serves the narrative, not to stretch the background at every emotional turn. Exaggerated hallucination requires the user's established stylistic permission.

### Environmental lens dirt and foreground

Ask internally whether the camera is actually in a mud/debris splash path, whether that material exists, and whether current action can cause it. Existing blood/mud may briefly reach the lens edge as position allows; add no blood without a corresponding injury and no unexplained lens smear without nearby impact. Favor existing doorframes/shoulders; do not invent occlusion for a cinematic look.

Dirt serves space and force rather than covering the entire critical action. If retained, track it in camera continuity; a continuous shot cannot suddenly become clean. Complex lens effects can move to post; do not claim actual filming is complete.

### Presentation

Integrate executable camera relationships directly into plain prose without psychology explanations or a shot checklist. Refining fixed position/focus adds no core mandatory action. Independent camera switches and extra movement cannot hide in atmosphere; the original one-shot camera rules and [load contract](../core/pipeline.md) still apply. Route match cuts, precise frame holds, and post compositing through the original three layers.

## Dialogue blocking and camera handoff

Design characters' spatial choices through [dialogue spatial blocking](../dialogue/spatial-blocking.md) before photographing them. Wide, medium-wide, or anchored medium shots can establish rising, walking around, yielding a route, pausing at a threshold, and listener responses. Move closer after the path is established; do not make every line a shot/reverse shot. A scene holding position can use a fixed camera; the combat dual-axis criteria above do not apply.

Pushes, orbits, and reverse angles change the viewing relationship, not character displacement. When characters circle a table, move to a window, or change relative height, camera coverage must contain a connectable path and destination; two isolated before/after positions cannot conceal teleportation. Intimate or cooperative spatial development does not automatically become pressure, pursuit, or looming. For mixed dialogue/combat, use each mode's spatial design and carry real positions into the transition.
