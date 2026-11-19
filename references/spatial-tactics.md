# Spatial Tactics and 3D Footwork

`choreography.md` and `action-modes.md` decide **what happens in an exchange** and **how the fight flows**. Neither decides **where the fighters go**. v3.2 defined position as one scalar ("distance between the two") plus facing, so every fight collapsed onto a short line segment: step in, step back, along one axis, with no lateral travel, no height change, and no use of the space. This file adds the missing macro layer. **Check usable space before choreography. Use concise relational facts for simple exchanges and coordinates for complex paths, groups or continuity.**

A linear or stationary exchange is valid when it serves the goal and its contact/support remains readable. Spatial variety is a design option, not an acceptance requirement.

## 1. The model: arena, ledger, movement

1. **Arena card:** the 3D volume the fight happens in, with named landmarks.
2. **Position record:** opening and changed states, with facing and support. Expand to per-beat coordinates and anchors for complex choreography.
3. **Movement plan:** how each fighter answers the last beat through a purposeful move or hold, checked against scene constraints.

## 2. The arena card (write before choreography)

| Field | Content |
|---|---|
| **Volume** | X (along the main path), Y (across it), Z (height), in body-lengths (BL). Example: 14 x 8 x 3 BL |
| **Landmarks** | Named points with coordinates and type: wall, boulder, ledge, step, post, slope, door, hazard, cover, exit |
| **Surfaces and heights** | Floor level 0; ledge at +1 BL; rock step at +0.5 BL; a pit at -1 BL |
| **Footing zones** | Firm, loose gravel, slick, narrow |
| **Routes** | The actual usable routes between start zones; one may be sufficient. Do not invent routes or landmarks to fill a quota |
| **Light and cover** | Where the sun, shadows, and obstructions are, if they matter tactically |

Use the world axes for the ledger and the camera's axes separately (section 7): a camera turn does not change world coordinates.

## 3. The position ledger

For every beat, for each fighter:

`beat | time | x, y, z | facing (degrees, 0 = +X) | stance | anchor (landmark touched or used) | event`

Derived, per beat:
- **Distance d** between the fighters in the ground plane.
- **Relative bearing theta:** the angle of the line from fighter A to fighter B against the world X axis. This is the **duel line**.
- **Change in theta** from the previous beat. A fight locked on one line has theta nearly constant.
- **Facing offset:** each fighter's facing minus the duel line (are they square, flanked, or turned away?).

## 4. The path vocabulary

Choose a movement or motivated hold for each response and follow-up. The following paths are options, not a required collection:

| Path | Spatial effect | Visible wording |
| --- | --- | --- |
| Advance, retreat | Moves along the duel line; theta unchanged | "steps in", "gives ground" |
| **Off-line slip** | Leaves the attack line sideways; theta changes | "slides off the line to the outside of the right blade" |
| **Arc / orbit** | Circles the opponent at distance; large change in theta | "circles left, boots carving an arc in the gravel, until the sun is behind him" |
| **Cross-step / pivot** | Turns the front; changes facing without travel | "pivots on his left heel and presents his shoulder" |
| **Pass / switch sides** | Goes past the opponent; theta flips about 180 degrees | "cuts past the raider's left shoulder and spins to face his back" |
| **Level down** | Duck, drop, roll, slide; Z goes down | "drops under the sweep and rolls to one knee" |
| **Level up** | Leap, vault, climb; Z goes up | "springs onto the low rock, a full pace above the raider" |
| **Anchor push-off** | Springs from a wall, post, the opponent's blade or shoulder | "plants a boot on the crossed blades and pushes off over his head to land behind him" |
| **Terrain funnel** | Drives the opponent into a wall, corner, or hazard | "drives him back along the wall until the boulder pins his backswing" |
| **Obstacle play** | Keeps a post or boulder between them | "keeps the pillar between them and circles as the blade chases" |

## 5. Spatial integrity and optional variety

Establish positions, facing, support and usable routes before the exchange. Track changes and carry them into the next action. Do not teleport, reset to a home mark or change a held object without an event. For a simple doorway parry, one concise spatial record can suffice. For complex crossings, use per-beat x/y/z, facing and anchors.

Select off-line movement, arcs, passing, level changes and terrain play when they advance attack, defense, pursuit or character intent. A planted defense, a linear thrust, a fixed camera or a sustained hold can be the right design. No universal lateral-distance, rotation, height, anchor, defense-share or shot-axis threshold applies.

Airborne trajectory changes require an impulse or an established ability; rotation and limb posture alone do not change the body's flight path. Preserve the world's declared physical rules.

When the user explicitly requests circling, a leap, changing height or a fixed position, make that target observable. Numeric thresholds may be attached to a particular design experiment; record why they matter and never present them as model limits.

## 6. Spatial signatures by action mode

Each mode has a characteristic way of occupying space. These signatures suggest possibilities; purpose, constraints and user choices decide actual travel.

| Mode | Spatial signature |
|---|---|
| Duel of equals | Arcs around a shifting center; off-line slips; control of the center; occasional pass |
| Desperate last stand | The radius shrinks: the defender is driven back toward a wall, door, or corner; short lateral breaks; anchor use for a final push-off |
| Stealth takedown | A path along cover and shadow; a change of level at the contact; one clean line **in** (legitimate linear travel) and an exit |
| Sparring | A defined ring; both stay inside; arcs and entries; moving back to reset position is legitimate |
| Ambush | An entry vector from outside the frame; the victim's scatter in several directions |
| Overwhelming dominance | The dominant holds the center; the other orbits the edge or is cornered |
| Flight fight | Linear trajectory through the space, interrupted by level and anchor changes (vaults, drops, obstacles) |
| Brawl | Short drifting arcs, clinches that rotate the pair, falls to the ground |
| Group melee | Movement through zones; the lead fighter's local arcs; flows around obstacles |
| Ritual duel | **Prescribed marks and formal positions.** Linear and symmetric is legitimate. A breach of the marks may be the turn when established by the story |

## 7. Camera and space

The camera shows the 3D movement or it is invisible.

- **Choose the camera axis** relative to the duel line: choose the axis or axes that make the important paths readable (a 90-degree side view, a roughly 45-degree three-quarter, an over-the-shoulder from behind, a high or low view). A fixed view can preserve clear geography; change axes only when new information benefits.
- Add **depth cues**: foreground occluders (rock, post), parallax from a moving camera, a visible far wall, objects at different distances.
- Show **Z** with low or high angles, a camera that rises or drops with the fighter, and the landing point visible after a jump.
- For an intended continuous take, an orbit, crane, handheld arc or rotating push can reveal another axis. For requested cuts, follow [camera execution choices](camera-and-rhythm.md#camera-stance-observer-participant-subjective-context-routed) and inspect actual results; do not automatically replace cuts with movement.

## 8. Writing movement in space (prompt sentences)

A path sentence has three parts: **where from (landmark or opponent-relative), what shape, where to (landmark or relationship).**

- Opponent-relative terms work well: "to his right", "outside the right blade", "behind his shoulder", "with the sun behind him".
- Landmark terms anchor the path: "around the boulder", "up the rock step", "along the canyon wall".
- Use shapes (arc, circle, diagonal, pass, drop, spring), not only step counts.

When the scene needs changing routes, do not substitute repeated "steps in" and "steps back" for that design. A purposeful linear defense or fixed position remains valid. The optional `--density-diagnostic --scene-type action` in `scripts/lint_prompt.py` reports a coarse movement-word imbalance for review; it cannot judge geometry or impose movement quotas.

Example (replacing a linear exchange): "As the raider's right blade comes down, the swordsman slides off the line to its outside and keeps circling left, boots carving an arc in the gravel, until the sun is behind him and the raider has his back to the boulder. The raider pivots to follow; the swordsman drops under the sweeping left blade, rolls to one knee, and springs onto the low rock, a full pace above the raider."

## 9. Spatial diagnostics

For a numeric ledger, run `python scripts/check_spatial.py ledger.json`. This validates input and reports lateral travel, bearing change, each fighter's own height range, and each fighter's anchor transitions. Different starting heights or different actors' anchors are not changes over time. A declaration of a duck is separate from measured foot elevation.

By default these are observations, not artistic pass/fail thresholds. Optional `requirements` may contain `min_lateral_bl`, `min_bearing_sweep_deg`, `min_height_change_bl`, and `min_anchor_changes` for explicit project targets only. A failed requirement concerns the design data, not generated footage. The checker does not prove contact, support, facing correctness or plausible speed. Watch continuous output to assess those.

## 10. Procedure

1. Read the Context Profile and the action mode.
2. Sketch usable space; use an arena card for complex geography.
3. Record opening positions, facing and support; use coordinates when useful.
4. For each beat, record the response's path or hold and update changed states.
5. Review paths against scene purpose and constraints; run diagnostics when a numeric ledger is useful.
6. Convert the ledger to path sentences (section 8) and choose camera axes (section 7).
7. Write the end ledger as the seam.
