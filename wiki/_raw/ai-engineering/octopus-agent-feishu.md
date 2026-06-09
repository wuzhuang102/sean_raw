source: https://my.feishu.cn/docx/L6kmdHxPAoJi90x0UWucCnvKnEh
fetched: 2026-06-09
format: markdown

# 章鱼给 AI Agent 的一课：真正的智能，不只住在“大脑”里

<callout emoji="🤔">
章鱼最迷人的地方，不是它像人一样聪明，而是它聪明得很不像人。
它提醒我们：智能不一定只待在一个中央大脑里，也可能长在手臂、吸盘、动作和环境反馈之间。
</callout>

把一只章鱼放进陌生水箱，它不会先停下来做一份完整计划。

它会先伸出一条腕摸一摸，另一条腕绕到旁边试探缝隙；吸盘贴上石头，像舌头一样“尝”表面的化学味道。哪里不对，腕会马上调整，不需要中央脑替每个吸盘写动作指令。

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=M2IwMDU2ZGEyYmMwM2JlMjYxMTMzY2Y2N2NiZjY1ZTNfNDMzMTI5OGQ5ZmIyM2NmMDU5NTgwMzg0Y2QzYWNlNmZfSUQ6NzY0ODg1ODM0NjYwMzIyMDE2MV8xNzgwOTc0MjQ0OjE3ODA5Nzc4NDRfVjM)

这和我们平时理解“智能”的方式很不一样。

我们很容易把智能想象成一个指挥中心：大脑负责理解、计划、下命令，身体只负责执行。做 AI Agent 时，我们也常常沿用这个想象：中间放一个强大的 LLM，外面挂搜索、浏览器、代码、数据库、文档等工具。模型思考，工具执行。

章鱼给了另一种答案：智能可以分散在身体里；越靠近世界的地方，越应该有一点自己的判断。

它不是一个大脑拖着八条被动的绳子，更像一支在海底协作的小队：中央脑负责目标、学习和仲裁；视叶处理复杂视觉；八条腕贴近环境，自己感知、自己探索、自己修正动作；每个吸盘既能抓取，也能感知。

把这个视角放到 AI Agent 上，启发很直接：

<callout emoji="🔥">
未来真正强大的 Agent，不应该只是“一个更聪明的大脑调用一堆工具”，而应该是“一个中央目标系统，协调一组贴近环境、能局部判断、带着 Skill 运行的执行器”。
</callout>

---

## TLDR：章鱼给 Agent 的三句提醒

如果只用三句话概括，我会这样说：

1. **LLM 不该被迫微操一切。** 它更适合做目标理解、策略选择和冲突仲裁。
2. **工具层应该有触觉。** 好工具不只返回结果，还要返回状态、异常、置信度和下一步线索。
3. **真正的 Agent 需要“身体”。** 也就是能持续行动、局部校验、失败重试、沉淀经验的 Skill 系统。

这里补一句，避免误会：Skill 本身通常不是一条会自己行动的触手。它更像腕里的动作程序或能力包；真正像章鱼腕的，是被中央 Agent 唤起后，能带着 Skill、工具和反馈继续往前推进的半自主执行器。

---

## 一、章鱼不是“九个脑子”，而是一套分层分布式系统

很多人会说章鱼有“九个脑子”。这个说法好记，也很有传播性，但它容易把重点带偏。

更准确地说，章鱼有一个复杂的中央神经系统，同时也把大量神经计算放进了腕部。2015 年发表在 Nature 的章鱼基因组研究指出，章鱼拥有无脊椎动物中极其庞大的神经系统，神经元数量接近 5 亿，其中相当大一部分分布在腕部神经系统中。[Octopus genome and the evolution of cephalopod neural and morphological novelties](https://www.nature.com/articles/nature14668)

这不是一个冷知识，而是理解章鱼智能的关键。

如果神经元大多集中在头部，身体就更像被动执行器。可一旦大量神经元进入腕、吸盘和局部神经环路，身体就不只是“被控制”的东西，它本身也开始参与计算。

章鱼的每条腕中都有贯穿全长的轴神经索。2025 年 Nature Communications 的研究进一步发现，章鱼腕部轴神经索存在分段式组织；在 Octopus bimaculoides 中，研究者观察到每个吸盘大约对应 7.5 个神经段，并且这些神经段与吸盘和腕部肌肉控制关系紧密。[Neuronal segmentation in cephalopod arms](https://www.nature.com/articles/s41467-024-55475-5)

换句话说，章鱼的腕不是一根柔软的机械臂，而是一串带局部计算能力的模块。

<whiteboard token="CD0YwbSoghKyy6bHqkfcfxWRnSg"></whiteboard>

如果把这张图翻译成 Agent 架构，可以这样理解：

中央 LLM 不该被迫读取每一个像素、每一个 DOM 节点、每一次 API 细节和每一行日志。它真正需要的是局部模块处理后的信号：目标是否完成，环境是否变化，哪里异常，是否需要重新规划。

---

## 二、吸盘不是“按钮”，而是靠近世界的传感器

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDM1NTE3NTZjNGFmZmM5YmY1YjkyOWNhNzM4NDQzOTdfNjY2ODNjNTFjYTNjMWJjYjlmMTYzMDUyODJlMDRmYjNfSUQ6NzY0ODg1ODM2MjUyNTA2MDMyMF8xNzgwOTc0MjQ0OjE3ODA5Nzc4NDRfVjM)

章鱼的吸盘很适合拿来理解 Agent 的工具层。

我们通常把吸盘想象成“抓东西”的部件。但对章鱼来说，吸盘不只是抓手，也是传感器。2020 年 Cell 的研究发现，章鱼腕部存在特化的 **chemotactile receptors(趋化触受体)**，能够检测接触表面的化学信息，让章鱼通过触摸来“品尝”环境。[Molecular basis of chemotactile sensation in octopus](https://www.cell.com/cell/fulltext/S0092-8674(20)31149-1)

这件事放到 Agent 里，很有启发。

章鱼不是先把所有原始信息上传给中央脑，再由中央脑决定每个吸盘怎么反应。吸盘和腕部神经环路就在最靠近世界的位置，很多初步判断可以在本地完成。

今天很多 Agent 系统的问题，正好反过来。

我们把工具做成裸 API，然后让 LLM 自己判断一切：返回值对不对？网页有没有加载完？命令失败能不能重试？空结果是正常没数据，还是查询条件写错了？文件是不是真的写成功？权限错误应该换路径，还是请求授权？

这有点像让章鱼的中央脑亲自解释每个吸盘碰到的每一点泥沙。

更好的方式，是让工具层先有一点“触觉”。

<whiteboard token="NsHKwAjaihMvk0bZyTjc4Wk4nub"></whiteboard>

一个章鱼式工具适配器，不应该只把原始结果扔回给 LLM。它应该先做一层本地判断：输入是否合法，权限够不够，调用是否成功，空结果到底是“确实没有数据”，还是“查询条件可能错了”。

它还应该知道哪些失败值得重试，哪些操作有副作用，哪些结果可以直接交给下一步，哪些必须先让中央 Agent 重新判断。

这些听起来不大，但会决定 Agent 是在清楚的反馈里行动，还是在一团噪声里猜。

很多时候，Agent 失败不是因为中央模型不够聪明，而是因为它被迫在低质量反馈里工作。

---

## 三、章鱼腕会“自己做动作”

章鱼腕的运动控制，是这篇文章里最容易被误解、也最有价值的一点。

经典 Science 论文《Control of octopus arm extension by a peripheral motor program》发现，章鱼腕部可以包含外围运动程序。研究者通过实验说明，伸腕这类动作并不完全依赖中央脑逐步计算每个细节，而可以由腕部局部神经系统承载一部分运动程序。[Science 2001, DOI 10.1126/science.1060976](https://www.science.org/doi/10.1126/science.1060976)

这和很多今天的 Agent 设计形成了鲜明对比。

很多 LLM Agent 仍然像一个过度操心的经理：

1. 看网页。
2. 决定点哪个按钮。
3. 看返回结果。
4. 决定是否滚动。
5. 再看页面。
6. 再决定复制哪段文字。
7. 再判断是否完成。

每一步都回到中央模型。这个模式当然灵活，但代价也很高：慢、贵、上下文膨胀、容易丢目标，也容易在长任务里被低层噪声拖垮。

章鱼式 Agent 更应该把连续动作交给“**带 Skill 的半自主执行器**”。

Skill 本身通常不是会自己行动的东西；真正像腕的，是被中央 Agent 唤起后，能使用 Skill、调用工具、观察反馈、继续推进的小闭环。

<whiteboard token="SOwPwunkqhe7ghbmImScZ9NqnMc"></whiteboard>

把中央Agent从低层微操里解放出来，让它专心做更有价值的事：理解用户真正要什么，识别约束和风险，选择策略，解释权衡，决定什么时候停止。

比如浏览网页，中央模型不必决定每一次滚动和点击。更好的做法是让浏览执行器在被调用后自己搜索、过滤、抽取、截图；只有目标变化、页面异常或需要判断时，才把问题交回中央。

比如写代码，中央模型不必反复猜格式错误和测试失败。代码执行器可以根据 Skill 流程修改、格式化、运行测试、定位日志，再把“我改了什么、测试是否通过、失败卡在哪里”交回中央。

比如做研究，中央模型也不必逐条读搜索结果。研究执行器可以先完成多源检索、去重、可信度评分和引用整理，再把真正需要判断的冲突交出来。

所以，一个成熟 Agent 的能力，不只取决于中央模型参数量，也取决于这些“腕部执行器”是否可靠。否则它看起来像 Agent，实际只是一个很忙、很累、很容易分心的聊天框。

---

## 四、中央脑依然重要：它负责目标、学习和仲裁

强调分布式智能，很容易走向另一个误区：以为章鱼就是八条腕各干各的。其实并不是这样。

章鱼有复杂中央脑，也有强大的视觉系统和学习记忆结构。2022 年 Nature Communications 的章鱼脑细胞图谱研究指出，章鱼脑具有高度多样的细胞类型和复杂脑叶组织。[Cell type diversity in a developing octopus brain](https://www.nature.com/articles/s41467-022-35198-1)

章鱼的 vertical lobe 通常被认为与学习和长期记忆密切相关。2023 年 eLife 的连接组研究分析了 Octopus vulgaris vertical lobe 的局部连接结构，认为它为长期记忆获取提供了重要的网络基础，并展示了稀疏表征、前馈网络和可塑性相关位点等机制。[Connectomics of the Octopus vulgaris vertical lobe](https://elifesciences.org/articles/84257)

所以章鱼不是“无中心系统”。更准确地说，它是一个“分层分布式系统”。

中央脑不需要管每个吸盘的微动作，但它要负责更高层的事：

1. **定义目标。** 到底要探索、捕食、躲避，还是打开一个罐子。
2. **整合情境。** 视觉、触觉、化学感知和过去经验如何合并。
3. **仲裁冲突。** 多条腕、多种感知、多种行动倾向如何排序。
4. **巩固经验。** 哪些模式以后可以复用，哪些风险需要避免。

AI Agent 也一样。

中央模型不应该是事事亲自上手的微操者，而应该是目标解释器、策略规划器、冲突仲裁者和经验压缩器。

<whiteboard token="MXkcwmiy1hDuHKbK5gscHdJKnYf"></whiteboard>

在这张图里，中央 Agent 仍然重要，但它不再吞下所有细节。它下达意图、接收摘要、处理例外、做最终判断。

---

## 五、Agent 不缺“大脑”，缺的是“身体”

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NGQwNWNjYzI1YjRkNTU0ZDkyOWEyNmQ2MTE5MWYxNTFfYTgwNWNjNjcwZGYxMzQxODc4Nzg4Mjc1YjhiNjBlNjdfSUQ6NzY0ODg1ODM4MDczMjIzOTA1Ml8xNzgwOTc0MjQ0OjE3ODA5Nzc4NDRfVjM)

过去几年，AI Agent 的主流叙事一直在强化“大脑”：

- 模型更大
- 上下文更长
- 推理更强
- Prompt 更复杂

这些当然重要。但章鱼提醒我们，真实世界里的智能不只来自大脑内部，也来自身体、传感器、反馈环和环境之间的配合。

机器人学里，Rodney Brooks 在《Intelligence without representation》中批评过过度依赖中央表征的路线。他提出的 subsumption architecture 强调，多个行为层可以直接连接感知和动作，而不是所有事情都先构建一个完整世界模型。[Intelligence without representation](https://people.csail.mit.edu/brooks/papers/representation.pdf)

强化学习里，Sutton、Precup 和 Singh 的 options 框架把动作扩展成可以持续执行的高层行为单元，让系统在不同时间尺度上组织行为。[Between MDPs and semi-MDPs](https://www.sciencedirect.com/science/article/pii/S0004370299000521)

LLM Agent 研究也在走向类似方向。ReAct 把推理和行动交替起来，让模型通过外部观察更新思考；Voyager 则展示了技能库的重要性：Agent 可以在 Minecraft 中持续积累可复用代码技能，而不是每次从零开始。[ReAct](https://openreview.net/forum?id=WE_vluYUL-X) [Voyager](https://arxiv.org/abs/2305.16291)

这些方向合在一起，指向一个很朴素的结论：

<callout emoji="❗">
Agent 的下一阶段，不只是让中央模型“想得更久”，而是让系统拥有更好的身体：更可靠的工具适配器、更强的局部反馈、更可复用的 Skill、更清晰的记忆机制。
</callout>

---

## 六、什么是“章鱼式 Agent”

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NzFjZDY5NmU3MzA1MjU0ZjIwNWMyZDhhNzc3N2NiZWJfYWVkOWMyNmQ0ZDIyMzRiZmNlY2EzYmQ2YmMxMzAxZDRfSUQ6NzY0ODg2NzE0MzQ0Mjc3OTA5Nl8xNzgwOTc0MjQ0OjE3ODA5Nzc4NDRfVjM)

中央 Agent 像中央脑，负责理解目标、判断优先级、处理冲突。它不应该盯着每一次点击，也不应该亲自解释每一次 API 报错。

记忆系统像 vertical lobe，负责把经验留下来。哪些用户偏好是稳定的，哪些流程已经跑通过，哪些失败模式以后要避开，都不应该每次从零开始。

带着 Skill 运行的半自主执行器像腕。浏览、写代码、查资料、做数据、写文档，这些都不该只是“一次工具调用”，而应该是能持续行动的小闭环。严格说，Skill 本身更像腕里的动作程序；它需要 Agent 或 runtime 调用后，才会真正动起来。

工具适配器像吸盘。它们贴着世界，最先知道页面有没有加载、命令有没有失败、数据是不是空、权限是不是不够。

最后还需要腕间协调：共享状态、资源锁、安全边界、任务优先级。没有这一层，多条腕会互相打架；没有这一层，多 Agent 也很容易变成一群互相打断的聊天窗口。

当这些边界清楚了，Agent 才会从一个长上下文聊天循环，变成一个真正能工作的系统。

---

## 结语：未来的 Agent，会更像章鱼，而不是更像一个孤独的大脑

![](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=N2MxOGYzZDAyNTMzNGYyYzE4NWZkMDJiMDQ5NjI1ZWJfMWE5YzZjYWFhYTI4NWE2YjRlM2MyZDYwMmQ3N2M1OTNfSUQ6NzY0ODg1ODQwMTY5NDQ2OTM1Nl8xNzgwOTc0MjQ0OjE3ODA5Nzc4NDRfVjM)

我们常常把 AI 的进步想象成“大脑越来越聪明”。

模型更大，推理更强，上下文更长。

但真实世界的智能，从来不只是大脑的胜利。它还来自身体、传感器、反馈环、环境结构、记忆机制和低层动作程序。

章鱼迷人的地方，不是它像人。

恰恰相反，它展示了一种很不像人的智能：中央脑不必知道一切，身体可以承担计算，动作可以携带知识，靠近世界的地方也应该有自己的判断。

对 AI Agent 来说，这可能比“让模型想得更久”还重要。

<callout emoji="🔥">
少一点中央微操，多一点局部闭环；少一点纯文本思考，多一点可执行技能；少一点把世界塞进上下文，多一点让系统在世界里自己校验。
</callout>

真正强大的 Agent，不只是有一个聪明的大脑。

它还应该长出腕、吸盘、神经环和记忆。更准确地说，它需要一套能被中央目标唤起、能在局部行动和校验的身体。

---

## 延伸阅读

1. [Octopus genome and the evolution of cephalopod neural and morphological novelties](https://www.nature.com/articles/nature14668)
2. [Neuronal segmentation in cephalopod arms](https://www.nature.com/articles/s41467-024-55475-5)
3. [Cell type diversity in a developing octopus brain](https://www.nature.com/articles/s41467-022-35198-1)
4. [Molecular basis of chemotactile sensation in octopus](https://www.cell.com/cell/fulltext/S0092-8674(20)31149-1)
5. [Control of octopus arm extension by a peripheral motor program](https://www.science.org/doi/10.1126/science.1060976)
6. [Connectomics of the Octopus vulgaris vertical lobe](https://elifesciences.org/articles/84257)
7. [Intelligence without representation](https://people.csail.mit.edu/brooks/papers/representation.pdf)
8. [Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning](https://www.sciencedirect.com/science/article/pii/S0004370299000521)
9. [ReAct: Synergizing Reasoning and Acting in Language Models](https://openreview.net/forum?id=WE_vluYUL-X)
10. [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)

---

<synced_reference src-block-id="WveCd6kpBssPBwbNeGlcj1gAnzf" src-token="FztOden2SobyNbxc2Dyclsfbnsc"></synced_reference>
