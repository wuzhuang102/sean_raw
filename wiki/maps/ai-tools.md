---
type: "map"
status: "active"
created: "2026-05-25"
updated: "2026-05-25"
sources:
  - "../_raw/ai-tools/freu-cli-sources.md"
  - "../_raw/ai-tools/browser-use-sources.md"
  - "../_raw/ai-tools/agent-computer-use-sources.md"
tags: ["ai-tools", "tool-evaluation", "automation"]
---

# 专栏定位

AI 工具专栏用于持续整理 AI 工具的全方位知识：产品定位、核心能力、技术架构、适用场景、集成方式、商业与开源模式、使用风险、可替代方案，以及对工程实践的启发。

每个工具条目优先回答七个问题：

- 它解决什么重复、高成本或高不确定性的问题？
- 它把 AI 放在工作流的哪个环节：理解、规划、执行、验证，还是记忆？
- 它依赖哪些关键技术路径：LLM、视觉模型、浏览器/桌面自动化、RAG、Agent skill、MCP、本地模型等？
- 它如何接入现有工作流：CLI、IDE、浏览器扩展、桌面 App、API、插件或企业系统？
- 它的成本结构是什么：一次性推理、持续推理、本地执行、订阅、开源自托管？
- 它的主要风险是什么：稳定性、安全权限、隐私、幻觉、维护成本、平台限制？
- 它和相邻工具相比的差异化在哪里？

# 工具索引

## 自动化与 Agent 执行

- [Browser Use](../topics/ai-engineering/browser-use.md) - 动态浏览器 Agent 框架，支持本地 Python SDK、CLI、Cloud 托管浏览器和 Agent 运行。
- [Freu CLI / Freu AI](../topics/ai-engineering/freu-cli.md) - 通过一次录制/学习把浏览器或桌面工作流编译为可复用 DSL 命令，目标是降低重复 UI 自动化的 token 成本和执行延迟。
- [agent-computer-use / agent-cu](../topics/ai-engineering/agent-computer-use.md) - 通过 accessibility tree 和 CDP 给 Agent 提供本地桌面 App 控制能力，强调结构化、确定性和低 token 成本。

# 评价框架

## 产品层

看工具的目标用户、核心场景、输入输出、学习成本和默认工作流。AI 工具容易把演示做得很强，但真正价值通常来自重复任务、强上下文任务或跨系统任务的稳定落地。

## 技术层

关注它将不确定推理和确定执行如何分层。可复用工具通常会把 LLM 放在理解、编排或生成阶段，把高频执行沉淀为脚本、DSL、索引、缓存、规则或本地模型。

## 集成层

判断它是否能进入用户已有工作台，而不是要求用户迁移到新的孤岛。CLI、浏览器扩展、IDE 插件、Agent skill、MCP server、API 和企业权限模型，都会决定工具能否被日常使用。

## 风险层

AI 工具的风险不只来自模型错误，也来自权限过大、自动执行不可追踪、外部 UI 变化、供应商锁定、数据外发、成本不可控和缺少回滚机制。记录工具时要把风险作为一等信息。

# 关联主题

- [Agent Skill 基础概念](../topics/ai-engineering/agent-skills-basic-concepts.md)
