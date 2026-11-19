# Ability Style and Effect Types/Intensity

## Ability card: rules before appearance

`source/carrier | trigger | target | direction/range | duration/cooldown | consumption/cost | countermeasures | failure appearance | visual identifiers | environment relationship`

Distinguish rules known by characters, rules currently known by viewers, and the author's full rules. Suspense may temporarily hide information, but decisive results cannot be solved through arbitrary new abilities.

Make abilities differ behaviorally: a blade film deflects along contact, a pressure ring pushes outward, a thin line needs endpoints/tension, an illusion changes perception without necessarily causing physical impact. Recoloring the same sphere does not establish a different mechanism. Preserve the user's patterns, component counts, and structure rather than changing them for a wide shot or burst.

## Effect types and uses

| Type | What to describe | Key fields and misuse |
|---|---|---|
| Trails/speed lines/afterimages | Direction, acceleration, brief visual emphasis | Start/end, tracked subject, disappearance; an afterimage is not another physical person |
| Sparks/impact plane/pressure wave | Contact, deflection, force release | Contact point, normal/propagation direction; a miss does not automatically create contact sparks |
| Elements/energy | Ability state/mechanism | Carrier, motion rules, boundaries, interactions; not everything explodes |
| Shields/barriers/fields | Defensive extent and loading | Boundary, deformation, failure, leakage; clarify inside/outside and ally positions |
| Destruction/debris/dust | Material, scale, landing, consequence | Force source, size hierarchy, direction, residue; not random scattering every time |
| Environment/weather | Depth and baseline motion | Separate from local disturbances triggered by footsteps/impacts |
| Graphic emphasis | Emotion, momentary impact, subjective perception | Entry/exit of impact frames, lines, color blocks; not physical objects in the world |
| Lens/compositing treatment | Viewing experience | Blur, shake, exposure, color shifts controlled by information needs; not substitutes for bodily reaction |
| Damage/machine failure | Combat cost | Torn clothing, armor gaps, limited motion, smoke/sparks; intensity follows audience/story |

## Intensity is not one slider

Specify coverage, brightness/contrast, particle/line density, duration, deformation, environmental effect, and camera disturbance separately. A wide effect can be dim; a powerful attack can barely glow. Character strength, damage, and screen brightness are not equivalent.

The following internal project levels can support discussion, not serve as industry standards:

- L0: no additional emphasis; body, props, natural surroundings carry it.
- L1: local emphasis, such as a short trail, a few fragments, or small material change.
- L2: clear ability/important encounter, covering a local area with readable force consequences.
- L3: this scene's visual peak, potentially changing environment or visual language substantially; retain causal lead-in and result windows.

No requirement to reach L3 in every scene or limit it to once. Multiple peaks need different narrative meanings/hierarchy. State which dimension increases with intensity; “increase everything” rarely guides production.

## Specifications for one effect event

`effect ID/shot ID | source and attachment | triggering action | start/end time | path/direction | affected range | intensity dimensions | occlusion limits | lighting response | decay/residue | next state`

Example: “As blade meets shield, a few short sparks scatter from contact along the shield rim; the shield dents locally and the character's rear foot slides. Sparks die first; the water trace remains into the next shot.” An ordinary collision need not become a power halo.

## Compositing and production order

Validate action/collision proxies, add the main effect, then secondary debris, dust, and camera treatment. Specify depth order among characters, props, foreground occluders, and effects. Effects pass correctly in front of/behind bodies rather than remaining stickers over faces.

For 2D, match the film's lines, planes, brushwork, and pose-update rhythm. For 3D, test timing/boundaries with inexpensive proxies before simulation/rendering; balance fine particles/volumes against framing/resources. Mixed production unifies edges, tonal steps, and movement rhythm so setting and abilities do not look like separate works.

AI prompts bind effects to specific actions/objects, describing start, trigger, and decay. Split complex interactions into connectable short segments. Inspect actual output for floating, penetration, premature bursts, weapon duplication, and vanishing residue; writing a restriction does not solve the video.

## Four effect layers and readable hands/blades

Approve action footage without effects first, then organize editable layers by these four tasks. Not every strike needs all four layers, nor four separate AI generations. Choose generation, tracked compositing, local editing, or animation appropriately.

| Layer | Source/binding | Production/compositing specifications | Acceptance focus |
|---|---|---|---|
| Trail | Actual weapon/limb trajectory | Track endpoints/direction; length varies with speed/style; correct depth, clear of grip and blade-identification boundaries | No continued erratic travel after the weapon stops; no second physical weapon |
| Light core | Actual encounter point | Small/brief emphasis; record trigger frame, peak extent, decay; separate footage matches perspective/occlusion | Contact before light; readable contact surface, hands, blade edges; avoid white clipping |
| Pressure wave | Contact release or explicit ability trigger | Radial/directional spread specified by impact plane, material, ability; local editing/compositing possible; not every attack explodes in a circle | Valid origin/direction, correct foreground/background travel and character occlusion |
| Aftereffect | Consequences of this collision/destruction | Select sparks, dust, arcs by source; layer with matching speed, light/color, lifespan; record residue for next segment | No sudden clearing of damage or smoke obscuring the next critical contact |

Record each event: `VFX_ID/shot | source and tracked object | trigger/decay | depth order | protected hand/blade/contact areas | mask changes | blending/lighting response | material version | residue state`. Track protected areas frame by frame; mask edges match this film's silhouette/blur. Do not incorrectly move a physical weapon behind a hand merely to expose the hand.

“Hands and blades stay clear” means effects do not persistently cover grip relationships, weapon outline, or critical encounters. Normal bodily occlusion is allowed with enough readable pre/post-contact windows. Do not destroy real occlusion to expose everything. If the user requires the entire encounter visible, revise camera angle/effect path before masks.

Acceptance order: clean action → trail only → add light core → add pressure wave → add aftereffects → compare all layers with effects off. At actual speed and phone-small size, identify attacker, defender, contact point, and displaced character. If a layer hides a previously clear mechanism, reduce extent/duration, redirect, or remove it first; do not keep increasing brightness to compensate.
