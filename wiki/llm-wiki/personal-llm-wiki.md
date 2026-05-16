# Personal LLM Wiki

> Sources: Andrej Karpathy, 2026-04-04; Juan M. Huerta, 2026-05; xoai, 2026-05; NiharShrotri, 2026-05; Proudfrog, 2026-04; acmerfight, 2026-05
> Raw: [Personal LLM Wiki Research](../../raw/llm-wiki/2026-05-16-personal-llm-wiki-research.md)

## Overview

个人 LLM wiki 是一种让 LLM 持续维护个人知识库的工作流：人类收集原始资料，LLM 把资料编译成互相链接的 Markdown wiki，并在后续 ingest、query、lint 中持续更新。它的核心价值不是"让 AI 总结文档"，而是把分散来源整合成可追溯、可更新、可复利的概念网络。

## Core Pattern

基本架构是三层：

- `raw/`: 原始资料归档。它是事实来源，应该保持不可变。
- `wiki/`: 编译后的知识层。LLM 可以创建、合并、重写和维护页面。
- schema: 给 LLM 的操作规约，通常放在 `AGENTS.md`、`CLAUDE.md` 或技能文件中，规定命名、链接、来源、冲突处理和日志规则。

这个模式把知识处理前移到 ingest 阶段。传统 RAG 往往在提问时检索相似 chunk，再临时合成回答；LLM wiki 则在资料进入系统时就完成概念抽取、页面合并、交叉引用和索引更新。查询时，模型优先读取已经编译好的 wiki。

## Operations

Ingest 是核心操作。新资料进入 `raw/` 后，LLM 读取它，判断它影响哪些已有概念页或实体页，然后创建或更新 wiki 页面、维护交叉引用、更新索引，并写入日志。好的 ingest 不是一篇资料对应一篇摘要，而是把资料并入现有知识网络。

Query 是消费操作。用户提问时，LLM 先读 `wiki/index.md`，再读相关页面，最后用 wiki 中已有内容回答并给出引用。特别有价值的回答可以归档为新的 wiki 页面，让分析本身继续复利。

Lint 是健康检查。它用于发现断链、孤儿页面、过时说法、页面间矛盾、缺失交叉引用，以及被多次提到但还没有独立页面的概念。

## Difference From RAG

LLM wiki 与 RAG 的差异在于知识整理发生的时间点和产物形态。RAG 的主要产物是可检索 chunk，回答往往是临时生成的；LLM wiki 的主要产物是持久 Markdown 页面，回答建立在已经整理好的页面网络之上。

这种做法的优势是知识会积累：每次 ingest 都可能增强已有页面，每次高质量 query 都可以沉淀为新页面。代价是系统必须承担"编译损失"风险：LLM 在把 raw 压缩成 wiki 时可能遗漏事实、错误合并概念，或写出支持不足的综合判断。

## Practical Tooling

最小可行版本只需要文件系统、Markdown、一个 schema 文件和能读写文件的 LLM agent。Obsidian 很适合作为阅读和图谱浏览界面，但不是必需。

当规模扩大后，常见增强包括：

- hybrid search: BM25、向量检索和 reranking，用于查找 wiki 或 raw。
- MCP 或 CLI: 让 agent 能触发 ingest、query、lint。
- web UI: 上传资料、查看任务、浏览图谱、保存 query 结果。
- git: 记录 LLM 对 wiki 的每次改动，便于 diff 和回滚。

## Boundaries

这个模式适合中小规模、来源可控、需要长期积累的个人研究和项目知识。它不适合把大量低质量资料无差别倒入，也不适合未经人工复核就用于法律、医疗、金融等高风险判断。

最大技术风险是 lossy compilation。WiCER 论文把这个问题称为 compilation gap：原始资料中存在的关键事实没有被可靠保留到 wiki 中。缓解方向是让系统生成诊断问题、检查 wiki 能否回答、找出遗漏事实，再重新编译或补写页面。

## Operating Principles

- `raw/` 必须保留来源和采集日期。
- `wiki/` 中的关键结论要能追溯回 raw 或外部来源。
- 重要资料优先一次 ingest 一份，便于人工审阅。
- schema 要短而明确，避免让 agent 在每次会话里重新猜工作流。
- 定期 lint，尤其是在批量 ingest 之后。
- 高质量 query 结果应归档回 wiki。

## See Also

- [Karpathy LLM Wiki Skill Usage](karpathy-llm-wiki-usage.md)
