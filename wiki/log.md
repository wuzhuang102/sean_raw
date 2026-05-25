# 2026

## 2026-05

### 2026-05-25 | maintain | Wiki knowledge directory rename
- raw: none
- knowledge: `knowledge/`, `_meta/filing-rules.md`, `index.md`, `log.md`
- notes: 将可读知识层目录从 `pages/` 改名为 `knowledge/`，保留“领域优先、内容形态其次”的结构，并同步调整 skill 默认规则与日志字段。

### 2026-05-25 | maintain | Wiki category model
- raw: none
- knowledge: `_meta/filing-rules.md`, `index.md`, `knowledge/ai/summaries/ai-tools.md`, `knowledge/frontend-backend/fundamentals/docker-basic-syntax.md`, `knowledge/frontend-backend/technology/backend-knowledge-system.md`, `knowledge/ai/technology/agent-skills-basic-concepts.md`, `knowledge/ai/technology/llm-maintained-wiki.md`
- notes: 按用户要求调整为“领域优先、内容形态其次”：先分 AI、前后端/全栈，再分汇总、基础文档、技术、商业化。Docker 归入前后端基础文档，AI tools 归入 AI 汇总。

### 2026-05-25 | maintain | Wiki directory simplification
- raw: none
- knowledge: `knowledge/`, `notes/`, `_meta/filing-rules.md`, `index.md`, `log.md`
- notes: 将 wiki 从按知识类型分散的 `maps/`、`topics/`、`patterns/`、`reading-notes/`、`meta/` 重构为按使用方式组织的 `knowledge/`、`notes/`、`_meta/`；skill 改为按需创建目录，不再内置完整初始化树。

### 2026-05-25 | maintain | Wiki filing rules and AI tool catalog
- raw: none
- knowledge: `_meta/filing-rules.md`, `knowledge/ai/summaries/ai-tools.md`, `index.md`, `log.md`
- notes: 将“轻量分类内容作为聚合页子项维护”的规则固化到 wiki；AI 工具专栏改为默认维护工具条目，不再为每个工具单开 topic 页。

### 2026-05-25 | ingest | VoltAgent 与 awesome-design-md
- raw: `wiki/_raw/ai-tools/voltagent-design-md-sources.md`
- knowledge: `knowledge/ai/summaries/ai-tools.md`, `index.md`, `log.md`
- notes: 按用户要求对 VoltAgent 和 awesome-design-md 做轻量分类与简介：前者归为 TypeScript Agent 工程平台，后者归为 AI 辅助 UI 生成的 DESIGN.md 资源集合，不展开详细使用文档。

### 2026-05-25 | ingest | 后端知识体系
- raw: `wiki/_raw/backend/backend-knowledge-system-request.md`
- knowledge: `knowledge/frontend-backend/technology/backend-knowledge-system.md`, `index.md`, `log.md`
- notes: 整理后端技术栈总纲与学习地图，覆盖 API、应用分层、数据库、事务、缓存、消息队列、安全、可观测性、测试、部署、分布式和阶段化学习路径。

### 2026-05-25 | ingest | Browser Use 与 agent-computer-use
- raw: `wiki/_raw/ai-tools/browser-use-sources.md`, `wiki/_raw/ai-tools/agent-computer-use-sources.md`
- knowledge: `knowledge/ai/summaries/ai-tools.md`, `index.md`, `log.md`
- notes: 调研 Browser Use 和用户所称 compute-use 的最匹配项目 agent-computer-use，整理动态浏览器 Agent、托管浏览器、accessibility-first desktop control、Agent Skill 集成、适用场景和风险边界。

### 2026-05-25 | ingest | Freu CLI / Freu AI
- raw: `wiki/_raw/ai-tools/freu-cli-sources.md`
- knowledge: `knowledge/ai/summaries/ai-tools.md`, `index.md`, `log.md`
- notes: 开辟 AI 工具专栏，收集 Product Hunt、官网和 GitHub 仓库信息，整理 Freu CLI/Freu AI 的产品定位、AOT 编译工作流、Agent Skill 集成、适用场景和风险观察点。

### 2026-05-25 | reading-note | LLM Wiki
- raw: `wiki/_raw/ai-engineering/karpathy-llm-wiki.md`
- knowledge: `notes/technology.md`, `knowledge/ai/technology/llm-maintained-wiki.md`, `index.md`, `log.md`
- notes: 收集 Karpathy 的 LLM Wiki gist，按“少原文翻译、多总结判断”的方向沉淀为 LLM 维护持久 Markdown 知识库的实践模式，并预留后续实践经验入口。

### 2026-05-22 | reading-note | FDE——AI 时代的职业转型已经打响？
- raw: `wiki/_raw/sources/fde-ai-career-transition.md`
- knowledge: `notes/work.md`, `index.md`, `log.md`
- notes: 读取飞书 Wiki 文章，按职业转型和岗位形态归入 Work 阅读笔记，并将 reading-notes 分类入口迁移为扁平 markdown 文件。

### 2026-05-22 | maintain | Sean raw wiki maintenance rules
- raw: none
- knowledge: `index.md`, `log.md`
- notes: 将 index 改为按真实目录结构分组；合并同日重复日志，后续同日同主题维护应修订既有条目而不是机械追加。

### 2026-05-22 | revise | Agent Skill 基础概念
- raw: `wiki/_raw/ai-engineering/agent-skill-basic-concepts-sources.md`, `wiki/_raw/ai-engineering/grill-me-web-sources.md`
- knowledge: `knowledge/ai/technology/agent-skills-basic-concepts.md`, `index.md`, `log.md`
- notes: 整理 Agent Skill 页面：保留基础速记，将 grill-me 并入具体 skill 聚合页，按“提效类”二级分类组织，使用已验证可访问的 GitHub/skills.sh 来源链接。

### 2026-05-22 | maintain | Wiki page conventions
- raw: none
- knowledge: `index.md`, `knowledge/ai/technology/agent-skills-basic-concepts.md`, `knowledge/frontend-backend/fundamentals/docker-basic-syntax.md`, `log.md`
- notes: 统一页面标题策略：文件名/索引承载页面标题，正文从真实内容章节开始；移除重复 `title` frontmatter。

### 2026-05-22 | maintain | Raw source directory taxonomy
- raw: `wiki/_raw/infra/docker-basic-syntax-sources.md`
- knowledge: `knowledge/frontend-backend/fundamentals/docker-basic-syntax.md`, `log.md`
- notes: 将 raw 来源统一到 `wiki/_raw/` 并按语义目录归档，迁移 Docker 来源到 `wiki/_raw/infra/`。

### 2026-05-22 | ingest | Docker 常用基础语法
- raw: `wiki/_raw/infra/docker-basic-syntax-sources.md`
- knowledge: `knowledge/frontend-backend/fundamentals/docker-basic-syntax.md`, `index.md`, `log.md`
- notes: 调研 Docker 官方文档，整理镜像、容器、Dockerfile、存储、网络、Compose、清理命令和常见工作流。

### 2026-05-22 | init | Sean raw wiki workspace
- raw: none
- knowledge: none
- notes: 初始化 sean-llm-wiki 默认知识库。
