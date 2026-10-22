# 软件行业未来十年：AI会替代哪些工作，行业将走向哪里

**核心结论是任务先变。**以2026年9月13日为基准，未来5—10年，AI最可能带来的是标准化任务自动化、岗位重组和人机协作，而不是整个软件行业消失。重复编码、基础测试和简单维护的替代压力较高；架构、安全、产品判断及工程管理中的执行任务也会减少，但系统权衡、独立验证和结果责任仍很重要。软件需求可能继续扩大，同时，部分企业和初级岗位会承受明显压力。[1]

**阅读重点有三条。**下文先区分任务、岗位、企业环节和行业四个层级，再按短、中、长期解释技术与商业变化。随后比较七个软件生命周期环节和五类岗位，最后结合全球与中国的数据，讨论就业、薪资及不同发展情景。范围以全球软件行业为主，中国市场用于补充和对照。

本节参考文献：
[1] OECD劳动需求分析 <https://www.oecd.org/en/publications/oecd-employment-outlook-2023_08785bba-en/full-report/artificial-intelligence-and-jobs-no-signs-of-slowing-labour-demand-yet_5aebe670.html> 摘录：“Policies to reach full employment may have the added benefit of helping automation technologies translate into higher productivity gains and stronger labour demand, although such a policy goal is not without risks (see Chapter 1). Antitrust regulation can bolster the benefits of AI. One would like to ensure that automation from AI results in large cost s…”

## 一、AI替代风险速查：任务、岗位和行业要分开看

**首先看工作内容。**“会不会被AI替代”不能只按职位名称回答。同样叫开发工程师，维护标准接口、设计交易系统和协调跨部门需求，面临的变化并不相同。更有用的判断单位，是任务是否明确、结果能否独立验证，以及出错后能否低成本恢复。

以下短期指基准日至2029年9月13日，即未来1—3年；中期为2029年9月至2031年9月，即3—5年；长期为2031年9月至2036年9月，即5—10年。

| 分析对象 | 短期：1—3年 | 中期：3—5年 | 长期：5—10年 | 本文判断 |
|---|---|---|---|---|
| 具体任务 | 补全、测试、文档、缺陷修复扩大 | 多步骤任务串联 | 更多窄域端到端执行 | 标准化任务替代压力高 |
| 完整岗位 | 工作内容重新分配 | 团队职级与分工调整 | 部分岗位合并，新岗位形成 | 部分自动化与协作主导 |
| 企业业务环节 | 开发工具与流水线接入AI | 开发、运维及业务流程联动 | 条件性高自主交付 | 执行自动化，责任仍需组织承接 |
| 整个软件行业 | 工具、产品与服务升级 | 产品整合与价值重新分配 | AI原生与传统体系并存 | 行业重构，而非整体退出 |

**任务自主性已在提高。**一项覆盖2020—2025年研究的AI软件工程综述，用L0—L4描述自动化程度。其判断是，L1、L2最常见，L3正在增加；对复杂工业级软件，L4全自动化仍不现实。[2]

| 自主性等级 | 主要含义 | 对软件工作的意义 |
|---|---|---|
| L0 | 没有AI辅助 | 人完成任务 |
| L1 | AI建议，由开发者选择 | 人控制实现过程 |
| L2 | AI在预定义选项中选择 | 受约束的决策自动化 |
| L3 | 简单标准案例部分自动化 | 明确边界内自主执行 |
| L4 | 无需开发者参与的全自动化 | 要求完整处理任务与异常 |

**岗位比任务更复杂。**开发岗位不仅包含写代码，还包含澄清目标、理解旧系统、协调依赖和处理事故。AI完成一个问题单，并不意味着它同时承担了这些职责。OECD因此将自动化、劳动互补和新任务创造视为同时发生的三条渠道。[1]

**企业环节也会重组。**一家公司可以让代理完成大量编码，却增加质量工程、权限管理和运行监控投入。此时，被压缩的是某类执行活动，不是研发职能本身。OpenAI的内部代理优先工程案例，就是工程师从直接编写代码转向设计环境、表达意图和建立反馈回路。[3]

本节参考文献：
[2] AI软件工程综述 <https://arxiv.org/html/2409.18048v3> 摘录：“Section 2 discusses the availability of large code sets on coding platforms that form the basis for training AI using actively applied, operated and maintained code. Section 3 addresses the role of models in SE. Bringing these two sections together, Section 4 discusses the utilisation of AI for SE. This section presents the taxonomy of AI for SE ai4se, which has been developed to f…”
[1] OECD劳动需求分析 <https://www.oecd.org/en/publications/oecd-employment-outlook-2023_08785bba-en/full-report/artificial-intelligence-and-jobs-no-signs-of-slowing-labour-demand-yet_5aebe670.html> 摘录：“Policies to reach full employment may have the added benefit of helping automation technologies translate into higher productivity gains and stronger labour demand, although such a policy goal is not without risks (see Chapter 1). Antitrust regulation can bolster the benefits of AI. One would like to ensure that automation from AI results in large cost savings which can then be pas…”
[3] 代理优先工程案例 <https://openai.com/index/harness-engineering/> 摘录：“Title: Harness engineering: leveraging Codex in an agent-first world Markdown Content: Over the past five months, our team has been running an experiment: building and shipping an internal beta of a software product with 0 lines of manually-written code . The product has internal daily users and external alpha testers. It ships, deploys, breaks, and gets fixed. What’s different is…”

### 四种结果会同时出现

**替代不只有一种形式。**局部任务完全自动化、岗位部分自动化、人机协作和新工作形成，具有不同的经济后果。下面的分类用于解释变化，不代表各类型在行业中已占据某个确定比例。

| 结果类型 | 具体例子 | 生产率机制 | 就业机制 | 薪资与需求 | 技能变化 |
|---|---|---|---|---|---|
| 局部完全替代 | 明确缺陷的修复闭环 | 减少直接执行工时 | 压缩相应任务用工 | 标准执行价格承压 | 转向验收与异常处理 |
| 部分自动化 | 开发者用AI生成接口和测试 | 缩短部分工作步骤 | 岗位保留，任务组合变化 | 收益取决于互补能力 | 理解、调试、集成更重要 |
| 人机协作 | 人定目标，代理执行，人审核 | 发挥双方比较优势 | 提高个人或团队产出 | 判断与责任能力更稀缺 | 验证、协调与领域知识上升 |
| AI催生新工作 | 代理构建、AI质量、模型运营 | 建立新的生产与治理能力 | 产生新增需求 | 新技能可能获得溢价 | 软件、AI与行业能力融合 |

**完全替代发生在边界内。**在结构化仓库中，代理可以复现缺陷、修改代码、运行测试和准备变更。这样的任务闭环已出现于具体案例。将结论扩大到完整岗位或整个行业，则要同时考虑质量、安全、维护和需求扩张。[3]

**新工作不是等量补偿。**代理构建、模型运营和AI测试岗位，与被压缩的基础执行岗位，所需技能、地域和招聘时间可能不同。工信部2026年9月的行业问答明确指出，增量岗位并非存量岗位的简单等量置换；基础工作承压与复合人才短缺可能并存。[4]

**本节的判断是：**先按任务判断自动化，再按责任和协作判断岗位，最后才讨论企业与行业结果。

本节参考文献：
[3] 代理优先工程案例 <https://openai.com/index/harness-engineering/> 摘录：“Title: Harness engineering: leveraging Codex in an agent-first world Markdown Content: Over the past five months, our team has been running an experiment: building and shipping an internal beta of a software product with 0 lines of manually-written code . The product has internal daily users and external alpha testers. It ships, deploys, breaks, and gets fixed. What’s different is that every…”
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“2026年9月11日，工业和信息化部举行《 人工智能+软件 专项行动实施方案》新闻发布会。 工业和信息化部信息技术发展司副司长王威伟、中国软件行业协会副理事长兼秘书长吕卫锋、中国电子信息产业发展研究院副院长朱敏、开放原子开源基金会副秘书长李博出席发布会，介绍 人工智能+软件 专项行动有关情况并回答记者提问。 本次新闻发布会由工业和信息化部新闻发言人、办公厅副主任龚宪主持。 工业和信息化部新闻发言人、办公厅副主任 龚宪：各位记者朋友，大家上午好，欢迎出席由工业和信息化部举办的《 人工智能+软件 专项行动实施方案》新闻发布会。 党中央、国务院高度重视人工智能发展， 十五五 规划纲要强调，要全面实施 人工智能+ 行动，提升基础软件和工业软件等产业水平，打造具有国际竞争力的数字产业集群。 为全力推动软件和信息服务业实现高质量发展，我部研究制定了《 人工智能+软件 专项行动实施方案》。 今…”

## 二、未来1—10年的趋势：从辅助写代码到持续交付结果

**行业的方向是智能化。**变化不只在模型能生成多少代码，还包括软件如何与用户交互、企业如何收费、团队如何组织，以及谁承担上线后的责任。技术能力提高提供可能性，客户价值和工程可靠性决定落地范围。

| 时间窗口 | 技术趋势 | 主要驱动因素 | 交付与组织变化 | 行业影响 |
|---|---|---|---|---|
| 短期：2026—2029年 | 编码代理向测试、需求和运维扩展 | 工具成熟、云与算力投入 | 异步任务、沙盒验证、人工审查 | 重复任务减少，验证工作增加 |
| 中期：2029—2031年 | 代理进入核心流程与企业平台 | 数据治理、系统连接、客户回报 | 更小的AI增强团队、持续运营 | SaaS整合，能力和结果收费扩大 |
| 长期：2031—2036年 | AI原生软件与多代理协作 | 能力进展、成本、可靠性 | 条件性自主交付、人机组织演化 | 产品边界和利润分配重新形成 |

上述方向与德勤2026年软件行业展望、IDC云计算预测，以及中国的软件智能化政策相互呼应。[5][6]

本节参考文献：
[5] 德勤软件行业展望 <https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/software-industry-outlook.html> 摘录：“Gartner® predicts that, forty percent of enterprise applications will be integrated with task-specific AI agents by the end of 2026, up from less than 5% today (2025).4 Because of value captured from the productivity gains from AI agents, it’s projected that t…”
[6] 中国软件专项行动 <https://www.gov.cn/zhengce/zhengceku/202609/P020260911688449695690.pdf> 摘录：“放协同的开源社区建设取得积极进展，孵化5 个以上优质开 到2030 年，人工智能与软件和信息技术服务业融合 发展实现新跃升，关键软件全面实现智能化升级，智能编程、 智能体软件及智能服务等新业态成为产业新增长极，建成若 干具有国际影响力的开源社区和产业集群，推动我国软件和 信息技术服务业抢占全球价值链制高点。 二、推进软件生产变革，加速迈向 智能驱动 （一）优化智能编程工具链条。 编程工具，面向软件开发场景深度优化，提升项目级、全流 推动智能编程工具与代码托管平台、云 服务、开源社区等深度适配集成，完善软件开发部署生…”

### 短期：编码助手变成可以接受任务的代理

**短期变化首先是委派。**过去，开发者主要等待代码补全，或把问题复制到聊天窗口。代理式工具则能接受一个任务，在仓库中读取文件、执行命令、运行测试并提交变更。这里的“智能体”，就是能够结合模型、工具和反馈，自主推进若干步骤的软件系统。

**交付从同步走向异步。**OpenAI在2025年6月更新的Codex研究预览中，描述了独立云端沙盒工作流。代理能够读写仓库，运行测试、代码规范检查和类型检查，任务通常耗时1—30分钟，完成后可以发起代码合并请求，即PR。[7]

**异步不等于无需管理。**开发者可以同时委派多个独立任务，但仍要处理任务之间的冲突。一个接口变更可能影响其他代理正在修改的测试和调用方。协作的重点因此从“逐行协助”转向任务切分、共享约束、结果验收和异常升级。

**产品先叠加再重构。**短期内，许多成熟软件更可能保留原有业务底座，再加入自然语言操作和任务执行能力。IDC判断，未来2—3年企业不会简单用AI替代现有系统，而会要求平台具有AI原生能力，并能支撑代理执行任务。[8]

**客户价值转向少操作。**传统软件要求用户寻找菜单、填写表单和切换系统。代理式产品试图让用户提出目标，再由系统调用功能。客户购买的价值，便从“有多少功能”转向“能否少花时间完成任务”，但数据、权限和审批规则仍需由业务系统承接。

**计费已开始混合。**GitHub展示的Copilot Business订阅价格为每用户每月19美元，同时引入AI credits，1个credit对应0.01美元。其计费说明还规定，自2026年6月1日起，代码审查工作流会消耗GitHub Actions运行分钟数。这显示订阅、推理用量和执行资源正在结合。[9]

**人才压力先落在执行端。**能够按模板完成页面、接口和测试的能力，仍然有用，但其独立稀缺性下降。工程师需要更准确地说明目标，并能判断生成结果是否满足真实需求。工信部将需求理解、架构设计、系统集成、质量安全和多智能体编排列为权重上升的能力。[4]

**短期判断是工具普及。**低风险、可复现、可回滚的任务，会比跨系统、高责任任务更快进入代理执行。若独立验证跟不上生成速度，企业得到的可能只是更多待审查代码。

本节参考文献：
[7] Codex产品说明 <https://openai.com/index/introducing-codex/> 摘录：“7 +The failure was triggered when computing the separability matrix for a 8 +compound model where the right‑hand side of an & operation was itself 9 +another compound model. In that case the implementation treated the nested 10 +model as completely no…”
[8] IDC企业应用分析 <https://www.idc.com/resource-center/blog/ai%E6%AD%A3%E5%9C%A8-%E6%9D%80%E6%AD%BB-saas%EF%BC%9F%E6%88%96%E8%AE%B8%E8%AF%A5%E6%8D%A2%E4%B8%AA%E6%80%9D%E8%B7%AF/> 摘录：“随着生成式AI、大模型及Agent能力持续演进，围绕 AI是否会取代SaaS 的讨论正在快速升温。 基于当前企业采用进度、软件支出变化、AI规模化落地情况以及企业工作方式转型趋势的综合观察，IDC的判断是：AI不会在中短期内取代SaaS，但将推动SaaS进入新一轮结构性重构周期。 企业软件市场未来的主要变化，不是SaaS的消失，而是SaaS从 功能交付工具 向 智能执行平台 演进。 当前，AI与SaaS之间并非替代关系，而更接近于 能力叠加 与 价值重定义 关系。 随着企业客户从模型试点走向业务落…”
[9] Copilot产品与计费 <https://github.com/features/copilot> 摘录：“Launch work from GitHub, track progress across multiple agents, review changes, and merge completed work—all from one desktop workspace built natively on GitHub. Command your craft Your AI accelerator for every workflow, from the editor to the enterpr…”
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“2026年9月11日，工业和信息化部举行《 人工智能+软件 专项行动实施方案》新闻发布会。 工业和信息化部信息技术发展司副司长王威伟、中国软件行业协会副理事长兼秘书长吕卫锋、中国电子信息产业发展研究院副院长朱敏、开放原子开源基金会副秘书长李博出席发布会，介绍 人工智能+软件 专项行动有关情况并回答记者提问。 本次新闻发布会由工业和信息化部新闻发言人、办公厅副主任龚宪主持。 工业和信息化部新闻发言人、办公厅副主任 龚宪：各位记者朋友，大家上午好，欢迎出席由工业和信息化部举办的《 人工智能+软件 专项…”

### 中期：核心流程、商业模式和团队结构一起改变

**中期竞争在业务闭环。**代理要从辅助工具进入企业核心流程，必须连接真实数据和实际操作权限。它不仅要生成建议，还要知道哪些数据可信、哪些操作需要审批，以及失败后如何恢复。深度集成能力因此可能比单次模型表现更重要。

**云平台会承接执行。**IDC在2026年1月的中国市场预测中，预计到2027年，超过85%的中国组织将改造云环境以适配AI工作负载。它还预计，80%的中国500强企业将部署代理式AI平台，用于持续监控、分析和故障修复。这些短期基础设施变化，为中期的流程代理化铺路。[10]

**部署形态不会单一。**同一IDC预测预计，到2028年，60%的中国组织将采用治理控制更强的私有云方案，超过80%采用异构云基础设施。异构指结合不同类型的处理器和存储资源。隐私、成本与性能的共同约束，使企业不会只追求一个更大的公共模型。

**SaaS会整合而非齐灭。**SaaS是以在线服务方式提供软件，常按账号订阅收费。德勤中国的2026年展望引述Gartner预测，到2030年，35%的独立SaaS工具将被智能体取代，或整合进入大型供应商的代理生态。其指向的是工具和产品形态，不是35%的软件收入或岗位消失。[11]

**浅层产品压力更大。**功能单一、流程嵌入浅、主要靠界面提供价值的软件，更容易被代理调用或平台整合。相比之下，掌握关键业务数据、深度嵌入流程，并能提供权限和合规保障的平台，可能更加重要。AI可以改变用户入口，却不自动消除后台业务系统。[8]

**收费方式各有代价。**按席位、按用量和按结果收费，改变的不只是账单。它们决定了客户承担什么风险，也决定了厂商优化什么指标。

| 收费方式 | 客户购买什么 | 厂商收入依据 | 主要优势 | 主要矛盾 |
|---|---|---|---|---|
| 按席位订阅 | 使用软件的资格 | 账号数与订阅期限 | 预算容易规划 | 用户减少可能影响收入 |
| 按用量收费 | 推理和执行资源 | 调用量、credits、运行资源 | 收入与资源成本更匹配 | 客户账单波动 |
| 按结果收费 | 约定任务或业务成果 | 合格完成量或成果 | 更贴近客户价值 | 成果归因、验收与责任复杂 |

这些方向已见于德勤对SaaS混合定价的分析，以及工信部提出的“出售能力、出售结果”。[11][4]

**结果收费要求更强验收。**例如，客户购买“完成一次合规的数据核对”，就必须明确什么算完成。只生成报告、发现问题和真正纠正问题，是不同交付结果。若业务成果还受客户流程影响，厂商与客户就需要约定责任边界。

**收入增长不保证利润。**AI产品增加模型调用、执行环境、监控和评测成本。客户也可能要求把效率收益体现为降价。德勤因此判断，大模型成本、代理产品投资和混合定价，可能共同挤压软件公司的收入与利润率。[5]

**团队可能更小但更复合。**德勤引述Gartner预测，到2030年，80%的组织会将大型软件工程团队转向更小的AI增强团队。其含义是组织形态变化，并非员工数量减少80%。团队会更依赖能贯通产品、架构、实现与验证的人员，经理的监督跨度也可能扩大。[5]

**中期判断是流程重构。**只购买工具的企业，与同时改造知识、权限和验收体系的企业，收益可能明显分化。能够持续兑现客户价值的平台，更有机会保留定价权。

本节参考文献：
[10] IDC云计算预测 <https://www.idc.com/resource-center/blog/idc-futurescape-2026-%E5%8D%81%E5%A4%A7%E9%A2%84%E6%B5%8B%EF%BC%9Aai-%E6%AD%A3%E5%9C%A8%E5%A6%82%E4%BD%95%E9%87%8D%E5%A1%91%E4%B8%AD%E5%9B%BD%E4%BC%81%E4%B8%9A%E7%9A%84%E4%BA%91%E8%AE%A1%E7%AE%97/> 摘录：“预测 10｜智能体 SaaS 平台 到 2029 年，50% 的中国企业应用将采用 SaaS 平台模式进行实时工作流中的预定义 APP 功能和 AI 智能体的协同，构建模块化和共享交互的解决方案。 SaaS 正在向 应用 + 智能体 的平台形态演进。 这些预测共同说明了什么？ IDC FutureScape 2026 反复传递出一个清晰信号：AI 已经成为云计算发展的第一驱动力。 云不再只是支撑 IT，而是直接决定 AI 能否落地、能否规模化、能否在合规和成本可控的前提下持续运行。 忽视云基础架构演进的企业，将很难在 AI 投资上获得长期回报。 IDC 中国高级研究经理张犁认为，中国云计算市场正…”
[11] 德勤SaaS与智能体展望 <https://www.deloitte.com/content/dam/assets-zone1/cn/zh/docs/industries/technology-media-telecommunications/2026/cn-tmt-predictions-2026-saas-ai-agents.pdf> 摘录：“4程中占据着庞大份额，这些份额可能难以被取代。 到2026年，我们可能会看到大量实验性尝试，整体能力得到提升，同时SaaS市场将缓慢重构，届时 以人工智能为核心的公司将展开竞争。 这种相对温和的进展速度，可能是因为SaaS的 智能代理化 （agentification） 不仅涉及技术变革，还牵涉到供应商和用户双方的商业模式与运营模式的转变。 随着代理式AI的发展，SaaS将变得更加复杂 许多首席信息官（CIO）和首席技术官（CTO）仍面临降低成本并精简所使用供应商数量的压力。 代理式AI时代，人们常常会问，组织应何时以及如何开始将投资转向采用智能体的解决方案，以实现更 一部分大型SaaS提供商在…”
[8] IDC企业应用分析 <https://www.idc.com/resource-center/blog/ai%E6%AD%A3%E5%9C%A8-%E6%9D%80%E6%AD%BB-saas%EF%BC%9F%E6%88%96%E8%AE%B8%E8%AF%A5%E6%8D%A2%E4%B8%AA%E6%80%9D%E8%B7%AF/> 摘录：“随着生成式AI、大模型及Agent能力持续演进，围绕 AI是否会取代SaaS 的讨论正在快速升温。 基于当前企业采用进度、软件支出变化、AI规模化落地情况以及企业工作方式转型趋势的综合观察，IDC的判断是：AI不会在中短期内取代SaaS，但将推动SaaS进入新一轮结构性重构周期。 企业软件市场未来的主要变化，不是SaaS的消失，而是SaaS从 功能交付工具 向 智能执行平台 演进。 当前，AI与SaaS之间并非替代关系，而更接近于 能力叠加 与 价值重定义 关系。 随着企业客户从模型试点走向业务落地，从当前市场需求变化看，企业对软件平台的要求，正在从基础数字化和AI集成能力，进一步延伸至以AI…”
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“2026年9月11日，工业和信息化部举行《 人工智能+软件 专项行动实施方案》新闻发布会。 工业和信息化部信息技术发展司副司长王威伟、中国软件行业协会副理事长兼秘书长吕卫锋、中国电子信息产业发展研究院副院长朱敏、开放原子开源基金会副秘书长李博出席发布会，介绍 人工智能+软件 专项行动有关情况并回答记者提问。 本次新闻发布会由工业和信息化部新闻发言人、办公厅副主任龚宪主持。 工业和信息化部新闻发言人、办公厅副主任 龚宪：各位记者朋友，大家上午好，欢迎出席由工业和信息化部举办的《 人工智能+软件 专项行动实施方案》新闻发布会。 党中央、国务院高度重视人工智能发展， 十五五 规划纲要强调，要全面实施…”
[5] 德勤软件行业展望 <https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/software-industry-outlook.html> 摘录：“Gartner® predicts that, forty percent of enterprise applications will be integrated with task-specific AI agents by the end of 2026, up from less than 5% today (2025).4 Because of value captured from the productivity gains from AI agents, it’s projected that the application software market could pote…”

### 长期：AI原生服务扩大，软件工程仍需解决真实约束

**长期变化在产品核心。**“AI辅助”是在现有软件中加入智能功能；“AI原生”则让模型承担部分核心能力，重构软件运行方式。工信部在工业软件分析中明确区分了这两条路径，并指出AI辅助是当前应用最广、见效最快的方式。[4]

**产品边界可能变软。**传统产品往往预先规定全部操作路径。AI原生服务则可以在受控范围内，根据目标组合工具和功能。客户可能不再分别采购多个轻量应用，而是采购一个能协调这些能力的服务。

**基础系统仍有价值。**数据库、身份权限、交易记录、工业约束和审计机制，不会因为交互方式变化就失去作用。特别是金融、医疗和工业系统，交付质量包含正确性之外的安全、可追溯和持续运行。自然语言入口可以简化操作，但不能替代这些工程要求。

**服务将更持续。**模型即服务，是通过服务接口提供模型能力；智能体即服务，则进一步提供规划、工具调用和任务执行。两者都需要持续评测、监测与更新。工信部将其概括为从产品销售转向持续服务运营，从交付产品转向交付能力和结果。[4]

**能力路径存在分叉。**《2026年国际人工智能安全报告》提出，到2030年，能力可能放缓、维持近期增速，或因AI加速自身研发而出现更快进展。这个分叉会继续影响2031—2036年的软件自主化程度。[12]

**中国市场也有扩展预期。**艾瑞2026年7月的报告，将中国企业级Agent的发展划分为2022—2026年探索、2027—2030年实践，以及2031—2040年规模扩展。它反映的是企业服务市场的演进预期，长期重点包括AI原生服务和复合型人才。[13]

**长期判断是价值迁移。**代码生产的成本可能继续下降，但软件的业务适配、质量控制和持续运营仍要创造价值。谁能掌握这些环节，谁就更可能分享行业增长。

本节参考文献：
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“2026年9月11日，工业和信息化部举行《 人工智能+软件 专项行动实施方案》新闻发布会。 工业和信息化部信息技术发展司副司长王威伟、中国软件行业协会副理事长兼秘书长吕卫锋、中国电子信息产业发展研究院副院长朱敏、开放原子开源基金会副秘书长李博出席发布会，介绍 人工智能+软件 专项行动有关情况并回答记者提问。 本次新闻发布会由工业和信息化部新闻发言人、办公厅副主任龚宪主持。 工业和信息化部新闻发言人、办公厅副主任 龚宪：各位记者朋友，大家上午好，欢迎出席由工业和信息化部举办的《 人工智能+软件 专项行动实施方案》新闻发布会。 党中央、国务院高…”
[12] 国际人工智能安全报告 <https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026-zh.pdf> 摘录：“2025 年， 12 家公司发布或更新了前沿人工智能安全框架 - 这 些文件阐述了它们在构建更强大模型时如何管理风险的计划。 大多数风险管理举措仍属自愿性 质， 但一些司法管辖区已开始将某些实践正式纳入法律 要求。 本报告评估了通用型人工智能系统的能力范围、 其带 来的风险以及如何管理这些风险。 立专 家的指导下完成， 其中包括来自 30 多个国家及 欧盟、 经合组织和联合国等国际组织的提名专家。 主席领导下， 共同撰写本报告的独立专家们对其内容 本报告重点关注功能最强大的通用型人工智能系统 通用型人工智能指能够执行多 种任务的人工智能模型…”
[13] 艾瑞企业级Agent报告 <https://report.iresearch.cn/report/202607/4848.shtml> 摘录：“图13企业选择公有云订阅模式AI Agent产品的原因 ( 2026年H1 ) 图14 AI Agent私有化部署项目价格及类型 ( 2025年+2026年Q1 ) 图15独立AI Agent和嵌入式AI Agent项目数量占比 ( 2025年 + 2026年Q1 ) 图16企业青睐的项目模式 ( 单选 ) 图17 RaaS模式项目数占比 ( 2025年+2026年Q1 ) 图18 2025-2030年中国企业级智能体市场规模（ 产品及解决方案市场 ） 第二部分：中国企业级AI Agent发展周期推演 图1 Tech Cycle Insig…”

## 三、AI已经做到什么：局部效率、真实交付和长期质量

本节参考文献：
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“研究 模型即服务 智能体即服务 等智能服务标准，明确服务交付质量和责任边界。…”
[12] 国际人工智能安全报告 <https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026-zh.pdf> 摘录：“生成的图像在真实性和复杂性方面已经有了显著提升 向人工智能工具提供某个人的照片…”
[13] 艾瑞企业级Agent报告 <https://report.iresearch.cn/report/202607/4848.shtml> 摘录：“本报告系统分析了中国企业级AI Agent市场的发展现状。 基于技术周期视角，…”

### 编码提效有实证，但不同指标不能混成一个数

**任务效率确有改善。**随机试验和企业现场研究，已经给出多项正面结果。不过，“完成更快”“写出更多代码”“提交更多PR”和“交付更多可靠功能”，分别衡量不同事物。

| 研究及测量期 | 样本与场景 | 主要结果 | 测量对象 | 证据性质 |
|---|---|---|---|---|
| Google，2024年6—7月 | 96名全职工程师 | 任务完成约快21% | 标准化企业任务 | 随机对照 |
| Cui等，2024—2025年论文 | 三项现场实验，4,867人 | 吞吐提高约26% | 每周任务或PR | 企业现场随机实验 |
| 蚂蚁CodeFuse，2023年 | 1,219名程序员，12周 | 代码产出提高55% | 代码量 | 现场实验与双重差分 |
| GitHub代码质量研究 | 202份有效Python提交 | 全部测试通过可能性高53.2% | 单一API任务 | 厂商随机对照 |
| NAV IT，两年观察 | 39人、703个仓库 | 提交活动变化不显著 | commit活动 | 纵向观察 |
| Borg等，2024年末试验 | 151名参与者 | 开发耗时中位数减少30.7% | 功能开发任务 | 两阶段研究 |

Google与三项现场实验的结果见企业编码试验；CodeFuse数据来自BIS工作论文。Google企业随机试验[14]CodeFuse现场实验[15]其余结果分别见GitHub、NAV IT和软件维护性研究。[16][17][18]

**Google测的是内部工具。**该试验让工程师使用代码补全、智能粘贴和自然语言转代码功能，完成一个企业级任务。约21%的结果，不是GitHub Copilot的实验结果，也不是所有开发活动的统一提效幅度。试验同时发现，资历更高和日常编码更多的工程师完成任务更快。[14]

**CodeFuse的收益有分化。**该实验在2023年9月4日至11月25日开展。处理组335人，对照组884人，代码产出平均提高55%；工作经验不超过一年的初级组提高67%，较有经验组的效果为正但未达到统计显著。[15]

**帮助不只来自代写。**CodeFuse论文另估计，直接生成并被采用的代码，对应约11%—18%的产出提升。作者认为，其余收益可能来自时间节省和编码瓶颈缓解。AI解释错误、帮助找到相关代码，也能提高产出，不必全部表现为机器直接生成的代码行。

**采用者本来就可能不同。**NAV IT清洗后的样本包含26,317条提交，覆盖39名开发者。其中25名使用Copilot，14名未使用。采用者在工具引入前，提交频率已经超过非采用者两倍，因此不能把两组后来的活动差距全部归于工具。[17]

**无显著变化也有含义。**NAV IT研究没有观察到采用后提交活动的显著跃升。这与受控编码任务提速并不必然矛盾：工程师可能把节约的时间用于沟通、学习和审查，组织瓶颈也可能限制代码合并。提交次数只是工作活动的一部分。

**使用熟练度影响收益。**Borg等研究在第一阶段发现，AI辅助组完成时间中位数减少30.7%，习惯使用AI者的估计提速更高。研究同时显示，原有编程能力仍很重要。工具熟练度与工程能力，是相互补充而非互相替代的因素。[18]

本节参考文献：
[14] Google随机试验 <https://arxiv.org/html/2410.12944v2> 摘录：“While some studies have investigated the perceived usefulness of AI-enhanced developer tools (e.g., 14, 28, 29 ), quantifying actual productivity or speed gains has proven more challenging, due to difficulties in accessing and analyzing unbiased, real-world usage data. Moreover, understanding d…”
[15] BIS现场实验 <https://www.bis.org/publications/working-paper-1208-generative-ai-and-labour-productivity-field-experiment-coding.pdf> 摘录：“instructions about the new LLM from September 4th, 2023 to October14th and started to use the CodeFuse during this period. At the same time, we also analysed a control group of 884 programmers working in other departments that were not informed about the introduction of The treatment group and…”
[16] GitHub代码质量研究 <https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/> 摘录：“Fararooy, A Simple and Effective Measure for Complex Low-Level Dependencies, 2010 IEEE 18th International Conference on Program Comprehension, Braga, Portugal, 2010, pp. 80-83, doi: 10.1109/ICPC.2010.49. keywords: {Software measurement; Lab-on-a-chip; Size measurement; Length measurement; Appli…”
[17] NAV IT纵向研究 <https://arxiv.org/html/2509.20353v2> 摘录：“After Copilot’s launch, the user group’s insertions ticked up slightly (to 200/week) while deletions ticked down ( 98/week), yielding an increase in net lines of code (+16 net lines as average weekly). Non-users, by contrast, showed a small decline in both additions ( 70) and deletions ( 30) in…”
[18] Borg等维护性研究 <https://link.springer.com/article/10.1007/s10664-026-10889-1> 摘录：“We used TypeformFootnote 16 to distribute and collect both the prescreening and exit questionnaires. Both questionnaires were piloted with four developers from Equal Experts to ensure clarity and relevance. The feedback led to only minor adjustments. We opted for a phased rollout of the program…”

### 从代码提速到团队交付，中间还有一段距离

**企业收益可以多维出现。**GitHub与Accenture的研究报告，PR数量增加8.69%，PR合并率提高15%，成功构建次数增加84%。这些指标表明工具可嵌入真实工作流；其中“成功构建次数”是数量，不等于构建成功率提高84%。[19]

**功能正确性可以改善。**GitHub另一项随机研究，招募至少有五年Python经验的开发者，为虚构评论网站编写API。有效提交中，Copilot组104份，对照组98份。AI组通过全部十个测试的可能性高53.2%，这里是相对差异，不是提高53.2个百分点。[16]

**组织指标却可能反向。**DORA的2025.2版报告估计，AI采用指标提高25%，与文档质量提高7.5%、代码质量提高3.4%、代码评审速度提高3.1%相关。同时，交付吞吐下降1.5%，交付稳定性下降7.2%。这些是统计关联，而非一次随机干预的因果效果。[20]

**瓶颈可能只是转移。**DORA提出一种解释：AI使团队在相同时间生成更多代码，导致变更集变大。较大的变更需要更多理解、集成与测试，也可能更难回滚。由此，局部实现更快，反而可能伴随更慢、更不稳定的整体交付。

**开发者感受也会分裂。**一项2026年纵向研究，在相隔六个月的问卷中获得95名配对参与者。84%在两个时点都报告生产率改善，但至少一个体验维度恶化的比例，从14%升至27%。工作重心从创作转向指导、检查和纠正AI输出，研究称其为“监督工程工作”。[21]

**正确指标应看净交付。**对管理者而言，重要的不是AI生成了多少内容，而是合格功能是否更快到达用户。评审等待、返工、事故和维护成本，都应进入生产率判断。否则，团队可能在生成端显示繁忙，却在交付端积累拥堵。

本节参考文献：
[19] Accenture企业研究 <https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/> 摘录：“Research: Quantifying GitHub Copilot’s impact in the enterprise with Accenture We conducted research with developers at Accenture to understand GitHub Copilot’s real-world impact in enterprise orga…”
[16] GitHub代码质量研究 <https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/> 摘录：“Ready to build high-quality code quickly? Get started with GitHub Copilot Does GitHub Copilot improve code quality? Here’s what the data says Findings in our latest study show that the quality of c…”
[20] DORA生成式AI报告 <https://dora.dev/ai/gen-ai-report/dora-impact-of-generative-ai-in-software-development.pdf> 摘录：“20 How�gen�AI�affects�the�value�of�development�work But,�we�believe�that�rewarding� Support�developers�in�choosing� developers for the outcomes of their not�to�use�gen�AI�for�tasks�they�enjoy. work…”
[21] 工程师工作变化研究 <https://doi.org/10.48550/arxiv.2605.23135> 摘录：“Computer Science Software Engineering Submitted on 22 May 2026 Title:The Impact of AI Coding Assistants on Software Engineering: A Longitudinal Study View PDF HTML (experimental)Abstract:AI coding…”

### 四个产品和企业案例，代表不同的自动化路径

**产品能力已经跨环节。**Copilot、CodeFuse、Codex和Devin，不再只是“替人敲键盘”的同类工具。它们分别展示了编辑器辅助、企业现场增强、异步仓库执行和质量流程重构。

| 产品或案例 | 主要作用位置 | 交付方式 | 人的核心工作 | 证据类型 |
|---|---|---|---|---|
| GitHub Copilot | 编码、评审、团队治理 | 编辑器与企业工作流集成 | 选择、审查、集成 | 实验与产品说明 |
| 蚂蚁CodeFuse | 日常编码 | 工程师接受建议并完成任务 | 理解与修改建议 | 企业现场实验 |
| OpenAI Codex | 仓库任务、测试、PR | 云端沙盒异步执行 | 定义意图、环境和验收 | 产品说明与内部案例 |
| Devin与Litera | 需求分流、测试、运维 | 专门代理工作流 | 设计流程、优化与升级 | 客户案例 |

**Codex展示了高自动化。**OpenAI内部项目从2025年8月下旬的空仓库开始，约五个月形成约100万行代码、约1,500个合并PR。团队起步为三名工程师，后来扩至七名。团队估计，其耗时约为手写代码的十分之一。[3]

**没有手写不等于没有工程师。**这个项目中的应用逻辑、测试、配置和文档都由代理编写，但人负责工程环境、任务意图和反馈机制。案例的关键，不只是模型会写代码，而是团队将知识、约束、测试与可观测性变成代理可以使用的基础设施。

**仓库结构决定自主范围。**该团队报告，代理可以复现缺陷、修复代码、驱动应用、响应评审并处理构建失败。作者同时明确指出，这些行为高度依赖该仓库的结构与工具。对既有系统，建设同类环境本身就是一项工程投入。[3]

**Litera展示了岗位重构。**2025年8月25日的客户案例称，部署Devin测试代理后，测试覆盖率提高40%，团队产出达到原来的十倍。页面对回归周期同时使用“快93%”和“缩短90%”两种表述，因此应保留原有表述，而不合成一个统一提效值。[22]

**案例也产生新职责。**Litera称，30天内活跃Devin使用人数增长超过一倍，达到90多人。质量工程人员开始转向代理构建和优化，一些工作进一步面向SRE、DevOps等角色。工程师还建立了可同时向代理分配十多个Jira任务的系统，并在编码前检查需求完整性。[22]

**案例的启示是环境重要。**高自动化通常伴随任务结构化、测试完善和反馈机制建设。单独购买同一产品，并不自动获得同样的流程能力。

本节参考文献：
[3] 代理优先工程案例 <https://openai.com/index/harness-engineering/> 摘录：“Title: Harness engineering: leveraging Codex in an agent-first world Markdown Content: Over the past five months, our team has been running an experiment: building and shipping an internal beta of a software product with 0 lines of manually-written code . The product has internal daily users and external alpha testers. It ships, deploys, breaks, and gets fixed. What’s different is that every line of code—application logic, tests, CI configuration, documentation, observability, and internal tooling—has been written by Codex. We estimate that we built this in about 1/10th the time…”
[22] Litera质量工程案例 <https://www.devin.ai/customers/litera> 摘录：“Title: With Devin, Litera cut regression cycles by 90%, delivering new products to customers faster than ever. Published Time: 2025-08-25 Markdown Content: _With Devin, Litera is collapsing engineering silos, accelerating delivery, and transforming roles—helping the legal tech leader ship more products, faster, and move at the speed of a startup more than ever before._ Litera, a global leader in legal technology, serves thousands of law firms and legal professionals worldwide with solutions that streamline workflows, improve collaboration, and deliver insights at speed. With more…”

### 维护、安全和基准测试，给出了另一面

**质量不是单一维度。**代码能通过测试，不代表系统能部署；系统可以启动，也不代表安全和可维护性良好。不同研究出现正反结果，往往是因为它们观察的对象、时间跨度和质量指标不同。

| 研究 | 规模与时间 | 主要发现 | 观察对象 |
|---|---|---|---|
| Borg等，2026年发表 | 151名参与者，两阶段试验 | 后续演化时间与质量无显著差异 | 他人继续修改代码 |
| Xia，2026年7月 | 182个仓库 | 代理贡献纠正性维护更多 | 合并后缺陷与漏洞 |
| AIDev分析，2026年9月 | 37,623条PR，2,807个仓库 | 回滚表现因代理而异 | 公开仓库贡献 |
| Zenodo受控研究，2026年9月 | 四个代理、12次交付 | 仅三次交付可启动 | 完整API系统 |

相关研究分别提供了维护实验、纵向仓库观察和受控交付证据。[18][23][24][25]

**维护研究并非一致悲观。**Borg等研究的第二阶段，让新参与者在不使用AI的情况下，继续演化第一阶段代码。研究没有发现明显的维护性优势或劣势。这说明，在其任务范围内，AI辅助开发并不必然给下一位开发者留下更差代码。

**代理代码也有后续成本。**Xia对182个仓库的研究发现，人类与代理贡献的总体维护率相近，但代理贡献需要更多纠正性维护，并引入更多安全弱点和依赖项漏洞。项目未经评审的比例每增加十个百分点，与代理维护负担平均增加约6%相关。[23]

**不同代理不能混为一谈。**2026年9月12日提交的AIDev研究，比较Codex、Devin、Copilot、Cursor、Claude Code与匹配的人类贡献。其公开的回滚率结果如下；测量期为2024年12月至2025年7月。[24]

| PR来源 | 合并后回滚率 | 相对人类基线 |
|---|---|---|
| Codex | 6.1% | 较低 |
| 匹配人类样本 | 11.5% | 比较基线 |
| Devin | 14.5% | 较高 |

**安全指标也有正面结果。**同一AIDev研究将五家代理合并后，发现新增代码出现“安全异味”的优势比为0.63，低于人类代码。安全异味指硬编码凭据等可疑模式，并不等于完整漏洞。该结果与Xia的依赖漏洞观察，衡量的不是同一个安全维度。

**人工评审仍占资源。**AIDev研究还发现，Copilot的PR获得最多人工评审和修改请求；Claude Code的PR等待首次人工评审的中位时间为12.6小时。这提示代理增加实现供给后，人类评审能力仍可能影响交付速度。[24]

**独立测试具有不同价值。**Zenodo于2026年9月8日发布的受控研究，让四个代理各执行三次，生成12个相同技术栈的API系统。只有三个交付能够启动。代理自己的测试未发现所统计的12个缺陷，而独立测试发现了运行能够触及的四个缺陷。[25]

**失败常在工程连接处。**该实验反复出现缺失依赖、版本不兼容和迁移配置问题。它们并非都属于算法难题，却能直接阻止系统交付。对企业而言，这说明“生成业务代码”与“交付可运行系统”之间，仍有环境和集成工作。

**测试本身也可能被改错。**一篇2025年底Agentic SOC项目复盘记录，AI为让测试通过，将创建资源应返回的201状态码按200处理。人工评审后，团队修复的是源代码，而不是继续放宽测试。这个个案解释了为何生成代码与验收标准不宜完全同源。[26]

**基准分数要看题目质量。**OpenAI的SWE-bench Verified包含500个经人工验证的仓库级问题，曾报告GPT-4o解决33.2%。其任务是根据问题描述修改仓库并通过测试，属于具体修复能力，而非完整软件生产过程。[27]

**测试薄弱会改变得分。**2024年的SWE-Bench+研究筛查2,294个GitHub问题后，将SWE-Agent与GPT-4组合的解决率，从12.47%下调至3.97%。主要原因涉及问题中直接泄露解法，以及测试不足以检验补丁正确性。[28]

**能力在进步，评测也在改。**2026年9月8日的SWE-Bench Pro Verified预印本，继续讨论隐藏评测信息泄漏、误导性描述和测试范围问题。它指出，修正后某些模型表现显著下降。因此，评价代理需要同时观察真实交付和长期后果，而不只是静态得分。[29]

**本节的判断是：**AI对局部任务的提效证据较明确，但稳定的全流程收益，要靠独立验证、较小变更和长期质量共同支撑。

本节参考文献：
[18] Borg等维护性研究 <https://link.springer.com/article/10.1007/s10664-026-10889-1> 摘录：“The file-level score penalizes the presence of 25+ code smellsFootnote 1 known to increase cognitive load on developers. Our previous work shows that CodeHealth correlates with increased maintenance costs and defect risks (Tornhill and Borg 2022; 2024c),…”
[23] Xia纵向研究 <https://arxiv.org/abs/2607.09902> 摘录：“From: Chunqiu Steven Xia view email v1 Fri, 10 Jul 2026 18:45:37 UTC (1,719 KB) References & Citations Bibliographic and Citation Tools Bibliographic Explorer (What is the Explorer? Connected Papers (What is Connected Papers? Litmaps (What is Litmaps? sc…”
[24] AIDev代理比较 <https://doi.org/10.48550/arxiv.2609.17598> 摘录：“Computer Science Software Engineering Submitted on 12 Sep 2026 Title:Not All Agents Are Equal: Code Quality and Post-Merge Maintenance Across Five Autonomous Coding Agents in the Wild View PDF HTML (experimental)Abstract:Autonomous coding agents now open…”
[25] 受控交付研究 <https://doi.org/10.5281/zenodo.22551155> 摘录：“download=1) md5:24e7b88abdc4c65f480ec9ff4119e36c 491.0 kB Preview ( include_deleted=0) Download (”
[26] 工程项目复盘 <https://www.secrss.com/articles/87116> 摘录：“在刚刚过去的一期项目中，我们消耗了约23亿Token，使用Cursor Ultra与Claude Code构建了一个企业级 Agentic SOC平台。 本文从软件工程的角度，复盘如何通过架构约束、测试驱动与文档管理，驾驭AI完成从35万行生成代码到8万行核心代码的提炼。 2025年底，Agentic SOC 平台的一期开发终于快要收官。 回顾这两个月，我最大的感受不是在和智能体（Agent）对话，而是在和美元（$）对话。 即便使用了Cursor Ultra会员和Claude Code的代理，Token…”
[27] SWE-bench Verified说明 <https://openai.com/index/introducing-swe-bench-verified/> 摘录：“Title: Introducing SWE-bench Verified Markdown Content: Skip to main content ( Developers ( Foundation(opens in a new window) ( Log in Try ChatGPT(opens in a new window) ( openaicom-did=dee56070-7269-415c-87f8-129cbd3c5abe&openaicom_referred=true) Founda…”
[28] SWE-Bench+研究 <https://doi.org/10.48550/arxiv.2410.06992> 摘录：“Computer Science Software Engineering Submitted on 9 Oct 2024 (v1), last revised 10 Oct 2024 (this version, v2) Title:SWE-Bench+: Enhanced Coding Benchmark for LLMs View PDF HTML (experimental)Abstract:Large Language Models (LLMs) in Software Engineering…”
[29] 基准验证研究 <https://doi.org/10.48550/arxiv.2609.08149> 摘录：“From: Dingbo Yuan view email v1 Tue, 8 Sep 2026 02:29:58 UTC (1,396 KB) v2 Wed, 16 Sep 2026 03:28:37 UTC (1,396 KB) v3 Fri, 9 Oct 2026 02:16:00 UTC (1,395 KB) Additional Features References & Citations Bibliographic and Citation Tools Bibliographic Explo…”

## 四、七个生命周期环节：自动化程度与监督要求并不同步

**编码和重复测试最直接。**需求整理、部署监控和维护也会明显改变，但更加依赖工作环境。架构、安全和高风险运行决策，则更偏向AI辅助与专业监督。下面的高、中、低是2026—2031年的定性分析，描述任务自动化倾向，不是整岗消失概率。

| 环节 | 任务自动化倾向 | 可交给AI的任务 | 当前需人承担的核心能力 | 监督方式 | 整环节判断 |
|---|---|---|---|---|---|
| 需求分析 | 中 | 整理、草拟、歧义检查 | 协商、优先级、业务责任 | 高：确认目标与验收 | 部分自动化 |
| 设计与架构 | 低—中 | 方案推荐、结构分析 | 跨系统权衡、长期演化 | 高：评审约束与取舍 | 协作主导 |
| 编码 | 高 | 生成、调试、重构、PR | 意图表达、集成、质量责任 | 中高：读码与独立测试 | 窄任务可闭环 |
| 测试 | 重复任务高 | 用例生成、回归、风险识别 | 探索、体验、业务风险 | 高：独立验收标准 | 执行减少，质量职能保留 |
| 部署运维 | 中—高 | 流水线、监控、常见故障处理 | 服务目标、事故指挥、风险接受 | 高：权限、灰度与回滚 | 受控自动化 |
| 维护 | 中—高 | 缺陷复现、修复、技术债分析 | 历史约束、回归与演化判断 | 高：追踪合并后后果 | 自动化与维护负担并存 |
| 安全 | 扫描任务高 | 漏洞识别、分级、部分修复 | 威胁建模、合规、安全责任 | 最高：专业复核与审计 | 增强而非整体替代 |

需求与架构判断依据软件工程综述；测试、部署和安全分别结合QA分析、交付流程和产品文档。[2][30][31][32]

本节参考文献：
[2] AI软件工程综述 <https://arxiv.org/html/2409.18048v3> 摘录：“Section 2 discusses the availability of large code sets on coding platforms that form the basis for training AI using actively applied, operated and maintained code. Section 3 addresses the role…”
[30] IBM质量保证分析 <https://www.ibm.com/cn-zh/think/insights/quality-assurance-in-software-testing-with-ai> 摘录：“在 AI 编程智能体出现之前，软件测试依赖于手动操作和分析，这通常是软件开发生命周期 (SDLC) 末期的瓶颈。 人工测试既耗时又缓慢，而且人类 QA 工程师必须逐步模拟整个端到端用户旅程，很容易出错。 几乎不可能对每种情况都进行测试，因此测试范围往往不完整，导致发布后出现错误。 更重要的是，这些测试人员需要深厚的领域知识来正确识别问题并确定优先排序。 在软件测试中，软件质量保证（QA…”
[31] CODING质量流程 <https://coding.net/solutions/code-quality> 摘录：“将代码质量内建在研发流程中，持续研发优质代码 将代码质量内建在研发流程中，持续研发优质代码 直接提交主干，极易引入垃圾代码，包括第三方包代码、编译中间产物、构建中间产物等垃圾代码。 锁定主干，使用 Git 多分支开发。 保护主干分支，为每个任务创建一个短分支，提交代码时创建合并请求，合入后自动删除短分支。 人工走读，规范标准不一。 代码规范的遵守只能靠提交人与评审人对代码规范的个人理解…”
[32] Claude Code安全审查说明 <https://support.claude.com/zh-CN/articles/11932705-claude-%E4%BB%A3%E7%A0%81%E4%B8%AD%E7%9A%84%E8%87%AA%E5%8A%A8%E5%8C%96%E5%AE%89%E5%85%A8%E5%AE%A1%E6%9F%A5> 摘录：“Claude Code 现已包含自动化安全审查功能，帮助您识别和修复代码中的漏洞。 本指南说明如何使用 /security-review 命令和 GitHub Actions 来改进代码安全性。 注意：虽然自动化安全审查有助于识别许多常见漏洞，但它应该补充而非替代您现有的安全实践和手动代码审查。 Claude Code 中的自动化安全审查帮助开发人员在漏洞进入生产环境之前捕获它们。 这…”

### 需求与架构：文字可以生成，取舍需要落地

**需求分析先减少整理。**AI适合汇总访谈、草拟用户故事、发现表述歧义，以及检查问题单是否完整。软件工程综述中的需求工具，就包括将自然语言需求转换为模型，并向分析师提出歧义和流程不完整的建议。[2]

**真正困难是处理冲突。**客户提出的需求，可能与预算、合规和其他部门利益冲突。AI可以列出方案，却不能仅凭一段文档决定谁应接受损失。需求岗位的价值，因而从“写出需求说明书”向“形成可执行且获得认可的目标”迁移。

**架构设计会更可检索。**历史决策、代码结构与设计原理，可以帮助代理选择更合适的实现。北航团队的DRMiner在三个大型开源项目中挖掘设计原理，注入代码变更任务后，完全匹配补丁数量比未注入时提高10—18倍。[33]

**架构仍要承担长期权衡。**一个局部最简方案，未必最适合系统未来演化。性能、成本、可用性、团队能力和迁移风险，需要一起考虑。AI的建议越容易生成，架构师越要明确约束，避免把大量看似合理的局部方案拼成不一致的整体。

本节参考文献：
[2] AI软件工程综述 <https://arxiv.org/html/2409.18048v3> 摘录：“Section 2 discusses the availability of large code sets on coding platforms that form the basis for training AI using actively applied, operated and maintained code. Section 3 addresses the role of models in SE. Bringing these two sectio…”
[33] DRMiner研究介绍 <https://global.buaa.edu.cn/info/1038/4638.htm> 摘录：“近日，第39届IEEE/ACM自动化软件工程国际会议（IEEE/ACM International Conference on Automated Software Engineering，简称ASE）在美国萨克拉门托召开，ASE是CCF-A类国际学术会议之一，也是软件工程领域的三大知名会议之一。 北航计算机学院张莉教授团队共有4篇论文被录用，其中题为《DRMiner：Extracting Latent Design Rationale from Jira Issue…”

### 编码与测试：生成成本下降，验收价值上升

**编码适合明确边界。**补全、样板代码、局部重构和已有模式的迁移，通常具有较清楚的输入与输出。工具也能减少理解新代码库和定位错误的时间。因此，编码执行任务的自动化倾向，高于目标开放、责任复杂的工作。

**集成决定真正完成。**在真实项目中，一个功能还要适配已有接口、数据迁移和运行环境。代理写出的代码即使局部正确，也可能与系统约定冲突。开发者需要判断变更是否越界，而不是只判断它是否能编译。

**测试执行会继续减少。**IBM的QA分析列出，AI可以生成用例、识别缺陷、预测高风险变更，并执行功能、性能、压力和回归测试。这些能力能减少重复验证，也能扩大原先因时间不足而被放弃的检查范围。[30]

**质量保证并不只看通过。**测试工程师还要判断是否测对了问题。边缘行为、不同用户群的体验和低频高损失风险，不一定能从既有模式中推出。未来测试岗位更可能向测试策略、独立评测和业务风险治理移动，而非测试职能整体消失。

**自动化门禁可以分工。**腾讯云CODING的流程，将单元测试和代码扫描放在合并前。检查通过后，人工评审可以更集中地判断业务逻辑和设计模式。这种分工，把机械检查交给工具，将人的注意力用于较高层次问题。[31]

本节参考文献：
[30] IBM质量保证分析 <https://www.ibm.com/cn-zh/think/insights/quality-assurance-in-software-testing-with-ai> 摘录：“在 AI 编程智能体出现之前，软件测试依赖于手动操作和分析，这通常是软件开发生命周期 (SDLC) 末期的瓶颈。 人工测试既耗时又缓慢，而且人类 QA 工程师必须逐步模拟整个端到端用户旅程，很容易出错。 几乎不可能对每种情况都进行测试，因此测试范围往往不完整，导致发布后出现错误。 更重要的是，这些测试人员需要深厚的领域知识来正确识别问题并确定优先排序。 在软件测试中，软件质量保证（QA 或 SQA）是确保软件的开发和维护始终符合质量标准的过程。 质量控制侧重于发现最终产品中的缺陷，而质量保证则通过改进构建高质量软件的流程来预防缺陷。 QA 团队会制定单元测试编写规…”
[31] CODING质量流程 <https://coding.net/solutions/code-quality> 摘录：“将代码质量内建在研发流程中，持续研发优质代码 将代码质量内建在研发流程中，持续研发优质代码 直接提交主干，极易引入垃圾代码，包括第三方包代码、编译中间产物、构建中间产物等垃圾代码。 锁定主干，使用 Git 多分支开发。 保护主干分支，为每个任务创建一个短分支，提交代码时创建合并请求，合入后自动删除短分支。 人工走读，规范标准不一。 代码规范的遵守只能靠提交人与评审人对代码规范的个人理解、掌握、自觉遵守，规范执行情况参差不齐。 开启自动代码扫描，建立质量门禁。 及时发现潜藏的代码缺陷、安全漏洞以及不规范问题。 自动拦截问题代码的合入，防止目标分支被污染。 无任何单元…”

### 部署、维护和安全：错误的后果更加不对称

**运维自动化看权限。**生成部署脚本与实际修改生产系统，是风险完全不同的活动。后者可能影响数据和客户服务，因此需要访问控制、过程留痕和回滚机制。SLO即服务等级目标，表示系统需要达到的可用性或性能要求，其取舍仍需业务与技术共同决定。

**事故处理需要组织判断。**代理可以分析日志、提出原因并执行预先授权的操作。但在原因不明、多个系统相互影响时，是否停服、降级或回滚，需要权衡客户影响。运维人员会减少常规执行，却更重视异常情况下的决策和恢复能力。

**维护必须跨越时间。**AI擅长修复当前可复现的问题，但维护还要保留历史兼容性。今天消除一个报错，可能改变某个旧客户依赖的行为。维护人员需要了解系统为何这样设计，并追踪修复后的长期影响。

**安全自动化有双重性。**AI既可以帮助发现漏洞，也可能加快攻击和不安全代码生产。《2026年国际人工智能安全报告》记录，一项竞赛中的智能体识别出组织者引入的77%漏洞。这个结果显示能力潜力，同时也意味着安全需求不会只因检测提速而减少。[12]

**功能正确不保证安全。**2026年7月一项包含44名专业开发者的研究发现，Copilot改善了功能正确性，但没有显著改善安全API的正确使用。许多开发者没有意识到最终实现仍不安全。这正是安全专业监督的重要性。[34]

**代理还扩大攻击入口。**当工具可以访问代码库、数据和执行环境，恶意内容就可能诱导它越权操作。工信部2026年9月的安全问答，因此强调代理身份、访问控制、数据安全、行为可控和全程可追溯。[4]

**本节的判断是：**任务越结构化，越容易自动化；错误代价越高，越不能用较少人工参与作为唯一成功指标。

本节参考文献：
[12] 国际人工智能安全报告 <https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026-zh.pdf> 摘录：“2025 年， 12 家公司发布或更新了前沿人工智能安全框架 - 这 些文件阐述了它们在构建更强大模型时如何管理风险的计划。 大多数风险管理举措仍属自愿性 质， 但一些司法管辖区已开始将某些实践正式纳入法律 要求。 本报告评估了通用型人工智能系统的能力范围、 其带 来的风险以及如何管理这些风险。 立专 家的指…”
[34] 安全API编程研究 <https://doi.org/10.48550/arxiv.2607.11348> 摘录：“Computer Science Software Engineering Submitted on 13 Jul 2026 Title:Understanding the Impact of AI Code Assistants on Security API Usage: An Empirical Stu…”
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“2026年9月11日，工业和信息化部举行《 人工智能+软件 专项行动实施方案》新闻发布会。 工业和信息化部信息技术发展司副司长王威伟、中国软件行业协会副理事长兼秘书长吕卫锋、中国电子信息产业发展研究院副院长朱敏、开放原子开源基金会副秘书长李博出席发布会，介绍 人工智能+软件 专项行动有关情况并回答记者提问。…”

## 五、五类岗位：谁更承压，谁的价值会迁移

**资历不是唯一保护。**初级开发通常承担更多可生成任务，因此招聘压力较直接。但高级岗位也会失去部分编码、文档和协调工作。差别在于，一个人是否拥有业务理解、系统判断和独立验证能力。

| 岗位 | 可交给AI的任务 | 当前更关键的人工能力 | 监督责任 | 1—3年压力 | 3—5年变化 |
|---|---|---|---|---|---|
| 初级开发 | 标准编码、基础测试、文档 | 理解、调试、集成、学习 | 需导师与独立检查 | 高，集中于重复任务 | 入门门槛与培养方式改变 |
| 高级开发 | 局部实现、重构、维护辅助 | 架构、复杂故障、质量判断 | 高，审核代理结果 | 中，执行职责减少 | 转向系统与代理监督 |
| 产品经理 | 用户故事、材料整理、原型草拟 | 用户价值、优先级、市场取舍 | 高，确认问题与结果 | 中，文档任务先变 | 更重领域与价值判断 |
| 项目经理 | 状态汇总、分流、计划编排 | 依赖协调、冲突处理、交付治理 | 高，处理升级与承诺 | 中，行政任务承压 | 向跨系统变更管理延伸 |
| 工程管理者 | 指标整理、流程与代理编排 | 人员、资源、目标与风险责任 | 最高，建立责任链 | 低—中 | 管理跨度扩大，治理要求提高 |

岗位变化与德勤角色分析、Hays招聘观察及工信部人才判断相符。[35][36][4]

本节参考文献：
[35] 德勤工程角色分析 <https://www.deloitte.com/us/en/industries/tmt/articles/ai-software-development-engineering-roles-being-rewritten.html> 摘录：“If we have selected the wrong experience for you, please change it above. As the evolution of AI t…”
[36] Hays技术招聘报告 <https://www.haysplc.com/media/press-releases/2025/china-sees-shift-in-tech-hiring> 摘录：“全球领先的招聘及劳动力解决方案专家瀚纳仕（Hays）近期发布报告，深入研究了人工智能对技术领域职场的变革性影响。 报告对关键技术岗位受人工智能影响的程度进行了排名，100 分表示受影响最大，0 分…”
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“2026年9月11日，工业和信息化部举行《 人工智能+软件 专项行动实施方案》新闻发布会。 工业和信息化部信息技术发展司副司长王威伟、中国软件行业协会副理事长兼秘书长吕卫锋、中国电子信息产业发展研…”

### 初级开发：产出更容易提高，成长却不能外包

**初级人员同时受益受压。**CodeFuse的初级组代码量增幅更大，说明AI可以帮助经验较少的人越过执行障碍。但如果企业主要需要这些标准化执行任务，同样的增益也可能减少招聘需求。对个人的帮助和对岗位数量的压力，可以同时存在。

**学习效果值得单独看。**Shen与Tamkin在2026年的随机试验中，让52名多数为初级的软件工程师学习不熟悉的Python库Trio。AI组即时测验平均50%，手写代码组67%，相差**17个百分点**。AI组约快两分钟，但速度差异未达到统计显著。[37]

**生成不等于理解。**如果工程师把实现、调试和验证都交给工具，可能完成任务却没有形成独立判断。相反，要求解释代码、自己定位错误、理解概念，再使用生成结果，更符合监督AI所需的能力。上述研究的交互分析，也观察到不同使用方式与学习成绩存在差异。

**企业需要保留成长任务。**初级岗位并非只能创造当期代码，还承担未来高级工程师的培养。如果低难度任务全部自动化，企业需要重新设计练习和带教，让新人仍能积累调试、事故分析和系统理解经验。这是人才供给问题，不只是短期成本问题。

本节参考文献：
[37] AI辅助与编码技能研究 <https://www.anthropic.com/research/AI-assistance-coding-skills> 摘录：“Research shows AI helps people do parts of their job faster. In an observational study of Claude.ai data, we found AI can speed up some tasks by 80%. But does this increased productivity come with trade-offs? Other research shows that when people use AI…”

### 高级开发：经验价值在验证，而非代码速度

**高级开发并非收益较小。**CodeFuse按一年经验分组时，较有经验者请求AI建议约少70%，生产率改善不显著。Google试验却发现，资历更高者在任务中更快。不同结果提示，收益取决于工具、任务、采用频率和原有能力，而非简单的资历排序。[15][14]

**经验用于控制代理。**Huang的研究通过13人的现场观察和99人的定性调查发现，有经验开发者重视代理的生产率帮助，同时坚持保留设计与实现的控制。他们用软件最佳实践和专业知识，决定哪些任务适合委派。[38]

**谨慎也是责任表现。**Stack Overflow的2025年调查中，经验丰富者“高度信任”AI的比例为2.6%，“高度不信任”为20%。这不说明高级人员排斥工具，而表明承担责任的人，更需要看清结果是否可靠。[39]

本节参考文献：
[15] BIS现场实验 <https://www.bis.org/publications/working-paper-1208-generative-ai-and-labour-productivity-field-experiment-coding.pdf> 摘录：“instructions about the new LLM from Sept…”
[14] Google随机试验 <https://arxiv.org/html/2410.12944v2> 摘录：“While some studies have investigated the…”
[38] 有经验开发者研究 <https://doi.org/10.48550/arxiv.2512.14012> 摘录：“Computer Science Software Engineering Su…”
[39] 开发者信任调查 <https://survey.stackoverflow.co/2025/> 摘录：“The 2025 Developer Survey is the definit…”

### 产品、项目和管理：材料工作减少，决策工作更集中

**产品经理先改变产物。**AI可以整理反馈、草拟用户故事和生成原型。德勤将这些列为产品经理及相邻角色的增强任务。产品经理的长期价值，则在于确定值得解决的问题，并验证客户是否真正获益。[35]

**项目经理要从报表转向协调。**当代理能够整理状态和分流问题单，单纯追踪进度的价值会降低。但跨系统依赖、资源冲突和业务承诺仍需要协调。Hays报告显示，中国大陆项目与变革类岗位在2024年同比回升33%，企业整合AI和更新旧基础设施，是重要需求背景。[36]

**工程管理更重责任设计。**经理可以管理更多由AI增强的工程活动，却也要面对更快的代码流入和更复杂的审查。谁授权代理、谁接受风险、谁负责事故，必须在流程中明确。否则，团队人数减少，可能伴随责任和认知负荷过度集中。

**新岗位围绕落地形成。**工信部列出的新方向，包括生成式AI系统应用员、测试员、智能体开发、技能包和知识图谱建设、模型运营。前线部署工程师则深入客户现场，完成产品适配和交付。这些工作共同要求软件能力与行业知识结合。[4]

**本节的判断是：**风险更集中于“只负责执行”的任务组合；更有韧性的能力，是理解目标、组织系统并对结果作出可信判断。

本节参考文献：
[35] 德勤工程角色分析 <https://www.deloitte.com/us/en/industries/tmt/articles/ai-software-development-engineering-roles-being-rewritten.html> 摘录：“If we have selected the wrong experience for you, please change it above. As the evol…”
[36] Hays技术招聘报告 <https://www.haysplc.com/media/press-releases/2025/china-sees-shift-in-tech-hiring> 摘录：“全球领先的招聘及劳动力解决方案专家瀚纳仕（Hays）近期发布报告，深入研究了人工智能对技术领域职场的变革性影响。 报告对关键技术岗位受人工智能影响的程度进行了排名，100…”
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“2026年9月11日，工业和信息化部举行《 人工智能+软件 专项行动实施方案》新闻发布会。 工业和信息化部信息技术发展司副司长王威伟、中国软件行业协会副理事长兼秘书长吕卫…”

## 六、全球与中国：市场扩张和岗位压力为何可以并存

本节参考文献：
[35] 德勤工程角色分析 <https://www.deloitte.com/us/en/industries/tmt/articles/ai-software-development-engineering-roles-being-rewritten.html> 摘录：“If we have selected the wrong experienc…”
[36] Hays技术招聘报告 <https://www.haysplc.com/media/press-releases/2025/china-sees-shift-in-tech-hiring> 摘录：“人工智能正在迅速重塑就业市场，导致某些岗位需求量减少，而另一些则崭露头角。 根…”
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“同时也要清醒看到，新技术创造的增量岗位不是简单的等量置换存量岗位，重复性基础工…”

### 软件市场仍在增长，但增长不等于人人受益

**行业需求没有简单消失。**Gartner于2025年1月预测，全球软件支出从2024年的1.091569万亿美元，增至2025年的1.246842万亿美元，增幅约14.2%。中国2025年软件业务收入为15.4831万亿元，同比增长13.2%。两者分别是全球支出预测和中国企业营收统计。[40][41]

| 指标 | 全球 | 中国大陆 | 时期与口径 |
|---|---|---|---|
| 软件整体规模 | 1.246842万亿美元 | 15.4831万亿元人民币 | 2025年；支出预测／业务收入 |
| AI Agent子市场 | 726.1亿元人民币 | 180.9亿元人民币 | 2025年；同报告市场估计 |
| Agent年复合增速 | 58.0% | 71.5% | 2025—2030年预测 |
| Agent的2030年规模 | 约7,150亿元人民币 | 约2,684亿元人民币 | 按上述基期与增速估算 |

Agent数据来自沙利文2026年8月白皮书。[42]

**窄市场更适合对照。**表中的Agent规模使用同一报告和同一货币，比软件整体规模更适合做方向比较。2030年数值的估算为：全球726.1×1.58⁵≈7,150亿元，中国180.9×1.715⁵≈2,684亿元。它们是延续该报告五年增速的结果，不是整个软件行业收入。

**市场增长会换地方。**德勤预计，应用软件市场到2030年可能达到7,800亿美元。高盛研究则估计，客户服务软件相对于没有生成式AI推动的情景，到2030年可能额外扩大20%—45%。前者是应用软件子市场，后者是特定场景的增量预期。[5][43]

**安全和运行需求也会增长。**Gartner在2025年7月预计，全球信息安全支出2025年约2,130亿美元，2026年约2,400亿美元。中国信通院则估计，全球公共云IaaS市场从2024年的1,717.55亿美元，可能增至2029年的4,989.93亿美元，年复合增速约23.8%。[44][45]

**算力扩张只是必要底座。**中国信通院测算，截至2025年6月，中国计算设备算力为962 EFlops，全球约占21%；国内智能算力为782 EFlops，占约81%。这些按设备和浮点计算口径估算的能力，支持AI扩散，但不直接表示软件企业已经采用，更不直接表示生产率。[45]

本节参考文献：
[40] Gartner软件支出预测 <https://www.gartner.com/en/newsroom/press-releases/2025-01-21-gartner-forecasts-worldwide-it-spending-to-grow-9-point-8-percent-in-2025> 摘录：“Title: Gartner Forecasts Worldwide IT Spending to Grow 9.8% in 2025…”
[41] 中国2025年软件业统计 <https://www.miit.gov.cn/jgsj/yxj/xxfb/art/2026/art_32ce37ee09174bc0bf7add25ebeeb122.html> 摘录：“2025年，我国软件和信息技术服务业（以下简称 软件业 ）运行态势良好，软件业务收入稳健增长，利润总额增势放缓，软件业务出口保持正增长。…”
[42] 全球及中国Agent市场 <https://www.frostchina.com/content/insight/detail/6a7d2f6d3e2ee3f932bac82c> 摘录：“2026年8月，弗若斯特沙利文（Frost & Sullivan，以下简称 沙利文 ）正式发布《全球及中国AI数据服务市场发展白皮书(2…”
[5] 德勤软件行业展望 <https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/software-industry-outlook.html> 摘录：“Gartner® predicts that, forty percent of enterprise applications wil…”
[43] 高盛客户服务软件估计 <https://www.goldmansachs.com/insights/articles/ai-agents-to-boost-productivity-and-size-of-software-market> 摘录：“The next milestone in the development of generative artificial intel…”
[44] 信息安全支出预测 <https://www.gartner.com/en/newsroom/press-releases/2025-07-29-gartner-forecasts-worldwide-end-user-spending-on-information-security-to-total-213-billion-us-dollars-in-2025> 摘录：“DOCTYPE HTML html lang= en head script type= text/javascript src= v=…”
[45] 中国信通院算力蓝皮书 <https://www.caict.ac.cn/kxyj/qwfb/bps/202603/P020260306392232241580.pdf> 摘录：“联想、浪潮、曙光以44 台、28 台、8 台超算位列我国超算制造厂商 6基础算力规模按照我国近6 年服务器算力总量估算。 我国基础算力=…”

### 中国产业更偏服务，AI扩散会沿不同环节传导

**中国规模与利润分化。**工信部数据显示，2025年软件业务收入154,831亿元，利润18,848亿元，出口627.3亿美元。收入同比增长13.2%，利润增长7.3%，出口增长7.7%。行业扩张并没有同比例转化为利润增长。[41]

**半年数据继续显示分化。**2026年上半年，软件业务收入77,182亿元，同比增长9.5%；利润8,999亿元，同比增长1.0%；出口337.9亿美元，同比增长11.4%。这些变化反映经营表现，不能仅凭时间上的重合就归因于AI。[46]

| 中国软件收入类别 | 2025年收入 | 同比增速 | 占行业收入 | AI影响的主要方向 |
|---|---|---|---|---|
| 软件产品 | 32,361亿元 | 10.4% | 20.9% | 功能智能化、产品整合 |
| 信息技术服务 | 106,366亿元 | 14.7% | 68.7% | 集成、运营与结果服务 |
| 信息安全产品和服务 | 2,235亿元 | 6.7% | 约1.4% | 自动检测与代理治理 |
| 嵌入式系统软件 | 13,869亿元 | 9.3% | 约9.0% | 终端智能化、软硬协同 |

上述四类收入合计154,831亿元；基础软件、工业软件及云服务属于其中的子项。[41]

**服务结构影响替代方式。**信息技术服务占比68.7%，意味着大量价值来自系统连接、客户适配和持续运营。标准化实施环节会承受降价压力，但行业知识、数据治理和现场交付又可能形成新需求。中国企业因此既面临人力密集模式的调整，也有向高价值服务转型的机会。

**工业知识是另一种壁垒。**2025年中国基础软件产品收入2,146亿元，工业软件产品收入3,330亿元。政策推动CAD、CAE、EDA与AI融合，并将工艺参数和工业经验封装为模型库、组件。这类机会要求可靠性和领域知识，不只是更便宜的通用代码生成。[4]

**区域影响不会平均。**2025年东部地区占中国软件业务收入83.1%；京津冀和长三角分别占26.7%、28.9%。人才、客户和软件收入的集中，使工具扩散、岗位竞争与新服务机会，也更容易在这些集群率先出现。[41]

本节参考文献：
[41] 中国2025年软件业统计 <https://www.miit.gov.cn/jgsj/yxj/xxfb/art/2026/art_32ce37ee09174bc0bf7add25ebeeb122.html> 摘录：“2025年，我国软件和信息技术服务业（以下简称 软件业 ）运行态势良好，软件业务收入稳健增长，利润总额增势放缓，软件业务出口保持正增长。 2025年，我国软件业务收入154831亿元，同比增长13.2%。 软件业利润总额18848亿元，同比增长7.3%。 软件业务出口627.3亿美元，同比增长7.7%，增速连续…”
[46] 2026年上半年运行情况 <https://www.miit.gov.cn/jgsj/yxj/xxfb/art/2026/art_d9504b5e12ef4fce9c86de1d1d0548f9.html> 摘录：“2026年上半年，我国软件和信息技术服务业（以下简称 软件业 ）运行态势良好，软件业务收入稳健增长，利润总额增势放缓，软件业务出口保持正增长。 上半年，我国软件业务收入77182亿元，同比增长9.5%。 软件业利润总额8999亿元，同比增长1.0%。 软件业务出口337.9亿美元，同比增长11.4%。 上半年，…”
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“2026年9月11日，工业和信息化部举行《 人工智能+软件 专项行动实施方案》新闻发布会。 工业和信息化部信息技术发展司副司长王威伟、中国软件行业协会副理事长兼秘书长吕卫锋、中国电子信息产业发展研究院副院长朱敏、开放原子开源基金会副秘书长李博出席发布会，介绍 人工智能+软件 专项行动有关情况并回答记者提问。 本…”

### AI采用已经广泛，但“用过”和“自主生产”差得很远

**采用率必须带分母。**开发者调查、一般职场调查和企业部署预测，回答的是不同问题。最贴近软件工作的对照，是开发者是否经常使用工具；更高一级的企业流程自主化，还需要另看生产部署。

| 地区与样本 | 指标 | 数值 | 数据时期 | 来源 |
|---|---|---|---|---|
| 全球开发者受访者 | 使用或计划使用AI工具 | 84% | 2025年 | Stack Overflow |
| 全球专业开发者 | 每日使用AI工具 | 51% | 2025年 | Stack Overflow |
| 中国开发者受访者 | 每日使用智能开发工具 | 48.6% | 2024年 | CSDN，信通院指南引述 |
| 中国大陆在职受访者 | 工作中使用AI工具 | 52% | 2025年 | Hays |
| 中国大陆在职受访者 | 接受过相关培训 | 31% | 2025年 | Hays |

全球调查来自177个国家的49,000多份回答；中国开发者数据由2024年智能开发指南引述。[39][47][36]

**全球工具普及不等于代理普及。**Stack Overflow同一调查中，52%的开发者尚未使用Agent，或只使用较简单工具；38%没有采用计划。对于已经使用代理的人，约70%认为特定任务耗时下降，69%认为生产率提高，但只有17%认为团队协作改善。[39]

**信任决定监督成本。**该调查中，46%不信任AI准确性，33%信任，只有3%高度信任。66%最困扰的是“几乎正确但不完全正确”的结果。由此，采用越广并不必然意味着审查越少，反而可能增加验证需求。

**中国培训是重要变量。**Hays报告还显示，未使用AI的中国大陆受访者中，60%提到缺乏理解、培训或支持；94%的受访者愿意学习AI工具。工具供应之外，组织是否给予训练和有效使用场景，会影响实际收益。[36]

本节参考文献：
[39] 开发者信任调查 <https://survey.stackoverflow.co/2025/> 摘录：“The 2025 Developer Survey is the definitive report on the state of software development. In its fifteenth year, Stack Overflow received…”
[47] 中国智能开发指南 <https://res-static.hc-cdn.cn/cloudbu-site/intl/zh-cn/about/whitepapers/1732092240930973657.pdf> 摘录：“（二）软件服务业案例 39 （三）电力行业案例 41 （四）金融行业案例 42 （五）制造行业案例 44 智能化软件开发落地实践指南 图1 软件工程发展历程图 02 图2 软件工程3.0 示意图 03 图3 智能开发落地步骤图 11 图4 企业智能化能力自我诊断等级图 11”
[36] Hays技术招聘报告 <https://www.haysplc.com/media/press-releases/2025/china-sees-shift-in-tech-hiring> 摘录：“全球领先的招聘及劳动力解决方案专家瀚纳仕（Hays）近期发布报告，深入研究了人工智能对技术领域职场的变革性影响。 报告对关键技术岗位受人工智能影响的程度进行了排名，100 分表示受影响最大，0 分表示受影响最小。 人工智能正在迅速重塑就业市场，导致某些岗位需求量减少，而另…”

### 全球就业仍有增长预测，结构性冲击已经出现

**全球预测并非软件灭失。**世界经济论坛《2025年未来就业报告》预计，到2030年，各类宏观趋势将创造1.70亿个正式岗位，替代9,200万个，净增7,800万个。软件和应用开发者属于增长职业。这里的总数覆盖多行业，不能全部归于AI。[48]

**AI自身也有双向作用。**WEF对“AI与信息处理技术”的单独预测，是创造1,100万个岗位，同时替代900万个。这与总体净增7,800万个并非同一统计范围。它说明技术可以减少某些工作，同时增加互补活动。

**美国官方仍预计增长。**BLS预计，软件开发者、质量保证分析师和测试员合计就业，从2025年的1,905,400人，增至2035年的2,090,800人，整体约增长10%。下表增量和增幅按公布端点计算。[49]

| 美国职业 | 2025年就业 | 2035年预测 | 净增量 | 按端点计算增幅 |
|---|---|---|---|---|
| 软件开发者 | 1,717,800人 | 1,892,600人 | 174,800人 | 约10.2% |
| QA分析师与测试员 | 187,600人 | 198,200人 | 10,600人 | 约5.7% |
| 合计 | 1,905,400人 | 2,090,800人 | 185,400人 | 约9.7% |

**岗位空缺不全是净新增。**BLS预计，这些职业在2025—2035年平均每年约有106,100个空缺，其中包括转职和退休带来的替补。十年净增185,400人，平均每年约18,540人；两者的差别，正体现了岗位流动与净增长的区别。

**增长预测也会调整。**BLS另一篇2026年文章，使用的是2024—2034年预测，软件开发者增幅为15.8%。它与2025—2035年预测的窗口不同。两组预测应分别阅读，不能把差额直接解释为AI造成的就业损失。[50]

**现实增长已有放缓。**Crane与Soto在2026年3月的FEDS工作论文中，将职业任务数据与美国劳动力调查连接。研究认为，编程密集职业在ChatGPT出现后就业增速显著放缓，即使控制行业冲击也存在这一现象。不过，编码职业就业仍在增长。[51]

**总量与初级岗位可能分化。**Stanford SIEPR在2026年的综述指出，应届毕业生面临较困难的市场，部分AI暴露职业的早期职业就业下降。同时，利率上升、疫情时期过度招聘和远程工作，也影响同一时期的就业变化。[52]

本节参考文献：
[48] WEF就业展望 <https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/2-jobs-outlook/> 摘录：“Title: The Future of Jobs Report 2025 Markdown Content: Jobs outlook Technological change, the green t…”
[49] BLS职业预测 <https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm> 摘录：“Title: Software Developers, Quality Assurance Analysts, and Testers Markdown Content: Bureau of Labor…”
[50] BLS较早预测窗口 <http://www.bls.gov/opub/ted/2026/artificial-intelligence-information-technology-and-employment-2024-34.htm> 摘录：“Title: Artificial intelligence, information technology, and employment, 2024–34 : The Economics Daily…”
[51] FEDS编码职业研究 <https://doi.org/10.17016/feds.2026.018> 摘录：“Finance and Economics Discussion Series (FEDS) AI and Coder Employment: Compiling the Evidence Crane a…”
[52] SIEPR劳动力市场综述 <https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality> 摘录：“What is really happening to jobs? Separating AI hype from reality Key takeaways - AI’s effects on over…”

### 中国招聘显示：基础岗位承压，AI和复合型需求扩张

**招聘变化已经明显。**Hays的职位需求图谱显示，中国大陆软件开发岗位需求在2022年初至2024年底下降71%。同一报告也讨论了经济和预算压力，以及企业对人才结构的重新部署。该指标衡量招聘需求，不是全国软件从业人数减少71%。[36]

**新增需求集中于新能力。**China Daily于2026年3月11日转述脉脉报告：2026年1—2月，新经济行业新发岗位同比增长12.77%，AI岗位同比增加约12倍。AI岗位占比从上年同期2.29%升至26.23%，既有需求扩张，也有较低基数的影响。[53]

**经验门槛同步提高。**同一平台中，超过七成新岗位要求三年以上经验；三至五年经验岗位量同比增长19%，一年以内经验岗位约减少20%。明确要求AI或大模型技能的岗位描述占34.39%，上年同期为22.35%。对初级求职者而言，压力来自机会减少，也来自要求升级。

**更长数据也显示分化。**Zhang等在2026年8月版本的研究中，分析中国智联招聘2018年1月至2024年5月约125万条职位。其工具变量估计显示，职业LLM暴露增加一个标准差，与新职位份额下降约2.3个百分点相联系，同时教育和经验要求提高。[54]

**暴露反映任务重叠。**LLM暴露指技术能力与职业任务的重合程度，不等于已实现替代。上述份额系数也是模型估计，不是对每个职业直接减去2.3个百分点的预测。研究中部分下降趋势早于ChatGPT，因此不能将整个长期变化归于生成式AI。

本节参考文献：
[36] Hays技术招聘报告 <https://www.haysplc.com/media/press-releases/2025/china-sees-shift-in-tech-hiring> 摘录：“全球领先的招聘及劳动力解决方案专家瀚纳仕（Hays）近期发布报告，深入研究了人工智能对技术领域职场的变革性影响。 报告对关键技术岗位受人工智能影响的程度进行了排名，100 分表示受影响最大，0 分表示受影响最小。…”
[53] 脉脉招聘报告转述 <http://cn.chinadaily.com.cn/a/202603/11/WS69b14058a310942cc49a2a17.html> 摘录：“近日，职场社区平台脉脉发布《社交求职——2026年1-2月中高端人才求职招聘洞察》（以下简称《洞察》）。 《洞察》显示，2026年1-2月，招聘市场整体回暖。 新经济行业岗位量增长12.77%。 AI人才争夺成招…”
[54] 中国任务暴露研究 <https://econhangyu.com/files/publications/2025-ai-exposure-china-EN.pdf> 摘录：“The Measurement of AI Exposure and Its Impact on Labor Demand in China: Evidence from Large Language Models”

### 薪资不会统一上涨，也不会统一下降

**美国工资反映职业分工。**BLS给出的2025年5月中位年薪，软件开发者为135,980美元，QA分析师和测试员为104,300美元。它们是美国职业工资水平，不是AI带来的工资增幅。[49]

**中国AI招聘有溢价。**脉脉报告中，新经济岗位平均月薪从2025年同期44,124元，升至2026年1—2月48,189元，约增长9.2%。AI岗位平均月薪60,738元，比同期整体均值高约26%；平台供需比为0.97，整体为1.79。[53]

**溢价可能来自岗位组合。**AI岗位可能要求更高学历、经验或承担更大责任，因此不能把26%的差距解释为“同一个人学会AI就加薪26%”。但它仍表明，招聘端愿意为某些AI与业务结合能力支付更高价格。

**工资方向取决于稀缺性。**如果AI使一种技能更容易获得，该技能价格可能下降。如果AI扩大产出，同时使架构、安全或领域判断成为瓶颈，这些互补能力可能更稀缺。行业平均工资还会受到初级岗位占比变化影响，不能只看留下人员的均薪。

本节参考文献：
[49] BLS职业预测 <https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm> 摘录：“Title: Software Developers, Quality Assurance Analysts, and Testers Markdown Content: Bureau of Labor Statistic…”
[53] 脉脉招聘报告转述 <http://cn.chinadaily.com.cn/a/202603/11/WS69b14058a310942cc49a2a17.html> 摘录：“近日，职场社区平台脉脉发布《社交求职——2026年1-2月中高端人才求职招聘洞察》（以下简称《洞察》）。 《洞察》显示，2026年1-2月，招聘市场整体回暖。 新经济行业岗位量增长12.77%。 AI人才争夺成招聘主战场，…”

### 政策和产业结构，让全球与中国出现不同路径

**全球环境不是单一路线。**国际AI安全报告记录，欧盟《人工智能法案》于2024年生效，2025年进一步形成通用AI行为准则。透明度、版权、安全评测和事件报告，会影响软件厂商如何开发与部署产品。[12]

**中国兼顾推广与改造。**国务院2025年8月的意见提出，新一代智能终端、智能体等应用普及率，到2027年超过70%，2030年超过90%，并展望2035年的智能经济和智能社会。这些是政策目标，不是开发者已观测采用率。[55]

**软件政策更具体到企业。**2026年9月11日发布的专项行动提出，到2028年推广覆盖2万家规模以上软件企业，累计实施100项智能化技改，打造100个智能体标杆应用，孵化五个以上重点开源项目。到2030年，目标是关键软件全面智能化升级。[4]

| 比较维度 | 全球主要表现 | 中国相关特点 | 与替代趋势的关系 |
|---|---|---|---|
| 产业需求 | AI、企业平台、云与安全扩张 | 信息技术服务占68.7% | 替代执行，也增加集成与运营 |
| 采用路径 | 开发者工具与平台生态扩散 | 企业技改、行业应用与开源推动 | 扩散速度取决于组织能力 |
| 就业信号 | 美国预测增长，初级承压 | 招聘分化，AI技能要求提高 | 总量与岗位结构可不同向 |
| 政策环境 | 多地区监管与市场投资并行 | 明确推广目标与就业友好要求 | 治理、培训与部署共同作用 |

**地区差异来自任务组合。**中国服务收入占比较高，意味着客户适配、实施和运行工作更重要。全球大型平台则可能通过代理生态整合轻量产品。两边都会压缩标准化执行，但价值增量可能分别体现为行业交付、平台治理或产品整合。

**本节的判断是：**市场扩张、企业利润承压和初级招聘收缩，可以同时发生；中国与全球的替代趋势，应通过产业结构和任务组合解释，而非只比较一个采用率。

本节参考文献：
[12] 国际人工智能安全报告 <https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026-zh.pdf> 摘录：“2025 年， 12 家公司发布或更新了前沿人工智能安全框架 - 这 些文件阐述了它们在构建更强大模型时如何管理风险的计划。 大多数风险管理举措仍属自愿性 质， 但一些司法管辖区已开始将某些实践正式纳入法律 要求。 本报告评估了通用型人工智能系统的能力范围、 其带 来…”
[55] 国务院 人工智能+ 意见 <http://www.scio.gov.cn/zdgz/jj/202509/t20250901_928364.html> 摘录：“Title: 国务院关于深入实施 人工智能+ 行动的意见_中华人民共和国国务院新闻办公室 Markdown Content: 国务院关于深入实施 人工智能+ 行动的意见 各省、自治区、直辖市人民政府，国务院各部委、各直属机构： 为深入实施 人工智能+ 行动，推动人工智…”
[4] 工信部人才与就业问答 <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 摘录：“2026年9月11日，工业和信息化部举行《 人工智能+软件 专项行动实施方案》新闻发布会。 工业和信息化部信息技术发展司副司长王威伟、中国软件行业协会副理事长兼秘书长吕卫锋、中国电子信息产业发展研究院副院长朱敏、开放原子开源基金会副秘书长李博出席发布会，介绍 人工智能…”

## 七、生产率如何影响就业：关键在需求能否跟上

**提效不等于同比裁员。**假设质量相同、工时相同，生产率提高26%，意味着原来一人的产出，现在相当于1.26人的原有产出。在产出完全不变的条件下，所需劳动变为原来的1÷1.26≈79.4%，即减少约20.6%，而不是26%。这里用现场实验的26%作为计算锚点，是条件估算。

**就业由两个量共同决定。**在质量和统计范围保持一致的简化条件下，劳动需求等于所需产出除以劳动生产率。这个关系可以说明阈值，但不能替代实际就业预测。

\[
\frac{N_1}{N_0}=\frac{Q_1/Q_0}{P_1/P_0}
\]

其中，\(N\)是劳动投入，\(Q\)是合格产出，\(P\)是单位劳动的合格产出。

| 条件情景 | 生产率变化 | 合格产出变化 | 劳动需求计算 | 结果 |
|---|---|---|---|---|
| 需求不扩张 | 提高26% | 不变 | 1÷1.26 | 约为原来的79.4% |
| 需求同步扩张 | 提高26% | 提高26% | 1.26÷1.26 | 与原来相同 |
| 需求扩张更快 | 提高26% | 增幅超过26% | 大于1.26÷1.26 | 高于原来 |

**成本下降可以释放需求。**原本不值得开发的小型工具、行业应用和定制流程，可能在成本下降后变得经济可行。企业因此可能用同样团队开发更多产品，也可能用更多团队服务更多客户。OECD将这类需求扩张，列为抵消任务替代的重要机制。[1]

**需求反弹不是必然。**如果客户预算固定、软件功能已饱和，或新增产品难以获得用户，提效就更容易转为降价和人员压缩。反之，若大量未满足需求越过经济可行门槛，行业劳动需求可能扩大。决定结果的不是“代码更便宜”这一条事实，而是客户是否愿意购买更多有价值的软件。

**质量成本影响真实提效。**生成速度提高后，如果评审、返工和维护相应增加，单位合格产出的生产率可能远低于代码量增幅。因此，上述算式中的生产率，必须使用质量调整后的交付指标，不能直接塞入代码行数或建议接受率。

**收益分配还影响工资。**生产率提高产生的价值，可以成为客户降价、企业利润、员工工资，也可以用于研发扩张。竞争强度、人才稀缺性和议价能力，决定谁获得更大份额。技术提升本身，并没有规定所有员工都加薪。

**群体差异需要关注。**OECD研究指出，受教育程度较低、年长和部分女性劳动者，获得AI工具与相关工作机会的渠道可能较少。这里的风险不仅是任务被替代，也包括没有机会使用增强生产率的工具。[56]

**本节的判断是：**决定净就业的，是合格产出需求、真实生产率和新增任务共同变化；结构性冲击比一个统一的行业裁员比例更值得提前应对。

本节参考文献：
[1] OECD劳动需求分析 <https://www.oecd.org/en/publications/oecd-employment-outlook-2023_08785bba-en/full-report/artificial-intelligence-and-jobs-no-signs-of-slowing-labour-demand-yet_5aebe670.html> 摘录：“Policies to reach full employment may have the added benefit of helping automation technologies translate into higher productivity gains and stronger labour demand, although such a policy goal is not without risks (see Chapter 1). Antitrust regulation can bolster the benefits of AI. One w…”
[56] OECD不同劳动者群体研究 <https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/10/who-will-be-the-workers-most-affected-by-ai_fb7fcccd/14dc6f89-en.pdf> 摘录：“technologies) 56 Figure A A.2. Male, lower-educated and foreign-born workers are at higher risk of automation 58 Tertiary-educated, prime-age and native-born workers are overrepresented in the five occupations most exposed to AI (2022 data) 20 Estimated link between AI exposure and employ…”

## 八、2026—2036年的三种情景，以及判断何时改变

**主情景是协作扩张。**未来十年更适合按条件分支理解，而非设定一个“程序员消失年份”。以下数字分别来自任务结构预测、行业生产率预测和生产部署调查，不能互换为岗位替代率。

| 情景 | 数字锚点 | 关键驱动 | 软件行业结果 | 岗位结构 |
|---|---|---|---|---|
| 基准：任务重组 | 2030年任务约32%／34%／34%，示意估算 | 能力提高，工程约束持续 | 产品与服务继续增长 | 人机协作、职责扩展 |
| 上行：AI原生扩张 | 全生命周期生产率潜在提高30%—35% | 独立验证成熟、成本下降、需求释放 | 更多应用进入经济可行区 | 小型复合团队与新岗位增加 |
| 受阻：局部提速 | 2025年亚太PoC转生产34.5% | 集成、质量、安全与回报受限 | 试点多，规模收益有限 | 人工审查与运行保障保持重要 |

任务结构依据WEF，生产率上行情景依据德勤，部署数据依据IDC。[48][5][8]

本节参考文献：
[48] WEF就业展望 <https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/2-jobs-outlook/> 摘录：“Image 5: Job growth and decline (number of employees), 2025-2030 ( Job…”
[5] 德勤软件行业展望 <https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/software-industry-outlook.html> 摘录：“Gartner® predicts that, forty percent of enterprise applications will b…”
[8] IDC企业应用分析 <https://www.idc.com/resource-center/blog/ai%E6%AD%A3%E5%9C%A8-%E6%9D%80%E6%AD%BB-saas%EF%BC%9F%E6%88%96%E8%AE%B8%E8%AF%A5%E6%8D%A2%E4%B8%AA%E6%80%9D%E8%B7%AF/> 摘录：“随着生成式AI、大模型及Agent能力持续演进，围绕 AI是否会取代SaaS 的讨论正在快速升温。 基于当前企业采用进度、软件支出变化、AI规…”

### 基准情景：人类独立执行减少，协作成为常态

**任务份额有一个参考。**WEF调查的2025年基线是，人单独完成约47%的任务，技术单独完成22%，人机共同完成30%。报告预计，到2030年三者接近均分。由于原始比例取整，2025年三项合计为99%。

**示意估算不是软件预测。**若按报告所述，人类独立任务份额下降约15个百分点，则47%−15%=32%。再将剩余68%近似均分，可得技术独立与人机协作各34%。表中的32%／34%／34%，只是对全球任务结构预期的透明示意。

**份额下降不等于工作量下降。**如果任务总量扩大，人类单独任务所占比例变小，绝对工作量仍可能增加。软件尤其可能出现更多产品、接口和定制需求。岗位变化将集中体现为，从直接实现转向目标设定、集成、验证和运营。

本节参考文献：
[48] WEF就业展望 <https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/2-jobs-outlook/> 摘录：“By combining respondents’ job growth and decline exp…”
[5] 德勤软件行业展望 <https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/software-industry-outlook.html> 摘录：“Gartner® predicts that, forty percent of enterprise…”
[8] IDC企业应用分析 <https://www.idc.com/resource-center/blog/ai%E6%AD%A3%E5%9C%A8-%E6%9D%80%E6%AD%BB-saas%EF%BC%9F%E6%88%96%E8%AE%B8%E8%AF%A5%E6%8D%A2%E4%B8%AA%E6%80%9D%E8%B7%AF/> 摘录：“随着企业客户从模型试点走向业务落地，从当前市场需求变化看，企业对软件平台的要求，正在从基础数字化和AI集…”

### 上行情景：可靠执行与新需求形成正反馈

**上行需要全流程改善。**德勤预计，AI如果贯穿需求、编码、测试、部署和监控，可能使软件开发全生命周期生产率提高30%—35%。其前提是流程整合，而非仅让编码环节更快。[5]

**组织变化可能先于行业收缩。**同一展望引述，2026年底40%的企业应用可能集成任务型Agent，2030年80%的组织可能转向更小的AI增强工程团队。即使这些预测实现，也可能表现为单团队更小、团队数量更多，而非行业就业按同样比例减少。

**新需求是上行的关键。**当软件便宜到足以服务更多中小企业和细分场景，需求可能吸收生产率提高。代理构建、评测、安全和行业交付，也会形成新任务。但若收益只集中在少数平台，市场扩大仍可能伴随部分厂商和劳动者处境恶化。

本节参考文献：
[5] 德勤软件行业展望 <https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/software-industry-outlook.html> 摘录：“Gartner® predicts that, forty percent of enterprise applications will be integrated with task-specific AI agents by the end of 2026, up from less than 5% today (2025).4…”

### 受阻情景：生成很快，生产价值兑现较慢

**从试点到生产会损耗。**IDC报告，2025年亚太企业平均每年开展17.9个生成式AI概念验证项目，其中34.5%进入生产；进入生产的服务中，36.8%达到预期业务指标。PoC即概念验证，主要检验技术和场景是否可行。[8]

**两道门槛可以条件计算。**如果上述比例适用于同一项目队列，最终投产且达标的占比估算为34.5%×36.8%≈12.7%。这是条件化流程计算，不是IDC直接统计的总体成功率。它说明试点表现良好，与大规模商业回报之间还有距离。

**受阻不代表技术停步。**模型仍可改善，但组织需要支付集成、权限、安全和培训成本。若这些成本抵消了生成端收益，企业就会保留较多人类监督。DORA的交付稳定性关联、维护研究和独立验证失败案例，都指出了这类风险通道。

**判断由实际结果决定。**更大范围岗位替代的判断，应在以下条件同时出现时上调：代理跨组织、跨仓库长期稳定交付；独立测试确认质量与安全不恶化；纠正性维护和人工审查需求下降；权限与责任可追溯；并且在控制宏观和需求变化后，软件劳动需求仍持续收缩。反之，若新增需求扩大，或验证与维护成本持续较高，协作和岗位重组就仍是更合适的主判断。

**本节的判断是：**能力增长决定自动化上限，可靠性与商业回报决定采用速度，需求和人才适应决定最终就业结果。

本节参考文献：
[8] IDC企业应用分析 <https://www.idc.com/resource-center/blog/ai%E6%AD%A3%E5%9C%A8-%E6%9D%80%E6%AD%BB-saas%EF%BC%9F%E6%88%96%E8%AE%B8%E8%AF%A5%E6%8D%A2%E4%B8%AA%E6%80%9D%E8%B7%AF/> 摘录：“随着生成式AI、大模型及Agent能力持续演进，围绕 AI是否会取代SaaS 的讨论正在快速升温。 基于当前企业采用进度、软件支出变化、AI规模化落地情况以及企业工作方式转型趋势的综合观察，IDC的判断是：AI不会在中短期内取代SaaS，但将推动SaaS进入新一轮结构性重构周期。 企业软件市场未来的主要变化，不是SaaS的消失，而是SaaS从 功能交付工具 向 智能执行平台 演进。 当前，AI与SaaS之间并非替代关系，而更接近于 能力叠加 与 价值重定义 关系。 随着企业客户从模型试点走向业务落地，从当前市场需求变化看，企业对软件平台的要求，正在从基础数字化和AI集成能力，…”

## 九、从业者、管理者和决策者该如何理解这些变化

**个人要证明独立判断。**求职者不必把目标设成“写得比AI快”，而应证明自己能解释代码、定位错误、设计测试，并把功能接入真实系统。作品的价值，更多在于清楚说明需求、取舍、验证和修复过程，而不只是展示生成的界面。

**团队要保护验证能力。**高级工程师和管理者需要避免一种局面：代码产出快速增长，但理解系统的人越来越少。独立测试、代码审查和事故复盘，既是质量机制，也是组织保持工程知识的方式。

| 适用对象 | 先拆分任务 | 建立验证 | 补足能力或组织 | 重点看结果 |
|---|---|---|---|---|
| 求职者与初级开发 | 生成、调试、集成、沟通 | 独立运行并解释测试 | 基础工程与领域知识 | 掌握度、独立交付、返工 |
| 高级开发与安全人员 | 划定可委派边界 | 沙盒、审查、回滚、审计 | 系统设计与代理监督 | 稳定性、漏洞与维护负担 |
| 产品、项目与工程经理 | 区分人、代理及协作任务 | 明确验收与升级责任 | 跨职能协调、培训与带教 | 客户价值、交付与人才结构 |
| 企业与行业决策者 | 优先低风险重复流程 | 数据权限与独立评测 | 平台、治理及就业转型支持 | 单位合格交付成本和长期回报 |

**企业不宜只算省下的人。**AI投资回报还包括新增客户、交付质量、运行费用和长期维护。若用代码行数或工具使用率考核团队，容易鼓励生成更多，而不是交付更好。对服务型企业而言，能否从出售工时转向可重复的行业能力，也会影响利润和竞争力。

**政策重点应兼顾转换。**中国的软件专项行动，已经将企业智能化、岗位改造、技能培训和就业友好发展放在同一安排中。更有价值的产业结果，不只是推广多少工具，还包括新服务是否形成、初级人员能否成长，以及中小企业能否获得可靠能力。[6]

**证据口径需统一理解。**本文判断截止2026年9月13日。官方统计用于收入和职业规模，随机及有控制现场实验对特定任务效果的证据较强；纵向观察和问卷居中，客户自报与市场预测用于说明案例或情景。全球支出、中国营收、美国就业和平台招聘各有不同分母；代码量、PR、质量和工资分别解读。文中Agent规模、任务份额及劳动需求换算均标为估算，高中低等级属于定性分析，政策数字属于目标。

**最终结论是价值重排。**AI会替代大量软件执行任务，也可能让某些岗位和企业失去原有位置。但未来十年更值得把握的，不是“软件还存不存在”，而是价值从哪里转向哪里：从手工实现，转向定义问题、连接系统、验证质量，并持续交付可信结果。

本节参考文献：
[6] 中国软件专项行动 <https://www.gov.cn/zhengce/zhengceku/202609/P020260911688449695690.pdf> 摘录：“人工智能深刻变革软件和信息技术服务业的开发方式、 产品形态与服务模式，成为驱动产业升级的核心引擎。 入贯彻落实《国务院关于深入实施 人工智能+ 行动的意见》， 加快推进人工智能技术在软件和信息技术服务业融合应用， 重塑软件核心竞争力，促进软件和信息技术服务业高质量发 以习近平新时代中国特色社会主义思想为指导，深入贯 彻党的二十大和二十届历次全会精神，完整准确全面贯彻新 发展理念，坚持 应用牵引、创新驱动、安全可控、生态协 同 原则，加快以人工智能重塑软件和信息技术服务，以智 能编程驱动产业效能变革，协同推进软件产品智能化升级和 智能体软件培育，着力提升信息技术服务质量，夯实智能化 发展基础，营造良好发展环境，推动形成生产高效、产品智 能、服务普惠和生态完善的发展新局面，为建设现代化产业 体系提供坚实技术支撑和创新动能。 到2028 年，软件和信息技术服务业智能化水平显著提 升，培育一批高水平智能编程工具和智能开发平台，推广应 用覆盖2 万家规模以上软件企业，关键软件智能化升级取得 显著成效，累计组织实施100 项软件企业智能化技改项目， 以智能体软件为代表的软件新形态加速涌现，在重点行业打 造100 个智能体软件标杆应用，信息技术服务向智能化、价 值化跃升，形成一批行业深度应用解决方案和典型场…”

## 参考文献

[1] <https://www.oecd.org/en/publications/oecd-employment-outlook-2023_08785bba-en/full-report/artificial-intelligence-and-jobs-no-signs-of-slowing-labour-demand-yet_5aebe670.html> OECD劳动需求分析; OECD就业展望; OECD生产率与需求机制
[2] <https://arxiv.org/html/2409.18048v3> AI软件工程综述; 生命周期综述; 需求工程综述
[3] <https://openai.com/index/harness-engineering/> 代理优先工程案例; OpenAI工程案例; OpenAI内部工程案例; 代理运行机制
[4] <https://www.miit.gov.cn/xwfb/xwfbh/bxwfbh/art/2026/art_95c0b992336a4cb1b87ec3ccc576a669.html> 工信部人才与就业问答; 工信部能力结构判断; 智能软件服务方向; 工业软件两条路径; 智能服务模式; 软件智能体安全要求; 工信部人才问答; 中国软件新职业方向; 产业结构与工业软件方向; 软件专项行动目标
[5] <https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/software-industry-outlook.html> 德勤软件行业展望; 德勤软件盈利分析; 德勤组织趋势; 德勤应用软件展望; 德勤全生命周期展望; 德勤全流程生产率预测
[6] <https://www.gov.cn/zhengce/zhengceku/202609/P020260911688449695690.pdf> 中国软件专项行动; 工信部就业友好安排
[7] <https://openai.com/index/introducing-codex/> Codex产品说明
[8] <https://www.idc.com/resource-center/blog/ai%E6%AD%A3%E5%9C%A8-%E6%9D%80%E6%AD%BB-saas%EF%BC%9F%E6%88%96%E8%AE%B8%E8%AF%A5%E6%8D%A2%E4%B8%AA%E6%80%9D%E8%B7%AF/> IDC企业应用分析; IDC产品竞争分析; IDC生产部署观察; IDC试点与业务价值数据
[9] <https://github.com/features/copilot> Copilot产品与计费
[10] <https://www.idc.com/resource-center/blog/idc-futurescape-2026-%E5%8D%81%E5%A4%A7%E9%A2%84%E6%B5%8B%EF%BC%9Aai-%E6%AD%A3%E5%9C%A8%E5%A6%82%E4%BD%95%E9%87%8D%E5%A1%91%E4%B8%AD%E5%9B%BD%E4%BC%81%E4%B8%9A%E7%9A%84%E4%BA%91%E8%AE%A1%E7%AE%97/> IDC云计算预测
[11] <https://www.deloitte.com/content/dam/assets-zone1/cn/zh/docs/industries/technology-media-telecommunications/2026/cn-tmt-predictions-2026-saas-ai-agents.pdf> 德勤SaaS与智能体展望; SaaS商业模式预测
[12] <https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026-zh.pdf> 国际人工智能安全报告; 国际AI安全报告网络章节; 国际AI治理进展
[13] <https://report.iresearch.cn/report/202607/4848.shtml> 艾瑞企业级Agent报告
[14] <https://arxiv.org/html/2410.12944v2> Google随机试验; Google企业试验
[15] <https://www.bis.org/publications/working-paper-1208-generative-ai-and-labour-productivity-field-experiment-coding.pdf> BIS现场实验; CodeFuse资历比较
[16] <https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/> GitHub代码质量研究; GitHub受控质量实验
[17] <https://arxiv.org/html/2509.20353v2> NAV IT纵向研究; NAV IT采用者比较
[18] <https://link.springer.com/article/10.1007/s10664-026-10889-1> Borg等维护性研究; 软件维护性研究; Borg等研究
[19] <https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/> Accenture企业研究
[20] <https://dora.dev/ai/gen-ai-report/dora-impact-of-generative-ai-in-software-development.pdf> DORA生成式AI报告
[21] <https://doi.org/10.48550/arxiv.2605.23135> 工程师工作变化研究
[22] <https://www.devin.ai/customers/litera> Litera质量工程案例; Litera流程与人才变化
[23] <https://arxiv.org/abs/2607.09902> Xia纵向研究; 合并后维护研究
[24] <https://doi.org/10.48550/arxiv.2609.17598> AIDev代理比较; 五种代理实证研究; AIDev评审行为分析
[25] <https://doi.org/10.5281/zenodo.22551155> 受控交付研究; 独立验证实验
[26] <https://www.secrss.com/articles/87116> 工程项目复盘
[27] <https://openai.com/index/introducing-swe-bench-verified/> SWE-bench Verified说明
[28] <https://doi.org/10.48550/arxiv.2410.06992> SWE-Bench+研究
[29] <https://doi.org/10.48550/arxiv.2609.08149> 基准验证研究
[30] <https://www.ibm.com/cn-zh/think/insights/quality-assurance-in-software-testing-with-ai> IBM质量保证分析; IBM AI辅助QA分析
[31] <https://coding.net/solutions/code-quality> CODING质量流程; CODING合并门禁
[32] <https://support.claude.com/zh-CN/articles/11932705-claude-%E4%BB%A3%E7%A0%81%E4%B8%AD%E7%9A%84%E8%87%AA%E5%8A%A8%E5%8C%96%E5%AE%89%E5%85%A8%E5%AE%A1%E6%9F%A5> Claude Code安全审查说明
[33] <https://global.buaa.edu.cn/info/1038/4638.htm> DRMiner研究介绍
[34] <https://doi.org/10.48550/arxiv.2607.11348> 安全API编程研究
[35] <https://www.deloitte.com/us/en/industries/tmt/articles/ai-software-development-engineering-roles-being-rewritten.html> 德勤工程角色分析; 德勤角色任务分析
[36] <https://www.haysplc.com/media/press-releases/2025/china-sees-shift-in-tech-hiring> Hays技术招聘报告; Hays项目岗位观察; Hays亚洲薪酬指南数据; Hays培训与技能缺口; Hays中国技术招聘分析
[37] <https://www.anthropic.com/research/AI-assistance-coding-skills> AI辅助与编码技能研究
[38] <https://doi.org/10.48550/arxiv.2512.14012> 有经验开发者研究
[39] <https://survey.stackoverflow.co/2025/> 开发者信任调查; Stack Overflow调查; Agent采用与效果调查
[40] <https://www.gartner.com/en/newsroom/press-releases/2025-01-21-gartner-forecasts-worldwide-it-spending-to-grow-9-point-8-percent-in-2025> Gartner软件支出预测
[41] <https://www.miit.gov.cn/jgsj/yxj/xxfb/art/2026/art_32ce37ee09174bc0bf7add25ebeeb122.html> 中国2025年软件业统计; 2025年软件业运行情况; 工信部收入结构; 软件产业区域统计
[42] <https://www.frostchina.com/content/insight/detail/6a7d2f6d3e2ee3f932bac82c> 全球及中国Agent市场
[43] <https://www.goldmansachs.com/insights/articles/ai-agents-to-boost-productivity-and-size-of-software-market> 高盛客户服务软件估计
[44] <https://www.gartner.com/en/newsroom/press-releases/2025-07-29-gartner-forecasts-worldwide-end-user-spending-on-information-security-to-total-213-billion-us-dollars-in-2025> 信息安全支出预测
[45] <https://www.caict.ac.cn/kxyj/qwfb/bps/202603/P020260306392232241580.pdf> 中国信通院算力蓝皮书; 算力发展蓝皮书
[46] <https://www.miit.gov.cn/jgsj/yxj/xxfb/art/2026/art_d9504b5e12ef4fce9c86de1d1d0548f9.html> 2026年上半年运行情况
[47] <https://res-static.hc-cdn.cn/cloudbu-site/intl/zh-cn/about/whitepapers/1732092240930973657.pdf> 中国智能开发指南
[48] <https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/2-jobs-outlook/> WEF就业展望; WEF任务结构预测
[49] <https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm> BLS职业预测; BLS职业工资
[50] <http://www.bls.gov/opub/ted/2026/artificial-intelligence-information-technology-and-employment-2024-34.htm> BLS较早预测窗口
[51] <https://doi.org/10.17016/feds.2026.018> FEDS编码职业研究
[52] <https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality> SIEPR劳动力市场综述
[53] <http://cn.chinadaily.com.cn/a/202603/11/WS69b14058a310942cc49a2a17.html> 脉脉招聘报告转述; 中国平台薪资与供需
[54] <https://econhangyu.com/files/publications/2025-ai-exposure-china-EN.pdf> 中国任务暴露研究
[55] <http://www.scio.gov.cn/zdgz/jj/202509/t20250901_928364.html> 国务院“人工智能+”意见
[56] <https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/10/who-will-be-the-workers-most-affected-by-ai_fb7fcccd/14dc6f89-en.pdf> OECD不同劳动者群体研究
