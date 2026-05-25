---
type: "pattern"
status: "active"
created: "2026-05-25"
updated: "2026-05-25"
sources:
  - "../../../_raw/ai-engineering/karpathy-llm-wiki.md"
  - "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
tags: ["ai", "technology", "llm", "knowledge-base", "wiki", "rag", "agent-workflow", "obsidian"]
---

# 原文要点

LLM-maintained wiki 的核心是让 LLM 持续维护 Markdown 知识库，而不是只在查询时从 raw source 临时拼答案。每次新增资料、追问或复盘，都应更新可复用页面，让上下文、已有结论、争议点、缺口和实践经验沉淀下来。

它和 RAG 的区别：RAG 偏“查询时找证据”，wiki 偏“摄入时编译知识”。两者可以结合，但 wiki 层应该沉淀结构化判断，raw/RAG 层负责证据追溯。

# 设计原则

## Raw 少而稳，Wiki 多总结

raw source 只承担证据层职责，保持原文或原始抓取即可，不在生成页里复制大量翻译。生成页应该优先写：

- 这个资料改变了什么判断。
- 它适合归入哪个长期概念、模式或 playbook。
- 它对当前 wiki 维护方式有什么启发。
- 哪些结论需要等待后续实践验证。

## Page 是工作台，不是文章译文

一个 durable knowledge page 应该像工作台：有核心判断、适用场景、操作原则、失败模式、待补经验和来源。它不应该变成原文的中文展开版。

## 每次输入都要问“沉淀到哪里”

输入可以是文章、经验、对话、代码阅读或问题。处理时不只写摘要，而是判断它应该沉淀到：

- `notes/`：轻量记录读过什么。
- `knowledge/`：稳定概念、工程模式、操作手册、技术对比、项目上下文和具体选择。

# 当前可采用的操作框架

## Ingest

最小有效流程：

1. 保存 raw。
2. 写一条轻量 reading note。
3. 选择一个 durable home。
4. 更新 durable knowledge page 的判断和结构。
5. 更新 index/log。

更重要的是第 3-4 步：如果只保存 raw 和阅读笔记，知识不会真正复利。

## Query

有复用价值的问题不应只停留在聊天记录里。答案如果形成了方法、比较、复盘或判断，应回写到 wiki。这样 wiki 不只是资料库，也是思考过程的沉淀层。

## Lint

定期检查 wiki 是否开始退化成“文件堆”：

- raw source 是否没有被吸收到 durable knowledge page。
- durable knowledge page 是否只是摘要合集，没有自己的判断。
- 重要概念是否散落在多个页面。
- index 是否还能反映真实导航。
- log 是否能解释最近为什么改动。

# 后续实践经验入口

后续追加实践时，优先补这些内容：

## 有效做法

- 待补充。

## 失败模式

- 待补充。

## 判断标准

- 待补充。

## 工作流改进

- 待补充。

# 在本 wiki 中的落地建议

- generated wiki 不追求覆盖原文细节，优先沉淀可复用判断。
- raw source 可以完整保存，但页面正文避免大段翻译。
- 后续用户追加实践经验时，直接合并到“后续实践经验入口”，再按需要拆成 playbook 或 decision。
- 对“实践经验”类内容，优先记录真实上下文、做法、结果和边界条件。

# Sources

- [Karpathy gist: LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Raw gist content](https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw)
