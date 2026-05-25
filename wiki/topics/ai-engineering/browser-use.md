---
type: "topic"
status: "active"
created: "2026-05-25"
updated: "2026-05-25"
sources:
  - "../../_raw/ai-tools/browser-use-sources.md"
tags: ["ai-tools", "browser-automation", "ai-agents", "playwright", "cloud-browser"]
---

# 核心定位

Browser Use 是面向 AI Agent 的浏览器自动化框架。它把网页暴露给模型，让模型能观察浏览器状态、决定下一步动作，并通过浏览器自动化执行点击、输入、导航、提取内容等任务。

它有两个层次：

- Open-source agent：Python 框架，适合自托管、深度代码集成、自定义工具和本地实验。
- Browser Use Cloud：托管浏览器与托管 Agent 服务，强调 stealth browser、代理、CAPTCHA 处理、并发扩展、持久文件系统和集成能力。

# 工作流

典型开发路径是：

1. 创建 `Browser`，可以使用本地浏览器，也可以使用 Browser Use Cloud 的远程浏览器。
2. 创建 `Agent`，指定自然语言任务、LLM 和浏览器实例。
3. Agent 循环读取当前浏览器状态，规划下一步，执行动作，并根据页面变化继续迭代。

Cloud SDK 进一步区分 Agent 和 Browser：Agent 负责“给任务并让 AI 跑完”，Browser 负责“创建原始浏览器并通过 CDP 控制”。这个拆分很重要，因为生产系统有时只需要托管浏览器基础设施，不一定需要完整自主 Agent。

# 技术要点

## 动态浏览器 Agent

Browser Use 属于动态执行路径：模型在每一步仍然参与观察、决策和纠错。它适合任务目标开放、页面路径不固定、需要临场判断的 Web 操作，但成本和稳定性会受模型质量、页面复杂度、上下文长度和反爬机制影响。

这与 [Freu CLI / Freu AI](freu-cli.md) 的 AOT 编译思路形成对比：Freu 更强调把重复工作流提前编译成命令，Browser Use 更强调让 Agent 在运行时理解网页并完成任务。

## Playwright 与浏览器状态

GitHub 仓库主题标注了 Playwright，CLI 也提供 open、state、click、type、screenshot、close 等持久浏览器操作。对 Agent 来说，关键价值不是“能点击网页”，而是能把网页当前可操作状态组织成模型可消费的行动空间。

## Cloud 生产化能力

Browser Use Cloud 的卖点集中在浏览器基础设施：可扩展并发、内存管理、代理轮换、stealth fingerprint、CAPTCHA 处理、持久文件系统、记忆和大量集成。对于线上自动化，浏览器运行环境、登录态、反爬、资源消耗往往比单次动作 API 更难。

## Skill 与 Agent 集成

Browser Use 提供 Claude Code Skill，并有 CLI 形态。这说明它的使用方式不只是 Python SDK，也可以成为本地 Agent 的浏览器能力插件。

# 适用场景

适合优先评估 Browser Use 的场景：

- 需要处理开放式网页任务，例如表单填写、购物、订票、资料查找、网页研究和多步骤操作。
- 任务路径不完全固定，需要模型根据页面状态动态决策。
- 需要把浏览器操作嵌入 Python 应用或 Agent 框架。
- 生产上需要托管浏览器、代理、CAPTCHA、登录态和并发执行能力。
- 需要让 Coding Agent 临时打开网页、检查状态、点击元素或截图。

不适合直接使用的场景：

- 目标网站有稳定 API，可以直接通过 API 或后端集成完成。
- 任务完全固定且高频重复，确定性脚本、AOT 编译命令或内部 API 更便宜。
- 强登录态、高权限账号缺少隔离和审计。
- 页面中存在未隔离的用户内容，容易触发 prompt injection 或越权操作。

# 风险与观察点

## 成本与延迟

动态浏览器 Agent 每一步都可能消耗模型推理。复杂页面、长任务和频繁纠错会放大 token 成本和延迟。生产场景应尽量把确定子任务下沉为代码工具，而不是让模型反复“看页面、想下一步”。

## 可靠性

Browser Use 可以缓解传统 selector 自动化的脆弱性，但不能保证复杂业务流程稳定完成。真实系统应记录执行轨迹、截图、失败原因、重试策略和人工接管点。

## 安全

浏览器 Agent 常常运行在已登录环境中，拥有用户级权限。风险包括 prompt injection、跨站数据泄露、误提交、误购买、下载/上传敏感文件，以及代理或远程浏览器环境中的数据治理问题。

## 反爬与合规

Cloud 侧提供 stealth、代理和 CAPTCHA 能力，但这也意味着评估时必须明确目标网站条款、自动化边界和账号封禁风险。工程可行不等于业务合规。

# 对 AI 工具的启发

Browser Use 代表“运行时智能浏览器 Agent”路线：优点是通用、灵活、上手快；代价是成本、延迟和可靠性都与模型循环绑定。它适合作为探索和开放任务的执行层，但成熟流程最终往往需要把高频部分沉淀为 API、脚本、Skill 或工作流。

# Sources

- GitHub: [browser-use/browser-use](https://github.com/browser-use/browser-use)
- Docs: [Browser Use documentation](https://docs.browser-use.com/)
- Website: [Browser Use](https://browser-use.com/)
- Internal capture: `wiki/_raw/ai-tools/browser-use-sources.md`
