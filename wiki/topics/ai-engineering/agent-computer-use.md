---
type: "topic"
status: "active"
created: "2026-05-25"
updated: "2026-05-25"
sources:
  - "../../_raw/ai-tools/agent-computer-use-sources.md"
tags: ["ai-tools", "computer-use", "desktop-automation", "agent-skills", "accessibility"]
---

# 核心定位

用户提到的 “compute-use” 在公开搜索中没有对应到一个稳定主项目；这里记录的是最匹配、可验证的 `agent-computer-use`，它的命令和 npm 包名是 `agent-cu`。

agent-computer-use 是给 AI Agent 使用的本地桌面控制 CLI。它让 Agent 通过终端读取桌面 App 的可访问性树，拿到按钮、输入框、菜单项等元素引用，再执行点击、输入、按键、滚动、窗口管理、截图、等待和验证等动作。

它不是完整自主 Agent，更像一个 deterministic computer-use primitive：LLM 决定“点哪个 ref、输入什么”，`agent-cu` 负责本地执行。

# 工作流

基本循环是：

1. Snapshot：对目标 App 采集可交互元素，输出 `@e1`、`@e2` 等 refs。
2. Decide：Agent 根据任务和 snapshot 选择目标元素或 selector。
3. Act：通过 `agent-cu click`、`agent-cu type`、`agent-cu key` 等命令执行动作。
4. Verify：重新 snapshot、读取文本或等待目标元素出现，确认 UI 状态。

这个循环把“看屏幕”替换成“读结构化可访问性树”。相比视觉 computer use，它减少了截图推理和视觉 token；相比坐标点击，它能读到元素角色、名称、状态和值。

# 技术要点

## Accessibility-first

agent-computer-use 的核心依赖是系统可访问性接口：

- macOS：AXUIElement / CGEvent
- Linux：AT-SPI2
- Windows：UIAutomation

这条路线的关键优点是结构化、可读状态、低 token 成本和本地执行。关键限制是目标 App 必须暴露足够好的 accessibility 信息，否则仍需要退回坐标、截图或应用专属 API。

## Selector 与 refs

工具支持两类定位方式：

- refs：来自最近一次 snapshot 的 `@e5` 这类元素编号，速度快但需要在 UI 变化后重新采样。
- Selector DSL：按 role、name、id、包含匹配、层级链等方式定位元素，更适合可复用脚本。

这使它介于 pyautogui 和传统 RPA 之间：比纯坐标自动化可解释，比完整 RPA 平台轻量。

## Electron / CDP 支持

对 Slack、Cursor、VS Code、Postman、Discord、Notion 等 Electron App，agent-computer-use 可以自动通过 CDP 接入，把 DOM 访问和原生外壳结合起来。这对现代桌面软件很实用，因为很多“桌面 App”本质是 Electron Web 应用。

## Agent Skill 集成

GitHub README 说明它通过 skills.sh 分发为 Agent skill，可供 Claude Code、Cursor、Codex、Copilot、OpenCode、Cline 等使用。输出默认是 JSON，也符合 Agent 调用和解析的需求。

# 适用场景

适合优先评估 agent-computer-use 的场景：

- 本地桌面 App 自动化，例如 Finder、Calculator、Music、Slack、Cursor、VS Code、Notion 等。
- 需要低成本、无视觉 token、可解释的 computer use 操作。
- 希望让 Coding Agent 或本地 Agent 临时操作 GUI，但不想给它完整视觉模型循环。
- 目标 App accessibility 做得较好，元素 role/name/value 可读。
- 需要把桌面操作写成 YAML 工作流、batch 命令或 Agent skill。

不适合直接使用的场景：

- 目标界面 accessibility 暴露很差，元素没有稳定名称或状态。
- 需要理解复杂视觉布局、图像内容、canvas 或游戏界面。
- 操作风险很高但缺少确认、审计、撤销和权限隔离。
- 需要成熟企业 RPA 的队列、凭证、审批、审计、监控和异常处理平台能力。

# 风险与观察点

## 权限

桌面控制需要系统 accessibility 权限，这通常是很高的本机权限。安装到 Agent skill 后，必须控制哪些 Agent、项目和命令可以调用它，避免“自然语言误触发桌面操作”。

## 预览状态

GitHub README 把 macOS、Windows、Linux 和 Electron 支持都标为 Preview。评估时应把它看作快速发展的工具，而不是稳定 RPA 平台。

## 可访问性质量

Accessibility-first 的上限取决于 App 暴露的信息质量。原生控件通常较好，自定义 canvas、复杂 WebView、未命名按钮和虚拟列表可能会降低可用性。

## 与视觉 computer use 的边界

它不依赖截图推理，因此便宜、快、可结构化；但遇到必须看图、读非结构化视觉内容或判断空间关系的任务时，仍可能需要视觉模型补位。

# 对 AI 工具的启发

agent-computer-use 体现了一个务实方向：先把操作系统已经有的结构化 UI 信息暴露给 Agent，而不是默认让模型看截图。对很多办公自动化任务，accessibility tree 加 selector 已经足够完成 80% 的控制需求；视觉模型应该作为补充，而不是每一步的默认执行路径。

它也提醒 AI 工具设计者：真正有价值的 computer use 不只是“模型会点鼠标”，而是给 Agent 一个低成本、可验证、权限可控、输出结构化的动作层。

# Sources

- Docs: [agent-computer-use](https://www.agent-computer-use.dev/)
- GitHub: [kortix-ai/agent-computer-use](https://github.com/kortix-ai/agent-computer-use)
- Internal capture: `wiki/_raw/ai-tools/agent-computer-use-sources.md`
