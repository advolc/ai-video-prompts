# 从v1迁移

v1有104个文件、约215K中文字符。v2有14份Markdown文件和一个静态检查脚本，约130K英文字符（合计约32K token）。典型任务加载 `SKILL.md` 和两三份参考，约10—17K token，而不是从大得多的文件树中取六个模块。采用v2前请先归档v1（例如打上 `v1-archive` 标签）；本版不要求删除旧版。

## 保留了什么（深度系统）

| 系统 | v1来源 | v2位置 | 变化 |
|---|---|---|---|
| 台词引擎：四层、三轴、现场取材、六种手法、场景公式、6＋4种质感引擎、语言DNA、负向约束、音频分流 | `dialogue-engine.md` | `dialogue-engine.md` | 翻译并压缩；保留权力宣示的窄例外；题材种子库缩为五类 |
| 14张台词卡 | `dialogue-reference-cards.md` | `dialogue-cards.md` | JSON改为表格；14张全部保留 |
| 心理动作、微相矩阵、可见化转换、降级预案、反套话、生理泄露、题材矩阵、视距转译、三轴 | `performance-and-psychology.md` | `performance-psychology.md` | 全部保留；保留“不能静默降级明确的脸部目标” |
| 生活微动作与道具 | `narrative/life-actions.md`、`prop-storytelling.md` | `performance-psychology.md` §11 | 合并 |
| 动作编排：选择、兵器逻辑、发力链、距离、连招母题、动作单元、群战 | `choreography.md` | `action-causality.md` | 保留 |
| 打击因果链与受击上下文推演 | `hit-feel.md` | `action-causality.md` §5、`camera-and-sound.md` §7 | 合并 |
| 动作参考卡 | `action-reference-system.md` | `action-causality.md` §11 | 压缩为术语到措辞的转换表 |
| 状态接缝台账、六项传递 | `choreography.md`、`consistency.md` | `action-causality.md` §10、`character-scene-continuity.md` | 保留；接缝仅定义一次 |
| 人物建构、服装、无参考图锚点 | `character-and-performance.md`、`generation-handoff.md` | `character-scene-continuity.md` | 保留 |
| 环境与天气、可交互物分级 | `visual/environment-interaction.md` | `character-scene-continuity.md` §8 | 保留 |
| 运镜、节奏、镜头表、声音分层、主观心理声学 | `camera-and-rhythm.md`、`sound/sound-design.md` | `camera-and-sound.md` | 合并 |
| 纯文本交付、四条红线、剧本转提示词、负荷检查 | `generation-handoff.md`、`anti-lazy-and-delivery.md` | `delivery.md` | 合并并去重 |

## 移除了什么，以及原因

- **加载图、任务路由器、模块契约、precedence-rules、五处“最高权限”声明。** 改为 `SKILL.md` 中的一套优先级和一张路由表。其他文件若宣称优先权，`check_skill.py` 现在会报错。
- **推荐/忽略/拒绝状态机和“质感探针”。** 深度系统改为按内容启用（有对白的场景加载台词引擎），用户可说“quick”。不再记授权流水账。
- **带有三条例外的“3+2”硬法。** 改为约5秒片段的明确指导值，须实测校准，以“每段一个主要交互”为主导。
- **发行、发布、封面/标题、A/B、协作、管理，以及大部分质检与后期。** 这些是通用制作管理检查表，有能力的模型本已掌握。
- **工程G表输出与导出脚本。** 最终只交纯文本；制作备注放复制区外。需要工程表时保留v1处理。
- **灵感向导与灵感库。** 不属于核心价值；需要头脑风暴时保留v1。
- **平台矩阵。** 用一套方法（`models/`）替代：能力检查表、各项答案如何改变提示词的对照表，以及只能依据已核来源或自己的试片填写的适配器模板。

## 未迁移、需要你核对的内容

我没有阅读，也没有迁移：灯光、构图、画面框定/合规、世界与画风、文化考据、音色设计、音频后期、AI管线与生成段文件，以及模板。若其中有你依赖的知识，把相关段落从v1移入最接近的v2参考文件，而不是恢复整份文件。台词引擎中更完整的题材种子库也按此处理。

## 诚实说明

- v2经过人工翻译和压缩。中文原稿的一些细微含义可能丢失；对最重视的文件逐节比较。
- 两个版本都没有做过基准测试。v2增加 `evals/cases.md`，供你验证。
- 当前默认面向英语使用，也支持中文输出；题材示例主要是武侠和仙侠，因为原始示例如此。按实际工作补充自己的题材。
