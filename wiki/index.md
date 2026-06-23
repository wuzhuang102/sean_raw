This wiki is maintained by the `sean-llm-wiki` skill. It is a working engineering knowledge base: readable by humans, maintained by LLMs, and grounded in raw source files when raw capture is needed.

# AI

## 汇总

- [AI 产品专栏](knowledge/ai/AI产品.md) - AI 下重要产品的轻量分类、产品分析、Agent 评测/治理平台、评价框架和后续拆页入口。
- [AI 工具专栏](knowledge/ai/AI工具.md) - AI 下重要 tool 项目的轻量分类、工具条目、代码智能与检索工具、评价框架和后续拆页入口。

## 技术

- [AI 建站](knowledge/ai/AI建站.md) - AI 辅助建站的长期入口；当前先沉淀网页设计专项，以及 AI 生成页面常见蓝紫色模板风的成因。
- [AI Agent 实战](knowledge/ai/AI%20Agent实战.md) - AI Agent 实战文章草稿，待后续补充。
- [Agent Skill 基础概念](knowledge/ai/Agent-Skill基础概念.md) - Agent skill 的组成、触发方式、适用边界和具体 skill 分类记录。
- [Agent Sandbox](knowledge/ai/Agent%20Sandbox.md) - Agent 受控执行环境的概念边界、典型使用场景、工具版图和选型框架，预留后续实践追加入口。
- [LLM-maintained wiki](knowledge/ai/LLM维护Wiki.md) - 用 LLM 增量维护持久 Markdown 知识库的架构、操作循环和实践边界。

# 前后端 / 全栈

## 汇总

- [技术学习资料](knowledge/技术学习资料.md) - 长期维护技术站点、专题课程和分类导航类资料入口，作为后端、通用工程与 AI Agent 工程补课时的资源索引。

## 基础文档

- [Python 入门到进阶](knowledge/frontend-backend/Python入门到进阶.md) - Python 从入门语法、小脚本、标准库，到测试、包管理、类型标注、Web 后端、数据处理和并发的学习路径与资料索引。
- [Docker 常用基础语法](knowledge/frontend-backend/Docker基础语法.md) - Docker 镜像、容器、Dockerfile、volume、网络、Compose 和清理命令的基础用法速查。

## 技术

- [后端知识体系](knowledge/frontend-backend/后端知识体系.md) - 后端技术栈能力地图，覆盖 API、数据库、事务、缓存、队列、安全、可观测性、部署、分布式和学习路径。
- [认证、授权与安全](knowledge/frontend-backend/后端知识点/认证授权与安全.md) - 后端安全基础专题，覆盖认证方式、会话、JWT、OAuth/OIDC 与 CAS 对比、权限模型、多租户隔离、常见 Web/API 风险、审计和检查清单。

# 产品

## 专题

- [工作、技术、AI、产品想法规划](knowledge/product/工作技术AI产品想法规划.md) - 长期记录和规划关于工作、技术、AI 与产品的个人判断、待验证问题、行动实验和后续拆页入口。
- [判断力](knowledge/product/判断力.md) - 长期沉淀判断力的来源、校准、决策应用和后续案例，先保留为可追加草稿。
- [产品 Sense](knowledge/product/产品Sense.md) - 产品判断力的形成机制、领域边界、用户接触方法、组织协作、社区争议和常见误区。

## 商业化 / 增长

- [Product Hunt 调研](knowledge/product/Product%20Hunt调研.md) - Product Hunt 作为科技产品发布、发现、早期反馈和社会证明平台的机制、使用手册、信号价值和局限。

# 商业化

商业化、行业分析、定价、增长、公司和产品商业化资料优先按领域落到 `knowledge/<domain>/`，并在索引中按“商业化”分组。当前已有产品领域的 [Product Hunt 调研](knowledge/product/Product%20Hunt调研.md)。

# Notes

- [Technology](notes/技术.md) - engineering, AI, architecture, tools, technical papers, and implementation writeups.
- [Work](notes/工作.md) - management, collaboration, retrospectives, organizational process, and career material.
- [Product](notes/产品.md) - product design, product judgment, UX, growth, requirements, and user research.

# Maintenance

- [Filing Rules](_meta/filing-rules.md) - 本 wiki 的本地分类规则，控制什么时候创建独立知识文件、什么时候写入聚合页子项。

# Directory Model

- `knowledge/ai/`: AI、Agent、LLM、模型、AI 工具和 AI 工程。
- `knowledge/frontend-backend/`: 前端、后端、全栈、基础设施和通用工程。
- `knowledge/frontend-backend/后端知识点/`: 后端知识体系拆出的详细知识点目录，用于承载比总纲更细的专题页面。
- `knowledge/product/`: 产品方法论、Product Sense、产品设计、用户研究、需求、增长、产品组织和产品商业化。
- `knowledge/技术学习资料.md`: 跨前后端、通用工程与 AI Agent 工程的学习资料入口。
- 领域目录下直接放知识文件；不再按 `summaries/`、`fundamentals/`、`technology/`、`business/` 继续分层。
- 跨领域资料导航页可以直接放在 `knowledge/` 顶层。
- 内容形态通过 frontmatter `type`、tags 和本索引中的分组表达。
- `notes/`: 轻量阅读记录；只创建实际有记录的分类文件。
- `_raw/`: 内部原始来源；只在需要保留 provenance 时创建。
- `_meta/`: 维护规则、分类规则、lint 和迁移记录。
