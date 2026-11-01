---
id: "dialogue-reference-cards"
layer: "narrative"
priority: "P1"
depends_on: ["dialogue-engine"]
conflicts_with: []
load_when: ["台词参考卡库"]
not_for: []
---

# 台词参考卡库

按[台词深度引擎](dialogue-engine.md)启用条件检索，先按场景目的筛选，再按题材与人物DNA改写。下列10张卡均为本技能的**原创示例**，不是影视原句、学术引文或已验证的表演处方。`prompt_fragment`用于编剧/配音设计，不能直接塞进视频正文；复杂停顿与潜台词整体转制作备注。

## 潜台词类：4张

```json
[
  {
    "id": "SUB-01",
    "source": "原创示例：门口的回避",
    "principle": "用可行动的物件回避暴露恐惧",
    "pattern": "对方问心理状态，回答眼前未完成的任务",
    "prompt_fragment": "问：你怕了？答：门还没关。",
    "anti_pattern": "回答与在场物件、目标完全无关",
    "genre_fit": ["武侠", "犯罪", "悬疑"],
    "scene_fit": "出口仍开着，人物确实要守住门，恐惧不宜明说"
  },
  {
    "id": "SUB-02",
    "source": "原创示例：临别整理",
    "principle": "以具体照顾承载未说出口的牵挂",
    "pattern": "情感表达改为对已存在物件的一句叮嘱",
    "prompt_fragment": "扣子扣好，外面风大。",
    "anti_pattern": "场景无风、服装无扣仍机械套用",
    "genre_fit": ["日常", "历史", "武侠"],
    "scene_fit": "熟悉的人即将分别，关系支持克制关心"
  },
  {
    "id": "SUB-03",
    "source": "原创示例：泄露方向",
    "principle": "借不应知道的细节暴露信息差",
    "pattern": "抓住对方未获告知却说出的具体名词",
    "prompt_fragment": "我没说过人在北门。",
    "anti_pattern": "前文已经明确告知北门，却还假装抓到破绽",
    "genre_fit": ["悬疑", "犯罪", "科幻"],
    "scene_fit": "剧情已经建立知情边界，人物察觉对方说漏嘴"
  },
  {
    "id": "SUB-04",
    "source": "原创示例：嘴上放行",
    "principle": "言行错位显露不愿承认的挽留",
    "pattern": "口头允许离开，身体仍守住出口",
    "prompt_fragment": "随你。说话者的手仍压着门闩。",
    "anti_pattern": "没有动机地制造控制行为，或改变双方关系性质",
    "genre_fit": ["日常", "武侠", "悬疑"],
    "scene_fit": "人物本就想留住对方，出口与门闩真实在场"
  }
]
```

## 言语行动类：3张

```json
[
  {
    "id": "ACT-01",
    "source": "原创示例：把注意移向手",
    "principle": "试探对方保护对象，诱使其暴露选择",
    "pattern": "指出一个可见习惯，等待对方纠正或遮掩",
    "prompt_fragment": "你一直护着那只手。",
    "anti_pattern": "画面没有保护动作，却凭台词凭空识破秘密",
    "genre_fit": ["武侠", "犯罪", "热血"],
    "scene_fit": "先前确有护手动作，说话者试探而非全知"
  },
  {
    "id": "ACT-02",
    "source": "原创示例：有条件的让路",
    "principle": "把威吓变成可执行的条件交换",
    "pattern": "一个明确条件，换一个当前能履行的承诺",
    "prompt_fragment": "放下钥匙，我让开这道门。",
    "anti_pattern": "承诺超出人物控制范围，或条件无法被看见兑现",
    "genre_fit": ["犯罪", "科幻", "悬疑"],
    "scene_fit": "钥匙是既定目标，说话者确实控制出口"
  },
  {
    "id": "ACT-03",
    "source": "原创示例：让同伴先动",
    "principle": "安抚通过具体行动指令生效",
    "pattern": "短指令后接本人能承担的动作",
    "prompt_fragment": "看着台阶，我扶你过去。",
    "anti_pattern": "本人双手持械或不在身旁，却声称正在扶人",
    "genre_fit": ["日常", "历史", "热血"],
    "scene_fit": "同伴犹疑，双方距离与空手状态允许搀扶"
  }
]
```

## 类型对白类：3张

```json
[
  {
    "id": "GEN-01",
    "source": "原创示例：武侠的欠账",
    "principle": "用既定旧物承载未清的关系",
    "pattern": "提物不提情，行动补足意义",
    "prompt_fragment": "剑还你，账还没清。",
    "anti_pattern": "凭空增加旧债、借剑经历或复仇关系",
    "genre_fit": ["武侠", "历史"],
    "scene_fit": "归还兵器和未解决的关系都已在剧情中确立"
  },
  {
    "id": "GEN-02",
    "source": "原创示例：科幻的权限",
    "principle": "技术词必须改变当下选择",
    "pattern": "给一项有限权限，同时指出其直接后果",
    "prompt_fragment": "我能开门，关不上第二次。",
    "anti_pattern": "为了台词临时改变设备规则，或长篇解释系统史",
    "genre_fit": ["科幻", "悬疑"],
    "scene_fit": "门控限制已定，人物需要据此决定撤离顺序"
  },
  {
    "id": "GEN-03",
    "source": "原创示例：热血的关键词回响",
    "principle": "相同短句在行动变化后获得新含义",
    "pattern": "前段由被保护者听到，后段由其主动说出",
    "prompt_fragment": "这次，跟着我。",
    "anti_pattern": "没有能力或选择变化，只靠重复制造成长假象",
    "genre_fit": ["热血", "武侠", "日常"],
    "scene_fit": "此前确有带领关系，本场发生可信的责任交接"
  }
]
```

## 检索与落位

用`scene_fit`检查事实，用`genre_fit`缩小风格；一次取最相关的1—3张做备选，不强塞10张。移植的是说话策略，人物、道具和秘密必须来自当前项目。台词文本、潜台词分析和重音进制作备注；可见的手位、视线与动作反应再经负荷检查进入内部G单元。最终纯文本照常去标签、补角色前缀，卡ID不进入正文。
