# 全球具身智能技术路线与代表公司全景：技术、产品、商业化、融资与团队（截至2026年9月13日）

**核心结论。** 全球具身智能不是一条“人形机器人路线”，而是“硬件与应用场景×模型、数据与控制”的组合。商业化领先的是仓储移动机器人、专用清洁配送和工业巡检；工业人形、移动操作正在从试点走向早期交付。开放家庭操作和跨本体通用模型，仍以能力验证为主。[1]

**公司优势各异。** Figure的突出证据是宝马生产现场运行；Agility是物流任务与RaaS；优必选是工业产品收入；宇树是低成本本体和平台出货。Dexterity、Mujin、ANYbotics、普渡等公司的价值，则更多来自任务闭环、系统集成和持续运营，不能用人形机器人的融资热度衡量。

| 路线或公司群 | 核心技术组合 | 代表公司 | 决定性进度 | 当前判断 |
|---|---|---|---|---|
| 基础模型与平台 | VLA、世界模型、跨本体学习、仿真 | PI、Skild、DeepMind、NVIDIA | 跨本体演示、模型集成与工具生态 | 技术扩展潜力大 |
| 海外工业人形 | 双足本体、分层控制、视觉操作 | Figure、Agility、Apptronik、Tesla、Boston Dynamics | 宝马约1,250小时；Digit厂商口径65,000小时 | 早期交付与试点并存 |
| 中国人形与移动操作 | 本体自研、运动控制、工业数据、VLA | 优必选、宇树、智元、智平方、傅利叶 | 优必选2026年上半年921台全尺寸产品 | 制造与场景推进快 |
| 家庭及认知人形 | 柔顺驱动、端侧模型、记忆与交互 | 1X、NEURA | NEO预订；4NE1产品准备 | 自主性与安全是门槛 |
| 仓储物流与工业 | AMR、机械臂、数字孪生、规划编排 | Amazon、Dexterity、Covariant、Mujin、Intrinsic | Amazon整体机器人超过100万台 | 近期商业确定性较强 |
| 四足与轮腿巡检 | 学习型运动、定位导航、专业传感器 | Spot、ANYbotics、宇树、云深处、Ghost | ANYbotics每月分析12万余次巡检 | 地形与行业决定价值 |
| 家庭及商用服务 | 导航、群控、端侧AI、专用执行机构 | 普渡、擎朗、科沃斯、石头 | 普渡累计出货超过12万台 | 专用产品已规模化 |
| 相邻Physical AI | 车辆或无人机、导航、仿真、运营 | Waymo、Tesla、DJI、Skydio | Waymo累计服务超过2,000万次 | 可借鉴导航与数据闭环 |

**数据出处。** 表中运行、交付和经营数字，分别来自人形部署追踪[2]、优必选中期公告[3]、Amazon机器人报道[4]、ANYbotics官网[5]、普华资本披露[6]及Waymo运营报道[7]。各数字保留自身统计期间，后文逐项展开。

**阅读路线。** 下文先解释“身体、模型、训练方式”如何交叉，再按人形、仓储工业、四足巡检、家庭服务整理公司。每家公司均围绕技术、产品、商业、融资和团队展开。最后比较成本、可靠性、资本结构及未来12—24个月的关键变化。

本节参考文献：
[1] IFR服务机器人统计 <https://ifr.org/img/worldrobotics/Executive%5FSummary%5FWR%5F2025%5FService%5FRobots.pdf> 摘录：“(AP8), professional cleaning (AP2), agriculture (AP1), and search & rescue, security Mobile robot solutions are well established in transportation and logistics (AP5) with 14% more units sold in 2024. More than every other professional service robot sold in 2024 was built for the transportation of goods or cargo. This is also reflected in the number of su…”
[2] 宝马部署证据 <https://nexi.fund/humanoid-robot-deployments-2026/> 摘录：“The one site-level record inside the filing, Digit v4 at Schaeffler's plant in Cheraw, South Carolina, placing 25-pound baskets into an industrial washing machine, is evidence tier T3: vendor disclosure in a regulated filing, with no operator account from Schaeffler. The Comparison Table Investors Need Company Flagship Verified deployment Valuation --- --…”
[3] 中期技术披露 <https://stockn.xueqiu.com/09880/20260828390148.pdf> 摘录：“茲提述本公司日期為2025 年3 月30日、2025年4 月22日、2026年7 月3 日、10 日及16日的公告，內容有關將5,453,931股內資股轉換為H股的實施及該等 轉換H股（「轉換H股」）於聯交所主板的上市及流通（「H股全面流通」）。 司已向聯交所申請批准轉換H股上市及准許買賣，而聯交所已於2026年7 H股全面流通已於2026年7 月16日完成，而轉換H 股 亦已於2026 年7月17日上午九時正開始於聯交所上市。 誠如本公司日期為2026年8月10日的通函（「該通函」）、2026年8月10日及2026 年8月26日的公告（「該等公告」）所披露，本公司已於2026年8月26日舉行的 2026 年第三次臨時股東會，批准對2025年11月配售事項所得款項淨額的 有關調整詳情，請參閱該通函及該等公…”
[4] Amazon产品规模 <https://www.automate.org/robotics/industry-insights/blue-jay-way> 摘录：“This story first appeared in A3's Automated newsletter. Subscribe here. Development was a big piece of last week’s Blue Jay unveil. The move was something of a shift for Amazon Robotics, which has tended to spend the majority of a product reveal discussing the technology itself. Here, however, chief technologist Tye Brady devoted a chunk of his stage time…”
[5] 运营规模 <https://www.anybotics.com/> 摘录：“Title: ANYbotics Autonomous Legged Robots for Industrial Inspection Markdown Content: Autonomous robotic inspection solutions Our ANYmal robotic solutions automate industrial inspections. They provide operator insights that increase plant uptime, reduce costs, and improve safety by removing workers from hazardous areas. Autonomous inspection at scale insp…”
[6] 普渡经营规模 <http://www.puhuacapital.com/mobile/index.php/news/info/297> 摘录：“普华资本于2022年投资普渡机器人C轮融资。 本轮融资后，公司估值突破百亿元人民币，彰显资本市场对普渡产品技术壁垒、商业落地能力与全球化领导力的高度认可。 融资资金将重点投入具身智能技术研发、产品矩阵扩充、全球市场纵深拓展、规模化产能建设与供应链升级，全面巩固公司在全球商用服务机器人赛道的领先优势，为登陆资本市场、引领机器人行业高质量发展筑牢根基。 普华资本新能源新材料投资董事陆建良 表示： 普渡机器人创立于2016年，是全球商用服务机器人领导者。 秉承 用AI和机器人，让工作更轻松，生活更美好 的使命，普渡致力于打造全球性的智能机器人基础设施，让机器人服务100亿人。 商业实力领跑，增长动能强劲。 普渡机器人已形成服务配送、商用清洁、工业配送、通用具身智能四大核心产品线，商业表现亮眼：近年收入保持高速增…”
[7] 运营规模 <https://www.stcn.com/article/detail/3628362.html> 摘录：“从规模上看，Waymo凭借超2000万英里测试里程、纯L4运营经验，仍是行业技术 天花板 ，但其发展受制于两大瓶颈：其15万美元的单车成本虽较早期大幅下降，但仍无法适配除欧美日外的新兴市场； 而美国本土出行需求增速有限，伦敦、东京等新市场需应对更高的合规成本。 而小马智行和文远知行两家头部企业则受益于国内对无人驾驶的大力支持而后劲十足。 得益于地方政府通过 智能网联汽车示范区 提供政策支持，小马智行快速获得全无人运营许可，特别是广州 黄金走廊 的高客流密度，直接支撑了 单车盈亏平衡 的突破。 文远知行选择了 轻资产+出海 路径，用B端场景分摊风险，用新兴市场打开增量。 有分析认为，Waymo凭借技术积累与资本优势，仍是全球L4赛道的 领跑者 ，但中国企业凭借政策适配、成本控制与多场景创新，已在局部市场形成…”

## 技术路线地图：先看任务，再看身体和智能系统

本节参考文献：
[1] IFR服务机器人统计 <https://ifr.org/img/worldrobotics/Executive%5FSummary%5FWR%5F2025%5FService%5FRobots.pdf> 摘录：“Executive Summary World Robotics 2025 -…”
[2] 宝马部署证据 <https://nexi.fund/humanoid-robot-deployments-2026/> 摘录：“Figure AI operates more robots than it…”
[3] 中期技术披露 <https://stockn.xueqiu.com/09880/20260828390148.pdf> 摘录：“為進一步提升人形機器人導航的擬人性、安全性、效率和智能 性，我們持續探索了數據…”
[4] Amazon产品规模 <https://www.automate.org/robotics/industry-insights/blue-jay-way> 摘录：“Industry Insights Blue Jay Way Amazon B…”
[5] 运营规模 <https://www.anybotics.com/> 摘录：“Title: ANYbotics Autonomous Legged Robo…”
[6] 普渡经营规模 <http://www.puhuacapital.com/mobile/index.php/news/info/297> 摘录：“融资资金将重点投入具身智能技术研发、产品矩阵扩充、全球市场纵深拓展、规模化产能…”
[7] 运营规模 <https://www.stcn.com/article/detail/3628362.html> 摘录：“而在中国市场，小马智行、文远知行等企业也已形成差异化竞争优势，三者在技术路线、…”

### 四条机器人主路线分别解决什么问题

**四条主线并行。** 通用人形追求适配人类工作空间；移动操作追求生产效率；四足解决复杂地形通行；服务机器人则围绕清洁、配送等具体需求优化。本体不是外观选择，而是对动作空间、能耗、维护和安全的选择。[8]

| 硬件与应用路线 | 技术定义及核心假设 | 典型硬件 | 主要优势 | 当前成熟度 |
|---|---|---|---|---|
| 通用人形、工业人形 | 用类人身体复用既有工位、工具与通道 | 双足、双臂、灵巧手 | 环境改造较少、任务扩展空间大 | 试点至早期交付 |
| 移动操作、仓储工业 | 把导航、抓取与调度组合成生产系统 | AMR、固定臂、轮式双臂、夹爪 | 任务明确、吞吐与回报可计量 | AMR成熟，操作持续扩展 |
| 四足、轮腿及特种巡检 | 用独立足点通过连续轮面难以通行的地形 | 四足、轮足、专业传感载荷 | 楼梯、缝隙、复杂地面通行 | 工业巡检已有持续部署 |
| 家庭、商用服务 | 先限定任务，再逐步增加理解与操作能力 | 清洁机、配送机、服务移动操作器 | 渠道成熟、专用任务容易复制 | 专用品规模化，通用品早期 |

**人形的核心取舍。** 双足可以跨越台阶，双手可以接近人类操作方式。但平衡和操作必须同时成功，关节、线束、散热与电池也随之复杂。只有当“适应现有环境”的收益超过这些额外成本，人形才比轮式底盘或固定机械臂更有经济价值。

**移动操作的核心取舍。** 平整工厂通常不需要双足，却需要稳定搬运、精准抓取和设备联动。Mujin把机器人、视觉和自动化设备放进统一控制环境；Dexterity则用工业机械臂与技能系统执行物流操作。这两者都把通用性放在软件层，而非要求身体完全仿人。[9][10]

**四足的核心取舍。** 四足以地形适应换取更高的机械和控制复杂度。在适合轮式通行的地面，轮式通常更高效；需要空中视角时，无人机又可能更合适。因此，电站楼梯、地下隧道和危险场所，比普通平面运输更能体现四足价值。[11]

**服务机器人的取舍。** 清洁和配送可以通过限定任务，降低操作难度。家庭管家却要处理衣物、杯具、杂物和个人偏好，任务边界远宽于扫地。专用服务机器人的出货规模，首先证明制造、渠道和售后能力，而不是自动证明通用家务能力。

本节参考文献：
[8] 具身AI综合综述 <https://arxiv.org/html/2407.06886> 摘录：“In Section 8, we discuss promising research directions. II Embodied Robots Embodied agents interact with the physical environment, including robots, smart appliances, and autonomous vehicles, etc. Fixed-base robots, shown in Fig. 2 (a), are used in laboratory automation and industry due to their precision, e.g., Franka Emika panda 19, 20 , Kuka iiwa 21, 22 , and Sawyer 23, 24 . Wheeled robots, depicted in Fig. 2 (b), are efficient in logistics…”
[9] Mujin技术架构 <https://mujin-europe.com/technology> 摘录：“Learn about the platform powering today's most advanced automation applications Learn about the platform powering today's most advanced automation applications Learn about the platform powering today's most advanced automation applications MujinOS: The Intelligence Behind Every Robot MujinOS: The Intelligence Behind Every Robot A universal robotics platform that enables robots to perceive, plan, and act autonomously through integrated percepti…”
[10] Dexterity平台 <https://dexterity.ai/platform> 摘录：“The result: 10+ years of mean time between failures, built to operate in 0°-50°C temperatures, up to 1,500m altitude, and up to 90% humidity. Made in America Designed, developed, and assembled in Redwood City, California. Key submodules sourced from world-leading manufacturers in Japan and Taiwan. Tested and validated in-house before every deployment. We're not looking for humanoid robots — we're looking for super humanoid robots, because mayb…”
[11] 四足市场调查 <https://www.goedelmachines.com/blog/quadruped-market-survey> 摘录：“This is Part 3 of our Physical AI series. Read the other articles: Part 1: Quadruped control architecture · Part 2: Quadruped mechanics. Quadrupeds are being used for industrial inspection, research, security, and work in places that are difficult or hazardous for people to reach. The robots look similar, but their customers and business models differ considerably. A small platform bought by a university lab is a different product from a robot…”

### 硬件路线与模型路线怎样交叉

**模型并不绑定形态。** 同一个VLA可以适配机械臂、轮式双臂或人形。强化学习既可训练四足步态，也可优化仓储调度。世界模型可以用于机器人动作规划，也可以留在云端生成训练和测试场景。[12]

| 机器人主线 | 模块化规划与控制 | VLM、VLA、VLN | 世界模型 | 主要训练数据 |
|---|---|---|---|---|
| 人形 | 全身协调、平衡、接触约束 | 指令理解与操作生成 | 预测交互、生成子目标 | 遥操作、人类动作、仿真 |
| 仓储工业 | 路径、抓取、力控、车队编排 | 语义拣选、柔性操作 | 装箱预测、场景仿真 | 生产动作、异常、物品数据 |
| 四足巡检 | 定位、任务执行、回坞 | 语义导航、仪表理解 | 地形与环境预测 | 仿真地形、现场巡检 |
| 家庭商服 | 导航、清洁、任务状态机 | 对话、语义地图、整理 | 物体变化、长期任务 | 使用反馈、示范、家庭场景 |

**工程上仍需分层。** 华为2026年9月报告给出的典型尺度是：决策约1—20Hz，执行约50—1,000Hz以上。语义推理可以慢一些，平衡和接触控制必须快速响应。端侧负责实时闭环，边侧负责现场协同，云侧负责训练、仿真和全局迭代。[13]

**成熟度已有分化。** IFR统计，2024年全球专业服务机器人销量超过19.9万台，消费服务机器人接近2,010万台。专业服务机器人中，超过一半用于货物运输。这个规模说明，具身智能产业不能只从人形新品发布会理解。[1]

**阶段标签统一。** 本文把设计展示称为“概念”，可运行样机称为“原型”，客户现场有限验证称为“试点”。重复生产并有限交付称为“小批量”，持续产线生产称为“量产”，客户收到并投入使用称为“交付”。软件和模型另用“发布、集成、商业授权”描述，不机械套用整机量产标签。

**本节判断。** 选路线应从任务和环境出发，再决定身体形态及模型组合；“是否人形”不是智能水平或商业价值的统一分界。

本节参考文献：
[12] 统一机器人学习综述 <https://arxiv.org/html/2609.03927v1> 摘录：“Toward Unified Robot Learning: Bridging Representation, Vision-Language-Action, and World Models For robots to operate reliably in real-world environments, they need to perceive their surroundings, act, and reason about the consequences of those actions. Rapid progress in the domains of representation learning, vision-language-action (VLA) models, and world models has significantly enhanced the capabilities of robot learning systems, enabling robots to work in increasingly complex environments. However, these paradigms are…”
[13] 云边端协同架构 <https://www-file.huawei.com/dam/asset/view/physical-ai-cloud-edge-device-collaboration-architecture.pdf> 摘录：“Title: 物理智能云边端协同架构研究报告 Number of Pages: 60 Markdown Content: 物理智能云边端协同架构 研究报告 具身智能机器人是我国前瞻布局的新兴产业，已上升为国家重要战略方向，是打通数字空间与物理世界、发 展新质生产力的关键载体，事关我国人工智能与机器人产业的全局竞争实力。 当前具身智能/物理智能快速兴 起，技术从数字智能向真实物理世界延伸，但物理闭环实时性保障、多智能体群体协同、模型持续迭代、异 构系统互联互通等工程问题突出，产业迫切需要一套可落地的参考架构与深度的产业研判。 《物理智能云边端协同架构研究报告》立足物理智能产业发展现状，聚焦云边端协同这一核心技术范式，针 对物理智能 端侧实时闭环、边侧增强智能、云侧全局演进 的分层特征，系统阐释云-边-端协同架构的生 成逻辑，提出 三域协同·一网贯通 参考架构，区分不同场景下架构的适用条件与风险边界，既解析实时 控制、多机协同、虚实仿真训练等技术价值，也对产业链分工、差异化部署模式、服务化商业演进路径开展 系统研判。 报告为芯片、模型、机器人本体、系统集成等产业各方提供架构设计与商业落地的重要参照，对 具身智能机器人走向规模化商用有重要价值。…”
[1] IFR服务机器人统计 <https://ifr.org/img/worldrobotics/Executive%5FSummary%5FWR%5F2025%5FService%5FRobots.pdf> 摘录：“(AP8), professional cleaning (AP2), agriculture (AP1), and search & rescue, security Mobile robot solutions are well established in transportation and logistics (AP5) with 14% more units sold in 2024. More than every other professional service robot sold in 2024 was built for the transportation of goods or cargo. This is also reflected in the number of suppliers with this application group. The IFR Statistical Department is currently aware of 333 companies that supply various types of logistics robots. though sales of robo…”

## 模型、学习与控制：当前主流是混合架构

本节参考文献：
[12] 统一机器人学习综述 <https://arxiv.org/html/2609.03927v1> 摘录：“Toward Unified Robot Learning: Bridging…”
[13] 云边端协同架构 <https://www-file.huawei.com/dam/asset/view/physical-ai-cloud-edge-device-collaboration-architecture.pdf> 摘录：“从毫秒级实时控制到小时、天级持 续学习与运营，任务时间尺度跨越多个数量级，推…”
[1] IFR服务机器人统计 <https://ifr.org/img/worldrobotics/Executive%5FSummary%5FWR%5F2025%5FService%5FRobots.pdf> 摘录：“Executive Summary World Robotics 2025 -…”

### 模块化、VLA和世界模型如何比较

**混合路线更接近现实。** 模块化系统便于诊断和安全约束，VLA有跨任务迁移潜力，世界模型补充动作后果预测。它们不是三选一。Figure的全身VLA仍包含不同频率的控制层，就是最直观的例子。[14]

| AI或控制路线 | 输入与输出 | 训练及数据 | 优势 | 瓶颈与落地位置 |
|---|---|---|---|---|
| 模块化、分层控制 | 感知→任务→轨迹→关节控制 | 标定、规则、优化与学习策略 | 可调试、可约束、可维护 | 接口误差；工业主流 |
| VLM视觉语言模型 | 图像与语言→理解、任务计划 | 图文、视频、具身问答 | 语义理解与任务分解 | 物理约束和动作落地 |
| VLN视觉语言导航 | 视觉与指令→导航目标、路径 | 指令轨迹、地图、在线交互 | 语义寻路、进度判断 | 长期记忆与错误恢复 |
| VLA视觉语言动作 | 视觉、语言、本体状态→动作块 | 机器人示范、网页与视频混合 | 跨物体、任务迁移 | 分布外失败、实时性 |
| 世界模型、WAM | 状态与动作→未来状态或观测 | 交互序列、视频、仿真 | 预测后果、评估候选动作 | 物理一致性、计算成本 |
| 模仿学习 | 专家示范→行为策略 | 遥操作、动作捕捉、UMI | 降低人工编程需求 | 示范成本、错误累积 |
| 强化学习 | 状态、奖励→优化策略 | 仿真或真实交互 | 运动与适应能力强 | 奖励设计、试错安全 |
| 仿真到现实 | 虚拟训练→真实执行 | 域随机化、参数辨识、真机校正 | 安全、并行、可重复 | 接触、摩擦、柔性物体差异 |

**VLA不是一个配方。** NVIDIA将常见方案概括为动作分词、视觉语言能力保留训练，以及独立动作头。连续动作被编码成模型可以学习的序列，再由动作模块生成控制输出。这样可以保留语义能力，同时减少动作微调对原有模型能力的破坏。[15]

**语言理解不是抓取。** “把杯子放到那个盒子旁边”需要识别指代、建立三维关系，再处理接近、接触与松手。模型能解释指令，并不意味着能可靠执行最后几厘米的操作。因此，视觉、触觉、本体反馈和低层控制，仍是VLA落地的组成部分。

**世界模型重在动作。** 机器人世界模型要预测“采取这个动作后，环境如何变化”。仅生成逼真视频，不足以证明它能服务控制。2026年世界模型综述进一步把策略、可控世界模型和逆动力学，看作联合预测与控制的不同分解。[16]

**组合架构已有实例。** π0.7由高层策略生成子任务，BAGEL世界模型把子任务转成视觉子目标，再由动作专家执行。它让“要完成什么”与“具体做到什么状态”之间多了一层视觉约束。这有助于复杂指代任务，但不要求所有VLA都增加完整视频生成器。[15]

**时延必须分清。** 深蓝学院介绍的Fast-WAM在训练时联合建模视频与动作，推理时跳过显式未来视频生成，报告延迟190毫秒。这个数字是模型推理时延，不是关节控制周期。机器人仍需在两次模型更新之间，维持快速、稳定的反馈控制。[17]

本节参考文献：
[14] Helix 02技术披露 <https://www.figure.ai/news/helix-02> 摘录：“Introducing Helix 02 Last year, Helix showed that a single neural network could control a humanoid’s upper body from pixels. Today, Helix 02 extends that control to the entire robot - walking, manipulating, and balancing as one continuous system. Helix 02 is Figure’s most capable humanoid model yet: A single neural system that controls the full body directly from pixels, enabling dexterous, long horizon autonomy across an entire room. Helix 02 represents several breakthroughs: Autonomous, long‑horizon loco-manipulation: Helix 02 unloads and reloads a dishwasher across a full-sized kitchen - a f…”
[15] NVIDIA技术综述 <https://developer.nvidia.com/blog/pretrained-to-imagine-fine-tuned-to-act-the-rise-of-world-action-models/> 摘录：“200k hours of egocentric human video plus 15k hours of robot demonstrations. Architecture Hierarchical latent-plan policy; LSTM low-level decoder. Large MoT transformer for latent world-action modeling. Latent variable Trajectory-level latent plan, prior/posterior training. Same prior/posterior structure, foundation-model scale. Policy interface Predict prior plan; low-level policy conditioned on observation and goal executes it. Train both branches; at test time only the prior branch runs through the compact latent interface. The key difference is not the latent variable itself. Play-LMP alrea…”
[16] 世界模型综合综述 <https://arxiv.org/html/2605.00080> 摘录：“(\hat{o}_{t+1},\hat{r}_{t},\hat{d}_{t})\sim p_{\phi}(\cdot\mid o_{\leq t},a_{\leq t},l), (16) where the world model p_{\phi} provides imagined transitions, and optionally rewards and termination signals. The policy is then improved from imagined rollouts by maximizing expected return, J(\theta)=\mathbb{E}_{\hat{\tau}\sim(\pi_{\theta},p_{\phi})}\! \left \sum_{t}\gamma^{t}\hat{r}_{t}\right , (17) or, in practice, through a GRPO-style policy optimization objective, \mathcal{L}_{\mathrm{RL}}(\theta)=-\mathbb{E}_{t}\Big \min\big(r_{t}(\theta)\hat{A}_{t},\,\mathrm{clip}(r_{t}(\theta),1-\epsilon,1+\ep…”
[17] Fast-WAM技术介绍 <https://www.shenlanxueyuan.com/news/detail/24> 摘录：“2026牌局过半，四个玩家正在交换手牌…… ——具身 四子 的 番位竞争 2026年，具身智能大模型的研究在四条技术路线上同步深化： VLA模型开始集成推理能力，VLN模型引入了自我认知机制，而世界模型也逐渐与动作生成相融合，形成了所谓的 世界动作模型 （WAM）。 基于上述技术架构与演进逻辑，2026 年各大高校、企业在四大技术赛道均产出了突破性研究成果。 本文将围绕 2026 年以来的代表性工作，逐一梳理各方向的最新进展。 VLM：从二维理解到三维空间感知 2026年，VLM 的核心挑战是：如何让模型在不依赖外部深度传感器的前提下，理解三维空间结构，并支持机器人的精细操作与推理。 VLM-3R：融合三维重建的空间推理框架 发文团队：德克萨斯大学奥斯汀分校（UT Austin）， 现有的大型多模态模型在二维图像理解上表现出色，但在具身场景中，机器人需要从单目视频中理解三维空间结构。 传统方法往往依赖外部深度传感器或离线三维地图，限制了其在动态、时敏场景中的适用性。 VLM-3R提出了一种统一框架，通过三维重建指令微调（3D Reconstructive Instruction Tuning）来增强VLM的空间感知能力。 模型使用几何编码器从单目视频帧中提取隐式三维Token，再通过空间-视觉-视角融合机制将空间上下文与自然语言指令对齐。 团队构建了超过20万条三维重建指令问答对，并…”

### 为什么数据数量不能直接代表能力

**数据路线需要组合。** 真机遥操作最接近目标硬件，但采集昂贵。人类第一视角视频容易扩大规模，却存在人手与机器手的差异。仿真可以大量试错，但摩擦、接触和软物体往往与现实不同。Skild因此组合Robot Teleop、UMI、第一视角视频和仿真数据。[18]

**三维对齐尤其重要。** RoboTron-Mani论文指出，异构数据的坐标系、相机参数和动作表示可能相互冲突。同样是向下移动，在不同坐标系中可能对应相反符号。其RoboData整合约7万段episode、700万个样本，重点工作之一就是统一空间与动作表示。[19]

**测试结果要看任务。** 该论文在LIBERO报告91.7%成功率，在RoboCasa为47.4%，在RT-1相关评测为60%。RT-1评测还进行了传感器参数补充、损失项调整和缺失相机处理。这组差异说明，单个高成功率并不能概括开放环境能力。[19]

**数据规模口径不同。** Generalist AI的GEN-1采用约50万小时UMI式可穿戴数据；优必选披露约1,100万条真机数据；Figure披露超过20万个并行仿真环境。“小时、条、环境数”衡量的是不同资源，不能直接排出数据优势榜。[15][20][14]

本节参考文献：
[18] Skild数据策略 <https://hub.baai.ac.cn/view/57478> 摘录：“henry 发自 凹非寺 量子位 公众号 QbitAI 具身智能的大结果，要来了！ 自上周Generalist发布能够学习3到12秒动作的具身大脑Gen 1.5 以来～ 刚刚，北美具身初创Skild AI又发布了全新机器人基础模型S1，直接把机器人上下文学习的任务长度拉到了10分钟往上。 这次的S1主打上下文学习（in-context learning，ICL）： 无需在后训练阶段专门学习新…”
[19] RoboTron-Mani论文 <https://arxiv.org/html/2412.07215v2> 摘录：“19 100% 64 80% 20 100% 65 100% 21 85% 66 100% 22 90% 67 100% 23 70% 68 95% 24 100% 69 95% 25 100% 70 100% 26 90% 71 100% 27 75% 72 95% 28 100% 73 70% 29 100% 74 90% 30 100% 75 70% 31 100% 76 100% 3…”
[15] NVIDIA技术综述 <https://developer.nvidia.com/blog/pretrained-to-imagine-fine-tuned-to-act-the-rise-of-world-action-models/> 摘录：“Instead of training a smaller transformer-style policy around a video-prediction head, it starts from Wan 2.1-I2V-14B-480P and turns the video diffusion backbone into a joint world-action model. Th…”
[20] 优必选数据披露 <https://www.iyiou.com/news/202608281139470> 摘录：“优必选2026年上半年营收12.7亿元，全尺寸人形产品收入增长1445% 8月28日， 人形机器人第一股 优必选（股份代码：9880.HK）发布2026年中期业绩报告：总营收12.7亿元，同比大幅增长104.2%； 人形机器人总销量16123台，同比大幅增长268.3%； 全尺寸具身智能人形机器人（非遥控非玩具，大脑芯片算力≧200T，身高160cm以上）收入5.9亿元，同比大幅增长1445…”
[14] Helix 02技术披露 <https://www.figure.ai/news/helix-02> 摘录：“Introducing Helix 02 Last year, Helix showed that a single neural network could control a humanoid’s upper body from pixels. Today, Helix 02 extends that control to the entire robot - walking, mani…”

### 基础模型与平台代表公司

| 公司与主要地区 | 技术及产业定位 | 产品与商业阶段 | 融资节点 | 团队依据 |
|---|---|---|---|---|
| Physical Intelligence，旧金山 | 跨本体VLA模型层 | π0系列，研发与合作集成 | 2024年11月4亿美元 | Google Brain、Stanford背景 |
| Skild AI，美国CMU研究圈 | 跨本体机器人“大脑” | S1，长任务与一次示范验证 | 2024年A轮3亿美元 | Pathak、Gupta |
| Google DeepMind，全球研发体系 | VLA与具身推理平台 | Gemini Robotics、ER合作应用 | 企业研究组织口径 | 多本体学习、产业合作 |
| NVIDIA，全球平台体系 | 模型、算力、仿真工具 | GR00T、Isaac Sim/Lab生态 | 上市公司平台投入口径 | GR00T与仿真研究团队 |
| Covariant，美国伯克利 | 基础模型与仓储操作系统 | RFM-1商业部署、模型授权 | 2023年C轮7,500万美元 | Abbeel、Chen、Duan |

**表格依据。** 公司定位与融资节点来自机器人操作市场报告[21]、基础模型公司指南[22]及Skild专题[18]。Covariant在仓储工业部分继续展开。

**Physical Intelligence：卖模型能力。** PI的π0、π0.5用一组权重控制不同机器人，展示过折衣和清理桌面。其本体、执行器和传感器来自被适配的机器人，而不是独立整机产品。π0把视觉语言模型与流匹配动作生成结合，后续π0.7进一步引入视觉子目标。[22][23]

**PI的商业判断。** 这一路线的规模单位应是接入本体、付费集成与模型复用，而非机器人出货。2025年行业报告列其2024年11月融资4亿美元，轮次标作B轮，估值24亿美元。团队来源指向Google Brain和Stanford，π0论文作者包括Karol Hausman、Chelsea Finn等研究者。[21][23]

**Skild：强调看示范适应。** 2026年8月发布的S1，以不改变模型权重的上下文学习为重点。媒体转述的未见任务成功率为66%，语言提示VLA为9%；传统后训练增加到约2,000次示范后达到86%。因此，它体现的是新任务适配成本的变化，而不是后训练全面失去价值。[18]

**Skild的资本与团队。** 2024年A轮为3亿美元，估值15亿美元。同一2026年报道还列“当年1月”C轮14亿美元、估值超过140亿美元，SoftBank领投，NVIDIA和Bezos参与。两笔列示融资合计17亿美元，这是算术合计，不是完整累计融资账本。创始人Deepak Pathak、Abhinav Gupta来自CMU，方向覆盖机器人学习、强化学习、视觉和自监督。[18]

**DeepMind：推理与动作分工。** Gemini Robotics 1.5通过Motion Transfer学习异构机器人数据，ER系列负责空间理解、任务进度和物理约束推理。与Boston Dynamics合作的工业仪表读取，报告成功率93%。它证明的是特定感知推理任务，不是通用操作成功率。[17]

**DeepMind的产业位置。** 其机器人产品形态是模型和合作集成，Apollo等整机提供实际执行载体。资金与团队按Google研究组织理解；商业判断应落到模型接入后的任务性能、部署成本和机器人合作方扩展，而不是把母公司资源当作具身业务独立估值。

**NVIDIA：提供开发底座。** Isaac GR00T提供人形基础模型，Isaac Sim生成数字场景和传感器数据，Isaac Lab支持模仿与强化学习。硬件厂商提供执行器和本体，NVIDIA提供训练、仿真、计算与部署工具。这使它能够同时服务多条整机路线。[22]

**NVIDIA的组织优势。** GR00T N1论文作者包括Johan Bjorck、Linxi Fan、Dieter Fox等，体现模型与机器人研究的结合。其商业模式对应算力、开发平台和生态采用。评价重点是工具能否降低真机数据与适配成本，以及端侧推理能否满足功耗和时延要求。[23]

**本节判断。** 当前更有解释力的技术问题不是“VLA还是世界模型”，而是模型如何接入实时控制、使用何种数据，以及新增能力能否降低现场适配成本。

本节参考文献：
[21] 融资与团队画像 <https://www.roboticscenter.ai/research/robot-manipulation-market-landscape-2025> 摘录：“The Robot Manipulation Market Landscape 2025: Companies, Investors, and Opportunities Comprehensive overview of the robot manipulation industry — hardware vendors, software platforms, data providers, service companies, and investment landscape. The robot manipulation market is structurally reorganizing. Hardware commoditizes, software and data become the defensible layer. Here is who is building what, who is funding them, and where the gaps are. Market Structure The robot manipulation industry operates as a three-layer value chain: - Hardware layer — robot arms, grippers, sensors, and mobile bases. Increasingly commoditized for standard DOF configurations. Margin pressure from Chinese man…”
[22] PI产业定位 <https://www.evsint.com/top-robotics-foundation-model-embodied-ai-companies-2026/> 摘录：“Physical Intelligence, Skild AI, Figure AI, Google DeepMind, and NVIDIA lead on model capability, while EVST and other industrial manufacturers are now bringing factory-grade hardware and real-world manipulation data into the category. This guide ranks the most influential players and what each one actually ships. What Counts as a Robotics Foundation Model Company in 2026 A robotics foundation model is a large neural network trained on diverse robot, vision, and language data so a single model can generalize across many tasks and robot bodies, rather than being hand-coded for one job. The vision-language-action (VLA) architecture, which maps camera input plus a language instruction direct…”
[18] Skild数据策略 <https://hub.baai.ac.cn/view/57478> 摘录：“刚刚，北美具身初创Skild AI又发布了全新机器人基础模型S1，直接把机器人上下文学习的任务长度拉到了10分钟往上。 这次的S1主打上下文学习（in-context learning，ICL）： 无需在后训练阶段专门学习新的操作数据，只需看一段人类示范视频，就能 照猫画虎 ，直接完成一整套从未见过的复杂操作流程。 在官方演示里，机器人完成了煎饼、冲泡咖啡、给植物换盆，以及设备组装等长程任务。 并且在未见过的任务上，把成功率干到了66%，远超基于语言提示的VLA（只有 9%）。 另外，哪怕是走传统后训练微调的路线，想追平S1只看一次演示的效果，大概也要喂进去380次左右的任务演示。 可以说，最近这一波集中在上下文学习的工作，又给不少人重新燃起了对具身的希望。 有推特网友表示，通用机器人可能两年后就会出现，而不是七年。 还有网友表示，从Rhoda，到上周Generalist，再到现在Skild S1的10分钟任务，机器人真正的GPT时刻似乎正在出现。 因为一旦这种能力真的泛化，以后开发机器人技能，可能真的会变得像给ChatGPT 写 Prompt一样。 从BERT时代，迈向GPT时代 想要理解S1这次到底怎么个上下文学习，咱们得先看看，传统机器人是怎么学习一个新技能的。 在传统的pipeline里，机器人学习其实和大模型差不多： 先在海量数据上进行预训练，学会一些基础能力； 然后到了具体场景，再针对某个任务收集数据，通过后训练，让机器人学会专有技能。 只不过问题在于，机器人和大模型虽然流程差不多，但数据成本却完全不是一回事。 大模型的预训练数据，大量来自互联网； 哪怕到了编…”
[23] 模型架构综述 <https://arxiv.org/html/2507.00917v2> 摘录：“While previous surveys have typically focused on individual components (such as robotics simulators 19, 20, 21 and world models 22, 23, 24 ) our work bridges these domains to reveal their complementary roles in intelligent robot development. Contribution. The main contributions of this survey are: Levels of intelligent robots: Propose a comprehensive five-level grading standard (IR-L0 to IR-L4) for humanoid robot autonomy evaluation across four key dimensions: autonomy, task handling ability, environmental adaptability, and societal cognition ability. Analysis of recent techniques of robot learning: Systematically review recent developments in intelligent robotics across legged locomotion…”
[17] Fast-WAM技术介绍 <https://www.shenlanxueyuan.com/news/detail/24> 摘录：“2026牌局过半，四个玩家正在交换手牌…… ——具身 四子 的 番位竞争 2026年，具身智能大模型的研究在四条技术路线上同步深化： VLA模型开始集成推理能力，VLN模型引入了自我认知机制，而世界模型也逐渐与动作生成相融合，形成了所谓的 世界动作模型 （WAM）。 基于上述技术架构与演进逻辑，2026 年各大高校、企业在四大技术赛道均产出了突破性研究成果。 本文将围绕 2026 年以来的代表性工作，逐一梳理各方向的最新进展。 VLM：从二维理解到三维空间感知 2026年，VLM 的核心挑战是：如何让模型在不依赖外部深度传感器的前提下，理解三维空间结构，并支持机器人的精细操作与推理。 VLM-3R：融合三维重建的空间推理框架 发文团队：德克萨斯大学奥斯汀分校（UT Austin）， 现有的大型多模态模型在二维图像理解上表现出色，但在具身场景中，机器人需要从单目视频中理解三维空间结构。 传统方法往往依赖外部深度传感器或离线三维地图，限制了其在动态、时敏场景中的适用性。 VLM-3R提出了一种统一框架，通过三维重建指令微调（3D Reconstructive Instruction Tuning）来增强VLM的空间感知能力。 模型使用几何编码器从单目视频帧中提取隐式三维Token，再通过空间-视觉-视角融合机制将空间上下文与自然语言指令对齐。 团队构建了超过20万条三维重建指令问答对，并提出了视觉-空间-时序智能基准（VSTI），包含13.86万个问答对，覆盖五类时序空间推理任务。 VLM-3R在VSTI基准和多个三维问答任务上均取得了优于现有方法的表现，证明了在不依赖深度传…”

## 人形机器人：工业交付、低价平台与家庭路线正在分化

本节参考文献：
[21] 融资与团队画像 <https://www.roboticscenter.ai/research/robot-manipulation-market-landscape-2025> 摘录：“The Robot Manipulation Market Landscape…”
[22] PI产业定位 <https://www.evsint.com/top-robotics-foundation-model-embodied-ai-companies-2026/> 摘录：“Last updated: May 29, 2026 The companie…”
[18] Skild数据策略 <https://hub.baai.ac.cn/view/57478> 摘录：“还有网友表示，从Rhoda，到上周Generalist，再到现在Skild S…”
[23] 模型架构综述 <https://arxiv.org/html/2507.00917v2> 摘录：“A Survey: Learning Embodied Intelligenc…”
[17] Fast-WAM技术介绍 <https://www.shenlanxueyuan.com/news/detail/24> 摘录：“这一设计使模型能够利用极为多样的数据，包括人工示范、含失败案例的自主数据，以及…”

### 海外工业人形：先比较生产任务，而不是演示动作

| 公司与地区 | 技术路径 | 产品与商业阶段 | 资金锚点 | 团队锚点 |
|---|---|---|---|---|
| Figure，美国湾区 | 本体、Helix、制造垂直整合 | Figure 02客户交付；03扩产 | 2025年9月10亿美元 | Brett Adcock |
| Agility，美国俄勒冈州 | 物流专用双足、Arc调度 | Digit商业部署、RaaS | 累计6.41亿美元口径 | OSU动态机器人实验室 |
| Apptronik，美国奥斯汀 | 模块化本体、模型合作 | Apollo企业试点 | 2026年2月5.2亿美元 | UT Austin、NASA背景 |
| Tesla，美国奥斯汀 | 自研本体、AI与制造复用 | Optimus产线安装、内部训练 | 母公司内部资金 | Elon Musk、Tesla AI体系 |
| Boston Dynamics，美国沃尔瑟姆 | 电动Atlas、动态控制积累 | Atlas工业化；Spot已交付 | Hyundai并购支持 | MIT Leg Lab、Robert Playter |

**表格依据。** 资金和组织信息来自公司画像[24]、Sacra融资比较[25]及部署追踪[2]；Tesla阶段采用财报口径报道[26]。

本节参考文献：
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“AI 平台：Figure 专有的 Helix 视觉-语言-动作（VLA）模型采用双系统架构——System 1 以 200 Hz 运行用于底层电机控制，System 2 以 7–9 Hz 运行用于规划和推理。 该公司于 2025 年结束与 OpenAI 的合作，转而构建完全专有的 AI。 生产：Figure 的专用人形机器人制造工厂是 BotQ，目标是每年生产 1.2 万台。 这是首个专为人形机器人建造的工厂。 融资：总计超过 19 亿美元，投资方包括杰夫·贝佐斯、微软、英伟达、英特尔、高通、T-Mobile、Salesforce 和…”
[25] 累计融资比较 <https://sacra.com/research/figure-vs-apptronik-vs-agility-robotics/> 摘录：“- The primary emerging business model of robotics-as-a-service (RaaS) allows customers treat humanoid robots as operational expense—budgeted alongside labor rather than as multi-hundred-thousand-dollar capital purchases—with unit pricing targets of sub-$20K designed to…”
[2] 宝马部署证据 <https://nexi.fund/humanoid-robot-deployments-2026/> 摘录：“The one site-level record inside the filing, Digit v4 at Schaeffler's plant in Cheraw, South Carolina, placing 25-pound baskets into an industrial washing machine, is evidence tier T3: vendor disclosure in a regulated filing, with no operator account from Schaeffler. Th…”
[26] 财报阶段报道 <https://www.tmtpost.com/8118474.html> 摘录：“截至7月22日的Q2财报，特斯拉官方口径是第一代Optimus产线 正在安装 ，生产 预计年内启动 。 也就是说，弗里蒙特这条被寄予厚望的产线，尚未真正投入运转。 马斯克本人对 年产百万台 这一目标反复重申，但这更接近方向性的意志表态，缺乏附有时间表的施工计划。 他在2025年初曾表示当年要生产上万台Optimus，实际交付数字远低于预期。 Figure则呈现出不同的节奏，没有宏大的产能宣言，只有连续数月的进度更新。 4月底，每小时一台，24倍提速。 到8月，按当时公布的周产55台的速度倒推，实际产量大概率已明显超过350台的基数。…”

### Figure AI：全栈模型与制造一体化

**技术路径。** Figure同时设计本体、执行器、电机、传感器、电池和电子系统。Figure 03增加掌部相机与触觉，指尖传感可检测低至3克的力。掌部相机减少近距离抓取盲区，触觉则帮助处理滑移和精细接触。[27][14]

**学习与控制。** Helix 02的System 2负责场景和语言理解；System 1以200Hz生成全身关节目标；System 0以1kHz处理平衡、接触与协调。S0约1,000万参数，训练结合超过1,000小时人类运动数据与超过20万个并行仿真环境。[14]

**产品进度。** Figure 02在宝马Spartanburg执行钣金件装载。运营方口径为约10个月、超过9万个部件、支持超过3万辆X3、约1,250运行小时。公司复盘采用11个月部署窗口，并描述测试到生产的推进过程。[2][28]

**商业化进度。** 按9万个部件÷约1,250小时，估算全流程平均处理量约72件/小时。这个代理指标衡量特定工位产出，不是单次抓取成功率，也不是替代人数。Figure 03则由公司披露已交付超过350台，生产速率从每天1台提升到每小时1台。[29]

**融资情况。** PANews整理的2025年9月融资为10亿美元，估值390亿美元。累计融资摘要分别出现Sacra的17.5亿美元和RobotBelt的超过24亿美元。投资者包括Microsoft、NVIDIA、OpenAI和Bezos等；单轮与累计分别保留。[24][25][30]

**团队情况。** Brett Adcock于2022年创立Figure。制造侧的组织建设同样关键：公司披露招聘制造工程专家，并由可靠性团队进行加速寿命测试。其下一阶段优势，要由BotQ规划年产1.2万台转化为稳定生产、客户使用和维护能力。[24][27]

本节参考文献：
[27] BotQ供应链设计 <https://www.figure.ai/news/botq> 摘录：“Introducing BotQ Introducing BotQ, Figure’s new high-volume manufacturing facility for humanoid robots. BotQ’s first generation manufacturing line will be capable of manufacturin…”
[14] Helix 02技术披露 <https://www.figure.ai/news/helix-02> 摘录：“Introducing Helix 02 Last year, Helix showed that a single neural network could control a humanoid’s upper body from pixels. Today, Helix 02 extends that control to the entire ro…”
[2] 宝马部署证据 <https://nexi.fund/humanoid-robot-deployments-2026/> 摘录：“Unitree H2 Plus ◐ catalog listing, no order flow $7B IPO target Read the table vertically. The highest valuations sit on the least independent evidence. Tesla's implied standalon…”
[28] Figure现场复盘 <https://www.figure.ai/news/production-at-bmw> 摘录：“The challenge of this use case is in balancing speed and precision – placing parts within a 5-millimeter tolerance in just 2 seconds. To meet this, our robot had to achieve preci…”
[29] Figure 03生产披露 <https://www.figure.ai/news/ramping-figure-03-production> 摘录：“Ramping Figure 03 Production The transition from functional prototype to scalable fleet is a significant hurdle in humanoid robotics. Figure has cleared that gap with BotQ, our h…”
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“- 资历最老： 波士顿动力 (Boston Dynamics)（30 多年） - 生产规模最大： 特斯拉（目标年产 100 万台） - 首个商业化部署： Agility Robotics Digit - 最适合家用： 1X NEO（售价 2 万美元或每月 499 美元） 2026 年人形机器人公司完整对比： 特斯拉 — Optimus 总部：德克萨斯州奥…”
[25] 累计融资比较 <https://sacra.com/research/figure-vs-apptronik-vs-agility-robotics/> 摘录：“- The primary emerging business model of robotics-as-a-service (RaaS) allows customers treat humanoid robots as operational expense—budgeted alongside labor rather than as multi-…”
[30] 另一累计口径 <https://robotbelt.com/americas-humanoid-robot-race-six-players-three-paths/> 摘录：“Agility charges about US$25 an hour under a robots-as-a-service model, while US warehouse labour costs about US$30 or more an hour. The company target is to push operating cost t…”

### Agility Robotics：把人形收敛为物流设备

**技术路径。** Digit面向周转箱搬运，约1.75米高、最大载荷约16千克。其软件组合自主导航、操作规划和仿真到现实。Agility Arc负责云端部署与设备协同，机器人不必独立承担整座仓库的流程智能。[31]

**控制与安全。** 公司升级包括最长4小时续航、自动回充、更坚固的肢体与末端。安全功能包括Safety PLC、机载急停、CAT1停止和FSoE。Digit还可调度AMR把物料送往下一工位，体现“双足操作器+轮式运输”的组合。[32]

**产品进度。** 2023年Amazon启动Digit仓储测试。2026年6月SEC投资者演示的厂商口径是：截至5月，在9个客户设施累计运行65,000小时。客户包括GXO、Amazon、Toyota Canada、Schaeffler和Mercado Libre。[2]

**商业化进度。** 媒体报道截至2026年4月，Amazon Spanaway部署75台，搬运超过10万个料箱。Toyota Canada采用RaaS，贸易媒体列试点3台、后续7台。约25美元/小时是公开报道的服务价格；2—3美元/小时则是规模化运营成本目标。[30][33]

**融资情况。** Sacra列累计融资6.41亿美元、估值21.2亿美元。拟议Churchill SPAC交易另采用约25亿美元估值，计划毛融资约6.2亿美元，包括4.2亿美元信托和2亿美元PIPE。2025年收入180万美元、经营亏损1.4亿美元，显示商业部署与公司盈利之间仍有较长距离。[25][2]

**团队情况。** 公司源于Oregon State University Dynamic Robotics Lab，Damion Shelton是创始团队代表。其学术积累首先体现在动态双足运动，商业组织则围绕物流任务、云端调度和现场安全建设。RoboFab设计产能为每年1万台，下一阶段要看多客户复制与收费利用率。[24][2]

本节参考文献：
[31] Digit产品画像 <https://www.evsint.com/zh-CN/top-8-humanoid-robot-companies-2026/> 摘录：“上次更新时间：4月24，2026 2026年最值得关注的8家人形机器人公司分别是：Figure AI、Agility Robotics、特斯拉、波士顿动力、Apptronik、1X Technologies、Unitree Robotics和AgiBot。 我们根据三个标准对它们进行排名：商业部署规模、硬件技术成熟度（自由度、有效载荷、运动可靠性）以及软件栈深度，特别是每家公司是否已从远程操作转向自主操作或视觉-语言-动作（VLA）模型驱动…”
[32] Agility产品公告 <https://www.agilityrobotics.com/content/agility-robotics-announces-new-innovations-for-market-leading-humanoid-robot-digit> 摘录：“Article Sidebar Agility Robotics, creator of the humanoid robot Digit, has unveiled new capabilities and advancements that expand the work Digit is able to perform for Agility’s growing customer base. These innovations wer…”
[2] 宝马部署证据 <https://nexi.fund/humanoid-robot-deployments-2026/> 摘录：“The one site-level record inside the filing, Digit v4 at Schaeffler's plant in Cheraw, South Carolina, placing 25-pound baskets into an industrial washing machine, is evidence tier T3: vendor disclosure in a regulated fili…”
[30] 另一累计口径 <https://robotbelt.com/americas-humanoid-robot-race-six-players-three-paths/> 摘录：“Agility charges about US$25 an hour under a robots-as-a-service model, while US warehouse labour costs about US$30 or more an hour. The company target is to push operating cost to US$2 to 3 an hour at scale. Customers beyo…”
[33] Toyota部署追踪 <https://augustadynamics.com/de/resources/humanoid-robot-deployments-in-industry> 摘录：“Jede Woche erscheint ein neues Video, in dem ein humanoider Roboter etwas Beeindruckendes tut. Weit weniger dieser Roboter erledigen echte Arbeit, für einen echten Kunden, in einer echten Halle. Diese Seite verfolgt genau…”
[25] 累计融资比较 <https://sacra.com/research/figure-vs-apptronik-vs-agility-robotics/> 摘录：“Human teleoperation has emerged as a critical bridge strategy where operators intervene when robots encounter novel situations, serving a dual purpose: (1) ensuring robots provide immediate value rather than disrupting ope…”
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“- 最适合家用： 1X NEO（售价 2 万美元或每月 499 美元） 2026 年人形机器人公司完整对比： 特斯拉 — Optimus 总部：德克萨斯州奥斯汀 成立时间：2021 年启动机器人项目 CEO：埃隆·马斯克 特斯拉可以说是世界上最受瞩目的人形机器人公司，这很大程度上要归功于马斯克对特斯拉 Optimus 的大胆宣传。 该公司利用其现有的 AI 基础设施来训练其人形机器人，包括全自动驾驶神经网络和 Dojo 超级计算机。 主要产…”

### Apptronik：用模块化降低部署和维护复杂度

**技术路径。** Apollo高约1.73米、重约73千克、载荷25千克，电池续航约4小时。平台支持固定、轮式和双足配置。它的技术假设是：认知和操作能力可以复用，移动方式按客户环境选择。[34]

**学习与控制。** Apptronik与Google DeepMind合作，引入Gemini Robotics认知能力。本体则强调换电、模块化关节和现场维护。相比把所有模型能力都纳入内部研发，这条路线把资源集中在执行平台、可靠性和客户集成。[31]

**产品进度。** 2025—2026年的主要公开节点是Mercedes-Benz、GXO和Jabil企业试点。阶段判断为“客户试点”，目标任务包括工位补货、物料搬运、码垛和设备操作。下一阶段是从有限工位扩展到多配置、多场地部署。[34]

**商业化进度。** Apollo采用RaaS方向，降低客户一次性资本开支。换电和现场更换模块有助于减少停机，但经济价值最终取决于有效工作时间。媒体所列Mercedes物流效率约提高40%，应理解为该试点的报道结果，而非所有客户的普遍增益。[30]

**融资情况。** 列示融资包括2025年3月4.03亿美元，以及2026年2月5.2亿美元扩展轮。两笔合计9.23亿美元；较新的媒体累计口径超过9.35亿美元，估值约50亿—55亿美元。Google及John Deere、AT&T Ventures、QIA等企业和机构出现在相关报道中。[24][30]

**团队情况。** CEO为Jeff Cardenas，公司源于UT Austin的Human Centered Robotics实验室，并有NASA Valkyrie合作背景。团队路线与产品取向一致：从人机协作、模块化执行和维护性出发，借助模型合作补充泛化能力。[24]

本节参考文献：
[34] Apollo规格与配置 <https://ifactoryapp.com/industries/manufacturing-plant/manufacturing-humanoid-vendor-comparison-unitree-apollo-figure-2026> 摘录：“manufacturing floor is changing faster than most CFOs can budget for. By mid-2026, more than 1,000 Tesla Optimus units are working inside Gigafactory operations, Figure 03 fleets have entered paid commercial duty at BMW Spartanburg, NEURA Robotics is shipping its Studio F.A. Porsche-designed 4NE1 Gen 3.5 with a published price tag, and Unitree's H2 has cleared…”
[31] Digit产品画像 <https://www.evsint.com/zh-CN/top-8-humanoid-robot-companies-2026/> 摘录：“上次更新时间：4月24，2026 2026年最值得关注的8家人形机器人公司分别是：Figure AI、Agility Robotics、特斯拉、波士顿动力、Apptronik、1X Technologies、Unitree Robotics和AgiBot。 我们根据三个标准对它们进行排名：商业部署规模、硬件技术成熟度（自由度、有效载荷、运动可靠性）以及软件栈深度，特别是每家公司是否已从远程操作转向自主操作或视觉-语言-动作（VLA）模型驱动的操作。 对于希望将此全球人形机器人市场地图与EVST自身产品方向进行比较的读者，请参阅以下内容。 EVST 具身人工智能解决方案涵盖了该公司的人形机器人、灵巧手、四足机器人和具身人工智能数据收集路线图。 我们如何对这些公司进行排名 首先是商业部署：已向工业或物流领域的付费客户交…”
[30] 另一累计口径 <https://robotbelt.com/americas-humanoid-robot-race-six-players-three-paths/> 摘录：“Agility charges about US$25 an hour under a robots-as-a-service model, while US warehouse labour costs about US$30 or more an hour. The company target is to push operating cost to US$2 to 3 an hour at scale. Customers beyond Amazon: Toyota Canada signed a robots-as-a-service deal in February 2026. GXO and Latin American e-commerce firm Mercado Libre use it too.”
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“- 资历最老： 波士顿动力 (Boston Dynamics)（30 多年） - 生产规模最大： 特斯拉（目标年产 100 万台） - 首个商业化部署： Agility Robotics Digit - 最适合家用： 1X NEO（售价 2 万美元或每月 499 美元） 2026 年人形机器人公司完整对比： 特斯拉 — Optimus 总部：德克萨斯州奥斯汀 成立时间：2021 年启动机器人项目 CEO：埃隆·马斯克 特斯拉可以说是世界上最受瞩目的人形机器人公司，这很大程度上要归功于马斯克对特斯拉 Optimus 的大胆宣传。 该公司利用其现有的 AI 基础设施来训练其人形机器人，包括全自动驾驶神经网络和 Dojo 超级计算机。 主要产品：Optimus Gen 2（第二代擎天柱）身高 5 英尺 8 英寸（约 1.…”

### Tesla Optimus：制造与AI资源强，产品阶段按产线建设理解

**技术路径。** Tesla以自研执行器、视觉神经网络、计算基础设施和制造能力推进Optimus。机器人项目自2021年启动，Gen 2于2023年底展示。它复用的是自动驾驶的视觉、训练和工程资源，而不是把驾驶模型直接等同于全身操作模型。[24]

**产品进度。** 截至2026年7月22日Q2财报口径，第一代产线仍在安装，生产预计年内启动。另有工厂调研转述称，Gen 3设计定稿、供应链基本锁定，Fremont产线正在安装。本文据此归入“产线建设与内部训练”。[26][35]

**商业化进度。** 管理层时间表是先进入Optimus Academy积累数据，再推广至Tesla内部工厂，最早2027年下半年外部销售。这个顺序体现内部工厂的双重作用：既是潜在客户，也是训练和可靠性验证场地。[35]

**融资情况。** Optimus采用Tesla内部资金。公司层面2026年约200亿美元资本开支计划，同时覆盖机器人、制造与计算等项目，应作为母公司资源理解，而不是Optimus单独融资额。机器人估值也不能直接采用Tesla整体市值。[24]

**团队情况。** Elon Musk是项目战略与资源配置的核心人物，技术基础来自Tesla AI及制造体系。其组织优势在视觉训练、硬件协同和量产工程。未来能否形成领先位置，要由内部训练向外部付费客户的转换来决定。

本节参考文献：
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“编译：Felix, PANews 人形机器人行业正呈现爆发式增长，从少数几个研究实验室发展成为 2025 年规模达 29 亿美元的全球市场，预计到 2030 年将达到 40 亿至 180 亿美元。 数十家人形机器人公司目前正竞相制造能够行走、说话并与人类协同工作的机器。 本指南旨在介绍 2026 年主流人形机器人公司，包括其主要机器人、融资情况、定价以及每家公司的独特之处。 - 估值最高： Figure AI（估值 390 亿美元） - 价格最低： 宇树科技 G1（1.6 万美元） - 资历最老： 波士顿动力 (Boston Dynamics)（30 多年） - 生产规模最大： 特斯拉（目标年产 100 万台） - 首个商业化部署： Agility Robotics Digit - 最适合家用： 1X NEO（售价 2 万美元或每月 499 美元） 20…”
[26] 财报阶段报道 <https://www.tmtpost.com/8118474.html> 摘录：“人形机器人的量产竞赛正逼近窗口期，但发布会上的叙事与产线上的真实进度之间存在明显落差。 8月的加州弗里蒙特，一条运行十余年、先后生产过大量Model S和Model X的汽车产线，正在被拆除清空。 46天前，工人们还在这里完成电动轿车的总装； 46天后，产线骨架已经腾出，等待安装Optimus Gen3的专属工装。 同一个州，圣何塞，Figure AI的BotQ工厂，从今年1月到4月，日产能从一台提升至具备每小时一台的生产能力。 到4月底，工厂已向客户交付350余台Figure 03。 其中一批已进驻宝马斯巴坦堡工厂，承担一项新的物流作业。 人形机器人的 iPhone时刻 是否已经到来？ 当两家公司均宣称 已从实验室走向商业化 ，其中哪一方更接近事实，哪一方仍停留在愿景阶段？ Figure 03的规格几乎全部公开且可核实，身高168厘米，体重60公斤，负…”
[35] 工厂调研转述 <https://wallstreetcn.com/articles/3779791> 摘录：“特斯拉两大核心叙事——Robotaxi规模化部署与Optimus人形机器人商业化——正从概念走向可量化的执行路径。 摩根大通近期对特斯拉弗里蒙特工厂完成实地调研，并与公司投资者关系团队举行会面，整体来看，分析师对上述两条业务线的推进节奏给予积极评价，认为均与此前管理层披露的时间表基本吻合。 据摩根大通报告，Robotaxi车队规模扩张的关键触发点已明确锁定在FSD v15的年内推出。 管理层表示，Cybercab小规模测试车队的技术验证工作持续推进，约40%的v15核心技术模块已在Robotaxi车队中接受测试，初步反馈积极； 与此同时，公司有意控制Model Y向Robotaxi车队的转化数量，显示出对Cybercab近期可规模化交付的信心。 Optimus方面，Gen 3设计已完成定稿，供应链已基本锁定，生产线正在弗里蒙特工厂安装中，量产启动（SoP…”

### Boston Dynamics：动态控制积累转向电动工业平台

**技术路径。** Boston Dynamics在2024年退役液压Atlas，转向全电动版本。这个变化降低了液压系统的工程负担，更适合工业产品化。公司同时拥有Spot四足和Stretch仓储产品，覆盖运动、巡检及物流执行。[24]

**产品进度。** RobotBelt报道2026年1月5日发布生产版Atlas：高约1.9米、56个自由度、负载50千克，支持少于3分钟自动换电。按该报道应归入“生产版与早期工业化”，2026年产能主要对应Hyundai RMAC及Google DeepMind合作。[30]

**商业化进度。** Atlas的早期市场是工业搬运和制造任务。相比独立创业公司，Hyundai可以提供制造场景、供应链和产业支持。Spot则已形成对外销售和巡检集成经验，为企业软件、现场支持及维护组织提供基础。

**融资情况。** 2021年Hyundai并购口径约11亿美元，当时取得80%股权。它是产业并购与集团支持路径，不是Atlas专项私募融资。Hyundai规划年产3万台机器人工厂，也应与Atlas当期实际交付分开理解。[24][11]

**团队情况。** 公司1992年起源于MIT Leg Lab，CEO为Robert Playter。其优势是长期动态控制、机械设计和现场产品经验。相应挑战是把高性能运动能力，变成可维护、可复制且成本合理的工业任务系统。[24]

本节参考文献：
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“融资：现隶属于现代汽车集团（2021 年以约 11 亿美元收购）。 此前曾由软银和谷歌/ Alphabet 持有。 独特之处：三十年的运动学研究使波士顿动力公司在双足运动方面拥有无可比拟的专业知识。 其用于车队管理的 Orbit 云平台是企业部署的关键优势。 Agility Robotics — Digit 总部：俄勒冈州科瓦利斯 成立时间：2015 年 CEO：Damion Shelton Agility Robotics 打造了 全球首款商用人形机器人 。 当其他公司仍在试点阶段时，Digit 已在客户仓库投入使用。 主要产品：Digit 是一款专为物流而设计的双足人形机器人，可执行拣货、堆垛和卸货等任务。 它的设计目标是填补美国超过 100 万个物料搬运岗位的空缺。 商业模式：机器人即服务 (RaaS)，并配备用于车队管理的 Agility Arc 云平台。 主…”
[30] 另一累计口径 <https://robotbelt.com/americas-humanoid-robot-race-six-players-three-paths/> 摘录：“Agility charges about US$25 an hour under a robots-as-a-service model, while US warehouse labour costs about US$30 or more an hour. The company target is to push operating cost to US$2 to 3 an hour at scale. Customers beyond Amazon: Toyota Canada signed a robots-as-a-service deal in February 2026. GXO and Latin American e-commerce firm Mercado Libre use it too. On the manufacturing side…”
[11] 四足市场调查 <https://www.goedelmachines.com/blog/quadruped-market-survey> 摘录：“This is Part 3 of our Physical AI series. Read the other articles: Part 1: Quadruped control architecture · Part 2: Quadruped mechanics. Quadrupeds are being used for industrial inspection, research, security, and work in places that are difficult or hazardous for people to reach. The robots look similar, but their customers and business models differ considerably. A small platform boug…”

### 中国代表公司：平台销售与工业解决方案是两种生意

| 公司与地区 | 技术路径 | 产品及商业锚点 | 资金锚点 | 团队锚点 |
|---|---|---|---|---|
| 优必选，深圳 | 本体、小脑、大脑、群体智能 | 2026年上半年全尺寸921台 | 2025年三次配售 | 周剑；研发1,103人 |
| 宇树，杭州 | 核心部件、运动控制全栈自研 | 2025年纯人形出货超过5,500台 | 2025年6月估值127亿元 | 王兴兴 |
| 智元，上海 | 本体、遥操作、数据基础设施 | A2工业试点与平台扩展 | 宁德时代战略支持 | 彭志辉等核心创业团队 |
| 智平方，深圳 | 轮式升降本体、GOVLA | 2025年9月订单超过500台 | 2026年2月B轮10亿元 | 郭彦东、AI与硬件团队 |
| 傅利叶，上海 | 康复机器人向通用人形延伸 | GR-1平台、GR-3伙伴定位 | 康复经营与人形研发协同 | 顾捷；康复与生物力学积累 |

**表格依据。** 分别采用优必选公告[3]、宇树招股书[36]、公司产业画像[24]、智平方产品报道[37]和融资整理[38]。

本节参考文献：
[3] 中期技术披露 <https://stockn.xueqiu.com/09880/20260828390148.pdf> 摘录：“2025年12月24日、2026年3月10日、2026 年3 月12 日及2026 年4 月24 日的公告 所披露，於2026年3月，我們收購了浙江鋒龍電氣股份有限公司（「鋒龍股 份」）65,529,906 股A股（約佔鋒龍股份全部已發行股本的29.99%股權），並成 為鋒龍股份控股股東（經計該通函所詳述該等賣方放棄與預接受股份有 於2026年4月，我們收購了鋒龍…”
[36] 宇树技术披露 <https://dataclouds.cninfo.com.cn/sjother2/documents/2026/2026-05-25/3d7fc0538abe281340a95c9c77a90525.pdf> 摘录：“12 中网投 6.0926 2.1089% 13 Vertex 5.2248 1.8085% 14 嘉兴睿利 4.7067 1.6292% 15 海克斯康 3.8456 1.3311% 16 新疆深创投 3.7234 1.2888% 17 光合贰期 3.5340 1.2232% 18 经纬叁号 3.4467 1.1930% 19 浙江容腾 3.4288 1.186…”
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“4.03 亿美元的 A 轮融资（2025 年 3 月，由谷歌领投）和 5.2 亿美元的 A 轮扩展融资（2026 年 2 月），投后估值约为 50 亿美元。 2025 年入选 CNBC Disruptor 50 强。 独特之处：务实且以投资回报率为导向的方法。 当竞争对手追逐头条新闻时，Apptronik 专注于在特定的物流任务中证明其经济价值。 首席执行官 Je…”
[37] 产品形态与GOVLA <https://www.cls.cn/detail/2135323> 摘录：“nav=tips class= m-r-50 f-s-15 c-6a6a6a h-t-d-u 帮助 /a /div /div /div div class= p-r m-a w-1200 div class= c-b p-t-16 p-b-16 h-52 level-1-nav-box a href= / class= f-l h1 div class= p-r…”
[38] 2026年融资节点 <https://news.pedaily.cn/202606/565245.shtml> 摘录：“千寻智能就是这场资本盛宴中最耀眼的明星之一，4个月完成3轮融资，累计45亿，一家头部公司半年的融资额，相当于200家公司总和的三分之一。 钱没有消失，只是流向了少数人。 决定这些钱流向谁的，不在是传统的财务 VC，而是产业/大厂资本和地方国资/政府引导基金，他们用截然不同的逻辑在押注，有人要生态绑定，有人要税收落地，有人要供应链话语权。 这篇复盘试图回答五个问题：…”

### 优必选：工业数据和上市公司收入形成支撑

**技术路径。** 优必选以“具身大脑、仿人小脑、高性能本体、群体智能”组织技术。硬件包括高性能伺服驱动与类人眼双目视觉；软件覆盖全身控制、强化学习、灵巧操作和纯视觉导航。BrainNet 2.0与Co-Agent承担任务分解和多机协同。[3]

**模型与数据。** 公司构建Thinker基座、Thinker-WM世界模型和Thinker-VLA行动模型。披露真机数据约1,100万条，超过80%来自工业场景；端侧全功能模块GPU显存需求由64GB降至32GB。后者直接影响部署硬件选择和成本。[20]

**产品进度。** Walker S在2025年进入小批量工业交付。2026年上半年，Walker S2量产交付扩张；6月发布Cruzr Y1、Walker C1、U1，分别覆盖工业仓储、商服教育和消费陪伴。新产品发布与既有产品销售，按各自阶段理解。[20]

**商业化进度。** 截至2026年6月30日止六个月，全尺寸具身智能人形产品及解决方案收入5.903亿元，销量921台。公司总收入12.691亿元，期内亏损3.388亿元。全尺寸业务约占收入46.5%，计算为5.903÷12.691。[3]

**收入应看产品包。** 按5.903亿元÷921台，估算每台对应产品及解决方案收入约64.1万元。这是收入摊值，不是裸机售价。工业客户包括空客、比亚迪、吉利、富士康等，任务集中在搬运、上下料、分拣和拆码垛。[20]

**融资情况。** 2023年12月香港IPO约1.3亿美元，上市前私募融资超过9.4亿美元。2025年2月、7月、11月配售净额分别为8.7632亿、24.1026亿、30.5571亿港元，合计63.4229亿港元。配售资金支持产品迭代、商业化和产业链整合。[24][3]

**团队情况。** 创始人为周剑。2026年上半年研发人员1,103人，研发投入超过3亿元。其组织路线不是单一模型实验室，而是伺服、本体、模型、工业数据及客户方案共同推进；下一阶段重点是把订单转成持续验收和复购。[24][20]

本节参考文献：
[3] 中期技术披露 <https://stockn.xueqiu.com/09880/20260828390148.pdf> 摘录：“2025年12月24日、2026年3月10日、2026 年3 月12 日及2026 年4 月24 日的公告 所披露，於2026年3月，我們收購了浙江鋒龍電氣股份有限公司（「鋒龍股 份」）65,529,906 股A股（約佔鋒龍股份全部已發行股本的29.99%股權），並成 為鋒龍股份控股股東（經計該通函所詳述該等賣方放棄與預接受股份有 於2026年4月，我們收購了鋒龍股份28,450,000股A股（約佔鋒 龍股份全部已發行股本的13.02%），本公司合共持有鋒龍股份93,979,906股 A股（約佔其全部已發行股本的43.01%）。 鋒龍股份之財務業績已自2026年 4月起計入本集團合併財務報表。 除上文所述外，本集團於報告期間概無重大收購及出售事項。 截至2026年6月30日止六個月期間，我們的業務主要位於中國，大部分交 本公司及附屬公司的功能貨幣為人民幣。 月30 日，我們的現金及現金等價物結餘主要以人民幣計值。 外匯風險管理採取審慎政策。 於報告期間，我們並無就外幣交易、資產 及負債制定外幣對沖政策。 我們將定期審閱外匯風險，並於有需要時使 用衍生金融工具對沖有關風險。 截至2026年6月30日，我們的業務並無面 截至2025 年12月31日及2026 年6 月30日，本集團附屬公…”
[20] 优必选数据披露 <https://www.iyiou.com/news/202608281139470> 摘录：“优必选2026年上半年营收12.7亿元，全尺寸人形产品收入增长1445% 8月28日， 人形机器人第一股 优必选（股份代码：9880.HK）发布2026年中期业绩报告：总营收12.7亿元，同比大幅增长104.2%； 人形机器人总销量16123台，同比大幅增长268.3%； 全尺寸具身智能人形机器人（非遥控非玩具，大脑芯片算力≧200T，身高160cm以上）收入5.9亿元，同比大幅增长1445.0%，已成为公司主要收入组成和核心增长引擎； 研发投入超3亿元，研发人员规模达1103人，研发投入力度、人才储备体量远超同行； 整体毛利5.7亿元，同比大幅增长160.9%； 整体毛利率为44.7%，同比提升9.7个百分点； 报告期内公司实现大幅减亏，经调整EBITDA为-1.7亿元，同比减亏1.5亿元，大幅减亏45.9%，朝着扭亏为盈的目标健康快速发展。 一、全尺寸人形机器人收入增1445%，三项全球第一 2026 年上半年，优必选交出高增长、高质量的中期答卷：总营收同比增长104.2%，达12.7亿元，在人形机器人公司营收规模中位列全球第一； 人形机器人总销量为16123台，同比增长268.3%，斩获全球销量第一； 全尺寸具身智能人形机器人（非遥控非玩具，大脑芯片算力≧200T，身高160c…”
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“特斯拉的目标是将每台的制造成本控制在 2 万美元，零售目标价为 2 万至 3 万美元。 现状： 根据马斯克在 2025 年第四季度财报电话会议上的说法，Optimus 正在特斯拉自己的工厂里执行基本任务，但 尚未实质性投入使用 。 特斯拉计划改造其弗里蒙特工厂，以便每年生产多达 100 万台 Optimus。 预计于 2027 年底开始公开销售。 独特之处： 没有任何一家人形机器人公司拥有特斯拉那样的制造规模、AI 计算基础设施或品牌知名度。 如果马斯克的计划哪怕只有部分准确，特斯拉也可能凭借其庞大的产量主导消费级人形机器人市场。 融资：由特斯拉自筹资金。 该公司已承诺在 2026 年投入 200 亿美元的资本支出，用于 Optimus 和其他项目的制造和计算基础设施。 总部：加利福尼亚州圣何塞 成立时间：2022 年 CEO：Brett Adcock Figure AI 是估值增长最快的人形机器人公司，在 2025 年 9 月融资 10 亿美元后，估值达到 390 亿美元。 在不到三年的时间里，Figure 从一家白手起家的初创公司跃升为历史上资金最雄厚的机器人公司之一。 主要产品：Figure 02 是该公司的工业级人形机器人，目前正在与宝马合作进行汽车制造试点项目。 Figur…”

### 宇树科技：低成本本体与开发者生态

**技术路径。** 宇树采用“本体+小脑+大脑”全栈路径。自研范围包括电机、减速器、编码器、关节模组、灵巧手、激光雷达、能源与散热系统。深度强化学习首先用于运动控制，形成高速奔跑、抗扰动和复杂动作能力。[36]

**模型与数据。** 公司前期研发重点是本体和运动控制，自2024年加强认知模型。WMA于2025年下半年发布，VLA于2026年1月发布；招股书将通用模型的应用阶段描述为自有工厂等场景测试。由此看，成熟本体产品与通用任务能力处在不同阶段。[36]

**产品进度。** H1于2023年面市，当年销售5台；G1于2024年上市，当年销售410台。2025年纯人形出货超过5,500台，不含轮式双臂。R1和H2于2025年加入产品线，形成不同尺寸、配置和价格的开发平台。[39]

**商业化进度。** G1起价8.5万元，R1 Air为2.99万元。2025年前三季度人形收入中，科研教育占73.60%，商业消费17.39%，行业应用9.01%。这意味着平台出货已经形成规模，但主市场仍是科研、开发与展示，而非大规模替代工厂岗位。[39]

**成本与经营。** 招股书相关报道列，人形单位成本从2023年7.32万元降至2025年前三季度6.22万元。2025年公司收入16.9927亿元、扣非净利润5.9075亿元；2026年一季度收入增长68.49%，扣非净利润下降52.55%。增长与加大研发、销售投入可以同时发生。[39][36]

**融资情况。** 2025年6月融资投后估值127亿元，公开股东包括美团、红杉中国、经纬、腾讯等。2026年7月1日证监会同意IPO注册；8月媒体报道发行估值约90亿美元、募资约9.05亿美元。监管注册与媒体发行数据分别标注。[39][40][41]

**团队情况。** 王兴兴为创始人、董事长和实际控制人。员工持股平台上海宇翼持股10.94%；公司计划扩充AI、运动控制与感知交互研发。下一阶段关键是把本体和成本优势，转成更多工业操作数据及可重复任务能力。[42]

本节参考文献：
[36] 宇树技术披露 <https://dataclouds.cninfo.com.cn/sjother2/documents/2026/2026-05-25/3d7fc0538abe281340a95c9c77a90525.pdf> 摘录：“12 中网投 6.0926 2.1089% 13 Vertex 5.2248 1.8085% 14 嘉兴睿利 4.7067 1.6292% 15 海克斯康 3.8456 1.3311% 16 新疆深创投 3.7234 1.2888% 17 光合贰期 3.5340 1.2232% 18 经纬叁号 3.4467 1.1930% 19 浙江容腾 3.4288 1.1868% 20 Galaxy Z 2.9432 1.0187% 21 成都龙珠 2.9432 1.0187% 22 中关村科学城 2.6894 0.9309% 23 容腾二号 2.6638 0.9220% 24 厦门雅恒 2.6144 0.9049% 25 极思投资 2.5943 0…”
[39] 产品销售时间线 <https://www.eeo.com.cn/2026/0320/813654.shtml> 摘录：“经济观察报 关注 2026-03-20 21:52 2026年3月20日，宇树科技股份有限公司（下称 宇树科技 ）首次公开发行股票并在科创板上市的招股说明书（预先审阅稿）（下称 招股书 ）正式披露，上交所同日受理其科创板IPO申请。 这也是科创板发行上市预先审阅机制落地后的第2单申报企业。 根据招股书数据，宇树科技拟公开发行不低于4044.64万股，募集资金42.02亿元。 这家成立于2016年的公司，主要产品是通用机器人，创始人兼实际控制人王兴兴持有公司23.82%的股份，通过特别表决权安排控制68.78%的表决权。 宇树科技的股东名单包括美团、红杉中国、经纬创投、腾讯等，2025年6月最近一轮融资投后估值为127亿元。 招股书显示，2…”
[40] 证监会批复 <https://www.csrc.gov.cn/csrc/c105906/c7642867/content.shtml> 摘录：“索 引 号 bm56000001/2026-00007362 分 类 --- --- --- --- 名 称 关于同意宇树科技股份有限公司首次公开发行股票注册的批复 文 号 证监许可〔2026〕1612号 主 题 词 关于同意宇树科技股份有限公司首次公开发行股票注册的批复 中国证券监督管理委员会收到上海证券交易所报送的关于你公司首次公开发行股票并在科创板上市的审核意见及你公司注册申请文件。 根据《中华人民共和国证券法》《中华人民共和国公司法》《国务院办公厅关于贯彻实施修订后的证券法有关工作的通知》（国办发〔2020〕5号）和《首次公开发行股票注册管理办法》（证监会令第205号）等有关规定，经审阅上海证券交易所审核意见及你公司注册申请文件，…”
[41] IPO媒体口径 <https://robot24.com/quadruped-robots-finally-have-a-business-model-so-why-is-the-us-banning-the-cheapest-ones> 摘录：“Quadruped Robots Are Becoming Big Business: Here’s Why The US Is Targeting Chinese Makers Quadruped robots now run paid inspection contracts for oil, gas, and utility operators. A new US rule just decided which country's robots get to keep doing that. Boston Dynamics, Switzerland's ANYbotics and China's Unitree have turne…”
[42] 团队与人才规划 <https://static.sse.com.cn/stock/disclosure/announcement/c/202603/002178_20260320_QY8F.pdf> 摘录：“24 厦门雅恒 2.6144 0.9049% 25 极思投资 2.5943 0.8980% 26 德迅投资 2.5024 0.8662% 27 广州初心 1.8747 0.6489% 28 杭州初心 1.7638 0.6105% 29 中移和创 1.7295 0.5986% 30 腾讯科技 1.7295 0.5986% 31 无锡锦秋 1.7295 0.5986% 32 琥珀安云 1.7259 0.5974% 33 江苏疌泉 1.7144 0.5934% 34 杭州灏月 1.2971 0.4490% 35 创新资本 1.0839 0.3752% 36 上海科创 1.0823 0.3746% 37 中证投资 0.9757 0.3377% 3…”

### 智元机器人：本体、数据采集与生态共同推进

**技术路径。** 智元总部上海，产品包括远征A2、A2-W、X1/X2研究平台和OmniHand等。其路径不只是一台双足整机，而是本体、末端执行器、数据集及开发生态组合。行业报告将GO-1列为端到端任务执行方向。[24][43]

**学习与控制。** 智元建设人工操作员网络与机器人部署组成的遥操作采集基础设施。其技术逻辑是先取得与真实本体一致的动作数据，再用于操作模型训练。深蓝学院介绍的GenieReasoner，还用流匹配动作分词器把推理与连续轨迹生成连接起来。[31][17]

**产品与商业。** A2面向工业和物流，公开画像给出约1.73米高度、约30千克载荷，并列有汽车OEM试点。2026年工作重点是提高产量、扩大数据采集机器人队伍及非结构化物流能力。行业报告列A2约20万元、2026年目标4,000台，这里保留为报告中的价格和目标。[31][43]

**融资与团队。** 宁德时代是公开产业支持者，资本关系与电池、制造资源具有路线关联。彭志辉是核心创业团队代表，公司于2023年创立。组织能力要同时覆盖本体工程、模型、数据采集和生产交付，其价值应看数据能否减少新客户的任务适配成本。[24]

本节参考文献：
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“编译：Felix, PANews 人形机器人行业正呈现爆发式增长，从少数几个研究实验室发展成为 2025 年规模达 29 亿美元的全球市场，预计到 2030 年将达到 40 亿至 180 亿美元。 数十家人形机器人公司目前正竞相制造能够行走、说话并与人类协同工作的机器。 本指南旨在介绍 2026 年主流人形机器人公司，包括其主要机器人、融资情况、定价以及每家公司的独特之处。 - 估值最高： Figure AI（估值 390 亿美元） - 价格最低： 宇树科技 G1（1.6 万美元）”
[43] GO-1路线 <https://pdf.dfcfw.com/pdf/H3_AP202605071822028328_1.pdf?1778171901000.pdf> 摘录：“图表24 2026 年端到端大模型技术参数对比 ............................................................ 图表25 具身智能技术体系架构 ................................................................................. 图表26 世界模型技术路线对比 ...........................................…”
[31] Digit产品画像 <https://www.evsint.com/zh-CN/top-8-humanoid-robot-companies-2026/> 摘录：“上次更新时间：4月24，2026 2026年最值得关注的8家人形机器人公司分别是：Figure AI、Agility Robotics、特斯拉、波士顿动力、Apptronik、1X Technologies、Unitree Robotics和AgiBot。 我们根据三个标准对它们进行排名：商业部署规模、硬件技术成熟度（自由度、有效载荷、运动可靠性）以及软件栈深度，特别是每家公司是否已从远程操作转向自主操作或视觉-语言-动作（VLA）模型驱动的操作。 对于希望将此全球人形机器人市场…”
[17] Fast-WAM技术介绍 <https://www.shenlanxueyuan.com/news/detail/24> 摘录：“2026牌局过半，四个玩家正在交换手牌…… ——具身 四子 的 番位竞争 2026年，具身智能大模型的研究在四条技术路线上同步深化： VLA模型开始集成推理能力，VLN模型引入了自我认知机制，而世界模型也逐渐与动作生成相融合，形成了所谓的 世界动作模型 （WAM）。 基于上述技术架构与演进逻辑，2026 年各大高校、企业在四大技术赛道均产出了突破性研究成果。 本文将围绕 2026 年以来的代表性工作，逐一梳理各方向的最新进展。 VLM：从二维理解到三维空间感知 2026年，VLM…”

### 智平方：轮式升降本体与全身VLA

**技术路径。** 智平方位于深圳，AlphaBot、AlphaBot 1S、AlphaBot 2均为轮式可升降类人形。它用轮式底盘降低双足平衡负担，用升降机构拓展操作空间，再以AlphaBrain和GOVLA协同理解、推理与全身动作。[37]

**模型与数据。** GOVLA于2025年4月发布，开源版本FiS-VLA于6月推出。公司官网报告其所称评测中综合性能较π0高30%。这个结果用于说明模型路线与研发进展，商业判断仍落在汽车、半导体、生物制造等现场任务。[44]

**产品与商业。** 截至2025年9月4日，公司披露年内订单超过500台，自有产线年产能超过1,000台，进入密集交付期。客户行业集中在工业服务和部分公共服务。轮式路线更适合平整地面、高频上下料、设备操作及场内搬运。[37]

**融资情况。** 截至2025年9月的半年内完成7轮“数亿级”融资，深创投在相关A系列单家投资超过1亿元。2026年1月A+轮投后估值30亿元；2月B轮10亿元，投后估值100亿元，参与者包括百度、国泰海通、中车资本等。[37][38]

**团队情况。** 创始人兼CEO郭彦东，曾在微软、OPPO、小鹏负责核心研发，并受聘香港科技大学广州校区兼职教授。公司称团队来自微软、Google、OPPO、小鹏、Momenta及多所高校。它体现的是智能汽车与消费电子AI向机器人操作迁移的组织路径。[44]

本节参考文献：
[37] 产品形态与GOVLA <https://www.cls.cn/detail/2135323> 摘录：“url=https%3A%2F%2Fwww.cls.cn%2Fdetail%2F2135323 target= _blank rel= noopener noreferrer class= d-i-b v-a-m m-r-30 w-16 h-13 bg-r-n bg-p-c bg-s-100-100 share-weibo /a span class= d-i-b v-a-m w-16 h-13 bg-r-n bg-p-c bg-s-100-100 c-p share-weixin /span /div /div /div /div div class= f-r w-280 div div class= c-b m-b-20 w-100p h-39 l-h-38p f-s-14 t-a-c c-747474 b-b-w-1 b-b-s-s b-c-e6e7…”
[44] 智平方技术自述 <https://ai2robotics.com/about/> 摘录：“智平方（AI² Robotics）成立于2023年4月，是AGI原生的通用智能机器人企业，也是行业稀缺的生产力型通用智能机器人研发、生产与服务提供商。 公司由国家创新领军郭彦东博士创立，汇聚多位全球前2%科学家，核心团队兼具 AI 创新＋终端智能化变革 的基因，对智能终端的演进规律有深刻洞察。 智平方坚持以具身大模型为核心驱动，系统化叠加量产级机器人硬件正向设计、生产制造与规模化交付体系，形成 模型×硬件×场景 的协同优势，在真实生产力场景中实现持续的数据积累与能力迭代。 公司的产品已经在汽车、半导体、生物制造、公共服务、新零售等领域实现落地应用，订单体量与场景覆盖处于行业前列，率先跑通 数据×商业 双闭环。 面向未来，智平方致力于加速通用智能机器人的全球普及，让机器人承担更多人类不愿从事的工作，持续拓展人类能力，推动社会走向更加高效、可靠与可持续的未来。…”
[38] 2026年融资节点 <https://news.pedaily.cn/202606/565245.shtml> 摘录：“江浙沪合计117起（浙江45起、上海38起、江苏34起），这一区域更倾向于场景定义，融资企业大量集中在工业喷涂、家庭陪伴、清洁服务等垂直细分赛道。 比如智元旗下的清洁业务机器人智鼎（完成数亿 A 轮），以及理疗与家庭服务等垂直场景。 北京出大脑/本体，广东出零部件，江浙沪跑场景的格局在2026年上半年初步成型。 五、草根入局还有机会吗？ 要回答这个问题，得先看看早期融资的钱到底流向了谁。 2026年上半年，种子轮和天使轮共73起，合计融资金额不到13亿，占全赛道的3%。 穿透金额层面，我们发现另外一个故事，能拿到钱的早期团队，清一色由 大厂核心高管、学术界泰斗组成。 比如，德塔智能的创始人马晓健，本科毕业于清华大学计算机系，博士毕业于UCLA，曾在Google Robotics、NVIDIA Research工作。 2026年4月完成近亿元天使轮融资。 具…”

### 傅利叶智能：康复积累向人形与陪伴扩展

**技术路径。** 傅利叶位于上海，核心特点是从医疗康复机器人进入通用人形。行业报告列GR-1约165厘米、55千克、40个自由度，应用涉及科研教育及医疗康复。与物流型人形相比，其积累更接近人体生物力学、人机接触和辅助运动。[43]

**产品与商业。** 2026年公司画像已列GR-3，定位为可靠伙伴；RehabHub提供康复业务基础。GR-1行业报价约40万元，2026年出货目标2,000台。这里应区分既有康复业务、研究开发平台与家庭伙伴产品，三者的验收和销售逻辑不同。[24][43]

**资本与团队。** 傅利叶由顾捷领导，2015年成立。其资金与组织应按“康复业务经营基础+人形研发扩展”理解。团队的差异化不是最高奔跑速度，而是长期接触式交互和康复场景知识；通用伙伴产品则要进一步证明自主操作、家庭安全及持续使用价值。[24]

本节参考文献：
[43] GO-1路线 <https://pdf.dfcfw.com/pdf/H3_AP202605071822028328_1.pdf?1778171901000.pdf> 摘录：“图表24 2026 年端到端大模型技术参数对比 ............................................................ 图表25 具身智能技术体系架构 ................................................................................. 图表26 世界模型技术路线对比 ................................................................................. 图表27 2026 年多模态感知系统技术参数 .........................................................…”
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“编译：Felix, PANews 人形机器人行业正呈现爆发式增长，从少数几个研究实验室发展成为 2025 年规模达 29 亿美元的全球市场，预计到 2030 年将达到 40 亿至 180 亿美元。 数十家人形机器人公司目前正竞相制造能够行走、说话并与人类协同工作的机器。 本指南旨在介绍 2026 年主流人形机器人公司，包括其主要机器人、融资情况、定价以及每家公司的独特之处。 - 估值最高： Figure AI（估值 390 亿美元） - 价格最低： 宇树科技 G1（1.6 万美元） - 资历最老： 波士顿动力 (Boston Dynamics)（30 多年） - 生产规模最大： 特斯拉（目标年产 100 万台） - 首个商业化部署： Agility Robotics Digit - 最适合家用： 1X NEO（售…”

### 家庭与认知人形：1X和NEURA选择更宽的任务边界

| 公司与地区 | 本体及模型方向 | 产品阶段 | 商业价格或信号 | 融资与团队 |
|---|---|---|---|---|
| 1X，挪威及美国 | 腱驱动、软壳、端侧VLA | EVE部署；NEO测试与早期供货 | 2万美元或499美元/月 | OpenAI等；Børnich |
| NEURA，德国Metzingen | 多形态认知机器人、技能平台 | 4NE1预订与产品准备 | 单台9.8万欧元报价 | 2026年C轮最高14亿美元；约1,400人 |

**1X的技术路径。** 1X先以轮式EVE进入安保和设施服务，再以双足NEO进入家庭。NEO采用自研腱驱动和聚合物软壳，Redwood约1.6亿参数VLA部署在Jetson Thor上。人类视频、实际部署数据和世界模型共同支撑其学习路线。[30]

**1X的产品商业。** NEO于2025年10月开放预订，媒体称首年1万台名额5天售罄，2026年开始美国供货。价格为2万美元买断或499美元/月。Hayward工厂目标年产1万台，San Carlos目标2027年底年产10万台；早期家庭测试同时显示远程协助的重要性。[30]

**1X的融资团队。** 创始人为Bernt Øyvind Børnich。2023年OpenAI领投2,350万美元A轮；不同时间的融资摘要分别列累计约1亿美元和超过1.25亿美元，投资者还包括Tiger Global、三星。其组织特点是挪威本体研发基础与美国制造、家庭部署结合。[31][24]

**NEURA的技术路径。** NEURA同时布局协作臂LARA、MAiRA，移动平台MAV、服务机器人MiPA和4NE1。Neuraverse承担操作系统与技能市场角色。2026年4NE1 Gen 3.5披露Qualcomm Dragonwing参考设计；供应商比较另列AURA AI、环视相机和人工皮肤配置。[45][34]

**NEURA的产品商业。** 4NE1按公司时间表在2026年底可用，接受100欧元可退款预订。供应商表列个人单台9.8万欧元，20台以上每台6万欧元；媒体专题列公司订单及部署管线超过10亿美元。其当前阶段以产品准备和预订理解，下一步是制造及客户现场兑现。[45]

**NEURA的融资团队。** 2024年A轮6,600万欧元，2025年1月B轮1.2亿欧元。2026年6月10日宣布C轮最高14亿美元，Tether领投，Qualcomm、Amazon、NVIDIA、Bosch、Schaeffler等参与。创始人David Reger于2019年创立公司，员工约1,400人。[45]

本节参考文献：
[30] 另一累计口径 <https://robotbelt.com/americas-humanoid-robot-race-six-players-three-paths/> 摘录：“Agility charges about US$25 an hour under a robots-as-a-service model, while US warehouse labour costs about US$30 or more an hour. The company target is to push operating cost to US$2 to 3 an hour at scale. Customers beyond Amazon: Toyota Canada signed a robots-as-a-service deal in February 2026. GXO and Latin American e-commerce firm Mercado Libre use it too. On the manufacturing side, Agility runs RoboFab in Salem,…”
[31] Digit产品画像 <https://www.evsint.com/zh-CN/top-8-humanoid-robot-companies-2026/> 摘录：“上次更新时间：4月24，2026 2026年最值得关注的8家人形机器人公司分别是：Figure AI、Agility Robotics、特斯拉、波士顿动力、Apptronik、1X Technologies、Unitree Robotics和AgiBot。 我们根据三个标准对它们进行排名：商业部署规模、硬件技术成熟度（自由度、有效载荷、运动可靠性）以及软件栈深度，特别是每家公司是否已从远程操作转向自主操作或视觉-语言-动作（VLA）模型驱动的操作。 对于希望将此全球人形机器人市场地图与EVST自身产品方向进行比较的读者，请参阅以下内容。 EVST 具身人工智能解决方案涵盖了该公司的人形机器人、灵巧手、四足机器人和具身人工智能数据收集路线图。 我们如何对这些公司进行排名 首先是商业部署：已向工业或物流领域的付费客户交付机器人的公司得分高于仍在保密协议下进行试点运营的公司。 其次是已披露的总融资额和估值，以此作为衡量公司发展前景和投资…”
[24] Figure融资节点 <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> 摘录：“编译：Felix, PANews 人形机器人行业正呈现爆发式增长，从少数几个研究实验室发展成为 2025 年规模达 29 亿美元的全球市场，预计到 2030 年将达到 40 亿至 180 亿美元。 数十家人形机器人公司目前正竞相制造能够行走、说话并与人类协同工作的机器。 本指南旨在介绍 2026 年主流人形机器人公司，包括其主要机器人、融资情况、定价以及每家公司的独特之处。 - 估值最高： Figure AI（估值 390 亿美元） - 价格最低： 宇树科技 G1（1.6 万美元） - 资历最老： 波士顿动力 (Boston Dynamics)（30 多年） - 生产规模最大： 特斯拉（目标年产 100 万台） - 首个商业化部署： Agility Robotics Digit - 最适合家用： 1X NEO（售价 2 万美元或每月 499 美元） 2026 年人形机器人公司完整对比： 特斯拉 — Optimus 总部：德克萨斯州…”
[45] NEURA产品体系 <https://www.humanoidsdaily.com/features/the-humanoids-of-europe> 摘录：“- Published on The Humanoids of Europe: Built by Their Customers One tap, and our reporting appears more often in your Google Top Stories. It makes a real difference to a small newsroom. Rich Robinson Jee Chee Ren · Executive tour See China’s AI and robotics ecosystem first-hand. Six days exploring AI, robotics and advanced manufacturing. With Rich Robinson, Clinical Professor of Entrepreneurship at Peking University…”
[34] Apollo规格与配置 <https://ifactoryapp.com/industries/manufacturing-plant/manufacturing-humanoid-vendor-comparison-unitree-apollo-figure-2026> 摘录：“DOF 31 ~30 40+ 45 28 + 50 hand Battery Runtime ~3 hr 4 hr (hot-swap) ~5 hr wireless 6-8 hr (hot-swap) 10-12 hr Compute Integrated Gemini Robotics Helix AI NVIDIA Thor T5000 Tesla Custom Pricing $40,900 Contact sales $25/hr (BMW) €60K-€98K $20K-$30K target Availability Q2 2026 Pilots active Commercial June 2026 External 2027 Total Cost of Ownership and ROI Signals List price is rarely the deciding factor in a humanoid…”

### 欧洲补充案例：工业能力并不只来自双足整机

**欧洲路径更重集成。** 欧洲代表企业往往把工业客户、零部件供应商和资本关系结合起来。轮式双臂、轮足、灵巧手和外骨骼技术复用，都是与标准双足人形竞争的现实方案。[45]

| 公司与地区 | 技术及产品 | 产品商业进展 | 融资节点 | 团队背景 |
|---|---|---|---|---|
| Agile Robots，德国慕尼黑 | 工业臂、力觉、Agile ONE | 2025年公司收入约3亿欧元 | 累计约15亿美元 | DLR分拆；约3,200人 |
| Humanoid，英国伦敦 | 轮式双臂、KinetIQ分层栈 | Ford测试83次抓取/小时 | 2026年A轮1.52亿美元 | Artem Sokolov创立 |
| Hexagon，瑞典及苏黎世 | AEON轮足、测量与数字孪生 | BMW生产任务；7年千台承诺 | 上市集团业务投入 | Arnaud Robert领导 |
| Wandercraft，法国巴黎 | 外骨骼控制复用于Calvin-40 | Renault处理轮胎；40千克负载 | 报道列7,500万美元D轮 | École Polytechnique源起 |

**替代方案值得比较。** Humanoid把轮式移动操作作为工业主线，双足作为研究方向；Hexagon以轮足结合平地效率与越障。Wandercraft则把医疗产品中验证的执行和平衡软件复用到工业本体。它们共同说明，通用操作的突破不必等待统一的人形外观。[45]

**本节判断。** 工业人形正在形成真实产品，但平台出货、客户生产和家庭预订是三种不同进度。Figure、Agility、优必选、宇树各自领先的维度，应分别判断。

本节参考文献：
[45] NEURA产品体系 <https://www.humanoidsdaily.com/features/the-humanoids-of-europe> 摘录：“- Published on The Humanoids of Europe: Built by Their Customers One tap, and our reporting appears more often in your Google Top Stories. It makes a real difference to a small newsroom. Rich Robinson Jee Chee Ren · Executive tour See China’s AI and robotics ecosystem first-hand. Six days exploring AI, robotics and advanced manufacturing. With Rich Robinson, Clinical Professor of Entrepreneurship at Peking University Beijing · Guangzhou · Shenzhen 29 November–4 December 2026 Referral partnership · We earn a commission on referred bookings. - Seven European manufacturers — NEURA Robotics, Agile Robots, Hexagon, Humanoid, Wandercraft, Generative Bionics and UMA — now build humanoid hardware on the continent, across five countries. - Europe's distinguishing feature is not the robots but the buyers: Schaeffler, Bosch, Renault, BMW, Siemens, SAP and Fincantieri are simultaneously customers, component suppliers, contract manufacturers and, in several cases, shareholders. - Schaeffler alone has committed to a mid-four-digit NEURA rollout by 2035, at least 1,000 Hexagon AEON units over seven years, and a four-digit Humanoid deployment by 2032 — while supplying actuators to all three. - Disclosed capital is concentrating fast: NEURA's $1.4 billion Series C (June 2026) and Humanoid's $152 million Series A at a $1.35 billion valuation (July 2026) sit alongside Agile Robots' ro…”

## 移动操作、仓储物流与工业：近期商业化更看系统能力

本节参考文献：
[45] NEURA产品体系 <https://www.humanoidsdaily.com/features/the-humanoids-of-europe> 摘录：“- Published on The Humanoids of Europe: Built…”

### 五家代表公司的共同比较

**仓储优势来自可计量任务。** 箱子、料箱、托盘和工位流程具有重复性，吞吐、停机和人工节省可以被计量。IFR认为AMR物流已成熟，创业活动正从硬件开发更多转向AI软件及系统集成。[1]

| 公司与地区 | 技术路径 | 产品与商业锚点 | 资金路径 | 团队依据 |
|---|---|---|---|---|
| Dexterity，美国Redwood City | 世界模型、技能代理、工业双臂 | Fortune 50真实动作超过1亿次 | 2025年融资9,500万美元 | Samir Menon、Stanford背景 |
| Covariant，美国伯克利 | RFM-1、仓储拣选 | 15余个伙伴、3,000余万次拣选 | 2023年C轮7,500万美元 | Berkeley创业团队 |
| Intrinsic，美国Alphabet体系 | Flowstate工业机器人软件 | 软件编程与集成平台 | Alphabet支持 | 感知与规划组织 |
| Amazon Robotics，美国 | AMR、机械臂、履约编排 | 整体机器人超过100万台 | 内部资本与技术许可 | 履约工程、模型团队 |
| Mujin，日本东京 | 数字孪生、运动规划、控制器 | 工业商业交付及全球扩张 | D轮首交割2.33亿美元 | 两位创始人、500余员工 |

本节参考文献：
[1] IFR服务机器人统计 <https://ifr.org/img/worldrobotics/Executive%5FSummary%5FWR%5F2025%5FService%5FRobots.pdf> 摘录：“(AP8), professional cleaning (AP2), agriculture (AP1), and search & rescue, security Mobile robot solutions are well established in transportation and logistics (AP5) with 14% more units sold in 2024. More than every other professional service robot sold in 2024 was built for the transportation of goods or cargo. This is also reflected in the number of suppliers with this application group. The IFR Statistical Department is currently aware of 333 companies that supply various types of logistics robots. though sales of robots for hospitality (AP8) decreased by 11%, the number of sales in absolute numbers with more than 42,000 sold remains the second highest volume amongst all application groups. Demand for professional cleaning robots (AP2) grew Sales of more than 25,000 units were reported to the IFR Statistical Department. Sales in agriculture (AP1) contracted slightly by 6% with close to 19,500 units sold For the application group of search & rescue, security robots (AP7) 3,128 robots sold (+19%) were reported for 2024. The application group inspection and maintenance (AP3) experienced tremendous gr…”

### Dexterity：工业机械臂与世界模型结合

**技术路径。** Dexterity的Mech是物流制造专用工业设备，机械臂来自Kawasaki，精密运动部件还来自HiWin。平台以Foresight世界模型和68余个技能代理，编排感知、空间推理、装箱、轨迹、力控和任务分配。硬件抽象层允许技能适配不同臂、夹爪和底盘。[10]

**产品与商业。** 公司称模型训练经验超过1亿次自主动作，Fortune 50客户运营中完成1亿余次真实动作。客户包括FedEx和UPS。阶段为工业运营与扩展，价值集中在装箱、分拣等高频任务，商业接口是设备、软件和现场集成。[10][46]

**可靠性含义。** 公司列Mech超过10年MTBF，并配置安全监控和实时性能遥测。MTBF是硬件系统故障间隔指标，不能解释为AI策略十年才犯一次任务错误。对采购方，更重要的是任务异常率、恢复时间与整个生产系统的可用性。[10]

**融资与团队。** TechCrunch在2025年3月11日引述Bloomberg称，融资9,500万美元，投后估值16.5亿美元，累计接近3亿美元。投资者包括Lightspeed和Sumitomo。创始人兼CEO Samir Menon有Stanford博士研究经历，路线强调任务专用AI与工业系统工程。[46]

本节参考文献：
[10] Dexterity平台 <https://dexterity.ai/platform> 摘录：“The result: 10+ years of mean time between failures, built to operate in 0°-50°C temperatures, up to 1,500m altitude, and up to 90% humidity. Made in America Designed, developed, and assembled in Redwood City, California. Key submodules sourced from world-leading manufacturers in Japan and Taiwan. Tested and validated in-house before every deployment. We're not looking for humanoid robots — we're looking for super humanoid robots, because maybe they need to have a couple of elbows. More degrees of freedom. As covered…”
[46] 客户与业务报道 <https://techcrunch.com/2025/03/11/yet-another-ai-robotics-firm-lands-major-funding-as-dexterity-closes-latest-round/> 摘录：“The intersection of robotics and AI continues to attract attention from investors and Big Tech alike. The latest indicator? Dexterity, a startup specializing in industrial robots with human-like finesse, has raised $95 million at a post-money valuation of $1.65 billion, per Bloomberg. The investment, which includes backing from Lightspeed Venture Partners and Sumitomo Corp., highlights the growing demand for machinery powered by AI and comes amid a wave of excitement from companies like Meta and Apple, which are repor…”

### Covariant：从基础模型进入仓储系统与授权

**技术路径。** Covariant以RFM-1为核心，面向视觉理解、抓取和仓储拣选。硬件通过ABB等伙伴进入系统，公司的关键资产在模型、操作数据和部署经验。相比全栈人形，它用成熟工业臂降低本体研发负担。[21]

**产品与商业。** 2025年行业报告列15余个仓储合作伙伴，客户案例包括DHL、GEODIS等，累计记录3,000余万次拣选。公司从纯AI向ABB渠道中的完整系统扩展。2024年8月Amazon取得其基础模型非独家许可，形成另一种商业出口。[21][47]

**融资与团队。** 公开报告列2023年C轮7,500万美元。创始人包括Pieter Abbeel、Peter Chen、Rocky Duan，背景来自UC Berkeley机器人研究。上述核心成员及约四分之一员工加入Amazon，属于影响技术组织的重要变动；Covariant同时继续服务数十家客户。[21][47]

**路线的实际意义。** 这个案例表明，机器人基础模型公司可以通过整机系统、渠道合作或非独家授权变现。对投资者，模型资产的价值应与留存团队、客户维护及授权后的竞争关系一起判断，而不是只看累计拣选次数。

本节参考文献：
[21] 融资与团队画像 <https://www.roboticscenter.ai/research/robot-manipulation-market-landscape-2025> 摘录：“The Robot Manipulation Market Landscape 2025: Companies, Investors, and Opportunities Comprehensive overview of the robot manipulation industry — hardware vendors, software platforms, data providers, service companies, and investment landscape. The robot manipulation market is structurally reorganizing. Hardware commoditizes, software and data become the defensible layer. Here is who is building what, who is funding them, and where the gaps are. Market Structure The robot manipulation…”
[47] Amazon许可公告 <https://www.aboutamazon.com/news/company-news/amazon-covariant-ai-robots> 摘录：“With decades of experience pioneering the use of machine learning models and developing and deploying the world’s largest fleet of industrial robotics, Amazon has a long history of driving innovation in supply chain, logistics, and warehouse automation. AI technology and AWS infrastructure powers the hundreds of thousands of mobile robots, robotics arms, and other automation systems in our operations, assisting our employees as we deliver billions of customers’ orders every year. Amaz…”

### Intrinsic：把工业机器人能力放进软件平台

**技术路径。** Intrinsic于2021年从Alphabet内部孵化体系分拆，Flowstate面向工业机器人编程。其产业位置是感知、规划与软件集成，不是独立人形本体。2025年行业报告已将Flowstate列为平台产品，形成2021—2025年的公开产品发展窗口。[21]

**产品与商业。** 该路线把合作厂商的机械臂、末端执行器和传感器作为执行层，把任务编程及软件技能作为价值层。商业比较对象是软件平台和工业集成方案，而不是每台机器人硬件售价。下一阶段的决定性结果是项目部署周期、软件复用和集成伙伴扩张。

**融资与团队。** Intrinsic采用Alphabet支持的企业孵化路径。报告还列其通过吸收感知、规划相关技术组织扩展能力。团队结构与路线的关联在于软件工程、机器人技能和工业接口整合，应采用业务组织口径，与独立创业公司的私募轮次分开。[21]

本节参考文献：
[21] 融资与团队画像 <https://www.roboticscenter.ai/research/robot-manipulation-market-landscape-2025> 摘录：“The Robot Manipulation Market Landscape 2025: Companies, Investors, and Opportunities Comprehensive overview of the robot manipulation industry — hardware vendors, software platforms, data providers, service companies, and investment landscape. The robot manipulation market is structurally reorganizing. Hardware commoditizes, software and data become the defensible layer. Here is who is building what, who is funding them, and where the gaps are. Market Structure The robot manipulation industry operates as a three-layer value chain: - Hardware layer — robot arms, grippers, sensors, and mobile bases. Increasingly commoditized for standard DOF configurations. Margin pressure from Chinese manufacturers. Differentiation through precision, payload, and support. - S…”

### Amazon Robotics：规模化AMR与新型机械臂并行

**技术路径。** Amazon以AMR、Robin、Cardinal、Sparrow和Blue Jay组成履约系统。机器人、输送设备、库存和订单共同优化，平台价值在整体流程。Covariant许可则用于增强既有机器人学习、泛化和适应能力。[47]

**产品进度。** A3报道，Amazon履约中心机器人超过100万台，绝大多数是AMR；Robin机械臂约3,000—4,000台，Blue Jay当时为1台。六臂Blue Jay从概念到生产用时一年多，进入南卡罗来纳州履约中心。[4]

**商业化进度。** Amazon主要通过内部效率回收机器人投资，而非对外出售统一RaaS套餐。其百万台规模证明物流自动化的可复制性，但Blue Jay代表的新型操作能力仍要逐站扩展。整体机器人数量，不能作为单一机械臂或基础模型的部署量。

**融资与团队。** 资金来自Amazon内部投入及技术合作。应用科学负责人Aaron Parness在报道中强调，模型及基础设施帮助原型更快进入现场。团队结合履约流程、硬件工程、应用科学及Covariant研究人员，是“真实场景+模型团队”的组织方式。[4]

本节参考文献：
[47] Amazon许可公告 <https://www.aboutamazon.com/news/company-news/amazon-covariant-ai-robots> 摘录：“With decades of experience pioneering the use of machine learning models and developing and deploying the world’s largest fleet of industrial robotics, Amazon has a long history of driving innovation in supply chain, logistics, and warehouse automation. AI technology and AWS infrastructure powers the hundreds of thousands of mobile robots, robotics arms, and other automation systems in our operations, assisting our employees as we deliver billions of customers’ orders every year. Amazo…”
[4] Amazon产品规模 <https://www.automate.org/robotics/industry-insights/blue-jay-way> 摘录：“Industry Insights Blue Jay Way Amazon Blue Jay System This story first appeared in A3's Automated newsletter. Subscribe here. Development was a big piece of last week’s Blue Jay unveil. The move was something of a shift for Amazon Robotics, which has tended to spend the majority of a product reveal discussing the technology itself. Here, however, chief technologist Tye Brady devoted a chunk of his stage time not just to how the industrial system was created — but how quickly the team w…”

### Mujin：用数字孪生和厂商无关控制降低集成成本

**技术路径。** Mujin总部东京，在美国、欧洲和中国设区域办公室。MujinOS利用视觉与传感器更新工作区模型，在数字孪生中计算无碰撞路径，再控制不同品牌机器人。上层WMS、WES、MES下发任务，平台处理单元级运动和多设备编排。[9]

**控制与安全。** MujinController负责实时执行，披露UL 61010和Category 3 PLd功能安全，并连接Ethernet/IP、Profinet、Modbus等工业协议。这种路线更重视确定的设备接口、路径约束与可靠执行，不以VLA端到端作为唯一技术标签。[9]

**产品与商业。** 应用包括码垛、料箱拣选、机床上下料、卡车卸货、订单履约和车队管理。商业模式覆盖软件、控制器、系统集成和服务。下一阶段是产品化、区域工程支持与认证集成商网络，使项目经验可以跨站点复制。[48]

**融资情况。** 2025年12月2日D轮首交割2.33亿美元，由1.33亿美元股权和1亿美元债务组成，累计融资4.11亿美元。股权投资者包括NTT、QIA、Mitsubishi HC Capital Realty和Salesforce Ventures。股权与债务不能都解释为估值认可。[48]

**团队情况。** 联合创始人为Ross Diankov、Issei Takino，全球员工超过500人。东京Robot Center拥有数十台多品牌生产级机械臂及AGV。团队优势在感知、运动规划、控制和现场服务的贯通，而非单一模型规模。[49]

**本节判断。** 仓储工业路线的近期胜负，更取决于异常处理、系统集成和跨站点复制；新模型有价值，但必须缩短部署周期或改善产出。

本节参考文献：
[9] Mujin技术架构 <https://mujin-europe.com/technology> 摘录：“Learn about the platform powering today's most advanced automation applications Learn about the platform powering today's most advanced automation applications Learn about the platform powering today's most advanced automation applications MujinOS: The Intelligence Behind Every Robot MujinOS: The Intelligence Behind Every Robot A universal robotics platform that enables robots to perceive, plan, and act autonomously through integrated perception, motion…”
[48] Mujin业务与扩展 <https://mujin-corp.com/resources/news/seriesd-announcement-advancing-industrial-automation-intelligent-robotics> 摘录：“Learn more about MujinOS Learn about the platform powering today's most advanced automation applications Mujin Raises US$ 233 Million to Accelerate Global Growth and Drive the Future of Intelligent Automation Mujin Raises US$ 233 Million to Accelerate Global Growth and Drive the Future of Intelligent Automation Accelerate the advancement of MujinOS as the industry’s preferred intelligent robotics platform by productizing core technologies TOKYO & ATLANT…”
[49] Mujin团队与设施 <https://gembawalk.mujin.co.jp/about-mujin/overview> 摘录：“Company Overview is a pioneer in Physical AI and intelligent industrial robotics, developing MujinOS to enable autonomous perception, motion planning, and fleet execution. Key Highlights & Operational Metrics Global Footprint 500+ employees worldwide across headquarters in Tokyo and regional offices in Atlanta (USA), Eindhoven (Netherlands), and Guangzhou (China). Capital & Growth Momentum Backed by ¥36.4 Billion ($240M+) in Series D funding led by NTT…”

## 四足、轮腿与特种：地形通行之后，竞争转向巡检闭环

本节参考文献：
[9] Mujin技术架构 <https://mujin-europe.com/technology> 摘录：“Learn about the platform powering today…”
[48] Mujin业务与扩展 <https://mujin-corp.com/resources/news/seriesd-announcement-advancing-industrial-automation-intelligent-robotics> 摘录：“Learn more about MujinOS Learn about th…”
[49] Mujin团队与设施 <https://gembawalk.mujin.co.jp/about-mujin/overview> 摘录：“Company Overview is a pioneer in Physic…”

### 高端集成、低价平台与行业方案如何比较

| 公司与主要地区 | 技术及产品 | 产品商业进度 | 资本路径 | 团队与定位 |
|---|---|---|---|---|
| Boston Dynamics，美国 | Spot、可配置载荷与SDK | 2020年商业销售 | Hyundai产业支持 | 动态机器人及企业软件 |
| ANYbotics，瑞士苏黎世 | ANYmal、RL运动、边缘AI | 每月分析12万余次巡检 | 新投资6,000万美元节点 | ETH分拆、工业巡检 |
| 宇树，中国杭州 | Go2/B系列、低价执行器 | 报告期四足累计超过3万台 | IPO及经营资金 | 本体制造、开发者生态 |
| 云深处，中国杭州 | X30、轮足M20 | 电力巡检超过300台 | Pre-C、C轮及IPO计划 | 浙江大学控制团队 |
| Ghost Robotics | Vision 60、四足特种条目 | 按特种任务平台归类 | 公司法人及交易口径 | 特种载体目录位置 |

**比较基础。** 四足产品与应用资料来自四足市场调查[11]、ANYbotics官网[5]、宇树招股书[42]及云深处经营报道[50]。Ghost Robotics在本文承担特种路线边界说明。

**运动只是第一层。** 四足控制通常把关节位置、IMU和动作历史构成状态，策略输出位置或扭矩命令。然后再叠加定位、路线执行、专业传感和回坞。运动策略、总线和传感器必须严格同步，控制时序偏差也可能导致策略失效。[51]

本节参考文献：
[11] 四足市场调查 <https://www.goedelmachines.com/blog/quadruped-market-survey> 摘录：“Reporting on DEEP Robotics’ IPO application, accepted in May 2026, gives annual revenue of approximately RMB 50 million in 2023, RMB 103 million in 2024, and RMB 337 million in 2025. These figures describe the company’s growth rather than th…”
[5] 运营规模 <https://www.anybotics.com/> 摘录：“Title: ANYbotics Autonomous Legged Robots for Industrial Inspection Markdown Content: Autonomous robotic inspection solutions Our ANYmal robotic solutions automate industrial inspections. They provide operator insights that increase plant up…”
[42] 团队与人才规划 <https://static.sse.com.cn/stock/disclosure/announcement/c/202603/002178_20260320_QY8F.pdf> 摘录：“1 王兴兴 69.9592 69.9592 26.9673% 2 上海宇翼 17.1432 16.1768 6.6082% 3 汉海信息 20.7538 20.7538 8.0000% 4 宁波红杉 17.9408 17.9408 6.9157% 5 Astrend IV 12.7825 12.7825 4.9273% 6 金石成长 11.9954 11.9954 4.6239% 7 经纬壹号 11.6317 11.6317 4.4837% 8 君万弘毅 11.4632 11.…”
[50] 产品扩展时间线 <https://www.21jingji.com/article/20260530/ef49a0aa425d14230b0c015aaa31178e.html> 摘录：“5月中旬，他掌舵的杭州云深处科技，在科创板IPO申请获受理，计划募资25亿元，保荐机构为中信建投。 这是继宇树科技之后，又一家向A股发起冲击的 杭州六小龙 企业。 远上寒山石径斜，白云深处有人家。 云深处的名字透出一股不张扬的气质，其招股书披露的数字却相当亮眼。 2023年至2025年，云深处的营收从5011万元飙至3.37亿元，两年增长近7倍； 净利润从亏损2585万元，转为盈利2868万元，经营活动现金流净额转正。 根据沙利文数据，2025年公司在四足机器人行业应用领域收入…”
[51] 四足控制回路分析 <https://newsletter.semianalysis.com/p/quadruped-state-of-the-market-unitree> 摘录：“Quadrupeds are the most advanced general-purpose robots today. While they don’t grab as many headlines as their Humanoid counterparts, their Level 2 Autonomy coming online opens up a plethora of new market opportunities previously unavailabl…”

### Boston Dynamics Spot：高端本体、载荷和软件集成

**技术与产品。** Spot于2020年6月开放销售，此前早期采用者项目超过150台。它可搭载热成像、声学、气体检测及扫描设备，并提供SDK、客户端库和API。产品价值是可通行的传感平台，而非只有四条腿的裸机。[11]

**商业化进度。** 应用覆盖建筑、电力、核设施、工厂和研究，案例包括Pomerleau、Hensel Phelps、Aker BP。Boston Dynamics还以Orbit组织企业级机群管理。客户支付的是机器人、载荷、软件、部署、培训和维护组成的系统。[11]

**资金与团队。** Spot与Atlas共享Boston Dynamics的集团支持和机器人组织积累。与人形产品相比，Spot的对外销售、SDK和现场服务经验更成熟。其下一阶段竞争点，是让采集结果更深地进入客户设备维护流程。

本节参考文献：
[11] 四足市场调查 <https://www.goedelmachines.com/blog/quadruped-market-survey> 摘录：“This is Part 3 of our Physical AI series. Read the other articles: Part 1: Quadruped control architecture · Part 2: Quadruped mechanics. Quadrupeds are being used for industrial inspection, research, security, and work in places that are difficult or hazardous for people to reach. The robots look similar, but their customers and business models differ considerably. A small platform bought by a university lab is a different product from a robot supplied with inspection sensors, site integration, and a maintenance contract. This…”

### ANYbotics：从机器人巡检走向巡检数据系统

**技术路径。** ANYmal以强化学习驱动四足运动，高端传感器、边缘计算和机载AI承担定位、数据解释及异常检测。支持无互联网任务、路径优化、备选路径、连续采集与自动回坞，适合多楼层工业设施。[52]

**产品与商业。** 2017年首次销售，2018年已有海上部署。官网披露每月分析超过12万次巡检，监测1,000余项工业资产；客户标识包括Siemens Energy、GE Vernova、Equinor、SLB、Yokogawa等。[11][5]

**软件形成黏性。** 2025年2月推出Data Navigator，组织和分析巡检记录。客户一旦把数据与巡检例程纳入维护系统，切换厂商就不只是更换机器人。这是硬件销售之外更可持续的价值来源。[11]

**融资与团队。** Greater Zurich Area报道新投资6,000万美元，外部总融资超过1.3亿美元，Qualcomm Ventures和Supernovainvest共同领投，TDK Ventures参与。公司2016年从ETH Zurich分拆，联合创始人兼CEO为Péter Fankhauser博士。[53]

本节参考文献：
[52] ANYmal能力 <https://www.anybotics.com/robotics/robot-capabilities/> 摘录：“Title: Robot capabilities Markdown Content: ANYmal inspection solution capabilities Safety, mobility and autonomy make ANYmal the world's most capable end-to-end robotic i…”
[11] 四足市场调查 <https://www.goedelmachines.com/blog/quadruped-market-survey> 摘录：“This is Part 3 of our Physical AI series. Read the other articles: Part 1: Quadruped control architecture · Part 2: Quadruped mechanics. Quadrupeds are being used for indu…”
[5] 运营规模 <https://www.anybotics.com/> 摘录：“Title: ANYbotics Autonomous Legged Robots for Industrial Inspection Markdown Content: Autonomous robotic inspection solutions Our ANYmal robotic solutions automate industr…”
[53] 融资与科研背景 <https://www.greaterzuricharea.com/zh-hans/news/anybotics-zairongzi-6000-wanmeiyuankuozhangmeiguoshichang> 摘录：“根据一份新闻稿，ANYbotics 已获得 6000 万美元的新投资。 至此，这家 2016 年从瑞士苏黎世联邦理工学院分拆而来的公司，其外部总融资额已超过 1.3 亿美元。 这家由人工智能（AI）驱动的四足检测机器人制造商现在将把注意力转向为其全球扩展和美国扩张注入额外动力，并促进其全球团队的发展。 新一轮融资由位于美国加利福尼亚州圣地亚…”

### 宇树四足：低价与开放生态扩大硬件覆盖

**执行器路线。** SemiAnalysis将宇树四足归为准直接驱动QDD，执行器通常采用低于10∶1的减速比。低摩擦和反驱性有利于地形柔顺，也能压低成本；耐久性、间隙及重型平台稳定性则需要在长期任务中判断。[51]

**产品商业。** Go2系列起价约1,600美元，Go2 Pro约2,800美元。开发权限随型号不同，EDU与消费版并非同一软件产品包。2022年至2025年9月报告期四足销量累计超过3万台，单位成本从2022年2.23万元降至2025年前三季度1.21万元。[11][39]

**生态路线含义。** 低价本体让高校、软件商和集成商更容易获得机器，扩大算法与应用生态。与ANYbotics自建巡检闭环相比，宇树把更多行业实现留给合作伙伴。其融资和创始团队与前述人形业务共用公司口径，不重复计算。

本节参考文献：
[51] 四足控制回路分析 <https://newsletter.semianalysis.com/p/quadruped-state-of-the-market-unitree> 摘录：“Quadrupeds are the most advanced general-purpose robots today. While they don’t grab as many headlines as their Humanoid counterparts, their Level 2 Autonomy coming o…”
[11] 四足市场调查 <https://www.goedelmachines.com/blog/quadruped-market-survey> 摘录：“This is Part 3 of our Physical AI series. Read the other articles: Part 1: Quadruped control architecture · Part 2: Quadruped mechanics. Quadrupeds are being used for…”
[39] 产品销售时间线 <https://www.eeo.com.cn/2026/0320/813654.shtml> 摘录：“其招股书列出了一长串运动性能纪录：2024年全球首次全尺寸电驱人形机器人原地后空翻，2025年人形机器人奔跑速度超过5米/秒刷新世界纪录，首届世界机器人运动会上拿了4块金牌、11枚奖牌。 2026年春晚，25台机器人完成了集群武术表演《武BOT》，刷新了连续花式翻桌跑酷、弹射空翻等多项全球纪录。 在 大脑 层面，问询函回复内容披露…”

### 云深处DEEP Robotics：电力场景先行，再扩展形态

**技术与产品。** X30面向电力巡检、隧道和应急响应。产品资料列含电池56千克、IP67、工作温度－20至55℃、最高45度坡度、至少20厘米越障、2.5—4小时续航及换电。2025年4月又推出轮足M20，10月发布IP66人形DR02。[11][50]

**商业化进度。** 截至2026年5月报道，电力巡检累计销售超过300台，进入国家电网、南方电网下属100余个变电站，产品销往45个国家或地区。行业调查另估公司约600台、覆盖40余国。新加坡SP Group以SPock执行电力隧道巡检，供应商识别其平台为X30。[50][11]

**经营与融资。** 公司收入从2023年5,011万元增至2025年3.37亿元，2025年净利润2,868万元。2025年7月Pre-C轮近5亿元，12月C轮超过5亿元，随后有数亿元Pre-IPO轮。2026年5月IPO申请获受理，拟募资25.03亿元，其中11.69亿元用于具身算法和模型。[50]

**团队情况。** 朱秋国、李超于2017年创办公司，来自浙江大学实验室。朱秋国为控制科学与工程博士，并有浙大任职经历。这解释了其从运动控制和电力概念验证起步，再延伸到轮足与人形的路线。[50]

**特种边界位置。** Ghost Robotics的Vision 60列入四足特种路线。此类产品的决定性比较轴是任务授权、自主程度、载荷、通信和现场安全，而不是家庭操作能力。特种采购与普通消费或工业巡检，也采用不同的客户、产品包和交易口径。

**本节判断。** 四足商业化的核心不是跑得最快，而是能否独立完成巡检、回传可用数据，并以可接受的维护成本长期工作。

本节参考文献：
[11] 四足市场调查 <https://www.goedelmachines.com/blog/quadruped-market-survey> 摘录：“Reporting on DEEP Robotics’ IPO application, accepted in May 2026, gives annual revenue of approximately RMB 50 million in 2023, RMB 103 million in 2024, and RMB 337 million in 2025. These figures describe the company’s growth rather than the size of the overall quadruped market. 36Kr’s filing coverage Industrial specifications The manufacturer’s X30 page lists a weight of 56 kg including the battery, IP67 protection, an operating range of −20°C to 55°C, slope capability up to 45°, and obs…”
[50] 产品扩展时间线 <https://www.21jingji.com/article/20260530/ef49a0aa425d14230b0c015aaa31178e.html> 摘录：“创业九年，朱秋国想带着机器狗去敲钟。 5月中旬，他掌舵的杭州云深处科技，在科创板IPO申请获受理，计划募资25亿元，保荐机构为中信建投。 这是继宇树科技之后，又一家向A股发起冲击的 杭州六小龙 企业。 远上寒山石径斜，白云深处有人家。 云深处的名字透出一股不张扬的气质，其招股书披露的数字却相当亮眼。 2023年至2025年，云深处的营收从5011万元飙至3.37亿元，两年增长近7倍； 净利润从亏损2585万元，转为盈利2868万元，经营活动现金流净额转正。 根据沙利文数据，2025年公司在四足机器人行业应用领域收入排名全球第一，四足机器人收入排名全球第二，仅次于宇树科技。 从创业到冲刺IPO，朱秋国团队熬了9年。 朱秋国1982年出生于浙江海宁，从小就对机械抱有浓厚兴趣。 他是工学博士，毕业于浙江大学控制科学与工程专业，后留校就职于浙江大学控制科学与工程学院、国家卓越工程师学院。 2010年前后，波士顿动力发布的四足机器人视频在学术圈流传开来。 朱秋国反复观看，一个问题在心头萦绕不去：中国什么时候能造出自己的高性能机器人？ 2017年秋天，朱秋国与浙大实验室的同事李超联手创…”

## 家庭与商用服务：专用规模化，通用操作仍在爬坡

本节参考文献：
[11] 四足市场调查 <https://www.goedelmachines.com/blog/quadruped-market-survey> 摘录：“This is Part 3 of our Physical AI serie…”
[50] 产品扩展时间线 <https://www.21jingji.com/article/20260530/ef49a0aa425d14230b0c015aaa31178e.html> 摘录：“彼时，全球四足及轮足机器人尚未进入规模化放量阶段，下游应用集中在科研教育、军事…”

### 四家代表公司的统一比较

| 公司与主要地区 | 技术路径 | 产品阶段与商业证据 | 资金路径 | 团队依据 |
|---|---|---|---|---|
| 普渡，深圳 | 导航、操作、交互，一脑多形 | 累计出货超过12万台 | 2026年融资近10亿元 | 深圳、成都、香港研发 |
| 擎朗，中国 | 清洁配送向通用人形延伸 | 全球部署超过10万台 | 专用产品与通用化业务口径 | 服务产品及场景协同 |
| 科沃斯，苏州 | 家庭导航、端侧AI、执行器整合 | 2025年品牌服务机器人440万台 | 上市、可转债及经营现金流 | 总员工10,730人 |
| 石头，中国及沪深研发 | 清洁底盘增加AI机械臂 | Saros Z70已上市 | 消费机器人企业资源 | AI专家扩招、双地研发 |

本节参考文献：
[11] 四足市场调查 <https://www.goedelmachines.com/blog/quadruped-market-survey> 摘录：“Reporting on its March 2026 IPO filing describes more than 30,000 quadrupeds sold between 2022 and September 2025. That is a cumulative company figure, not a total for the global market. The Shanghai Stock Exchange subsequently announced…”
[50] 产品扩展时间线 <https://www.21jingji.com/article/20260530/ef49a0aa425d14230b0c015aaa31178e.html> 摘录：“2025年10月，云深处发布第二代人形机器人DR02，这是业内少数具备IP66防护等级的产品，定位于全天候作业领域，尚处于商业化起步阶段。 由此，公司形成覆盖四足及轮足机器人、人形机器人的多形态产品矩阵，应用于电力巡检、应急消防、警务安防、物流运输等领域。 在全球市场，朱秋国团队也实现突破，产品销往美国、新加坡、德国、土耳其、韩国、日本等45个国家或地区，境外收入高速增长。 云深处一路成长过程中，始终有着耐心资本的支持。 2018年7月，云深处完成天使轮融资，银杏谷资本…”

### 普渡机器人：从配送、清洁走向“一脑多形”

**技术路径。** 普渡全球总部深圳，研发在深圳、成都和香港协同。自研导航、多机调度、群控、运动控制器和一体化关节模组，以具身导航、操作、交互三类能力支撑专用、类人形及人形产品。[54]

**产品与商业。** 截至2026年4月23日披露，累计出货超过12万台，服务超过4万家客户，覆盖80余个国家和地区、1,000余座城市。工业配送机器人上市一年多出货超过4,000台。客户包括家乐福、沃尔玛、Edeka等连锁企业。[6]

**收入结构已变化。** 2025年营收同比增长超过100%，商用清洁业务营收占比超过70%，EBITDA接近转正。说明普渡已从餐饮配送的单一印象，转向多场景商用设备平台。对其新型人形，仍应单看操作能力和客户采用，而不是分摊整体出货。[6]

**价格与商业机制。** 行业报告列“欢乐送”售价3万—5万元，日均配送300—400盘，回报周期8—12个月。其价值来自减少高频往返，而非接管服务员所有工作。商业模式以设备和方案销售为基础，再由渠道、售后与场景集成支持扩张。[43]

**融资与团队。** 2026年4月新融资近10亿元，估值突破100亿元，龙岗金控、亚投资本联合领投，北汽产投、蓝思科技等参与。普华资本于2022年参与C轮。组织优势体现在导航、群控、执行机构和海外产品服务协同，下一阶段是清洁规模化与新形态研发共同推进。[6]

本节参考文献：
[54] 普渡技术架构 <https://www.pudurobotics.com/en/company> 摘录：“Empowering easier work and better life through Al and robotics Pudu Robotics, a global leader in the commercial service robotics sector, is dedicated to empowering easier work and better lives through AI and robotics, with a vision of building a global intelligent rob…”
[6] 普渡经营规模 <http://www.puhuacapital.com/mobile/index.php/news/info/297> 摘录：“近日，全球商用服务机器人领军企业深圳市普渡科技有限公司（以下简称：普渡机器人）完成近10亿元新一轮融资，由龙岗金控、亚投资本联合领投，北汽产投、蓝思科技、弘晖基金、珠三角与长三角等多地政府引导基金及知名硬科技投资机构共同参与。 普华资本于2022年投资普渡机器人C轮融资。 本轮融资后，公司估值突破百亿元人民币，彰显资本市场对普渡产品技术壁垒、商业落地能力与全球化领导力的高度认可。 融资资金将重点投入具身智能技术研发、产品矩阵扩充、全球市场纵深拓展、规模化产能建设与供应链升级，全面巩固公司在全球商用服务机器人赛道的领先优势，为登陆资…”
[43] GO-1路线 <https://pdf.dfcfw.com/pdf/H3_AP202605071822028328_1.pdf?1778171901000.pdf> 摘录：“2026 年智能机器人行业深度分析报告 客户名称： 公司 中投产业研究院版权所有 www.ocn.com.cn 1 2026 年智能机器人行业深度分析报告 本研究报告由中投产业研究院制作出品，产品版权由本公司唯一拥有。 目前本公司所有研究报告均没有委托其他任何第三方代理销售，即如果您 收到的报告不是从本公司直接购买，或本产品不是由本公司向您直接发送， 则一定是盗版者非法向您或贵公司销售，敬请您拨打举报电话0755- 82571566，我公司将以特定的方式向您表示感谢。 本产品版权受《中华人民共和国著作权法》保护，是由本公司直接向客…”

### 擎朗KEENON：先按服务角色部署，再扩展通用能力

**技术路径。** 擎朗产品覆盖DINERBOT配送、KLEENBOT清洁及XMAN-R1、XMAN-F1等形态。专用产品承担高频任务，人形承担操作和交互，形成“角色化部署—通用化”的路线。[55]

**产品进度。** 2026年WAIC展示XMAN-R1拿杯、制咖啡、递送饮料，以及酒店洗衣、零售拣选等任务。公司称这些人形演示自主运行、没有远程操作。产品阶段上，专用服务机属于规模交付，人形部分属于现场演示和角色化验证。[56]

**商业化进度。** 公司援引IDC称2025年商用服务机器人出货排名第一，全球累计部署超过10万台，商用清洁机器人出货同比增长超过800%。这证明清洁、配送体系的市场覆盖，也为新操作产品提供客户入口。[56]

**资本与团队。** 擎朗应按商用机器人企业整体评价资本和组织，而不是把XMAN系列单独视为一家模型初创公司。其技术组织价值在于导航、清洁执行、配送调度和人形操作能否共同服务酒店、餐饮、医疗等流程。进一步的通用化收益，要由这些客户的持续使用和复购决定。

本节参考文献：
[55] 产品与场景目录 <https://www.keenon.com/zh-cn/news?page=> 摘录：“专业四合一地面清洁机器人 在几分钟内了解您的机器人投资回报率 提升酒店服务：使用服务机器人提升服务和客人体验 转变餐饮体验：利用服务机器人提高效率和服务卓越性 动态促销、重物搬运、一尘不染的清洁，全自动化 医疗数字化智能医院解决方案 赋予护理人员权力，提升老年生活水平 global@keenon.com”
[56] WAIC产品披露 <https://www.keenon.com/zh-cn/news/gcsrslkphtwaw2> 摘录：“KEENON Robotics将其全球商业领导力带到2026年世界人工智能大会（WAIC）上，这表明人形机器人已经准备好超越舞台表演，承担真正的服务工作。 根据IDC的数据，KEENON在2025年全球商用服务机器人出货量排名第一，连续多年保持全球领先地位。 该公司还继续引领全球送货机器人市场，其商用清洁机器人的出货量同比增长超过800%。 2025年，全球商用服务机器人出货量超过15万台，突显出该行业正加速向大规模部署转变。 在H3-C201展位上，KEENON的 体现服务社区 将这些数字转化为四种商业场景的行动：咖啡服务、酒店洗衣、甜品店和零售履行。 在咖啡亭，XMAN-R1充当机器人咖啡师，独立拿起杯子，准备咖啡，并将饮料…”

### 科沃斯：制造、渠道和经营现金流支撑家庭新品

**技术路径。** 科沃斯以DEEBOT扫地、WINBOT擦窗、GOAT割草形成家庭机器人底座。技术包括建图、移动导航、三维避障与环境语义识别。向上游延伸的电机、电池、传动与灵巧手布局，则服务新型执行能力。[57]

**新品与模型。** 2026年一季度发布家庭管家“八界”和陪伴机器人“毛团儿”。八界结合物体识别、记忆、自然语言交互和拟态执行，目标是收纳、归位及桌面清洁；毛团儿则走仿生、多模态感知和情感交互路线。新品按“发布与能力展示”理解。[58]

**商业化进度。** 2025年科沃斯品牌服务机器人出货440万台，销售收入105.35亿元。年报产品分类表另列服务机器人销量4,476,901台、收入106.80亿元，属于另一统计分类。品牌经营与产品分类分别保留，两者均不对应八界单品规模。[57]

**融资与资金。** 公司2018年在上交所上市，2021年11月30日发行10.40亿元可转债，净募集10.2964亿元。2025年集团经营活动现金流净额33.87亿元，研发费用9.8052亿元。与依靠连续私募的初创公司相比，它拥有成熟消费业务支持长期研发的能力。[57]

**团队情况。** 创始人、董事长钱东奇毕业于南京大学哲学系；David Cheng Qian任服务机器人CEO。研发负责人徐伟强为同济大学硕士，有诺基亚研发管理经历。2025年末总员工10,730人，研发1,704人，其中博士6人、硕士408人，显示消费制造组织与AI研发并行。[57]

**路线的关键转变。** 科沃斯已证明大规模制造和全球销售，下一道门槛是把平面清洁经验转成接触丰富的立体操作。长期记忆能解释偏好，却不能代替抓取安全、手臂可靠性和售后成本控制。

本节参考文献：
[57] 科沃斯2025年报 <http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESH_STOCK/2026/2026-4/2026-04-25/12191589.PDF> 摘录：“保险合同准备金 长期借款 应付债券 七、 46 1,064,561,673.18 1,031,523,664.89 其中：优先股 永续债 租赁负债 七、 47 3,464,741.57 5,370,608.22 长期应付款 长期应付职工薪酬 预计负债 递延收益 七、 51 37,142,193.27 35,139,545.22 递延所得税负债 七、 29 96,917,885.71 55,441,619.35 其他非流动负债 非流动负债合计 1,202,086,493.73 1,127,475,437.68 负债合计 8,388,924,825.99 7,829,324,218.96 所有者权益（或股东权益）： 实收资本（或股本） 七、 53 578,921,306.00 575,295,227.00 其他权益工具 七、 54 117,913,955.97 117,922,236.11 其中：优先股 永续债 资本公积 七、 55 1,747,457,403.25 1,482,498,326.95 减：库存股 七、 56 165,509,720.71 187,966,757.46 其他综合收益…”
[58] 新品发布时间 <https://www.xinhuanet.com/finance/20260427/78fa95b18a06411e88cd766a8fce4a17/c.html> 摘录：“4月24日，科沃斯集团（603486.SH）发布2025年度报告及2026年一季报。 2025年公司实现营业收入190.40亿元，同比增长15.10%； 归属于上市公司股东的净利润17.58亿元，同比大幅增长118.13%，扣非归属于上市公司股东的净利润16.20亿元，同比大幅增长126.14%。 经营活动产生的现金流量净额达33.87亿元，同比大增297.39%。 2026年一季度增长势头进一步提速，营收达49.02亿元，同比增长27.06%，一季度扣非后归母净利润为3.97亿元，同比、环比均实现明显增长。 科沃斯与添可两大品牌在各自赛道上不仅保持传统优势产品地位稳固，新品类也实现全面开花。 科沃斯品牌持续深耕扫地机器人核心赛道，奥维云网数据显示，科沃斯已连续11年蝉联中国扫地机器人市场规模第一，2025年线上销量份额达30.4%，同比增长6.6个百分点。 添可品牌围绕 智能生活电器 定位，不断突破场景边界。 据欧睿国际按全球零售渠道数据认证，添可已连续四年（2022—2025年）摘得洗地机销量全球第一，同时实现连续六年全国销额销量第一。 两大自有品牌合计贡献营收186.52亿元，占公司总收…”

### 石头科技：在成熟清洁产品上增加机械臂

**技术路径。** Saros Z70把AI机械臂加入清洁底盘，路线更渐进：先移动小物体、改善清洁，再扩大操作范围。公司总裁Quan Gang认为，机械臂能力和降本的主要挑战在算法与数据，而不是单纯硬件。[59]

**产品与商业。** Z70于2025年CES期间推出并开售。2025年8月Amazon售价约2,600美元，具体计算为原定1,899美元加700美元，即2,599美元。CNBC同时转述初期评测更推荐约1,600美元的Saros 10R，说明增加操作功能后，还要证明体验增益值得价格溢价。[59]

**资本与团队。** 对该产品，应以石头消费机器人业务资源和AI组织投入评价，而不是另立机械臂专项估值。2025年8月公司称当年已招聘近100名AI专家，目标全年合计近200名；上海设AI实验室，深圳设研究院。扩招数字是当时的新增与计划，不是2026年总团队人数。[59]

**路线的实际意义。** 与一步进入双足家庭管家相比，“清洁底盘+机械臂”保留原有导航、渠道和基站价值，试错成本相对集中。但如果操作功能增加价格、故障与维护，却不能稳定减少用户劳动，成熟产品反而可能更有竞争力。

**本节判断。** 专用服务机器人是具身产业最扎实的规模基础；向通用化扩展能否成功，要由新增操作能力带来的净用户价值决定。

本节参考文献：
[59] CNBC石头专访 <https://www.cnbc.com/2025/08/22/chinas-robot-vacuum-roborock-plans-mass-market-cleaners-with-ai-arms.html> 摘录：“BEIJING — Household robots for cleaning are about to quickly become an affordable reality. At least that's what Quan Gang, president of Beijing-based robot vacuum cleaner company Roborock, has in mind as he strategizes for the next five years. The company ranks first among smart vacuums by global market share, according to IDC Research. Last week, it reported a nearly 79% revenue surge in the first half of this year. About half of sales came from outside China. In an exclusive interview with CNBC on Wednesday, Quan predicted that human-like robots will become part of many households by 2030, thanks largely to advances in generative artificial intelligence. And before then, he expects, Roborock can make its latest, high-end cleaner with an AI-powered robotic arm so cheap that t…”

## 自动驾驶与无人机：相邻Physical AI，不混入机器人操作排名

本节参考文献：
[59] CNBC石头专访 <https://www.cnbc.com/2025/08/22/chinas-robot-vacuum-roborock-plans-mass-market-cleaners-with-ai-arms.html> 摘录：“BEIJING — Household robots for cleaning ar…”

### Waymo与Tesla提供两种移动智能参照

| 比较对象 | 感知与模型路线 | 产品商业进度 | 资本与组织 | 对机器人可借鉴部分 |
|---|---|---|---|---|
| Waymo | 多传感器、模块化Transformer | 地理围栏Robotaxi收费运营 | Alphabet体系、车队运营组织 | 仿真、安全、区域扩张 |
| Tesla驾驶业务 | 摄像头、端到端视频Transformer | Robotaxi有限区域推进 | 整车、AI、制造体系 | 低成本感知、大规模数据 |
| DJI、Skydio | 无人机邻接路线 | 按飞行任务与运营条件判断 | 公司及产品法人口径 | 定位、避障、飞控与远程运营 |

**Waymo技术路径。** Waymo使用摄像头、LiDAR、雷达和麦克风，在限定运行设计域内提供服务。2026年2月推出基于Genie 3的World Model，生成摄像头和LiDAR仿真，用于长尾场景与反事实测试。公司称真实全自动驾驶里程近2亿英里。[60]

**Waymo商业与团队。** 2023年8月取得加州收费Robotaxi许可，2025年通过Uber进入奥斯汀、亚特兰大。2025年服务1,500万次，截至2026年1月累计超过2,000万次；9月初周报列服务覆盖14座城市。团队起点是Sebastian Thrun参与建立的Google无人车项目，后来形成算法、车队与合规组织。[7][61][62]

**Tesla路线对照。** Contrary Research在2025年比较中列，Tesla使用8个摄像头和端到端视频Transformer。其估算传感器成本约400美元/车，Waymo第五代套件约12,700美元，均为相应时期成本估算。纯视觉以低硬件成本和数据规模换扩展性，多传感器则提供直接深度及互补观测。[63]

**运营仍有阶段性。** 2026年9月4日周报记录，Tesla Cybercab在奥斯汀有限区域提供公共乘坐，当地自动驾驶车队约420辆，其中Cybercab约45辆。这是公共运营推进信号，评价轴应是收费、利用率、远程协助和安全，而不是车辆数量本身。[61]

**无人机的边界。** DJI和Skydio纳入相邻路线，是因为自主飞行同样需要感知、规划、控制和反馈。它们与地面机器人共享定位、避障、端侧计算及运营工具，但飞行能力不能直接证明抓取或家庭整理成熟。空域、通信、气候和航空管理，还构成不同的商业化约束。[62]

**本节判断。** 自动驾驶和无人机最值得借鉴的是移动导航、仿真、安全与运营；开放式接触操作仍需机器人自身的数据和验证。

本节参考文献：
[60] Waymo世界模型 <https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation> 摘录：“The Waymo World Model: A New Frontier For Autonomous Driving Simulation The Waymo Driver has traveled nearly 200 million fully autonomous miles, becoming a vital part of the urban fabric in major U.S. cities and improving road safety. What riders and local communities don’t see is our Driver navig…”
[7] 运营规模 <https://www.stcn.com/article/detail/3628362.html> 摘录：“2月2日，Alphabet旗下自动驾驶企业Waymo正式宣布完成新一轮160亿美元（约合人民币1112亿元）融资。 此轮融资将重点用于扩大无人驾驶出租车（Robotaxi）车队规模，并计划于2026年将服务拓展至包括伦敦、东京在内的十余个国际新城市，标志着这家自动驾驶领域头部企业正式开启全球化商业化进程。 融资阵容豪华，估值达1260亿美元 据Waymo官方博客披露，此次融资由Dragoneer Investment Group、DST Global与Sequoia Capital（红杉资本）联合领投，同时吸引了众多全球知名投资机构参与。 其中，Andreessen Horowitz、Mu…”
[61] 2026年9月扩张 <https://acisresearch.com/research/physical-ai-robotics-weekly-2026-09-04> 摘录：“ACIS · PHYSICAL AI & ROBOTICS WEEKLY · ISSUE 003 · 2026.09.04 Cybercab真的上线了， 但Tesla还没有证明Robotaxi经济学 Physical AI、机器人与自动驾驶研究周报｜第003期 Robotaxi正在跨过 公开无人载客 门槛，但公开载客、收费运营与可盈利规模仍是三件不同的事。 Waymo继续证明城市复制能力； 人形机器人本周没有出现足以改变商业化判断的新证据。 EXECUTIVE SUMMARY 公共无人部署成立，不等于规模化付费成立 Tesla Cybercab从生产与测试跨入真实乘客运营，是产品成熟度的重…”
[62] 项目团队历史 <https://www.tmtpost.com/7779567.html> 摘录：“在摩根士丹利第24届亚太峰会上，自动驾驶领域的 教父级 人物Sebastian Thrun与知名分析师Adam Jonas进行了一场深度对话，内容涵盖自动驾驶技术路线、行业阶段判断、机器人赛道分化、Waymo早期秘历等多个维度。 作为谷歌无人车项目（Waymo前身）缔造者、斯坦福人工智能实验室前主任，Thrun的见解无疑为当前自动驾驶与机器人领域的发展提供了重要风向标。 自动驾驶技术路线之争：纯视觉方案的 成本革命 Thrun在对话中明确指出，自动驾驶领域当前最核心的技术分歧在于 纯视觉 与 多传感器融合 的路线博弈。 他特别强调，特斯拉在奥斯汀的纯视觉FSD实测将成为行业关键转折点。 如…”
[63] 传感器与模型比较 <https://research.contrary.com/report/tesla-waymo-and-the-great-sensor-debate> 摘录：“A few weeks ago, we unpacked the history and potential future of autonomous vehicles in our deep dive, The Trillion-Dollar Battle To Build a Robotaxi Empire. Now, the battle to become the leading robotaxi company is heating up. On June 22, 2025, Tesla launched its long-awaited robotaxi service wit…”

## 横向比较：哪些优势已经兑现，哪些仍是未来选择

本节参考文献：
[60] Waymo世界模型 <https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation> 摘录：“The Waymo World Model: A New Frontier F…”
[7] 运营规模 <https://www.stcn.com/article/detail/3628362.html> 摘录：“有分析认为，Waymo凭借技术积累与资本优势，仍是全球L4赛道的 领跑者 ，但…”
[61] 2026年9月扩张 <https://acisresearch.com/research/physical-ai-robotics-weekly-2026-09-04> 摘录：“其优势已经从单点驾驶能力扩展到新城验证、车队运营、公众导入、安全协作与标准化上…”
[62] 项目团队历史 <https://www.tmtpost.com/7779567.html> 摘录：“从经济学角度分析，纯视觉方案的最大优势在于成本。 目前高端激光雷达单价仍高达数…”
[63] 传感器与模型比较 <https://research.contrary.com/report/tesla-waymo-and-the-great-sensor-debate> 摘录：“A few weeks ago, we unpacked the histor…”

### 在统一维度下比较四条主路线

**近期排序是场景排序。** 若以持续部署和付费任务为标准，专用服务、仓储AMR及工业巡检领先。若以跨任务潜力看，人形和基础模型的上限更宽。两种判断不冲突，因为一个衡量当前产出，一个衡量未来适配空间。

| 路线 | 技术及产品成熟度 | 可靠性与安全重点 | 成本锚点 | 数据及扩展性 |
|---|---|---|---|---|
| 工业人形 | 试点、早期交付并存 | 平衡、接触、远程介入 | G1起价8.5万元 | 真机与仿真重，复制待深化 |
| 仓储工业 | AMR成熟，操作扩展 | 功能安全、异常恢复、吞吐 | Digit约25美元/小时 | 生产数据密集，软件可复用 |
| 四足巡检 | 工业部署成熟度较高 | 通行、回坞、网络与载荷 | Go2起价约1,600美元 | 行业数据与集成决定价值 |
| 家庭商服 | 专用量产，通用新品早期 | 人机接触、误操作、售后 | 配送机约3万—5万元 | 渠道广，操作数据仍需积累 |

**价格要对应交付物。** 表中锚点分别是售价、服务费和不同配置产品，不组成成本排名。[39][30][11][43]

**可靠性有不同层次。** 工业控制器的安全等级、机械硬件MTBF和AI任务成功率，不是同一个指标。Mujin的功能安全、Digit的急停系统、ANYmal的自主回坞，都有工程价值；但整套任务还要看异常发生时能否安全停止、恢复及继续生产。

**单位经济性要折算。** 以Digit报道的25美元/小时，对比美国仓储人工约30美元/小时，若机器人每收费小时创造的人类等效产出比例为q，则等效成本为25÷q。忽略其他费用，达到30美元以内需要q≥83.3%，计算为25÷30。[30]

**服务费不等于利润。** Nexi所述厂商文件列Digit v4物料成本约12.5万美元。仅用25美元/收费小时覆盖这项成本，就需约5,000收费小时，计算为125,000÷25；尚未计入维护、融资、计算和现场服务。RaaS降低客户采购门槛，也把利用率和残值风险留给厂商。[2]

本节参考文献：
[39] 产品销售时间线 <https://www.eeo.com.cn/2026/0320/813654.shtml> 摘录：“其招股书列出了一长串运动性能纪录：2024年全球首次全尺寸电驱人形机器人原地后空翻，2025年人形机器人奔跑速度超过5米/秒刷新世界纪录，首届世界机器人运动会上拿了4块金牌、11枚奖牌。 2026年春晚，25台机器人完成了集群武术表演《武BOT》，刷新了连续花式翻桌跑酷、弹射空翻等多项全球纪录。 在 大脑 层面，问询函回复内容披露了一个测试成绩：宇树的VLA模型UnifoLM-VLA-0在行业通用仿真测试基准LIBERO上拿了98.7分的平均分，在已公开测试结果…”
[30] 另一累计口径 <https://robotbelt.com/americas-humanoid-robot-race-six-players-three-paths/> 摘录：“The hands are the big upgrade: 22 degrees of freedom per hand, double Gen 2’s 11, with 25 actuators per forearm and 50 across both hands, using tendon-like drives that pull fingers from the forearm, mirroring human hand structure. Th…”
[11] 四足市场调查 <https://www.goedelmachines.com/blog/quadruped-market-survey> 摘录：“DEEP Robotics Jueying X30 Power infrastructure and industrial inspection Geography helps explain differences in manufacturing costs and customer access, but it does not divide the market neatly. Chinese manufacturers serve different…”
[43] GO-1路线 <https://pdf.dfcfw.com/pdf/H3_AP202605071822028328_1.pdf?1778171901000.pdf> 摘录：“微笑曲线，上游零部件利润最高（30- 价值分布 85%（减速器/电机/丝杠/传感器 行星滚柱丝杠、六维力传感器、RV 减 丝杠良率60% vs 海外85%+， 速器 传感器精度±2% vs ±0.5% 特斯拉/Figure/智元布局端到端， 技术路线 分层式架构为主，端到端大模型探索 2028 年或成高端标配 全球智能机器人2026 年2,430 亿美元 中国人形机器人2026 年90 亿元 →2035 年2 万亿美元 →2035 年1.35 万亿元 成本下降（…”
[2] 宝马部署证据 <https://nexi.fund/humanoid-robot-deployments-2026/> 摘录：“Unitree H2 Plus ◐ catalog listing, no order flow $7B IPO target Read the table vertically. The highest valuations sit on the least independent evidence. Tesla's implied standalone value of $150 billion or more rests on zero published…”

### 融资与团队：比较资源结构，不做混合金额榜

**资本路径分成四类。** 独立整机创业公司需要融资支持本体、产线和现场服务；模型公司重点投入数据与训练；上市机器人企业可以依靠配售、债券和经营现金流；大集团项目则复用母公司资源。直接把它们按“融资总额”排序，会混淆资金用途与经营成熟度。

| 资本与组织类型 | 代表公司 | 已披露资源锚点 | 主要用途 | 评价重点 |
|---|---|---|---|---|
| 高融资整机创业 | Figure、Apptronik、NEURA | 亿美元级单轮 | 本体、工厂、数据与服务 | 交付和现金消耗 |
| 模型创业 | PI、Skild、Covariant | 模型融资与授权 | 数据、训练、适配 | 付费集成和复用 |
| 上市机器人企业 | 优必选、宇树、科沃斯 | 配售、IPO、债券、经营 | 研发、供应链、扩产 | 收入质量和资本效率 |
| 集团内部平台 | Tesla、Amazon、DeepMind、Intrinsic | 母公司资源 | 工程平台与业务协同 | 项目投入和实际收益 |
| 工业软件及方案 | Mujin、ANYbotics、Dexterity | 股权、债务、产业资本 | 产品化、全球服务 | 跨站点复制和续约 |

**融资热度确实上升。** 新华网引IT桔子统计，截至2026年5月11日，中国具身智能融资218起、金额超过577亿元，超过70%的融资额流向B轮及以后。另一公开整理在1月1日至6月4日记录288起、金额超过460亿元，采用了不同的披露与估算规则，两组不是连续时间序列。[64][38]

**团队人数也有分母。** NEURA约1,400人、Mujin超过500人，属于总员工口径；优必选1,103人和科沃斯1,704人是研发人员。科沃斯年报另列集团总员工10,730人。总人数、研发人数和单一机器人项目人数，应分别用于组织与执行能力判断。[45][49][20][57]

**履历要对应路线。** CMU、Stanford、Berkeley团队擅长模型、视觉和机器人学习；ETH、OSU、UT Austin及浙大团队有运动、控制或本体积累。消费机器人企业则更擅长制造、渠道、质量和售后。跨过商业化门槛，通常需要这些能力组合，而不是某一类背景独占优势。

本节参考文献：
[64] 新华网融资统计 <https://www.news.cn/tech/20260513/358cfbcbd83f440a8a4eec65d9e75528/c.html> 摘录：“具身智能领域投资热度不减。 机构数据显示，截至5月11日，2026年国内具身智能领域投资总额已经超过2025年全年，单笔10亿元及以上融资超过10起。 投资热度之下，具身智能产业正经历一场从 讲故事 到 交答卷 的深刻转折。 多位业内人士对《经济参考报》记者表示，机构的关注重点正在转向企业落地实绩，复购率、连续运行时长等因素成为投资的 硬指标 。 最近一个月，多家企业宣布完成大额融资。 Vbot维他动力5月11日宣布完成Pre…”
[38] 2026年融资节点 <https://news.pedaily.cn/202606/565245.shtml> 摘录：“江浙沪合计117起（浙江45起、上海38起、江苏34起），这一区域更倾向于场景定义，融资企业大量集中在工业喷涂、家庭陪伴、清洁服务等垂直细分赛道。 比如智元旗下的清洁业务机器人智鼎（完成数亿 A 轮），以及理疗与家庭服务等垂直场景。 北京出大脑/本体，广东出零部件，江浙沪跑场景的格局在2026年上半年初步成型。 五、草根入局还有机会吗？ 要回答这个问题，得先看看早期融资的钱到底流向了谁。 2026年上半年，种子轮和天使轮共73…”
[45] NEURA产品体系 <https://www.humanoidsdaily.com/features/the-humanoids-of-europe> 摘录：“GENE.01 was shown as a concept at CES 2026 and unveiled as working, fully sensorised hardware on 20 July 2026, built in six months. Its distinguishing feature is a distributed tactile skin across the body, paired wi…”
[49] Mujin团队与设施 <https://gembawalk.mujin.co.jp/about-mujin/overview> 摘录：“Company Overview is a pioneer in Physical AI and intelligent industrial robotics, developing MujinOS to enable autonomous perception, motion planning, and fleet execution. Key Highlights & Operational Metrics Global…”
[20] 优必选数据披露 <https://www.iyiou.com/news/202608281139470> 摘录：“优必选2026年上半年营收12.7亿元，全尺寸人形产品收入增长1445% 8月28日， 人形机器人第一股 优必选（股份代码：9880.HK）发布2026年中期业绩报告：总营收12.7亿元，同比大幅增长104.2%； 人形机器人总销量16123台，同比大幅增长268.3%； 全尺寸具身智能人形机器人（非遥控非玩具，大脑芯片算力≧200T，身高160cm以上）收入5.9亿元，同比大幅增长1445.0%，已成为公司主要收入组成和核心…”
[57] 科沃斯2025年报 <http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESH_STOCK/2026/2026-4/2026-04-25/12191589.PDF> 摘录：“Published Time: Fri, 24 Apr 2026 16:20:39 GMT Number of Pages: 262 Markdown Content: 科沃斯机器人股份有限公司 2025 年年度报告 公司代码：603486 公司简称：科沃斯 转债代码：113633 转债简称：科沃转债 科沃斯机器人股份有限公司 2025 年年度报告 科沃斯机器人股份有限公司 2025 年年度报告 一、本公司董事会及董事、高级管…”

### 全球地域差异：北美模型、欧洲工业、中国制造正在交叉

| 地区 | 较突出的基础 | 代表性路径 | 商业化优势 | 下一阶段约束 |
|---|---|---|---|---|
| 北美 | 基础模型、芯片、软件与资本 | PI、Figure、NVIDIA、Amazon | 模型与企业客户结合 | 本体成本、交付与运营 |
| 欧洲 | 工业自动化、精密制造、汽车客户 | ANYbotics、NEURA、Hexagon、Mujin欧洲业务 | 集成、专业场景和服务 | 制造规模、成本和扩张 |
| 中国 | 供应链、本体制造、多样场景 | 宇树、优必选、云深处、普渡、科沃斯 | 价格、迭代、渠道与部署 | 通用操作、品牌和全球合规 |

**地区不是技术标签。** 北美也有物流专用系统，中国也有模型优先公司，欧洲也在扩张基础模型组织。华为产业报告提出的区域比较，更适合作为资源分布解释，而非判断单个公司能力的规则。[13]

**本节判断。** 当前竞争优势来自本体成本、真实任务数据、模型适配、安全和交付组织的组合；融资额和团队头衔只能说明资源，不能代替产品结果。

本节参考文献：
[13] 云边端协同架构 <https://www-file.huawei.com/dam/asset/view/physical-ai-cloud-edge-device-collaboration-architecture.pdf> 摘录：“Title: 物理智能云边端协同架构研究报告 Number of Pages: 60 Markdown Content: 物理智能云边端协同架构 研究报告 具身智能机器人是我国前瞻布局的新兴产业，已上升为国家重要战略方向，是打通数字空间与物理世界、发 展新质生产力的关键载体，事关我国人工智能与机器人产业的全局竞争实力。 当前具身智能/物理智能快速兴 起，技术从数字智能向真实物理世界延伸，但物理闭环实时性保障、多智能体群体协同、模型持续迭代、异 构系统互联互通等工程问题突出，产业迫切需要一套可落地的参考架构与深度的产业研判。 《物理智能云边端协同架构研究报告》立足物理智能产业发展现状，聚焦云边端协同这一核心技术范式，针 对物理智能 端侧实时闭环、边侧增强智能、云侧全局演进 的分层特征，系统阐释云-边-端协同架构的生 成逻辑，提出 三域协同·一网贯通 参考架构，区分不同场景下架构的适用条件与风险边界，既解析实时 控制、多机协同、虚实仿真训练等技术价值，也对产业链分工、差异化部署模式、服务化商业演进路径开展 系统研判。 报告为芯片、模型、机器人本体、系统集成等产业各方提供架构设计与商业落地的重要参照，对 具身智能机器人走向规模化商用有重要价值。 物理智能/具身智能是复杂技术、产品和应用的产业生态领域，跨计算、电子、通信、自动化、机械多个领 域，因此离不开产学研用各环节和各产业领域的深度协同。 期待本报告能够成为产业沟通的基础之一，推 动产业链在架构理念、技术路径、产品形态、生态建设上形成广泛共识，凝聚产…”

## 未来12—24个月：哪些信号会改变当前判断

本节参考文献：
[13] 云边端协同架构 <https://www-file.huawei.com/dam/asset/view/physical-ai-cloud-edge-device-collaboration-architecture.pdf> 摘录：“.......................................…”

### 看公司目标如何变成客户结果

**未来判断有条件。** 2027—2028年能否进入更广的规模化竞争，取决于客户确认交付、稳定运行、远程介入下降、复购和单位经济性同时改善。以下以公司已给出的节点作观察对象，不另外假设市场出货增长率。

| 公司或路线 | 已有基线 | 未来节点或条件 | 如何改变判断 |
|---|---|---|---|
| Figure | 宝马约1,250小时；03公司披露350余台 | BotQ年产1.2万台规划转成客户使用 | 从扩产能力走向复制能力 |
| Agility | 厂商口径9设施、65,000小时 | RaaS续约、多站点有效收费 | 从部署走向可持续经营 |
| Tesla | 2026年产线安装与训练 | 最早2027年下半年外销时间表 | 从内部项目走向外部产品 |
| 1X | NEO预订及家庭测试 | 2027年底10万台年产能目标 | 需同步证明家庭自主性 |
| 优必选 | 2026年上半年全尺寸921台 | Walker S年度5,000台目标及验收 | 检验工业订单兑现 |
| 通用家庭机器人 | 产品发布、上市与早期使用 | 多家庭持续任务、售后及复购 | 检验新增操作净价值 |

**目标的来源。** 对应节点来自Figure制造规划[27]、Agility部署与交易资料[2]、Tesla调研转述[35]、1X产能计划[30]及优必选券商跟踪[65]。

**工业首先看连续性。** 客户确认连续运行超过3个月，是有用的观察门槛。它能够跨过简单演示，开始暴露零件磨损、异常恢复、软件升级和人员培训问题。新华网转述的行业白皮书，也把这一门槛及复购作为投资评价重点。[64]

**模型首先看适配成本。** 跨本体演示之后，应看换机器人、换工位或换物体需要多少新增数据和工程工作。若仍需大量现场采集和逐任务调参，基础模型的商业价值主要是加速工具；若能显著减少这些工作，软件授权与多本体复用才会成为更强的商业模式。

**家庭首先看净劳动节省。** 机器人每天需要用户整理环境、处理卡住、清洁末端和修正任务的时间，应从其节省劳动中扣除。价格下降只能降低购买门槛，真正支持复购和口碑的，是稳定省时、安全和低维护。

**巡检首先看数据闭环。** 四足下一阶段要看自主完成任务、回坞成功、异常发现质量，以及与客户维护系统的连接。若这些指标领先，高端集成方案可以维持溢价；若低价本体加第三方软件达到相同结果，生态路线的优势就会扩大。

本节参考文献：
[27] BotQ供应链设计 <https://www.figure.ai/news/botq> 摘录：“Introducing BotQ, Figure’s new high-volume manufacturing facility for humanoid robots. BotQ’s first generation manufacturing line will be capable of manufacturing up to 12,000 humanoids per year. This is just the start and we will…”
[2] 宝马部署证据 <https://nexi.fund/humanoid-robot-deployments-2026/> 摘录：“The Q2 2026 earnings call was the next dated checkpoint, and Q1 guidance pointed to Fremont production beginning late July or August 2026. A company claim, like everything else about the program. That is the paradox in its purest…”
[35] 工厂调研转述 <https://wallstreetcn.com/articles/3779791> 摘录：“阴极和阳极材料的自产产能于2026年1月开始投产，预计将逐步带来成本改善，但由于影响因素较多，具体贡献难以单独量化——通常需要约18个月时间工厂才能达到合理规模和利用率。 摩根大通预计特斯拉2026年交付量约为180万辆，而公司当前总产能目标上限约为300万辆，产能利用率的提升空间为管理层扩大营收提供了重要支撑。”
[30] 另一累计口径 <https://robotbelt.com/americas-humanoid-robot-race-six-players-three-paths/> 摘录：“The United States now fields at least six serious robot companies: Tesla, Figure, Boston Dynamics, Agility, Apptronik, plus Norway-born, US-landed 1X. Six firms, six completely different technical routes. Rankings are easy to fake.”
[65] 财通证券:《订单高增验证商业化拐点，全场景成长空间打开｜09880优必选投资分析》-发现报告 <https://www.fxbaogao.com/detail/5620397> 摘录：“2）战略布局，如 人机共生 战略覆盖三大场景，U1系列超仿生人形机器人的推出； 3）市场表现，如2025年销量全球第一（1,079台），2026年上半年预计出货700台，以及京东预售锁单13,361台等关键数据； 4）研发投入，2025年5亿元，2026年超7亿元（超七成投向人形机器人）。 此外，报告还梳理了盈利预测（2026-2028年营收36.10/50.17/72.55亿元，归母净利润-4.37/-1.76/+1.98亿元）及投资建议（维持 增持 评…”
[64] 新华网融资统计 <https://www.news.cn/tech/20260513/358cfbcbd83f440a8a4eec65d9e75528/c.html> 摘录：“具身智能领域投资热度不减。 机构数据显示，截至5月11日，2026年国内具身智能领域投资总额已经超过2025年全年，单笔10亿元及以上融资超过10起。 投资热度之下，具身智能产业正经历一场从 讲故事 到 交答卷 的深刻转折。 多位业内人士对《经济参考报》记者表示，机构的关注重点正在转向企业落地实绩，复购率、连续运行时长等因素成为投资的 硬指标 。 最近一个月，多家企业宣布完成大额融资。 Vbot维他动力5月11日宣布完成Pre-A轮融资，融资金额近5亿元，…”

### 给采购、战略和投资读者的使用顺序

**先锁定一个任务。** 工厂搬箱、隧道巡检、酒店配送和家庭整理，不应放进同一采购需求。先确定地形、负载、节拍、人员接触及异常类型，再比较双足、轮式、固定臂或四足。

**再看已完成阶段。** 采购应优先看客户验收、实际运行和服务责任；战略研究可以关注模型与供应链趋势；投资则需要同时看现金消耗、订单收入转换和下一轮资金需求。不同目的可以关注同一公司，但应使用不同证据。

**最后看扩展代价。** 最值得持续跟踪的指标是：有效运行小时、远程介入次数、任务恢复时间、故障与安全事件、单任务成本、续约复购、真实交付及端侧算力。它们能把技术、产品和商业判断连接起来。

**口径与证据。** 全文主截止日为2026年9月13日。年报、监管文件、客户披露、公司自述、媒体和行业估算分别按原身份使用；订单、预订、管线、产能及目标不计作交付或收入。金额保留原币种，计算均列输入；硬件售价、BOM、RaaS费率、总员工和研发人员分别比较。Ghost Robotics、DJI、Skydio等边界条目的细分技术、融资估值和团队判断，以截至日前产品规格、客户合同、交易公告及法人组织边界为决定条件。

**最终判断。** 全球具身智能已进入产业现场，但仍是分任务、分形态发展的市场。近期更扎实的机会，在可重复任务、低维护设备和可复制交付；更大的长期空间，在跨任务模型与通用操作。真正能把两者连接起来的公司，才有机会从“机器人产品”走向持续扩展的平台。

本节参考文献：
[27] BotQ供应链设计 <https://www.figure.ai/news/botq> 摘录：“Introducing BotQ Introducing BotQ, Figure’s new high-volume manufacturing facility for humanoid robots. BotQ’s first generation manufact…”
[2] 宝马部署证据 <https://nexi.fund/humanoid-robot-deployments-2026/> 摘录：“Its tracker documents seven deployments as of August 9, 2026. Four pass the operator-side test. One deployment in the entire world, the…”
[35] 工厂调研转述 <https://wallstreetcn.com/articles/3779791> 摘录：“Optimus方面，Gen 3设计已完成定稿，供应链已基本锁定，生产线正在弗里蒙特工厂安装中，量产启动（SoP）后初步部署目标为2026年下半年进入 Optimus Academy 训练阶段，最早2027年下半年实现对外商业销售。 摩根大通维持对特斯拉的中性（Neutra…”
[30] 另一累计口径 <https://robotbelt.com/americas-humanoid-robot-race-six-players-three-paths/> 摘录：“In 2026, America’s humanoid robot industry stopped showing off and started defending itself. Against whom? The United States now fields…”
[65] 财通证券:《订单高增验证商业化拐点，全场景成长空间打开｜09880优必选投资分析》-发现报告 <https://www.fxbaogao.com/detail/5620397> 摘录：“从行业数据看，优必选2026年Walker S出货目标提升至5,000台，产能规划年产10,000台，同时发布覆盖工业、商业、家庭三大场景的 人机共生 战略。 工业端订单加速释放，空客、比亚迪等大客户持续加码采购； 消费端U1机器人预售锁单达13,361台，教育、政务场景…”
[64] 新华网融资统计 <https://www.news.cn/tech/20260513/358cfbcbd83f440a8a4eec65d9e75528/c.html> 摘录：“根据跃迁联盟等多家机构在北京亦庄具身纪元·智创百家生态大会上共同发布的《2026全球具身智能未来独角兽发展趋势》（下称《白皮书》），2026年开年至今，行业关注焦点从 谁出货更多 转向了 出货之后发生了什么 ，估值锚点从创始人背景变成了客户复购率。 交付力已取代技术力成为…”

## 参考文献

[1] <https://ifr.org/img/worldrobotics/Executive%5FSummary%5FWR%5F2025%5FService%5FRobots.pdf> IFR服务机器人统计; IFR年度统计; IFR物流机器人分析
[2] <https://nexi.fund/humanoid-robot-deployments-2026/> 宝马部署证据; Digit运行与客户; 拟议上市交易与财务; 产能与部署; Digit成本与交易文件口径
[3] <https://stockn.xueqiu.com/09880/20260828390148.pdf> 中期技术披露; 优必选中期业绩; 配售资金表
[4] <https://www.automate.org/robotics/industry-insights/blue-jay-way> Amazon产品规模; 研发与组织报道
[5] <https://www.anybotics.com/> 运营规模
[6] <http://www.puhuacapital.com/mobile/index.php/news/info/297> 普渡经营规模; 普渡收入结构; 融资与研发组织
[7] <https://www.stcn.com/article/detail/3628362.html> 运营规模
[8] <https://arxiv.org/html/2407.06886> 具身AI综合综述
[9] <https://mujin-europe.com/technology> Mujin技术架构; MujinOS架构; 控制器与接口
[10] <https://dexterity.ai/platform> Dexterity平台; Dexterity官方平台; 平台规模披露; Mech运行指标
[11] <https://www.goedelmachines.com/blog/quadruped-market-survey> 四足市场调查; 公司股权历史; Spot产品与接口; Spot客户与产品包; 公司发展节点; Data Navigator商业分析; Go2版本与接口; X30参数; 隧道案例与行业估算; Go2价格
[12] <https://arxiv.org/html/2609.03927v1> 统一机器人学习综述
[13] <https://www-file.huawei.com/dam/asset/view/physical-ai-cloud-edge-device-collaboration-architecture.pdf> 云边端协同架构; 全球物理智能格局
[14] <https://www.figure.ai/news/helix-02> Helix 02技术披露; Figure仿真训练; Helix感知与控制; Helix 02架构
[15] <https://developer.nvidia.com/blog/pretrained-to-imagine-fine-tuned-to-act-the-rise-of-world-action-models/> NVIDIA技术综述; π0.7架构分析; GEN-1数据路线
[16] <https://arxiv.org/html/2605.00080> 世界模型综合综述
[17] <https://www.shenlanxueyuan.com/news/detail/24> Fast-WAM技术介绍; Gemini Robotics技术介绍; GenieReasoner介绍
[18] <https://hub.baai.ac.cn/view/57478> Skild数据策略; S1实验报道; Skild融资与团队
[19] <https://arxiv.org/html/2412.07215v2> RoboTron-Mani论文; 论文实验与数据处理
[20] <https://www.iyiou.com/news/202608281139470> 优必选数据披露; 模型及数据披露; 产品矩阵与发布节点; 客户与应用; 研发团队披露; 优必选研发
[21] <https://www.roboticscenter.ai/research/robot-manipulation-market-landscape-2025> 融资与团队画像; Covariant市场画像; 仓储部署与拣选; 融资及团队来源; Intrinsic产业定位; 平台与资本路径
[22] <https://www.evsint.com/top-robotics-foundation-model-embodied-ai-companies-2026/> PI产业定位; NVIDIA平台定位
[23] <https://arxiv.org/html/2507.00917v2> 模型架构综述; π0论文索引; GR00T与仿真综述
[24] <https://www.panewslab.com/zh/articles/019e42e8-ef56-76a1-81e6-dc86caf856f7> Figure融资节点; Figure团队画像; 团队与实验室背景; 融资时间线; 团队与科研来源; Optimus公司画像; Tesla资金口径; Atlas技术转型; 并购及产业计划; 团队与历史; 上市历史; 创始人画像; 智元产品与生态; 智元公司画像; 傅利叶产品定位; 傅利叶团队与业务画像; 另一融资摘要
[25] <https://sacra.com/research/figure-vs-apptronik-vs-agility-robotics/> 累计融资比较; 私募融资摘要
[26] <https://www.tmtpost.com/8118474.html> 财报阶段报道
[27] <https://www.figure.ai/news/botq> BotQ供应链设计; 制造与可靠性组织
[28] <https://www.figure.ai/news/production-at-bmw> Figure现场复盘
[29] <https://www.figure.ai/news/ramping-figure-03-production> Figure 03生产披露
[30] <https://robotbelt.com/americas-humanoid-robot-race-six-players-three-paths/> 另一累计口径; Digit商业模式; Apollo商业报道; 扩展轮报道; Atlas产品报道; 1X技术与产品报道; NEO价格、预订与工厂计划; Digit服务费; 价格与人工成本锚点
[31] <https://www.evsint.com/zh-CN/top-8-humanoid-robot-companies-2026/> Digit产品画像; 模型合作与维护设计; 数据采集路线; A2产品进展; 1X融资画像
[32] <https://www.agilityrobotics.com/content/agility-robotics-announces-new-innovations-for-market-leading-humanoid-robot-digit> Agility产品公告
[33] <https://augustadynamics.com/de/resources/humanoid-robot-deployments-in-industry> Toyota部署追踪
[34] <https://ifactoryapp.com/industries/manufacturing-plant/manufacturing-humanoid-vendor-comparison-unitree-apollo-figure-2026> Apollo规格与配置; 客户与场景比较; 配置比较
[35] <https://wallstreetcn.com/articles/3779791> 工厂调研转述; Optimus推进时间表
[36] <https://dataclouds.cninfo.com.cn/sjother2/documents/2026/2026-05-25/3d7fc0538abe281340a95c9c77a90525.pdf> 宇树技术披露; 模型应用阶段; 经营数据
[37] <https://www.cls.cn/detail/2135323> 产品形态与GOVLA; 订单与产线披露; 2025年融资报道
[38] <https://news.pedaily.cn/202606/565245.shtml> 2026年融资节点; 融资整理方法
[39] <https://www.eeo.com.cn/2026/0320/813654.shtml> 产品销售时间线; 价格与客户结构; 成本结构报道; 融资与股东; 销量及成本; 宇树价格
[40] <https://www.csrc.gov.cn/csrc/c105906/c7642867/content.shtml> 证监会批复
[41] <https://robot24.com/quadruped-robots-finally-have-a-business-model-so-why-is-the-us-banning-the-cheapest-ones> IPO媒体口径
[42] <https://static.sse.com.cn/stock/disclosure/announcement/c/202603/002178_20260320_QY8F.pdf> 团队与人才规划
[43] <https://pdf.dfcfw.com/pdf/H3_AP202605071822028328_1.pdf?1778171901000.pdf> GO-1路线; 行业产品表; GR-1行业参数; GR-1价格与目标; 服务机器人经济性案例; 配送机价格
[44] <https://ai2robotics.com/about/> 智平方技术自述; 创始人与团队
[45] <https://www.humanoidsdaily.com/features/the-humanoids-of-europe> NEURA产品体系; NEURA产品与商业进展; NEURA融资与组织; 欧洲机器人专题; 欧洲案例细节; NEURA团队
[46] <https://techcrunch.com/2025/03/11/yet-another-ai-robotics-firm-lands-major-funding-as-dexterity-closes-latest-round/> 客户与业务报道; 融资与创始人报道
[47] <https://www.aboutamazon.com/news/company-news/amazon-covariant-ai-robots> Amazon许可公告; 团队迁移公告; Amazon技术合作
[48] <https://mujin-corp.com/resources/news/seriesd-announcement-advancing-industrial-automation-intelligent-robotics> Mujin业务与扩展; Mujin融资公告
[49] <https://gembawalk.mujin.co.jp/about-mujin/overview> Mujin团队与设施; Mujin团队
[50] <https://www.21jingji.com/article/20260530/ef49a0aa425d14230b0c015aaa31178e.html> 产品扩展时间线; 电网部署与海外市场; 经营、融资与IPO报道; 创始团队背景
[51] <https://newsletter.semianalysis.com/p/quadruped-state-of-the-market-unitree> 四足控制回路分析; QDD执行器分析
[52] <https://www.anybotics.com/robotics/robot-capabilities/> ANYmal能力
[53] <https://www.greaterzuricharea.com/zh-hans/news/anybotics-zairongzi-6000-wanmeiyuankuozhangmeiguoshichang> 融资与科研背景
[54] <https://www.pudurobotics.com/en/company> 普渡技术架构
[55] <https://www.keenon.com/zh-cn/news?page=> 产品与场景目录
[56] <https://www.keenon.com/zh-cn/news/gcsrslkphtwaw2> WAIC产品披露; 经营规模与IDC口径
[57] <http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESH_STOCK/2026/2026-4/2026-04-25/12191589.PDF> 科沃斯2025年报; 年报经营与产品分类; 证券、现金流与研发数据; 管理层及人员表; 科沃斯人员表
[58] <https://www.xinhuanet.com/finance/20260427/78fa95b18a06411e88cd766a8fce4a17/c.html> 新品发布时间
[59] <https://www.cnbc.com/2025/08/22/chinas-robot-vacuum-roborock-plans-mass-market-cleaners-with-ai-arms.html> CNBC石头专访; Z70价格与初评; AI团队与研发布局
[60] <https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation> Waymo世界模型
[61] <https://acisresearch.com/research/physical-ai-robotics-weekly-2026-09-04> 2026年9月扩张; Cybercab周报
[62] <https://www.tmtpost.com/7779567.html> 项目团队历史; 空中机器人技术与基础设施讨论
[63] <https://research.contrary.com/report/tesla-waymo-and-the-great-sensor-debate> 传感器与模型比较
[64] <https://www.news.cn/tech/20260513/358cfbcbd83f440a8a4eec65d9e75528/c.html> 新华网融资统计; 交付评价变化
[65] <https://www.fxbaogao.com/detail/5620397>
