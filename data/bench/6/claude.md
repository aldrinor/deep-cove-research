# 全球具身智能技术路线与代表性公司全景报告（截至2026年10月16日）

截至2026年10月，全球具身智能已经分成三股力量。第一股是押注"通用机器人大脑"的模型公司，比如Physical Intelligence、Skild AI、Google DeepMind和NVIDIA，技术路线正从单一VLA走向"VLA+世界模型+强化学习"的融合。第二股是垂直整合的人形本体公司，美国有Figure、Tesla、Agility、Boston Dynamics。第三股是以出货量和资本化领先的中国本体与整机公司，比如宇树、智元、银河通用、优必选。中国在量产、出货和上市上明显领先；美国在模型、估值和单个客户的落地深度上领先。不过整个行业仍处在"融资和估值远超收入"的阶段。

## TL;DR

- **技术路线**："大脑"层的主流是端到端VLA，形态多为分层的快慢双系统，例如π0.7、Gemini Robotics 2、GR00T N1.7、Helix 02。2026年的新方向是"世界动作模型"（World Action Model），也就是让视频生成和世界模型进入预训练；GR00T N2预计2026年底推出，自变量WALL-B已经发布。运动控制层基本收敛到"仿真+强化学习"。数据层正从昂贵的真机遥操作，转向"人类第一视角视频+UMI轻量采集+仿真合成+少量真机"的数据金字塔。
- **商业化与出货**：中国厂商主导出货。据Counterpoint Research 2026年8月20日的报告，2026年上半年全球人形机器人出货超过2.2万台、同比增长接近300%，智元以9,700台居首、份额超43%，宇树超过7,000台（31.1%），前五名都是中国公司，合计占86%。宇树2025年营收17.08亿元、净利润2.88亿元，2026年8月19日登陆科创板，发行价对应市值约610亿元。美国头部公司的2025年出货只有百台量级：宇树招股书援引的行业数据（快科技称出自德意志银行）显示，Figure和Agility各约150台，且未经两家公司公开确认；Tesla Optimus截至2026年10月仍未公开量产。
- **资本**：一级市场估值在2026年急剧抬升。Figure的估值是390亿美元（2025年9月）；Skild超过140亿美元（2026年1月）；Physical Intelligence约110至112亿美元，这是2026年5月的工商备案，公司未正式宣布。中国有一批公司进入200亿元人民币以上估值档，包括银河通用、星海图、千寻、自变量，智元新一轮约500亿元。与此同时，二级市场和"数采中心订单"这类收入质量问题，正在推动行业"挤泡沫"。

## Key Findings（核心判断）

1. **"大脑"与"本体"分化已成定局，但两边都在往对方的地盘延伸。** 纯大脑公司（PI、Skild、Generalist、Genesis）不造本体，靠跨本体模型和授权获取价值。头部本体公司（Figure、Tesla、1X、智元、小鹏）则坚持全栈自研：Figure在2025年2月终止与OpenAI的合作，把Helix收回自研。Google\[1\]\[2\] DeepMind和NVIDIA通过与Apptronik、Boston Dynamics等本体厂商深度绑定，扮演"安卓"的角色。\[3\]\[4\]
2. **VLA仍是主流，但纯VLA的泛化瓶颈正在被"世界模型+RL"补足。** π0.7（2026年4月）强调技能组合泛化；Gemini Robotics 2（2026年7月30日）把规划（ER 2）与执行（VLA）拆开，做三模型协同；NVIDIA把GR00T N2定位为联合建模视频token与动作token的世界动作模型。这说明业界已有共识：单靠遥操作数据训练VLA，很难达到开放场景的可靠性。\[5\]\[6\]\[7\]
3. **数据是真正的护城河，路线之争正演变成"数据规模化成本"之争。** 公开信息中较有说服力的规模化证据，来自NVIDIA、UC Berkeley与马里兰大学联合发表的EgoScale论文（arXiv 2602.16710）：基于20,854小时人类第一视角视频训练，平均任务完成率从1,000小时时的0.30升至20,000小时时的0.71。千寻称真实交互数据超过20万小时，计划2026年突破100万小时。智元、优必选等中国公司则借地方政府"数采中心"项目，同时获取数据和收入，这种模式也引发了收入质量的争议。\[8\]\[9\]
4. **量产目标与实际交付之间普遍存在巨大落差。** Tesla多次推迟Optimus V3的量产时间点，2026年7月提交SEC的Q2材料只写道Fremont的Optimus产线在Model S/X产线退役后开工建设、"anticipated production later this year"，且首批Optimus将用于"Optimus Academy"采集训练数据。1X的NEO在2026年4月工厂投产，但截至2026年7月中旬尚无可独立核实的消费者交付。小鹏IRON计划2026年底量产，2027年才对外交付。\[10\]\[11\]
5. **资本化窗口集中在2026年开启。** 宇树科创板上市，从受理到过会只用了73天；智元启动港股IPO，但因新一轮融资，年内大概率无法挂牌；乐聚递表创业板；星海图、逐际动力、强脑科技据报已秘密递表港交所；Agility通过SPAC赴纳斯达克，交易作价25亿美元。\[12\]\[13\]\[14\]\[15\]\[16\]\[17\]\[18\]

---

## 第一部分：技术路线梳理

### A. 模型/算法层

| 路线 | 核心思想 | 代表成果（时间） | 优点 | 缺点/争议 | 成熟度判断 |
|---|---|---|---|---|---|
| 端到端VLA | 预训练VLM加动作输出头（扩散、流匹配或离散token），从像素和语言直接输出关节动作 | PI π0（开源）→π0.5→π0.6→π0.7（2026-04-16）；Gemini Robotics（2025-03）→Gemini Robotics 2（2026-07-30）；NVIDIA GR00T N1→N1.7（3B参数，Apache 2.0）；Figure Helix（2025-02）→Helix 02（2026-01）；智元GO-1；自变量WALL-OSS（开源）；千寻Spirit v1.5（2026-01开源）；星动纪元ERA-42；星海图G0（2025-08开源）；银河通用"银河星脑"等 | 能继承互联网知识，具备语言指令跟随和一定的零样本泛化；工程上统一 | 依赖昂贵的真机数据；长程任务和高精度接触任务的可靠性不足；评测标准不统一，各家多报相对基线的提升 | 实验室和受控场景可用；开放场景尚未达到产品级可靠性 |
| 分层/快慢双系统 | System 2由大模型做语义理解和任务规划（低频），System 1由小模型或控制器做高频动作；部分公司还加一层System 0做全身运动控制 | Figure Helix（S2/S1，Helix 02加入全身控制，删除109,504行手写C++代码）；Gemini Robotics 2（ER 2规划+VLA执行+On-Device）；GR00T N1.7"Action Cascade"双系统（Cosmos-Reason2-2B骨干+32层DiT）；逐际动力System\[5\]\[7\]\[19\] 0/1/2三层架构（COSA操作系统，2026-01）；小鹏IRON"VLT+VLA+VLM"；星海图联合创始人赵行提出的"快慢双系统"\[20\]\[21\]\[22\] | 兼顾推理能力与实时性；可替换模块，便于商业交付 | 层间接口和误差传播；"端到端"与"分层"的边界已经模糊 | 2026年事实上的主流工程形态 |
| 世界模型/视频生成驱动 | 学习物理世界的动态预测，用于想象推演、合成数据、策略评估，或直接联合预测"视频+动作" | NVIDIA Cosmos（世界基础模型）和GR00T N2（世界动作模型，2026-03预告，目标2026年底）；Google\[23\] Genie 3；1X World Model（用于评估与训练NEO策略）；自变量WALL-A（VLA与世界模型融合）和WALL-B（2026-04，"世界统一模型WUM"）；宇树称实现"世界模型实时驱动全自主人形机器人格斗"\[11\]\[24\]\[25\]\[26\] | 可利用海量视频数据，缓解真机数据瓶颈；适合做仿真与评测 | 物理一致性和可控性不足；算力成本高；"世界模型"的定义被泛用 | 研究前沿，2026年快速进入产品架构 |
| 仿真+强化学习（sim-to-real） | 在GPU并行仿真中大规模训练策略，再迁移到真机，主要用于行走、跑跳、全身控制 | NVIDIA Isaac Lab/Isaac Sim；Skild（报道称在Isaac Lab中同时运行10万个机器人实例）；宇树、逐际动力、Agility、Boston\[27\] Dynamics的运动控制；Figure 03自主爬梯（2026-08）\[28\] | locomotion已基本"解决"，成本低，可复制 | 灵巧操作的sim-to-real差距仍大；接触建模不准 | 运动控制层成熟，操作层仍在攻坚 |
| 融合趋势 | VLA做语义到动作的映射，世界模型做数据与评估，RL做后训练和真机自我改进，仿真做运动底座 | PI π0.6引入真实部署中的RL自我改进；GR00T N2；Gemini Robotics 2的全身智能 | — | — | 2026年下半年的主要方向 |

**判断**：2026年模型层竞争的焦点，已经从"谁先做出VLA"转为"谁能用最低成本、最多样的数据，加上RL后训练，把成功率从80%推到99%以上"。商业化真正需要的指标是连续作业时长和干预率。Figure公开过8小时连续班次、60多小时直播分拣8万多件包裹；Agility披露累计6.5万运行小时。这些指标比Demo更有说服力，但仍主要是公司自报。\[1\]\[12\]\[28\]

### B. 数据层

| 数据路线 | 代表 | 优点 | 缺点 |
|---|---|---|---|
| 真机遥操作 | Tesla（动捕和遥操作团队，后转向人类视频）、Figure（Project Go-Big，招聘大量遥操作和数据采集岗位）、1X（NEO早期任务依赖人类遥操作，作为数据闭环）、智元（AgiBot World数据集、数据采集工厂）、星海图（计划2026年建"全球最大规模真实场景具身数据集"）、千寻（20万小时以上真实交互数据）\[8\]\[29\]\[30\]\[31\]\[32\] | 质量高，与本体完全匹配 | 每小时成本高，扩展慢，换本体就要重采 |
| 仿真合成 | 银河通用（仿真合成数据训练GraspVLA等）、NVIDIA（Isaac/Cosmos合成数据、GR00T-Mimic动作重定向） | 可无限扩展，低成本，能自动标注 | 存在sim-to-real差距，尤其在柔性物体和接触任务上 |
| 人类视频/第一视角/UMI | NVIDIA（EgoScale论文：人类第一视角数据从1,000小时增至20,000小时，平均任务完成率从0.30升至0.71）、Figure（人类视频预训练）、Generalist（GEN-0用大规模真实世界数据验证scaling law） | 成本最低，规模最大，场景多样 | 存在形态差异（人手和机械手），缺少力觉和触觉信息 |
| 政府/产业"数采中心" | 优必选中标广西防城港、自贡、九江、惠州等数采中心项目；智元生态伙伴采购\[33\] | 同时获得数据和收入，推动订单规模 | 收入可持续性和真实需求受质疑：梅卡曼德创始人公开质疑部分企业借数采中心和关联交易制造收入，银河通用发表声明回应\[9\] |

**数据金字塔**是行业的共识形态：底层是海量互联网和人类视频，中层是仿真合成与UMI数据，顶层是少量高质量真机遥操作与部署数据，再叠加RL自我改进。

### C. 本体/硬件层

| 形态 | 代表产品 | 适用场景 | 评价 |
|---|---|---|---|
| 双足全尺寸人形 | Tesla Optimus V3、Figure 03、Boston Dynamics Atlas（产品版）、Agility Digit、Apptronik Apollo、1X NEO、宇树H2、优必选Walker S2、小鹏IRON、众擎、逐际动力 | 汽车工厂、物流、家庭（远期） | 通用性和叙事最强，但成本、安全与可靠性压力最大。Figure CEO称轮式是"死胡同"，双足与轮式之争仍未结束\[28\] |
| 轮式/轮臂人形 | 智元远征/精灵系列、银河通用Galbot G1/S1、星海图R1、智平方AlphaBot、千寻Moz | 零售、药房、工厂上下料、数采 | 稳定、续航长、成本低，2026年中国出货的主力形态之一 |
| 中小型人形 | 宇树G1、松延动力、加速进化、乐聚鲁班/Aelos | 科研教育、文娱、展示 | 出货量大但单价低，是中国出货量领先的主要来源 |
| 四足 | 宇树Go/B系列、Boston Dynamics Spot（2026-04接入Gemini Robotics-ER 1.6做巡检）、Neura\[34\] MiPA | 巡检、安防、科研 | 最成熟、已规模化盈利的形态 |
| 单臂/双臂操作平台 | PI、Generalist、Dyna、Genesis等大脑公司的研发平台；Neura LARA/MAiRA | 研发、桌面操作、柔性制造 | 是大脑公司的数据和验证载体 |
| 灵巧手 | 灵心巧手Linker Hand、因时RH56系列、强脑Revo2、1X NEO手（25个主动自由度，腱驱）、Tesla Optimus V3手（22自由度）、小鹏IRON手（22自由度）\[22\]\[29\] | 精细操作 | 正成为独立的高增长零部件赛道 |
| 专用机器人 | Mind Robotics（Rivian分拆，工厂AI机器人）、Agility\[35\] Digit（料箱搬运）、Dexterity、Covariant（Amazon） | 特定工序 | 商业化最快，但通用性低 |

---

## 第二部分：代表性公司

### 一、美国/加拿大

#### 1. Figure AI（全栈：双足人形+自研VLA）
- **技术路径**：自研Helix VLA，采用S2/S1双系统，2025年2月推出，同期终止与OpenAI的合作。2026年1月27日发布Helix\[1\]\[2\] 02，覆盖全身控制，删除109,504行手写C++代码。数据来自真机遥操作和人类视频预训练。硬件自研，并有自建工厂BotQ。CEO称已全面转向非中国供应链。\[19\]\[28\]\[36\]
- **产品进度**：Figure 03于2025年10月发布，Figure 02已退役。BotQ初始设计年产能12,000台。据报道，到2026年4月产线约每90分钟下线一台。2026年6月19日CEO\[37\]\[38\]\[39\] Brett Adcock在X上发帖称"For the first time, robots now outnumber humans at Figure"，约740台对约660人；据The Daily Star报道，这约660人中只有约314人是正式受薪员工，其余为小时工或合同工。已展示8小时连续班次、多日分拣直播、双机协同整理卧室（2026-05）和自主爬梯（2026-08）。CEO预告了Figure 4。\[1\]\[28\]
- **商业化**：BMW斯帕坦堡工厂，Figure 02参与生产3万多辆车；2026年6月30日Figure\[40\] 03进驻BMW。收入从未公开披露。\[36\]\[39\]\[41\]
- **融资**：2025年9月C轮超过10亿美元，投后估值390亿美元，Parkway Venture Capital领投，NVIDIA、Microsoft、Brookfield、Bezos等参与，累计约19亿美元。截至2026年9月没有新的一级市场定价。有二级市场报价下调的报道，来源可信度一般。2026年7月公司发声明，警示有人未经授权出售其股份。\[2\]\[36\]\[39\]\[42\]\[43\]
- **团队**：创始人Brett Adcock，此前创办Archer Aviation和Vettery，2026年另创AI实验室HARK。员工约660人（2026年6月）。\[2\]\[19\]\[44\]

#### 2. Tesla Optimus（全栈：车企复用）
- **技术路径**：复用FSD的端到端视觉网络、Dojo/Cortex算力和自研AI5芯片；数据依托"真实世界AI数据"。V3采用22自由度腱驱灵巧手。\[45\]\[46\]\[47\]
- **产品进度**：2026年4月22日的Q1电话会上，Musk把Fremont的Optimus生产初步定在2026年7月底或8月，并称爬坡会"非常缓慢"。据Tesla提交SEC的8-K附件99.1（Q2\[47\]\[48\] 2026 Update），Fremont工厂的Optimus产线在Model S和X产线退役后开工建设，"anticipated production later this year"，首批Optimus将用于"Optimus Academy"采集训练数据；材料没有给出具体日期、数量或价格。Fremont产线设计年产能100万台，德州二代产线的长期目标是年产1000万台，2027年起。2026年1月Musk承认，Optimus"尚未在工厂中实质性使用"。V3尚未正式亮相。\[49\]\[50\]\[51\]
- **商业化**：没有对外销售。售价目标是规模化后2万至3万美元，为Musk过往表态，属前瞻性说法。\[52\]
- **关注点**：2026年10月21日的Q3财报。\[53\]
- **判断**：Optimus是"承诺与交付差距"最大的样本。在实际交付出现之前，应把它当作期权，而不是现实产能。

#### 3. Physical Intelligence（π，纯大脑）
- **技术路径**：通用机器人基础模型。π0采用流匹配动作生成，已开源；之后有π0.5（开放家庭泛化）、π0.6（引入RL自我改进）和π0.7（2026年4月16日，技能组合泛化）。不造硬件，跨本体。\[7\]\[54\]\[55\]\[56\]\[57\]
- **产品与商业化**：没有公开产品和收入，也没有商业化时间表；路线接近"授权模型"。\[56\]\[58\]\[59\]\[60\]
- **融资**：种子轮7,000万美元（2024年3月）；A轮4亿美元，估值24亿美元（2024年11月）；B轮6亿美元，估值56亿美元（2025年11月，CapitalG领投）。2026年3月Bloomberg报道其洽谈约10亿美元、估值超过110亿美元的融资，Founders\[61\]\[62\]\[63\]\[64\] Fund、Lightspeed参与；2026年5月21日的公司备案显示已授权约10.5亿美元C轮股票，对应估值110至112亿美元，但公司尚未正式宣布。累计融资约21亿美元。\[57\]\[60\]\[62\]\[64\]
- **团队**：Karol Hausman、Sergey Levine、Chelsea Finn、Brian Ichter、Lachy Groom等，多来自Google DeepMind、伯克利和斯坦福。据报员工约80人，但这一数字的时间点不明。\[59\]

#### 4. Skild AI（纯大脑："omni-bodied brain"）
- **技术路径**：Skild Brain，跨本体通用基础模型，大量依赖NVIDIA Isaac Lab仿真和RL。\[27\]
- **商业化**：一份非一线来源报道称首年收入年化约3,000万美元，未经核实。SoftBank同期收购ABB机器人业务，市场预期Skild会成为其装机基础上的"大脑"层。\[27\]
- **融资**：2026年1月14日完成近14亿美元C轮，估值超过140亿美元，SoftBank领投，NVentures、Macquarie、Bezos Expeditions、1789 Capital参与，三星、LG、Schneider、Salesforce Ventures等战略方跟投。前一轮是2025年年中，估值约45亿美元。CEO\[65\]\[66\]\[67\] Deepak Pathak称累计融资超过20亿美元。\[68\]
- **团队**：Deepak Pathak（CEO）和Abhinav Gupta，均来自CMU。

#### 5. 1X Technologies（挪威起家、美国总部；家庭人形）
- **技术路径**：自研Redwood AI通用模型和1X World Model，用于评估和训练。NEO早期以人类遥操作作为数据闭环和兜底。腱驱手有25个主动自由度（2026年7月9日发布），自研手部产线，年产能1万只。\[10\]\[29\]\[69\]
- **产品进度**：2025年10月28日开放预订，售价2万美元或每月499美元订阅。据报5天内获得1万份预订，但这是二手报道。2026年4月30日Hayward工厂投产，满产年产能约1万台。CEO设定的2027年出货目标是5万台。\[29\]\[69\]
- **商业化**：与EQT签约，2026至2030年最多向其300多家被投企业提供1万台NEO。消费者交付存在冲突信息：TNW在2026年5月报道"开始发货"，而截至2026年7月中旬，第三方未能核实任何消费者交付，公司表示"部分用户今年拿到，部分更晚"。\[10\]\[29\]\[70\]
- **融资**：已披露的融资约1.25亿至1.4亿美元，包括OpenAI Startup Fund、EQT、Tiger Global、Samsung NEXT。The\[69\]\[70\]\[71\] Information在2025年9月报道其寻求最高10亿美元、估值至少100亿美元的融资，截至2026年中尚未确认完成。\[70\]\[72\]
- **团队**：CEO Bernt Børnich，工厂员工200多人。\[29\]\[73\]

#### 6. Agility Robotics（物流双足人形，率先SPAC上市）
- **技术路径**：Digit采用自研运动控制和Arc云平台；新一代Digit v5定位为"AI驱动、可协作安全"的人形机器人。Agility也是Gemini\[74\] Robotics-ER的受信测试方。\[75\]
- **商业化**：在9个客户设施有部署承诺，累计运行6.5万小时。客户包括Schaeffler、GXO、丰田加拿大工厂、Mercado Libre和Amazon；在GXO单个仓库已搬运超过10万个料箱。Digit\[12\]\[76\]\[77\]\[78\] v5的多年期合同订单超过3亿美元，约对应1,000台，采用RaaS模式，单台5年生命周期收入约50万美元，为示意性测算。\[76\]\[79\]
- **财务矛盾**：一份SEC文件摘要显示2025年净销售额为180万美元，另有媒体称"过去12个月收入3,700万美元、上年烧钱1亿美元"。两者口径冲突，以最终注册文件为准。\[12\]\[80\]
- **融资与IPO**：2026年6月24日宣布与Churchill Capital Corp XI合并，交易作价25亿美元（交易前股权价值），拟以AGLT代码在纳斯达克上市，附带2亿美元PIPE，由富士康领投。此前累计融资约6.4亿美元。\[12\]\[77\]\[81\]\[82\]
- **团队**：CEO Peggy Johnson，前微软高管。\[12\]

#### 7. Apptronik（双足人形，与Google DeepMind深度绑定）
- **技术路径**：Apollo接入Gemini Robotics模型，是Google的人形合作伙伴。与Jabil合作制造。\[83\]\[84\]\[85\]
- **产品进度**：2026年6月底通过官网更新低调推出Apollo 2，并启用约9万平方英尺的数据采集与训练基地Robot Park（奥斯汀）。\[86\]
- **商业化**：在Mercedes-Benz、GXO、Jabil做试点，没有公布价格和吞吐指标。\[86\]\[87\]
- **融资**：2026年2月11日完成5.2亿美元A轮扩展，A轮合计9.35亿美元。估值口径不一：CNBC报约50亿美元，Bloomberg报超过55亿美元。\[86\]投资方包括Google、Mercedes-Benz、B Capital等。\[82\]\[88\]
- **团队**：CEO Jeff Cardenas，来自UT Austin。员工400多人，计划一年内再招至少200人。\[85\]\[88\]

#### 8. Boston Dynamics（Hyundai全资；双足和四足）
- **技术路径**：电驱Atlas产品版在CES 2026（1月5日）发布，与Google DeepMind合作集成Gemini Robotics；执行器由Hyundai Mobis供应。\[3\]\[89\]Spot在2026年4月接入Gemini Robotics-ER 1.6。\[34\]
- **产品与商业化**：Atlas在波士顿总部立即投产，2026年产量全部承诺给Hyundai RMAC和Google DeepMind，\[90\]外部客户要到2027年。\[34\]\[89\]Hyundai计划2028年在美国Metaplant部署Atlas做零件排序，并建设年产3万台的机器人工厂。\[3\]\[34\]\[90\]\[91\]没有公开售价；韩国报道的32万美元来自匿名信源。\[92\]2026年10月公司披露单台Atlas组装约需1天，目标缩短到1小时。\[90\]
- **股权**：2026年6月，Hyundai以3.25亿美元收购SoftBank所持剩余9.65%股份，实现全资控股。\[90\]

#### 9. Google DeepMind（Gemini Robotics，平台型大脑）
- 2025年3月发布Gemini Robotics VLA和Gemini Robotics-ER。2026年7月30日发布**Gemini Robotics 2**系列，包含三个模型：执行用的VLA、规划用的Gemini Robotics ER 2，以及本地运行的On-Device 2。ER 2已通过Gemini API向开发者开放，输入价格为每百万token 2美元；VLA和On-Device仍面向受信测试者。本体伙伴有Apptronik、Boston\[5\]\[75\]\[93\] Dynamics和Agility等。\[3\]\[75\]
- **判断**：DeepMind是唯一同时拥有前沿多模态大模型、自有机器人团队和多家顶级本体伙伴的玩家，最有可能成为"机器人安卓"。但它的商业化以API和合作为主，不直接卖机器人。

#### 10. NVIDIA（GR00T/Isaac/Cosmos，"卖铲人"）
- GR00T N1.7于2026年3月GTC发布，4月17日开放早期访问，7月获得商业许可。参数3B，采用Cosmos-Reason2-2B骨干和32层DiT，Apache 2.0开源。GR00T N2是基于DreamZero研究的世界动作模型，2026年3月预告，目标2026年底推出。另有Isaac\[7\]\[23\] Sim/Lab仿真、Cosmos世界基础模型和Jetson Thor端侧算力。
- **战略**：NVIDIA通过NVentures投资了Skild、Generalist、Neura等，同时向几乎所有本体公司提供算力和工具链，是"大脑与本体分化"中最大的受益者。\[94\]\[95\]

#### 11. 其他美国新锐大脑/系统公司

| 公司 | 路线 | 最新进展 | 融资/估值 |
|---|---|---|---|
| Generalist AI | 通用操作基础模型，真实世界数据scaling | GEN-0（2025-11），GEN-1（2026-04）\[96\]\[97\] | 2026-06完成4亿美元B轮，估值20亿美元，Radical Ventures领投，NVIDIA、Bezos跟投；2026-08由8VC领投约2亿美元扩展，估值30亿美元（TechCrunch）；创始人Pete Florence、Andy Zeng、Andy Barry，均出自Google，参与过RT-2、PaLM-E\[65\]\[94\]\[98\] |
| Genesis AI | 全栈物理AI实验室（仿真+模型） | 2026-05发布首个机器人模型，灵巧手可做精细任务\[99\] | 2025-07种子轮1.05亿美元；2026-07 Bloomberg报道洽谈约5亿美元，投前估值30亿美元，Premji Invest拟领投，尚未确认完成\[100\]\[101\] |
| Mind Robotics | Rivian分拆的工厂AI机器人，CEO RJ Scaringe | 面向工业产线，认为人形存在弱点\[35\] | 种子轮1.15亿美元；2026-03完成5亿美元A轮，Accel、a16z领投；2026-05再融4亿美元，累计超过10亿美元\[35\] |
| Dyna Robotics | 商用操作基础模型 | 本轮研究未能核实最新产品 | 第三方数据库显示累计约1.44亿美元，未核实\[99\] |

注：The Bot Company、Covariant（已被Amazon吸纳团队）、Dexterity、Field AI、Hexagon AEON、Sanctuary AI这几家，本轮研究没有取得2026年可核实的新数据，因此不列具体数字。

### 二、中国

#### 1. 宇树科技（本体+小脑领先；已上市）
- **技术路径**：核心优势是自研电机、减速器、关节等组件和运动控制（"小脑"）。招股书坦言，公司在"大脑"（具身大模型）上投入较少，也没有大规模做真实数据采集，2024年起才开始加强。2026年称实现"世界模型实时驱动全自主人形机器人格斗"。\[17\]
- **产品与出货**：四足有Go和B系列，人形有G1和H2。据招股书，2025年人形机器人出货5,511台（不含轮式双臂），销售收入8.68亿元，占主营业务收入的51.78%，公司称全球第一。招股书规划的人形年产能为7.5万台。2026年春晚有24台G1和1台H2表演。\[102\]
- **财务**：2023至2025年营收分别为1.59亿、3.92亿、17.08亿元；净利润分别为-0.11亿、0.95亿、2.88亿元（另有口径为营收16.99亿、归母净利润2.78亿）。2025年末在手订单2.82亿元。2026年第一季度营收4.23亿元，增速从2025年的332.64%回落到68.4%左右。2026年上半年营收10.52亿至11.28亿元，同比增长35.6%至45.4%，扣非净利润同比下降。\[17\]\[102\]\[103\]\[104\]
- **IPO**：2026年3月20日科创板受理，6月1日过会（用时73天），8月19日上市，代码688836。发行价150.80元，对应发行后市值约609.93亿元，市销率约35.89倍。网上中签率0.018%，网上有效申购户数约978万户，均创科创板纪录。募资42.02亿元。\[17\]\[104\]\[105\]
- **团队**：创始人王兴兴。
- **判断**：宇树是全球唯一实现规模化盈利的人形和四足公司，但增速已在放缓，大脑能力是短板。上市后的估值溢价能否维持，取决于它能否把硬件优势转化为"模型+场景"的收入。

#### 2. 智元机器人（智元创新；全栈+生态）
- **技术路径**：自研GO-1通用具身基座模型（2025年3月）、AgiBot World真机数据集、BFM和GCFM等模型；产品线覆盖远征（轮式和双足）、精灵、灵犀等。2025年通过收购上纬新材控股权布局资本平台。
- **出货**：据Omdia，2025年出货超过5,100台，全球份额约39%。宇树对此口径有异议，称自己的纯双足终端交付更高。据Counterpoint\[106\] Research 2026年8月20日的报告，2026年上半年出货9,700台，份额超43%，全球第一。2026年9月24日第2万台下线。
- **收入**：2023年30万元，2024年6,000多万元，2025年10.5亿元；2026年第一季度超过10亿元（据投资人和公司人士）。另有说法称2026年全年目标40亿元，来源较弱。订单大量来自投资方、地方国资和400多家生态伙伴，需求真实性受到媒体质疑。\[106\]\[107\]\[108\]\[109\]
- **融资与IPO**：成立后完成10余轮融资，投资方50多家，包括腾讯、京东、上汽、比亚迪、红杉中国、高瓴。估值从2025年3月的约150亿元，涨到2026年10月新一轮（10亿至15亿元，接近收尾）的约500亿元（《财经》2026-10-13）。2026年7月24日确认启动港股IPO，基石投资人的目标估值为400亿至500亿港元。按港交所"递表后新融资需满120日"的规则，年内大概率无法上市，可能推迟到2027年初。\[18\]\[106\]\[108\]\[110\]
- **团队**：创始人邓泰华，联合创始人彭志辉（"稚晖君"，前华为"天才少年"）。

#### 3. 银河通用（Galbot；重大脑、仿真合成数据）
- **技术路径**：自研端到端具身大模型"银河星脑"，包括GraspVLA、GroceryVLA等；以仿真合成数据为核心。本体是轮式G1和S1。\[9\]
- **商业化**：主打"银河太空舱"无人便利店和智慧药房，已进入百台级运营。售价方面，G1约70万元、S1约105万元。2026年春晚为指定具身大模型机器人。据Counterpoint，2026年上半年出货全球第三。\[9\]\[18\]\[24\]\[30\]
- **出货口径冲突**：钛媒体报道"一年卖出150台"，另有报道称商业部署超过千台。\[111\]\[112\]
- **融资**：2025年6月完成11亿元融资，宁德时代领投；2025年12月融资3亿美元，估值30亿美元；2026年3月2日再融25亿元，投资方包括国家人工智能产业投资基金、中国石化、中信、上汽金控等。成立34个月累计融资约70亿元，估值超过200亿元，公司称是国内具身智能领域累计融资最多的公司。\[9\]\[30\]\[113\]\[114\]
- **争议**：梅卡曼德创始人质疑行业借数采中心和关联交易制造收入，银河通用发表声明回应。\[9\]
- **团队**：创始人王鹤，北京大学研究员。\[111\]

#### 4. 优必选（UBTECH，港股9880；工业人形）
- **技术路径**：Walker S2配备自主热插拔换电系统，搭载"群脑网络2.0（BrainNet 2.0）"和Co-Agent智能体。\[33\]\[115\]
- **产品与交付**：2025年11月12日开始量产交付；2025年交付超过500台；12月26日第1,000台在柳州下线。2025年Walker\[33\] S系列订单累计超过13亿元，单笔最大合同2.5亿元。2026年产能目标5,000台，并指向万台级。客户包括德州仪器，另据报道有空客、比亚迪等。\[33\]\[116\]\[117\]
- **说明**：部分2026年的订单和交付细节（如空客首批100台）来自东方财富财富号等自媒体，未经核实。另获Infini\[117\] Capital 10亿美元战略授信。\[118\]

#### 5. 小鹏IRON（车企路线）
- **技术路径**：82个全身自由度，灵巧手22自由度，搭载3颗自研图灵AI芯片，算力2250 TOPS；采用第二代VLA，以"VLT+VLA+VLM"大小脑协同，感知复用智驾鹰眼方案。\[22\]
- **进度**：2026年7月24日广州工厂小批量试产；9月8日产线正式启用，核心制程自动化率超过80%。目标是2026年底规模量产、月产1,000台；2027年上半年在门店和商业场景交付，随后出海；2028年进入家庭。何小鹏自2026年6月起亲自兼任机器人业务CEO。截至2026年10月尚未向付费客户交付。\[22\]\[50\]\[119\]\[120\]\[121\]\[122\]

#### 6. 小米
- 2026年3月有报道称小米机器人已进厂做拧螺丝作业。\[123\]小米战投还连续参与了自变量的三轮融资。\[25\]本轮研究未能核实小米人形机器人的量产时间表。

#### 7. 大脑与模型型创业公司

| 公司 | 技术路径 | 产品/商业化 | 融资（时间） | 团队 |
|---|---|---|---|---|
| 自变量机器人（深圳，2023-12成立） | 走"VLA+世界模型"融合路线：WALL-A，开源WALL-OSS，WALL-B（2026-04，"世界统一模型"）；本体为量子系列\[24\]\[25\]\[26\]\[124\] | 58到家家政服务、汽车零部件产线，二手来源；没有公开台数\[124\] | 2026-01完成A++轮10亿元，字节跳动、红杉领投；2026-02上汽金控领投，估值超过百亿元；2026-04至06连续完成B、B+、B++、C四轮，其中B轮近20亿元由小米战投领投，投后估值超过200亿元，投资方包括中国移动、红杉、IDG、阿里云和美团（早期轮）\[25\]\[125\]\[126\]\[127\]\[128\] | 王潜，清华电子系本硕，USC博士；CTO王昊\[124\]\[126\] |
| 千寻智能（杭州，2024-01成立） | Spirit v1 VLA（2025-03），Spirit v1.5（2026-01开源，RoboChallenge Table30得66.09分，超过π0.5）；本体Moz\[129\] | 在宁德时代产线作业，插接成功率99%；与京东合作零售场景；真实数据超过20万小时\[8\]\[130\]\[131\] | 2026-02两轮近20亿元，估值超过百亿元；2026-04完成10亿元，顺为、云锋领投，多家媒体称估值超过200亿元；2026-06完成15亿元；三个月累计近50亿元（轮次命名口径混乱）\[8\]\[114\]\[132\]\[133\] | 韩峰涛（CEO，浙大，珞石机器人联合创始人）、高阳（清华交叉信息研究院助理教授）\[134\]\[135\]\[136\] |
| 星海图（北京，2023-09成立） | G0 VLA（2025-08开源），G0 Plus（2026-01），G0 Tiny（2026-02）；本体R1系列\[137\] | 获头部车企和物流企业的千台级订单；CEO称2026年陆续交付千台，2027年目标万台以上；与京东签三年战略合作\[32\]\[138\]\[139\] | 2026-02完成B轮10亿元，估值百亿元；2026-04完成B+轮近20亿元，估值超过200亿元，蓝思科技参与并负责量产；累计近50亿元；据报2026-09秘密递表港交所，公司未确认\[16\]\[30\]\[31\]\[140\]\[141\]\[142\] | 高继扬（CEO，曾在Waymo、Momenta）、赵行（清华交叉信息研究院）、李天威\[143\] |
| 星动纪元（北京，清华交叉信息研究院孵化） | ERA-42端到端VLA；本体STAR1、L7、Q5；灵巧手XHAND1\[144\]\[145\] | 累计订单超过5亿元；与中国邮政、顺丰在10多个物流中心落地，称2026年第二季度起千台级交付；创始人自认"量产是小批量"\[113\]\[144\]\[146\] | 2026-03完成10亿元，估值超过百亿元，三星等参与；2026-04融资超过2亿美元，顺丰领投；2026-07完成10亿元，诚通基金领投；2026年累计近50亿元\[113\]\[140\]\[147\]\[148\] | 陈建宇，清华交叉信息研究院助理教授\[148\] |
| 智平方（AI2 Robotics，深圳） | GOVLA全域VLA，AlphaBrain；本体AlphaBot\[24\] | 覆盖7个行业的商业闭环（公司口径）\[149\] | 一年完成12轮；2026-02 B轮超过10亿元，估值超过百亿元；TechCrunch在2026-07报道约7.35亿美元融资，估值近30亿美元\[79\]\[140\] | — |

#### 8. 本体与运动控制型公司

| 公司 | 要点 |
|---|---|
| 逐际动力（深圳） | 采用System 0/1/2三层架构，COSA具身操作系统于2026-01发布；累计数千台订单，一半以上来自海外（中东、北美）。2026-02完成2亿美元B轮；2026-07完成近2亿美元Pre-IPO轮，投后估值150亿元，IDG、蓝思等参与，约七成资金来自海外。2026-03完成股改，据报已秘密递表港股。创始人张巍，南方科技大学教授，曾任俄亥俄州立大学长聘教授\[13\]\[20\]\[21\]\[150\]\[151\] |
| 乐聚机器人（深圳） | 2026-05-19创业板IPO获受理，拟募资26亿元。2025年营收2.58亿元，其中人形机器人2.17亿元；2023至2025年累计亏损超过1.7亿元。按Omdia和Counterpoint，2025年出货全球第四，2026年上半年全球第五。产品有夸父、鲁班、Aelos，大脑借助华为盘古等伙伴。股东包括腾讯（7.32%）、东方精工等。创始人冷晓琨，哈工大背景\[14\]\[18\]\[152\]\[153\]\[154\]\[155\]\[156\] |
| 傅利叶（上海） | 从康复机器人起家，截至2025年第一季度总交付超过1万台（以康复设备为主）。人形产品有GR-1、GR-2、GR-3（康养交互，2025-09预售），2026年WAIC推出GR\[157\] Mini和GR Nano。2025-01完成近8亿元E轮；2025-05润阳科技出资不超过3亿元，对应投前估值约80亿元。2026年没有找到新一轮融资的可靠报道；科创板辅导备案进度未经核实。CEO顾捷\[158\]\[159\]\[160\] |
| 众擎、松延动力、加速进化、星尘智能、开普勒等 | 松延动力2026-03完成B轮10亿元，曾登上春晚；众擎、乐聚等在2026年春节后完成10亿元级融资（财新）。其余公司本轮没有取得可核实的2026年数据\[114\] |
| 灵初智能、它石智航、穹彻智能、极佳科技 | 极佳视界在2026年3月完成超过10亿元融资（知乎和具身智能之心统计，二手）。其余公司本轮没有取得可核实数据\[140\] |
| 华为 | 以"大脑"和生态赋能为主，例如乐聚借助盘古大模型，哈勃投资入股千寻。本轮没有核实到自有人形量产计划\[154\]\[161\] |

#### 9. 灵巧手厂商

| 公司 | 产品与出货 | 融资 |
|---|---|---|
| 灵心巧手（北京） | Linker Hand系列，覆盖腱绳、直驱、连杆三种路线，O6售价6,666元；自称占全球高自由度灵巧手市场80%以上；2026年初累计订单超过1万台，单月最高产能4,000只，2026年交付目标5万至10万只\[162\]\[163\] | 2026-02完成B轮近15亿元；2026-04完成B+轮。估值说法冲突：媒体称超过200亿元，新一轮"目标60亿美元"，而祥源新材的转让公告对应约164亿元\[162\]\[163\]\[164\] |
| 因时机器人（北京） | RH56系列，2026-03发布RH56H1；登上2026年春晚；美国售价6,500美元起；"年出货超过1万台"的说法未经核实\[165\]\[166\]\[167\] | 2026-02完成C1、C2两轮合计数亿元，投资方包括中国移动链长基金、深创投、北京人工智能产业基金、博原资本等，估值未披露\[168\]\[169\] |
| 强脑科技（BrainCo，杭州） | 智能仿生手和Revo2仿生灵巧手，脑机接口背景\[170\]\[171\] | 2026年1月融资约20亿元，投后估值超过13亿美元，IDG、华登领投，蓝思、韦尔、领益等参与；据Bloomberg报道已向港交所秘密递表，中金、瑞银为保荐人，是否已挂牌未核实。创始人韩璧丞，哈佛脑科学博士期间创业\[171\]\[172\]\[173\]\[174\]\[175\] |

### 三、欧洲及其他

| 公司 | 路线与产品 | 进度/商业化 | 融资 | 团队 |
|---|---|---|---|---|
| Neura Robotics（德国） | 4NE1人形，与Porsche设计合作，号称可举100公斤，使用GR00T N1；另有LARA、MAiRA协作臂和MiPA四足；2025-10收购ek robotics\[69\]\[176\] | 4NE1计划2026年底首次批量出货，目标2030年出货500万台（公司口径）；与Kawasaki合作推出CL系列协作机器人\[69\]\[95\]\[176\] | 2026-06完成最高14亿美元C轮，Tether领投，Amazon、NVIDIA、欧洲投资银行参与。Bloomberg在2026-03报道估值约40亿欧元，另有媒体估约70亿美元，口径不一\[69\]\[95\]\[177\] | 创始人David Reger，员工约1,200人\[69\]\[176\] |
| Humanoid（英国） | HMND 01人形\[178\] | 工业场景，投资方包括Schaeffler、Bosch\[179\] | 2026-07-21完成1.52亿美元A轮，估值13.5亿美元，Prime Movers Lab领投，累计2.7亿美元；欧洲首家纯人形独角兽\[178\]\[179\] | — |
| Mimic（瑞士）、Wandercraft（法国） | 灵巧手及操作；外骨骼和自平衡人形 | 本轮没有取得可核实的2026年数据 | — | — |
| Rainbow Robotics（韩国） | 三星已成为其最大股东（2024年至2025年，背景信息） | 据报三星计划在CES 2027首秀人形机器人（IT之家，属"消息称"）\[11\] | — | — |
| 日本 | SoftBank以资本方身份布局Skild，并收购ABB机器人业务；Kawasaki与Neura合作 | 本轮没有核实到日本本土人形创业公司的大额进展 | — | — |

---

## 第三部分：横向对比与趋势

### 综合对比表（数据截至2026年10月，单位按原口径）

| 公司 | 所属路线 | 核心产品/模型 | 量产/交付规模 | 商业化阶段 | 最新融资/估值 | 创始人/团队 |
|---|---|---|---|---|---|---|
| 宇树 | 本体+小脑 | G1/H2、Go/B系列 | 2025年人形5,511台（招股书） | 规模化盈利，已上市 | 科创板上市，发行市值约610亿元（2026-08）\[105\] | 王兴兴 |
| 智元 | 全栈+生态 | 远征/精灵、GO-1 | 累计2万台（2026-09）；2026上半年9,700台\[18\] | 规模营收（2025年10.5亿元） | 约500亿元（2026-10，新一轮接近收尾）；港股IPO进行中\[18\] | 邓泰华、彭志辉 |
| 银河通用 | 大脑+仿真数据 | G1/S1、银河星脑 | 百台到千台级（口径冲突） | 零售和药房运营 | 超过200亿元，累计约70亿元（2026-03） | 王鹤 |
| 优必选 | 工业人形 | Walker S2 | 2025年超过500台；第1,000台于2025-12下线 | 订单超过13亿元，港股上市 | 港股9880 | 周剑 |
| 小鹏IRON | 车企全栈 | IRON | 2026-09产线启用 | 未交付，2027年上半年交付 | 集团内部 | 何小鹏兼任CEO |
| Figure | 全栈双足 | Figure 03、Helix 02 | 约740台在运行（2026-06，自报）\[2\] | BMW商用试点 | 390亿美元（C轮，2025-09）\[43\] | Brett Adcock，约660人 |
| Tesla Optimus | 车企全栈 | Optimus V3 | 尚未公开量产 | 内部使用 | 上市公司 | Elon Musk |
| Agility | 物流双足 | Digit v5 | 9个客户设施，6.5万小时 | 订单超过3亿美元，RaaS | SPAC作价25亿美元（2026-06） | Peggy Johnson |
| Apptronik | 双足+Gemini | Apollo 2 | 试点 | 试点 | 约50亿至55亿美元（2026-02） | Jeff Cardenas，400多人 |
| Boston Dynamics | 双足和四足 | Atlas、Spot | 2026年产量全部给Hyundai和DeepMind\[34\] | Spot已商用；Atlas内部部署 | Hyundai全资（2026-06） | — |
| 1X | 家庭人形 | NEO、Redwood | Hayward工厂满产年产约1万台 | 预订阶段，交付待核实 | 已披露约1.25亿至1.4亿美元；100亿美元估值融资未确认 | Bernt Børnich |
| Physical Intelligence | 纯大脑 | π0到π0.7 | — | 研究阶段，无收入 | 约110亿至112亿美元（2026-05备案）\[57\]\[60\] | Hausman、Levine、Finn等 |
| Skild AI | 纯大脑+仿真 | Skild Brain | — | 早期商业化 | 超过140亿美元（2026-01） | Deepak Pathak、Abhinav Gupta |
| Google DeepMind | 平台大脑 | Gemini Robotics 2 | — | API开放（ER 2） | — | Carolina Parada（机器人负责人） |
| NVIDIA | 工具链+开源模型 | GR00T N1.7/N2、Cosmos、Isaac | — | 平台 | — | — |
| Generalist | 纯大脑 | GEN-1 | — | 少量客户 | 30亿美元（2026-08） | Pete Florence等 |
| 自变量 | VLA+世界模型 | WALL-OSS/WALL-B | 未披露 | 早期 | 超过200亿元（2026-06） | 王潜 |
| 千寻 | VLA | Spirit v1.5、Moz | 未披露 | 工厂试点 | 约200亿元（2026-04，媒体口径） | 韩峰涛、高阳 |
| 星海图 | VLA+真机数据 | G0、R1 | 2026年交付千台（目标） | 订单阶段 | 超过200亿元（2026-04） | 高继扬、赵行 |
| 星动纪元 | VLA | ERA-42、STAR1 | 小批量；订单超过5亿元 | 物流落地 | 超过百亿元（2026-03） | 陈建宇 |
| 逐际动力 | 运动控制+三层架构 | 双足/轮足、COSA | 数千台订单 | 海外占一半以上 | 150亿元（2026-07，Pre-IPO） | 张巍 |
| Neura | 全栈（欧洲） | 4NE1 | 2026年底首批出货 | 协作臂已商用 | 最高14亿美元C轮（2026-06） | David Reger，约1,200人 |

### 2025至2026年关键趋势

1. **VLA开源化成为中国与NVIDIA的共同策略。** 开源的有π0（PI）、GR00T N1.x（Apache 2.0）、WALL-OSS、星海图G0和千寻Spirit v1.5。PI、Figure、DeepMind的最新旗舰模型则保持闭源。可以预期，开源模型会把"可用基线"迅速拉平，竞争力将来自数据和部署闭环，而不是模型权重本身。
2. **数据规模竞赛正从"真机小时数"转向"人类视频与世界模型"。** NVIDIA的人类视频scaling结果和GR00T N2，Figure的人类视频预训练，自变量的WUM，都在押注能低成本扩展的数据源。真机遥操作仍是质量锚点，但已不再是规模主力。
3. **量产目标与实际交付存在系统性落差。** 典型例子有：Tesla（产线安装中，产量未知）、1X（交付待核实）、小鹏（2027年才交付）、Neura（2026年底首批）。中国的高出货量中，相当部分来自科研教育、文娱、数采中心和生态伙伴采购，不应直接等同于产线上的生产力替代。
4. **IPO潮在2026年开启。** 已完成的有宇树（科创板，2026-08-19）。进行中的有：智元（港股，大概率推迟到2027年）、乐聚（创业板已受理）、Agility（SPAC）。据报已秘密递表的有星海图、逐际动力、强脑科技（均为港股）。Figure、PI、Skild暂无IPO时间表。
5. **融资热度与估值。** 据网易科技，2026年上半年中国赛道融资总额超过900亿元，而2025年国内人形机器人市场规模仅约30亿元。全球方面，有媒体统计2026年人形机器人创业公司融资超过180亿美元，而头部公司2025年合计收入约3.4亿美元，属二手统计。估值与收入之比极高，是本轮周期最大的风险点。2026年出现了"百亿元只是第一梯队门槛"的现象，也出现了围绕收入质量的公开争议，以及二级市场的降温信号：宇树2026年增速放缓，智元IPO受阻，Figure的二级市场报价据报下调。\[9\]\[95\]\[134\]
6. **中美路线差异。** 美国以大脑为先：估值集中在模型公司，人形本体公司走"少量、高价、深度客户"的路线，如BMW、Hyundai、GXO。中国以本体和规模为先：依托供应链与地方产业资本，用数量换数据、换收入，大脑公司普遍还配套自研本体。国家人工智能产业投资基金、中国石化、诚通等"国家队"资本大规模入场，是中国的独特变量。
7. **大脑公司与本体公司在分工中合作。** 已形成的组合有：DeepMind与Apptronik、Boston Dynamics、Agility；NVIDIA GR00T与Neura等；SoftBank同时持有Skild（大脑）和ABB机器人业务（本体）；银河通用直接采用宇树等成熟硬件。另一方面，Figure、Tesla、1X和小鹏证明，头部本体公司会把大脑收回自研。最终格局大概率是：少数平台大脑（DeepMind、NVIDIA、PI、Skild）加上若干全栈巨头（Tesla、Figure、智元、小鹏）并存。

---

## Recommendations（决策建议）

- **评估公司时，看可验证的部署指标，不看Demo。** 重点关注四项：连续无干预作业时长、单位任务成本与ROI、付费客户数量与续约、扣除数采中心和关联方后的收入。按这些标准，目前可信度较高的是宇树（经审计的财报和上市披露）、Agility（SEC文件中的订单与运行小时）和Figure（BMW数据，但为自报）。
- **投资和合作上，优先选择"数据闭环+场景"组合。** 纯大脑公司的估值已经远超可证收入（PI、Skild），适合长期、能容忍高风险的资本。产业方更现实的路径是：采用开源基座（GR00T N1.7、π0、国产开源VLA），再用自有场景数据做微调和RL后训练。
- **场景选择上，2026至2027年优先考虑料箱搬运、上下料、零件排序、零售和药房拣选、巡检。** 家庭场景至少还要数年；Figure CEO也称家庭"还需要个位数年份"。\[180\]
- **硬件选型上**，结构化工厂可优先考虑轮式双臂，成本和稳定性更优；需要上下台阶或跨越复杂地形时再选双足。灵巧手是确定性较高的零部件机会。
- **风险监控方面**，需要关注的节点有：Tesla Q3财报（2026-10-21）和V3发布、GR00T N2发布（目标2026年底）、智元IPO进度、Agility的SPAC交割和正式财报、1X的消费者交付验证。

## Caveats（不确定性说明）

- **未正式宣布或"据报"的数据**：PI的C轮（备案口径，公司未宣布）、1X的100亿美元估值、Genesis AI的30亿美元估值、星海图/逐际动力/强脑科技的秘密递表，都属于此类，不应视为既成事实。
- **口径冲突**：
  - 宇树与智元的"全球第一"统计口径不同（纯双足与含轮式）。
  - 宇树营收有17.08亿元和16.99亿元两种数字，可能分别对应营业收入和主营收入。
  - 银河通用的出货有"150台"与"超过千台部署"两种说法。
  - Agility的收入有"2025年净销售180万美元"与"过去12个月3,700万美元"两种说法。
  - 灵心巧手的估值有三种说法。
  - Apptronik的估值有约50亿与超过55亿美元两种说法。
  - Neura的估值有约40亿欧元与约70亿美元两种说法。
- **前瞻性陈述**：Tesla的100万台年产线、1,000万台规划和2万至3万美元售价，1X的2027年5万台，Neura的2030年500万台，智元的2027年营收100亿元，小鹏的月产1,000台，都是公司目标或预测，不是已实现的业绩。
- **来源质量**：部分数据来自自媒体或聚合站（东方财富财富号、知乎、valueaddvc、robozaps等），已尽量标注；部分公司（Mimic、Wandercraft、Sanctuary、The Bot Company、Dexterity、Field AI、众擎、加速进化、灵初、它石、穹彻等）本轮未取得可核实的2026年数据，报告中没有编造具体数字。
- **时效性**：本报告信息截至2026年10月16日。行业融资与产品节奏以月为单位变化，关键数字使用前应再次核对原始公告。

## 資料來源

1. [Figure AI's Helix-02 Robots Complete Full 8-Hour Autonomous Shifts as Humanoid Race Intensifies](https://www.techtimes.com/articles/316632/20260514/figure-ais-helix-02-robots-complete-full-8-hour-autonomous-shifts-humanoid-race-intensifies.htm)
2. [Figure AI: Inside the \$39B Humanoid Robotics Company](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)
3. [Boston Dynamics Atlas Robot That Beat Tesla To The Factory Floor](https://www.forbes.com/sites/jonmarkman/2026/01/19/boston-dynamics-atlas-robot-that-beat-tesla-to-the-factory-floor/)
4. [Introducing Gemini Robotics and Gemini Robotics-ER, AI models designed for robots to understand, act and react to the physical world. — Google DeepMind](https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/)
5. [Gemini Robotics 2: what DeepMind's own numbers show](https://www.eesel.ai/blog/gemini-robotics-2)
6. [Humanoid Robot Development Complete Roadmap 2026.10｜香川友志](https://note.com/kagawatomo/n/nb26b8c9b3768?hl=en)
7. [Top 10 Physical AI Models Powering Real-World Robots in 2026 - MarkTechPost](https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/)
8. [雷军马云罕见联手领投：千寻智能30天融资30亿，估值破200亿 - 21经济网](https://www.21jingji.com/article/20260409/herald/5fada821db647bb788dd048c0475f8a7.html)
9. [银河通用：成立34个月、6轮融资70亿：具身智能赛道“资金收割机”的底气与隐忧-虎嗅网](https://www.huxiu.com/article/4890421.html)
10. [1X NEO Review: Price, Pre-Order & Release Date (2026)](https://blog.robozaps.com/b/1x-neo-review)
11. [小鹏机器人生产线正式启用，“全球首位高阶通用人形机器人”自主走下产线 - IT之家](https://www.ithome.com/0/999/529.htm)
12. [Agility Robotics Will List on Nasdaq After a \$2.5 Billion SPAC Merger - Startup Fortune](https://startupfortune.com/agility-robotics-will-list-on-nasdaq-after-a-25-billion-spac-merger/)
13. [逐际动力“秘交”港股，人形机器人再冲IPO - 搜狐时间线](https://timeline.sohu.com/news/yTiHsUHJfH)
14. [乐聚机器人成创业板第四套标准首单，贡献关联公司近一半营收 - 21经济网](https://www.21jingji.com/article/20260520/herald/41902d125c673921f715ec27d5ea116a.html)
15. [消息称强脑科技已秘密提交香港IPO申请 刚完成近20亿元融资|融资|香港IPO|脑机接口\_新浪科技\_新浪网](https://finance.sina.com.cn/tech/roll/2026-01-13/doc-inhhchmx6200269.shtml)
16. [具身智能独角兽「星海图」，据报秘密递交香港上市申请\_腾讯新闻](https://news.qq.com/rain/a/20260909A07R5Z00)
17. [宇树科技科创板IPO过会，从受理到上会用时仅73天](https://m.thepaper.cn/newsDetail_forward_33280884)
18. [消息称具身智能独角兽公司智元启动新一轮融资，估值约 500 亿元\_新浪科技\_新浪网](https://finance.sina.com.cn/tech/digi/2026-10-14/doc-iniveefp7774904.shtml)
19. [The End of C++: Brett Adcock on Helix 02 and Figure’s Path to "Room-Scale" Autonomy](https://www.humanoidsdaily.com/news/the-end-of-c-brett-adcock-on-helix-02-and-figure-s-path-to-room-scale-autonomy)
20. [估值150亿，半年融资4亿美元，逐际动力稳步推进IPO进展\_腾讯新闻](https://news.qq.com/rain/a/20260714A03TY700)
21. [半年融4亿美元、估值150亿，逐际动力完成股改冲刺IPO\_腾讯新闻](https://news.qq.com/rain/a/20260714A08YEO00)
22. [小鹏IRON人形机器人广州工厂开启试生产 年底冲刺量产\_凤凰网](https://i.ifeng.com/c/8v1vX9SetFw)
23. [NVIDIA GR00T N2 Explained](https://robocloud-dashboard.vercel.app/learn/blog/gr00t-world-action-models-2026)
24. [2026 具身智能投资窗口：银河通用、灵初智能等 14 家企业最新进展](https://m.jiemian.com/article/14531147.html)
25. [自变量机器人投后估值超200亿元](https://www.stdaily.com/web/gdxw/2026-06/29/content_539279.html)
26. [10亿元！自变量机器人完成2026年首笔融资\_模型\_投资\_智能](https://www.sohu.com/a/975456958_100053070)
27. [SoftBank and Nvidia Close \$1.4Bil Deal to Anoint Skild AI as the “Universal Brain” for Robotics at \$14Bil Valuation](https://pittsburghstartupnews.substack.com/p/softbank-and-nvidia-finalizing-deal)
28. [Figure-03](https://www.humanoidsdaily.com/tags/figure-03)
29. [1X Technologies - Company Profile, Milestones & Funding - Venture Atlas](https://www.ventureatlas.org/company/1x-technologies)
30. [2026年Q1具身智能企业估值盘点｜50+公司最新进展梳理\_荣格工业资源网](https://www.industrysourcing.cn/article/476234)
31. [星海图完成近20亿元B+轮融资，估值超200亿元](https://m.thepaper.cn/newsDetail_forward_32878036)
32. [再融20亿！星海图把具身智能头部门槛抬到了200亿](https://www.qbitai.com/2026/04/394626.html)
33. [Walker S2\_百度百科](https://baike.baidu.com/item/Walker%20S2/66227110)
34. [Boston Dynamics Ships Full Atlas Production Run to Hyundai and DeepMind](https://ai2.work/blog/boston-dynamics-ships-full-atlas-production-run-to-hyundai-and-deepmind)
35. [Mind Robotics](https://en.wikipedia.org/wiki/Mind_Robotics)
36. [Figure AI — \$39B · Brett Adcock](https://siliconvalleyinvestclub.com/companies/figure/)
37. [Humanoid robots decommissioned in Terminator-style molten steel leap](https://interestingengineering.com/ai-robotics/humanoid-robot-decommissioned-molten-steel)
38. [Figure AI IPO 2026: \$39B Valuation, Risks & Bull Case](https://techmarketbriefs.com/pre-ipo/figure-ai/)
39. [Figure AI Explained: Brett Adcock's \$39B Humanoid Robot (2026) - Beginners in AI](https://beginnersinai.org/figure-ai-explained/)
40. [Figure AI Statistics 2026: Valuation, Robots, Funding & Production Data - Axis Intelligence](https://axis-intelligence.com/figure-ai-statistics/)
41. [Figure AI Valuation (2026): \$39B — The Biggest Pre-Revenue Bet in Robotics](https://www.teahose.com/guides/figure-ai-valuation)
42. [Apptronik Scores \$935 Million, Hits Top 3 For Humanoid Robotics Funding](https://www.forbes.com/sites/johnkoetsier/2026/02/11/apptronik-scores-935-million-hits-top-3-for-humanoid-robotics-funding/)
43. [Figure AI: \$39B Valuation vs. \$174 Secondary Price](https://valueaddvc.com/blog/figure-ai-valuation-2026-39b-humanoid-robotics-investors)
44. [Figure AI](https://en.wikipedia.org/wiki/Figure_AI)
45. [Tesla, Inc. - Form 10-Q - FY2026](https://www.sec.gov/Archives/edgar/data/0001318605/000162828026026673/tsla-20260331.htm)
46. [Tesla, Inc. - Form 10-Q - FY2026](https://www.sec.gov/Archives/edgar/data/0001318605/000162828026049270/tsla-20260630.htm)
47. [Tesla Optimus Gen 3 Explained: Real Specs, Price, AI5 Chip & 2026 Release - Robo Pulse](https://robopulse.net/reviews/tesla-optimus-gen-3/)
48. [Tesla Optimus V3: Release Dates & Timing Claims](https://humanoidversus.com/timelines/tesla-optimus-v3)
49. [Optimus (robot)](<https://en.wikipedia.org/wiki/Optimus_(robot)>)
50. [小鹏启动IRON人形机器人量产，特斯拉Optimus进展迟缓](https://m.thepaper.cn/newsDetail_forward_34031129)
51. [Tesla Optimus Gen 3: Release Date & Price (Aug 2026)](https://blog.robozaps.com/b/tesla-optimus-gen-3)
52. [Tesla Optimus V3 Production Starts This Summer: Full Timeline](https://www.basenor.com/blogs/news/tesla-optimus-v3-production-starts-this-summer-full-timeline)
53. [Tesla, Inc. - Form 8-K - FY2026](https://www.sec.gov/Archives/edgar/data/0001318605/000162828026064366/exhibit991111111.htm)
54. [Physical Intelligence in 2026: Valuation, Funding, Models, Founders & Score](https://brightsentience.com/company/physical-intelligence/)
55. [Physical Intelligence (π) — Complete Profile & Analysis 2026](https://www.roboticscenter.ai/companies/physical-intelligence)
56. [Physical Intelligence Funding 2026: \$1.07 billion Raised](https://www.netfigo.com/startup/physical-intelligence/)
57. [Physical Intelligence Pre-IPO Stock — Price & Valuation](https://axevil.com/company/physical-intelligence)
58. [Andrew Benson on X: "The \$11 billion company with no product, no revenue, and no timeline. On purpose. Physical Intelligence just closed roughly \$1.6B across two rounds at an \$11.2B valuation. It sells nothing. It plans to sell nothing for a while. And both Jeff Bezos and OpenAI are on the cap tab… / X](https://x.com/AndrewBenson/status/2086846023658525180)
59. [Lukas Ziegler on X: "JUST IN: @physical\_int raising \$1B at \$11B+ valuation! The valuation has doubled in 4 months! Physical Intelligence, the SF robotics startup, is in discussions to raise about \$1 billion in new funding at a valuation exceeding \$11 billion, according to Bloomberg. @foundersfu… / X](https://x.com/lukas_m_ziegler/status/2037865145553027461)
60. [Physical Intelligence funding: Every round, investor, and valuation (2026)](https://www.revenuememo.com/p/physical-intelligence-funding)
61. [Physical Intelligence Seeks \$1B at \$11B Valuation](https://www.implicator.ai/physical-intelligence-nears-1-billion-round-doubling-valuation-in-four-months/)
62. [Physical Intelligence: \$5.6B Now, \$11B Round in Talks](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)
63. [Physical Intelligence Inc.](https://en.wikipedia.org/wiki/Physical_Intelligence_Inc.)
64. [Physical Intelligence — \$11B · Karol Hausman, Chelsea Finn](https://siliconvalleyinvestclub.com/companies/physical-intelligence/)
65. [Robotics startup Generalist reaches \$3B valuation, sources say](https://techcrunch.com/2026/08/25/robotics-startup-generalist-reaches-3b-valuation-sources-say/)
66. [Skild AI Robotics Manufacturing Foundation Model Raised \$1.4B](https://medium.com/@creed_1732/skild-ai-robotics-manufacturing-foundation-model-raised-1-4b-bffbaad0e70e)
67. [Skild AI Raises \$1.4B, Now Valued Over \$14B](https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B)
68. [Robotics software maker Skild AI hits \$14B valuation](https://techcrunch.com/2026/01/14/robotic-software-maker-skild-ai-hits-14b-valuation/)
69. [Top 10 humanoid robot startups to watch in 2026, ranked by total funding — TFN](https://techfundingnews.com/top-humanoid-robot-startups-2026-funding/)
70. [1X Technologies Company Profile: Founders, Funding, Humanoid Robots](https://embodyvc.com/companies/1x-technologies/)
71. [Top 10 Humanoid Robot Companies & Startups 2026: Ranked](https://theroboticlife.com/top-10-humanoid-robot-startups-2026/)
72. [Norway’s 1X raising \$1B at \$10B valuation to bring humanoid robot NEO into homes - Tech Startups](https://techstartups.com/2025/09/24/norways-1x-raising-1b-at-10b-valuation-to-bring-humanoid-robot-neo-into-homes/)
73. [Report: Humanoid Robotics Firm 1X Seeking Up to \$1B at a Valuation of \$10B or More](https://www.humanoidsdaily.com/news/report-humanoid-robotics-firm-1x-seeking-up-to-dollar1b-at-a-valuation-of-dollar10b-or-more)
74. [Churchill Capital Corp XI - Form 425 - FY2026](https://www.sec.gov/Archives/edgar/data/0002074973/000121390026071290/ea029548401ex99-1.htm)
75. [Google announces Gemini Robotics, a Gemini 2.0 model optimized for robots - Neowin](https://www.neowin.net/news/google-announces-gemini-robotics-a-gemini-20-model-optimized-for-robots/)
76. [Investor Presentation of Churchill, dated June 2026](https://www.sec.gov/Archives/edgar/data/2074973/000121390026071287/ea029548401ex99-2.htm)
77. [Churchill Capital Corp XI - Form 425 - FY2026](https://www.sec.gov/Archives/edgar/data/0002074973/000121390026094533/ea0303767-425_churchill11.htm)
78. [Agility Robotics plans SPAC merger for public listing](https://humanoid.guide/agility-robotics-plans-public-listing-through-spac-merger/)
79. [Churchill Capital Corp XI - Form 425 - FY2026](https://www.sec.gov/Archives/edgar/data/0002074973/000121390026076112/ea0297344-425_churchill11.htm)
80. [Churchill XI highlights \$2.5B Agility Robotics SPAC](https://www.stocktitan.net/sec-filings/CCXI/425-churchill-capital-corp-xi-business-combination-communication-e50d6c7efbd9.html)
81. [Figure, Agility, Apptronik: Who's Winning the \$39B Race?](https://universeblend.blog/agility-figure-apptronik-funding/)
82. [Humanoid Robot Funding Tracker 2026 — Every Deal, Every Round](https://humanoidindex.org/funding)
83. [Apptronik valuation, funding & news](https://sacra.com/c/apptronik/)
84. [Apptronik - In The News](https://apptronik.com/company/in-the-news)
85. [Apptronik raises \$520 million at \$5 billion valuation for Apollo robot](https://www.cnbc.com/2026/02/11/apptronik-raises-520-million-at-5-billion-valuation-for-apollo-robot.html)
86. [Apptronik - Company Profile, Milestones & Funding - Venture Atlas](https://www.ventureatlas.org/company/apptronik)
87. [How's Apptronik doing these days?](https://newmarketpitch.com/blogs/news/humanoid-robotics-apptronik-upate)
88. [Apptronik: Funding, Valuation, Robot Specs & More](https://humanoidindex.org/companies/apptronik)
89. [Boston Dynamics Unveils New Atlas Robot to Revolutionize Industry](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/)
90. [Inside Atlas's Prototype Shop: Boston Dynamics Discloses One-Day Build, Targets One Hour](https://www.techtimes.com/articles/329041/20261014/inside-atlass-prototype-shop-boston-dynamics-discloses-one-day-build-targets-one-hour.htm)
91. [Boston Dynamics unveils production-ready version of Atlas robot at CES 2026 - Engadget](https://www.engadget.com/big-tech/boston-dynamics-unveils-production-ready-version-of-atlas-robot-at-ces-2026-234047882.html)
92. [Boston Dynamics Atlas Robot: Price, Specs & Can You Buy One?](https://blog.robozaps.com/b/boston-dynamics-atlas-review)
93. [Gemini Robotics](https://en.wikipedia.org/wiki/Gemini_Robotics)
94. [Nvidia-Backed Robotics Startup Generalist AI Valued at \$2 Billion - Bloomberg](https://www.bloomberg.com/news/articles/2026-06-04/nvidia-backed-robotics-startup-generalist-ai-valued-at-2-billion)
95. [NEURA Raises Up to \$1.4 Billion in Largest Humanoid Round](https://www.implicator.ai/neura-raises-up-to-1-4-billion-as-humanoid-funding-outruns-robot-revenue/)
96. [Generalist AI raises \$400 million to accelerate development of robot foundation models](https://roboticsandautomationnews.com/2026/06/05/generalist-ai-raises-400-million-to-scale-robot-intelligence-platform/102307/)
97. [Generalist AI to Raise a New Funding Round at a \$3 Billion Valuation](https://siliconvalleyinvestclub.com/2026/07/30/generalist-ai-to-raise-a-new-funding-round-at-a-3-billion-valuation/)
98. [Generalist AI Raised \$400M to Put an AI Foundation Model Inside Robots](https://www.humphreytheodore.com/writing/generalist-ai-robotics-foundation-model-2b-2026)
99. [Genesis AI - 2026 Company Profile, Team, Funding & Competitors - Tracxn](https://tracxn.com/d/companies/genesis-ai/__ElX8vCbm0IkpzgXTiDtwa9nLi1JUwNSN3zY03pjL-Fg)
100. [Robotics Startup Genesis in Talks to Raise at \$3 Billion Valuation - Bloomberg](https://www.bloomberg.com/news/articles/2026-07-23/robotics-startup-genesis-in-talks-to-raise-about-500-million)
101. [Genesis AI in Talks to Raise \$500M at \$3B Valuation](https://valueaddvc.com/pulse/genesis-ai-500m-robotics-3b-valuation-2026)
102. [深度拆解宇树科技招股书：一年营收17亿，宇树机器人都卖给了谁？ - 经济观察网 － 专业财经新闻网站](https://www.eeo.com.cn/2026/0320/813654.shtml)
103. [宇树科技IPO过会 A股将迎“具身智能第一股”-新华网](http://www.xinhuanet.com/tech/20260602/e042e10266944c2dbd55a27684b5e5b1/c.html)
104. [宇树科技，8月19日上市](https://www.cls.cn/detail/2456358)
105. [宇树科技将于8月19日科创板上市\_新浪财经\_新浪网](https://finance.sina.com.cn/jjxw/2026-08-18/doc-ininsfpx9860006.shtml)
106. [人形机器人公司智元创新启动赴港上市流程-电子工程专辑](https://www.eet-china.com/news/202607275399.html)
107. [智元已启动港股上市流程，机器人资本竞速 - 知乎](https://zhuanlan.zhihu.com/p/2064839519426425748)
108. [智元机器人启动港股上市，投资人称目标估值400亿至500亿港元\_新浪财经\_新浪网](https://finance.sina.com.cn/wm/2026-07-25/doc-iniiyptt1420151.shtml)
109. [两个“世界第一”打到交易所，智元要和宇树争400亿身价-虎嗅网](https://www.huxiu.com/article/4879097.html)
110. [智元最新估值500亿，IPO暂缓，具身智能开始“挤泡沫”|ipo|机器人|新材|上市\_网易科技](https://www.163.com/tech/article/L9CR3I1D00098IEO.html)
111. [银河通用遭同行“点名”质疑，公司成立三年融资70亿元，资本化进程受关注|上市|机器人|订单服务期限\_网易订阅](https://www.163.com/dy/article/L7EEG8HO05568W0A.html)
112. [融资最多的机器人公司，一年卖出了150台-钛媒体官方网站](https://www.tmtpost.com/8020648.html)
113. [机器人公司星动纪元估值破百亿 创始人称量产是小批量](https://m.caixin.com/m/2026-03-05/102419654.html)
114. [银河通用再融25亿元 称是估值最高未上市机器人公司](https://m.caixin.com/m/2026-03-02/102418619.html)
115. [首批数百台“亮剑集结”，优必选全尺寸工业人形机器人 Walker S2 量产交付 - IT之家](https://www.ithome.com/0/897/076.htm)
116. [耗资16亿！优必选上演H吃A，补齐制造拼图](https://eu.36kr.com/zh/p/3618094353036040)
117. [优必选2026年年后新订单落地全览（截至2026年2月13日）优必选在2026年\_财富号\_东方财富网](https://caifuhao.eastmoney.com/news/20260213144625435243740)
118. [5000万元“机器人+大模型”订单落锤！优必选Walker S2年内交付](https://news.aibase.com/zh/news/23538)
119. [小鹏IRON人形机器人试生产启动，量产倒计时|小鹏|机器人|何小鹏\_新浪新闻](https://www.sina.cn/news/article/niiyimn9174637.html)
120. [小鹏机器人自己走下产线，人形机器人竞赛来到“量产关”](https://www.guancha.cn/qiche/2026_09_08_830474.shtml)
121. [小鹏机器人完成总装，2027 上半年交付，能记住你的对话|小鹏汽车|人形机器人|巴黎车展|小鹏iron\_新浪新闻](https://www.sina.cn/weibo/detail/5353315888008559.html)
122. [小鹏人形机器人，明年全球推出！\_新浪财经\_新浪网](https://finance.sina.com.cn/wm/2026-07-19/doc-iniiktnr3169641.shtml)
123. [人形机器人商业化元年来了？小米机器人进厂拧螺丝，小鹏人形机器人年底量产|机器人\_新浪财经\_新浪网](https://finance.sina.com.cn/wm/2026-03-03/doc-inhpsxzq4703222.shtml)
124. [自变量机器人 - 人形机器人公司资料、融资、产品与估值](https://www.robothub.app/zh/companies/x-square-robot)
125. [自变量机器人两月双融资估值超百亿元 创始人谈中美技术差距](https://m.caixin.com/m/2026-02-25/102416985.html)
126. [具身智能开年最大融资，字节红杉领投10亿](https://www.qbitai.com/2026/01/369147.html)
127. [自变量机器人再获数亿元新融资，1个月内吸金十几亿|机器人\_新浪财经\_新浪网](https://finance.sina.com.cn/wm/2026-02-26/doc-inhpcush7264694.shtml)
128. [深圳机器人新秀，忙着插花叠衣服，拿下20亿元融资！ - 21财经](https://m.21jingji.com/article/20260422/herald/1971e8ec4867219ba253a3c76c4bca47.html)
129. [2年估值破100亿，千寻智能却不敢松口气|机器人\_新浪财经\_新浪网](https://finance.sina.com.cn/stock/t/2026-03-02/doc-inhpqvan8248575.shtml)
130. [融资20亿，估值破百亿，成立仅2年的千寻智能凭什么杀出重围？-太平洋科技](https://www.pconline.com.cn/focus/2102/21025412.html)
131. [千寻智能宣布完成新一轮10亿融资：顺为与云锋基金联合领投\_创事记\_新浪科技\_新浪网](https://finance.sina.com.cn/tech/csj/2026-04-07/doc-inhtryta3632295.shtml)
132. [机器人公司千寻智能完成近20亿融资 估值超百亿\_公司频道\_财新网](https://companies.caixin.com/2026-02-24/102416440.html)
133. [投资人疯抢千寻智能，3个月融资50亿元！具身模型力压英伟达|智能\_新浪财经\_新浪网](https://finance.sina.com.cn/wm/2026-06-03/doc-iniacxkk4007887.shtml)
134. [100亿，机器人第一梯队新门槛\_投资界](https://news.pedaily.cn/202603/561347.shtml)
135. [千寻智能再获10亿元融资，30天累计融资30亿加速具身模型全球竞争\_腾讯新闻](https://news.qq.com/rain/a/20260407A02U9700)
136. [环球老虎财经-A股24小时快讯，专业权威的原创金融投资分析平台](https://www.laohucaijing.com/Www_detail/index/150464/)
137. [星海图获20亿融资估值破200亿，具身智能百亿俱乐部扩至9家|融资\_新浪财经\_新浪网](https://finance.sina.com.cn/roll/2026-04-02/doc-inhtavkc4453641.shtml)
138. [星海图据报已秘密递表港交所，蚂蚁、美团、高瓴集体站台|融资|机器人|知名企业\_网易订阅](https://www.163.com/dy/article/L6EVAITM0519VPHD.html)
139. [对话星海图创始人高继扬：具身智能无瞬间拐点 坚持用真实数据\_新浪财经\_新浪网](https://finance.sina.com.cn/roll/2026-08-23/doc-iniphhay2631989.shtml)
140. [百亿估值之上，第一阵营格局初定...... - 知乎](https://zhuanlan.zhihu.com/p/2016093781372448930)
141. [机器人公司星海图再获20亿元融资估值超200亿元 - 财新](https://m.caixin.com/m/2026-04-02/102430120.html)
142. [具身智能公司星海图完成10亿元B轮融资\_公司频道\_财新网](https://companies.caixin.com/2026-02-11/102413493.html)
143. [星海图又融资20亿，估值突破200亿！ - NE时代](https://www.ne-time.cn/web/article/38356)
144. [星动纪元再获10亿元融资，估值突破百亿元\_腾讯新闻](https://news.qq.com/rain/a/20260305A03JGT00)
145. [星动纪元完成新一轮10亿元融资，2026年来累计融资近50亿\_机器人\_公司\_智能](https://www.sohu.com/a/1046500229_130887)
146. [星动纪元完成新一轮10亿元融资，2026年来累计融资近50亿|人形|机器人\_网易订阅](https://www.163.com/dy/article/L15N8ODO05198NMR.html)
147. [顺丰红杉IDG联手，星动纪元融资2亿美金](https://m.thepaper.cn/newsDetail_forward_33060590)
148. [星动纪元完成新一轮10亿元融资，2026年来累计融资近50亿\_新浪财经\_新浪网](https://finance.sina.com.cn/roll/2026-07-06/doc-inifwfpu1875055.shtml)
149. [2026具身智能独角兽企业融资情况：从百亿俱乐部到港股IPO的资本竞赛全景 - IT之家](https://www.ithome.com/0/968/269.htm)
150. [逐际动力完成近2亿美元Pre-IPO融资估值150亿元人民币 - 财新](https://m.caixin.com/m/2026-07-14/102464079.html)
151. [半年融资4亿美金、估值150亿 逐际动力冲刺IPO\_新浪财经\_新浪网](https://finance.sina.com.cn/jjxw/2026-07-17/doc-iniianxe7441848.shtml)
152. [哈工大学子创业机器人，做出一个IPO\_新浪科技\_新浪网](https://finance.sina.com.cn/tech/roll/2026-06-17/doc-inictnur5963921.shtml)
153. [首家第四套标准！乐聚智能创业板IPO获受理，拟募资26亿元，腾讯、深创投为股东\_新浪财经\_新浪网](https://finance.sina.com.cn/wm/2026-05-20/doc-inhypaep9452101.shtml)
154. [本体厂的野心：拆解乐聚机器人对外投资，看懂人形机器人赛道的“生态卡位”战 - 搜狐时间线](https://timeline.sohu.com/news/B9nTH1Gl4O)
155. [乐聚智能IPO申请获受理，机器人板块迎来密集催化。-虎嗅网](https://www.huxiu.com/moment/1246529.html)
156. [哈工大同学带队，乐聚机器人要IPO了 - 21经济网](https://www.21jingji.com/article/20260508/herald/24c26da1601fcf6309583cd203dfd165.html)
157. [为人形机器人穿上“新衣” 这家上市公司3亿元投向傅利叶](https://www.cls.cn/detail/2042476)
158. [傅利叶（Fourier） · Series D+ — RobotScope](https://robotscope.net/companies/fourier-intelligence/)
159. [傅里叶有没有IPO计划？谢谢！傅利叶智能IPO计划：已有明确上市规划，预计202\_财富号\_东方财富网](https://caifuhao.eastmoney.com/news/20251123210435656165930)
160. [傅利叶完成近8亿元E轮系列融资](https://www.yicai.com/news/102430454.html)
161. [千寻智能30天融资30亿元 马云、雷军旗下公司联合领投-经济参考网 \_ 新华社《经济参考报》官方网站](https://www.jjckb.cn/20260410/8f978f88dc76476db9f5d2430e66934d/c.html)
162. [灵心巧手完成近15亿元B轮融资 目标在2026年实现5万—10万台灵巧手交付规模|机器人|b轮融资\_网易订阅](https://www.163.com/dy/article/KLJE9KC2053469RG.html)
163. [灵心巧手目标估值冲刺60亿美元，一家公司估值已超2030年全球灵巧手市场规模\_凤凰网](https://i.ifeng.com/c/8vsuVtEs1la)
164. [具身智能持续火热 北京灵心巧手2个月内连融2轮|融资\_新浪财经\_新浪网](https://finance.sina.com.cn/jjxw/2026-05-01/doc-inhwkimm6730040.shtml)
165. [因时机器人完成数亿元C1轮及C2轮融资 - NE时代](https://ne-time.cn/web/article/37972)
166. [资讯 l 华沿机器人（1021.HK）港股上市、因时机器人推出全新小尺寸灵巧手、灵猴机器人完成数亿元B轮融资 - 艾邦机器人](https://www.aibangbots.com/a/8062)
167. [因时机器人 · Series C — RobotScope](https://robotscope.net/companies/yinshi-robotics/)
168. [机器人灵巧手公司因时机器人完成数亿元C1轮及C2轮融资|机器人\_新浪财经\_新浪网](https://finance.sina.com.cn/wm/2026-02-27/doc-inhphuuy3414142.shtml)
169. [因时机器人：机器人产品、融资与商业进展](https://www.roboatlas.ai/zh-CN/companies/inspire-robots)
170. [BrainCo强脑科技](https://pitchhub.36kr.com/project/1744027642944386)
171. [2026年第一季度中国医疗器械领域融资大案盘点：脑机接口成吸金热门，神经介入、可吸收材料领域持续火热\_财富号\_东方财富网](https://caifuhao.eastmoney.com/news/20260416183733297624050)
172. [强脑科技拟赴港IPO，脑机接口商业化前景如何？ - 21经济网](https://www.21jingji.com/article/20260126/herald/b9f6662edb0bc0893877078e97e7b85b.html)
173. [曝强脑科技秘密提交港股IPO申请 刚完成近20亿元融资\_宇树\_接口\_投资方](https://www.sohu.com/a/975181101_115831)
174. [消息称BrainCo秘密申请香港IPO，或成“杭州六小龙”首家上市企业 - 动点科技](https://cn.technode.com/post/2026-01-13/brainco-confidential-hk-ipo-filing/)
175. [截至2026年5月14日，强脑科技（BrainCo）港股IPO仍处于审核冲刺阶段\_财富号\_东方财富网](https://caifuhao.eastmoney.com/news/20260519122735974934550)
176. [Neura Robotics](https://en.wikipedia.org/wiki/Neura_Robotics)
177. [AI Robot Startup Neura Robotics Valued at €4 Billion After Tether Investment - Bloomberg](https://www.bloomberg.com/news/articles/2026-03-04/neura-robotics-raising-1-billion-in-round-backed-by-tether)
178. [Humanoid Raises \$152 Million At \$1.35 Billion Valuation: Europe’s Newest Robot Unicorn](https://www.forbes.com/sites/johnkoetsier/2026/07/21/humanoid-raises-152-million-at-135-billion-valuation-europes-newest-robot-unicorn/)
179. [UK's Humanoid Raises \$152M, Becomes a \$1.35B Robotics Unicorn](https://valueaddvc.com/pulse/humanoid-152m-series-a-robotics-2026)
180. [Figure AI: Robots Now Outnumber Humans at the Company 2026](https://explainx.ai/blog/figure-ai-robots-outnumber-humans-milestone-2026)