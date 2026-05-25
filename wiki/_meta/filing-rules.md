---
type: "meta"
status: "active"
created: "2026-05-25"
updated: "2026-05-25"
sources: []
tags: ["wiki-maintenance", "taxonomy", "filing-rules"]
---

# 目标

这份文件记录本 wiki 的本地分类规则。后续使用 `sean-llm-wiki` 时，先读这里，再读 skill 内置 taxonomy；当两者冲突时，以这里更具体的规则为准。

# 总原则

- 不把每个来源、工具、文章或临时想法都单开页面。
- 只有当内容会被独立反复打开、引用、扩展，或已经沉淀为可复用知识时，才创建独立知识文件。
- 如果内容只是“归类、概括、加入某个专栏、先轻量记录、作为子项维护”，优先写入现有聚合页的子项。
- 聚合页负责承载目录、分类规则、轻量条目和后续拆页入口。
- 当一个子项变复杂时，先在聚合页保留摘要，再链接到 `knowledge/` 下新拆出的独立知识文件。

# 目录原则

- 不预创建完整目录树。
- 顶层目录按使用方式组织：`knowledge/`、`notes/`、`_raw/`、`_meta/`，需要导出时再创建 `exports/`。
- `knowledge/` 承载所有可读知识页；在 `knowledge/` 内按需用“领域/内容形态”二级路径组织，不创建空目录。
- 领域优先使用这些目录名：`frontend-backend/` 表示前端、后端、全栈、基础设施和通用工程；`ai/` 表示 AI、Agent、LLM、模型、AI 工具和 AI 工程；未来出现稳定新领域时再按需新增。
- 内容形态在领域目录内使用这些目录名：`summaries/` 表示汇总、专栏、目录和轻量 catalog；`fundamentals/` 表示基础 API、基础语法、基础操作手册和速查；`technology/` 表示可复用技术专题、工程模式、架构、技术栈和实践；`business/` 表示商业化、行业、公司、商业模式和增长相关知识。
- 目录表达主归属；frontmatter `type` 继续表达知识文件语义，例如 topic、pattern、playbook、decision、project、comparison、map、catalog。
- `notes/` 只保留有真实记录的阅读笔记分类文件，不保留空占位文件。
- `_raw/` 只在需要 provenance 时创建来源文件和语义子目录。
- `_meta/` 承载本文件、lint、contradiction、migration 等维护状态。

# 路径分类决策

新建或迁移页面时，先判断“领域”，再判断“内容形态”：

1. 先选领域：AI/Agent/LLM/模型/AI 工具归入 `knowledge/ai/`；前端/后端/全栈/基础设施/通用工程归入 `knowledge/frontend-backend/`。
2. 如果页面主要是目录、清单、专题入口、工具集合、资料聚合或轻量子项容器，放入 `knowledge/<domain>/summaries/`。
3. 如果页面主要是基础 API、基础语法、命令速查、协议基础、框架入门或可按手册查阅的底层知识，放入 `knowledge/<domain>/fundamentals/`。
4. 如果页面主要是技术体系、工程模式、架构判断、实践方法、技术对比、项目落地和长期专题，放入 `knowledge/<domain>/technology/`。
5. 如果页面主要是商业化策略、行业分析、公司/产品商业模式、增长、定价、市场、销售和组织经营，放入 `knowledge/<domain>/business/`。
6. 如果一个页面跨多个领域，选择最主要的长期使用场景作为主路径，在 tags 和交叉链接里标注其他领域，不复制页面。

当前已落地的主分类：

- `knowledge/ai/summaries/ai-tools.md`：AI 下重要 tool 项目的汇总和轻量条目。
- `knowledge/frontend-backend/fundamentals/docker-basic-syntax.md`：前后端/全栈工程基础文档。
- `knowledge/frontend-backend/technology/backend-knowledge-system.md`：前后端技术体系入口。
- `knowledge/ai/technology/agent-skills-basic-concepts.md`：AI 工程基础概念。
- `knowledge/ai/technology/llm-maintained-wiki.md`：AI 工程知识库维护模式。

# 创建独立页面的条件

满足任一条件时，可以创建或更新独立知识文件：

- 它是稳定概念、工程模式、操作手册、架构决策、项目上下文、技术对比或术语定义。
- 它需要多节结构来说明机制、适用场景、风险、案例和来源。
- 它被多个页面引用，或预计会成为后续问答/检索的主要入口。
- 它包含需要长期维护的判断、争议、版本变化或实践经验。
- 用户明确说“展开成页面”“沉淀为专题”“整理成文档”“作为长期知识维护”。

# 作为聚合页子项的条件

满足任一条件时，优先更新聚合页，不创建独立页面：

- 用户说“分类”“概括”“简单介绍”“加到专栏”“作为子项”“先别展开”“轻量记录”。
- 内容是工具、链接、资料、文章、项目、公司、人物、资源集合或短观察。
- 当前只需要一句话定位、分类、适合场景、风险和来源链接。
- 还没有形成独立工程模式、技术对比或实践手册。

# Raw Capture 规则

- 对证据密集、需要复盘、来源不可稳定访问、私有文档、长文档、用户要求保留原始信息的内容，保留 `wiki/_raw/`。
- 对轻量子项，如果只有公开链接、用户给的一句话描述或简单分类，可以不创建 raw 文件，直接在聚合页条目里放来源链接。
- 如果后续把轻量子项扩展成独立页面，再补充 raw capture 或在页面 `sources` 中记录稳定外部来源。

# 当前聚合页规则

## AI 工具

- 聚合页：`knowledge/ai/summaries/ai-tools.md`
- 默认形态：工具作为子项维护，不单开 topic 页。
- 子项字段：`分类`、`定位`、`技术路径`、`适合场景`、`风险`、`来源`。
- 允许的一级分类：
  - `自动化与 Agent 执行`
  - `AI 辅助设计与 UI 生成`
  - `Agent 工程平台`
  - `模型与推理基础设施`
  - `知识库、记忆与检索`
  - `评测、观测与治理`
  - `其他待归类`
- 拆页条件：某个工具需要展开架构分析、替代方案比较、落地 playbook、长期使用记录，或被多个知识页面引用。

## 阅读笔记

- 聚合页目录：`notes/`
- 默认形态：写入一个主分类 markdown 文件，不为每篇文章单开页面。
- 只有当用户要求“沉淀观点”“整理到知识库”“提炼长期知识”时，才在写阅读笔记后更新 durable knowledge file。

# 维护规则

- 新增或调整分类原则时，优先更新本文件。
- 更新聚合页结构时，同步更新 `wiki/index.md` 的描述。
- 重大迁移或拆页/合并应记录在 `wiki/log.md`。
