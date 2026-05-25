This wiki is maintained by the `sean-llm-wiki` skill. It is a working engineering knowledge base: readable by humans, maintained by LLMs, and grounded in raw source files when raw capture is needed.

# AI

## 汇总

- [AI 工具专栏](knowledge/ai/summaries/ai-tools.md) - AI 下重要 tool 项目的轻量分类、工具条目、评价框架和后续拆页入口。

## 技术

- [Agent Skill 基础概念](knowledge/ai/technology/agent-skills-basic-concepts.md) - Agent skill 的组成、触发方式、适用边界和具体 skill 分类记录。
- [LLM-maintained wiki](knowledge/ai/technology/llm-maintained-wiki.md) - 用 LLM 增量维护持久 Markdown 知识库的架构、操作循环和实践边界。

# 前后端 / 全栈

## 基础文档

- [Docker 常用基础语法](knowledge/frontend-backend/fundamentals/docker-basic-syntax.md) - Docker 镜像、容器、Dockerfile、volume、网络、Compose 和清理命令的基础用法速查。

## 技术

- [后端知识体系](knowledge/frontend-backend/technology/backend-knowledge-system.md) - 后端技术栈能力地图，覆盖 API、数据库、事务、缓存、队列、安全、可观测性、部署、分布式和学习路径。

# 商业化

当前还没有商业化知识文件。后续商业模式、行业分析、定价、增长、公司和产品商业化资料，优先按领域落到 `knowledge/<domain>/business/`。

# Notes

- [Technology](notes/technology.md) - engineering, AI, architecture, tools, technical papers, and implementation writeups.
- [Work](notes/work.md) - management, collaboration, retrospectives, organizational process, and career material.

# Maintenance

- [Filing Rules](_meta/filing-rules.md) - 本 wiki 的本地分类规则，控制什么时候创建独立知识文件、什么时候写入聚合页子项。

# Directory Model

- `knowledge/ai/`: AI、Agent、LLM、模型、AI 工具和 AI 工程。
- `knowledge/frontend-backend/`: 前端、后端、全栈、基础设施和通用工程。
- `<domain>/summaries/`: 汇总、专栏、目录和轻量 catalog。
- `<domain>/fundamentals/`: 基础 API、基础语法、基础操作手册和速查。
- `<domain>/technology/`: 技术体系、工程模式、架构和长期专题。
- `<domain>/business/`: 商业化、行业、公司、商业模式和增长相关知识；按需创建。
- `notes/`: 轻量阅读记录；只创建实际有记录的分类文件。
- `_raw/`: 内部原始来源；只在需要保留 provenance 时创建。
- `_meta/`: 维护规则、分类规则、lint 和迁移记录。
