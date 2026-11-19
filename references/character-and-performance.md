# Character Construction and Combat Performance

## Design must support the fighting style

A character design card has four layers:

- Identity lock: face shape, proportions, hair silhouette, costume structure, identifiers, dominant colors. The user's established design takes priority.
- Action structure: handedness, habitual center of mass, range of motion, weapon length, grip points, foot support, combat silhouette.
- Personality in combat: cautious characters observe and retain an escape; impatient ones may overcommit. Do not let personality labels determine every behavior; preserve immediate choices and growth.
- Current state: injury, fatigue, costume damage, dirt, fear, self-control. Carry state variants forward rather than restoring a clean character every shot.

Check long hair, capes, skirts, armor, and scabbards for clearance during arm swings, deep squats, waist rotation, and falls. Reduce occlusion, design segmented parts, or control secondary motion; do not solve action through body interpenetration. Faces and weapons need identifiable silhouettes even in a small image.

## Facial structure and surface design (avoid a plastic mannequin look)

Do not write only “handsome/beautiful.” Use the character's experience and established style to propose visible facial-structure and surface candidates. For an unlocked character, select at least one subtle asymmetric facial identifier, such as an old scar at the left brow, a slightly lowered eyelid on one side, or a faint bend in the nose. Choose one rather than stacking scars, aging, and a crooked nose. Choose one of three approaches:

1. **Researched realism:** choose specific traces of life load, such as sun spots, thick knuckles, or light fingertip calluses. Select face/hand details by what this shot shows; see [cultural research](cultural-research.md) for form and period evidence.
2. **Reality plus invention:** support movement with functional form such as a lean silhouette, cheekbone transitions, and mobile shoulders/back. These are design candidates; do not equate an occupation with a particular bone structure or substitute “explosive power” for visible structure and action.
3. **Pure AI invention:** within established world rules, choose nonhuman pupils for a demon species, pale translucent skin, or a broad skeletal frame for a body cultivator. Establish the form and source of abilities first; a genre label does not automatically transform the character.

The user's established face, references, and identity features take priority. Do not add scars, change the nose, or change age to satisfy asymmetry. Reuse existing asymmetry; offer candidates for confirmation if a new design is genuinely necessary. Clean, flat, or idealized styles do not receive imposed pores or aging; use permitted silhouette/brow differences. Design cards may be detailed, but prompts retain only necessary anchors visible in the shot. Fixed facial structure adds no performance action.

## Costume and material design (avoid cheap cosplay)

Do not write only “wearing historical clothing.” Specify material, cut, fastenings, and wear locations according to established class, occupation, period, and range of motion. Choose one of three approaches; do not stack every detail onto one character:

1. **Researched realism:** coarse-cloth short clothing, movement-friendly boots, washed-out linen, or worn cuffs may be candidates. Verify period/identity for constables' or scholars' exact clothing; examples are not universal historical facts across dynasties.
2. **Reality plus invention:** an assassin might wear a broad outer robe over fitted protection, with tied cuffs. Explain fastening and joint clearance rather than hiding interpenetration under “loose robe.”
3. **Pure AI invention:** an established cultivator might use waterlike translucent fabric; an established cyber swordsman might use waterproof nanofiber. Depict thickness, reflection, drape, and response to force rather than only naming materials.

Wear follows current state. Do not distress clean formalwear, new clothes, or a specified identity unnecessarily, or automatically change class/period because a design seems plain. Materials and cut precede added ornament/glow; clothing layers still support checks for arm swings, squats, weapon use, and occlusion.

## Three visual storytelling questions (optional depth)

Enabled by default; omit for an explicit “brief/lite” request. Check internally rather than requiring user forms. Established designs take priority.

| Question | Design inquiry | Candidate |
|---|---|---|
| What experience does appearance communicate? | Which facial structure, skin, posture, or clothing comes from a specific experience? | Established long-term weapon use may justify knuckles/calluses; unilateral changes require an established old injury. Add no scars or invented backstory |
| What class/occupation does appearance communicate? | Do material, cut, and wear support the character? | Choose grounded workwear/formalwear functions; poverty does not mandate rags, wealth does not mandate gold |
| What visual relationship exists between characters in frame? | How do silhouette, color blocks, and material distinguish them? | Choose a suitable height, width, value, or texture contrast, rather than separating factions only through glow |

These questions sit alongside the three approaches to face and costume. One principal narrative point per character suffices; do not turn all three questions into cumulative design tasks. Retain clean formalwear, new clothes, and approved looks; depth is not permission to change identity.

## Handoff-ready character consistency card

`CHAR_ID/version/approval status | facial proportions and identifiers | hair-color regions/front-side-back silhouettes | character-relative left/right shoulder armor and patterns | clothing layers/fastenings | height proportions | handedness/weapon dimensions and grip | fixed power components | initial and changing damage | voice/lip-sync baseline | reference files, responsibilities, and non-inherited elements`.

State trajectory for this stage: initial state ______; changes this stage ______; basis ______. Record established changes only; do not invent unknowns. Carry versions across segments.

Connect every item to an actual reference or explicit description and label it “immutable,” “may vary with performance,” or “updated by story.” Identity cards exclude temporary stances; state sheets carry dust, wounds, weapon ownership, and remaining abilities across generation segments. If front/side/back views do not support complex upward looks, falls, or weapon interactions, add the relevant angles; generating a different face is not filling angle coverage. See [consistency engineering](consistency.md) for version maintenance.

## Actual character model/design construction routes (as needed)

### 2D

First establish front/side/back and critical angles, proportions, and identifiers; then combat key poses, expressions/visemes, layered clothing/hair, and damage replacements. Frame-by-frame drawing and cutout rigs need different resources: the former can redraw exaggerated angles; the latter needs planned turn replacements, limb occlusion, and controls. One character illustration is not a complete action asset.

### 3D

Block out silhouette/proportions, check head/body and weapon scale in common shots, then refine. Topology prioritizes deformation at shoulders, elbows, hips, knees, hands, and face; split armor/hard surfaces according to real or established connections. Allocate UVs/materials by framing. Rig torso, center of mass, limbs, eyes, jaw, and necessary facial controls.

Configure hand/foot IK/FK switching, contact locks, weapon attachments, two-hand grip relationships, and clothing/hair controls according to action needs. Not every character needs the same controllers. Test proxy geometry before costly cloth/hair simulation. Stylized squash/stretch can be built into the rig, with identity preserved after recovery.

Minimum deformation checks use poses actually needed here, such as raised arms, wide squats, torso twists, gripping, falling, and turning the head. Check joint collapse, foot sliding, intersections, attachment jumps, and facial tearing. A completed design card or rigging specification does not mean a usable 3D model exists.

### AI-generated assets

Fix identity images, full-body costume, and key-prop references, assigning each image responsibility for identity, action, or style. Add side/back views as needed. A facial close-up cannot carry full costume consistency. After generation, actually check face, handedness, prop count, and damage continuity. Prompts express constraints; they do not guarantee correct output or replace model files.

## Expression follows attention and bodily load

Design performance as “what is seen → how it is judged → bodily change → action taken.” Expression extends beyond brows/eyes to breathing, neck/shoulders, fingers, and stance.

| Combat state | Gaze/facial choice | Body and breath | Dialogue tendency |
|---|---|---|---|
| Observation/probing | Gaze moves among weapon, feet, or exit; brows/mouth may stay restrained | Adjust weight while retaining recovery options | Probe intent or remain silent |
| Active attack | Fix on a specific target; focused need not mean angry | Exhale with effort, restore support afterward | Short instruction or misdirection; avoid naming every move |
| Pressure/surprise | Eyes first follow the new threat; jaw or mouth tightens | Sudden support change, interrupted breathing | Unfinished short phrase or breathy voice |
| Pain/damage | Local contraction, protective gaze; scale follows personality/style | Protect injury, shift load, restrict movement | May conceal it; shouting is not required |
| Fatigue | Slower focus shifts or deliberate concentration, not mechanically drooping lids | Changes in breathing intervals, arm lift, recovery, while retaining strategy | Shorter phrases, recovery time |
| Reversal of judgment | Gaze leaves the threatened area for an opportunity; tension may subside | Weight changes before the counter | One purposeful line, or let action speak first |
| Fear/anger | A combination of gaze direction, brows/mouth, avoidance/staring | Fear may freeze or overaccelerate; anger may be reckless or calm | Follow the character's established speech |

Do not maximize all emotions at once. A small image may need stronger key expressions; restrained characters can reveal feeling through hands/breath. Facial acting may briefly precede action to reveal judgment, or bodily avoidance may precede facial recognition of danger. Choose for narrative purpose.

When this scene needs psychological-action breakdown, subtle expression, and visible translation, read the relevant [performance and psychology](performance-and-psychology.md) sections by default. Ground vague wording such as “he is tense” in visible behavior here; do not await extra module authorization or load unrelated matrices.

**Prevent unfocused gaze:** generation prose must not substitute abstract directions such as “look at each other/look forward” for attention targets. Name the physical point, such as fingers gripping the opponent's knife, an envelope seal on the table, or a door bolt. For intentional eye contact, specify how their eyes meet rather than replacing face attention with weapon attention. Wide shots use head/shoulder and body orientation; medium close-ups can trace eyelines; close-ups specify pupil contraction only as needed. Retain the existing performance load, adding no collection of subtle signals.

## Dialogue: purpose before words

Choose one function per line: convey tactics, delay, lure, conceal injury, change relationship, or reveal understanding. Remove slogans that merely repeat the picture without character grounding. This does not make everyone silent; talkativeness, theatricality, or ritual move-naming may define a character, while the opponent and battle continue changing.

Original examples: an escort says “Go through the door first. I'll follow,” changing the companion's action; an enemy says “You keep protecting your left,” revealing observation; a defender deliberately answers “Then try it,” supporting a lure that the next action must fulfill.

Brief exertion, choking, or repeated rolls usually leave no room for calm long sentences. Identify internal monologue, subjective time, or comic rules when used. Time lines through actual delivery; fixed character-count formulas are not performed duration. Distinguish speech, breathing, groans, and silent mouth movement. Without recording, do not claim listening acceptance.

For dialogue in this scene, use relevant [dialogue design](dialogue-engine.md) checks by context by default. Use the [dialogue support card](../assets/templates/dialogue-design-card.md) when expanded records are needed. Complex pauses, emphasis, and subtext analysis remain in production notes; every line need not use every device.

## Voice and lip-sync handoff

Voice parameters: see [character voice design](../sound/sound-and-voice.md) as needed. Record applicable pitch, breath, articulation, accent, change patterns, and voice version as character properties carried across segments. Do not fill them without a voice task or load the entire parameter system merely because the character card has the field.

Build `line ID/character voice version | text and speaking purpose | start/end/pauses/breath | onscreen/offscreen/internal | face angle and visible mouth shapes | audio source/authorization | sync acceptance`. Final lip sync follows the selected audio timing. Read through before locking action gaps; a long lip-synced sentence during a fast turn can sacrifice performance and stability. Shorten it, move it to a readable interval, or explicitly use offscreen voice.

If audio can be generated with video, first test voice, content, and timing control; one result does not guarantee consistency across segments. If uncontrollable, add voice, breath, and effects afterward, repairing local lip sync if needed. Carry unfinished syllables, inhales, and tails across segments rather than restarting every sentence. Report synchronization passed only after hearing actual audio and viewing actual mouth movement; correct subtitles do not prove correct spoken content or lip sync.

## Character arcs and performance responsibilities

[Character arcs](../narrative/story-and-scene.md) handles desire, choice, cost, and change across scenes. This file handles immediately visible acting. One breathing change cannot replace an entire arc, and an arc does not require subtle signals piled into every shot.
