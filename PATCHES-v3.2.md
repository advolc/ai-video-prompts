# v3.2 Patch Report: Context-Aware Routing

This report lists every change made after v3.1, with the exact old and new text. Files marked NEW were created whole. Each change shows the anchor text that was replaced (`Old`) and what it became (`New`). For appended sections, `Old` is the end of the file.

## 1. Audit: where v3 was one-size-fits-all

| Area | Finding | Where | Fix |
|---|---|---|---|
| Fight pacing | Every fight is a closed exchange: attack, block, step back, reset. No initiative, pressure, overlap or consequence accumulation | `references/choreography.md` (action unit, 'handover'); `references/prompts-and-segments.md` (前冲→接触→分开→再接触) | New `action-modes.md` (10 modes); unit gains initiative and trace fields; the closed loop is labeled duel-only |
| Tier A density | One universal number ('about 3 per ~5 s') for a stealth kill and a brawl alike | `SKILL.md`, `core/pipeline.md`, `references/generation-handoff.md` | Density and splitting are set by the mode |
| Fatigue | Stamina is a ledger field with no effect on tempo, guard, or breath | `references/choreography.md` (state ledger) | Fatigue routing table; ledger sentence made behavioral |
| Reach and terrain | Weapon specs exist, but reach and terrain never change pacing | `references/choreography.md` | Reach and environment routing tables in `action-modes.md` |
| Rhythm | A menu of curves, no router | `references/camera-and-rhythm.md` (规划节奏) | Rhythm routed by mode; camera stance table (observe, participate, subjective) |
| Dialogue physicality | Every scene is seated and calm: one dyad table, one coverage table, one tea example | `lens/body-and-status.md`, `dialogue/conversation-units.md` | `dialogue/situation-profiles.md` (13 profiles); seated templates labeled profile A; section 13 situation routing |
| Speech timing | One pace (2–3 words/s) and one silence share (20–35%) for all states | `dialogue/conversation-units.md` | Pace by arousal; silence share by situation |
| Unit skeleton | One five-stage skeleton (gambit→exit) for every exchange | `dialogue/conversation-units.md` | Labeled formal-exchange only; skeletons per situation |
| Face display | One mask/leak model regardless of audience, arousal, or fatigue; 'one leak' as a flat rule | `lens/face-pass.md` | Section 10 display rules; leak count conditional |
| Look and light | Presets and mood independent of the scene's purpose and privacy | `lens/optics-and-stock.md`, `lens/physical-light.md` | Context-to-look table; mood and context light table |
| Output shape | Fixed slot weights; length by duration only; every example ends on a still hold | `lens/output-skeletons.md` | Scene-type weighting, words per second by event density, four end-state modes |
| Sound | Universal layering; no routed silence | `sound/sound-and-voice.md` | Routed sound strategy |
| Tests and examples | Evals and examples cover mostly duels and tables | `evals/cases.md`, `examples/` | Cases 14–19, a mode-fit rubric line, profile labels on every example, six routed examples |

## 2. New files

- `core/context-routing.md`: Context Profile (10 axes), what it routes, resolution rules, unknown-profile handling, anti-template rule
- `references/action-modes.md`: Ten fight modes with parameters, cross-mode grammar, fatigue, reach and environment routing, procedure
- `dialogue/situation-profiles.md`: 13 situation profiles, speech timing by arousal, skeletons, physical-state modifiers
- `examples/context-routing-examples.md`: Six routed cases and two Compact prompts (lint-clean)

## 3. Patched files (exact changes)

### `SKILL.md` (6 changes)

**1. Add the routing step to the pipeline entry**

Old:
```text
Output is an internal design record. It never appears in the prompt. See `core/pipeline.md`.
```

New:
```text
**First build the Context Profile and route** (`core/context-routing.md`): purpose, power, body state, space, audience, relationship, tools, tone, stakes. The profile picks the action mode, the situation profile, the display rules, the camera stance, and the look. Output is an internal design record. It never appears in the prompt. See `core/pipeline.md`.
```

**2. New rule 8: route before writing**

Old:
```text
7. **Protect explicit user targets.** If one competes with something else, offer options and wait; never silently downgrade.
```

New:
```text
7. **Protect explicit user targets.** If one competes with something else, offer options and wait; never silently downgrade.
8. **Route by context.** There is no default scene. A fight is a duel, a last stand, a stealth takedown, a sparring match, or another mode; a conversation is a seated exchange, a street argument, a farewell, or another situation. Build the Context Profile first; never copy an example's posture, rhythm, or ending into a scene whose profile differs.
```

**3. Tier A density is no longer one universal number**

Old:
```text
| A: story and contact | Attack/defense/transfer events, outcomes, ability use | Strict: about 3 independent interactions per ~5 s of runtime; split clips beyond that |
```

New:
```text
| A: story and contact | Attack/defense/transfer events, outcomes, ability use | Strict, and **mode-dependent**: density comes from the action mode (`references/action-modes.md`). A duel may run 1–3 interactions per ~5 s, a last stand 2–4 overlapping, a stealth takedown 0–1 per clip. Split clips beyond the mode's density |
```

**4. Route the router file as always-read**

Old:
```text
| Any prompt output (always) | `core/pipeline.md`, `lens/lens-layer.md`, `lens/output-skeletons.md` |
```

New:
```text
| Any prompt output (always) | `core/pipeline.md`, `core/context-routing.md`, `lens/lens-layer.md`, `lens/output-skeletons.md` |
```

**5. Dialogue routing file**

Old:
```text
| Any spoken line, monologue, negotiation, confrontation | `dialogue/spoken-register.md`, `dialogue/conversation-units.md`, then
```

New:
```text
| Any spoken line, monologue, negotiation, confrontation | `dialogue/situation-profiles.md`, `dialogue/spoken-register.md`, `dialogue/conversation-units.md`, then
```

**6. Action modes file**

Old:
```text
| Fight, chase, weapons, multi-clip action | `references/choreography.md`,
```

New:
```text
| Fight, chase, weapons, multi-clip action | `references/action-modes.md`, `references/choreography.md`,
```

### `core/pipeline.md` (4 changes)

**1. Director's Room starts with routing**

Old:
```text
| Director's Room | The user's story, constraints, references | Choices, contact and support,
```

New:
```text
| Director's Room | The user's story, constraints, references | **Context Profile and routing** (`context-routing.md`), choices, contact and support,
```

**2. Replace the universal '3 per 5 s' with mode-dependent density**

Old:
```text
- Guideline: about **3 independent interactions per ~5 s** of runtime. This calibrates to short clips; scale after testing on your model and duration.
```

New:
```text
- Density is **mode-dependent** (`references/action-modes.md`): a duel about 1–3 independent interactions per ~5 s, a last stand 2–4 with overlap, an ambush 3 or more in the first 2 s, a stealth takedown 0–1 per clip, a ritual duel 0–2. These are starting points for short clips; scale after testing on your model and duration.
```

**3. Design record carries the profile**

Old:
```text
`Locked facts | Added texture | Beats and status shifts |
```

New:
```text
`Context Profile and routed modes | Locked facts | Added texture | Beats and status shifts |
```

**4. Splitting follows the mode**

Old:
```text
Split by Tier A. Within a clip, B and C are unlimited.
```

New:
```text
Split by Tier A **as set by the action mode** (a stealth approach and its strike stay one unit; a last stand chains clips). Within a clip, B and C are unlimited.
```

### `references/generation-handoff.md` (1 change)

**1. Splitting rules per mode**

Old:
```text
- **Guideline:** about 3 independent interactions per ~5 s of runtime. This calibrates to short clips on current-generation models; scale after testing at your real duration.
```

New:
```text
- **Density depends on the action mode** (`references/action-modes.md`), not on one number: duel 1–3 per ~5 s, last stand 2–4 with overlap, ambush 3 or more in the first 2 s then 1–2, sparring 1–2, stealth 0–1 per clip, ritual 0–2. Starting points for short clips; scale after testing at your real duration.
- **Splitting by mode:** a duel splits by exchange pairs; a last stand chains clips and carries stamina and injury in the seam; a stealth takedown keeps approach and strike in one unit; an ambush splits burst from aftermath; sparring splits by teaching beat; a flight fight splits by terrain segment.
```

### `references/choreography.md` (5 changes)

**1. Point the universal physics page at the router**

Old:
```text
# 动作编排、武指与状态连续

## 从角色的选择开始
```

New:
```text
# 动作编排、武指与状态连续

> **情境路由：** 本页是通用的物理与因果规则（选择、兵器、发力链、距离、接触、状态）。整场打斗的**节奏、主动权、停顿是否合法、体力曲线、距离与环境影响、失败态**由[动作模式](action-modes.md)按[情境档案](../core/context-routing.md)路由；下方“动作单元”是记录一次交汇的格式，不是整场的节奏模板。

## 从角色的选择开始
```

**2. Link choices to modes**

Old:
```text
竞技可以强调得分条件与剩余时间。
```

New:
```text
竞技可以强调得分条件与剩余时间。整场的节奏、主动权与停顿是否合法，不在本页规定，由[动作模式](action-modes.md)按情境路由。
```

**3. Add initiative and consequence fields to the action unit**

Old:
```text
| 衔接 | 收势如何变成下一动作，而非瞬间复位 |
```

New:
```text
| 衔接 | 收势如何变成下一动作，而非瞬间复位；是否与上一动作重叠由动作模式决定 |
| 主动权 | 此刻谁掌控局势，是否因本次交汇易手，原因是什么 |
| 代价与痕迹 | 体力、站位、地形或装备留下了什么，会怎样改变下一动作 |
```

**4. Stop the closed exchange from being the universal template**

Old:
```text
省略行程可以加速，不能省略决定胜负的机制后再假装它已解释清楚。
```

New:
```text
省略行程可以加速，不能省略决定胜负的机制后再假装它已解释清楚。同一单元格式适用于所有模式；但“交汇后分开、重置、再交汇”只是对决模式的节奏，困兽之斗、潜入、伏击、对练等按[动作模式](action-modes.md)处理重叠、停顿与终态。
```

**5. Make stamina change behavior**

Old:
```text
愤怒可以改变判断，不能自动治好腿。
```

New:
```text
愤怒可以改变判断，不能自动治好腿。体力与伤势须按[体力路由](action-modes.md)改变速度、防守高度、步幅与呼吸，而不只是登记在账本里。
```

### `references/prompts-and-segments.md` (1 change)

**1. Mark the default splitting as duel-specific**

Old:
```text
## 单段单事件的默认拆法

复杂接触未验证时，
```

New:
```text
## 单段单事件的默认拆法（对决类情境；其他模式见动作模式）

本节的“前冲—接触—分开—再接触”拆法对应对决类、复杂接触未验证的情境。潜入、困兽、伏击、对练、混战等按[动作模式](action-modes.md)的拆分规则处理，不套用这套节拍。复杂接触未验证时，
```

### `references/camera-and-rhythm.md` (2 changes)

**1. Rhythm is routed, not a single curve**

Old:
```text
## 规划节奏

先写信息节拍，
```

New:
```text
## 规划节奏

节奏曲线由情境档案与动作模式决定（[情境路由](../core/context-routing.md)、[动作模式](action-modes.md)）：对决可有起伏与停顿，困兽之斗是持续压迫，潜入是漫长接近加一次接触，对练允许纠错停顿，仪式性对决由规矩规定停顿。下文各点是菜单，不是统一曲线。

先写信息节拍，
```

**2. New camera stance section routed by context**

Old:
```text
## 声音与台词时间
```

New:
```text
## 镜头姿态：旁观、参与、主观（按情境路由）

镜头姿态由情境档案决定，不是统一设定。

| 姿态 | 适用情境 | 做法 | 避免 |
|---|---|---|---|
| 旁观 | 仪式性对决、潜入、压倒性优势、正式谈话、庄重告别 | 固定或缓慢移动，较长焦距或对称广角，景别变化少，让动作在画内发生 | 全程旁观，把整场打斗拍成侧面剖面的舞台 |
| 参与 | 困兽之斗、伏击、混战、街头争吵、逃亡 | 手持贴近，随受力抖动，低位俯冲、推近、甩镜绕肩；视线跟着危险走，被刀光逼退 | 无动机乱晃；遮住关键接触 |
| 主观 | 恐惧、负伤、醉酒、眩晕、濒死 | 以角色视线、焦点收窄、失焦、呼吸晃动表达状态 | 用模糊遮盖失败的动作；不交代就回到客观视角 |

姿态在**转折点**切换，例如对练转真打时由旁观转参与；切换要有诱因（一击见血、一声喊叫）。若所用模型不执行文字写的“切镜”（已有实测被渲染为连续镜头），参与感改用连续的镜头运动表达：手持后退、低位俯冲、推近、绕肩甩镜；需要硬切时改用平台自己的分镜语法。

## 声音与台词时间
```

### `sound/sound-and-voice.md` (1 change)

**1. Append routed sound strategy**

Old:
```text
(end of file)
```

New:
```text
## 按情境路由的声音策略

声音密度与静默由情境档案决定，不是统一铺满：

- **潜入/暗杀：** 近乎静默，只留一个受控的声音（靴底碎石、一口气），让静默成为张力。
- **困兽之斗：** 破碎的呼吸、衣物、持续的撞击，不给安静的恢复。
- **对练：** 木器或软器的轻响，随口的交谈、笑。
- **仪式性对决：** 近乎寂静，一个仪式性的声音，规矩被破坏时声音才破。
- **街头争吵：** 人群、叫喊、重叠的话语，声音多层。
- **告别：** 环境声拖长，人离开后保留一段空间的声音（站台、门外的风）。
- **耳语/秘密：** 呼吸占主导，环境里的响动制造威胁。
- **事后喘息：** 呼吸、金属落地、衣物摩擦，台词被呼吸切断。

选择一项主声音，其余让位；原生音频是否可用仍以实测为准。
```

### `lens/body-and-status.md` (3 changes)

**1. Mark the dyad table as seated-formal only**

Old:
```text
## 8. Dyad templates (starting points, adapt to the story)
```

New:
```text
## 8. Dyad templates for seated and formal scenes (situation profile A)

These templates assume furniture and a table. For standing, walking, public, farewell, whispered, and post-exertion scenes, use `dialogue/situation-profiles.md` and section 13 below.
```

**2. Label the example's profile**

Old:
```text
## 9. Example: the tea scene as a beat timeline
```

New:
```text
## 9. Example: the tea scene as a beat timeline (profile A, seated formal)
```

**3. Add situation routing to the body and status pass**

Old:
```text
(end of file)
```

New:
```text
## 13. Situation routing

The vocabulary above was first built for seated scenes. Adapt it by situation (`dialogue/situation-profiles.md`); do not import seated business into a standing or moving scene.

| Situation | How status and behavior change |
|---|---|
| Standing | Status shows in weight, space, and who moves. The dominant moves less and chooses where to stand; the subordinate adjusts, shifts, and fills silence. Hands are visible, still, or occupied with a purposeful object |
| Walking | Pace, lead and follow, and alignment carry status. Slowing or stopping is a status move; speeding up is an escape; stepping into the other's path is confrontation |
| Public with onlookers | Status is performed for the audience; volume drops, gestures shrink, and the rupture is a status event when a mask fails |
| High arousal | Status signals compress. Composure becomes the signal of status; losing it is a status loss and can be the turn |
| Exhausted or injured | Status goes to whoever can still stand, support the weight, and speak clearly; leaning, sitting, and breath are status facts |
| Intimate or private | Status flattens; distance, touch, and who initiates are the vocabulary |
| Confined space (car, kitchen, elevator) | Avoidance is gaze and posture; whoever blocks the exit or drives holds the status |
| Moving platform (horse, boat, cart) | Balance and control of the platform are status; who holds the reins, the oar, or the wheel |

Rules: choose the situation first; props must exist in the setting; a cup is one choice, not the default business; status in motion is shown by space and pace before hand business; when the situation changes, the status vocabulary changes with it.
```

### `lens/face-pass.md` (2 changes)

**1. Leak count is conditional, not a flat one**

Old:
```text
- A leak is **one** small thing. Do not stack three leaks.
```

New:
```text
- A leak is a small, specific thing. How many a face can hold depends on context: a calm public mask holds one; high arousal, exhaustion, or high stakes make the mask fail in more channels (section 10), but always in an order the viewer can follow, never all at once.
```

**2. Add display rules routed by audience and state**

Old:
```text
(end of file)
```

New:
```text
## 10. Display rules: who is watching

People manage their faces by context. The same news looks different in a closed car and in a courtroom corridor. Route the face by **audience, relationship, arousal, fatigue, and stakes** (`core/context-routing.md`).

| Context | Mask | Where the leak shows | Recovery | Notes |
|---|---|---|---|---|
| Private, intimate | Low or none | Everywhere; large, unguarded expressions, crying, laughter | Slow | The mask is lowered; closeness allows big expressions |
| Semi-public (colleagues, neighbors) | A professional or social mask | Eyes, hands, voice, breath; small | Moderate | The courtesy smile or flat politeness holds, with a lag |
| Public with an audience (court, ceremony, crowd) | Strong; flat or composed | Jaw, throat, hands, posture; the face stays disciplined | Fast | Wider shots let the body carry it; close shots catch the tight margins |
| Under authority or threat | Deferential or blank | Brows and mouth for an instant, masked at once | Very fast | Gaze lowered; compliance on the surface |
| Among enemies | Stoic composure; contempt may show | Controlled; a flicker of satisfaction or fear | Fast | The mask is a weapon |
| Performing a deception | Over-smooth | The leak is **timing** (a late smile, a too-long pause), not intensity | Moderate | A smooth face can be the tell |

**Modifiers.**
- **Arousal and exhaustion** reduce masking capacity: leaks appear in more channels and recovery slows. A worn face is slack, with heavy lids and slower expression changes.
- **Stakes** scale expression: low stakes, small expressions; high stakes, larger ones or harder suppression.
- **Public and private versions of the same beat:** write the public mask first, then the private after-beat when the door closes (the face drops, the breath breaks). The after-beat suits a close shot.
- **Culture and era:** display rules differ across cultures and periods (whether grief or anger is shown in public, how contempt is signalled). Do not assume. Pick what fits the established world and label the assumption outside the copy block.
- **Do not invent a mask where none is motivated.** If nobody is watching and nothing is at stake, let the face move.

Shot size routing still applies (section 7): a public mask suits wider shots where the body does the work; a private leak suits a close-up.
```

### `lens/optics-and-stock.md` (2 changes)

**1. Presets are examples**

Old:
```text
## 8. Look presets (starting points, adjust to the story)
```

New:
```text
## 8. Look presets (examples of context-to-look mappings; see section 10 to route)
```

**2. Add context routing for lens and look**

Old:
```text
(end of file)
```

New:
```text
## 10. Routing the look from context

Choose the look from the Context Profile (`core/context-routing.md`). These are **leanings**, not rules; confirm per model.

| Context | Lens and camera leaning | Light and grade leaning |
|---|---|---|
| Intimate talk, confession | 85–100 mm, shallow depth of field, locked or a very slow push | Single warm practical, deep shadow, fine grain |
| Panic, ambush, chaos | 24–35 mm handheld, narrow shutter, camera as participant | High contrast, coarse grain, harsh or mixed light |
| Stealth | Long lens from distance, a slow creep or locked, one close detail at the contact | One hard source, deep shadow, cool and low saturation |
| Ritual, formal | Wide, symmetrical, locked, slow push; anamorphic or clean spherical | Even stable light, restrained palette |
| Public argument | 28–35 mm handheld, deep focus for crowd layers | Ambient daylight or street light, natural contrast |
| Farewell | 85–135 mm compression, lingering locked frame; a hold after the departure | Soft backlight, low contrast, lifted blacks |
| Dominance and menace | A lower angle, steady, modest lens; the dominant given room and the other cropped | Directional light with a clean edge on the dominant |
| Grief | 50–85 mm, steady, patient | Soft window light, low saturation |
| Comic | Wider, brighter, stable framing | High key, saturated, clear |
| Horror | Slow push, off-center framing, space left empty | Shadows, a motivated source that does not reveal everything |

If the scene changes profile mid-clip, the look may shift at the turn; write it as a depicted change (the light narrows, the lens pushes in), not as a second look anchor.
```

### `lens/physical-light.md` (1 change)

**1. Add light routing by mood and context**

Old:
```text
(end of file)
```

New:
```text
## 12. Mood and context routing

Light should answer the Context Profile (`core/context-routing.md`), not a preset.

| Context | Lighting behavior |
|---|---|
| Private, intimate | Small warm sources; the light pool shrinks with closeness; shadows hold the edges |
| Public, formal | Even, structural light (ceiling, daylight, windows); little shadow drama |
| High stakes | More contrast; a single hard source; deeper shadow |
| Low stakes, comic | High key, even, saturated |
| Public humiliation or exposure | Flat bright light that hides nothing |
| Stealth | One hard source, cool or night; deep shadow; the subject at the edge of the light |
| Dominance | A clean edge light on the dominant; the other in softer or mixed light |
| Grief | Soft window light, low contrast |
| Time pressure | Moving or changing light (a flickering lamp, passing headlights) only if the source exists |

The sources named in the scene stay consistent; routing chooses how they are used (how close, how hard, how much), never invents a new one.
```

### `lens/output-skeletons.md` (4 changes)

**1. Slot 4 weight depends on scene type**

Old:
```text
| 4 | Performance timeline | Time-ordered beats: body, hands, gaze, face, prop business, listener, spoken lines with delivery, and any Tier A contact events written as one recordable chain | ~55–65% of the text |
```

New:
```text
| 4 | Performance timeline | Time-ordered beats: body, hands, gaze, face, prop business, listener, spoken lines with delivery, and any Tier A contact events written as one recordable chain | Weight set by scene type (section 11); about 55–65% for dialogue-driven and mixed scenes |
```

**2. End state is not always a still hold**

Old:
```text
| 7 | End state | The final frame: positions, posture, held objects, light, what holds still. Doubles as the seam into the next clip | 1–2 sentences |
```

New:
```text
| 7 | End state | The final frame or the handoff state (end modes in section 11): positions, posture, held objects, light. It may hold still or leave motion in progress. Doubles as the seam into the next clip | 1–2 sentences |
```

**3. Length scales with event density, not time alone**

Old:
```text
That is a single data point, so treat it as a hypothesis and test it with `evals/cases.md` case 10.
```

New:
```text
That is a single data point, so treat it as a hypothesis and test it with `evals/cases.md` case 10. It describes a **dense, multi-event** clip; sparse scenes (stealth, atmosphere, a held look) need fewer words per second, and padding them with invented activity breaks their mode (section 11).
```

**4. Add scene-type weighting and end-state modes**

Old:
```text
## 11. Before delivery
```

New:
```text
## 11. Scene-type weighting and end-state modes

Slot weights and length follow the **scene type**, set by the Context Profile.

| Scene type | Emphasis | Words per second (rough lean) |
|---|---|---|
| Action-dominant (fight, chase) | Slot 4 with the Tier A chain about 60–70%; slot 5 camera 2–5 sentences; slot 6 impact and breath; slot 3 compact | 25–35 for dense multi-shot |
| Dialogue-dominant | Slot 4 beats and speech about 60–70%; slot 2 faces; camera 1–3 sentences | 15–30, by the speech pace |
| Intimate or emotional | Slots 2 (skin, face) and 4 (face beats) heavier; soft light; few words of action | 15–25 |
| Stealth, atmosphere, establishing | Slots 3 and 6 (space, light, sound) about 40–50%; slot 4 sparse; long holds | 10–20 |
| Insert, transition, montage | Compact-leaning; one image per sentence | n/a |

**End-state modes** (pick one; do not end every clip on a still hold):

| Mode | Use | How to write the last sentence |
|---|---|---|
| Hold | A scene that closes, a ritual, a farewell after the departure, an aftermath | Positions and light settle; a held frame |
| Handoff in motion | Last stand, chase, brawl, ambush burst | The last sentence leaves motion in progress with the state that carries into the next clip |
| Cut on action | An impact or an entry | The clip ends at the moment of contact or entry; the next clip opens on the result |
| Reveal | A twist or a discovery | The last image shows the new information |

A still hold at the end of a chase or last stand tells the model the fight has stopped. The examples in this skill end on holds because their profiles are hold-type.

## 12. Before delivery
```

### `dialogue/conversation-units.md` (5 changes)

**1. The five-stage skeleton is formal-exchange only**

Old:
```text
## 2. Unit skeleton

| Stage |
```

New:
```text
## 2. Unit skeleton

This is the skeleton for a **formal exchange** (situation profiles A and B in `situation-profiles.md`). Other situations (street argument, farewell, confession, interrogation, walking talk, post-exertion) use their own skeletons in `situation-profiles.md` section 3.

| Stage |
```

**2. Pace depends on arousal**

Old:
```text
with pauses taking more. Plan with these as estimates, then read it aloud.
```

New:
```text
with pauses taking more. These figures are for **calm speech**. Other states change the pace (hot anger, whisper, grief, breathless, panic): use the table in `situation-profiles.md` section 2 and plan with the pace of the character's state. Then read it aloud.
```

**3. Silence share depends on the situation**

Old:
```text
- Silence takes about **20–35%** of a dialogue clip. Do not fill it.
```

New:
```text
- Silence share depends on the situation: about 5–15% in a street argument or banter, 20–35% in a formal exchange, 35–55% in a farewell or a confession (`situation-profiles.md`). Do not fill the silence the situation needs.
```

**4. Coverage table is seated-only**

Old:
```text
## 6. Coverage inside a unit

| Moment |
```

New:
```text
## 6. Coverage inside a unit

The table below is for a seated two-person exchange. Other situations route the camera by profile: handheld and participant for a street argument, tracking beside or in front for a walking talk, a long lens and a hold after the departure for a farewell, tight and low-key for a whisper (`situation-profiles.md`).

| Moment |
```

**5. Checklist asks for the situation profile**

Old:
```text
- [ ] Does the unit have a single turn?
```

New:
```text
- [ ] Is the situation profile named, and do movement, distance, pace, and silence match it (not a default table)?
- [ ] Does the unit have a single turn?
```

### `evals/cases.md` (2 changes)

**1. Add routing cases to the eval set**

Old:
```text
| 13 | **Dialogue framing:** the same two lines in a medium-wide, a medium, and a close shot | Lip sync, face acting, listener beats |
```

New:
```text
| 13 | **Dialogue framing:** the same two lines in a medium-wide, a medium, and a close shot | Lip sync, face acting, listener beats |
| 14 | **Stealth takedown:** an assassin and a sleeping target, 15 s | Mode fit: one contact, silence, no flurry |
| 15 | **Last stand:** a wounded guard against a squad, 20 s | Overlap, fatigue, no clean resets, accumulating consequence |
| 16 | **Sparring:** master and student, 15 s | Legitimate pauses, light contact, play |
| 17 | **Street argument:** two people in a public lane, 15 s | Movement, overlap, onlookers, high arousal |
| 18 | **Farewell:** a platform or doorway, 15 s | Delay, silence 35–55%, hold after the departure |
| 19 | **Public vs private face:** the same bad news in a courtroom corridor vs a closed car | Display rules, mask strength |
```

**2. Add mode-fit rubric line**

Old:
```text
**Prompt quality** (all):
```

New:
```text
**Mode and situation fit** (cases 14–19): pacing, pauses, and fail-state match the mode (a stealth clip is quiet and singular; a last stand has no clean resets); movement, distance, pace, and silence match the situation (a farewell is not seated); the mask matches the audience; the clip does not end on a still hold unless the profile calls for it.

**Prompt quality** (all):
```

### `examples/v3-extended-examples.md` (3 changes)

**1. Label example 1 with its profile**

Old:
```text
**Design record (internal, not in the prompt):**
- Locked: Chen superior,
```

New:
```text
**Profile:** situation A (seated formal) | Purpose: expose a failure and test composure | Power: Chen high, Wu low | Audience: none | End mode: hold.

**Design record (internal, not in the prompt):**
- Locked: Chen superior,
```

**2. Label example 2 with its profile**

Old:
```text
**设计记录（内部）：**
```

New:
```text
**情境档案：** 动作模式：对决（守门的僵持，一方隐藏伤势）｜终态：定格。若改为困兽之斗，节奏会不同（见 `context-routing-examples.md` 第2例）。

**设计记录（内部）：**
```

**3. Label example 3 with its profile**

Old:
```text
**Design (internal):** Mask: calm and level.
```

New:
```text
**Profile:** display rules: among enemies, strong mask | shot: close | End mode: hold.

**Design (internal):** Mask: calm and level.
```

### `README.md` (6 changes)

**1. Version**

Old:
```text
# ai-video-prompts v3.1
```

New:
```text
# ai-video-prompts v3.2
```

**2. Describe routing in the README**

Old:
```text
Texture Authority: story facts are **locked**;
```

New:
```text
**Context-Aware Routing:** before anything is written, the Director's Room builds a Context Profile (purpose, power, body state, space, audience, relationship, tools, tone, stakes) that routes to an action mode, a dialogue situation, display rules, a camera stance, and a look. There is no default scene.

Texture Authority: story facts are **locked**;
```

**3. README layout**

Old:
```text
             precedence.md    Resolution examples for the single ladder
```

New:
```text
             precedence.md    Resolution examples for the single ladder
             context-routing.md  Context Profile and routing to modes, situations, display rules, camera, look
```

**4. README layout**

Old:
```text
             conversation-units.md    Multi-turn units, timing math, coverage, seams
```

New:
```text
             conversation-units.md    Multi-turn units, timing math, coverage, seams
             situation-profiles.md    13 situation profiles: movement, pace, silence, camera
```

**5. README layout**

Old:
```text
references/  Director's Room systems: choreography,
```

New:
```text
references/  action-modes.md  Ten fight modes with pacing, fatigue, reach, terrain, fail-states
             Director's Room systems: choreography,
```

**6. README layout**

Old:
```text
examples/     v3-extended-examples.md
```

New:
```text
examples/     context-routing-examples.md    Six routed cases (stealth, last stand, sparring, street argument, farewell, public/private)
              v3-extended-examples.md
```

### `MIGRATION.md` (1 change)

**1. Migration notes**

Old:
```text
# Migration: v1 to v3.1

```

New:
```text
# Migration: v1 to v3.2

## v3.2 changes (Context-Aware Routing)

- **Context Profile and router** (`core/context-routing.md`): every scene is profiled before writing; nothing defaults to a template scene.
- **Action modes** (`references/action-modes.md`): ten fight modes (duel, last stand, stealth, sparring, ambush, dominance, flight fight, brawl, group melee, ritual duel) with their own rhythm, density, initiative, pause legitimacy, fatigue, reach, terrain, and fail-states. The closed exchange is the duel mode only. Tier A density is mode-dependent, not "about 3 per 5 s".
- **Situation profiles** (`dialogue/situation-profiles.md`): 13 conversation situations (seated formal, standing, street argument, walking, farewell, confession, interrogation, public address, whisper, confined space, bedside, post-exertion, banter) with movement, pace by arousal, silence share, skeletons, and camera. The tea scene is profile A only.
- **Display rules** (`lens/face-pass.md` section 10): mask strength by audience, relationship, arousal, fatigue, and stakes; public and private versions of one beat.
- **Camera stance** routed (observe, participate, subjective); **look and light** routed by context; **slot weights and end-state modes** by scene type (not every clip ends on a still hold).
- **Patched** in place: `choreography.md`, `prompts-and-segments.md`, `camera-and-rhythm.md`, `sound-and-voice.md`, `body-and-status.md`, `conversation-units.md`, `optics-and-stock.md`, `physical-light.md`, `output-skeletons.md`, `generation-handoff.md`, `pipeline.md`, `SKILL.md`. The exact changes are in `PATCHES-v3.2.md`.
- **Evals:** cases 14–19 and a mode-fit rubric line.

# Migration: v1 to v3.1

```
