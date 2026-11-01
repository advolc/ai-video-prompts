---
id: "module-contract"
layer: "core"
priority: "P0"
depends_on: []
conflicts_with: []
load_when: ["模块契约"]
not_for: []
---

# 模块契约


每个规则模块使用七个 YAML 字段：`id / layer / priority / depends_on / conflicts_with / load_when / not_for`。id 在全库唯一，依赖和冲突以 id 引用，不使用显示标题。layer 为所在分层目录；旧 references 按职责赋层，不移动旧路径。priority 只管加载先后，不能推翻主技能既有 P0/P1/P2 质检。

```yaml
id: color-system
layer: visual
priority: P0
depends_on: []
conflicts_with: []
load_when: ["用户指定配色或需要色彩叙事"]
not_for: ["只检查兵器接触"]
```

depends_on 仅列完成本模块不可缺的规则，交叉链接不是强依赖。已有用户授权限制必须传递；批准一个模块不批准它链接的其他高级模块。命中 not_for 跳过；若显式依赖反而不可用，先缩小任务、提供候选或分阶段，不能悬空执行依赖模块。发现依赖环停止该分支并修配置，不无限递归。

控制层能力未核实不能填肯定值；生成层只写可见/可原生生成信息；分析、评分、软件操作进入管理层。所有新模块均服从[模板契约](../references/template-contract.md)和[默认交付协议](../references/anti-lazy-and-delivery.md)。模板与风格卡用于诊断补缺，不用于替换用户的表达。

## 无依赖解析器的头部写法

为保证标准库检查器可直接运行，本仓库采用YAML的平坦子集：字符串标量、单行字符串数组；数组推荐JSON兼容写法，如`["dialogue-engine"]`，空值用`[]`。不使用嵌套映射、多行块或YAML锚点。主SKILL的name/description使用宿主技能元数据规范，不加模块七字段替换它。
