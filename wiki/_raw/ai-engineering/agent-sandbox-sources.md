---
source_type: "research-notes"
captured: "2026-05-28"
scope: "Agent sandbox background, scenarios, and tool landscape"
---

## User Request

调研沉淀 agent sandbox 的背景、使用场景以及相关工具，后续实践再追加。

## Working Definition

Agent sandbox 是给 agent 提供受控执行环境的一类基础设施。它的核心不是“完全禁止执行”，而是把执行限制在一个可审计、可配置、可回收的边界里，让 agent 能跑命令、读写文件、操作浏览器或桌面，同时降低对宿主机、生产环境和敏感数据的直接风险。

## Sources Fetched On 2026-05-28

- OpenAI, Running Codex safely at OpenAI
  - https://openai.com/index/running-codex-safely/
  - 要点：approval policy 和 sandbox boundary 是两层控制；sandbox 定义文件、网络、路径的技术边界。

- OpenAI, Building a safe, effective sandbox to enable Codex on Windows
  - https://openai.com/index/building-codex-windows-sandbox/
  - 要点：没有 sandbox 时，用户通常只能在“频繁人工批准”和“full access”之间做糟糕选择；文章系统性解释了 OS-level sandbox 的需求。

- OpenAI, Introducing Codex
  - https://openai.com/index/introducing-codex/
  - 要点：云端 coding task 每个任务运行在独立 cloud sandbox environment；初始默认网络禁用。

- Anthropic, Computer use tool
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
  - 要点：computer use 需要 virtual display、desktop environment、applications、tool implementation 和 agent loop；参考实现跑在 container 里。

- E2B, Coding Agents
  - https://www.e2b.dev/docs/use-cases/coding-agents
  - 要点：把 coding agent 放进隔离 Linux 环境，提供 terminal、filesystem、git 和模板。

- E2B, Computer Use
  - https://e2b.dev/docs/use-cases/computer-use
  - 要点：提供带 VNC 的 desktop sandbox，支撑 computer-use agent。

- E2B, OpenAI Agents SDK
  - https://e2b.dev/docs/agents/openai-agents-sdk
  - 要点：提供 OpenAI Agents SDK 的 sandbox backend，把 SandboxAgent 跑进 E2B session。

- Daytona Documentation
  - https://www.daytona.io/docs/
  - 要点：把 sandbox 定义为 composable computers，强调 snapshots、filesystem、process、runtime config，以及面向 AI-generated code 的 secure infrastructure。

- Modal, Sandboxes
  - https://modal.com/docs/guide/sandboxes
  - 要点：把 sandbox 定义为 secure containers for executing untrusted user or agent code，并提供 readiness probe、tunnel、filesystem 等能力。

- Docker Docs, Docker Sandboxes
  - https://docs.docker.com/ai/sandboxes/
  - https://docs.docker.com/ai/sandboxes/security/
  - 要点：本地 microVM sandbox；每个 sandbox 拥有独立 Docker daemon、filesystem、network；通过代理和 allowlist 管控 credential 与网络访问。

- Browserbase, Introduction
  - https://docs.browserbase.com/welcome/introduction
  - 要点：更偏 browser agent runtime，提供 cloud browsers、search、fetch 和 sandbox runtime，而不是通用 coding sandbox。

## Synthesis Notes

- Agent sandbox 已经从“安全附属品”变成 agent 产品的核心 runtime。
- 主要场景可以分成三类：coding、browser、computer use；三者对环境形态要求不同。
- 选型时最重要的不是品牌，而是边界模型：文件、网络、凭证、状态持久化、可观测性、人工接管能力。
- Browserbase 这类工具更像浏览器执行层；E2B、Daytona、Modal、Docker Sandboxes 更接近通用执行环境。
- OpenAI 和 Anthropic 的文档更适合作为 sandbox 设计参照，而不只是产品介绍。
