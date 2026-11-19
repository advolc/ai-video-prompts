# Arena Construction and Visual Style

## The setting supports action first

Verify routes with an overhead sketch or whitebox before decorating. Map boundaries, starting positions, goals, entrances/exits, elevation, occlusion, destructible objects, and required camera positions. Use character height as scale. Pursuit needs distance, long weapons need backswing room, and giant characters need standing/turning clearance.

### Three layers for making a setting concrete (avoid mere labels)

After the user selects a historical tavern, bamboo forest, ruined temple, or another setting, turn its name into furnishings, layout, and environmental feedback before action/dialogue prompts. Reuse established detail; for gaps, offer brief suggestions to choose or delegate rather than interrogating every item or presenting suggestions as facts.

1. **Furnishings/props:** table/bench material, screens, pillars, upper floor, existing tabletop objects. Identify items serving dialogue occlusion, hand responses, or action support; add no weapons just to increase detail.
2. **Spatial layout:** entrances, doors/windows/oil lamps, characters at center/wall/dead end. Define character/light/route relationships that support camera and blocking.
3. **Environmental feedback:** what drafts, damp, or heat actually affect, such as moving curtain corners, wet boot marks, steam at a bowl. Route ambient sound by actual native capability or post responsibility.

Check all three internally, selecting only a few relevant handles here. Two or three layout candidates and one key question may come first. For an explicitly brief prompt, draft from known information and distinguishable candidates without a furnishing questionnaire. Fixed scenery is Tier C and uses no event count; new visible interactions affecting outcome are Tier A, not hidden in scenery description.

| Setting layer | Design question | Combat impact |
|---|---|---|
| Ground/support | Slippery, rubble, planks, low gravity, or flight? | Starts, braking, footprints, falls, landings |
| Routes/elevation | Which path is fast, where can it be intercepted? | Position pressure, circling, pursuit, escape |
| Occlusion/visibility | Who sees whom, when is a target lost? | Ambush, misjudgment, protection, ranged lines |
| Interactive objects | What do rails, doors, pillars, ropes, mechanisms do? | Support, obstruction, redirection, competing goals |
| Destruction | Trigger threshold, fracture direction, debris landing? | New obstacles/dangers, irreversible spatial change |
| Weather/atmosphere | How do baseline weather and action disturbances differ? | Depth, speed references, clothing/hair/material response |
| Visual anchors | Which silhouettes/value blocks identify across shots? | Reorientation after fast cuts or large camera moves |

Environment serves this scene's concrete needs; major destruction is not mandatory. Open flat ground can stress distance/lack of cover; a narrow room can stress close contact/door control. Do not add props that obstruct established actions merely to enrich the setting.

## Three setting-story questions (optional depth)

Enabled by default; omit for an explicit “brief/lite” request. These guide internal choices, not user forms.

| Question | Design inquiry | Candidate |
|---|---|---|
| What pressure does it apply? | How do existing space, light, material, sound restrict choice? | Existing low ceilings, narrow paths, wet ground may affect support/passage; do not add rain/slipping for this |
| What does it tell viewers? | What can the location communicate without dialogue? | Existing warmth in an empty seat or bolt state may supply an established clue; furnishings do not authorize new secrets |
| What relationship can it echo? | Does current spatial arrangement reflect character relationships? | Inside/outside or elevation may mean protection/power, or simply terrain; omit if unsupported |

Action comes before narrative. Choose one principal function on top of furnishings/layout/feedback rather than packing pressure, information, and metaphor into every scene. New key clues, destruction, or outcome changes still require existing authorization and event accounting.

## Environmental physics and dynamic feedback (avoid a stage backdrop)

Feedback follows established weather, media, materials, and actions. Describe one visible response at this segment's key foot plant/contact, then use the following relationships only when their conditions exist. This is a causal check, not a requirement to add wind, dust, rain, and explosions to every segment.

- **Wind/air pressure:** with an existing wind field, hems, hair, and wind-driven objects share direction. If fallen leaves/dust truly exist near a large action, describe their lifted path. Internal energy can shake/sound windows only with established pressure effects and windows within range; not every spell shakes windows.
- **Material contact:** each key step should have ground-appropriate feedback, such as crushed dry leaves, yielding wet mud, or shallow water displaced along boots. Hard ground may use loaded soles and grounded shadows; not every surface fractures. One continuous walk can establish a sustained footfall rule in one sentence rather than ten new events. Route echoes/audio between generation and post for this task.
- **Fluids/particles:** with established rain, drops strike the existing blade and scatter along its surface. With existing low fog, the body's passage precedes disturbance. Dry bare ground does not invent mist, leaves, or dust clouds; particle response cannot precede its trigger.

Favor one environmental response as a direct main-action consequence. Clothing/hair and noncritical particles are Tier C and enter naturally as needed. Independent destruction, object displacement, or state changes are Tier A events, not hidden “environment.” References and six seam items inherit established wind, moisture, powers, and damage. Unverified sound support moves sound to production notes without removing visible physics.

## Construction order and delivery

1. Functional layout: map routes, danger areas, action contact points; establish actual or relative scale.
2. Blockout validation: use blocks/planes/simple layered drawings to verify passage and camera sightlines; label intentional virtual-camera wall crossings and their spatial explanation.
3. Art refinement: allocate detail by primary shots, prioritizing contact objects, close materials, identifying anchors. Reuse distant repeating elements.
4. State variants: intact, destroyed, residual versions correspond to shot IDs. Debris cannot vanish next shot or block a route still needed.
   - Temporality (available by default): add when the setting needs prior history/foreshadowing. Existing repairs may suggest history; current force or water-level changes may visibly foreshadow later change. History needs evidence and foreshadowing present causality, rather than narration or invented wars, collapse, fire, or flood added for depth. Compact may omit this layer.
5. Lighting check: normal, power-lit, post-burst states retain readable silhouettes, gaze, and key hands.

2D delivery includes overhead layout, perspective design, depth layers, interactive props, and damage replacements. 3D delivery includes scale, modules, materials, collision/contact proxies, and destruction-variant specifications. Polygon/texture budgets follow target platform/framing, not one universal value. AI production delivers stable anchors, principal-angle references, and state descriptions; one text description does not automatically maintain all angles.

## Style is not a list of adjectives

Build a style card:

`character proportions | silhouette and line | facial simplification | materials/textures | light/dark grouping | light-source logic | color hierarchy | perspective/composition | action deformation amplitude | effect drawing language | background detail density`

Map these to the [seven art dimensions](../visual/style-translation.md#seven-visual-art-dimensions-and-three-audiovisual-dimensions): proportions, silhouette/form, and facial abstraction belong to form/proportion; outlines, line quality, edge softness within “silhouette and line” belong to line/edge; materials/textures to material/texture; value grouping/source logic to lighting; color hierarchy to color; perspective, static composition, background density to space/perspective; effect drawing to effect drawing language. Action deformation amplitude is form/proportion expressed over time, not an eighth dimension called “motion/deformation.” Do not infer dynamic rules from still images; fill them from actual before/after footage only. Retain original field names as video-production implementations of the seven dimensions, not a parallel classification. Inheriting art style does not automatically inherit camera movement, editing, or sound.

Choose one principal language and use others locally. These are optional directions, not genre requirements:

| Direction | Characters/settings | Action/effect adaptation |
|---|---|---|
| Clear cel shading | Abstracted form, limited value levels, controlled outlines | Strong key poses, local speed lines, planar impact; avoid accidentally becoming realistic smoke/fire |
| Semi-realistic 3D | Fuller volume/material/light relationships | Clear weight/secondary motion; local particles/volumes retain silhouettes |
| Ink/flat decoration | Unified negative space, brushwork, planar composition | Ink motion may replace trails, broken ink may carry impacts; retain target/situation clues |
| Exaggerated comedy | More elastic proportions/deformation | Delayed reaction, squash/stretch, graphic impact; recovery follows this film's comic rules |
| Graphic science fiction | Clear structural regions, signals, mechanical shapes | Readable charge states, failures, beam boundaries; interface text stays clear of combat |

Abilities may differ while line weight, shadow treatment, particle scale, and compositing habits belong to one work. Strong characters need not glow more; evil characters need not be black/purple. Distinguish factions through shape, posture, motion, and material response as well as color.

## Chinese-animation visual motifs and scene-anchor maps

This motif library is optional project vocabulary, not permission to pack every Chinese-style element into one shot.

| Motif direction | Possible visual/action language | Selection/research boundaries |
|---|---|---|
| Brush movement, negative space, ink tonal layers | Combination directions, held anticipation, aftermath edges | Distinguish brush marks from physical force; ink does not prove traditional authenticity |
| Rock, cloud/water, terrain | Movement routes, near/far scale, environmental breathing | Specific landforms/material logic rather than repeating symbolic backgrounds |
| Beams, pillars, gates, courtyards | Blocking routes, pushing off pillars, inside/outside relationships | Verify architecture/load against prototypes; decorative parts cannot carry entire structures |
| Textiles, armor plates, metal surfaces | Identity silhouette, action drag, tactile material | Source dates, craft, pattern applicability rather than random dragon/phoenix textures |
| Geometric patterns, object structures, ritual order | Spell components, rhythm, arrays, spatial composition | Verify specific religious/ritual meanings separately; original powers are not historical magic |

Select a few principal motifs per project and record `motif ID | cultural/material prototype and source | form rules | action/ability/setting use | excluded borrowing`. Characters, settings, and effects share rules without copying the same pattern everywhere. Verify facts through [cultural research](cultural-research.md).

Scene-anchor maps include at least overhead layout and principal camera angles, marking left/right endpoints, center, depth layers, elevation, exits, interaction points, character scale. Give anchors stable IDs, such as doorpost P01 or broken beam B02; map intact/perforated/remaining-frame state versions. Mark camera side, travel route, lateral coverage, and nonpenetrable regions. Preserve anchor order/perspective when extending laterally.

Generation segments reference exact angles/state versions. Dense repeating wall textures may be reduced; repeating tiles cannot be the sole locator. Contact, fall, and destruction segments prioritize same-angle first/last anchors. Do not assume AI reconstructs all space from one wide.

## Landscape lighting and viewing size

Dark scenes retain critical silhouettes/local contrast rather than simply lifting everything. If a burst illuminates a character, show corresponding changes on attached surfaces/nearby surroundings. Flat abstract effects may explicitly not participate in realistic lighting. Rain/fog, background textures, and decorative lines must not steal action focus.

Landscape uses left/right regions and depth layers for multiple relationships. Critical contact stays readable in the central action-safe area; edges carry less sole-source information. Check full-body silhouette, weapon hand, and faction recognition separately on desktop and portrait-held phone. Add medium-close coverage for critical mechanisms unreadable when small; subtitles avoid action. See [framing and compliance](framing-and-compliance.md) for specification fields.

Changing ratio requires recomposition and acceptance, not just cropping.

## Additional style signature

Add a “style signature” to the original card: irreplaceable user-confirmed features, usually 3–5 without forcing a count. If borrowing only a few dimensions, record only supported items. Carry them across segments as fixed descriptions, not new events. Further color/composition/light refinement appears as needed in [color](../visual/composition-and-color.md), [composition](../visual/composition-and-color.md), and [lighting](../lens/physical-light.md); do not create duplicate aesthetic thresholds.

Transcription example: card “red-leaf dominant palette, gray/black characters, axial tree rows, cool sidelight” → “Realistic 3D Chinese animation: a black-haired, gray-clad swordsman holds a straight sword. Dark red leaves cover the forest path; straight tree rows extend into thin mist, and cool light from the left grazes the sword hand.” These are replaceable form examples, not a default red forest chosen for the user. This file constructs space/fixed style; [style translation](../visual/style-translation.md) extracts signatures from references.

## Intentional evolution (optional depth)

Enabled by default; omit for an explicit “brief/lite” request. Confirmed signatures still carry across segments by default; most short films need only one principal language.

- Change only one of the seven art dimensions at a time, such as color temperature, compositional density within space, or material language. Do not change multiple dimensions or call an entire style replacement a small evolution.
- Require an established narrative trigger, such as entering a new space, relationship change, or time jump. Do not change for its own sake or invent plot to explain the style.
- Preserve the work's identifiable principal language and record the changed dimension, retained features, reason for changing here, and subsequent state.
- Without sufficient basis/reason, hold the style. Honor an explicitly requested overall transformation by redesigning scenes/transitions, rather than mislabeling it this section's single-dimension evolution.
