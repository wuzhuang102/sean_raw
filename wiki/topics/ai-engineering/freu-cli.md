---
type: "topic"
status: "active"
created: "2026-05-25"
updated: "2026-05-25"
sources:
  - "../../_raw/ai-tools/freu-cli-sources.md"
tags: ["ai-tools", "browser-automation", "desktop-automation", "agent-skills", "rpa"]
---

# 核心定位

Freu 当前对外有两个相关层次：

- Freu AI：Product Hunt 页面展示的是面向 Mac 的桌面 AI 自动化产品，目标是用自然语言自动化任意桌面 App。
- Freu CLI：GitHub 开源的是 Browser Edition，定位为浏览器自动化引擎，把录制过的 Web 工作流编译为可复用的 Skill 命令。

它的核心思路不是让 Agent 每次执行任务时都重新“看屏幕/读 DOM/推理下一步”，而是把重复 UI 工作流提前编译成确定性 DSL。LLM 或视觉模型主要承担学习和编译阶段的理解成本，后续执行尽量变成低成本、本地化、可复用的命令运行。

# 工作流

Freu CLI 的浏览器自动化流程可以拆成三段：

1. Learn：人类正常操作浏览器，`freu-cli learn` 捕获点击、输入、导航和 DOM 上下文，并用 LLM 把原始事件归纳成语义动作。
2. Build：Freu 将动作解析为 DSL 命令，生成 `SKILL.md` 和一个或多个 JSON 命令文件；对于数据获取类目标，还会识别结果元素并声明输出。
3. Run：Agent 通过 `freu-cli run` 执行已经编译好的命令，避免每次都把页面结构或截图放进模型上下文重新推理。

Product Hunt 上的 Freu AI 桌面版本沿用同一类思路：用户示范一次跨 App 工作流，系统通过视觉理解生成可复用 DSL，之后在本地执行。

# 技术要点

## AOT 编译

Freu 把自身解释为 UI 自动化的 Ahead-of-Time 编译器。传统 Agent 更像 Just-in-Time 解释器：每次执行都观察当前页面或屏幕，再让模型决定下一步。AOT 的价值在于把高频任务的智能成本前移，让重复运行更便宜、更快，也更容易被审计。

## Semantic UI / DOM constellation

Freu CLI 不只记录固定 CSS selector 或坐标，而是记录目标元素、祖先、邻近元素、子元素和语义锚点组成的上下文。README 把这种定位称为 constellation。运行时再在当前页面中寻找最匹配的元素，以提高对 class 重命名、布局轻微变化和运行时 hash 的抗干扰能力。

桌面版 Product Hunt 介绍中使用的是 Semantic UI 说法：动作锚定在按钮、文本框、图标等 UI 语义上，而不是固定 X/Y 坐标。

## Agent Skill 输出

Freu CLI 的输出天然接近 Agent skill：一个说明文件加上结构化命令文件。GitHub README 列出的目标集成目录包括 Claude Code、Codex CLI、Cursor、OpenClaw 和 Hermes。这说明它不只是一个单独自动化 CLI，也是在尝试成为 Agent 的可复用“肌肉记忆”生成器。

# 适用场景

适合优先评估 Freu 的场景：

- 重复执行的浏览器后台、运营、数据录入、信息检索和跨系统搬运任务。
- 操作路径相对稳定，但页面 DOM、样式类名或布局会发生轻微变化的业务系统。
- 希望减少 Agent 长上下文、截图推理和反复网页导航 token 消耗的团队。
- 已经在使用 Claude Code、Codex CLI、Cursor 等本地 Agent skill 机制，希望把浏览器动作沉淀成工具命令的个人或团队。

不适合直接期待它解决的场景：

- 每次任务目标和页面路径都高度开放，需要持续重新规划。
- 页面或桌面 App 经常发生完整重构，原工作流本身不稳定。
- 强权限、高风险操作缺少人工确认、审计和回滚机制。
- 需要完全离线且当前异常恢复也不能触发云端模型的敏感环境。

# 风险与观察点

## 稳定性

Constellation 和 Semantic UI 能缓解脆弱 selector 与坐标问题，但不能消除工作流级变化。如果目标 App 改了业务流程、权限弹窗、页面结构或关键文案，仍可能需要重新学习或加入异常恢复策略。

## 异常处理

Product Hunt 评论中，maker 对突发弹窗的回答是当前会安全暂停；自动恢复可能临时调用云模型理解异常画面。也就是说，零 token 执行更适用于正常路径，异常路径目前仍可能回到模型推理。

## 隐私与权限

桌面自动化天然需要较高本地权限，浏览器自动化也会接触业务系统页面和操作状态。评估时需要明确捕获日志保存在哪里、是否上传、是否包含敏感 DOM/截图、生成的 Skill 是否会泄露业务字段。

## 开源许可

GitHub 仓库显示 Freu CLI 使用 AGPL-3.0。商业产品或内部平台集成时，需要单独评估 AGPL 对网络服务、分发和衍生修改的合规影响。

# 对 AI 工具的启发

Freu CLI 代表一种重要 AI 工具设计模式：把 LLM 从高频执行路径里拿出来，只在学习、编译、修复或异常恢复时使用。这个模式适合所有“任务重复、界面复杂、推理昂贵、动作可结构化”的场景。

对工程团队而言，值得关注的不是“AI 能不能替人点击”，而是能否把一次性智能转化为可版本化、可审计、可复用、可失败恢复的确定性资产。Freu 的 Skill/DSL 方向与 Agent skill、MCP tool、内部自动化脚本之间有明显交集。

# Sources

- Product Hunt: [Freu AI](https://www.producthunt.com/products/freu-cli)
- Official site: [Freu](https://www.freu.ai/)
- GitHub: [freu-ai/freu-cli](https://github.com/freu-ai/freu-cli)
- Internal capture: `wiki/_raw/ai-tools/freu-cli-sources.md`
