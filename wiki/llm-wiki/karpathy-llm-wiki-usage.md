# Karpathy LLM Wiki Skill Usage

> Sources: Local `karpathy-llm-wiki` skill, 2026-05-16
> Raw: [Karpathy LLM Wiki Skill Notes](../../raw/llm-wiki/2026-05-16-karpathy-llm-wiki-skill-notes.md)

## Overview

`karpathy-llm-wiki` 是本地 Codex 技能，用来在当前项目根目录维护个人 LLM wiki。它规定了 `raw/` 和 `wiki/` 的目录职责、ingest/query/lint 的行为、文章格式、索引格式和日志格式。

## Directory Contract

`raw/` 是不可变来源层。每次 ingest 都要把资料保存到 `raw/<topic>/`，文件名使用日期和描述性 slug。raw 文件包含来源、采集日期、发布时间，并保留资料本身或研究笔记。

`wiki/` 是编译知识层。文章放在 `wiki/<topic>/<article>.md`，只允许一层 topic 目录。文章应包含 Sources 和 Raw 元数据，正文要综合资料而不是照搬资料。

`wiki/index.md` 是全局目录。回答问题时先读它；ingest 后必须新增或更新被触及文章的条目。

`wiki/log.md` 是追加式操作日志。ingest、archive、lint 都要写入日期和操作摘要。

## Ingest Workflow

使用方式可以直接用自然语言触发，例如：

```text
把这篇文章 ingest 到个人 wiki
调研 X，然后 ingest 到个人 wiki
把这个 PDF 加到 LLM wiki
```

执行时应按顺序完成：

1. 检查并初始化 `raw/`、`wiki/`、`wiki/index.md`、`wiki/log.md`。
2. 获取来源内容，保存到合适的 `raw/<topic>/` 文件。
3. 判断是更新既有文章还是创建新概念页。
4. 写入或更新 `wiki/<topic>/<article>.md`。
5. 检查同 topic 文章和 index 中相关主题是否需要级联更新。
6. 更新 `wiki/index.md`。
7. 追加 `wiki/log.md`。

## Query Workflow

查询类请求不会改文件，除非用户明确要求归档。常见触发：

```text
我关于 X 知道什么？
总结 wiki 里和 Y 相关的内容
基于我的 wiki 对比 A 和 B
```

回答时先读 `wiki/index.md`，再读相关文章，并在对话里用 `wiki/topic/article.md` 形式引用。

## Lint Workflow

lint 用于维护健康度。确定性问题可以自动修：index 缺条目、唯一可定位的断链、Raw 引用路径错误、明显缺失的 See Also。判断性问题只报告：矛盾、过时、孤儿页、缺少冲突标注、跨主题引用不足、概念缺页等。

## Local Convention For This Wiki

本仓库当前将个人 LLM wiki 主题放在 `llm-wiki` topic 下：

- raw sources: `raw/llm-wiki/`
- compiled articles: `wiki/llm-wiki/`
- global index: `wiki/index.md`
- operation log: `wiki/log.md`

## See Also

- [Personal LLM Wiki](personal-llm-wiki.md)
