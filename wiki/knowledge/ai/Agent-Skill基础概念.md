---
type: "topic"
status: "active"
created: "2026-05-22"
updated: "2026-05-26"
sources:
  - "../../_raw/ai-engineering/agent-skill-basic-concepts-sources.md"
  - "https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md"
  - "https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me"
  - "https://github.com/mattpocock/skills"
  - "https://www.skills.sh/mattpocock/skills"
tags: ["ai", "technology", "agent", "skills", "ai-engineering"]
---

# Agent Skill 速记

- 定义：agent skill 是可复用的任务能力包，用来把稳定流程、约束、参考资料和脚本交给 agent 按需使用。
- 结构：常见形态是一个目录，核心文件是 `SKILL.md`；复杂 skill 可附带 `scripts/`、`references/`、`assets/`。
- 触发：agent 先读取名称和描述，任务匹配后再加载完整说明，需要时才读取附加资源。
- 适用：重复执行、步骤多、容易漏、依赖团队/项目/工具知识的工作流适合做成 skill。
- 不适用：一次性问题、简单事实查询、几句话能说明的偏好，不必做成 skill。
- 注意：第三方 skill 可能包含脚本或工具调用规则，安装前要检查 `SKILL.md`、脚本和依赖。

# 具体 Skill 介绍

## 提效类

### grill-me

- 细分：规划评审 / 需求澄清。
- 来源：[Raw SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md)、[GitHub 目录](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)、[GitHub 仓库](https://github.com/mattpocock/skills)、[skills.sh 索引](https://www.skills.sh/mattpocock/skills)。
- 用途：在实现前 stress-test 计划或设计，通过连续追问澄清目标、约束、依赖、边界和取舍。
- 场景：技术方案评审、架构决策前、项目计划落地前、需求边界不清时。
- 触发：用户提到 “grill me”、拷打方案、连续追问、stress-test plan/design 等。
- 备注：它不直接生成交付物，也不直接编码；每次只问一个问题，能通过代码库验证的问题先查代码库。

# Sources

- [OpenAI skills catalog](https://github.com/openai/skills)
- [Claude.ai Skills overview](https://claude.com/docs/skills/overview)
- [Claude Code skills docs](https://docs.claude.com/en/docs/claude-code/skills)
- [Anthropic guide: The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
- [grill-me Raw SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md)
- [grill-me GitHub directory](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)
- [mattpocock/skills GitHub repository](https://github.com/mattpocock/skills)
- [mattpocock/skills on skills.sh](https://www.skills.sh/mattpocock/skills)
