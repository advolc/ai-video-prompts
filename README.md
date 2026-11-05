# ai-video-prompts（v2）

用于设计AI视频提示词的技能。它让模型呈现**可见、符合物理关系、有因果**的场景：打斗先接触再出结果，对白意图通过身体显现，表演用一个可读信号胜过堆满表情，多片段场景逐段传递状态。

## 目录结构

```
SKILL.md                              工作流程、7条规则、唯一优先级顺序、路由表
references/
  action-causality.md                 接触、支撑、结果、兵器逻辑、状态接缝台账
  dialogue-engine.md                  四层模型、潜台词三轴、质感引擎、音频分流
  dialogue-cards.md                   14张可适配的言语策略卡
  performance-psychology.md           心理动作、微相、泄露公式、降级规则
  character-scene-continuity.md       人物与服装建构、环境、一致性、返工
  camera-and-sound.md                 镜头选择、节奏、镜头表、声音分层
  delivery.md                         信息收集、负荷检查、纯文本组装、自检
models/                               能力检查表＋空白逐模型适配器（根据测试填写）
examples/worked-example.md            运用三套深度系统的双片段场景（示意）
evals/cases.md                        8个测试案例和用于衡量效果的评分标准
scripts/check_skill.py                静态检查：体量预算、链接、路由、优先权冲突
MIGRATION.md                          v1以来的改动与各系统去向
```

## 使用方法

加载 `SKILL.md` 和任务所需的参考文件（通常两三份）。说“quick”即可走精简流程：保留七条规则，不展开深度分析。编辑后运行 `python scripts/check_skill.py .`。

## 当前状态

仅为设计原则。尚未做基准测试。信赖某条规则前，先在你的模型上运行 `evals/cases.md`。
