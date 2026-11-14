# Spatial Tactics and 3D Footwork

`choreography.md` and `action-modes.md` decide **what happens in an exchange** and **how the fight flows**. Neither decides **where the fighters go**. v3.2 defined position as one scalar ("distance between the two") plus facing, so every fight collapsed onto a short line segment: step in, step back, along one axis, with no lateral travel, no height change, and no use of the space. This file adds the missing macro layer. **Spatial design comes before exchange design, and it is mandatory for any clip with a fight.**

A fight on one line is a defect unless the mode calls for it (a ritual duel with prescribed marks, or a declared plant-and-absorb defense).

## 1. The model: arena, ledger, movement

1. **Arena card:** the 3D volume the fight happens in, with named landmarks.
2. **Position ledger:** where each fighter is at the start of every beat, in three dimensions, with facing and anchor.
3. **Movement plan:** how each fighter answers the last beat **by moving**, chosen from a path vocabulary, and checked against the line-break rules.

## 2. The arena card (write before choreography)

| Field | Content |
|---|---|
| **Volume** | X (along the main path), Y (across it), Z (height), in body-lengths (BL). Example: 14 x 8 x 3 BL |
| **Landmarks** | Named points with coordinates and type: wall, boulder, ledge, step, post, slope, door, hazard, cover, exit |
| **Surfaces and heights** | Floor level 0; ledge at +1 BL; rock step at +0.5 BL; a pit at -1 BL |
| **Footing zones** | Firm, loose gravel, slick, narrow |
| **Routes** | At least three distinct ways between the two start zones (direct, around landmark A, over landmark B) |
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

Every response to an attack, and every attack's follow-up, includes a **displacement**. Choose from:

| Path | 中文 | Spatial effect | Visible wording |
|---|---|---|---|
| Advance, retreat | 进、退 | Moves along the duel line; theta unchanged | "steps in", "gives ground" |
| **Off-line slip** | 离线侧闪 | Leaves the attack line sideways; theta changes | "slides off the line to the outside of the right blade" |
| **Arc / orbit** | 绕步、环绕 | Circles the opponent at distance; large change in theta | "circles left, boots carving an arc in the gravel, until the sun is behind him" |
| **Cross-step / pivot** | 交叉步、转身 | Turns the front; changes facing without travel | "pivots on his left heel and presents his shoulder" |
| **Pass / switch sides** | 穿身、换位 | Goes past the opponent; theta flips about 180 degrees | "cuts past the raider's left shoulder and spins to face his back" |
| **Level down** | 沉身、滚翻 | Duck, drop, roll, slide; Z goes down | "drops under the sweep and rolls to one knee" |
| **Level up** | 腾跃、攀踏 | Leap, vault, climb; Z goes up | "springs onto the low rock, a full pace above the raider" |
| **Anchor push-off** | 借力蹬踏 | Springs from a wall, post, the opponent's blade or shoulder | "plants a boot on the crossed blades and pushes off over his head to land behind him" |
| **Terrain funnel** | 逼入地形 | Drives the opponent into a wall, corner, or hazard | "drives him back along the wall until the boulder pins his backswing" |
| **Obstacle play** | 绕障碍 | Keeps a post or boulder between them | "keeps the pillar between them and circles as the blade chases" |

## 5. The mandatory rules

Thresholds are **starting heuristics** for short clips. Test and tune them on your model.

1. **Arena first.** No exchange is choreographed before the arena card and the opening ledger exist.
2. **Every beat is in the ledger** with x, y, z, facing, and anchor.
3. **Line-break rule.** At most **2 consecutive beats** may keep theta within 20 degrees of the previous beat. The third beat must change theta by at least 30 degrees, **or** change Z by at least 0.5 BL, **or** change anchor.
4. **Displacement answer.** Every defensive response contains a path from section 4. A stationary defense is allowed only as a declared **plant-and-absorb** beat with a reason (an immovable guard, a pinned foot, a held doorway), and no more than one in three beats.
5. **The attacker moves too.** A follow-up attack starts from where the attacker now is, not from the previous spot. No return to a home mark.
6. **Lateral deviation.** At least once per clip, a fighter leaves the initial duel line by 1 BL or more (perpendicular distance).
7. **Vertical plan.** If the arena has height, the clip uses at least one level change (up or down). On flat ground a duck, roll, vault, or leap counts. The Z plan names where, when, and why.
8. **Airborne rule.** An airborne fighter can rotate, tuck, extend, and change blade angle freely, but can change the **trajectory of the body** only through an impulse: pushing off the opponent's blade, a wall, a post, or a collision, or through a declared ability (an established "air-step" in a wuxia world). A mid-air parry is legitimate when it is such a push-off or a posture change; "changes direction in empty air" is not, unless the world allows it. This extends `choreography.md` (airborne bullet in the force chain).
9. **Anchor change.** In a terrain-rich arena, at least one anchor change per ~10 s of runtime, and at least two distinct anchors per clip.
10. **Seam includes space.** The end ledger entry (x, y, z, facing, anchor) is the next clip's opening.

## 6. Spatial signatures by action mode

Each mode has a characteristic way of occupying space. Linear travel is **legitimate** only where the signature says so.

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
| Ritual duel | **Prescribed marks and formal positions.** Linear and symmetric is legitimate. Waive rules 3 and 6; the turn is a breach of the marks |

## 7. Camera and space

The camera shows the 3D movement or it is invisible.

- **Vary the camera axis** relative to the duel line: use at least two distinct axes per clip (a 90-degree side view, a roughly 45-degree three-quarter, an over-the-shoulder from behind, a high or low view). A fixed side-on profile flattens any movement into a line, so it hides the lateral and depth travel.
- Add **depth cues**: foreground occluders (rock, post), parallax from a moving camera, a visible far wall, objects at different distances.
- Show **Z** with low or high angles, a camera that rises or drops with the fighter, and the landing point visible after a jump.
- A model that does not cut on text instruction needs **continuous motion** through the axes: orbit, crane, handheld arc, a push-in that rotates around the shoulder.

## 8. Writing movement in space (prompt sentences)

A path sentence has three parts: **where from (landmark or opponent-relative), what shape, where to (landmark or relationship).**

- Opponent-relative terms work well: "to his right", "outside the right blade", "behind his shoulder", "with the sun behind him".
- Landmark terms anchor the path: "around the boulder", "up the rock step", "along the canyon wall".
- Use shapes (arc, circle, diagonal, pass, drop, spring), not only step counts.

Avoid a prompt where most movement sentences are "steps in", "steps back", "retreats half a step", "pulls back his front foot". Those verbs live on the duel line. `scripts/lint_prompt.py` warns when linear verbs outnumber spatial verbs.

Example (replacing a linear exchange): "As the raider's right blade comes down, the swordsman slides off the line to its outside and keeps circling left, boots carving an arc in the gravel, until the sun is behind him and the raider has his back to the boulder. The raider pivots to follow; the swordsman drops under the sweeping left blade, rolls to one knee, and springs onto the low rock, a full pace above the raider."

## 9. The spatial QA gate

Run before delivery (design check, from the ledger): `python scripts/check_spatial.py ledger.json`.

| Check | Pass |
|---|---|
| Line-lock run | No more than 2 consecutive beats on the same duel line without a Z or anchor change |
| Lateral deviation | At least one fighter leaves the initial duel line by 1 BL or more |
| Bearing sweep | The duel line rotates by at least 60 degrees per 10 s (waived in ritual mode; relaxed in stealth) |
| Level change | A Z change of at least 0.5 BL, or a declared level-change event |
| Anchors | At least two distinct anchors in a terrain-rich arena |
| Plant-and-absorb share | At most one beat in three |
| Bearing coverage | The duel-line bearing covers several directions (circular variance at least 0.05, roughly a spread of 30 degrees either side). A fight confined to one line scores near 0. This uses the relative bearing, because a whole fight may legitimately drift along a canyon while the fighters still circle each other |

Examples: `examples/spatial/canyon_as_written.json` (fails 5 checks), `canyon_prompt_B_reconstructed.json` (fails 2), `canyon_3d_redesign.json` (passes). The first two are reconstructed from prompt text, not measured from any clip; the third is an illustrative design.

The script checks the **design**, not the generated video. For the generated clip, score the rubric items in `evals/cases.md` case 20 by watching: lateral travel visible, the duel line rotating, a level change, an anchor change, and more than one camera axis.

## 10. Procedure

1. Read the Context Profile and the action mode.
2. Write the arena card (volume, landmarks, heights, routes).
3. Write the opening ledger.
4. For each beat, write the answer's displacement from the vocabulary and update the ledger.
5. Run the line-break rule and the QA gate.
6. Convert the ledger to path sentences (section 8) and choose camera axes (section 7).
7. Write the end ledger as the seam.
