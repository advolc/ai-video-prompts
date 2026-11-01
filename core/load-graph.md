---
id: "load-graph"
layer: "core"
priority: "P0"
depends_on: []
conflicts_with: []
load_when: ["按需加载图"]
not_for: []
---

# 按需加载图


## 解释与预算
路由→裁决→必需内容→递归补 depends_on→过滤 not_for/未授权→拓扑排序。P0先于P1先于P2先于P3，同级按任务相关性；加载依赖后才能使用依赖者。单轮新增内容模块≤6；已读规则摘要复用，后续阶段逐步换入，不同一轮堆全库。

core/ux 是入口控制元数据：其必要规则已摘要于SKILL，初始化时读取，稳定后不每轮重读；预算计本轮新读的专业内容文件，不能用此定义把整套参考伪装成控制元数据。若首次既要初始化又要复杂任务，先完成初始化，再加载内容阶段，切勿一次读全目录。正文中的表和链接是索引，不是隐式读取授权。

超额时只移出非必需分支及其依赖；先骨架再深化，但同一回复内换阶段不重置6个新增内容文件的总预算。核心检查优先使用SKILL已载入条文及此前摘要，确需新读必需文件时移出非必需深化项，不能截掉依赖或防偷懒。截断对用户静默，不说已省略哪个模块；若影响用户所求结果，用自然语言说明阶段范围，不能静默删掉需求，也不能扣留用户已要的全量文字。模块名不是对外话术。

## 方向明确的打戏风格例
“做一段张艺谋风格打戏”的内容集合恰好6项：`color-system, composition, visual-style-library-zhang-yimou, choreography, prompts-and-segments, anti-lazy-and-delivery`。风格卡提供初步光向与材质，不再强依赖lighting/world-and-style。此轮先按SKILL已载入的交付与完成条件检查平台、参考、声音、起止和自足性，不默认再读第7个文件；若本次平台问题确需新读generation-handoff，优先复用此前摘要，或将非必需的美学深化留到下一轮，先保必需交接。不能把6份风格设计当平台能力已验证。
此处优先级：为路由加载的P0仅表示该阶段内容，不改变主技能原P0/P1/P2质量含义。

## 原模块默认映射（未补头部时使用；补齐后以头部为准）

本表只列尚未补 frontmatter 的旧模块；新增分层模块（core/ux/visual/narrative/production/sound/post/distribution/management/quality）的 layer 与 depends_on 一律以各自文件头部为准，不在本表重复。旧模块补头部后，以头部覆盖本表。

| id | layer | depends_on |
|---|---|---|
| inspiration-wizard | ux | [] |
| inspiration-library | ux | [] |
| anti-lazy-and-delivery | core | [] |
| generation-handoff | production | [] |
| template-contract | core | [] |
| choreography | production | [] |
| camera-and-rhythm | production | [] |
| world-and-style | visual | [] |
| character-and-performance | narrative | [] |
| powers-and-vfx | production | [] |
| hit-feel | sound | [] |
| prompts-and-segments | production | [] |
| consistency | management | [] |
| ai-pipeline | production | [] |
| dialogue-engine | narrative | [] |
| dialogue-reference-cards | narrative | [dialogue-engine] |
| performance-and-psychology | narrative | [] |
| action-reference-system | production | [] |
| cultural-research | narrative | [] |
| delivery-and-example | production | [] |
| framing-and-compliance | production | [] |
| source-scope | core | [] |
| methods | production | [] |

这些默认空依赖表示可在已载入核心不变量下独立使用，不表示质检取消；按需交叉引用不能全部递归当硬依赖。索引查找先用头部与目录，定位小节再读，不为了查名读整库。

## 连续对话
微调沿用上轮模块集、事实摘要与授权，不重新路由或重新加载。方向改变才重新走图，未变事实继续保留。各模块相关摘要留在内部状态，不强迫用户填卡；片段之间的六项状态仍逐段恢复。
