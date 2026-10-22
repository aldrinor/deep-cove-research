# 低代码与无代码：交付提速有多大，维护成本何时反而更高

**结论先行。**低代码/无代码已经明显改变企业应用开发，但改变的是重复实现、业务参与和交付分工，并没有取消软件工程。低代码的效率收益是真实的：2022年一项同需求实验中，含配置和测试的耗时从2303分钟降至716分钟，约为传统方式的3.22倍生产率。[1]

**收益存在边界。**2026年一项覆盖7个企业部署、持续18个月的观察报告称，稳定流程型应用的交付时间减少57%。同一研究也报告了约为传统基线1.6倍的低代码修复负担，复杂算法和重度集成应用的优势明显收窄。[2] 因此，短期提速可以成立，长期成本仍可能上升。未来更有依据的判断，是按场景采用并与专业代码混合，而不是企业全面放弃传统开发。

| 核心问题 | 关键结果 | 决策判断 |
|---|---|---|
| 低代码与无代码是否相同 | 前者允许代码扩展，后者主要依靠配置 | 分开评估能力与收益 |
| 行业影响有多大 | KPMG的2024年样本中，37%将其置于战略核心 | 已进入企业常规开发组合 |
| 哪些流程变化最大 | 配置、组件复用、发布和标准变更 | 实现提速，验证责任保留 |
| 效率是否真正提高 | 实验716对2303分钟；项目库1.8对8.3小时/功能点 | 标准化任务收益显著 |
| 维护是否可能更贵 | 18个月观察报告修复负担约1.6倍 | 复杂度、集成和治理可使收益反转 |
| 哪些场景优先采用 | 简单原型用无代码，稳定流程用低代码 | 核心复杂逻辑优先混合架构 |
| 开发者与管理者如何协调 | 速度、成本与控制权关注点不同 | 共同承担生命周期结果 |
| 未来会否全面转向 | 2026—2031年更支持场景化混合 | 专业代码继续承担关键工程工作 |

**阅读路线。**下文先区分三种开发方式，并建立统一比较基线。随后考察全球采用趋势，以及需求、实现、测试、部署和迭代的变化。再分别比较效率、维护、适用场景与组织分工，最后判断2026—2031年的采用路径。讨论以全球软件开发行业为范围，主要采用2021年至2026年9月13日视野内的证据；中国材料仅用于说明具体机制和场景。

本节参考文献：
[1] IEEE受控实验 <https://doi.org/10.1109/mitp.2022.3189880> 摘录：“U U C P=U A W+U U C W.(1) View Source! Image 1: Right-click on figure for MathML and additional features. ( Adjustment of UUCP, considering a set of technical and environmental factors represented by the technical complexity factor (TCF) and the environmental factor (EF) v…”
[2] 企业部署观察 <https://www.sci-open.net/index.php/JTIE/article/view/16625> 摘录：“Journal of Software: Evolution and Process, 37(2), e2680. Kumar, A., & Patel, N. Productivity measurement in low-code development: A controlled experiment. Empirical Software Engineering, 29(4), 92. Zhang, L., Chen, H., & Liu, M. Comparing defect density and resolution tim…”

## 一、问题的价值：不是少写多少代码，而是整个生命周期是否更划算

本节参考文献：
[1] IEEE受控实验 <https://doi.org/10.1109/mitp.2022.3189880> 摘录：“Title: Low-Code Versus Code-Based Softw…”
[2] 企业部署观察 <https://www.sci-open.net/index.php/JTIE/article/view/16625> 摘录：“Low-Code Platform-Driven Software Engin…”

### 三种开发方式，交换的是不同层次的控制权

**低代码保留扩展。**低代码通常通过可视化模型、预制组件和流程编排构建应用，并允许加入脚本、手写代码和自定义连接器。它主要服务专业开发者，以及业务人员与开发者组成的混合团队。无代码则主要面向业务用户和领域专家，通过拖放、模板、公式或自然语言完成限定范围的应用构建。[3][4]

| 开发方式 | 典型使用者 | 主要表达方式 | 配置—代码边界 | 主要控制能力 |
|---|---|---|---|---|
| 传统专业代码 | 软件工程师、专业团队 | 编程语言、框架、代码库 | 直接实现核心行为 | 逻辑、性能、数据与运行方式 |
| 低代码 | 专业开发者、融合团队 | 可视模型、组件加代码 | 标准部分配置，特殊部分扩展 | 保留接口与扩展控制 |
| 无代码 | 业务用户、领域专家 | 模板、拖放、公式、自然语言 | 主要在平台功能集内配置 | 控制业务配置，底层依赖平台 |

**无代码仍需知识。**“不写通用编程代码”不等于“不需要技术判断”。Gartner把只需输入公式或简单表达式的平台也纳入无代码范围，并指出复杂配置仍可能需要专业技能。[5] 数据关系、访问权限和异常处理，并不会因为操作界面变成拖放而自动正确。

**边界不是品牌。**同一产品可以同时提供无代码入口、低代码扩展和专业开发接口。2026年的Power Platform文档审批研究就描述了这种组合：业务用户搭建应用，专业开发者处理程序化数据访问、业务逻辑、自定义连接器和外部集成。[6] 因而，不能仅凭“使用Power Apps”就把全部结果归为无代码。

**控制也有代价。**传统代码允许团队直接优化复杂逻辑、资源消耗、长期维护和安全修复。低代码把部分控制换成交付便利，无代码进一步把控制集中到平台预设能力中。[7] 这种交换可以非常划算，但前提是被隐藏的部分确实不是项目必须经常修改的部分。

本节参考文献：
[3] IBM术语比较 <https://www.ibm.com/cn-zh/think/topics/low-code-vs-no-code> 摘录：“对超自动化和 IT 现代化的需求在增长，但企业一直难以跟上这些趋势，因为目前拥有开发者人才的数量有限。 许多 IT 项目由于缺乏具备专业技术技能的资源而被搁置在 待处理 文件夹中。 因…”
[4] Google Cloud比较 <https://cloud.google.com/discover/low-code-vs-no-code?hl=zh-CN> 摘录：“不妨将这些开发方法的差异比作建造厨房。 虽然这两种方法都优先考虑速度和易用性，但它们满足了不同的需求，服务于不同类型的用户。 目标用户 专业开发者 业务用户/主题专家 主要界面 可视化…”
[5] Gartner定义 <https://www.gartner.com/en/newsroom/press-releases/2022-12-13-gartner-forecasts-worldwide-low-code-development-technologies-market-to-grow-20-percent-in-2023> 摘录：“Webinar 5 Game-Changing AI and Innovation Trends for Global CIOs Register Now ( Webinar Ctrl…”
[6] Power Platform系统研究 <https://doi.org/10.3390/info17010046> 摘录：“Figure 6. Low-code Power Automate flow for automated PDF generation and email distribution.…”
[7] Cigref企业工作组报告 <https://www.cigref.fr/wp/wp-content/uploads/2023/02/Cigref-EN-New-Low-Code-No-Code-development-practices-December-2022-v2.pdf> 摘录：“New Low Code/No Code development prac�ces Unlocking value by controlling risks December 2022…”

### 比较基线必须包含测试、运维和退出

**传统不等于从零。**合理的传统开发基线，是专业团队使用框架、组件、自动化测试和开发运维协作，而不是每项功能都重新手写。比较的流程仍是需求分析、设计、编码、测试、部署、维护和持续改进。[8] 低代码的优势应相对于这条完整链条判断。

**效率要分三层。**开发周期是从需求进入到验收上线的日历时间。投入工时是参与者付出的人小时，生产率则是单位工时完成的功能产出。缩短工期、减少开发者工时和增加业务价值，可以同时发生，也可能只发生其中一种。

**成本要算全程。**总拥有成本，即TCO，应覆盖首次交付、许可、运行资源、集成、测试、维护、升级、培训、治理和退出。ISBSG在给出明显生产率优势的同时，专门要求另外考虑许可证、云消耗、维护和支持。[9] 只比较开发人员工资，会系统性高估平台带来的净节省。

**周期背景也要分场景。**艾瑞与数睿数据合作的2023年中国企业级无代码白皮书，将传统企业项目周期描述为数月至1—2年。[10] 这说明长交付链条确实存在，但具体选型仍应回到同范围项目，而不是拿一个简单表单去对照一个多年核心系统。

本节参考文献：
[8] Microsoft开发方式比较 <https://www.microsoft.com/en-us/power-platform/products/power-apps/topics/low-code-no-code/low-code-vs-traditional-development> 摘录：“How low-code and traditional app development differ Low-code development differs from tradi…”
[9] ISBSG生产率报告 <https://www.isbsg.org/wp-content/uploads/2021/08/Short-Paper-2021-06-Productivity-of-Low-Code-projects.pdf> 摘录：“Analysis of Productivity of Projects Developed in Low Code Development Technology Published…”
[10] 中国企业级无代码白皮书 <https://pdf.dfcfw.com/pdf/H3_AP202304191585562131_1.pdf?1681902388000.pdf> 摘录：“此时，企业仍应回到 树立目标 和 盘点资源 的环节上去，想明白企业的核心竞争力到底是什么， 以及该如何进行内外部分工。 如果软企确认行业认知、算法等才是核心竞争力，则又进入下一步的问…”

### 四个动因，最终汇成同一个决策问题

**增长使选择重要。**低代码已经不是只用于演示原型的小众工具。企业开始围绕它安排平台投资、团队分工和应用组合，这使错误选择具有持续影响，而不只是一次开发工具选错。

**速度不代表净节省。**应用更早上线，可以提前创造收入或减少业务等待。与此同时，后续许可、接口维护和升级回归，也可能吃掉前期收益。问题的价值正在于识别这两条不同的成本曲线。

**分歧反映责任。**管理者常先看到交付积压和人员约束，开发者则更直接承担调试、变更和事故责任。把这种差异解释为“管理者懂业务、开发者抵触新工具”，会错过真正的组织问题。

**预测影响长期投入。**如果未来只是按场景扩散，企业就应保留专业开发能力和接口边界。如果误判为全面替代，便可能过早削减架构、测试和维护投入。Microsoft自身也把低代码定位为传统开发的补充，而不是替代品。[8]

**本节判断。**低代码/无代码的价值，应以“同等业务结果下的生命周期净收益”衡量，而不是以界面上少了多少代码衡量。

本节参考文献：
[8] Microsoft开发方式比较 <https://www.microsoft.com/en-us/power-platform/products/power-apps/topics/low-code-no-code/low-code-vs-traditional-development> 摘录：“How low-code and traditional app development differ Low-code development differs from traditional app development in that it extends the ability to create apps or websites to a larger swath of people. While traditional coding requires professional developers with…”

## 二、行业趋势与流程影响：采用正在扩大，工作正在重新分配

本节参考文献：
[8] Microsoft开发方式比较 <https://www.microsoft.com/en-us/power-platform/products/power-apps/topics/low-code-no-code/low-code-vs-traditional-development> 摘录：“How low-code and traditional app develo…”

### 全球扩张明确，但采用率有不同分母

**战略采用在上升。**KPMG于2025年发布的报告，主要使用2024年2170家企业的IT与业务高管样本。其中，37%把低代码置于软件开发战略核心，高于此前调查中的20%和31%。[11]

| 调查对应年份 | 样本规模 | 低代码处于开发战略核心 | 变化 |
|---|---:|---:|---|
| 2022年 | 715家企业 | 20% | 较早阶段 |
| 2023年 | 2000家企业 | 31% | 较上年增加11个百分点 |
| 2024年 | 2170家企业 | 37% | 较上年增加6个百分点 |

**区域节奏不同。**在KPMG报告明确列出的四个区域中，ASPAC，即亚洲及太平洋地区，战略采用比例最高。美国接近，欧洲和中东相对较低。[11]

| 四区域排序 | 区域 | 区域样本数 | 战略核心比例 |
|---|---|---:|---:|
| 1 | ASPAC | 447家企业 | 43% |
| 2 | 美国 | 638家企业 | 41% |
| 3 | 中东 | 214家企业 | 30% |
| 4 | 欧洲 | 641家企业 | 29% |

**扩散仍是分阶段。**同一调查中，18%已经实施首批项目，17%还在评估。计划启动者又分为未来12个月和未来2—5年两组。这种分布更像企业逐步扩大工具组合，而不是同时完成技术栈切换。[11]

| 2024年采用状态 | 受访企业比例 | 实际含义 |
|---|---:|---|
| 已成为开发战略核心 | 37% | 已制度化采用 |
| 已实施首批项目 | 18% | 进入实际交付 |
| 仍处于评估阶段 | 17% | 正在判断适配性 |
| 计划未来12个月启动 | 16% | 近期项目储备 |
| 计划未来2—5年启动 | 7% | 中期采用意向 |
| 可以想象未来使用 | 4% | 尚处于初步意向 |

**不同采用率并不冲突。**Mendix委托的2021年六国调查中，77%的受访组织以某种方式使用低代码。样本为2025名IT领导者和软件开发者，来自员工数至少50人的组织。[12] Forrester的市场展望文章则称，87%的企业开发者至少在部分工作中使用低代码。[13]

| 指标 | 比例 | 分母与时间口径 | 它衡量什么 |
|---|---:|---|---|
| 以某种方式使用低代码 | 77% | Mendix，2021年六国组织样本 | 是否接触或采用 |
| 将低代码置于战略核心 | 37% | KPMG，2024年企业样本 | 采用的战略深度 |
| 至少部分工作使用低代码 | 87% | Forrester展望所引开发者调查 | 开发者工具使用 |

**样本不能混成普查。**Mendix 2021年的美国采用比例为80%，中国为75%，欧洲为74%。欧洲样本来自英国、德国、比利时和荷兰。[12] 这些结果说明扩散跨越多个地区，也说明“已经使用”和“已成为战略核心”回答的是不同问题。

**增长也受样本结构影响。**KPMG的2024年样本中，信息与通信技术行业占48%，员工数500—4999人的企业占55.4%。[11] 因而，这组结果最直接描绘的是具备软件开发活动的企业，而不是把所有行业、所有规模企业等权平均后的全球比例。

本节参考文献：
[11] KPMG全球调查 <https://assets.kpmg.com/content/dam/kpmgsites/sa/pdf/2025/accelerating-digital-transformation-with-ai-and-low-code.pdf.coredownload.inline.pdf> 摘录：“11 Outlook development. are potentially missing out on these benefits. Study design and sample © 2025 Copyright owned by one or more of the KPMG International entities. KPMG International entities provide no services to clients. All rights reserved. name and logo are trademarks…”
[12] Mendix 2021调查 <https://www.mendix.com/wp-content/uploads/Mendix_2021_State_of_LowCode_Whitepaper.pdf> 摘录：“THE STATE OF LOW-CODE 2021: A LOOK BACK, THE LIGHT AHEAD 12 THE STATE OF LOW-CODE 2320: A LOOK BACK, THE LIGHT AHEAD 13 COVID-19 has accelerated the shift to low-code The pandemic has prompted different ways of working to meet the changing needs of customers, workers, and emplo…”
[13] Forrester市场展望 <https://www.forrester.com/blogs/the-low-code-market-could-approach-50-billion-by-2028/> 摘录：“A $13-Billion Market For Low-Code And DPA Platforms After analyzing relevant data from over 100 vendors, Forrester estimates that the combined low-code and digital process automation (DPA) market reached $13.2 billion by the end of 2023. This represents a growth rate of roughly…”

### 市场规模证明扩张，不能替代生产率证据

**三个金额不能相加。**Gartner、Forrester和IDC使用不同市场范围。它们共同支持行业扩张，但金额差异本身并不说明谁的统计更准确，更不能拼成一条连续增长曲线。

| 统计机构 | 市场范围 | 金额与时期 | 增长表述 |
|---|---|---|---|
| Gartner | 全球低代码开发技术 | 2023年预测269亿美元 | 较2022年增长19.6% |
| Forrester | 低代码加数字流程自动化DPA | 2023年底估计132亿美元 | 回顾2019年以来约21%的增长率 |
| IDC | 智能开发技术加低代码/无代码 | 2024年323亿至2029年2254亿美元 | 报告CAGR约47.4% |

**统计边界解释差异。**Gartner明确将无代码应用平台纳入低代码应用平台市场，并包含其他低代码开发技术。[5] Forrester把低代码与DPA合并，分析了100多家供应商的数据。[13] IDC的范围进一步包括智能开发技术。[14]

**增长率应与端点对应。**IDC给出的323亿至2254亿美元，跨越2024—2029年的五个年度。按公开端点计算，复合年增长率约为47.5%，即“（2254÷323）的五次方根减1”；与报告约47.4%的表述接近。[14] 这里的高速增长，包含智能开发工具扩张，并不全部等于可视化低代码应用收入。

**市场增长不是工程结果。**企业愿意购买平台，可能因为交付积压、业务自助需求或AI集成，也可能因为现有生态带来便利。收入增长能够证明商业采用增强，却不能直接证明缺陷减少、返工下降或维护更便宜。工程收益仍要回到项目和任务层面比较。

本节参考文献：
[5] Gartner定义 <https://www.gartner.com/en/newsroom/press-releases/2022-12-13-gartner-forecasts-worldwide-low-code-development-technologies-market-to-grow-20-percent-in-2023> 摘录：“Webinar 5 Game-Changing AI and Innovation Trends for Global CIOs Register Now ( Webinar Ctrl+Alt+Cloud: Rebooting Your IT Career for What’s Ne…”
[13] Forrester市场展望 <https://www.forrester.com/blogs/the-low-code-market-could-approach-50-billion-by-2028/> 摘录：“A $13-Billion Market For Low-Code And DPA Platforms After analyzing relevant data from over 100 vendors, Forrester estimates that the combined…”
[14] IDC全球预测 <https://my.idc.com/getdoc.jsp?containerId=US53966325> 摘录：“Title: Worldwide Intelligent Developer Technologies and Low-Code and No-Code Forecast, 2025–2029 containerId=US53966325 Markdown Content: This…”

### 部署已经规模化，成功案例共同强调治理与复用

**采用不止是试验。**PG&E、Jabil和Petrobras的案例，分别显示了大型应用组合、全球制造现场和遗留应用现代化中的实际部署。下面的规模均为供应商发布的客户案例口径。

| 企业与平台 | 实施期 | 部署范围 | 组织方式 |
|---|---|---|---|
| PG&E／Power Platform | 四年累计 | 2000余应用、4200个流程、315余方案 | 卓越中心赋能业务开发 |
| Jabil／Mendix | 自2022年采用 | 近100个应用，覆盖25余国、100余基地 | 共用组件加现场定制 |
| Petrobras／OutSystems | 八个月开发期 | 48个应用 | 中央治理支持分散团队 |

**复用解释规模价值。**Jabil的应用用于优化工作流、扩展制造执行系统，即MES，并结合生成式AI。其共同组件覆盖设计、功能和集成，现场团队再调整用户体验。案例报告累计避免成本1450万美元。[15] 这里的价值不是“所有工厂使用完全一样的应用”，而是“相同能力只建设一次，差异化保留在适当层次”。

**治理解释持续运行。**PG&E把应用、流程组合成业务解决方案，并建立卓越中心，简称CoE，负责赋能、规范和治理。案例描述了数据保护、监控和测试沙箱。[16] 这说明规模化公民开发并不是让业务人员脱离IT管理，而是改变IT提供支持的方式。

**旧系统同样有成本。**Petrobras在采用OutSystems前，面对2000余个使用.NET、Java、Delphi、Flex和Notes等技术开发的遗留应用。客户将其描述为现代化和新增功能的阻力。[17] 因此，正确比较不是“低代码有依赖，传统代码没有依赖”，而是两种具体架构各自的维护负担。

本节参考文献：
[15] Jabil客户案例 <https://www.mendix.com/customer-stories/jabil-delivers-100-mendix-apps-improving-global-site-operations-promoting-hyper-customization/> 摘录：“Jabil Delivers 100+ Mendix Apps Improving Global Site Operations & Promoting Hyper-Customization Manufacturing enterprises must strike a delicate bala…”
[16] PG&E客户案例 <https://www.microsoft.com/en/customers/story/1709539049606899869-pacific-gas-and-electric-microsoft-power-apps-energy-usa> 摘录：“Pacific Gas and Electric Company (PG&E) is one of the largest combined natural gas and electric energy companies in the United States. The company has…”
[17] Petrobras案例 <https://www.outsystems.com/case-studies/petrobras-agile-development> 摘录：“Petrobras' New Dev Culture Proves Even Giants Can Be Nimble Petrobras is Brazil's state-owned oil and gas corporation and one of the largest energy co…”

### 需求分析：反馈更直接，但业务规则仍须澄清

**原型缩短表达距离。**低代码可以把流程、业务规则和界面直接做成可运行原型。无代码进一步让业务专家直接配置和反馈。相较文字需求在多角色之间传递，这有助于及早暴露理解偏差。[3]

**收益来自减少转译。**例如，审批人不必只阅读“金额达到某条件后升级审批”的文字，可以直接操作流程并检查结果。艾瑞白皮书把这种机制概括为增加沟通带宽、提高表达保真度和缩短反馈时间。[10] 它改善的是需求沟通，不是自动替企业解决规则冲突。

**更快也会扩大范围。**Abendroth与Bender于2025年发表的ERP研究，基于2021年末11次访谈，指出低代码项目范围容易动态演化。[18] 当演示很容易修改，需求方也更容易持续追加要求。此时瓶颈会从“做不出原型”转为“谁决定范围、谁批准变更”。

本节参考文献：
[3] IBM术语比较 <https://www.ibm.com/cn-zh/think/topics/low-code-vs-no-code> 摘录：“对超自动化和 IT 现代化的需求在增长，但企业一直难以跟上这些趋势，因为目前拥有开发者人才的数量有限。 许多 IT 项目由于缺乏具备专…”
[10] 中国企业级无代码白皮书 <https://pdf.dfcfw.com/pdf/H3_AP202304191585562131_1.pdf?1681902388000.pdf> 摘录：“www.iresearch.com.cn 10 穷则思变——供方开发模式之变 从瀑布式到圆桌式，从高代码到数据驱动的无代码 随着理念的…”
[18] ERP访谈研究 <https://lswi.de/assets/downloads/publikationen/109/Abendroth_Bender_2025_Bridging_the_Gap_Low-Code_Platforms_and_the_Future_of_ERP.pdf> 摘录：“2021 IEEE/ACM 18th International Conference on Mining Software Repo…”

### 编码或配置：重复实现减少，复杂度转入模型与扩展

**实现环节提速最明确。**2022年的IEEE实验中，低代码开发阶段耗时504分钟，Django/Python方式为1369分钟。按这两个工时计算，低代码减少865分钟，约减少63.2%。[1]

**标准构件减少重复。**表单、列表、权限入口、基础数据操作和审批流，可以通过平台组件组装。专业开发者不再逐项实现这些通用能力，而把精力集中到特殊业务逻辑、接口与性能要求。无代码在标准构件范围内进一步降低实现门槛。[3]

**配置仍然表达程序。**一个包含多重条件、状态转换和异常分支的可视流程，仍然承载复杂业务逻辑。规则越多，团队越需要模块化、命名、依赖管理和版本控制。若只是把大量条件从文本代码搬成图形节点，复杂度并没有消失。

本节参考文献：
[1] IEEE受控实验 <https://doi.org/10.1109/mitp.2022.3189880> 摘录：“U U C P=U A W+U U C W.(1) View Source! Image 1: Right-click on figure for MathML and additional f…”
[3] IBM术语比较 <https://www.ibm.com/cn-zh/think/topics/low-code-vs-no-code> 摘录：“对超自动化和 IT 现代化的需求在增长，但企业一直难以跟上这些趋势，因为目前拥有开发者人才的数量有限。 许多 IT 项目由于缺乏具备专业技术技能的资源而被搁置在 待处理 文件夹中。 因此，运营效…”

### 测试：机械工作可减少，业务正确性不会自动获得

**测试是转移而非取消。**低代码减少部分手写代码错误，并可内置依赖检查和发布验证。无代码的测试重点则更多落在配置、数据流和权限上。IBM特别强调，无代码仍须保证配置和数据流正确。[3]

**实验显示整体节省。**IEEE实验中，开发加配置、测试的总耗时分别为716分钟和2303分钟。用总耗时减去开发阶段，得到配置与测试等剩余工作约212分钟和934分钟，这是据原始工时计算的残差估计。[1] 它说明实现之外的工作也可减少，但不能把全部残差都当成纯测试时间。

**覆盖能力比按钮重要。**Konersmann在2024年的低代码PaaS再工程分析中，指出所讨论平台方式的自动化测试和导出工件存在障碍。[19] 对企业而言，关键不是能否点击“运行测试”，而是关键业务路径、连接器异常和升级回归是否能持续验证。

本节参考文献：
[3] IBM术语比较 <https://www.ibm.com/cn-zh/think/topics/low-code-vs-no-code> 摘录：“对超自动化和 IT 现代化的需求在增长，但企业一直难以跟上这些趋势，因为目前拥有开发者人才的数量有限。 许多 IT 项目由于缺乏具备专业技术…”
[1] IEEE受控实验 <https://doi.org/10.1109/mitp.2022.3189880> 摘录：“U U C P=U A W+U U C W.(1) View Source! Image 1: Right-click on figure…”
[19] 低代码测试与再工程分析 <https://fb-swt.gi.de/fileadmin/FB/SWT/Softwaretechnik-Trends/Verzeichnis/Band_44_Heft_2/WSRE2024_01_Konersmann.pdf> 摘录：“Challenges of Low Code PaaS Environments for Future Software Reenginee…”

### 部署：发布步骤压缩，生产责任仍由企业承担

**平台能压缩发布操作。**低代码平台可以统一环境配置、依赖处理和应用发布。2026年的企业观察，把部署步骤列为稳定流程型应用中由平台承担的重要工作。[2] 无代码也能把限定范围应用快速分享给用户，例如Google展示的团队反馈应用，可从自然语言生成并发布可运行页面。[4]

**整体工期不等于部署工时。**Petrobras案例报告，应用从原先预计的6—8个月缩短到3个月交付。[17] 按端点计算，这是交付周期减少50%—62.5%。其中包含实现、协作和发布的共同变化，不应全部归因于部署按钮。

**风险集中到共同底座。**统一发布可以减少手工操作差异，但也使更多应用共享平台运行时、环境和连接器。环境分离、访问控制、备份、回滚和生产审批，仍应作为上线条件。Rierino对跨部门采用的建议，就包括开发、预发布和生产环境分离。[20]

本节参考文献：
[2] 企业部署观察 <https://www.sci-open.net/index.php/JTIE/article/view/16625> 摘录：“Journal of Software: Evolution and Process, 37(2), e…”
[4] Google Cloud比较 <https://cloud.google.com/discover/low-code-vs-no-code?hl=zh-CN> 摘录：“不妨将这些开发方法的差异比作建造厨房。 虽然这两种方法都优先考虑速度和易用性，但它们满足了不同的需求，服…”
[17] Petrobras案例 <https://www.outsystems.com/case-studies/petrobras-agile-development> 摘录：“Petrobras' New Dev Culture Proves Even Giants Can Be…”
[20] 跨团队平台能力 <https://rierino.com/blog/low-code-strategy-3-enterprise-paths-scale> 摘录：“Low code is no longer confined to experimental initi…”

### 迭代：模板内修改容易，越界变更可能突然变贵

**标准变更具有优势。**IEEE实验的维护阶段，要求修改现有功能并新增功能。低代码耗时233分钟，代码方式为573分钟，按工时计算减少约59.3%。[1] 这支持标准业务应用中短周期变更的效率收益。

**边界外成本不连续。**无代码修改字段、页面和简单流程，通常可以直接在平台中完成。但一旦需求涉及平台不支持的事务、数据验证或外部协议，修改可能升级为专业扩展、数据迁移甚至重建。迭代成本因此不一定随功能数量平稳增加。

**反馈速度不是唯一目标。**低代码越容易发布，越需要明确哪些配置能由业务用户自行调整，哪些变化需要工程评审。否则，快速变更可能绕开原本应有的数据、安全和集成检查。Cigref将生命周期责任与专门治理视为持续采用的重要条件。[7]

| 生命周期环节 | 传统专业代码基线 | 低代码变化 | 无代码变化 |
|---|---|---|---|
| 需求分析 | 文档、设计与专业团队转译 | 可运行模型促进协作 | 业务用户直接参与原型 |
| 编码或配置 | 代码与框架实现 | 组件组装加特殊代码 | 模板和配置实现 |
| 测试 | 代码、接口与系统验证 | 减少机械工作，验证模型与扩展 | 验证配置、权限与数据流 |
| 部署 | 团队组织发布与环境管理 | 平台统一部分发布步骤 | 快速发布到限定用户群 |
| 迭代 | 修改代码、测试、发布 | 标准变更快，越界扩展增加 | 模板内快，超边界需升级路线 |

**本节判断。**低代码/无代码对传统流程的影响很大，但主要表现为工作重新分配；需求决策、质量保证和生产责任并未消失。

本节参考文献：
[1] IEEE受控实验 <https://doi.org/10.1109/mitp.2022.3189880> 摘录：“U U C P=U A W+U U C W.(1) View Source! Image 1: Right-click on figure for MathML and additional features. ( Adjustment of UUCP, considering a set of technical and environmental factors represented by the tec…”
[7] Cigref企业工作组报告 <https://www.cigref.fr/wp/wp-content/uploads/2023/02/Cigref-EN-New-Low-Code-No-Code-development-practices-December-2022-v2.pdf> 摘录：“New Low Code/No Code development prac�ces Unlocking value by controlling risks December 2022 New Low Code/No Code development Unlocking value by controlling risks December 2022 Intellectual property rights A…”

## 三、效率是否真正提高：独立证据支持提速，但不是统一的行业倍数

本节参考文献：
[1] IEEE受控实验 <https://doi.org/10.1109/mitp.2022.3189880> 摘录：“Title: Low-Code Versus Code-Based Softw…”
[7] Cigref企业工作组报告 <https://www.cigref.fr/wp/wp-content/uploads/2023/02/Cigref-EN-New-Low-Code-No-Code-development-practices-December-2022-v2.pdf> 摘录：“New Low Code/No Code development prac�c…”

### 项目库、同需求实验与企业观察，分别回答不同问题

**效率不是纯宣传。**Gao、Fagerholm与Toivanen发表于2026年的系统综述，分析了2021年至2025年初的226篇文献。作者认为，已有充分证据支持低代码加快开发；质量和复杂度结果则依赖情境。[21]

| 研究与时期 | 比较对象 | 低代码结果 | 传统结果 | 对照含义 |
|---|---|---|---|---|
| ISBSG，2021年 | 57个低代码、1921个传统项目 | 中位1.8小时/功能点 | 中位8.3小时/功能点 | 实际项目投入参照 |
| IEEE，2022年 | 同一管理信息系统 | 含测试716分钟 | 含测试2303分钟 | 同需求实现比较 |
| IEEE，2022年 | 同一功能变更任务 | 233分钟 | 573分钟 | 短期迭代比较 |
| NexusBRaNT，2023年 | 信息与工作流系统 | 47.5工时 | 888工时 | 特定模型驱动案例 |
| JTIE，2026年 | 7个部署、18个月 | 稳定流程交付时间减少57% | 传统交付基线 | 企业场景中的持续观察 |

**项目库差距很大。**ISBSG比较了Mendix、OutSystems项目与.NET、Java项目。功能点用于衡量用户可见的功能规模，交付率PDR则表示每功能点投入多少小时，数值越低越好。[9]

**计算应区分表述。**ISBSG报告将生产率优势概括为约4.5倍。直接使用其公开中位数计算，8.3÷1.8约为4.61倍，每功能点工时减少约78.3%。这是中位交付率之比，并不是每个项目都能获得4.61倍提升。

**同需求实验更接近工具比较。**2022年的IEEE实验，用OutSystems和Django/Python实现同一管理信息系统。开发阶段规模为134个用例点，即UCP；维护任务为49个UCP。两名程序员分别具有两年以上OutSystems经验和五年以上Django/Python经验。[1]

**全程合计仍然领先。**把该实验的开发与维护两阶段相加，低代码为949分钟，代码方式为2876分钟。按相同功能产出计算，生产率比值约3.03，工时减少约67.0%。这一计算同时纳入了初始实现和一轮功能演进，而不只挑选编码最快的片段。

**企业观察补上场景差异。**JTIE的18个月观察，把明显收益放在稳定流程型应用上。平台承担表单、审批、基本数据操作和部署后，交付时间减少57%；算法型和集成密集型系统的优势则收窄。[2] 这与前述实验共同指向一个机制：标准组件覆盖的工作越多，重复实现越少。

**极高收益有具体条件。**NexusBRaNT实验用执行DEMO模型的平台实现信息与工作流系统。传统方式投入888工时，低代码为47.5工时；按公开工时计算，减少约94.65%。[22] 这个案例说明，在业务模型与平台表达高度契合时，收益可以远大于一般项目库差距。

**任务匹配解释差异。**表单和审批系统包含大量相似结构，平台可以集中实现。复杂算法则往往没有合适现成构件，团队仍需自行设计。因而，3倍、4.5倍和接近95%的工时减少，描述的是不同任务与比较设计，不能排列成平台能力排行榜。

本节参考文献：
[21] 系统性文献综述 <https://aaltodoc.aalto.fi/items/65c94b6a-2f70-4d7c-b52e-7cc0ceae5250> 摘录：“aalto1 untyped-item.component.html What does current research say about the viability of low-code development? A systematic literature review Access rights C…”
[9] ISBSG生产率报告 <https://www.isbsg.org/wp-content/uploads/2021/08/Short-Paper-2021-06-Productivity-of-Low-Code-projects.pdf> 摘录：“Analysis of Productivity of Projects Developed in Low Code Development Technology Published by the International Software Benchmarking Standards Group Functi…”
[1] IEEE受控实验 <https://doi.org/10.1109/mitp.2022.3189880> 摘录：“U U C P=U A W+U U C W.(1) View Source! Image 1: Right-click on figure for MathML and additional features. ( Adjustment of UUCP, considering a set of technica…”
[2] 企业部署观察 <https://www.sci-open.net/index.php/JTIE/article/view/16625> 摘录：“Journal of Software: Evolution and Process, 37(2), e2680. Kumar, A., & Patel, N. Productivity measurement in low-code development: A controlled experiment. E…”
[22] NexusBRaNT实验 <https://doi.org/10.1109/cbi58679.2023.10187470> 摘录：“Title: Traditional vs. low-code development: comparing needed effort and system complexity in the NexusBRaNT experiment Markdown Content: Download PDF ( You…”

### 工时下降，不一定按相同比例缩短产品周期

**等待也影响交付。**项目工期除了开发，还包括业务审批、数据接入、采购、安全评审和用户验收。平台减少编码工时后，原本次要的等待环节可能成为新瓶颈。企业若不调整协作方式，开发团队变快，整体上线速度仍可能改善有限。

**两个Mendix项目形成对照。**2024年的瑞士研究，比较同一服务商参与的两个项目。城市废弃物信息应用在20个工作日完成；医疗保险机构的企业客户报价流程，实际周期为24个月。[23] 研究者在前者明显观察到时间与成本收益，在后者则较少。

**区别不在平台名称。**城市应用由委托方与一名开发者组成核心实施团队，并以两日节奏评估、调整、测试和批准。保险流程涉及更大组织和更复杂环境。[23] 这个比较说明，平台提速必须通过决策和反馈链条，才能转化成产品交付提速。

**人员节省也有条件。**减少某项任务工时，不一定意味着减少同等比例编制。释放的开发能力可能被用于积压需求、新应用和复杂定制。Microsoft明确把这种重新分工列为低代码价值：让专业开发者少做重复劳动，转向创新和定制项目。[8]

本节参考文献：
[23] 瑞士两项目研究 <https://doi.org/10.1365/s40702-024-01095-y> 摘录：“Zusammenfassung Die Fähigkeit, benötigte Softwareapplikationen effizient bereitstellen zu können, ist für Unternehmen heute ein kritischer…”
[8] Microsoft开发方式比较 <https://www.microsoft.com/en-us/power-platform/products/power-apps/topics/low-code-no-code/low-code-vs-traditional-development> 摘录：“How low-code and traditional app development differ Low-code development differs from traditional app development in that it extends the a…”

### 质量与返工：更少手写错误，不等于更少系统问题

**实验没有显示提速换质量。**IEEE实验按规格符合度和软件错误进行最终评估，低代码为85.79%，代码方式为81.37%，差4.42个百分点。[1] 在这个低复杂度管理系统中，工时优势没有伴随较低的最终评分。

**评分不是缺陷率。**这两个百分比衡量的是论文的综合质量评估，不是每千行代码缺陷数，也不是生产故障率。它支持“该案例能够更快完成且质量相近”，而不是“低代码普遍减少某一固定比例缺陷”。

**平台自身也会出错。**Liu等人的研究分析了OutSystems、Mendix、Appsmith和Budibase四个平台的974个已确认缺陷。约60%涉及应用设计与规格阶段，超过37%使平台出现缺少显式信号的异常行为。[24]

**错误会跨层传播。**应用作者可能正确配置了业务规则，却仍受到平台组件或连接器行为影响。因此，低代码团队不仅要验证自己的逻辑，还要理解平台版本、组件和运行时的变化。可视化降低了部分错误入口，也增加了对共同底层能力的依赖。

**返工要看工作结构。**返工率可以按返工工时占总工时的比例衡量，而修复负担衡量的是问题处理投入。JTIE报告的约1.6倍属于后者。[2] 它能作为复杂项目后期负担的风险参照，不应改写成“返工率提高60个百分点”。

**传统方式也会积债。**2026年的Budibase与Java Spring实验，让13名计算机科学研究生完成5个维护和功能扩展场景。Spring用户完成率为100%，Budibase在复杂业务逻辑与数据验证任务中出现较多放弃；同时，传统实现也暴露了高耦合和模块化不足等结构性技术债。[25]

**反例说明工程仍重要。**低代码容易积累平台变通方案，传统代码容易积累结构耦合。二者不是“有技术债”和“无技术债”的对照，而是不同形式的债务。真正需要比较的是修改、定位和验证同一类变化时，哪种结构更容易维持。

本节参考文献：
[1] IEEE受控实验 <https://doi.org/10.1109/mitp.2022.3189880> 摘录：“U U C P=U A W+U U C W.(1) View Source! Image 1: Right-click on figure for MathML and additional features. ( Adjustmen…”
[24] IEEE平台缺陷研究 <https://doi.org/10.1109/tr.2023.3295009> 摘录：“punumber=24) Volume: 73 Issue: 1 ( isnumber=10460370&punumber=24) ( What's Wrong With Low-Code Development Platforms?…”
[2] 企业部署观察 <https://www.sci-open.net/index.php/JTIE/article/view/16625> 摘录：“Journal of Software: Evolution and Process, 37(2), e2680. Kumar, A., & Patel, N. Productivity measurement in low-code…”
[25] Budibase与Spring实验 <https://dspace.lib.uom.gr/handle/2159/34641> 摘录：“Please use this identifier to cite or link to this item: Author: Χρυσοχοΐδης, Αναστάσιος Title: Software maintainabil…”

### 无代码的主要效率价值，是让业务知识更快进入实现

**门槛降低确有意义。**无代码让熟悉业务但不熟悉编程的人，能够直接制作表单、简单工作流和原型。其效率价值首先体现在参与范围和反馈速度，而不是把专业开发者生产率倍数直接复制给业务用户。[3]

**业务用户省去部分排队。**许多Excel替代工具和部门流程，在中央IT排期中优先级不高。让需求方在受治理范围内自行构建，可以使原本长期等待的需求更快得到满足。[3] 这里的收益，可能是从“暂时不做”变成“可以交付”，而不是简单削减一张既有开发账单。

**专业知识没有清零。**业务用户节省了语法学习，但仍要学习条件逻辑、数据关系、权限和生命周期管理。复杂工具配置甚至可能重新形成专业分工。[5] 所以，无代码降低的是部分实现门槛，不是所有软件责任的门槛。

本节参考文献：
[3] IBM术语比较 <https://www.ibm.com/cn-zh/think/topics/low-code-vs-no-code> 摘录：“对超自动化和 IT 现代化的需求在增长，但企业一直难以跟上这些趋势，因为目前拥有开发者人才的数量有限。 许多 IT 项目由于缺乏具备专业技术技能的资源而被搁置在 待处理 文件夹中。 因此，运营效率持续…”
[5] Gartner定义 <https://www.gartner.com/en/newsroom/press-releases/2022-12-13-gartner-forecasts-worldwide-low-code-development-technologies-market-to-grow-20-percent-in-2023> 摘录：“Webinar 5 Game-Changing AI and Innovation Trends for Global CIOs Register Now ( Webinar Ctrl+Alt+Clo…”

### 厂商数字有参考价值，但要分清节省的是什么

**客户收益分属不同层次。**厂商调查和案例提供了规模化应用的具体线索，但开发速度、员工操作时间和投资回报是不同指标。把它们都写成“开发效率提高”，容易夸大工程效果。

| 来源与案例 | 报告结果 | 指标实际对应 | 实际意义 |
|---|---|---|---|
| Mendix，2021年委托调查 | 成本下降53%，开发速度提高56% | 受访低代码用户自报 | 用户感知的项目收益 |
| Petrobras／OutSystems案例 | 效率提高60%，个别达90% | 客户对高代码的比较 | 现代化交付收益 |
| PG&E／Microsoft案例 | 每年约52.7万小时、近7500万美元节省 | 业务方案年化收益 | 企业运营改善 |

**PG&E不是开发工时案例。**其52.7万小时，是应用与流程改善业务操作后报告的年度节省。7500万美元也是客户案例中的年化收益表达。[16] 这可以说明平台支撑了有价值的业务自动化，却不能当成“开发团队每年少工作52.7万小时”。

**调查中的速度也需保留原义。**Mendix 2021年调查称项目“快56%”，同时报告开发成本节省53%。[12] “速度快56%”与“耗时减少56%”并不是同一数学关系，因此这里保留其原始问法，不作等价换算。

**本节判断。**低代码确实提高了适配任务的开发效率；从工时到产品周期，再到企业收益，每向外推一层，都需要加入相应的组织和成本条件。

本节参考文献：
[16] PG&E客户案例 <https://www.microsoft.com/en/customers/story/1709539049606899869-pacific-gas-and-electric-microsoft-power-apps-energy-usa> 摘录：“Pacific Gas and Electric Company (PG&E) is one of the largest combined natural gas and electric energy companies in the United States. The company has enabled over 4,300 Power Platform maker…”
[12] Mendix 2021调查 <https://www.mendix.com/wp-content/uploads/Mendix_2021_State_of_LowCode_Whitepaper.pdf> 摘录：“53% and are 56% faster. The benefits have flowed to the top line, too. Customer apps built using low-code increased customer revenues by an average of 58%. Increasingly, low-code solutions a…”

## 四、维护成本何时反而更高：复杂性没有消失，只是换了位置

本节参考文献：
[16] PG&E客户案例 <https://www.microsoft.com/en/customers/story/1709539049606899869-pacific-gas-and-electric-microsoft-power-apps-energy-usa> 摘录：“Pacific Gas and Electric Company (PG&E)…”
[12] Mendix 2021调查 <https://www.mendix.com/wp-content/uploads/Mendix_2021_State_of_LowCode_Whitepaper.pdf> 摘录：“Title: Mendix_2021_State_of_LowCode_Whi…”

### 日常维护与复杂修复，可能出现相反结果

**维护收益取决于变更类型。**标准功能调整中，低代码能复用已有模型和组件，233对573分钟的实验结果支持这种优势。进入算法、异常数据、重度集成和平台扩展后，工作会更多转向调试与后期修复。[1][2]

| 生命周期维度 | 传统专业代码 | 低代码 | 无代码 |
|---|---|---|---|
| 标准功能变更 | 实验573分钟 | 实验233分钟 | 模板内直接调整 |
| 复杂修复负担 | 观察基线1 | 观察报告约1.6倍 | 配置、数据与接口问题转入支持 |
| 升级责任 | 框架、依赖与应用回归 | 平台与自定义扩展交叉回归 | 平台模板与业务配置验证 |
| 集成成本 | 自建接口与适配层 | 标准连接快，非标需扩展 | 少量标准连接更合适 |
| 技术债来源 | 耦合、重复代码、结构退化 | 重复规则、隐藏行为、变通方案 | 应用冗余、数据分散、责任缺位 |
| 扩展与灵活性 | 可直接改变底层行为 | 受运行时边界约束，可代码扩展 | 主要受模板和功能集约束 |
| 厂商锁定 | 依赖框架、云和服务 | 依赖模型、API与平台运行时 | 依赖配置、连接器与平台环境 |
| 生命周期经济性 | 初始工程投入较高 | 标准复用受益，复杂化后成本上升 | 简单范围较轻，关键化后治理加重 |

**修复负担需要分层换算。**若把1.6倍修复负担用于工时预算代理，须先假设修复负担与修复工时同比例。令修复占传统维护工时的比例为s，其他维护活动不变，则总维护工时增幅估算为0.6s。由s在0至1之间，可得0%—60%的条件区间；这是预算敏感性范围，而不是全部维护成本的观测增幅。

**生命周期长度会放大差异。**首次交付节省是一次性的，维护和许可支出会持续发生。一个标准流程若长期保持在平台能力范围内，可以持续受益；一个逐渐变为关键系统的部门工具，则可能不断引入例外逻辑和接口依赖。相同的首发速度，可能对应完全不同的长期经济结果。

本节参考文献：
[1] IEEE受控实验 <https://doi.org/10.1109/mitp.2022.3189880> 摘录：“U U C P=U A W+U U C W.(1) View Source! Image 1: Right-click on figure for MathML and additional features. ( Adjustment of UUCP, considering a set of technical and environmental factors represented by the technical complexity factor (TCF) and the envir…”
[2] 企业部署观察 <https://www.sci-open.net/index.php/JTIE/article/view/16625> 摘录：“Journal of Software: Evolution and Process, 37(2), e2680. Kumar, A., & Patel, N. Productivity measurement in low-code development: A controlled experiment. Empirical Software Engineering, 29(4), 92. Zhang, L., Chen, H., & Liu, M. Comparing defect dens…”

### 可视规则、连接器和变通方案，怎样形成额外工作

**重复规则产生隐性耦合。**多个页面各自复制审批条件，最初看起来比建设共用规则模块更快。业务政策变化时，团队却必须找到所有副本并保持一致。JTIE将重复视觉规则列为修复负担的重要来源。[2]

**隐藏行为提高定位成本。**平台可能自动管理数据更新、事件触发和执行顺序。标准路径运行顺利时，这种抽象很省力；出现边界问题时，开发者却需要先理解平台做了什么，才能判断问题属于应用、连接器还是运行时。问题定位因此可能比代码行数所暗示的更复杂。

**连接器省去的不是全部集成。**一个现成连接器可以处理认证和接口调用，但不会自动统一两套系统的客户编号、状态含义和异常处理。Haapala对Power Platform、OutSystems和Mendix的集成研究，具体指出了连接器文档不足，以及部分集成需要自定义编码的问题。[26]

**ERP知识仍然必要。**Abendroth与Bender的访谈指出，ERP缺少某些业务流程的标准化端点时，低代码集成仍需要大量定制和ERP知识。[18] 因此，“已有ERP连接器”和“已经完成业务集成”不是同一件事。

**自定义不必然是坏债。**把复杂计算封装为清晰接口，由专业代码维护，可以保留平台的流程效率。真正危险的是，为绕过平台限制而把特殊规则散落在多个页面、连接器和扩展里。Rierino建议把可复用组件与部门专用逻辑分开，并记录集成模式。[20]

**架构边界决定后果。**如果平台负责界面与流程，独立服务负责复杂领域逻辑，双方依赖可以被明确管理。若平台模型直接承担所有事务、异常和跨系统状态，任何一个接口变化都可能波及整个应用。混合开发是否划算，取决于是否真正隔离了变化，而不是是否同时用了两种工具。

本节参考文献：
[2] 企业部署观察 <https://www.sci-open.net/index.php/JTIE/article/view/16625> 摘录：“Journal of Software: Evolution and Process, 37(2), e2680. Kumar, A.,…”
[26] 集成开发研究 <https://trepo.tuni.fi/handle/10024/161705> 摘录：“Evaluating low-code platforms for integration development: Benefits,…”
[18] ERP访谈研究 <https://lswi.de/assets/downloads/publikationen/109/Abendroth_Bender_2025_Bridging_the_Gap_Low-Code_Platforms_and_the_Future_of_ERP.pdf> 摘录：“2021 IEEE/ACM 18th International Conference on Mining Software Reposi…”
[20] 跨团队平台能力 <https://rierino.com/blog/low-code-strategy-3-enterprise-paths-scale> 摘录：“Low code is no longer confined to experimental initiatives or isolate…”

### 升级和迁移：平台代管基础设施，也带来新的依赖

**升级并非完全外包。**平台可以统一补丁和运行环境，减少企业逐个维护基础构件的工作。但IBM指出，低代码平台的新版本和补丁，仍须与手动加入的代码共同测试。[3] 扩展越多，升级回归涉及的组合也越多。

**无代码有另一种交换。**模板化功能较少受自定义代码破坏，向后兼容可能更容易。与此同时，业务逻辑更依赖平台允许的配置路径。若未来变更超出这些路径，团队可能需要转换开发方式，而不仅是在原应用里增加一个模块。[3]

**锁定主要发生在运行模型。**Konersmann指出，厂商特定API使低代码PaaS应用难以直接转移到其他平台。[19] 能导出数据，不等于能导出可独立运行的业务逻辑；能拿到某些代码，也不等于脱离原运行时仍可维护。

**迁移案例展示真实工作。**Apvine描述，一家全球工程与咨询公司在三年内建设30多个OutSystems应用，续约成本显著上升后，选择在六个月内迁移到Mendix。迁移涉及自定义API、数据搬迁、工作流和用户体验重构。[27]

**迁移不是平台失败的同义词。**更换平台也可能降低许可成本，改善数据和应用结构。另一个咨询案例描述，美国农业化学品与种子企业把200多个应用迁移到Power Apps，以利用其已有Microsoft许可。[28] 这些案例共同说明，退出能力本身就是选型价值的一部分。

本节参考文献：
[3] IBM术语比较 <https://www.ibm.com/cn-zh/think/topics/low-code-vs-no-code> 摘录：“低代码具备完善的组件库，可扩展至包含繁重业务逻辑的应用程序，并可扩展到企业级规模。 此外，在…”
[19] 低代码测试与再工程分析 <https://fb-swt.gi.de/fileadmin/FB/SWT/Softwaretechnik-Trends/Verzeichnis/Band_44_Heft_2/WSRE2024_01_Konersmann.pdf> 摘录：“Challenges of Low Code PaaS Environments for F…”
[27] OutSystems至Mendix迁移 <https://apvine.com/cases/from-outsystems-to-mendix-a-cost-driven-migration> 摘录：“10 lessons learned from migrating from OutSyst…”
[28] Power Apps迁移案例 <https://www.apexsystems.com/insights/case-study/legacy-app-modernization-power-apps> 摘录：“An American agricultural chemical and seed com…”

### 总拥有成本：用可计算的临界点判断，而不是只看ROI口号

**成本研究并非一边倒。**2024年的专业低代码研究，对8个实证或调查来源进行详细分析。其综合判断是：开发资源节省，与集成、许可证、平台运营、治理和知识建设成本，大体形成抵消；质量、集成和维护表现则随情境变化。[23]

**一笔账可以说明反转。**ISBSG给出过100功能点项目的示例：按低代码1.8小时/功能点、传统8.3小时/功能点计算，分别需要180和830工时。使用其示例中的100美元/小时，首次交付人力成本分别为1.8万和8.3万美元，差额为6.5万美元。[9]

**临界点并不神秘。**在这个明确标为示例的估算中，若同一生命周期内，低代码相对传统的其他增量净成本超过6.5万美元，首次交付的人力优势就被抵消。若评估期取三年、不贴现，等额年度临界点约为2.17万美元，即6.5万÷3。这不是平台报价，而是由公开生产率和示例费率推导的预算边界。

**核算必须避免重复。**已计入首次交付工时的集成或测试，不应再完整计一次。业务用户投入也不应视为免费；他们用于配置、学习和支持的时间，属于组织成本。同样，共享平台固定成本不能全部压在第一个应用上，也不能在每个后续应用中都假定为零。

**统一表达更容易比较。**在相同寿命与功能范围下，可以将成本差写成：

\(\Delta TCO=-S_{\text{首次交付}}+\Delta C_{\text{许可与运行}}+\Delta C_{\text{集成与测试}}+\Delta C_{\text{维护与升级}}+\Delta C_{\text{治理与退出}}\)

**负值才是成本优势。**这里的S是首次交付节省，各项ΔC是低代码相对传统的增量成本。若企业还计入提前上市和运营改善，应把这些列为业务收益，而不是混进工程成本减少。这样才能看清“开发更贵但商业回报更高”，与“开发维护都更便宜”的区别。

本节参考文献：
[23] 瑞士两项目研究 <https://doi.org/10.1365/s40702-024-01095-y> 摘录：“Zusammenfassung Die Fähigkeit, benötigte Softwareapplikationen effizient bereitstellen zu können, ist für Unternehmen heute ein kritische…”
[9] ISBSG生产率报告 <https://www.isbsg.org/wp-content/uploads/2021/08/Short-Paper-2021-06-Productivity-of-Low-Code-projects.pdf> 摘录：“Analysis of Productivity of Projects Developed in Low Code Development Technology Published by the International Software Benchmarking St…”

### 正向财务案例说明：费用上升与净收益增长可以并存

**506%属于具体情景。**OutSystems委托Forrester Consulting在2022年访谈4名决策者，并构建复合组织。三年风险调整模型给出的收益现值为1769万美元，成本现值为292万美元，净现值为1477万美元，ROI约506%。[29]

**模型收益不只是省开发。**该模型同时计入开发节省、继续开发与支持节省、提前上市收入、运营改善提前实现，以及替代旧软件费用。按其细项现值计算，提前上市与提前运营改善合计约1137.70万美元，占收益约64.3%。[29] 因而，506%不能理解为“开发维护费用下降506%”。

**平台账单也会增长。**同一模型随着用户和应用范围扩大，OutSystems年度费用明显上升。这并未阻止模型得出正向净收益，因为覆盖的业务价值同时增加。

| TEI模型年度 | 内部／外部用户 | 在产应用数 | 风险调整平台费用 |
|---|---:|---:|---:|
| 第一年 | 1000／30000人 | 9个 | 705177美元 |
| 第二年 | 2000／60000人 | 22个 | 1049851美元 |
| 第三年 | 3000／100000人 | 39个 | 1598454美元 |

**费用增长要结合分母。**如果应用和用户增加，平台费用上升可能是规模扩大，而非单位效率恶化。反过来，若许可增长快于有效使用和可复用产出，即使每个项目开发很快，整体成本仍会失控。企业需要同时看账单、使用范围和业务结果。

**无代码尤其要管责任。**Cigref警告，未经IT监督的低代码/无代码应用，可能逐渐变复杂、变关键，并出现可运维性、安全、冗余和成本问题，最终比传统开发更贵。[7] 这条机制不要求应用一开始就复杂；一个没人正式接管的简单工具，也可能积累多年维护负担。

**本节判断。**维护成本反增，通常发生在平台标准路径之外的工作持续增多，而许可、治理和退出成本又没有被纳入最初决策时。

本节参考文献：
[29] Forrester／OutSystems TEI <https://insight.unipro.io/hubfs/low-code-roi-tei-outsystems%20(1).pdf> 摘录：“506% $14.77M To better understand the benefits, costs, and risks associated with this investment, Forrester interviewed development and maintenan…”
[7] Cigref企业工作组报告 <https://www.cigref.fr/wp/wp-content/uploads/2023/02/Cigref-EN-New-Low-Code-No-Code-development-practices-December-2022-v2.pdf> 摘录：“New Low Code/No Code development prac�ces Unlocking value by controlling risks December 2022 New Low Code/No Code development Unlocking value by…”

## 五、适用场景：按应用边界选择，不按行业或平台标签一刀切

本节参考文献：
[29] Forrester／OutSystems TEI <https://insight.unipro.io/hubfs/low-code-roi-tei-outsystems%20(1).pdf> 摘录：“The Total Economic Impact™ Of OutSystems”
[7] Cigref企业工作组报告 <https://www.cigref.fr/wp/wp-content/uploads/2023/02/Cigref-EN-New-Low-Code-No-Code-development-practices-December-2022-v2.pdf> 摘录：“New Low Code/No Code development prac�c…”

### 先看复杂度、寿命和集成，再决定路线

**最适配的是重复业务结构。**稳定的表单、审批、部门流程和基础数据管理，能够大量使用平台已有能力。无代码适合更窄、更简单的范围；低代码适合需要专业扩展、标准接口和持续迭代的企业应用。[3][7]

| 业务场景 | 复杂度与定制 | 生命周期 | 集成与合规 | 优先路线 | 成本反增信号 |
|---|---|---|---|---|---|
| 原型、MVP、简单网页 | 低，标准组件为主 | 短期验证 | 少量标准连接 | 无代码 | 原型直接变关键系统 |
| 部门表单、内部审批 | 低至中，规则清晰 | 可持续使用 | 权限与审计明确 | 无代码或低代码 | 规则重复、责任缺位 |
| 多站点运营工具 | 中，局部差异较多 | 长期迭代 | 共用数据与接口 | 低代码加融合团队 | 组件分叉、环境膨胀 |
| ERP周边应用 | 中，依赖业务语义 | 长期演进 | 标准API较重要 | 低代码加集成服务 | ERP端点缺失、异常复杂 |
| 客户关键业务流程 | 中至高 | 长期关键 | 强安全、审计要求 | 受治理低代码或混合 | 测试与恢复能力落后 |
| 复杂算法、高并发事务 | 高，深度定制 | 长期 | 性能与一致性关键 | 专业代码或混合 | 大量平台变通方案 |
| 实时飞控等安全关键系统 | 高，严格时间约束 | 长期关键 | 实时与安全证明 | 专业代码核心、平台外围 | 平台抽象妨碍验证 |

**适合不等于自动便宜。**即使只是审批应用，也可能涉及多个系统的权限、敏感数据和跨部门状态。范围小只是有利条件，标准化集成和明确责任同样重要。Rierino特别指出，有限集成也可能需要超出预期的协调。[20]

**复杂也不等于全部排除。**KPMG的2025年报告显示，在使用低代码的受访者中，28%表示非常广泛地用于复杂企业应用。[11] 这说明企业级场景已经存在；选型关键是平台能否满足具体工作负载，而不是把所有复杂系统都归为禁区。

本节参考文献：
[3] IBM术语比较 <https://www.ibm.com/cn-zh/think/topics/low-code-vs-no-code> 摘录：“对超自动化和 IT 现代化的需求在增长，但企业一直难以跟上这些趋势，因为目前拥有开发者人才的数量有限。 许多 IT 项目由于缺乏具备专业技…”
[7] Cigref企业工作组报告 <https://www.cigref.fr/wp/wp-content/uploads/2023/02/Cigref-EN-New-Low-Code-No-Code-development-practices-December-2022-v2.pdf> 摘录：“3 CHALLENGES AND OPPORTUNITIES FOR IT ...............................…”
[20] 跨团队平台能力 <https://rierino.com/blog/low-code-strategy-3-enterprise-paths-scale> 摘录：“Low code is no longer confined to experimental initiatives or isolate…”
[11] KPMG全球调查 <https://assets.kpmg.com/content/dam/kpmgsites/sa/pdf/2025/accelerating-digital-transformation-with-ai-and-low-code.pdf.coredownload.inline.pdf> 摘录：“11 Outlook development. are potentially missing out on these benefits.”

### 高合规、制造和金融，都需要拆分系统层次

**行业标签太粗。**一家银行的员工申请表、客户服务流程、核心账务和高频交易，并不是同一种软件问题。低代码可以适合其中部分流程，同时不适合承担某些实时或高性能核心。Cigref的企业决策树就同时考察战略性、用户规模、性能、界面复杂度和应用寿命。[7]

**制造现场也有分层。**Jabil的案例主要体现工作流、MES扩展和现场体验定制，并通过共用组件保持标准化。[15] 这与直接用通用可视平台实现所有设备控制算法，是不同层次的选择。

**实时边界尤其重要。**2025年的跨行业综述指出，航空航天系统常需要把低代码界面与传统嵌入式软件结合，以满足飞行控制的实时处理要求。[30] 这里的合理分工，是平台处理交互和外围流程，专业代码承担严格时序与关键控制。

**合规要求可以促进治理。**严格合规不是简单否决低代码的理由。若平台具备合适权限、日志、环境分离和测试门禁，它也可能帮助统一控制。相反，若业务用户能绕过这些控制，即使应用功能很简单，也不应直接进入敏感生产环境。

本节参考文献：
[7] Cigref企业工作组报告 <https://www.cigref.fr/wp/wp-content/uploads/2023/02/Cigref-EN-New-Low-Code-No-Code-development-practices-December-2022-v2.pdf> 摘录：“New Low Code/No Code development prac�ces Unloc…”
[15] Jabil客户案例 <https://www.mendix.com/customer-stories/jabil-delivers-100-mendix-apps-improving-global-site-operations-promoting-hyper-customization/> 摘录：“Jabil Delivers 100+ Mendix Apps Improving Globa…”
[30] 航空航天混合架构 <https://doi.org/10.3390/app15126481> 摘录：“Computer 2025 , 58, 30–40. Google Scholar ( tit…”

### 数据层选择，常常比页面搭建方式更影响长期成本

**一个具体案例说明取舍。**2026年的Power Platform文档审批研究，采用SharePoint Lists作为主要存储层，以获得成本和Microsoft 365兼容优势。研究同时说明，SharePoint Lists不具备传统关系数据库的关系约束，因此通过查找列模拟关系行为。[6]

**前期节省会产生后续责任。**对简单文档流程，这种选择可以合理。若系统后来需要更复杂的关系、一致性和事务处理，原先由数据库约束保障的工作，就可能转为应用配置和维护逻辑。问题不在“低代码是否有数据库”，而在选定的数据底座是否匹配未来业务结构。

**统一平台不自动统一数据。**艾瑞白皮书指出，开发变容易后，应用数量可能快速增加，并出现僵尸应用、数据标准不统一和关系混乱。[10] 因而，应用数量增加与企业数据能力提高，不是天然同步的两件事。

本节参考文献：
[6] Power Platform系统研究 <https://doi.org/10.3390/info17010046> 摘录：“Section 6 ( reports the empirical results, including performanc…”
[10] 中国企业级无代码白皮书 <https://pdf.dfcfw.com/pdf/H3_AP202304191585562131_1.pdf?1681902388000.pdf> 摘录：“数据从接入、存储、处理、数据能力 虽系企业增值能力，但能 产品集成 更低成本享有成熟产品竞 研发部门 分析、展现到应用的端到…”

### 多应用复用有价值，但没有普适的数量门槛

**访谈给出了复用锚点。**Sadovnikov等人的2023年BPM，即业务流程管理研究中，受访者提到约5—6个应用后更能看到平台附加价值。Abendroth与Bender的ERP研究中，另一位受访者提出约6—7个应用。[31][18]

**数量只是复用的外壳。**5—7个应用可以作为经验锚点，但真正创造价值的是共用身份认证、接口、规则、组件和测试资产。七个彼此无关、各自复制逻辑的应用，不一定比两个高度复用的应用更划算。

**首次引入与边际应用不同。**若企业已有平台、治理和可复用组件，新增一个小应用的成本，可能远低于从零引入平台。相反，专门为单个短期工具建设完整平台团队，固定投入可能过大。应用组合应作为核算单位之一，而不是只看孤立项目。

本节参考文献：
[31] BPM适用性研究 <https://www.ingevandeweerd.nl/wp-content/uploads/2023/05/Sadovnikov-et-al.-2023-A-framework-to-assess-the-suitability-of-low-code-for-BPM.pdf> 摘录：“and expert interviews, resulting in 18 factors to be as…”
[18] ERP访谈研究 <https://lswi.de/assets/downloads/publikationen/109/Abendroth_Bender_2025_Bridging_the_Gap_Low-Code_Platforms_and_the_Future_of_ERP.pdf> 摘录：“2021 IEEE/ACM 18th International Conference on Mining S…”

### 什么变化会触发重新选型

**规模变化需要复核。**Appfront用“第三年”模式描述一种实践风险：用户翻倍、外部API增加、领域模型复杂化，以及运行时续费高于预算。[32] 真正的触发因素是这些变化同时到来，而不是日历走到第三年本身。

**关键化比复杂化更危险。**一个部门工具即使功能没增加，也可能因为全公司开始依赖它，而需要正式支持、恢复和审计。此时，原先由个人兼任维护的方式可能不再适合。应用的重要性应单独评估，而不是只根据界面数量判断复杂度。

**五项核查能落实选择。**下面不是要求所有项目采用同一种流程，而是把前述比较转成可执行的决策输入。

| 顺序 | 核查输入 | 判定重点 | 结果应用 |
|---|---|---|---|
| 1. 确定边界 | 复杂度、寿命、用户、实时性 | 标准流程还是关键复杂逻辑 | 选择候选开发路线 |
| 2. 建同口径基线 | 工时、周期、功能产出、质量 | 同范围、同验收门槛 | 判断真实交付收益 |
| 3. 检查可运维性 | 测试、权限、日志、回滚 | 能否持续验证与恢复 | 决定是否进入生产 |
| 4. 核算生命周期 | 许可、集成、培训、升级、退出 | 初交节省能否覆盖增量成本 | 决定是否扩大采用 |
| 5. 设置复核触发 | 用户、API、规则、环境、责任 | 是否越过原有能力边界 | 加强治理或转混合 |

**本节判断。**无代码优先解决简单、限定范围的需求；低代码优先承接稳定、可复用的企业流程；复杂核心系统更适合保留专业代码，并按层次使用平台。

本节参考文献：
[32] 生命周期转折观察 <https://appfront.nl/en/kennisbank/lowcode-vs-maatwerk-development> 摘录：“Low-code vs custom: when Mendix, OutSystems or Power Apps are no longer enough Low-code platforms deliver speed where it matters: a first working version of an internal application within weeks, a citizen developer setting up a form…”

## 六、开发者与管理者：分歧不是支持或反对，而是优化目标不同

本节参考文献：
[32] 生命周期转折观察 <https://appfront.nl/en/kennisbank/lowcode-vs-maatwerk-development> 摘录：“Low-code vs custom: when Mendix, OutSys…”

### 两类人看到的收益和风险，发生在不同时间

**管理者优先处理供需差。**业务需求不断增加，而专业开发资源有限，管理者会首先关注积压、交付时间和成本。KPMG调查中，52%将流程效率改善列为低代码收益，46%提到员工生产率提升，39%提到成本降低。[11] 这些是选择该收益的受访者比例，不是各指标改善的百分比。

**开发者更接近后期责任。**开发者要处理平台能力之外的异常、扩展、测试和升级，因此更关注可调试性、模块化和控制权。ERP访谈中的开发者担心，多部门定制会增加技术债，要求应用结构良好、易调试和易扩展。[18]

| 共同议题 | 业务用户 | 企业与IT管理者 | 专业开发者 |
|---|---|---|---|
| 交付速度 | 尽快解决具体问题 | 清理积压、兑现业务目标 | 减少重复实现 |
| 灵活性 | 能否调整流程和界面 | 能否响应组织变化 | 能否改变核心逻辑 |
| 可扩展性 | 更多同事能否使用 | 能否跨部门、跨站点推广 | 性能、事务与运行时边界 |
| 控制权 | 自己验证和配置需求 | 成本、数据与风险可控 | 调试、测试和架构可控 |
| 技能变化 | 学习逻辑与数据配置 | 组织培训与岗位调整 | 建组件、做集成、辅导 |
| 成本 | 减少等待和手工业务操作 | 生命周期净收益 | 维护、升级和技术债投入 |
| 治理 | 清楚允许做什么 | 权限、审计与责任明确 | 标准能否落实到工程工具 |
| 成功标准 | 工具是否好用 | 业务价值是否兑现 | 系统能否可靠演进 |

**时间尺度造成冲突。**首次上线的收益通常很容易展示，而升级回归和迁移准备发生得更晚。如果交付团队只按上线速度考核，后续维护由另一团队承担，局部最优就可能变成企业总成本增加。低代码放大了这种风险，因为交付更快，也更容易把维护责任留到以后。

**分歧也不是绝对对立。**Mendix 2021年的同一问卷中，75%的IT领导者、67%的开发者认为低代码是不能错过的趋势，相差8个百分点。[12] 开发者总体同样认可其价值，只是对能力边界和持续工程投入更敏感。

本节参考文献：
[11] KPMG全球调查 <https://assets.kpmg.com/content/dam/kpmgsites/sa/pdf/2025/accelerating-digital-transformation-with-ai-and-low-code.pdf.coredownload.inline.pdf> 摘录：“11 Outlook development. are potentially missing out on these benefits. Study design and sample © 20…”
[18] ERP访谈研究 <https://lswi.de/assets/downloads/publikationen/109/Abendroth_Bender_2025_Bridging_the_Gap_Low-Code_Platforms_and_the_Future_of_ERP.pdf> 摘录：“2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR), 46–57. A., Uddin…”
[12] Mendix 2021调查 <https://www.mendix.com/wp-content/uploads/Mendix_2021_State_of_LowCode_Whitepaper.pdf> 摘录：“THE STATE OF LOW-CODE 2021: A LOOK BACK, THE LIGHT AHEAD 12 THE STATE OF LOW-CODE 2320: A LOOK BACK…”

### 管理者并非只看价格，安全和集成往往更重要

**平台选择重视控制。**KPMG调查中，把安全视为“非常重要或较重要”的受访者合计85%，集成易用性为84%，后端集成与API管理为83%。[11]

| 平台选择因素 | 非常重要 | 较重要 | 合计 |
|---|---:|---:|---:|
| 安全 | 58% | 27% | 85% |
| 集成易用性 | 50% | 34% | 84% |
| 后端集成与API管理 | 47% | 36% | 83% |

**成熟管理会扩大评价范围。**同一报告中，47%的企业把预算内交付纳入成功指标，36%关注平均恢复或修复时间。[11] 这说明成本和维护并非开发者单方面的议题。真正需要统一的是，哪些指标在采购前、上线时和运行后都要持续负责。

**感知收益与实现条件不同。**Mendix 2024年调查覆盖2000名大型企业技术高管和高级IT决策者，约80%称低代码改善团队生产率，73%称改善上市时间。[33] 同一调查也反映培训、风险和治理担忧，说明积极采用并不意味着认可“无需专业人员”。

**替代人才的预期值得警惕。**该调查中，39%的受访技术领导者认为，非技术高管希望用低代码替代开发人才。[33] 这个数字描述技术受访者的判断，实际决策含义是：应把节省重复实现，与取消架构、测试和维护能力明确分开。

本节参考文献：
[11] KPMG全球调查 <https://assets.kpmg.com/content/dam/kpmgsites/sa/pdf/2025/accelerating-digital-transformation-with-ai-and-low-code.pdf.coredownload.inline.pdf> 摘录：“11 Outlook development. are potentially missing out on these benefits. Study design and sample ©…”
[33] Mendix 2024企业调查 <https://www.mendix.com/wp-content/uploads/lowcode-barometer-2024-final.pdf> 摘录：“The Low-Code I N S I G H TS FROM ENTERPRISE IT LEADERS Conclusion Afterword 52 01 Introducing The…”

### 技能不会消失，而是从逐项实现转向平台工程

**专业开发者角色正在移动。**JTIE的企业观察中，开发者更多承担治理、可复用组件建设和辅导，业务分析师则对部门工具拥有更多责任。[2] 这是一种工作重组，而不是开发职责自然消失。

**培训应计入真实投入。**2022年的TEI模型，先为25名开发者各安排50小时培训，合计1250人小时。[29] 平台减少语法和框架工作，不代表开发者无需理解平台的数据模型、依赖、发布和扩展方式。

**融合团队更符合责任分配。**业务人员适合负责需求解释、流程验证和简单配置。专业开发者适合负责架构、复杂逻辑、接口、质量和运行治理。Mendix把这种跨专业协作称为融合团队，其目标是同时满足业务与安全合规要求。[34]

**治理团队不是全部维护团队。**PG&E案例中的CoE由3名员工领导，赋能1300名高级数字创建者，并培训3000余名公民开发者。[16] 这个数字体现的是平台赋能效率，不应解释为2000余个应用的所有维护工作只由3人完成。

**质量门禁仍然存在。**Petrobras以12人的CoE管理基础设施、集成、数据库和复用组件，支持500余名开发者及100余个敏捷团队。案例还描述了至少90%的BDD测试门槛；BDD是以业务行为描述测试的方式。[17] 其成功叙事包含强工程控制，而不是绕开工程控制。

本节参考文献：
[2] 企业部署观察 <https://www.sci-open.net/index.php/JTIE/article/view/16625> 摘录：“Journal of Software: Evolution and Proc…”
[29] Forrester／OutSystems TEI <https://insight.unipro.io/hubfs/low-code-roi-tei-outsystems%20(1).pdf> 摘录：“Average development effort for revenue-…”
[34] Mendix融合团队说明 <https://www.mendix.com/zh-CN/blog/understand-no-code-vs-low-code-development-tools/> 摘录：“无代码开发与低代码开发：差异、相似之处和用例 - 2024 年 3 月 5 日…”
[16] PG&E客户案例 <https://www.microsoft.com/en/customers/story/1709539049606899869-pacific-gas-and-electric-microsoft-power-apps-energy-usa> 摘录：“Pacific Gas and Electric Company (PG&E)…”
[17] Petrobras案例 <https://www.outsystems.com/case-studies/petrobras-agile-development> 摘录：“Petrobras' New Dev Culture Proves Even…”

### 影子IT可能增加，也可能因正式渠道而减少

**无监督开发会增加风险。**Cigref警告，业务部门绕过IT建设应用，容易产生重复系统、数据分散和无人维护的工具。[7] 无代码门槛越低，这种增长越容易发生。

**正式平台也能收拢需求。**Mendix 2021年调查中，25%的采用组织报告影子IT减少，并声称减少幅度为56%。同一调查称，59%的低代码项目由IT与业务合作完成。[12]

**两种方向由组织决定。**如果业务人员过去只能私建电子表格或外购工具，正式低代码平台可能提供受控出口。如果平台本身没有应用清单、权限和责任人，它又会成为新的影子IT载体。工具的易用性相同，治理安排不同，结果就可能相反。

**本节判断。**开发者与管理者的分歧，应通过共同的生命周期指标和责任分工解决，而不是要求其中一方只接受另一方的成功标准。

本节参考文献：
[7] Cigref企业工作组报告 <https://www.cigref.fr/wp/wp-content/uploads/2023/02/Cigref-EN-New-Low-Code-No-Code-development-practices-December-2022-v2.pdf> 摘录：“New Low Code/No Code development prac�ces Unlocking value b…”
[12] Mendix 2021调查 <https://www.mendix.com/wp-content/uploads/Mendix_2021_State_of_LowCode_Whitepaper.pdf> 摘录：“THE STATE OF LOW-CODE 2021: A LOOK BACK, THE LIGHT AHEAD 12…”

## 七、未来三至五年：场景化扩散与混合开发，比全面替代更可能

本节参考文献：
[7] Cigref企业工作组报告 <https://www.cigref.fr/wp/wp-content/uploads/2023/02/Cigref-EN-New-Low-Code-No-Code-development-practices-December-2022-v2.pdf> 摘录：“New Low Code/No Code development prac�c…”
[12] Mendix 2021调查 <https://www.mendix.com/wp-content/uploads/Mendix_2021_State_of_LowCode_Whitepaper.pdf> 摘录：“Title: Mendix_2021_State_of_LowCode_Whi…”

### 场景化与混合不是互斥选项

**主情景是共同使用。**2026—2031年，更有依据的路径是：企业扩大低代码/无代码使用范围，同时保留专业代码处理复杂逻辑、性能、关键集成和治理。场景化描述“用在哪里”，混合开发描述“怎样组成系统”，二者完全可以同时成立。

| 采用策略 | 2026—2031年判断 | 主要范围 | 专业代码的位置 | 关键条件 |
|---|---|---|---|---|
| 企业全面平台化 | 更适合业务结构高度标准化的组织 | 大部分自建应用 | 仍可能存在于平台与外部服务 | 平台覆盖需求且退出成本可控 |
| 局部纯低代码／无代码替代 | 将持续扩大 | 部门工具、简单应用、标准流程 | 在这些限定应用中减少 | 规则、集成和规模保持适配 |
| 企业级混合规模化 | 最有证据支持的主情景 | 跨部门、长期应用组合 | 承担复杂核心与平台扩展 | 清晰边界、复用资产与成熟治理 |

**案例研究支持多路径。**2023年的IEEE Access研究分析36个案例，识别出开发普惠、实现协同、缓解IT资源短缺三类采用原型，以及因复杂性而不采用的原型。[35] 不同动因对应不同平台角色，并不自然汇成一条全面替代路线。

**企业工具组合已经并存。**2024年对北欧52家领先企业、136名回应者的研究，同时观察到专业代码、低代码、机器人流程自动化RPA，以及部分AI和无代码使用。[36] 这比“所有开发迁移到一种工具”更接近大型企业的现实结构。

**用户扩大不等于代码消失。**Gartner在2022年曾预测，到2026年，正式IT部门之外的人员将至少占低代码工具用户的80%，高于2021年的60%。[5] 这个预测描述参与者构成，不是传统代码被替代的比例。

本节参考文献：
[35] IEEE采用案例研究 <https://doi.org/10.1109/access.2023.3325092> 摘录：“Title: A Multiple Mini Case Study on the Adoption of Low Code Development Platform…”
[36] 北欧企业工具组合研究 <https://doi.org/10.1007/978-3-031-66594-3_18> 摘录：“With the growing importance of business process automation practices, companies de…”
[5] Gartner定义 <https://www.gartner.com/en/newsroom/press-releases/2022-12-13-gartner-forecasts-worldwide-low-code-development-technologies-market-to-grow-20-percent-in-2023> 摘录：“Webinar 5 Game-Changing AI and Innovation Trends for Global CIOs Register Now ( We…”

### 2028年可以用数字情景比较，不能把市场金额换成替代概率

**市场前景有三种方向。**Forrester给出的2028年情景，包括约300亿美元的基准市场，以及AI推动下约500亿美元的上行情景。下行方向则是高代码AI工具提升效率，使低代码市场增速接近约11%。[13]

**统一基期后更清楚。**以下都以Forrester估计的2023年底132亿美元为起点。基准和上行金额取自来源；对应增速按五年端点计算。下行金额为条件估计：132×1.11⁵约等于222.4亿美元。

| 2028年情景 | 市场规模 | 2023—2028年复合增速 | 主要驱动 |
|---|---:|---:|---|
| 基准：场景化扩散 | 约300亿美元 | 端点计算约17.8%/年 | 公民开发和流程应用逐步成熟 |
| 上行：AI扩大能力边界 | 约500亿美元 | 端点计算约30.5%/年 | AI辅助构建、组件与连接器复用 |
| 下行：高代码相对效率提高 | 估计约222.4亿美元 | 假设11.0%/年 | 专业编程工具提效、平台成本压力 |

**增长不要求全面替代。**即使低代码市场达到上行情景，仍可能只是更多企业、更多部门和更多应用加入。企业也可能增加平台支出，同时增加专业代码开发。市场规模适合观察商业扩散，不适合直接换算企业全面转向的概率。

**专业代码也在进步。**Forrester的下行情景把AI辅助专业编程视为竞争变量。[13] 因而，低代码不能只和静止不变的传统工具比较。未来优势取决于两条开发路线的相对进步，以及各自的维护与治理成本。

本节参考文献：
[13] Forrester市场展望 <https://www.forrester.com/blogs/the-low-code-market-could-approach-50-billion-by-2028/> 摘录：“A $13-Billion Market For Low-Code And DPA Platforms After analyzing relevant data from over 100 vendors, Forrester estimates that the combined low-code and digital process automation (DPA) market reached $13.2 billion by the end of 2023.…”

### AI会降低表达门槛，但不会自动解决正确性

**探索性实验显示较大潜力。**Kothapalli与Vuppu发表于2026年的IEEE研究，纳入12名专业开发者和20名业务分析师，比较Oracle APEX加Select AI与ReactJS。研究报告等价功能平均完成速度为37倍，代码量减少95%；这个结果同时包含平台抽象与AI收益。[37]

**业务用户确实获得能力。**研究中的无SQL训练业务分析师，通过自然语言完成了78%的数据访问任务。[37] 这支持“更多业务人员能够参与”的判断，但任务完成能力与完整生产系统的维护能力仍是两种能力。

**准确率决定审核工作。**同一研究在1250次自然语言查询实验中，报告不同模型的准确率如下。[37]

| 查询模型 | 报告准确率 | 对业务使用的含义 |
|---|---:|---|
| GPT4 | 71% | 结果仍需业务与数据验证 |
| Cohere | 64% | 审核与纠错工作仍重要 |
| Oracle模型 | 61% | 适用任务和护栏影响效果 |

**安全护栏仍属工程。**在140个对抗提示测试中，行级安全机制拦截了96%的攻击。[37] 这说明权限约束可以发挥作用，也说明自然语言入口并不会自动消除安全验证。生成更快，反而更需要可追踪的授权和审核链条。

**AI可能改变瓶颈位置。**当生成界面、表结构和初步流程变得容易，难点会更集中在需求是否正确、数据是否一致、执行是否可靠。KPMG在讨论AI增强低代码的相关2130名受访者中，59%重视速度与敏捷，53%重视成本效率。[11] 这些期待能否兑现，仍取决于审核和运行成本有没有同步下降。

本节参考文献：
[37] Oracle APEX探索实验 <https://doi.org/10.1109/southeastcon63549.2026.11476427> 摘录：“Our findings reveal substantial productivity gains: developers completed equivalent functionality significantly faster t…”
[11] KPMG全球调查 <https://assets.kpmg.com/content/dam/kpmgsites/sa/pdf/2025/accelerating-digital-transformation-with-ai-and-low-code.pdf.coredownload.inline.pdf> 摘录：“11 Outlook development. are potentially missing out on these benefits. Study design and sample © 2025 Copyright owned by…”

### 企业采用会沿范围和治理能力扩张，而非机械地逐级升级

**三条路径可以并行。**Rierino把企业采用概括为部门加速、跨职能赋能和平台驱动规模化。[20] 它们不是每家企业都必须依次经过的成熟度阶梯；企业可以在不同业务中同时采用不同结构。

| 采用路径 | 主要范围 | 典型负责方 | 工程要求 |
|---|---|---|---|
| 部门加速 | 独立工作流、内部工具 | 业务部门、混合团队 | 基本权限、明确责任与有限集成 |
| 跨职能赋能 | 多部门流程与共用能力 | 技术与业务共同负责 | 标准API、复用组件、环境分离 |
| 平台驱动规模化 | 企业级长期应用基础 | 架构与平台团队 | 自动化交付、审计、运行治理 |

**扩大范围需要新增能力。**一个部门内有效的流程，可以依赖少数人协调。跨部门后，数据含义、权限和接口版本必须更一致。平台化之后，还要处理应用组合、容量、费用和退出安排；这些工作是规模收益的条件，而不是额外可省略的手续。

**领先指标应看可持续性。**应用数增长只能说明构建活动增加。更有决策意义的是，新增应用是否提高复用，是否保持质量，以及维护和费用是否跟得上。下表是据现有机制提出的观察指标，不给它们附加统计预测权重。

| 观察指标 | 具体看什么 | 积极信号 | 需要复核的信号 |
|---|---|---|---|
| 应用组合 | 活跃应用、关键应用与责任人 | 范围和所有权清楚 | 僵尸应用、关键工具无人接管 |
| 组件复用 | 跨团队共用规则与模块 | 新应用复用已有能力 | 多份相似规则各自修改 |
| 标准API | 接口覆盖、版本与异常处理 | 集成模式统一 | 非标连接与手工补偿增多 |
| 测试能力 | 关键路径自动验证、升级回归 | 变更后可持续验证 | 发布变快、验证跟不上 |
| 环境与权限 | 开发、预发布、生产隔离 | 授权和发布边界清晰 | 直接在生产修改 |
| 生命周期成本 | 用户、环境、运行与支持投入 | 费用与有效使用同步 | 许可增长快于价值 |
| 迁移能力 | 数据、逻辑和接口可转移程度 | 退出安排可执行 | 离开平台需全面重建 |
| AI可审计性 | 工作流执行、授权与人工接管 | 输出和动作可追踪 | 自动执行过程不透明 |

**转向幅度由条件决定。**2030—2031年企业是否大规模走向全面平台化，取决于AI能否提高复杂系统的正确性与可测试性、治理是否成熟、许可与迁移成本是否可控，以及专业代码工具的相对生产率。如果这些条件持续改善，低代码边界会扩大；若平台依赖和后期负担增长更快，采用会更集中在高收益场景。

**本节判断。**未来的竞争重点不是“哪种方式消灭哪种方式”，而是谁能让业务表达、专业工程和长期治理更有效地协作。

本节参考文献：
[20] 跨团队平台能力 <https://rierino.com/blog/low-code-strategy-3-enterprise-paths-scale> 摘录：“Low code is no longer confined to experimental initiatives or isolated automation projects. In many enterprises, it has become a structural component of how applications are delivered — whether to accelerate internal workflows, modernize legacy systems, support customer-facing platforms, or operationalize AI-driven use cases. What began as a tool for rapid development is now influencing broader architectural an…”

## 八、综合判断：真正要选择的是可持续的开发边界

**影响大，但不是全面替代。**低代码/无代码已经进入企业开发战略和大型应用组合，对编码配置、组件复用、业务参与和发布方式产生了实质影响。它们减少了部分重复工程，也增加了平台、数据和应用组合治理的重要性。

**效率提高，但要对应任务。**标准化、稳定、可复用的低代码任务，已经出现约3倍以上的实验生产率优势，以及明显的项目工时差距。无代码的突出价值，则是让业务专家更快形成可运行应用和反馈。对企业来说，真正重要的是这种优势能否通过测试、验收和组织协作，转化成更早、更可靠的业务交付。

**维护反转有明确机制。**复杂逻辑、重度集成、重复视觉规则、平台特定变通方案、许可扩张和责任缺位，都会把前期省下的工作转移到后期。传统代码也有技术债，因此决策应比较具体架构的可维护性，而不是把任一开发方式视为天然安全或天然便宜。

**证据口径应保持一致。**本文的实验分钟、项目库小时/功能点、交付周期和修复负担分别衡量不同结果；质量评分不等于缺陷率，修复负担不等于返工率。无代码按其明确的任务与角色边界判断，不承接低代码倍率。调查与客户案例保留自报属性，TEI为厂商委托复合情景，市场金额各有范围；文中的残差、工时比例、成本临界点和情景增速均已标明计算或估算。

**最终决策很具体。**让业务人员负责需求和简单流程，让专业开发者保留复杂逻辑、集成、测试与架构控制，再用完整生命周期成本决定是否扩大采用。低代码/无代码最值得购买的，不是“以后不需要开发者”的承诺，而是在清晰边界内，持续交付更多可靠软件的能力。

本节参考文献：
[20] 跨团队平台能力 <https://rierino.com/blog/low-code-strategy-3-enterprise-paths-scale> 摘录：“Dimension Path 1: Departmental Acceleration Path 2: Cross-Functional Enablement Path 3: Platform-Driven Scale --- --- --- --- Primary Driver We need to deliver faster without waiting on the central dev team. We can’t keep rebuilding…”

## 参考文献

[1] <https://doi.org/10.1109/mitp.2022.3189880> IEEE受控实验; IEEE开发阶段结果; IEEE工时结果; IEEE维护任务; IEEE实验设计; IEEE质量结果; IEEE维护实验
[2] <https://www.sci-open.net/index.php/JTIE/article/view/16625> 企业部署观察; JTIE企业观察; 修复负担观察; 企业长期观察; 重复规则与修复机制; 企业角色变化
[3] <https://www.ibm.com/cn-zh/think/topics/low-code-vs-no-code> IBM术语比较; IBM流程说明; IBM实现机制; IBM测试说明; IBM使用者与场景; IBM内部应用说明; IBM升级说明; IBM开放与封闭边界; IBM场景比较
[4] <https://cloud.google.com/discover/low-code-vs-no-code?hl=zh-CN> Google Cloud比较; Google应用示例
[5] <https://www.gartner.com/en/newsroom/press-releases/2022-12-13-gartner-forecasts-worldwide-low-code-development-technologies-market-to-grow-20-percent-in-2023> Gartner定义; Gartner市场预测; Gartner公民开发边界; Gartner用户结构预测
[6] <https://doi.org/10.3390/info17010046> Power Platform系统研究; 文档审批系统数据层
[7] <https://www.cigref.fr/wp/wp-content/uploads/2023/02/Cigref-EN-New-Low-Code-No-Code-development-practices-December-2022-v2.pdf> Cigref企业工作组报告; Cigref治理建议; Cigref生命周期风险; Cigref场景分类; Cigref选型案例; Cigref影子IT分析
[8] <https://www.microsoft.com/en-us/power-platform/products/power-apps/topics/low-code-no-code/low-code-vs-traditional-development> Microsoft开发方式比较; Microsoft定位说明; Microsoft补充开发定位
[9] <https://www.isbsg.org/wp-content/uploads/2021/08/Short-Paper-2021-06-Productivity-of-Low-Code-projects.pdf> ISBSG生产率报告; ISBSG项目库分析; ISBSG成本示例
[10] <https://pdf.dfcfw.com/pdf/H3_AP202304191585562131_1.pdf?1681902388000.pdf> 中国企业级无代码白皮书; 需求协作分析; 应用增长与数据治理
[11] <https://assets.kpmg.com/content/dam/kpmgsites/sa/pdf/2025/accelerating-digital-transformation-with-ai-and-low-code.pdf.coredownload.inline.pdf> KPMG全球调查; KPMG区域结果; KPMG采用状态; KPMG样本设计; KPMG企业应用使用; KPMG业务收益调查; KPMG平台选择因素; KPMG成功指标; KPMG的AI低代码价值判断
[12] <https://www.mendix.com/wp-content/uploads/Mendix_2021_State_of_LowCode_Whitepaper.pdf> Mendix 2021调查; Mendix区域结果; Mendix调查原文; Mendix角色态度比较; Mendix协作与影子IT结果
[13] <https://www.forrester.com/blogs/the-low-code-market-could-approach-50-billion-by-2028/> Forrester市场展望; Forrester市场估计; Forrester三种市场情景; Forrester情景驱动
[14] <https://my.idc.com/getdoc.jsp?containerId=US53966325> IDC全球预测; IDC预测摘要
[15] <https://www.mendix.com/customer-stories/jabil-delivers-100-mendix-apps-improving-global-site-operations-promoting-hyper-customization/> Jabil客户案例; Jabil实施方式
[16] <https://www.microsoft.com/en/customers/story/1709539049606899869-pacific-gas-and-electric-microsoft-power-apps-energy-usa> PG&E客户案例; PG&E效益说明; PG&E组织方式
[17] <https://www.outsystems.com/case-studies/petrobras-agile-development> Petrobras案例; Petrobras交付案例; Petrobras治理与测试
[18] <https://lswi.de/assets/downloads/publikationen/109/Abendroth_Bender_2025_Bridging_the_Gap_Low-Code_Platforms_and_the_Future_of_ERP.pdf> ERP访谈研究; ERP集成访谈; ERP复用访谈; 开发者维护关注
[19] <https://fb-swt.gi.de/fileadmin/FB/SWT/Softwaretechnik-Trends/Verzeichnis/Band_44_Heft_2/WSRE2024_01_Konersmann.pdf> 低代码测试与再工程分析; 平台锁定分析
[20] <https://rierino.com/blog/low-code-strategy-3-enterprise-paths-scale> 跨团队平台能力; 组件与集成治理建议; 部门采用中的集成风险; 企业采用路径
[21] <https://aaltodoc.aalto.fi/items/65c94b6a-2f70-4d7c-b52e-7cc0ceae5250> 系统性文献综述
[22] <https://doi.org/10.1109/cbi58679.2023.10187470> NexusBRaNT实验
[23] <https://doi.org/10.1365/s40702-024-01095-y> 瑞士两项目研究; 瑞士项目案例; 专业低代码成本综合
[24] <https://doi.org/10.1109/tr.2023.3295009> IEEE平台缺陷研究
[25] <https://dspace.lib.uom.gr/handle/2159/34641> Budibase与Spring实验
[26] <https://trepo.tuni.fi/handle/10024/161705> 集成开发研究
[27] <https://apvine.com/cases/from-outsystems-to-mendix-a-cost-driven-migration> OutSystems至Mendix迁移
[28] <https://www.apexsystems.com/insights/case-study/legacy-app-modernization-power-apps> Power Apps迁移案例
[29] <https://insight.unipro.io/hubfs/low-code-roi-tei-outsystems%20(1).pdf> Forrester／OutSystems TEI; TEI收益分项; TEI培训假设
[30] <https://doi.org/10.3390/app15126481> 航空航天混合架构
[31] <https://www.ingevandeweerd.nl/wp-content/uploads/2023/05/Sadovnikov-et-al.-2023-A-framework-to-assess-the-suitability-of-low-code-for-BPM.pdf> BPM适用性研究
[32] <https://appfront.nl/en/kennisbank/lowcode-vs-maatwerk-development> 生命周期转折观察
[33] <https://www.mendix.com/wp-content/uploads/lowcode-barometer-2024-final.pdf> Mendix 2024企业调查; 管理层认知调查
[34] <https://www.mendix.com/zh-CN/blog/understand-no-code-vs-low-code-development-tools/> Mendix融合团队说明
[35] <https://doi.org/10.1109/access.2023.3325092> IEEE采用案例研究
[36] <https://doi.org/10.1007/978-3-031-66594-3_18> 北欧企业工具组合研究
[37] <https://doi.org/10.1109/southeastcon63549.2026.11476427> Oracle APEX探索实验; 自然语言任务结果; 查询准确率实验; 安全测试结果
