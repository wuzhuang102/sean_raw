---
type: "topic"
status: "active"
created: "2026-05-28"
updated: "2026-05-28"
sources:
  - "../../_raw/ai-engineering/agent-sandbox-sources.md"
  - "https://openai.com/index/running-codex-safely/"
  - "https://openai.com/index/building-codex-windows-sandbox/"
  - "https://openai.com/index/introducing-codex/"
  - "https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool"
  - "https://www.e2b.dev/docs/use-cases/coding-agents"
  - "https://e2b.dev/docs/use-cases/computer-use"
  - "https://e2b.dev/docs/agents/openai-agents-sdk"
  - "https://www.daytona.io/docs/"
  - "https://modal.com/docs/guide/sandboxes"
  - "https://docs.docker.com/ai/sandboxes/"
  - "https://docs.docker.com/ai/sandboxes/security/"
  - "https://docs.browserbase.com/welcome/introduction"
tags: ["ai", "agent", "sandbox", "execution-environment", "computer-use", "coding-agent"]
---

# 历史背景

Agent sandbox 本质上是给 agent 提供一个受控执行环境，让它不仅能“回答”，还能“动手做事”，但又不直接拿到宿主机的无限权限。

它出现的背景很直接：

- coding agent 需要读写文件、跑命令、装依赖、执行测试；
- browser / computer-use agent 需要点网页、操作桌面、处理登录态和下载文件；
- 一旦直接运行在开发者电脑或生产环境里，风险会立刻变成文件误改、凭证泄露、prompt injection、外网数据外发和环境污染。

这一类能力的演进，大致可以理解为三步：

1. 早期 agent 主要停留在“问答”或“生成代码/文本”，很少真的执行。
2. coding agent、browser agent、computer-use agent 开始要求真实操作文件、命令、网页和桌面。
3. 平台方不得不补一层受控执行环境，否则用户只能在“频繁人工批准”和“直接 full access”之间做选择。

OpenAI 在 2026-05-13 发布的 Windows sandbox 设计文章里，明确把这个矛盾说成：没有可用 sandbox 时，开发者通常只能二选一，要么几乎每条命令都人工批准，要么直接给 agent full access。前者太打断，后者太危险。[OpenAI Windows sandbox](https://openai.com/index/building-codex-windows-sandbox/)

# 定义

在这份 wiki 里，`agent sandbox` 指的是一类给 agent 使用的受控执行边界。它允许 agent 在限定范围内执行真实操作，例如：

- 读写文件
- 执行 shell 命令
- 安装依赖
- 操作浏览器
- 操作桌面应用

同时限制它直接影响宿主机、生产环境、敏感目录、外部网络和凭证的能力。

它不是单纯的容器同义词，更强调“agent 可执行，但边界受控”。常见控制面一般包括：

- 文件权限范围
- 网络访问范围
- 凭证暴露方式
- 审批与日志
- 环境生命周期
- 可观测与回放

# 使用场景

## Coding agent

最常见场景是代码生成、重构、修 bug、补测试、跑 lint、跑 build、做 PR review。  
这类场景通常需要 agent 真正进入代码仓库上下文，执行命令并验证结果。

## Browser agent

当任务核心是网页交互时，agent 需要在真实浏览器环境里完成导航、点击、输入、抓取、登录后操作和文件下载上传。

## Computer-use agent

这类 agent 不只操作网页，而是直接操作桌面界面，例如文件管理器、IDE、聊天软件、办公软件或其他本地应用。

## 多任务并发执行

一个 agent 一个 sandbox，也是天然的任务隔离方式。  
不同 issue、不同 PR、不同用户任务可以拆到不同执行环境，避免状态互相污染。

## 不可信代码或命令执行

如果任务里包含模型自动生成的命令、第三方脚本、临时依赖或用户提供代码，sandbox 也是默认前提，用来降低直接在宿主机执行的风险。

# 关联页面

- [LLM-maintained wiki](LLM维护Wiki.md)

# Sources

- [Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely/)
- [Building a safe, effective sandbox to enable Codex on Windows](https://openai.com/index/building-codex-windows-sandbox/)
- [Introducing Codex](https://openai.com/index/introducing-codex/)
- [Anthropic computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)
- [E2B Coding Agents](https://www.e2b.dev/docs/use-cases/coding-agents)
- [E2B Computer Use](https://e2b.dev/docs/use-cases/computer-use)
- [E2B OpenAI Agents SDK integration](https://e2b.dev/docs/agents/openai-agents-sdk)
- [Daytona Documentation](https://www.daytona.io/docs/)
- [Modal Sandboxes](https://modal.com/docs/guide/sandboxes)
- [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/)
- [Docker Sandboxes Security Model](https://docs.docker.com/ai/sandboxes/security/)
- [Browserbase Introduction](https://docs.browserbase.com/welcome/introduction)
