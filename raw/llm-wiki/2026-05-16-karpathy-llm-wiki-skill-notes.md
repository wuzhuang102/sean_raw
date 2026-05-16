# Karpathy LLM Wiki Skill Notes

> Source: Local skill file `/Users/bytedance/.agents/skills/karpathy-llm-wiki/SKILL.md`
> Collected: 2026-05-16
> Published: Unknown

## Source notes

The local `karpathy-llm-wiki` skill defines a personal knowledge base workflow using two project-root directories:

- `raw/`: immutable source material. The assistant reads source files here and does not rewrite them.
- `wiki/`: compiled knowledge articles. The assistant has ownership of this layer and updates it as the knowledge base evolves.

Initialization happens only on first ingest. If `raw/` and `wiki/` do not exist, create missing directories, `.gitkeep` placeholders, `wiki/index.md`, and `wiki/log.md`. Query and lint operations should not initialize a missing wiki; they should tell the user to run an ingest first.

Every ingest must do both steps:

1. Fetch source content into `raw/<topic>/YYYY-MM-DD-descriptive-slug.md`.
2. Compile it into one or more wiki articles under `wiki/<topic>/<article>.md`.

Raw files need a title plus metadata for source URL or origin, collected date, and published date. If the published date is unknown, the metadata should say `Unknown`; if the file date is unknown, the date prefix may be omitted.

Compilation rules:

- Merge into an existing article when the source has the same core thesis.
- Create a new article when it introduces a new concept.
- If a source spans topics, place it in the most relevant topic and add See Also links.
- Annotate factual conflicts when new sources contradict existing content.
- Refresh the Updated date of materially changed articles.

After every ingest:

- Update `wiki/index.md` with every touched article.
- Append an operation entry to `wiki/log.md`.

Query behavior:

- Read `wiki/index.md` first.
- Read relevant articles.
- Answer from wiki content before relying on model memory.
- Cite wiki articles using project-root-relative paths in conversation.
- If the user asks to archive a query answer, write a new archive page, update the index, and log it.

Lint behavior:

- Deterministic checks can be auto-fixed: missing index entries, broken internal links with a unique fix, raw references with a unique fix, and obvious See Also maintenance.
- Heuristic checks should be reported: contradictions, stale claims, missing conflict notes, orphan pages, missing cross-topic references, concepts that deserve pages, and archive pages that may be stale.

The skill convention keeps `wiki/` one topic-directory level deep: `wiki/<topic>/<article>.md`. Links inside wiki files are relative to the current file. Conversation citations use project-root-relative paths.
