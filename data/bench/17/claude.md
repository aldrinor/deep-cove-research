# 低代码/无代码平台对传统开发流程的影响：效率红利、维护陷阱与 AI 时代的再定位（2026 年 10 月）

**结论先行：低代码/无代码已成为企业软件开发的主流"第二轨道"，但没有取代传统开发。它在内部工具、流程自动化、表单和 CRUD 类应用上确实能显著缩短交付周期；一旦应用进入高并发、复杂领域逻辑或需要深度定制的核心产品领域，厂商锁定、计价方式变化和被迫重写会让全生命周期总拥有成本（TCO）反超传统开发。AI 代码生成正在把"低代码"本身重塑为"AI 应用生成（AppGen）+ 治理平台"，两者趋于融合，并不是简单的替代关系。**

## TL;DR

- **影响有多大：** 规模大，但属于"增量轨道"。据 InfoWorld 2022 年 12 月报道的 Gartner 新闻稿，低代码开发技术市场将"在未来四年增长 19%，到 2026 年达到 445 亿美元"。Forrester 2024 年 1 月博客称，"87% 的企业开发者至少在部分开发工作中使用低代码开发平台"。萨提亚·纳德拉在微软 FY25 第三季度财报电话会（2025 年 4 月 30 日）上披露，Power Platform 月活达 5600 万，同比增长 27%。不过独立证据显示，它主要吸收的是 IT 积压需求和"长尾应用"，核心系统仍以传统开发为主。
- **是否真正提高效率：** 在合适场景下是。但最亮眼的 ROI 数据（如 Power Platform 224% ROI、开发时间缩短 35%）几乎都来自厂商委托研究，缺少独立的全生命周期 TCO 研究。短期交付速度提升较可信，长期维护成本基本没有被独立量化过。
- **何时反增维护成本：** 应用超出平台能力边界时（性能、定制化、集成）；平台单方面改价时（如 Bubble 2023 年的 workload unit 计价）；公民开发者在缺乏治理的情况下大量造出"影子 IT/僵尸应用"时；还有需要跨平台迁移时，往往等同于重写。AI"氛围编程"（vibe coding）正在放大同一类治理风险。

## 一、行业趋势：市场规模、采用率、平台格局与 AI 冲击

### 1.1 市场规模：口径差异很大，但方向一致

| 机构 | 口径 | 数据 | 性质 |
|---|---|---|---|
| Gartner | 低代码开发技术（含 LCAP、RPA、公民自动化等） | 2023 年 269 亿美元 → 2026 年 445 亿美元，年复合增长约 19%；其中 LCAP 2023 年接近 100 亿美元\[1\]\[2\] | 预测\[2\] |
| Gartner | 新应用开发占比 | 2026 年低代码工具占新应用开发的 75%（2021 年为 40%）\[1\] | 预测，非实测\[3\] |
| Forrester | 低代码 + 数字流程自动化（DPA） | 2023 年底实测约 132 亿美元；基准情景 2028 年 300 亿美元（约 21%/年）；AI 加速情景约 500 亿美元（33%/年）；AI 抑制情景仅 11%/年\[4\]\[5\] | 估算 + 三情景预测 |
| Grand View Research | 低代码开发平台 | 2022 年 67.8 亿美元 → 2030 年 352.2 亿美元（CAGR 22.9%）\[6\] | 商业预测 |
| Grand View Research | 低代码应用开发平台（含服务） | 2023 年 248 亿美元 → 2030 年 1017 亿美元（CAGR 22.5%）\[7\] | 商业预测 |
| IDC 中国 | 中国低代码与零代码软件 | 2024 年 40.3 亿元人民币；2029 年预计 129.8 亿元，CAGR 26.4%\[8\] | 跟踪 + 预测\[9\]\[10\] |

**解读：** 同一家 Grand View Research 的两份报告口径相差近 3 倍，说明"低代码市场规模"高度依赖定义（是否包含 RPA、BPM、服务、SaaS 内置定制能力）。决策者应该看增长方向和结构，绝对值不宜直接比较。Forrester 的三情景预测最有参考价值，因为它明确承认 AI 可能抑制低代码增长：当 AI 编程助手让传统编码足够高效时，专业开发者可能"回到全代码"，这种情景下增速只有 11%。\[4\]

另外要提醒：Gartner 的"2026 年 75% 新应用使用低代码"是 2021–2022 年做出的预测。部分厂商博客声称"已经实现"，但我们没有找到 Gartner 公开的实测验证，应视为未经证实。

### 1.2 企业采用率与平台格局

- **采用广度：** Forrester 博客《The Low-Code Market Could Approach $50 Billion By 2028》（2024 年 1 月）写道："根据我们最新的调查数据，87% 的企业开发者至少在部分开发工作中使用低代码开发平台。"萨提亚·纳德拉在微软 FY25 第三季度财报电话会（2025 年 4 月 30 日）上说："我们现在有 5600 万 Power Platform 月活用户，同比增长 27%。"同一场电话会披露 GitHub Copilot 用户超过 1500 万，同比增长 4 倍以上，AI 编程工具的增速明显更快。
- **Gartner 2025 年企业级 LCAP 魔力象限**（2025 年 7 月 28 日发布，评估 12 家厂商）的领导者为 Mendix、OutSystems、Microsoft、ServiceNow、Appian、Salesforce。Retool\[11\]\[12\] 被定位为面向专业开发者的内部工具平台。Bubble、Airtable、Webflow\[13\] 等更偏中小企业、创业公司和非技术用户的无代码工具不在企业级 LCAP 评估范围内。
- **分层格局：** ①企业级 LCAP（OutSystems、Mendix、Appian、Power Platform），面向关键业务应用和受监管行业；②SaaS 生态内置平台（Salesforce、ServiceNow），在既有系统上扩展；③开发者向内部工具平台（Retool），由工程师用 SQL/JS 快速搭后台；④无代码建站/应用（Bubble、Webflow、Airtable），主要服务创业 MVP 和团队协作。

### 1.3 中国市场

- IDC《2024 下半年中国低代码与零代码软件市场跟踪报告》：2024 年下半年市场规模 22.9 亿元，同比增长 20.2%；全年 40.3 亿元。低代码子市场占 85.6%，零代码占 14.4%。厂商类型包括独立厂商（奥哲、得帆、简道云）、应用软件/SaaS\[14\] 厂商（金蝶、用友）和平台型厂商（华为、浪潮）。金蝶自称以\[15\] 15.7% 份额连续五年第一，这是厂商新闻稿引用 IDC 的数据。\[16\]
- **协同办公平台的"表格化低代码"是中国特色主战场：** 飞书多维表格月活从 2024 年 9 月的 600 万增长到 2025 年 7 月接近 1000 万，单表容量提升到千万级"热行"，并开放给钉钉、企业微信使用。钉钉推出\[17\]\[18\] AI 表格与之竞争，其低代码平台宜搭被视为国内较成熟的 aPaaS。QuestMobile 数据显示钉钉月活约 2 亿，企业微信约 1 亿，飞书约 3000 万。\[19\]\[20\]
- **解读：** 中国市场总额（约 40 亿元人民币）相对全球很小，但"零代码 + 协同平台"的渗透深度很高，业务人员正在用多维表格承载原本属于 ERP/CRM 的功能。飞书方面称有客户单表达到 90 多万行。这正是全球讨论的"公民开发者把核心流程搬上轻量平台"的现象，治理风险也一样。值得注意的是，飞书\[17\] CEO 公开批评钉钉的部分权限隔离是用前端 JavaScript 实现的，并非后端隔离。这类竞争者指控未经独立验证，但它恰好说明了零代码平台上"看似有权限控制"的安全隐患。\[21\]

### 1.4 AI 辅助编程的冲击：替代还是融合？

**判断：融合为主，但低代码的"护城河"从"不用写代码"转向了"治理、部署、集成与运行时"。**

- **厂商与分析师的定位转变：** Forrester 分析师 2024 年提出低代码正在演变为"应用生成（AppGen）平台"，认为"低代码平台在\[22\] AppGen 上有先发优势"。2024\[23\] 年 11 月又称，AI 驱动的企业将更多"自建"而不是"采购"软件，大量应用会整合到低代码 AppGen 平台上。到\[24\] 2026 年，Forrester 已把相关报告更名为"AppGen 与低代码平台"版图。据\[25\]\[26\] MSDynamicsWorld 对 2025 年 Power Platform 社区大会（PPCC25，2025 年 10 月 28 日）的报道，微软商业与行业 Copilot 总裁 Charles Lamanna 直言"我们所知的低代码已经死了"，团队正在开发新一代能力，目标是把 5600 万月活扩展到 5 亿。
- **"替代"情景的证据：** 有用户把 Power Automate 流程替换为 Cursor、Claude Code 生成的代码；有咨询商把客户从\[27\] Bubble 迁移到"Claude Code + 云托管"方案。AI\[28\] 生成的是标准代码（如 Next.js、Python），天然规避了专有平台锁定，这是 vibe coding 对无代码最直接的冲击。\[29\]
- **"融合"情景的证据：** Gartner 已单独设立"企业 AI 编码代理"魔力象限（2026 年 5 月，据二手来源，领导者为 Anthropic、Cursor、GitHub、OpenAI）。传统\[12\] LCAP 厂商则普遍嵌入 AI 生成能力。一项 2024 年 arXiv 实证研究发现，24 个传统低代码工具中有 13 个自 2023 年起加入了 AI 功能。Retool\[30\] CEO David Hsu 的说法概括了融合逻辑："AI 降低了做原型的门槛，但上线的门槛没有变。"\[31\]
- **专业开发者对 AI 的态度同样谨慎：** Stack Overflow 2025 年开发者调查（2025 年 7 月 29 日发布，约 4.9 万名受访者）显示，84% 的开发者使用或计划使用 AI 工具（2024 年为 76%），但 46% 不信任其输出的准确性，较上一年的 31% 明显上升；信任的仅 33%，"高度信任"的仅约 3%。约 72% 表示 vibe coding 不是其专业工作的一部分，另有 5% 明确反对。METR 的随机对照试验（16 名资深开源开发者、246 个真实任务）发现，使用 AI 工具时任务耗时反而增加 19%，而开发者自认为快了 20%。METR\[32\] 称这是 2025 年初的特定情境结论，后续模型可能有所改善。\[33\]

**解读：** 如果 AI 让专业开发者写代码足够快，低代码"替开发者省时间"的价值会被压缩，这对应 Forrester 的悲观情景。但 AI 生成的代码同样需要部署、权限、审计和运维，而这正是企业级 LCAP 的强项。因此最可能的结局是：面向专业开发者的"可视化编码"价值下降，面向业务人员的"受治理的应用生成与运行平台"价值上升。

## 二、生产力 vs. 维护成本：短期速度与全生命周期 TCO

### 2.1 支持"提效"的证据（注意来源）

| 研究 | 主要发现 | 来源性质 |
|---|---|---|
| Forrester TEI：Microsoft Power Platform（2024） | 三年 ROI 224%，开发时间缩短 35%，三年直接开发与 IT 成本节省 4360 万美元（风险调整），回收期小于 6 个月\[34\] | **微软委托**的复合组织模型 |
| Forrester TEI：Power Automate（2024 年 6 月） | ROI 248%；三年收益 5593 万美元 vs 成本 1608 万美元；工作流开发时间缩短 20%\[35\]\[36\] | **微软委托**（复合组织 3 万员工） |
| Forrester TEI：Power Apps | ROI 206%，专业开发者效率收益 1470 万美元\[37\] | **微软委托** |
| 早期 Forrester TEI：Power Platform | ROI 502%，应用开发成本降低 48%\[38\] | **微软委托** |
| Forrester 自有调查 | 87% 企业开发者使用低代码\[5\] | 独立分析师数据（采用率，非效率）\[2\] |

**关键提醒：** 几乎所有"开发速度提升 X 倍、ROI 数百%"的数字都来自厂商委托的 TEI 研究。这类研究基于少量受访客户构建"复合组织"，方法透明，但样本经过选择，且通常只覆盖三年。同一套方法对同一厂商不同产品得出的 ROI 在 206% 到 502% 之间波动，本身就说明结果对假设很敏感。宜将其理解为"上限情景"，不宜当作行业平均值。

### 2.2 反面证据：技术债、锁定、计价与重写

1. **定制化与维护是开发者最大的痛点（独立学术研究）：** Alamin 等人在 Empirical Software Engineering（2023）上分析了约 3.37 万条 Stack Overflow 帖子，覆盖 38 个低代码平台。按话题统计，定制化约占 30%、数据存储约 25%、平台维护约 14%。研究结论是"敏捷维护与部署阶段是从业者面临的最具挑战性的阶段"，例如库依赖管理类问题有 70% 没有被采纳的答案。早期同类研究（约\[39\] 5000 条帖子、9 个平台）发现约 40% 的问题与 UI 定制挑战有关。\[40\]
2. **迁移约等于重写：** 2024 年 arXiv 研究（Liu 等）指出，传统低代码平台的局限中，"需要专业知识"占 34.74%，"数据迁移"占 16.84%，并明确写道："一旦数据和功能与某一平台紧密集成，迁移到另一平台可能需要完整重构应用，造成高昂成本。"研究还发现版本问题主要出现在维护阶段。\[30\]
3. **平台单方面改价：** Bubble 于 2023 年 4 月宣布、5 月起实施基于"workload unit（工作负载单位）"的计价。社区强烈反弹，有用户报告其应用上月消耗 2200 万 WU，而 Growth 套餐只含 25 万 WU。创始人随后发文道歉，并将关键操作的\[41\]\[42\] WU 消耗下调 50%–99%。这是"锁定\[42\]\[43\] + 定价权"风险的教科书案例：应用无法导出，用户只能接受新价格或重写。
4. **超出平台能力后被迫重写：** 多家迁移服务商公开的案例显示，创业公司在用户规模增长后会遇到 Bubble 性能瓶颈。某 B2B SaaS 迁移后月基础设施成本从 2400 美元降到 190 美元，复杂应用的迁移报价约 3.5 万–6 万美元、14–20 周。**注意：**\[44\]\[45\] 这些数据来自以迁移为业务的代理商，存在明显的利益倾向，只能作为方向性证据。
5. **安全与影子 IT：** OWASP 发布了公民开发十大风险（最初针对低代码/无代码，现已扩展到 AI 辅助编程和 AI 代理），包括"盲目信任""账户冒用""授权滥用""敏感数据泄露""资产管理失败"等。2026\[46\]\[47\] 年 arXiv 的一项访谈研究（12 名 DevOps 从业者）称低代码在 DevOps 中是"一把双刃剑"：自动化提效的同时增加安全与治理风险，并且存在"限制功能与成本的厂商锁定"。\[48\]

### 2.3 区分"短期交付速度"与"全生命周期 TCO"

| 维度 | 低代码/无代码 | 传统开发 |
|---|---|---|
| 首版交付速度 | **明显占优**（证据较一致，但量化多来自厂商） | 较慢 |
| 初期人力成本 | 低（可用业务人员或少量开发者） | 高 |
| 许可/订阅成本 | 随用户数、用量线性甚至超线性增长，且受厂商定价权支配 | 主要是基础设施与人力 |
| 定制化与扩展 | 碰到平台边界后成本陡增 | 线性增长 |
| 测试/CI/CD/可观测性 | 依赖平台能力，学术研究显示测试与部署是薄弱环节 | 生态成熟 |
| 退出/迁移成本 | **高**，通常需要重写 | 低到中 |
| 治理成本 | 公民开发规模化后需要专门投入 | 纳入既有 SDLC |

**结论：** 对生命周期短、需求稳定、规模有限的内部应用，低代码的 TCO 通常更低。对需要长期演进、规模增长不确定的对外产品，低代码相当于"用未来的迁移成本换今天的速度"。这笔交易是否划算，取决于产品能否在触及平台边界前验证商业价值。

**证据缺口：** 我们没有找到任何独立机构对低代码应用的长期维护成本、TCO 或重写率做过量化研究。现有"维护成本更低"的说法基本出自厂商。这本身就是重要发现：企业应自行建立 TCO 跟踪，而不是依赖厂商的 ROI 计算器。

## 三、开发者视角 vs. 业务视角

### 3.1 两种视角的对比

| 议题 | 业务决策者/CIO | 专业开发者 |
|---|---|---|
| 核心诉求 | 消化 IT 积压需求、加快交付、降低对稀缺工程师的依赖 | 可扩展性、可维护性、代码所有权 |
| 对成本的看法 | 看首年交付成本和人力节省 | 看锁定、改价、重写的长期成本 |
| 公民开发者 | 生产力杠杆，Gartner 称 41% 的员工已是"业务技术人员"\[49\] | 潜在的影子 IT 与"僵尸应用"来源 |
| 工程实践 | 关注较少 | 版本控制、自动化测试、CI/CD、调试、可观测性受限 |
| 职业影响 | 人才结构优化 | 担心技能"平台专有化"、简历价值下降 |
| 对 AI 的态度 | 业务压力迫使加速，见下文 Retool 调查 | 46% 不信任 AI 输出准确性\[50\] |

### 3.2 分歧的根源

1. **时间视野不同：** 业务方的考核周期以季度/年计，开发者要为三到五年后的维护负责。
2. **成本归属不同：** 交付收益记在业务部门账上，维护、安全事件和迁移成本最终落到 IT 头上。Gartner 2022 年 3 月 13 日的新闻稿（基于 2021 年 11–12 月对 1120 名经理级及以上人员的调查）显示，74% 的技术采购至少部分由 IT 以外的业务部门出资，只有 26% 完全由 IT 出资；同一新闻稿援引 Gartner 研究称 41% 的员工是"业务技术人员"。"谁付钱"和"谁兜底"已经分离。
3. **信息不对称：** Retool 2025/2026 年对 300 名 CIO/CTO/CISO 的调查（厂商调查）显示，93% 担心 vibe coding 生成的工具在生产环境运行，38% 视其为首要运营风险，只有 5% "非常有信心"掌握全部生产内部工具的情况，59% 无法确认是否发生过 AI 导致的生产事故。同时 90% 表示过去 12 个月来自业务的压力上升。\[51\]
4. **数字化成效本身不确定：** Gartner 2025 年 CIO 与技术高管调查（2024 年 10 月 22 日在 IT Symposium/Xpo 发布，覆盖 88 个国家的 3186 名受访者）显示，IT 以外的业务部门平均有 26% 的员工专门从事技术构建、实施或管理（Gartner 研究副总裁 Raf Gelders 语），但全企业范围内只有 48% 的数字化项目达到或超过业务目标。

### 3.3 成功与失败模式

- **成功模式（典型）：** 内部审批、数据采集、运营后台。例如在 Retool 上由小型技术团队快速搭建多页面内部应用并连接 Intercom、Zapier 等工具（用户评价），以及中国企业在飞书多维表格上搭建采购、项目跟踪系统。\[19\]\[52\]
- **失败模式（典型）：** ①创业公司在 Bubble 上验证 PMF 后遭遇性能和计价双重压力，被迫重写；②公民开发者构建的应用无人维护、权限配置错误，形成数据泄露面（OWASP 列举的"孤儿应用"场景）；③零代码平台承载了接近百万行的核心业务数据，却缺少后端级权限隔离和审计。\[45\]\[53\]

### 3.4 调和路径

- **融合团队（Fusion Teams）：** Gartner 研究显示，至少 84% 的企业和 59% 的政府机构（Gartner 另一处数据为 54%）已组建融合团队，约 1000 个受访融合团队中有 43% 汇报给 IT 以外的部门。关键是由专业开发者负责平台、集成、安全和"可复用组件"，业务人员在护栏内组装应用。\[54\]\[55\]
- **治理框架：** 包括应用清单、DLP 策略、环境隔离、审计日志（如 Power Platform 管理中心、Microsoft Purview）；按应用风险分级（个人/团队/部门/企业级）设定不同审查强度；为公民开发者设"毕业"机制，当应用用户数或数据敏感度超过阈值时，强制转交专业团队接管或重写。\[56\]
- **平台工程：** 把低代码平台作为内部开发者平台的一部分，统一身份、数据访问、CI/CD 和监控，并把 AI 生成的代码纳入同一套治理。这正是 Retool、Microsoft、ServiceNow 等厂商的转型方向。

## 四、未来发展预测（2026–2030）

### 4.1 场景适用性判断

| 场景 | 低代码/无代码适用性 | 理由 |
|---|---|---|
| 内部工具、管理后台、仪表盘 | **明确占优** | 用户量小、需求变化快、对极致性能不敏感 |
| 工作流自动化、审批、表单 | **明确占优** | 平台原生能力强，Appian、Power Automate、宜搭等的核心场景 |
| 原型 / MVP | **占优，但正被 AI 代码生成抢占** | vibe coding 生成可迁移的标准代码，没有锁定 |
| 部门级 CRUD 应用 | 占优 | 需配合治理 |
| 基于 SaaS 生态的扩展（CRM、ITSM） | 占优 | Salesforce、ServiceNow 内置平台，数据就在平台内 |
| 企业关键业务系统 | **有条件可行** | 企业级 LCAP（OutSystems、Mendix）正在进入，但需要专业团队主导 |
| 高并发、高性能对外产品 | **明确不适合** | 运行时不可控，计价随用量放大 |
| 复杂领域逻辑、算法密集 | **明确不适合** | 定制化是平台最大痛点（学术研究约 30%–40% 的问题与定制相关） |
| 需要深度差异化体验的核心产品 | **不适合** | 可视化组件限制体验和架构自由度，且面临锁定 |

### 4.2 分析师预测与我们的判断

- **Gartner（2024 年魔力象限）：** 到 2029 年，企业级 LCAP 将在全球 80% 的企业中用于关键业务应用开发，2024 年这一比例为 15%。**注意：**\[57\]\[58\] 这句话常被厂商误引为"80% 的关键业务应用将运行在低代码上"。原意是"80%\[2\] 的企业会在某些关键业务应用上使用 LCAP"，两者差别很大。
- **Forrester：** 基准情景下 2028 年低代码 + DPA 市场约 300 亿美元，AI 加速情景下约 500 亿美元。2026\[4\]\[5\] 年 Forrester 文章称"AppGen 正在吞噬低代码"，并警告不受管理的应用蔓延会"产生安全风险，留下资源消耗未知的僵尸软件……导致工作量与预算的浪费"。\[59\]
- **IDC 中国：** 2029 年市场达 129.8 亿元，并判断低代码与零代码正在融合，同时深度整合生成式\[14\] AI。\[9\]\[15\]

**我们的判断：**
1. **不会出现"企业全面转向低代码/无代码"。** 更可能的格局是三轨并存：核心系统与差异化产品由专业团队配合 AI 编码代理开发；企业级流程和内部应用由受治理的 AppGen/低代码平台承载；个人和团队级工具由协同平台里的零代码表格与 AI 生成满足。
2. **"低代码"作为一个独立品类会被重新定义。** 拖拽式可视化编程的相对价值在下降，平台竞争焦点转向治理、数据连接、身份权限、运行时和对 AI 生成产物的管控。Microsoft"低代码已死"的表态和 Forrester 的更名都指向这一点。
3. **AI 代码生成会同时扩大和压缩市场：** 它扩大了"人人可构建"的人群，例如 Retool 调查称 48% 的非工程师已能直接构建软件（厂商数据）；同时压缩了专业开发者使用可视化低代码的理由，并把影子\[31\] IT 风险从"低代码应用"扩散到"AI 生成应用"。OWASP 已把这两者合并到同一份风险清单中。\[47\]
4. **对 2026–2030 年的关键不确定性：** AI 编码代理的实际生产力（METR 的负面结果与开发者主观感受相反，Stack Overflow 显示信任下降）；以及厂商在 AI 时代是否会再次调整计价（按 AI 调用、按代理运行计费），这可能重演 Bubble 2023 年的改价冲击。

## 五、综合结论：直接回答核心问题

**1. 影响有多大？** 影响已经足够大，传统开发流程无法忽视它。低代码已成为企业应用组合中的常规组成部分，有数千万级的活跃用户和数百亿美元的市场规模。但它改变的主要是"谁来开发长尾应用"以及"IT 积压需求怎么消化"，并没有改变核心系统的开发方式。真正可能重塑传统开发流程的是 AI 编码代理，低代码平台正在向它靠拢。

**2. 是否真正提高效率？** 在适合的场景（内部工具、流程自动化、表单、CRUD、SaaS 扩展）中，首版交付速度的提升是真实的，方向一致的证据很多。但几百个百分点的 ROI 数字主要来自厂商委托研究，应打折理解。至于全生命周期，目前**没有独立的高质量证据**证明低代码 TCO 更低或更高。

**3. 什么情况下反而增加维护成本？** 以下五种情形最可能让低代码的 TCO 反超传统开发：
- ①应用规模或复杂度超出平台边界，需要大量变通方案和定制，最终被迫重写；
- ②平台单方面改价或调整计价模型，而应用无法迁移；
- ③公民开发缺乏治理，产生影子 IT、孤儿应用和安全事件；
- ④需要跨平台迁移或退出，通常相当于重建；
- ⑤测试、版本控制、CI/CD、可观测性薄弱，导致长期变更风险累积。

## 建议

1. **按场景而不是按"全面采用"决策：** 用第四节的适用性表做准入门槛，核心系统和对外高性能产品默认走专业开发（配合 AI 编码代理）。
2. **采购前评估"退出成本"：** 要求厂商说明数据导出、代码/元数据可移植性、计价模型历史变动和合同价格保护条款。把迁移成本计入 TCO，而不是只看三年 ROI。
3. **建立"毕业机制"和风险分级治理：** 应用超过用户数、数据敏感度或关键性阈值后，强制转交专业团队审查或重构。以 OWASP 公民开发十大风险作为安全检查清单。
4. **把 AI 生成应用和低代码应用纳入同一治理框架：** 统一应用清单、身份权限、审计与监控，避免 vibe coding 成为新的影子 IT。
5. **自建 TCO 度量：** 跟踪每个低代码应用的许可费、维护工时、事故数和变更周期，用真实数据取代厂商 ROI 计算器。
6. **对中国企业：** 在飞书多维表格、钉钉宜搭等平台上承载核心业务数据之前，须确认权限隔离是否在后端实现、是否有完整审计日志，以及数据能否导出。

## 注意事项

- **市场规模数据口径差异大：** 不同机构乃至同一机构的不同报告相差数倍，并且多为预测，不是实测。
- **效率数据存在利益倾向：** Forrester TEI 均由微软委托；Retool、金蝶、奥哲等的调查和排名为厂商自有或厂商发布；Bubble 迁移案例来自迁移服务商。
- **部分数据为二手来源：** Gartner 2025 年魔力象限的部分细节和 2026 年 5 月的"企业 AI 编码代理"魔力象限领导者名单来自厂商或第三方转述，未直接查阅 Gartner 原文。Gartner 融合团队中政府机构比例有 59% 与 54% 两个版本。\[54\]\[55\]
- **学术研究以 Stack Overflow 帖子分析和小样本访谈为主：** 能揭示痛点分布，但不能直接换算为成本。
- **METR 研究样本小**（16 名开发者），限定于资深开发者处理熟悉代码库的情境，且基于 2025 年初的模型，不宜泛化。\[33\]\[60\]

## 資料來源

1. [Low-code development technologies market forecast to hit \$44.5 billion by 2026](https://www.infoworld.com/article/2337677/low-code-development-technologies-market-forecast-to-hit-445-billion-by-2026.html)
2. [Low‑Code Trends & Statistics Shaping Enterprise IT in 2026 (Updated)](https://kissflow.com/low-code/low-code-trends-statistics/)
3. [Gartner Forecasts for the Low‑Code development Market Growth (2026)](https://kissflow.com/low-code/gartner-forecasts-on-low-code-development-market/)
4. [Forrester predicts three possible outcomes for the future of low-code - SD Times](https://sdtimes.com/low-code/forrester-predicts-three-possible-outcomes-for-the-future-of-low-code/)
5. [The Low-Code Market Could Approach \$50 Billion By 2028](https://www.forrester.com/blogs/the-low-code-market-could-approach-50-billion-by-2028)
6. [Low-code Development Platform Market Size Report, 2030](https://www.grandviewresearch.com/industry-analysis/low-code-development-platform-market-report)
7. [Low-code Application Development Platform Market Report, 2024-2030](https://www.grandviewresearch.com/industry-analysis/low-code-application-development-platform-market)
8. [IDC：预计到2029年中国低代码与零代码软件市场规模将达到129.8亿元](https://www.cls.cn/detail/2074887)
9. [IDC权威发布！奥哲再次获得中国低零代码独立厂商第一！|AI技术|AI图像生成|数据|客户|模型\_手机新浪网](https://finance.sina.cn/tech/2025-07-11/detail-inffafmt1009343.d.html)
10. [2025年低代码、零代码平台排行榜，哪家市场份额最大，哪家最好用、最安全？ - 知乎](https://www.zhihu.com/question/1910620641960366367/answer/1930582329736279992)
11. [Salesforce Named a Leader in the 2025 Gartner® Magic Quadrant™ for Enterprise Low-Code Application Platforms](https://www.salesforce.com/news/stories/gartner-magic-quadrant-low-code-application-2025/)
12. [Gartner Magic Quadrant for Enterprise Low code ...](https://kissflow.com/low-code/gartner-magic-quadrant-for-enterprise-low-code/)
13. [2025 Gartner Magic Quadrant for Enterprise LCAP: Low-code keeps gaining traction - Pretius](https://pretius.com/blog/gartner-quadrant-low-code)
14. [IDC：预计到2029年低代码与零代码软件市场规模将达到129.8亿元\_腾讯新闻](https://news.qq.com/rain/a/20250703A04HBD00)
15. [IDC：低代码与零代码深度融合生成式AI，重构开发范式](https://mfe-prod.idc.com/getdoc.jsp?containerId=prCHC53666825)
16. [金蝶五连冠！2024年中国低零代码软件市场排名出炉-金蝶官网](https://www.kingdee.com/newlist/61441)
17. [千万月活在即，飞书还是等不及了！“多维表格”打通钉钉、企微，协同办公“三国杀”暗流涌动](https://www.nbd.com.cn/articles/2025-07-10/3939922.html)
18. [飞书多维表格月活近千万，将接入钉钉与企业微信](https://article.pchome.net/news/4201.html)
19. [2025年了，钉钉、飞书、企业微信，中小企业选型指南](https://www.woshipm.com/it/6245641.html)
20. [协同办公概念“泛滥”，但中小企业和打工人真的需要吗？ - 21经济网](https://www.21jingji.com/article/20251205/herald/7dd1dd58b4c6135a57b884a3e6758ba3.html)
21. [飞书飞，钉钉追-太平洋科技](https://www.pconline.com.cn/focus/1947/19474054.html)
22. [Microsoft is leader in 2025 Forrester Wave™ for low-code platforms ranked top in strength of strategy and offering - Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/power-apps/microsoft-is-a-leader-in-2025-forrester-wave-low-code-platforms-for-professional-developers/)
23. [The Rise Of Application Generation Platforms](https://www.forrester.com/blogs/the-rise-of-application-generation-platforms/)
24. [AppGen Is An Existential Threat To The Enterprise App Business](https://www.forrester.com/blogs/appgen-is-an-existential-threat-to-the-enterprise-app-business/)
25. [Low-Code Platforms - Forrester](https://www.forrester.com/blogs/category/low-code-platforms/)
26. [AppGen And Low-Code Platforms - Mavengity](https://mavengity.com/research/appgen-and-low-code-platforms/)
27. [What Does Vibe Coding Mean for Low-Code Platforms? - Forward Forever](https://forwardforever.com/what-does-vibe-coding-mean-for-low-code-platforms/)
28. [jp.trustpilot.com](https://jp.trustpilot.com/review/bubble.io)
29. [Vibe Coding vs Low-Code: Key Differences Explained (2026)](https://www.memberstack.com/blog/how-does-vibe-coding-compare-to-low-code-platforms)
30. <https://arxiv.org/pdf/2402.01156>
31. [Everyone can go build: Retool adds latest chapter in movement to democratize software generation - SiliconANGLE](https://siliconangle.com/2025/10/08/everyone-can-go-build-retool-adds-latest-chapter-movement-democratize-software-generation/)
32. [METR study finds experienced developers were 19% slower...](https://vibegraveyard.ai/story/metr-ai-slows-experienced-developers-study/)
33. [Is AI Actually Making You Dumber and Slower?](https://ainewstoday.substack.com/p/metr-study-ai-coding-slower-apple-nvidia)
34. [Reduce development times and increase ROI with Microsoft Power Platform - Microsoft Power Platform Blog](https://www.microsoft.com/en-us/power-platform/blog/2024/09/03/reduce-development-times-and-increase-roi-with-microsoft-power-platform/)
35. [The Total Economic Impact™ Of Microsoft 365 For Business](https://tei.forrester.com/go/Microsoft/365Business/?lang=en-us)
36. [The Total Economic Impact™ Of Microsoft Power Automate](https://tei.forrester.com/go/microsoft/powerautomatetei/index.html)
37. [The Total Economic Impact™ Of Microsoft Power Apps](https://tei.forrester.com/go/microsoft/powerappstei/?lang=en-us)
38. [A FORRESTER TOTAL ECONOMIC IMPACT™ STUDY COMMISSIONED BY MICROSOFT](https://tools.totaleconomicimpact.com/go/microsoft/powerplatform/docs/TEIofPowerPlatform-FINAL.pdf)
39. [Developer Discussion Topics on the Adoption and Barriers of Low Code Software Development Platforms](https://arxiv.org/pdf/2209.00844)
40. [(PDF) An Empirical Study of Developer Discussions on Low-Code Software Development Challenges](https://www.academia.edu/86252506/An_Empirical_Study_of_Developer_Discussions_on_Low_Code_Software_Development_Challenges)
41. [More context on our changes to pricing - Announcements - Bubble Forum](https://forum.bubble.io/t/more-context-on-our-changes-to-pricing/255551)
42. [Bubble Reviews 2026: What 640+ Users Actually Think - Bubble](https://checkthat.ai/brands/bubble/reviews)
43. [An Update to Workload, Plus More Transparent Calculations - Announcements - Bubble Forum](https://forum.bubble.io/t/an-update-to-workload-plus-more-transparent-calculations/257080)
44. [Migrate from Bubble.io to Code 2026: Costs & Timeline](https://goodspeed.studio/blog/migrate-from-bubble-to-code)
45. [Case Study: Graduating from No-Code - Migrating a Bubble App to Scalable Custom Code](https://www.meerako.com/blogs/case-study-migrating-bubble-no-code-to-nextjs-custom-code)
46. [OWASP Citizen Development Top 10](https://owasp.org/www-project-citizen-development-top10-security-risks/)
47. [www-project-citizen-development-top10-security-risks/index.md at main · OWASP/www-project-citizen-development-top10-security-risks · GitHub](https://github.com/OWASP/www-project-citizen-development-top10-security-risks/blob/main/index.md)
48. <https://arxiv.org/pdf/2605.16971>
49. [Gartner Survey Finds Rise in Business Technologists is Driving Funding for Tech Purchases Outside of IT](https://www.gartner.com/en/newsroom/press-releases/2022-03-13-gartner-survey-finds-rise-in-business-technologists-is-driving-funding-for-tech-purchases-outside-of-it)
50. [Learning #1. AI adoption is accelerating, but trust is declining](https://stackoverflow.co/internal/resources/2025-stack-overflow-developer-survey-for-leaders/ai-adoption/)
51. [As Vibe Coding Tops C-suite’s List of Concerns, Retool Unveils First Platform to Extend Enterprise Governance to All AI-Coded Apps](https://finance.yahoo.com/technology/ai/articles/vibe-coding-tops-c-suite-140000880.html)
52. [Retool Reviews 2026: Details, Pricing, & Features](https://www.g2.com/products/retool/reviews)
53. [OWASP's Top 10 Risks for Citizen Development](<https://owasp.org/www-project-citizen-development-top10-security-risks/assets/images/OWASP's%20Top%2010%20Risks%20for%20Citizen%20Development%20(2).pdf>)
54. [Fusion Teams: A New Model for Digital Delivery for CIOs](https://www.gartner.com/en/doc/fusion-teams-a-new-model-for-digital-delivery)
55. [Gartner on X: "Gartner data shows that at least 84% of companies and 54% of government entities have set up fusion teams designed to deliver digital products rather than projects. Learn why fusion teams are on the rise 📈 for orgs: https://t.co/rvZUEyZyTR @Gartner\_IT #GartnerSYM #CIO" / X](https://twitter.com/Gartner_inc/status/1517566945666686979)
56. [Practical Power Platform: Areas for Microsoft 365 Administrators to Explore](https://practical365.com/practical-power-platform-areas-for-microsoft-365-administrators-to-explore/)
57. [Execute Your Development Needs with a Magic Quadrant™ Low-Code Leader](https://www.mendix.com/blog/gartner-mq-lcap-2024/)
58. [Mendix Named a Leader 2024 Gartner® Magic Quadrant™ for Enterprise Low-Code Application Development Platforms For The Eighth Consecutive Year\*](https://www.mendix.com/press/mendix-named-a-leader-2024-gartner-magic-quadrant-for-enterprise-low-code-application-development-platforms-for-the-eighth-consecutive-year/)
59. <https://www.forrester.com/blogs/appgen-is-eating-low-code-what-it-means-to-you>
60. [AI coding tools might actually be slowing you down](https://www.itbrew.com/stories/2025/08/04/ai-coding-tools-might-actually-be-slowing-you-down)