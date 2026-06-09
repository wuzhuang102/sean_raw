source: https://my.feishu.cn/wiki/ToaRw8BAUiAyFFkR3EAc05atnsg
fetched: 2026-06-09
format: lark docs +fetch markdown

<title>Harness 101：Loop Engineering—从 ReAct 到 Orchestration</title>

# 前言

2026 年春节前在我们从头设计 DeerFlow 2.0 时，曾认真考虑过一件当时觉得有点“反直觉”的事：与其为某一类任务费心写一个 Skill，让模型每次照着这份说明书临场发挥，**不如让 AI 直接为这个任务生成一段代码**，把流程钉进脚本里，之后照着脚本跑。当时这个想法没有名字，我们也没敢把它推到台前。现在回头看，它其实有了名字——这正是 Claude Code 之父 **Boris Cherny** 近期推出的 **Dynamic Workflow**，以及它背后那个更大的趋势：**Loop Engineering**。

让我把这件事说得更直白一些。Claude Code 的作者 Boris Cherny 在一次访谈里说过一句让笔者印象很深的话：

<callout emoji="👨‍🦲">
I don't **prompt** Claude anymore. I have **loops** running that prompt Claude and figuring out what to do.
*by Boris Cherny*
> 我已经不再亲自去 **prompt** Claude 了，我让一堆 **loop** 跑着，由它们来 prompt Claude、替我决定下一步做什么。
</callout>

同一时期，OpenClaw 之父 **Peter Steinberger** 也表达过几乎一样的判断——你不该再去 prompt 你的 coding agent，你该去设计那个替你 prompt agent 的 loop。两个人，两个团队，指向的是同一个方向。Addy Osmani 后来把这股潮流命名为 [Loop Engineering](https://addyosmani.com/blog/loop-engineering/)：你要做的不是写更好的 Prompt，而是设计一个能持续找活、派活、验收、记录、再决定下一步的 loop，让这个 loop 去戳 agent，而不是你自己。

<callout emoji="🔥">
**你知道吗——Loop Engineering 正在成为社区热词？**
它并不是某个人的个人口号。Boris Cherny（Claude Code）说“我的工作就是写 loop”，Peter Steinberger（OpenClaw）说“你应该设计让 agent 被 prompt 的 loop”，Addy Osmani 把这股潮流总结成 Loop Engineering——把找活、派活、验收、记账、决策这几件事固化成一个能自跑的系统。这更像是 Claude Code、Codex 这些团队不约而同走到的同一个路口。
</callout>

[在这个系列里](https://my.feishu.cn/wiki/L082wubkdie8uMkRUjgceKYQnIe)，我们聊过 Harness 如何自我进化。Loop Engineering 是紧随其后的又一个趋势——它不是笔者一个人的观察，而是 Claude Code、Codex 这些团队当下正在共同走的方向。它和 Harness 的话题彼此呼应，但落点不太一样：Harness 关心的是 agent 运行时周围的那一圈基础设施，而 Loop 关心的是“一次任务到底由哪些环节串成、这些环节怎么被组织起来反复跑”。

那它到底解决什么问题？说白了，Loop Engineering 针对的是那种**有明确阶段、有验收标准、还要被反复执行**的任务。这类任务如果只靠一条 Prompt 或一次 ReAct 跑下来，等于把整条流程都压在模型这一次的临场发挥上——偶尔成功，但跑得多了就会发现它不稳、丢步骤、也没法复盘。Loop Engineering 做的事，就是把这样一条任务拆成环节、组织成一个能反复跑、看得见、还能从断点续上的 loop，把流程的确定性从模型脑子里挪到结构里。但它不是万能药：面对一次性的、探索性的、边界还很模糊的任务，开一段对话、写一个 Skill 往往更轻、更灵活；搭一个 loop 是有前期成本的，只有当任务会被反复执行、阶段足够清晰、又需要可审计时，这份成本才真正划算。

至于为什么是现在——笔者觉得有三股力量凑到了一起。一是模型终于稳到可以被当成一个“可靠的被调用者”，你敢把一个子任务整段交给它；二是旗舰模型已经强到能把这段编排脚本现场生成出来，搭 loop 的门槛被拉低了；三是 agentic coding 用得越来越多，大家陆续撞上了单次 ReAct 的天花板，自然会往“把流程固化下来、让它能反复跑”这个方向找出路。三者叠加，Loop Engineering 就从少数人的玩法，变成了一个摆在台面上的趋势。

这篇文章想做两件事。一是把 Skill 和 Workflow 的分野讲清楚——它们常被混为一谈，但其实各管一段。二是把一个 loop 到底由什么构成讲清楚——当我们说“设计一个 loop”，到底是在设计什么。需要先说明的是，文中用来举例的 **DeerFlow 3.0** 预计的 API 形式还是计划阶段的草样，随时可能改；笔者更想借它把背后的思路讲明白，而不是把它当成定稿来推。



<grid><column width-ratio="0.500000"><p><b>加入 Agentara 2 群：</b></p><chat_card name="📯 Agentara Underground 情报站（2群）" chat-id="oc_87790dff43e23d2205d78baa8bff4f38"></chat_card></column><column width-ratio="0.500000"><p><b>加入 Agentara Undergound 情报站</b></p><p>加群获取更多线上资料，和 9,500+ 位 AI 爱好者一起学习 Prompt、Context Engineering、Harness Engineering 和 Skills。</p><blockquote><p><b>已经加入过 1 群的小伙伴</b>不用重复加入，也请分享给需要的同学们</p></blockquote><p></p></column></grid>



---



# 从 ReAct 到 Orchestration

第一代 Agent 范式的名字叫 **ReAct**。它的思路很优雅：让 LLM 自己充当那个 loop——reason（想一步）、act（做一步）、observe（看结果），再回到 reason，如此往复，直到任务完成。流程不写在代码里，而是藏在模型每一轮推理的“脑子”里；工程师能做的，是再配一份 Skill，当作交给模型的说明书，告诉它这类任务该怎么一步步走。

这套范式很好用，但放到要稳定交付的场景里，它的代价会慢慢显出来。最容易被提起的是 loop 本身的维护成本，但笔者觉得更要紧的，是它把整条流程的重量都压在了**模型运行时的 Instruction Following 上**。每跑一步，都要模型当场把 Skill 读懂、不跑偏、不漏步骤、不把顺序搞乱。一旦某一步理解偏了，后面整条链路就跟着歪下去，而且事后很难复盘——你说不清它到底是在哪一步、为什么飘走的。于是这套流程不太可靠、不太能重放、也不太好审计；更现实的是，往往只有旗舰模型才勉强扛得住这种全程高强度的 Instruction Following。

先看 ReAct 自己充当 loop 的样子——模型一个人既做决策又做执行，流程在它脑子里转圈：

![](https://feishu.cn/file/Xk1lbYFpvoUfbJxHlGaces2JnRe)

Orchestration 走的是另一条路。它无需模型在运行时凭 Prompt Instructions 或记忆维持流程，而是**先用一个模型（通常是旗舰模型），把整条流程一次性“编译”成一段 Workflow Script**——把每一步的 Prompt、要喂进去的上下文，都写进这段代码里。之后真正执行的时候，确定性交给代码（阶段顺序、异步并行、同步等待、循环、逻辑分支由脚本表达），判断力才留给被代码显式调用的 LLM：

![](https://feishu.cn/file/Yye7bfA7woN3cSxn99RcrGQ6nje)

这里有一件容易被忽略、却恰恰最关键的事：**这段 Workflow Script 本身就是模型生成的**。它不是懂 JavaScript 的工程师手写死的静态 pipeline，而是旗舰模型按“这次是什么任务”现场写出来的——这正是 Dynamic Workflow 里“Dynamic”的由来。生成之后，它就是一段普通的、看得见摸得着的代码，用户随时可以手工改它、把它固化下来、之后反复复用。

把流程编译成代码，换来一个很实际的好处。脚本一旦生成，结构就固化进了代码本身，运行时不再需要模型靠强 Instruction Following 去维持流程——于是负责 orchestration 的那个 agent，以及它派出去干活的各个 sub-agent，**都可以落到普通模型上**。旗舰模型只在“生成这段脚本”时出场一次，之后的多次执行交给便宜、够用的普通模型。一句话概括：**旗舰模型生成一次，普通模型执行多次**。稳定性、灵活性、可复用性、可观测性大体都能保住，成本还顺手压了下来。

那么 Loop Engineering 到底指什么？笔者比较认同 Boris Cherny 的讲法。他说自己几乎不再亲手给 Claude 写 Prompt 了，取而代之的是一些一直在跑的 loop，由这些 loop 去 prompt Claude。换句话说，工作的重心从“写好这一次的 Prompt”，挪到了“设计那个会反复 prompt agent 的循环”。这个循环负责把一类活儿从头管到尾：找活、把活拆开派给 agent、验收产出、记录状态、决定下一步该干什么——它能自己跑起来，人只在需要的时候搭把手。把这套围绕 loop 来组织工作的工程实践叫作 Loop Engineering，笔者觉得是贴切的。

要分清的是，Loop Engineering 是一种宏观的工程姿态，它并没有规定 loop 必须长成什么样——你可以用一个常驻进程加几个定时任务把它搭起来，也可以用别的形式。Dynamic Workflow 只是其中一种具体形态：它把“单个 loop”落成一段模型生成的脚本，用代码把骨架钉死、用 `agent()` 把智能嵌进去。本文之所以拿它当主角，是因为它把前面那条“确定性交给代码、判断力交给模型”的思路表达得最干净。下一节就从它和 Skill 的对照说起。



---



# Skill 与 Dynamic Workflow 的分水岭

Skill 和 Dynamic Workflow 常被放在一起谈，也常被混为一谈，但它们其实各管一段。把这条分野讲透，是这篇文章里笔者最想说清楚的一件事。

Skill 是写给 LLM 读的自然语言指令。它是一份说明书，灵活、可组合，你可以把好几个 Skill 凑在一起让模型自己取用。代价是：执行路径每一次都由模型即兴决定——这一回它先做 A 再做 B，下一回可能顺序就变了，甚至漏掉中间一步。稳定性靠模型“自觉”，因此对运行时的 Instruction Following 要求很高，往往只有旗舰模型才跑得比较稳。

Dynamic Workflow 是一段确定性代码。流程被钉死在脚本里，阶段顺序、并行、循环、分支由代码决定，绝不会因为模型“今天状态不太好”就丢了某一步。而 LLM 只在被显式调用的地方介入——比如 `agent()` 负责一段需要智能的子任务，`assert()` 负责一次需要判断的验收。代码管编排，模型管思考，各司其职。

两者的取舍，其实可以用一句话概括：**Skill 把结构交给模型，Workflow 把结构交给代码**。下面这张表把几个维度摊开对照：

| 维度 | Skill | Dynamic Workflow |
|-|-|-|
| 结构归属 | 交给模型，运行时即兴决定路径 | 交给代码，路径写死在脚本里 |
| 稳定性 | 靠模型自觉，每次可能不同 | 流程固化，绝不丢步骤 |
| 对运行时 Instruction Following 的要求 | 很高，每步都要模型当场读懂照做 | 很低，结构已进代码，模型只管被调用处 |
| 执行可用的模型档位 | 往往得用旗舰模型才跑得稳 | orchestration agent 与 sub-agent 都能用普通模型 |
| 可复用性 | 可复用，但每次执行结果会漂 | 脚本可存档、可反复跑出可比结果 |
| 可观测性 | 路径藏在模型脑子里，难审计 | 阶段、日志显式可见，可重放可审计 |
| 适合场景 | 探索性、边界模糊、要临场应变 | 阶段清晰、有验收标准、要稳定交付 |

把这张表读完，本文的中心论点也就浮出来了。一旦把结构交给代码，运行时就不再需要模型一个人扛住整条流程——于是 orchestration agent 和它派出去的 sub-agent 都可以降级到普通模型，旗舰模型只在“生成这段脚本”时出场那一次。

不过笔者想强调，**这并不是用代码去“取代”LLM**。Dynamic Workflow 的**精妙之处**，恰恰在于它用代码去**“编排（Orchestration）”**LLM——确定的事情让代码稳稳地执行，需要智能和灵活的地方仍然原原本本地交还给模型。它既要稳定，又要保住智能，两头都想要。

说到这里，笔者其实有点感慨：这正是我们做 DeerFlow 2.0 时隐约想要、却没能给它一个名字的东西。当时只觉得“让 AI 生成一段代码再照着跑”是个不太正经的念头，现在看来，它也许正是把灵活和稳定一起握住的那条缝。



---



# 一段深度研究 Workflow

前面讲的都是抽象，现在把它落到地上。我们拿“深度研究”这个任务做例子——给定一个用户问题，先快速理解，再拆成几个子课题并行去查，整合成稿，反复审改，最后做一次最终验证（终验）。这是一条阶段分明、又带验收标准的复杂任务，正适合用一段 Dynamic Workflow 来表达。

有一点想先说清楚：下面这段脚本不是哪位工程师坐下来一行行手写的，而是旗舰模型按“深度研究”这个任务现场生成的产物。**在 DeerFlow 3.0 的计划里**，它出自一个叫 workflow-creator 的 Skill——你把任务描述给它，它把这条 loop 写成代码交还给你。生成之后，这段脚本就是你的了：你可以手工改它、存档它、下次再原样跑一遍。

在读那一大段 JavaScript Workflow 脚本之前，先给大家看一张图建立骨架：

![](https://feishu.cn/file/HaNgbrNJhoV14SxlLkvcCPTUnnh)

骨架就是这么简单：快搜、规划、并行研究、起草、审稿循环、终验。审稿那一环画了一条回头的边，由 `assert` 判定是否要回炉——这是整条 loop 里唯一会循环的地方。

Workflow 的 API 很简单就这么几个：

```TypeScript
/* ====== 核心 LLM 方法 ===== */

// 用于创建子 Agent
async agent(taskPrompt, verificationPrompt?) 

// 用于通过 LLM 做断言（判断）
async assert(prompt): Promise<boolean> 


/* ====== 用户交互与反馈方法 ===== */

// 向用户发送当前进度通知
phase(phaseName, desc)  

// 向用户发送日志
log(text) 
```

让我们看一个 DeerFlow Deep Research 的示例，全部由模型生成：

```JavaScript
// 以下代码由 DeerFlow 3.0 workflow-creator Skill 按"深度研究"任务生成
// 部分和 Claude Code 的 API 略微有所不同

// `meta` 是不是和 Skill 的 Frontmatter 非常相似？
export const meta = {
  name: 'deep-research',

  description:
    'Answer a complex query end-to-end: quick-search the topic, plan parallel subtopics, research each subtopic with agent-managed web search+verification, draft, editor-review+revise, then return a final report.',

  whenToUse:
    'A complex, open-ended, or up-to-date question that should end in a synthesized research report. Pass args.query. Optional: language, maxSubtopics, maxRevisions, reportStyle.',

  // 提前告知有哪些阶段
  phases: [
    { title: 'Quick Search' },
    { title: 'Plan' },
    { title: 'Research' },
    { title: 'Draft' },
    { title: 'Review' },
    { title: 'Finalize' },
  ],
}

// 获取用户的原始问题
const query = args.query

// `phase` 和 `log` 用于即时反馈当前阶段
phase('Quick Search', '快速理解用户问题和主题')
log('开始 Quick Search')

const quick = await agent(`
  你是 DeerFlow Deep Research 的快速搜索员。
  用户问题：${query}
  请用 webSearch 完成一次 Quick Search，输出用户真正想问什么、
  关键实体、核心争议点、后续适合深入的方向。
`)

phase('Planning', '生成可并行研究的子课题')

const plan = await agent(`
  你是 DeerFlow 研究规划者。
  用户问题：${query}
  Quick Search：${quick}
  请生成 4-6 个可并行研究的子课题，每个含 title / goal / searchHint。
`)

phase('Parallel Research', '并行执行子课题研究')

const tasks = []
for (const item of plan) {
  log(`启动子课题研究：${item.title}`)
  tasks.push(agent(`
    你是 DeerFlow 子课题研究员。
    用户原始问题：${query}
    子课题：${item.title}／目标：${item.goal}／搜索提示：${item.searchHint}
    请用 webSearch 完成深度研究。你可以在内部多轮搜索、反思和修正，
    直到结果足够好。输出核心结论、关键事实、证据来源、不同观点、不确定性。
  `, `
    判断子课题研究是否合格：回答了目标、有清晰结论、有关键事实、
    有证据来源、标出了不确定性、可用于最终报告。
  `))
}

const results = await Promise.all(tasks)

phase('Drafting', '整合研究结果生成初稿')

let report = await agent(`
  你是 DeerFlow 报告写作者。
  用户问题：${query}
  子课题成果：${JSON.stringify(results)}
  请写一份中文报告：先给结论，再展开分析，合并重复，保留重要证据，标注不确定性。
`, `
  判断初稿是否合格：回答了问题、结构清晰、结论明确、
  子课题被有效整合、没有明显重复、保留重要不确定性。
`)

phase('Review', '编辑审稿并修改')

let revision = 0
while (revision < 3) {
  const review = await agent(`
    你是 DeerFlow 派来的严格编辑。
    用户问题：${query}／当前报告：${report}
    请审稿。没问题就输出 no issues；有问题就给具体修改意见。
  `)
  log(`第 ${revision + 1} 轮审稿：${review}`)

  const needsRevision = await assert(`
    判断这份编辑意见是否包含实质性修改要求。
    no issues 返回 false，含具体意见返回 true。
    编辑意见：${review}
  `)
  if (!needsRevision) break

  report = await agent(`
    你是报告改写者。
    用户问题：${query}／当前报告：${report}／编辑意见：${review}
    请输出完整新版报告。
  `, `
    判断修改后是否合格：已处理意见、没引入新问题、
    结构更清晰、可进入下一轮审稿。
  `)
  revision++
}

phase('Final Validation', '验证最终报告')

const passed = await assert(`
  判断最终报告是否可交付：回答了问题、结构清晰、结论明确、
  关键事实有依据、不确定性表达清楚、没有明显遗漏。
  最终报告：${report}
`)

if (!passed) throw new Error('报告未通过最终验证')

log('Deep Research completed')
return { plan, report }
```

## agent() 的两个参数

读这段脚本，最值得停下来看的是 `agent()` 的签名：`agent(taskPrompt, verificationPrompt?)`。

第一个参数是任务 prompt，告诉这次调用要干什么。

第二个可选参数 `verificationPrompt` 才是精妙所在，**也是 DeerFlow 3.0 独有的**——它是这次调用的“准出门”，包含用自然语言描述的验证（Rubrics）。`agent()` 内部并不是搜一次就交差：它可以多轮搜索、反思、自我修正，每产出一版结果，就拿 `verificationPrompt` 这把尺子把关，没过就接着改，直到通过这道门，才把结果返回给脚本。

这带来一个很干净的结果：**worker 的“重试”不写在脚本层，而是被内化进了 `agent()` 自身**。你在外层看不到任何 `for (retry...)` 的样板代码，因为“反复尝试直到合格”这件事，已经被那道门吞进调用内部了。脚本只管编排阶段，每个 `agent()` 自己保证交出来的东西达标。

<callout emoji="🎁">
**你知道吗——LLM-as-a-Judge？**
`verificationPrompt` 和 `assert()` 干的是同一件事：用一个 LLM 去判断另一个 LLM 的输出是否合格。这种“让模型当裁判”的做法在社区里叫 LLM-as-a-Judge。它的价值在于，给本来非确定的生成套上一道可编排的准出门——生成是发散的，判定是收敛的，两者一配，loop 才有了“过没过”这个清晰的二值信号。
</callout>

## 哪些是代码，哪些是模型

把这段脚本拆开看，会发现它泾渭分明地分成两类东西。

**一类是确定性的代码**。阶段的先后顺序（Quick Search 一定在 Planning 前面）、`Promise.all` 把子课题一次性铺开并行、`while (revision < 3)` 控制审改最多三轮、`if (!needsRevision) break` 的分支、最后的 `return report`——这些都是普通 JS 控制流，跑一百遍是同一个走法，不依赖模型的临场发挥。

**另一类是 LLM 真正发挥的地方**，全文只有两种调用：`agent()` 和 `assert()`。前者负责干活——搜索、规划、写作、改写；后者负责判断——这版报告该不该回炉、终稿能不能交付。除此之外，模型不掺和流程控制。

这恰好就是 Orchestration 的形态：**骨架是代码，血肉是模型**。代码保证流程不丢步、不跑偏、可重放；模型在被显式调用的那几个点上贡献智能。两边各管一段，谁也不越界。

还有两个不起眼但有用的调用：`phase()` 给每个阶段打标，`log()` 记细粒度日志。它们不参与逻辑，纯粹是为了让用户实时知道这条 loop 此刻跑到哪了、在干什么。一个在后台默默跑的长任务，如果不向外吐进度，对用户就是个黑箱；`phase` 和 `log` 就是把黑箱凿开的那两个窗口。



---



# Workflow 的解剖

上一章那段深度研究脚本是个具体例子。把它的各个零件拆开，会发现它们其实是一套可以复用的通用结构。一个成熟的 Dynamic Workflow，大致由八个部件构成。下面逐一过一遍，每讲一个，都对应回深度研究里它具体是哪一段。

| **Trigger（触发）** | 什么把这条 loop 启动了。可以是定时（每天早上跑一遍行业简报）、事件（收到一封邮件就触发归档）、或者手动（用户点一下“开始研究”）。深度研究的例子里，Trigger 就是用户抛出 `query` 那一刻。它不在脚本主体里，但它决定了脚本何时被唤醒。 |
|-|-|
| **Planner（规划器）** | ：把一个大任务拆成可以分头处理的子任务。对应深度研究里的 `Planning` 阶段——那个 `agent()` 调用读完 Quick Search，吐出 4-6 个带 `title` / `goal` / `searchHint` 的子课题。没有这一步，后面的并行就无从谈起。 |
| **State（状态）** | loop 跑到一半攒下来的东西，活在脚本的变量和外部存储里，而不是某一次对话的上下文窗口里。`quick`、`plan`、`results`、`report`、`revision`——这些变量就是这条 loop 的 State。把状态外部化是关键一笔：它不依赖单次对话，于是 loop 可以停、可以续、可以被另一个进程读取。 |
| **Workers（干活的）** | 真正出力的 `agent()` 调用。深度研究里，那一组并行的子课题研究员就是 Workers，每个 worker 领一个子课题，自己去搜、去整理、去交差。它们是这条 loop 的体力担当。 |
| **Evaluator（验收）** | 把关的环节，这里有两层。第一层是每个 `agent()` 自带的 `verificationPrompt`，也就是前面说的那道“准出门”，把单次调用的重试内化掉，worker 不达标就不许返回。第二层是独立的 `assert()`——它站在阶段与阶段之间，是更高一级的闸门，比如审稿后判断“该不该回炉”、终验时判断“能不能交付”。一层管单次调用的质量，一层管阶段流转的去留。 |
| **Loop / Branch（循环与分支）** | `while (revision < 3)` 的审改循环，和 `if (!needsRevision) break` 的条件分支。这正是“loop”这个词最字面的来源——流程不是一条直线走到底，而是会在某些点上绕回去、或者岔开。深度研究的回炉重写，就发生在这里。 |
| **Stop / Resume（停下与续跑）** | 能在中途停下，也能从断点接着跑。这是长任务的命脉。一条要跑半小时、调几十次模型的 loop，如果中间断了只能从头再来，那基本没法用。因为 State 已经外部化，停在哪一步、攒了哪些中间结果都记录在案，于是 Resume 才成为可能。 |
| **Repeatability（可重复）** | 同一份脚本，可以重复地、可审计地跑出可比的结果。流程钉在代码里，每次走的都是同一条路径，差异只来自 `agent()` 那几个调用点。这让 loop 既能复盘，又能比较——换个模型再跑一遍、改个 prompt 再跑一遍，结果是可对照的。 |

把这八个部件串成一张状态机，大概是这个样子：

![](https://feishu.cn/file/DmjNbNfDvoa4Aox1CyZcTtHKnBc)

> **注意：**这里只是举了一个例子，Dynamic Workflow 的灵魂是“Dynamic”，即动态灵活。



图里特意把 `Stop/Resume` 画成一个能回到 Workers 的状态：loop 可以在干活途中暂停，记下当下的 State，之后从断点处续跑，而不是推倒重来。这条“能回去”的边，是长任务能用起来的前提。

值得一提的是，这八个部件并非每条 workflow 都得集齐。简单的 loop 可能没有 Branch、也用不上 Resume；但 Trigger、Workers、Evaluator 这几样几乎是标配。把它们当成一张检查表，设计自己的 loop 时挨个问一遍“这一项我有没有想清楚”，往往就能少踩几个坑。

<callout emoji="🔂">
**你知道吗——Repeatability 与确定性重放（deterministic replay）？**
Dynamic Workflow 的可复现，本质是把 LLM 的非确定性全部收敛到了 `agent()` 这几个调用点上。骨架是确定的代码，发散只发生在被显式标记的地方，于是整条 loop 可以被审计、被复现——你能精确指出“不一样”是从哪一次调用开始的。这种“确定性重放”正是纯 Skill 范式难以保证的：Skill 的执行路径每次都由模型即兴决定，连“走了哪几步”都未必能复盘。
</callout>



---



# 让人留在 Loop 里

一个 loop 一旦跑起来，最省心的设想是：它自己埋头跑完，最后把结果端上来。但稍微长一点的任务，这个设想都很危险——它意味着无人值守的 loop，也在无人值守地犯错。自动化不等于失控，真正可用的 workflow，得让人能随时看见它、也随时插得进手。

需要先说明一下，下面提到的 `askUserQuestion()` 与 `drainInbox()` 都是 DeerFlow 3.0 计划里的形式，还会随实现调整，这里更多是想把“人怎么留在 loop 里”这件事讲清楚。

把人留在 loop 里，笔者觉得可以拆成两个方向。

**第一个方向是 workflow 主动找人**。脚本跑到关键岔路时，与其替用户做主，不如停下来问一句。`askUserQuestion()` 就是干这个的——比如深度研究到了规划阶段，几个子课题的取舍方向不明，或者视频生成里角色设定有两版风格难以定夺，workflow 可以在这里挂起，把选项摆给用户，等到答复再往下走。这就是典型的 Human-in-the-loop：人不是事后验收，而是在 loop 内部的决策点上被请进来。

**第二个方向是用户主动介入**。有些循环一跑就是十几分钟，用户中途想纠个偏，总不能等它跑完。办法是让脚本在循环里时不时调一次 `drainInbox()`，拉一下用户发来的 steering 消息——如果有，就把这条新指令并进当前上下文，及时调整；如果没有，就接着跑。这样用户不必盯着，但只要想说话，loop 在下一个检查点就能听见。

这两个方向，配合前面提到的 `phase()` / `log()` 实时上报，才算完整：`phase()` / `log()` 让用户**看得见**进度，`askUserQuestion()` / `drainInbox()` 让用户**插得上**手。看得见又插得上，loop 才不是个黑箱。

下面这张时序图把三方的配合画了出来——workflow 跑到关键点用 `askUserQuestion` 等用户答复，循环里则用 `drainInbox` 顺手拉取用户的 steering 消息。

<whiteboard token="NsEBwFEIPhuNVCbNjV8cGXAYn9c"></whiteboard>

`askUserQuestion()` 和 `drainInbox()` 看着只是 DeerFlow 3.0 规划两个 API，不是 Claude Code Beta 自带的，背后其实是同一个判断：loop 越自动，越要给人留好介入的接口。把这两个接口设计在哪、什么时候触发，往往比 loop 本身的逻辑更值得琢磨。



---



# 再看一个例子：视频生成

上一章把通用结构拆成了八个部件，但要验证它是不是真的通用，最好换个完全不同的任务试一遍。深度研究偏“文本”，容易让人觉得 Workflow 只适合研究类场景；那就换成生成一段视频，看看同样的模式搬过去还成不成立。

把“做一段视频”摊开，其实是一条很清楚的流水线：文字脚本 → 角色设计 → 分镜头 → 生成画面 → 配音 → 剪辑 → 字幕。七个阶段，每一段都有明确的输入输出，也都有“做得好不好”的判断标准。这恰好是 Workflow 最舒服的形状。

![](https://feishu.cn/file/LqL3bg9IkoV398xYgZjcFJDVneh)

图里画面与配音之所以分成两条线，是因为它们可以并行——分镜头一旦定下来，每个镜头的画面互不依赖，配音也不必等画面，统统可以一起跑。

落到脚本上，分工和深度研究里是一样的：每个阶段用 `phase()` 标记，方便用户实时知道进行到哪；创意判断（写脚本、定角色、排分镜）交给 `agent()`，让模型发挥；质量闸门交给 `assert()` 兜底，不合格就不放行；画面和配音这类能并行的生成，交给 `Promise.all` 一起跑。下面是这条 workflow 的一段伪代码，省去了细节只留骨架。

```JavaScript
// 以下代码由 DeerFlow 3.0 workflow-creator Skill 按"深度研究"任务生成
// 部分和 Claude Code 的 API 略微有所不同

export const meta = {
  name: 'make-short-video',

  description:
    'Create a short video end-to-end: write a script from a theme, design the main character, split the script into storyboard shots, generate frames and voiceover in parallel, edit them into a video, then validate sync and pacing.',

  whenToUse:
    'A user wants to turn a theme or idea into a short video, ad, reel, TikTok-style clip, concept video, or storyboarded video asset. Pass args.theme. Optional: duration, style, language, aspectRatio, voiceStyle.',

  phases: [
    { title: 'Script' },
    { title: 'Character' },
    { title: 'Storyboard' },
    { title: 'Generate' },
    { title: 'Edit' },
    { title: 'Validate' },
  ],
}

// ───────────────────────── args / defaults ─────────────────────────
const a = args || {}
const THEME = a.theme

if (!THEME) {
  throw new Error('make-short-video requires args.theme.')
}

const DURATION = a.duration || '30 seconds'
const STYLE = a.style || 'cinematic, polished, social-video friendly'
const LANGUAGE = a.language || 'zh-CN'
const ASPECT_RATIO = a.aspectRatio || '9:16'
const VOICE_STYLE = a.voiceStyle || 'natural, clear, emotionally engaging'

// ───────────────────────── Phase 0: Script ─────────────────────────
phase('Script', '写文字脚本')

const script = await agent(
  `你是短视频脚本作者。

主题：
${THEME}

请根据主题写一段 ${DURATION} 短视频脚本。

要求：
1. 适合 ${ASPECT_RATIO} 短视频。
2. 有开头钩子、中段展开、结尾收束。
3. 画面感强，适合后续拆分镜头。
4. 语言自然，不要像广告硬广。
5. 输出语言：${LANGUAGE}

整体风格：
${STYLE}`,
  `判断脚本是否合格：

1. 符合主题。
2. 适合 ${DURATION} 短视频。
3. 有明确开头、中段和结尾。
4. 有画面感。
5. 可以继续进入角色设计和分镜阶段。`
)

log('Script completed')

// ───────────────────────── Phase 1: Character ─────────────────────────
phase('Character', '设计角色')

const character = await agent(
  `你是角色设计师。

短视频脚本：
${script}

请为脚本设计主要角色的外观与气质。

要求：
1. 角色要服务脚本主题。
2. 描述外观、年龄感、服装、气质、表情、动作习惯。
3. 给出可用于画面生成的一致性描述。
4. 不要设计过多角色，优先保证主角稳定。
5. 输出语言：${LANGUAGE}

整体风格：
${STYLE}`,
  `判断角色设计是否合格：

1. 与脚本主题一致。
2. 角色外观清晰。
3. 气质明确。
4. 可以作为后续画面生成的稳定参考。
5. 没有与脚本冲突。`
)

log('Character completed')

// ───────────────────────── Phase 2: Storyboard ─────────────────────────
phase('Storyboard', '拆分镜头')

const shots = await agent(
  `你是分镜导演。

短视频脚本：
${script}

角色设定：
${character}

请把脚本拆成分镜头。

每个镜头包含：
- id
- duration
- desc
- camera
- action
- mood

要求：
1. 总时长接近 ${DURATION}。
2. 每个镜头都要有明确画面描述。
3. 镜头之间节奏自然。
4. 适合 ${ASPECT_RATIO} 视频。
5. 输出 JSON 数组。
6. 输出语言：${LANGUAGE}`,
  `判断分镜是否合格：

1. 是数组。
2. 每个镜头都有 desc。
3. 总体能覆盖完整脚本。
4. 镜头节奏适合 ${DURATION}。
5. 可以用于并行生成画面。`
)

log(`Storyboard: ${shots?.length ?? 0} shot(s)`)

// ───────────────────────── Phase 3: Generate ─────────────────────────
phase('Generate', '并行生成画面与配音')

const frameTasks = []

for (const shot of shots) {
  log(`生成画面：${shot.id || shot.desc}`)

  frameTasks.push(
    agent(
      `你是短视频画面生成 Agent。

分镜：
${JSON.stringify(shot, null, 2)}

角色参考：
${character}

整体风格：
${STYLE}

画幅：
${ASPECT_RATIO}

请生成该镜头的画面资产或画面生成结果。

要求：
1. 保持角色一致。
2. 符合分镜描述。
3. 构图适合 ${ASPECT_RATIO}。
4. 画面情绪符合脚本。
5. 返回可用于后续剪辑的 frame 结果。`,
      `判断画面结果是否合格：

1. 符合该镜头分镜。
2. 角色一致。
3. 构图清晰。
4. 风格一致。
5. 可以进入剪辑。`
    )
  )
}

const [frames, voice] = await Promise.all([
  Promise.all(frameTasks),
  agent(
    `你是短视频配音 Agent。

脚本：
${script}

请为脚本生成配音。

要求：
1. 时长接近 ${DURATION}。
2. 语气：${VOICE_STYLE}。
3. 语言：${LANGUAGE}。
4. 适合短视频节奏。
5. 返回可用于剪辑的 voice 结果。`,
    `判断配音是否合格：

1. 覆盖完整脚本。
2. 时长接近 ${DURATION}。
3. 语气自然。
4. 节奏适合短视频。
5. 可以与画面剪辑同步。`
  ),
])

log(`Generate completed: ${frames.length} frame(s) + voice`)

// ───────────────────────── Phase 4: Edit ─────────────────────────
phase('Edit', '剪辑与字幕')

const video = await agent(
  `你是短视频剪辑 Agent。

请把画面与配音剪成成片。

素材：
${JSON.stringify({ frames, voice }, null, 2)}

脚本：
${script}

分镜：
${JSON.stringify(shots, null, 2)}

要求：
1. 画面和配音节奏对齐。
2. 根据脚本添加字幕。
3. 保持 ${ASPECT_RATIO}。
4. 节奏适合 ${DURATION} 短视频。
5. 输出最终 video 结果。`,
  `判断剪辑结果是否合格：

1. 画面顺序符合分镜。
2. 配音和画面对齐。
3. 字幕可读。
4. 节奏自然。
5. 成片可以交付。`
)

log('Edit completed')

// ───────────────────────── Phase 5: Validate ─────────────────────────
phase('Validate', '质量校验')

const passed = await assert(
  `判断成片是否通过质量校验：

1. 节奏是否自然。
2. 画面与配音是否对得上。
3. 字幕是否清晰。
4. 角色是否一致。
5. 是否完整表达主题。
6. 是否适合 ${ASPECT_RATIO} 短视频。

成片：
${video}`
)

if (!passed) {
  throw new Error('make-short-video final video did not pass validation.')
}

log('Short video completed')

return {
  theme: THEME,
  duration: DURATION,
  style: STYLE,
  language: LANGUAGE,
  aspectRatio: ASPECT_RATIO,
  voiceStyle: VOICE_STYLE,
  script,
  character,
  shots,
  frames,
  voice,
  video,
}
```

换个领域，结论几乎没变：只要一个复杂任务有明确的阶段、有可验收的标准，它就可以、也大概应该被组织成一个 loop。这大概就是笔者一直想说的那句话——几乎每个代码场景都值得有一个 loop。不是说什么都得套上 Workflow，而是当你发现自己在反复手动串联这些阶段时，把它编译成一段脚本，往往比每次重新 prompt 更省心、也更稳。



---



# 总结

绕了一大圈，这篇文章想讲的其实是同一件事：重心的转移。早期的 ReAct 让 LLM 自己充当那个 loop——reason、act、observe 不断自循环，整条流程藏在模型每一轮推理里，再配一份 Skill 当说明书。它的灵活无可替代，但代价是把全部重量都压在运行时的 Instruction Following 上：每一步都得指望模型当场把 Skill 读懂、不跑偏、不丢步骤，于是它不稳、难复盘、也难审计，而且往往只有最强的那几个模型才勉强扛得住。Orchestration 走的是另一条路：先用旗舰模型把流程一次性“编译”成一段 Workflow Script，把确定性交给代码，把判断力留给被代码显式调用的 LLM。Loop Engineering 就是这次转移的名字——你不再亲手 prompt agent，而是去设计那个让 agent 被 prompt 的 loop；Dynamic Workflow，则是把单个 loop 落成代码的那种具体形态。

为了把这件事讲透，前面我们先分清了 Skill 与 Workflow 的分野——一个把结构交给模型即兴发挥，一个把结构钉死在代码里；再用一段“深度研究”的脚本把抽象落到地上，看清楚哪些是机械的确定性代码、哪些才是 `agent()` 与 `assert()` 真正调用模型的地方；接着把一个成熟的 loop 解剖成 Trigger、Planner、State、Workers、Evaluator、Loop/Branch、Stop/Resume、Repeatability 八个部件；又聊了怎么用 `askUserQuestion()` 和 `drainInbox()` 把人留在 loop 里，让它不至于无人值守地一路错下去；最后换了一个视频生成的例子，说明这套模式并不只服务于研究类任务——几乎每一个有明确阶段、有验收标准的复杂任务，都能被组织成一个 loop。

把流程编译成 Workflow Script，换来的是一整笔划算的交易。流程被钉在代码里，**稳定性**有了着落；脚本可改、可存档、可复用，**灵活性**和**可复用性**并没有因此丢掉；`phase()` 与 `log()` 让每一步都看得见，**可观测性**也在。更关键的是，结构既已固化进代码，运行时就不再需要模型靠强 Instruction Following 去维持流程——于是 orchestration agent 和它派出去的各个 sub-agent，都能落到便宜、够用的普通模型上。旗舰模型生成一次，普通模型执行多次，**成本**也跟着压了下来。这也是为什么笔者愿意把它单独拎出来讲：它不是用代码取代模型，而是用代码编排模型，让稳定和智能这两样东西第一次有机会一起握在手里。

所以 Skill 与 Workflow 从来不是谁取代谁，而是各管一段的分工：这一段的结构该交给模型即兴发挥，还是交给代码钉死，取决于你更需要灵活还是更需要稳定。多数真实场景里，两者是搭配着用的，而不是二选一。

也得诚实地交代边界。loop 把执行的确定性收住了，但**验证这件事仍然在人手里**——`assert()` 写得松，loop 照样会安静地错下去，而且错得很有条理、很难一眼看穿。它也不是万能的：面对一次性的、边界还很模糊的探索性任务，开一段对话、写一个 Skill 反而更轻。还要再说一遍，本文用来举例的这些 API 是 DeerFlow 3.0 的计划形式，远未定稿，笔者更想借它把“一个 loop 到底由什么构成”讲明白，而不是交一份接口规范出来。

往前看一步：当 loop 不再只是被人写出来，而是能被 Agent 自己读懂、自己改写时，Loop Engineering 就会和我们之前聊过的 Harness 自我进化合流——那会是另一个值得单独展开的话题。我们打算沿着这个方向，把更多 DeerFlow 3.0 的能力组织成可重放的 loop；也很想听听，在你自己的场景里，会怎么去设计这些 loop。





<grid><column width-ratio="0.500000"><p><b>加入 Agentara 2 群：</b></p><chat_card name="📯 Agentara Underground 情报站（2群）" chat-id="oc_87790dff43e23d2205d78baa8bff4f38"></chat_card></column><column width-ratio="0.500000"><p><b>加入 Agentara Undergound 情报站</b></p><p>加群获取更多线上资料，和 9,500+ 位 AI 爱好者一起学习 Prompt、Context Engineering、Harness Engineering 和 Skills。</p><blockquote><p><b>已经加入过 1 群的小伙伴</b>不用重复加入，也请分享给需要的同学们</p></blockquote></column></grid>



<synced_reference src-block-id="Al7fdhQBqssP3Fb7uNkczV3Cnse" src-token="DvmPdngkMoGkjexZbBgcuFfQnrO"></synced_reference>
