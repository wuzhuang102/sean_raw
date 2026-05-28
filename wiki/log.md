# 2026

## 2026-05

### 2026-05-28 | ingest | Python 入门到进阶
- raw: none
- knowledge: `knowledge/frontend-backend/Python入门到进阶.md`, `knowledge/frontend-backend/技术学习资料.md`, `index.md`, `log.md`
- notes: 整理 Python 从入门到进阶的系统学习路径，按语法、小脚本、标准库、项目结构、测试、包管理、类型标注、并发、Web 后端和数据处理组织，并补充已验证可访问的官方与优质外部资料链接；追加变量与类型、条件、循环、函数、列表/字典、字符串、异常、模块导入等基础语法示例，以及批量重命名、CSV 汇总、CLI、pytest、FastAPI、asyncio 和 pandas 的具体示例与关注点。

### 2026-05-28 | ingest | Agent Sandbox
- raw: `wiki/_raw/ai-engineering/agent-sandbox-sources.md`
- knowledge: `knowledge/ai/Agent Sandbox.md`, `index.md`, `log.md`
- notes: 按用户要求将页面收缩为最小骨架，只保留历史背景、定义和使用场景；后续工具、选型和实践内容单独追加。

### 2026-05-27 | catalog | 技术学习资料
- raw: none
- knowledge: `knowledge/frontend-backend/技术学习资料.md`, `index.md`, `log.md`
- notes: 按用户要求不作为 notes 保存；新建技术学习资料聚合页，并将程序园 Article 分类页以一句话介绍的轻量条目归入后端与通用工程学习资料。

### 2026-05-27 | classify | AnyGen
- raw: none
- knowledge: `knowledge/ai/AI产品.md`, `log.md`
- notes: 将 AnyGen 作为 AI 办公与知识工作产品补入 AI 产品专栏，记录其文档、幻灯片、分析型工作台定位，以及适用场景与采用风险。

### 2026-05-27 | ingest | Product Sense Reddit discussion
- raw: `wiki/_raw/product/product-sense-reddit-discussion.md`
- knowledge: `knowledge/product/产品Sense.md`, `index.md`, `log.md`
- notes: 按用户要求不写入读书笔记；将 Reddit r/ProductManagement 的 Product Sense 讨论补充为 Product Sense 专题数据源，记录社区对客户理解、领域判断、产品直觉和面试主观门槛的分歧。

### 2026-05-26 | ingest | CodeGraph
- raw: `wiki/_raw/ai-tools/codegraph-readme.md`
- knowledge: `knowledge/ai/AI工具.md`, `index.md`, `log.md`
- notes: 将 CodeGraph 作为本地语义代码图谱与 MCP code intelligence 工具归入 AI 工具专栏，记录其 tree-sitter/SQLite/FTS5 索引、符号与调用关系查询、route extraction、impact analysis、affected tests、Agent 集成和评估风险。

### 2026-05-26 | ingest | Product Judgment / 产品 Sense
- raw: `wiki/_raw/product/product-judgment-intercom.html`
- knowledge: `notes/产品.md`, `knowledge/product/产品Sense.md`, `index.md`, `log.md`
- notes: 抓取 Intercom Product Judgment 文章，新增产品类阅读笔记，并沉淀为 Product Sense 专题：整理直接用户接触、领域特定性、判断力边界、组织协作和训练清单。

### 2026-05-26 | maintain | Wiki knowledge 目录扁平化
- raw: none
- knowledge: `knowledge/ai/`, `knowledge/frontend-backend/`, `_meta/filing-rules.md`, `index.md`, `log.md`
- notes: 按用户要求移除 `knowledge/ai/` 和 `knowledge/frontend-backend/` 下按内容形态继续分层的目录；知识文件直接放在领域目录下，汇总、基础、技术、商业化等语义改由 `index.md` 分组、frontmatter `type` 和 tags 表达。

### 2026-05-26 | maintain | _meta 与 _raw 文件恢复英文命名
- raw: `wiki/_raw/`
- knowledge: `_meta/filing-rules.md`, `log.md`
- notes: 按用户要求将 `_meta/` 维护文件和 `_raw/` 原始来源文件恢复为英文文件名；`knowledge/` 与 `notes/` 下的可读 wiki 文件继续使用中文文件名，并同步更新内部引用。

### 2026-05-26 | maintain | 顶层导航文件恢复英文命名
- raw: none
- knowledge: `index.md`, `log.md`, `_meta/filing-rules.md`
- notes: 按用户要求将顶层导航和维护日志文件恢复为 `index.md` 与 `log.md`；其他 wiki Markdown 文件继续使用中文文件名，目录名保持英文不变。

### 2026-05-26 | maintain | 现有 wiki 文件中文命名迁移
- raw: `wiki/_raw/`
- knowledge: `index.md`, `log.md`, `_meta/filing-rules.md`, `knowledge/`, `notes/`
- notes: 按用户要求仅处理 wiki 内文件，将现有 Markdown 文件改为中文文件名或中文加必要专有名词；目录名保持英文结构不变，并同步替换 wiki 内部链接和历史日志路径。

### 2026-05-26 | maintain | Wiki 文件命名规则
- raw: none
- knowledge: `_meta/filing-rules.md`, `log.md`
- notes: 写入底层规则：wiki 中的具体 Markdown 文件名默认使用中文维护，目录名继续沿用现有英文结构；旧文件不自动批量重命名，后续新建或迁移时同步更新链接和日志。

### 2026-05-26 | ingest | Pencil.dev
- raw: `wiki/_raw/ai-products/pencil-dev-sources.md`
- knowledge: `knowledge/ai/AI产品.md`, `knowledge/ai/AI工具.md`, `_meta/filing-rules.md`, `index.md`, `log.md`
- notes: 调研 Pencil.dev 作为 AI-native 设计产品：按用户要求将 AI 产品和 AI 工具拆为两个专栏维护，Pencil.dev 迁入 AI 产品专栏，记录 IDE/桌面/CLI 入口、`.pen` Git-friendly 文件、MCP 设计操作、design-to-code 工作流、适用场景和评估风险。

### 2026-05-25 | maintain | Wiki knowledge directory rename
- raw: none
- knowledge: `knowledge/`, `_meta/filing-rules.md`, `index.md`, `log.md`
- notes: 将可读知识层目录从 `pages/` 改名为 `knowledge/`，保留“领域优先、内容形态其次”的结构，并同步调整 skill 默认规则与日志字段。

### 2026-05-25 | maintain | Wiki category model
- raw: none
- knowledge: `_meta/filing-rules.md`, `index.md`, `knowledge/ai/AI工具.md`, `knowledge/frontend-backend/Docker基础语法.md`, `knowledge/frontend-backend/后端知识体系.md`, `knowledge/ai/Agent-Skill基础概念.md`, `knowledge/ai/LLM维护Wiki.md`
- notes: 按用户要求调整为“领域优先、内容形态其次”：先分 AI、前后端/全栈，再分汇总、基础文档、技术、商业化。Docker 归入前后端基础文档，AI tools 归入 AI 汇总。

### 2026-05-25 | maintain | Wiki directory simplification
- raw: none
- knowledge: `knowledge/`, `notes/`, `_meta/filing-rules.md`, `index.md`, `log.md`
- notes: 将 wiki 从按知识类型分散的 `maps/`、`topics/`、`patterns/`、`reading-notes/`、`meta/` 重构为按使用方式组织的 `knowledge/`、`notes/`、`_meta/`；skill 改为按需创建目录，不再内置完整初始化树。

### 2026-05-25 | maintain | Wiki filing rules and AI tool catalog
- raw: none
- knowledge: `_meta/filing-rules.md`, `knowledge/ai/AI工具.md`, `index.md`, `log.md`
- notes: 将“轻量分类内容作为聚合页子项维护”的规则固化到 wiki；AI 工具专栏改为默认维护工具条目，不再为每个工具单开 topic 页。

### 2026-05-25 | ingest | VoltAgent 与 awesome-design-md
- raw: `wiki/_raw/ai-tools/voltagent-design-md-sources.md`
- knowledge: `knowledge/ai/AI工具.md`, `index.md`, `log.md`
- notes: 按用户要求对 VoltAgent 和 awesome-design-md 做轻量分类与简介：前者归为 TypeScript Agent 工程平台，后者归为 AI 辅助 UI 生成的 DESIGN.md 资源集合，不展开详细使用文档。

### 2026-05-25 | ingest | 后端知识体系
- raw: `wiki/_raw/backend/backend-knowledge-system-request.md`
- knowledge: `knowledge/frontend-backend/后端知识体系.md`, `index.md`, `log.md`
- notes: 整理后端技术栈总纲与学习地图，覆盖 API、应用分层、数据库、事务、缓存、消息队列、安全、可观测性、测试、部署、分布式和阶段化学习路径。

### 2026-05-25 | ingest | Browser Use 与 agent-computer-use
- raw: `wiki/_raw/ai-tools/browser-use-sources.md`, `wiki/_raw/ai-tools/agent-computer-use-sources.md`
- knowledge: `knowledge/ai/AI工具.md`, `index.md`, `log.md`
- notes: 调研 Browser Use 和用户所称 compute-use 的最匹配项目 agent-computer-use，整理动态浏览器 Agent、托管浏览器、accessibility-first desktop control、Agent Skill 集成、适用场景和风险边界。

### 2026-05-25 | ingest | Freu CLI / Freu AI
- raw: `wiki/_raw/ai-tools/freu-cli-sources.md`
- knowledge: `knowledge/ai/AI工具.md`, `index.md`, `log.md`
- notes: 开辟 AI 工具专栏，收集 Product Hunt、官网和 GitHub 仓库信息，整理 Freu CLI/Freu AI 的产品定位、AOT 编译工作流、Agent Skill 集成、适用场景和风险观察点。

### 2026-05-25 | reading-note | LLM Wiki
- raw: `wiki/_raw/ai-engineering/karpathy-llm-wiki.md`
- knowledge: `notes/技术.md`, `knowledge/ai/LLM维护Wiki.md`, `index.md`, `log.md`
- notes: 收集 Karpathy 的 LLM Wiki gist，按“少原文翻译、多总结判断”的方向沉淀为 LLM 维护持久 Markdown 知识库的实践模式，并预留后续实践经验入口。

### 2026-05-22 | reading-note | FDE——AI 时代的职业转型已经打响？
- raw: `wiki/_raw/sources/fde-ai-career-transition.md`
- knowledge: `notes/工作.md`, `index.md`, `log.md`
- notes: 读取飞书 Wiki 文章，按职业转型和岗位形态归入 Work 阅读笔记，并将 reading-notes 分类入口迁移为扁平 markdown 文件。

### 2026-05-22 | maintain | Sean raw wiki maintenance rules
- raw: none
- knowledge: `index.md`, `log.md`
- notes: 将 index 改为按真实目录结构分组；合并同日重复日志，后续同日同主题维护应修订既有条目而不是机械追加。

### 2026-05-22 | revise | Agent Skill 基础概念
- raw: `wiki/_raw/ai-engineering/agent-skill-basic-concepts-sources.md`, `wiki/_raw/ai-engineering/grill-me-web-sources.md`
- knowledge: `knowledge/ai/Agent-Skill基础概念.md`, `index.md`, `log.md`
- notes: 整理 Agent Skill 页面：保留基础速记，将 grill-me 并入具体 skill 聚合页，按“提效类”二级分类组织，使用已验证可访问的 GitHub/skills.sh 来源链接。

### 2026-05-22 | maintain | Wiki page conventions
- raw: none
- knowledge: `index.md`, `knowledge/ai/Agent-Skill基础概念.md`, `knowledge/frontend-backend/Docker基础语法.md`, `log.md`
- notes: 统一页面标题策略：文件名/索引承载页面标题，正文从真实内容章节开始；移除重复 `title` frontmatter。

### 2026-05-22 | maintain | Raw source directory taxonomy
- raw: `wiki/_raw/infra/docker-basic-syntax-sources.md`
- knowledge: `knowledge/frontend-backend/Docker基础语法.md`, `log.md`
- notes: 将 raw 来源统一到 `wiki/_raw/` 并按语义目录归档，迁移 Docker 来源到 `wiki/_raw/infra/`。

### 2026-05-22 | ingest | Docker 常用基础语法
- raw: `wiki/_raw/infra/docker-basic-syntax-sources.md`
- knowledge: `knowledge/frontend-backend/Docker基础语法.md`, `index.md`, `log.md`
- notes: 调研 Docker 官方文档，整理镜像、容器、Dockerfile、存储、网络、Compose、清理命令和常见工作流。

### 2026-05-22 | init | Sean raw wiki workspace
- raw: none
- knowledge: none
- notes: 初始化 sean-llm-wiki 默认知识库。
