# Personal LLM Wiki Research

> Source: Codex web research memo using public sources listed below
> Collected: 2026-05-16
> Published: Unknown

## Sources consulted

- Andrej Karpathy, `llm-wiki.md` gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Juan M. Huerta, `WiCER: Wiki-memory Compile, Evaluate, Refine Iterative Knowledge Compilation for LLM Wiki Systems`: https://arxiv.org/abs/2605.07068
- xoai, `sage-wiki`: https://github.com/xoai/sage-wiki
- NiharShrotri, `llm-wiki`: https://github.com/NiharShrotri/llm-wiki
- Proudfrog, `The Complete Guide to Karpathy's LLM Wiki Workflow`: https://proudfrog.com/en/insights/karpathy-llm-wiki-complete-workflow-guide
- acmerfight, `Karpathy LLM Wiki 方法论深度解读`: https://gist.github.com/acmerfight/1c26b29ef39c0acc20f2e6f1f84e025f

## Research notes

Personal LLM wiki is a file-system-based personal knowledge base where raw source documents are kept immutable and an LLM incrementally compiles them into persistent markdown wiki pages. The key shift is from query-time retrieval to ingest-time synthesis. Instead of answering by repeatedly searching raw chunks, the agent reads sources once, extracts entities and concepts, updates existing pages, adds cross-references, and maintains an index and operation log.

The core architecture is three layers:

- `raw/`: immutable source archive. It stores articles, notes, papers, transcripts, PDFs converted to text, or other original inputs. The LLM reads these files but should not rewrite them.
- `wiki/`: compiled knowledge layer. The LLM owns these markdown pages and may create, merge, restructure, and update them when new evidence arrives.
- schema file: operating rules for the agent, often `CLAUDE.md`, `AGENTS.md`, or a skill file. It defines file naming, article shape, update rules, citation rules, linting behavior, and human review conventions.

The important operations are:

- Ingest: add a new source, identify the concepts and existing pages it touches, create or update wiki articles, update index, and append a log entry. A good ingest is not a one-document summary; it performs local integration into the knowledge graph.
- Query: answer from the wiki first, with citations to relevant pages. Useful answers can be archived back into the wiki so analysis compounds rather than disappearing in chat history.
- Lint: periodically health-check the wiki for broken links, orphan pages, stale claims, contradictions, missing cross-references, and important concepts that deserve their own pages.

Compared with classic RAG, the wiki pattern moves editorial work earlier. RAG chunks and embeds sources, then retrieves similar chunks at question time. LLM wiki compiles sources into durable pages before questions are asked. This makes cross-references and contradiction handling persistent, but it also introduces compilation risk: the LLM can omit facts, over-merge concepts, or write confident synthesis that is not fully supported by sources.

Practical implementations are converging on markdown plus agent tooling. Some stay simple with Obsidian, `raw/`, `wiki/`, and a schema file. Others add hybrid search, embeddings, reranking, MCP servers, web upload UIs, watch modes, and graph visualizations. Community implementations commonly support PDFs, markdown, HTML, DOCX, and text files; some use BM25 plus vector search when the wiki grows too large for a single `index.md`.

Scale and risk profile:

- Works best for curated personal or team knowledge where source quality is controlled and the human reviews the compiled pages.
- At small to moderate scale, a single index file can guide the agent to relevant pages.
- At larger scale, the system needs search over both raw and wiki layers, sharding by topic, or a retrieval step over the compiled pages.
- The main failure mode is lossy compilation: facts present in raw sources may not survive into the wiki. The WiCER paper frames this as a compilation gap and proposes evaluate/refine loops to recover omitted facts.
- Raw provenance is essential. The wiki can be rewritten, but every material claim should remain traceable to raw source files or external citations.

Good use cases:

- Personal research notes and paper reading.
- Interview or technical prep where many notes should become concept pages.
- Project knowledge, design decisions, and recurring explanations.
- Meeting transcript synthesis, if the schema accounts for speaker attribution, decisions, and action items.

Poor fit or caution areas:

- Legal, medical, financial, or compliance repositories without strong human review.
- Large uncurated document dumps where source noise will dominate.
- Exact lookup data that is already tabular or structured; those should often stay in databases or structured files rather than being flattened into prose.

Operational recommendations:

- Keep `raw/` immutable and versioned.
- Treat `wiki/` as LLM-owned generated knowledge, not hand-maintained notes.
- Keep a short, explicit schema for ingest/query/lint rules.
- Require every article to include source provenance and raw links.
- Prefer one-source-at-a-time ingest for important material.
- Run lint after significant ingestion batches.
- Archive especially useful query answers back into the wiki.
- Use search only when the wiki outgrows the index; do not start with unnecessary infrastructure.
