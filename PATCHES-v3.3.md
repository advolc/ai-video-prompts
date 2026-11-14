# v3.3 Patch Report: Spatial Tactics and 3D Footwork

## 1. Diagnosis

| Question | Answer | Evidence |
|---|---|---|
| Is there a structural gap in macro 3D movement? | **Yes** | The action unit's `起点` defined position as `双方距离、身体朝向` (one scalar plus facing); the state ledger had `角色位置/朝向` (no Z, no anchors); `路径` meant the strike path, not the fighter's traversal; the spatial vocabulary in `delivery-and-qa.md`, `generation-handoff.md`, `hit-feel.md` and `core/pipeline.md` was zero |
| Did the action unit or QA catch a linear stand-and-fight? | **No** | `delivery-and-qa.md` had no spatial check; the 'reset test' failed only when two beats start from the *same* positions, so a fighter oscillating along one line passed it |

## 2. New and changed tools

- `references/spatial-tactics.md` (NEW): arena card, 3D position ledger, path vocabulary, ten rules, mode signatures, airborne rule, camera axes, path sentences, QA gate, procedure
- `scripts/check_spatial.py` (NEW): mode-aware gate on a ledger (line-lock run, lateral deviation, bearing sweep and coverage, level change, anchors, plant-and-absorb share)
- `scripts/lint_prompt.py` (CHANGED): warns when linear movement verbs outnumber spatial ones
- `examples/spatial/` (NEW): three ledgers (two reconstructed from prompt text, one illustrative redesign)

## 3. Test results on the ledgers

| Ledger | Result |
|---|---|
| `canyon_as_written` (reconstructed from prompt A) | FAIL: line-lock run 6, lateral 0.88 BL, bearing sweep 30 deg/10 s, anchors 1, bearing coverage 0.01 |
| `canyon_prompt_B_reconstructed` (my 'ceiling' prompt) | FAIL: line-lock run 3, anchors 1. Passes lateral, sweep, level, coverage |
| `canyon_3d_redesign` (illustrative) | PASS |

A metric error was found and fixed during the build: an earlier 'path linearity' check failed the 3D redesign because it measured the whole fight's drift along the canyon, not whether the fighters were collinear. It was replaced by circular variance of the duel-line bearing.

## 4. Patched files (exact changes)

### `SKILL.md` (2 changes)

**1. New rule 9: space is three-dimensional**

Old:
```text
never copy an example's posture, rhythm, or ending into a scene whose profile differs.
```

New:
```text
never copy an example's posture, rhythm, or ending into a scene whose profile differs.
9. **Space is three-dimensional.** Every fight starts with an arena card and a position ledger (x, y, z, facing, anchor per beat). Fighters traverse the arena, answer attacks with displacement (off-line, arc, pass, level change, push-off, terrain funnel), and change anchors. A fight confined to one line is a defect unless the mode calls for it (`references/spatial-tactics.md`).
```

**2. Route the spatial layer**

Old:
```text
| Fight, chase, weapons, multi-clip action | `references/action-modes.md`, `references/choreography.md`,
```

New:
```text
| Fight, chase, weapons, multi-clip action | `references/action-modes.md`, `references/spatial-tactics.md`, `references/choreography.md`,
```

### `core/pipeline.md` (2 changes)

**1. Director's Room writes the arena and ledger**

Old:
```text
**Context Profile and routing** (`context-routing.md`), choices,
```

New:
```text
**Context Profile and routing** (`context-routing.md`), **arena card and 3D position ledger** (`references/spatial-tactics.md`), choices,
```

**2. Design record carries the arena and ledger**

Old:
```text
`Context Profile and routed modes | Locked facts |
```

New:
```text
`Context Profile and routed modes | Arena card and position ledger | Locked facts |
```

### `core/context-routing.md` (2 changes)

**1. Space axis points at the arena card**

Old:
```text
| **Space** | confined, open, vertical, crowded, dark, unstable footing, moving platform (horse, boat, vehicle), weather |
```

New:
```text
| **Space** | confined, open, vertical, crowded, dark, unstable footing, moving platform (horse, boat, vehicle), weather. For any fight, build an arena card (`references/spatial-tactics.md`) |
```

**2. Add the spatial row to the routing table**

Old:
```text
| Fight pacing, initiative, pause legitimacy, fatigue, reach, terrain, fail-states | Purpose, power, state, space, tools, stakes | `references/action-modes.md` |
```

New:
```text
| Fight pacing, initiative, pause legitimacy, fatigue, reach, terrain, fail-states | Purpose, power, state, space, tools, stakes | `references/action-modes.md` |
| Fighter movement through the arena (3D ledger, footwork, path vocabulary, line-break rule) | Space, mode, tools | `references/spatial-tactics.md` |
```

### `references/choreography.md` (8 changes)

**1. Point choreography at the spatial layer**

Old:
```text
不是整场的节奏模板。
```

New:
```text
不是整场的节奏模板。**人在场内怎么走（场地卡、三维位置账本、走位路径、防直线规则）**由[空间战术](spatial-tactics.md)规定，编排任何交汇前必须先完成。
```

**2. Position is no longer one scalar distance**

Old:
```text
| 起点 | 双方距离、身体朝向、持械手、支撑或飞行方式 |
```

New:
```text
| 起点 | 三维位置（x,y,z）、与对方的相对方位角、距离、各自朝向、所依托的地物锚点、持械手、支撑或飞行方式（位置账本见[空间战术](spatial-tactics.md)） |
```

**3. Clarify that this row is the strike path**

Old:
```text
| 路径 | 从哪侧、什么高度、向哪个目标运动 |
```

New:
```text
| 招式路径 | 出招从哪侧、什么高度、向哪个目标运动（这是出招的路径，走位见下一行“位移”） |
```

**4. Add a mandatory displacement field to the action unit**

Old:
```text
| 应对 | 对方看见了什么，凭什么防、躲、截或硬接 |
```

New:
```text
| 应对 | 对方看见了什么，凭什么防、躲、截或硬接 |
| 位移（走位） | 此刻谁、沿什么路径（进退/离线侧闪/绕步/穿身/沉身/腾跃/借力蹬踏/逼入地形/绕障碍）移动到哪个位置、什么高度、哪个锚点。防守回应必须含位移；原地硬接须声明为“定桩承受”并给理由，且不超过三个回合中的一个 |
```

**5. State ledger gains Z and anchors**

Old:
```text
`角色位置/朝向｜支撑与姿态｜武器/物件持有者｜
```

New:
```text
`角色三维位置(x,y,z)与朝向｜所依托的地物锚点｜支撑与姿态｜武器/物件持有者｜
```

**6. Make the top-down check a mandatory ledger with a line-break rule**

Old:
```text
先用极简俯视图和数个关键姿态做通路检查。若拿掉镜头晃动与特效后仍无法说清谁打谁，先修编排，再美化画面。
```

New:
```text
编排前先写[场地卡](spatial-tactics.md)并建立三维位置账本，每个回合更新；若连续两个回合以上相对方位角几乎不变、且无高度或锚点变化，视为“直线对站”，必须改位移（可用 `scripts/check_spatial.py` 检查）。再用极简俯视图和数个关键姿态做通路检查。若拿掉镜头晃动与特效后仍无法说清谁打谁、人在场内怎么走，先修编排，再美化画面。
```

**7. Distance is one component of position**

Old:
```text
不能朝已经离开的空地挥完再让对方凭空受伤。
```

New:
```text
不能朝已经离开的空地挥完再让对方凭空受伤。距离只是位置的一个分量，不能代替位置：同样的距离可以出现在无数方位与高度上，方位角和高度必须写进位置账本。
```

**8. Link the airborne bullet to the airborne rule**

Old:
```text
空中：说明起跳/前一碰撞留下的动量、可用支点或能力推力；
```

New:
```text
空中：说明起跳/前一碰撞留下的动量、可用支点或能力推力（空中格挡成立的条件见[空间战术](spatial-tactics.md)的空中规则：借对方刃、墙、柱等的冲量蹬踏，或既定能力）；
```

### `references/action-modes.md` (5 changes)

**1. Point the modes at the spatial layer**

Old:
```text
Numbers below are starting points for a short-clip workflow. Test them on your model (`evals/cases.md`).
```

New:
```text
Numbers below are starting points for a short-clip workflow. Test them on your model (`evals/cases.md`).

**Where the fighters go** (arena, 3D position ledger, footwork, the line-break rule) is decided in `references/spatial-tactics.md` and is mandatory before any exchange is written. Each mode has a spatial signature there (section 6).
```

**2. Add the spatial signature as a mode parameter**

Old:
```text
| **Pause legitimacy** | When a separation or stand-off is allowed. **Resets are legitimate only if the mode or the fatigue state makes them meaningful** |
```

New:
```text
| **Pause legitimacy** | When a separation or stand-off is allowed. **Resets are legitimate only if the mode or the fatigue state makes them meaningful** |
| **Spatial signature** | How the mode occupies the arena: arcs, a shrinking radius, one clean line in, prescribed marks (`references/spatial-tactics.md` section 6) |
```

**3. Pressure gradient is 3D**

Old:
```text
Record start and end positions in body-lengths or landmarks.
```

New:
```text
Record start and end positions as (x, y, z) in the position ledger, not only as a distance; pressure that moves along one line is weaker than pressure that curves the defender around terrain.
```

**4. Reset test also catches linear oscillation**

Old:
```text
if two consecutive beats begin from the same positions, the mode has stalled.
```

New:
```text
if two consecutive beats begin from the same positions **or the same bearing and height**, the mode has stalled. A fight that oscillates along one line fails the line-break rule in `references/spatial-tactics.md` even though its positions differ.
```

**5. Procedure writes the arena first**

Old:
```text
4. Apply fatigue, reach, and environment adjustments.
```

New:
```text
4. Write the arena card and the position ledger (`references/spatial-tactics.md`), then apply fatigue, reach, and environment adjustments.
```

### `references/delivery-and-qa.md` (3 changes)

**1. Red line 4 covers path sentences**

Old:
```text
4. **Action reads as one connected chain** using temporal connectives (as, then, when, a beat later), not conditionals.
```

New:
```text
4. **Action reads as one connected chain** using temporal connectives (as, then, when, a beat later), not conditionals. Movement through space is written as **paths** (shape plus landmark or opponent-relative direction), not only as steps in and back.
```

**2. Add the spatial QA gate to the pre-delivery checklist**

Old:
```text
10. Verified, assumed, untested: labeled correctly, no result promises?
```

New:
```text
10. Verified, assumed, untested: labeled correctly, no result promises?
11. **Spatial gate** (any fight): is there an arena card and a position ledger? Does `python scripts/check_spatial.py ledger.json` pass for the mode (line-lock run, lateral deviation, bearing sweep and coverage, level change, anchors, plant-and-absorb share)? Does every defensive response include a displacement?
12. **Linear-verb check:** does `lint_prompt.py` report more linear moves (steps in or back, retreats) than spatial ones (circle, slip, pass, level change, push-off)? Does the camera use at least two axes relative to the duel line?
```

**3. Name the linear stand-and-fight failure**

Old:
```text
Label the failure type: identity, space, action, contact, light/optics, face, body, speech, sound.
```

New:
```text
Label the failure type: identity, space (including **spatial-linear**: a fight confined to one line), action, contact, light/optics, face, body, speech, sound.
```

### `references/camera-and-rhythm.md` (1 change)

**1. Camera axis variety so the 3D movement is visible**

Old:
```text
需要硬切时改用平台自己的分镜语法。
```

New:
```text
需要硬切时改用平台自己的分镜语法。

**镜头轴线要变化。** 摄影轴相对对战线（两人连线）至少用两种以上：90度侧拍、约45度三分之二、越肩后拍、高位或低位。固定的侧面剖面会把所有位移压平成一条线，掩盖横向与纵深移动。加入景深线索：前景遮挡物（岩石、柱子）、运动镜头的视差、可见的远墙、不同距离的物件；用低位或高位展示Z轴，让落点在跳跃后可见。模型不执行文字切镜时，用连续运动穿过多条轴线：环绕、升降、手持弧线、绕肩推近（见[空间战术](spatial-tactics.md)第7节）。
```

### `references/generation-handoff.md` (1 change)

**1. Seam includes 3D position and anchor**

Old:
```text
Position and facing, support and posture, held objects, injury and stamina, ability state, environment state, plus light direction, prop state, and distance for dialogue scenes.
```

New:
```text
Position (x, y, z) and facing, anchor, support and posture, held objects, injury and stamina, ability state, environment state, plus light direction, prop state, and distance for dialogue scenes.
```

### `lens/output-skeletons.md` (1 change)

**1. Slot 3 names the landmarks the fight uses**

Old:
```text
| 3 | Set and light physics | Space anchors and surfaces, named light sources
```

New:
```text
| 3 | Set and light physics | Space anchors and surfaces, **the named landmarks and heights the action will use**, named light sources
```

### `lens/lens-layer.md` (1 change)

**1. Add a path-sentence section to the Lens layer**

Old:
```text
(end of file)
```

New:
```text
## 9. Writing movement in space

Fighters move through three dimensions, and the prompt has to say how (`references/spatial-tactics.md`).

- A **path sentence** has three parts: where from (a landmark or an opponent-relative direction), what shape (arc, slip, pass, drop, spring, push-off), where to (a landmark or a relationship to the opponent).
- Prefer opponent-relative and landmark terms: "outside the right blade", "behind his shoulder", "around the boulder", "up the rock step", "with the sun behind him".
- Level changes are depicted, not named: "drops under the sweep and rolls to one knee", "springs onto the low rock, a full pace above him".
- A prompt in which most movement is "steps in", "steps back", "retreats half a step" keeps the fight on one line. `lint_prompt.py` warns on this pattern.
- Camera axis variety is part of the depiction: a fight filmed only in side profile looks linear whatever the ledger says.
```

### `evals/cases.md` (2 changes)

**1. Add the spatial eval case**

Old:
```text
| 19 | **Public vs private face:** the same bad news in a courtroom corridor vs a closed car | Display rules, mask strength |
```

New:
```text
| 19 | **Public vs private face:** the same bad news in a courtroom corridor vs a closed car | Display rules, mask strength |
| 20 | **Spatial navigation:** the same duel in an arena with three landmarks and a ledge, written with an arena card and ledger vs without | Lateral travel, bearing change, level change, anchor change |
```

**2. Add the spatial rubric lines**

Old:
```text
**Prompt quality** (all):
```

New:
```text
**Spatial** (case 20 and every fight): lateral travel is visible (a fighter leaves the initial line by about a body-length or more); the line between the fighters rotates; at least one level change (jump, drop, roll, climb); at least one change of anchor (a rock, post, wall, step); more than one camera axis; a response to an attack includes a displacement, not only a block. Also run `scripts/check_spatial.py` on the design ledger and compare its verdict with what you see.

**Prompt quality** (all):
```

### `README.md` (3 changes)

**1. Version**

Old:
```text
# ai-video-prompts v3.2
```

New:
```text
# ai-video-prompts v3.3
```

**2. README layout**

Old:
```text
references/  action-modes.md  Ten fight modes with pacing, fatigue, reach, terrain, fail-states
```

New:
```text
references/  action-modes.md  Ten fight modes with pacing, fatigue, reach, terrain, fail-states
             spatial-tactics.md  Arena card, 3D position ledger, path vocabulary, line-break rules, spatial QA gate
```

**3. README layout**

Old:
```text
              check_skill.py
```

New:
```text
              check_spatial.py               Spatial QA gate on a fight's position ledger (design check)
              check_skill.py
```

### `MIGRATION.md` (1 change)

**1. Migration notes**

Old:
```text
# Migration: v1 to v3.2

```

New:
```text
# Migration: v1 to v3.3

## v3.3 changes (Spatial Tactics and 3D Footwork)

- **Diagnosis:** the skill defined position as one scalar distance plus facing, so fights collapsed onto one line. The QA checklist had no spatial item, and the "reset test" caught only identical start positions.
- **New layer** (`references/spatial-tactics.md`): a mandatory arena card, a 3D position ledger (x, y, z, facing, anchor per beat), a path vocabulary (off-line slip, arc, pass, level down and up, anchor push-off, terrain funnel, obstacle play), ten rules including the line-break rule and a displacement answer for every defense, spatial signatures per mode, an airborne rule, camera-axis variety, and a QA gate.
- **Action unit** changed: "起点" now carries 3D position and bearing; a mandatory "位移（走位）" field was added; the state ledger gains Z and anchors.
- **Tools:** `scripts/check_spatial.py` (checks a ledger; mode-aware) and a linear-movement warning in `lint_prompt.py`.
- **Findings on the test clips:** a ledger reconstructed from prompt A fails five checks; one reconstructed from my "ceiling" prompt B fails two (a three-beat line-lock run, a single anchor), so B only partly fixes the problem; an illustrative 3D redesign passes. Reconstructions are from prompt text, not measured from any clip.
- **Patched files** and exact text are in `PATCHES-v3.3.md`.

# Migration: v1 to v3.2

```
