# 全球具身智能技术路线演进与核心企业全景研究报告（2026）

## 产业演进格局：从单点技术验证迈向VLA收敛与场景规模化拐点

2025年至2026年，全球具身智能（Embodied AI）与人形机器人产业正式跨越了早期实验室原型演示的萌芽阶段，进入从“技术验证”向“真实场景生产力落地”转型的历史性拐点 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。在算法范式层面，早年将高层任务规划、中层轨迹生成与底层全身运动控制割裂开发的模块化流水线架构，正加速向视觉-语言-动作（Vision-Language-Action, VLA）统一大模型、大行为模型（Large Behavior Models, LBM）以及物理世界基础模型（World Foundation Models）收敛 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。机器人获取运动与操作技能的核心方式，已从依赖高级工程师编写硬编码规则与显式运动学方程，全面转向基于强化学习（Reinforcement Learning）、模仿学习（Imitation Learning）与大规模物理仿真的端到端数据驱动范式 [3](https://www.tri.global/news/ai-powered-robot-boston-dynamics-and-toyota-research-institute-takes-key-step-towards-general)。

伴随技术范式的演进，全球商业化与资本版图在2026年呈现出剧烈的结构性分化与头部集聚效应 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。一方面，全球风险投资在2026年前三季度向人形机器人与具身智能初创企业注资已突破110亿至188亿美元，远超2025年全年48亿美元的历史纪录，其中中国市场贡献了全球近三分之二的融资份额，产业总规模在2025年达到9,150亿元人民币并在2026年突破万亿元大关 [6](https://dealroom.co/news/125782-apptronik-raises-520m-at-5-5b-valuation-to-scale-humanoid-robot-apollo/)；另一方面，过去一年全球已有超过20家缺乏核心造血能力或技术护城河的机器人企业遭遇破产清算或业务剥离，行业在“百亿估值独角兽集群崛起”与“商业化伪需求出清”的双重张力下加速洗牌 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。

审视当前全球头部玩家的技术架构与商业逻辑，具身智能的演进路径主要分化为四大核心流派：其一是以Physical Intelligence、Skild AI、Google DeepMind及NVIDIA为代表的跨本体通用具身大模型与世界模型路线（水平赋能层），致力于构建不绑定单一硬件的“机器人通用大脑”与底层训练基建 [4](https://exponentialindustry.com/ontology/physical-ai-robotics/)；其二是以Figure AI、Tesla、1X Technologies及智元机器人为代表的软硬一体全栈垂直整合端到端VLA路线，主张通过自有硬件本体、专用算力与自建产线构建封闭的数据飞轮 [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)；其三是以银河通用为代表的仿真合成数据驱动与“手眼脑”端到端协同路线，利用百亿级物理合成数据破解真机数据匮乏瓶颈，并以务实构型切入工业与零售场景 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)；其四是以宇树科技、波士顿动力（Boston Dynamics）、Apptronik、优必选、逐际动力及星尘智能为代表的高动态本体运控筑底与大行为模型渐进融合路线，凭借卓越的机电执行器、模型预测控制（MPC）与强化学习运控实现量产交付，再通过内生研发或外部生态耦合补齐高层认知能力 [16](https://www.huxiu.com/article/4884048.html)。

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

### 全球具身智能四大核心技术路线架构与数据闭环范式

[figure]

全球具身智能技术架构已分化为四大演进路径：**水平跨本体大模型层** 致力于通过统一VLA策略驱动异构硬件；**全栈垂直整合路线** 通过自有本体与端到端神经网络构建物理数据飞轮；**虚实融合路线** 依赖大规模物理仿真合成数据打通手眼脑协同；**高动态运控筑底路线** 则以强化学习小脑与高性能机电本体为基础向上融合大模型。

<!-- /figure 1 -->

这四大技术路线的分化，本质上源于产业界对具身智能第一性原理的不同解答：究竟应当先通过海量异构数据训练出具备泛化能力的“通用物理大脑”，还是必须通过特定硬件构型的规模化制造与部署来采集高质量同构真机数据？下表从核心技术机制、数据获取范式、核心优势与当前工程瓶颈四个维度，对全球四大主流技术路线进行了系统性解构。

| 技术路线分类 | 核心架构与算法机制 | 数据获取与训练范式 | 核心竞争壁垒 | 关键落地瓶颈 | 代表性企业/机构 |
| --- | --- | --- | --- | --- | --- |
| **路线一：跨本体通用具身大模型与世界模型（水平赋能层）** | 跨本体VLA架构、流匹配（Flow Matching）动作生成、云端具身推理（ER）+端侧轻量化适配、物理世界基础模型 | 跨构型开源与合作真机数据、第一视角人类视频迁移（Egocentric Video）、物理规则对齐的生成式合成视频 | 强泛化性与组合泛化能力；极高的顶尖AI学者密度；避免重资产硬件制造风险，具备软件级高毛利潜力 | 缺乏自有硬件部署场景导致闭环真机长尾数据获取受制于人；端侧算力受限下高自由度高频控制精度挑战 | Physical Intelligence (π\pi)、Skild AI、Google DeepMind、NVIDIA [4](https://exponentialindustry.com/ontology/physical-ai-robotics/) |
| **路线二：软硬一体全栈垂直整合端到端VLA路线** | 专有端到端VLA神经网络（直接从多目视觉像素映射至底层关节电机指令）、自研推理芯片、世界动作模型 | 自有工厂与客户产线规模化部署车队（Fleet Learning）、高强度人工遥操作示范与纠偏 | 软硬件深度耦合优化响应延迟；自有产线实现车规级供应链降本；闭环数据飞轮构筑极高壁垒 | 资本开支（CapEx）极其庞大；双足全身控制在非结构化场景的节拍速度与可靠性仍待提升 | Figure AI、Tesla (Optimus)、1X Technologies、智元机器人 (AgiBot) [4](https://exponentialindustry.com/ontology/physical-ai-robotics/) |
| **路线三：仿真合成数据驱动与“手眼脑”协同路线** | 打通高层多模态感知规划（大脑）、全身运动控制（小脑）与末端灵巧操作（神经控制）的端到端大模型 | 高精度物理仿真合成数据为主（百亿级规模遍历极端工况）+ 极少量真机数据微调（Sim-to-Real） | 彻底摆脱对大规模人工遥操作的依赖，训练效率成倍提升；轮式双臂与重载本体实现极高商业交付成功率 | 复杂柔性物体与高接触力控任务中的仿真到真实世界差距（Sim-to-Real Gap）仍需真机数据持续校准 | 银河通用 (Galbot) [1](https://caifuhao.eastmoney.com/news/20260305164448808529560) |
| **路线四：高动态本体运控筑底与大行为模型融合路线** | 模型预测控制（MPC）+ 深度强化学习（RL）全身动态控制、一体化高扭矩关节/绳驱传动，外挂或内嵌LBM/VLA | 物理引擎强化学习高频试错、动作捕捉重定向、遥操作示范与数字孪生协同训练 | 极致的本体运动爆发力、抗干扰鲁棒性与硬件成本控制能力；率先实现数千台级商业化出货与财务盈利 | 早期重“运动表演”轻“灵巧作业”，从高校科研/商演市场向工业严肃生产力转化面临大脑认知短板 | 宇树科技、Boston Dynamics & TRI、Apptronik、优必选、逐际动力、星尘智能 [16](https://www.huxiu.com/article/4884048.html) |

## 路线一：跨本体通用具身大模型与物理世界模型路线（水平赋能层）

水平赋能层路线的核心战略假设是：随着人形与特种机器人硬件本体的快速成熟与同质化，硬件制造本身将逐步演变为低毛利的供应链竞争，而真正能够攫取产业最丰厚利润与持久垄断价值的，是能够驱动任意形态机器人的“通用基础模型层”（General-Purpose Foundation Model Layer） [12](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)。这一阵营的企业不直接涉足重资产的机器人整机量产，而是通过算法架构创新与大规模异构数据预训练，向全球硬件制造商输出“即插即用”的具身智能大脑 [12](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)。

### Physical Intelligence：流匹配架构与在线强化学习驱动的跨本体VLA先锋

Physical Intelligence（简称 π\pi 或 PI）是全球“单一模型驱动所有机器人”（One Model for All Robots）理论最纯粹的技术标杆 [11](https://www.roboticscenter.ai/companies/physical-intelligence)。在技术路径上，公司摒弃了传统自回归离散Token预测在连续高频机器人控制中的局限，在其旗舰跨本体视觉-语言-动作模型 π0\pi_0 中开创性地引入了流匹配（Flow Matching）生成式建模技术，将预训练视觉语言模型（VLM）的语义表征与连续动作生成深度结合，使单一模型能够输出高频平滑的关节控制指令，跨平台控制涵盖单臂、双臂及移动操作机器人在内的5种以上异构硬件平台 [11](https://www.roboticscenter.ai/companies/physical-intelligence)。进入2025年末至2026年上半年，Physical Intelligence的技术迭代呈现出清晰的“后训练与自主进化”脉络：2025年11月发布的 π0.6∗\pi^*_{0.6} 引入了名为 Recap 的强化学习方法，将专家演示、遥操作员实时纠偏与机器人自主练习相结合，在叠衣服与意式浓缩咖啡制作等复杂长程任务中将作业吞吐量提升了约一倍 [21](https://www.humanoidsdaily.com/companies/physical-intelligence)；2025年12月，团队证实了规模化预训练模型具备从无专用采集设备的第一视角人类视频（Egocentric Human Video）中直接迁移学习机器人动作的“涌现能力” [21](https://www.humanoidsdaily.com/companies/physical-intelligence)；2026年3月，公司先后推出多尺度具身记忆（Multi-Scale Embodied Memory, MEM）与 RL Tokens 技术，前者将短期视频记忆与长期自然语言摘要配对，使机器人能够维持超过10至15分钟的超长程复杂任务而不遗忘步骤，后者则从VLA模型中提取特征Token训练轻量级Actor-Critic网络，仅需数小时数据即可在接触密集型（Contact-rich）任务中实现毫米级在线强化学习精度 [21](https://www.humanoidsdaily.com/companies/physical-intelligence)；2026年4月发布的 π0.7\pi_{0.7} 更首次验证了“组合泛化”（Compositional Generalization）能力，能够指挥从未在特定硬件与任务组合上训练过的双臂UR5e系统完成复杂的洗衣房协作任务 [21](https://www.humanoidsdaily.com/companies/physical-intelligence)。

在产品与商业化进度方面，Physical Intelligence采取了“优先攻克底层研究、审慎推进商业化”的策略，将自身定位为第三方硬件的“物理智能插件层”（Physical Intelligence Layer） [21](https://www.humanoidsdaily.com/companies/physical-intelligence)。2025年12月，其微调版 π0.6\pi_{0.6} 模型在涵盖洗刷油腻平底锅、开挂锁等高难度日常操作基准的“机器人奥林匹克”（Robot Olympics）评测中斩获五项大类中的三项金牌级成绩 [21](https://www.humanoidsdaily.com/companies/physical-intelligence)。2025年4月，公司与中国具身智能头部企业智元机器人（AgiBot）达成研究合作，展示了单一策略跨不同灵巧手与相机配置完成模特系围巾等多任务控制 [21](https://www.humanoidsdaily.com/companies/physical-intelligence)；2026年2月，公司首次公布了与家庭洗衣折叠机器人公司Weave Robotics及工业包装自动化企业Ultra Robotics（该公司融资6,200万美元并与PI深度绑定）的真实场景部署运行数据，拉开了机器人控制“API化”的序幕，但截至2026年第三季度尚未披露规模化企业级收入数据 [12](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)。

在融资与团队情况方面，Physical Intelligence于2024年初在旧金山成立，组建了全球机器人学习领域学术声誉最顶尖的七人联合创始人团队：首席执行官Karol Hausman曾任Google DeepMind资深研究科学家，深耕强化学习与Sim-to-Real迁移；总裁Lachy Groom为前Stripe高管，全面负责商业战略与资本运作；联创团队更汇聚了UC Berkeley教授Sergey Levine、Stanford教授Chelsea Finn以及Brian Ichter、Adnan Esmail、Quan Vuong等奠定现代模仿学习、元学习与机器人基础模型基石的学术泰斗，员工规模已扩展至约150至200人 [11](https://www.roboticscenter.ai/companies/physical-intelligence)。资本市场上，公司于2024年3月完成由Thrive Capital、Khosla Ventures与Lux Capital领投的7,000万美元种子轮（创下当时机器人领域最大种子轮纪录） [11](https://www.roboticscenter.ai/companies/physical-intelligence)；2024年11月完成由Jeff Bezos、OpenAI、Thrive Capital与Bond等参投的4亿美元A轮融资，估值达24亿至28亿美元 [11](https://www.roboticscenter.ai/companies/physical-intelligence)；2025年11月，公司完成由Alphabet旗下增长基金CapitalG领投、Lux Capital、NVentures（英伟达）、Index Ventures、T. Rowe Price及Redpoint参投的6亿美元B轮融资，确认投后估值跃升至56亿美元，累计披露融资额达10.7亿至11亿美元 [12](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)。2026年3月，市场传出其正与Founders Fund及Lightspeed洽谈新一轮10亿美元融资，拟议估值高达110亿美元以上 [12](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)。

### Skild AI：全向跨本体工业大脑与高通量商业化破局者

与Physical Intelligence偏重前沿学术探索与灵巧家务演示不同，同样定位于“不造硬件、只造大脑”的Skild AI采取了极其凌厉的工业与企业级商业化落地策略 [12](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)。在技术路径与产品进度上，Skild AI致力于构建全球首个全向跨本体（Omni-bodied）通用机器人基础模型 Skild Brain，其单一大脑架构能够同时适配四足巡检机器人、双足人形机器人以及工业机械臂，具备极强的物理环境自适应与高可靠操作能力 [4](https://exponentialindustry.com/ontology/physical-ai-robotics/)。

在商业化进度上，Skild AI创造了全球纯软件具身大模型赛道的商业化标杆：除了直接收购斑马技术（Zebra Technologies）旗下的机器人自动化业务以打通工业渠道外，截至2026年9月10日，Skild AI在完成首次商业部署后仅用时10个月，其年度经常性收入（ARR）便正式突破1亿美元大关，在全球超过60个客户现场实现了规模化落地，核心应用场景涵盖富士康（Foxconn）产线上的NVIDIA Blackwell服务器机柜组装操作、住友电工（Sumitomo）复杂的汽车线束柔顺装配，以及三井物产（Mitsui）商业厨房自动化作业 [4](https://exponentialindustry.com/ontology/physical-ai-robotics/)。

在团队与融资情况方面，Skild AI由卡内基梅隆大学（CMU）著名机器人与计算机视觉学者Deepak Pathak与Abhinav Gupta联合创立 [31](https://www.skild.ai/blogs)。公司于2024年7月完成由Lightspeed、Coatue、软银（SoftBank）及Jeff Bezos领投的3亿美元A轮融资 [31](https://www.skild.ai/blogs)；2026年1月14日，Skild AI宣布完成由软银领投，三星（Samsung）、LG、施耐德电气（Schneider Electric）及Salesforce Ventures等产业巨头参投的14亿美元C轮融资，投后估值超过140亿美元，约合Physical Intelligence已确认估值的2.5倍，稳居全球纯软件具身智能大模型估值榜首 [12](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)。

### Google DeepMind与NVIDIA：云边协同推理体系与物理AI底层算力基建

在初创独角兽之外，科技巨头Google DeepMind与NVIDIA正从“模型API平台”与“全栈仿真算力底座”两个维度塑造水平赋能层的行业标准 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。

Google DeepMind由机器人副总裁Carolina Parada及Steven Hansen、Peng Xu等核心学者领衔，明确选择了不参与人形本体硬件制造、专注于向全球硬件伙伴提供底层智能的平台化路线 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。继2025年3月首发Gemini Robotics及具身推理模型ER、2025年6月推出端侧版On-Device、2025年9月与2026年4月迭代1.5与ER 1.6版本后，DeepMind于2026年7月30日正式发布了里程碑式的 Gemini Robotics 2 模型家族 [33](https://en.wikipedia.org/wiki/Gemini_Robotics)。该体系并非单一庞大模型，而是由三个各司其职的模型构成的协同系统 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。其中，旗舰视觉-语言-动作模型 Gemini Robotics 2 (VLA) 首次将控制范围从2025年仅限上半身桌面操作扩展至全身控制（Whole-Body Control，“从脚趾到指尖”），通过单一学习策略同步协调人形机器人的双腿步态、躯干平衡、双臂延展与22自由度五指灵巧手（如SharpaWave、Inspire灵巧手或Franka平行夹爪），可完成弯腰、下蹲、拧灯泡、打结与封口拉链袋等精细动作 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。与之配合的高层大脑 Gemini Robotics ER 2 是基于Gemini 3.5 Flash架构构建的具身推理（Embodied Reasoning）模型，拥有128k上下文窗口，支持图文、视频与音频交错输入，负责多步骤长程任务规划、人类自然语言交互、工具调用、多机异构协作（如轮式机器人与双足人形机器人分工配合）以及基于ASIMOV-Agentic基准的安全驻停调度 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。而在边缘执行端，基于Gemma架构优化的本地化端侧轻量级模型 Gemini Robotics On-Device 2 无需云端网络连接即可运行，仅需不到200个演示样本与数小时训练即可快速迁移适配全新的双臂机器人构型 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。目前，Gemini Robotics ER 2已通过Google AI Studio与Gemini API向开发者全面开放，而全身VLA模型则定向赋能Apptronik（Apollo 2）、Boston Dynamics、Agility Robotics、Agile Robots及Franka等战略合作伙伴 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。不过，DeepMind披露的真实基准测试亦揭示了当前VLA在物理世界的局限：在Apollo 2上测试的五项精细手部任务中，拧下灯泡成功率达92%，但将灯泡重新拧入仅得36%，将垃圾扫入簸箕成功率仅为32%，且动作速度与端侧高自由度泛化能力仍有待提升 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。

NVIDIA则通过构建“物理AI”（Physical AI）全栈基础设施，扮演着全球具身智能“卖水人”与生态中枢的角色，其机器人研发团队包括Yuke Zhu等知名学者 [32](https://developer.nvidia.com/isaac)。NVIDIA的技术矩阵由三大核心支柱组成：首先是2025年1月发布并持续迭代至Cosmos 3 Edge的物理世界基础模型平台 NVIDIA Cosmos，该平台结合扩散模型（Diffusion）与自回归模型（Autoregressive）及专用物理Tokenizer，能够生成高度符合牛顿物理定律的合成视频以加速机器人策略训练 [4](https://exponentialindustry.com/ontology/physical-ai-robotics/)；其次是开源人形机器人基础模型项目 Project GR00T（已演进至GR00T N1、N1.5、N1.6版本，并在最新迭代中采用基于Qwen3-VL架构的Cosmos-Reason2-2B作为新型VLM骨干网络），配合HOVER全身控制器、基于Omniverse的 Isaac Sim / Isaac Lab 物理仿真环境以及 GR00T-Mimic / GR00T-Dreams 合成数据管线，帮助开发者弥补全球仅约30万小时真机操作数据的缺口 [5](https://medium.com/cathay-innovation/the-industrialization-of-embodied-robotic-intelligence-6d54374ed8f3)；最后是端侧算力硬件 Jetson Thor（提供高达800 TFLOPS的8位浮点Tensor算力）与云原生工作流编排平台 NVIDIA OSMO [4](https://exponentialindustry.com/ontology/physical-ai-robotics/)。与此同时，NVIDIA通过旗下风投机构NVentures大举投资Figure AI与Physical Intelligence等头部玩家，形成了“算力销售+软件生态绑定+资本卡位”的闭环统治力 [30](https://techfundingnews.com/physical-intelligence-1b-raise-11b-valuation-founders-fund-lightspeed/)。

## 路线二：软硬一体全栈垂直整合与端到端VLA闭环路线

与水平赋能层截然相反，全栈垂直整合路线的信奉者认为，通用具身智能在真实物理世界中的落地瓶颈在于硬件构型、传感器布局、底层执行器响应特性与神经网络控制策略之间的强耦合关系 [46](https://tsginvest.com/figure-ai/)。第三方通用大模型无法针对特定本体的动力学极限进行极致优化，唯有将本体设计、核心关节制造、端到端VLA大模型研发乃至量产代工产线全部收归自有，通过规模化部署同构机器人车队采集数万至数百万小时的同构物理交互数据，才能真正跑通具身智能的“规模法则”（Scaling Laws）与成本曲线 [4](https://exponentialindustry.com/ontology/physical-ai-robotics/)。

### Figure AI：全自研Helix架构、十万卡算力与BotQ产线构筑的工业人形霸主

Figure AI是全球软硬一体垂直整合路线估值最高、动作最激进的代表企业 [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)。在技术路径上，公司经历了重大的战略转折：早期Figure曾与OpenAI合作开发机器人语音与高层推理能力，但于2025年2月正式终止了与OpenAI的合作关系，首席执行官Brett Adcock明确指出“要在真实世界规模化解决具身AI问题，必须实现机器人AI的完全垂直整合” [46](https://tsginvest.com/figure-ai/)。随后，Figure推出了全自研端到端视觉-语言-动作神经网络平台 Helix VLA，该网络直接融合感知、推理与全身控制，使机器人能够零样本抓取几乎任何从未见过的小型家居与工业物品，并支持两台人形机器人之间的自主协同作业 [46](https://tsginvest.com/figure-ai/)。为支撑Helix模型的算力需求，Figure于2026年9月与AI云基础设施提供商Nscale签署了价值高达35亿美元的战略合作协议（Nscale亦对Figure进行了战略投资），部署多达10万块NVIDIA GPU用于端到端具身模型训练 [44](https://sacra.com/c/figure-ai/)。

在产品与商业化进度上，Figure的迭代速度领跑北美同行：继初代Figure 01与2025年在宝马工厂投入商用的Figure 02之后，公司于2025年10月正式发布第三代旗舰通用人形机器人 Figure 03（身高约1.73米/5英尺8英寸，体重约61公斤/135磅，配备16自由度灵巧手，单次续航约5小时，兼顾工业车间与未来家庭场景） [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)。2026年3月，Figure机器人在受控测试中展示了擦拭、清扫、刷洗、拖地、吸尘、除尘、抛光与整理等8项自主清洁技能，并于2026年3月25日在白宫面向45国代表的峰会上公开展示 [48](https://www.useluminix.com/reports/company-overviews/figure-robotics-company-overview-may-2026/source/0)。在制造端，公司自建了名为 BotQ 的专属人形机器人制造基地，首期规划年产能1.2万台，目标在未来四年内累计出货10万台 [46](https://tsginvest.com/figure-ai/)。商业化方面，公司自2025年1月起实现商业营收，Figure 03已于2026年6月在宝马（BMW）斯帕坦堡工厂产线上全面接替Figure 02执行端到端汽车制造任务 [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)；2026年6月，公司与零售巨头Catalyst Brands（JCPenney母公司）签署了价值4,000万美元的自动化部署合同，同时正切入规模达351亿美元的包装机器人市场，并与UPS开展物流场景探索性测试 [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)。尤为关键的运营指标是，2026年6月20日，Figure宣布其部署运行的机器人数量（约740台）首次超越了公司人类员工总数（约660人），标志着其内部数据与生产飞轮进入正向自加速区间 [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)。不过，前员工Gruendel提起的吹哨人安全诉讼截至2026年年中仍在联邦法院处于证据开示阶段，凸显出人形机器人从封闭工厂迈向家庭场景所面临的严峻合规与责任风险 [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)。

在团队与融资情况方面，Figure AI由知名连续创业者Brett Adcock于2022年5月在加州圣何塞/桑尼维尔创立（Adcock此前曾创立招聘平台Vettery并以1.1亿美元售予德科集团，后联合创立电动垂直起降航空企业Archer Aviation并推动其上市，2025年底又创立消费级AI硬件公司Hark并在2026年9月获60亿美元估值；Adcock持有Figure约50%股权，个人实时身家于2026年10月达234亿美元），核心管理层还包括联合创始人兼董事Gregg Hill与Jesse Coors-Blankenship [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)。融资历程上，Adcock于2022年自掏腰包出资1亿美元完成种子轮；2023年5月完成7,000万美元A轮；2024年2月完成由微软、NVIDIA、Jeff Bezos等参投的6.75亿美元B轮融资（估值26亿美元）；2025年9月，公司完成由Parkway Venture Capital领投，Brookfield Asset Management、NVIDIA、麦格理资本（Macquarie）、Intel Capital及LG参投的逾10.6亿至15亿美元C轮融资，投后估值飙升至惊人的390亿至395亿美元（18个月内暴涨15倍），累计融资额达19亿至25亿美元 [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)。2026年10月8日，市场传出NVIDIA正考虑向Figure AI追加新一轮10亿美元投资 [45](https://www.eweek.com/news/nvidia-figure-ai-1-billion-investment-humanoid-robots/)。

### Tesla Optimus：车规级FSD纯视觉迁移、AI5芯片与超级工厂内生闭环

如果说Figure代表了独角兽的资本爆发力，Tesla（特斯拉）旗下的 Optimus 则代表了依托顶级车企制造供应链与自动驾驶AI体系进行降维打击的极致内生模式 [15](https://ifactoryapp.com/industries/automotive-manufacturing/tesla-optimus-fremont-gen-3-humanoid-2026)。在技术路径上，Tesla将Optimus、全自动驾驶（FSD）与Dojo超算中心整合为统一的“真实世界AI”（Real-World AI）平台 [53](https://www.aparobot.com/robots/tesla-optimus)。Optimus完全复用了Tesla FSD的纯视觉端到端神经网络架构，机身搭载8颗Autopilot视觉相机，结合指尖触觉传感器与足部六维力/力矩传感器，通过端到端神经网络将相机像素输入直接转化为全身执行器的控制指令，并利用视频预测模型、遥操作模仿学习以及逾千台机群共享的“车队学习”（Fleet Learning）持续进化 [15](https://ifactoryapp.com/industries/automotive-manufacturing/tesla-optimus-fremont-gen-3-humanoid-2026)。2026年，Optimus在算力与交互层迎来两大突破：一是于2026年4月成功流片了优先面向Optimus设计的定制推理芯片 AI5，赋予机器人在断网或无Wi-Fi环境下独立执行安全与基础作业任务的本地智能 [23](https://optimusk.blog/blog/what-is-tesla-optimus/)；二是全面集成了xAI旗下的 Grok 大模型作为语音交互与高层任务编排引擎 [23](https://optimusk.blog/blog/what-is-tesla-optimus/)。

在产品与商业化进度上，继2023年12月发布配备11自由度灵巧手的Gen 2及随后的2.5过渡版本后，Tesla于2026年1月21日在弗里蒙特（Fremont）工厂正式启动首款面向大规模量产设计的 Optimus Gen 3（V3） 产线，并于2026年2月揭晓了Gen 3革命性的灵巧手设计 [23](https://optimusk.blog/blog/what-is-tesla-optimus/)：单手自由度从Gen 2的11个翻倍跃升至22个自由度，单手及前臂集成25个腱绳驱动执行器（双手合计50个执行器，为前代的4.5倍），每根手指均配备六轴力/力矩触觉感知；整机身高1.73米，体重57公斤，全身共28个结构自由度，内置2.3 kWh自研电池组（支持约8小时续航与2小时快充），移动承载能力20公斤，极限硬拉辅助负载达150公斤 [15](https://ifactoryapp.com/industries/automotive-manufacturing/tesla-optimus-fremont-gen-3-humanoid-2026)。在商业化节奏上，尽管Tesla未能兑现2025年内部部署5,000台的早期目标（2025年四季度财报电话会确认当年实际部署数百台用于“Optimus学院”训练） [23](https://optimusk.blog/blog/what-is-tesla-optimus/)，但在2026年实现了实质性产能跃升：截至2026年上半年，已有超过1,000台Optimus在弗里蒙特与得州超级工厂（Giga Texas）投入7×24小时全天候生产作业，不仅在电池模组车间以超过99%的报告成功率执行电芯分拣、导热垫铺设与高压线束布线，更在2026年5月29日发布的官方实测视频中展示了Gen 3在无人工干预下连续平稳搬运重达120磅（约54公斤）的Model Y电池托盘并精准放置于AGV小车上的工业级能力 [15](https://ifactoryapp.com/industries/automotive-manufacturing/tesla-optimus-fremont-gen-3-humanoid-2026)。供应链数据显示，2026年9月Tesla已下达约1.5万台Optimus的零部件订单，周产量从9月下旬的约1,000台爬坡至年底的2,500台/周 [23](https://optimusk.blog/blog/what-is-tesla-optimus/)。目前单机内部制造成本已从早期的约15万美元下探至5万至10万美元区间，公司计划于2026年底至2027年启动外部商业客户交付，并于2027年底前实现面向消费者的规模化销售，远期规模化目标售价锁定在极具颠覆性的2万至3万美元（Giga Texas正在建设远期规划年产能达1,000万台的专属工厂） [15](https://ifactoryapp.com/industries/automotive-manufacturing/tesla-optimus-fremont-gen-3-humanoid-2026)。

在团队与资金情况方面，项目由Elon Musk亲自挂帅，依托Tesla内部Autopilot视觉神经网络团队与机电工程团队协同攻坚，资金完全由Tesla上市公司自有现金流提供支撑（2026年Tesla全公司资本开支预算维持在200亿美元高位） [15](https://ifactoryapp.com/industries/automotive-manufacturing/tesla-optimus-fremont-gen-3-humanoid-2026)。

### 1X Technologies：面向非结构化家庭场景的仿生肌腱架构与真实长尾数采

在工业场景成为绝大多数人形机器人首选试验场的背景下，挪威裔美国机器人公司1X Technologies（前身为Halodi Robotics）独辟蹊径，将战略重心直接锚定在非结构化的私人家庭陪伴与家务服务市场 [22](https://en.wikipedia.org/wiki/1X_Technologies)。在技术路径与产品进度上，为了确保机器人在人类居住环境中的本质安全与亲和力，1X摒弃了刚性工业机械臂的粗重外观，于2024年8月推出并在2025至2026年持续迭代专为家庭设计的双足人形机器人 NEO [22](https://en.wikipedia.org/wiki/1X_Technologies)。NEO采用纤细的拟人化外观与柔性仿生肌腱驱动设计，动作柔顺自然；2026年7月，公司正式公布了NEO新一代灵巧手技术细节，单手拥有高达25个自由度，精细操作能力逼近人类手掌 [22](https://en.wikipedia.org/wiki/1X_Technologies)。此外，公司还保留了已在安防巡逻与物流场景成熟商用的轮式机器人 EVE [58](https://embodyvc.com/companies/1x-technologies/)。2026年4月30日，1X宣布在加州海沃德（Hayward）建立全新的NEO制造工厂以推进量产，NEO的目标终端售价定为2万美元 [58](https://embodyvc.com/companies/1x-technologies/)。

在商业化、团队与融资情况方面，1X由挪威机器人专家兼首席执行官Bernt Øivind Børnich于2014年创立 [57](https://unicornscreener.vc/blog/8-physical-ai-startups-racing-to-build-the-robot-economy)。Børnich明确提出，攻克家庭场景具身智能的唯一路径是通过早期家庭领养者部署NEO，采集海量真实的家庭长尾交互数据以训练端到端自主模型 [22](https://en.wikipedia.org/wiki/1X_Technologies)。工业端公司亦与企业软件巨头IFS达成合作将工业AI引入物理世界 [60](https://tracxn.com/d/companies/1x/__LHsrSyi_fXuqm41b2urwiNEhmn9qEjCh1Md-w2ep8KE)。在资本层面，1X是OpenAI最早重仓押注的具身智能硬件企业（2024年完成1亿美元融资，历史累计融资约8亿美元，OpenAI甚至曾考虑直接全资收购1X） [27](https://themimic.io/articles/physical-intelligence-1b-funding-humanoid-robots-2026)；2025年9月，1X曾寻求以100亿美元估值融资10亿美元 [22](https://en.wikipedia.org/wiki/1X_Technologies)；至2026年8月下旬，随着家庭场景商业化周期长于工业场景的现实凸显，软银集团（SoftBank）正深入洽谈以60亿美元估值收购1X Technologies的控股权，意图将其与软银投资的Skild AI等资产整合成庞大的机器人帝国 [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)。

### 智元机器人：全品类本体矩阵、世界动作模型与开源生态协同

在中国全栈具身智能阵营中，智元机器人（AgiBot）展现了极强的产品矩阵扩张能力与软硬全栈野心 [14](https://m.36kr.com/p/3261349018468489)。在技术路径上，智元坚持“本体硬件+小脑运控+具身大脑+数据生态”全栈自研：硬件底层自研了PowerFlow模块化准直驱关节、峰值扭矩达450Nm的双速比减速关节模组以及19自由度（12主动自由度）工业级视触觉灵巧手，控制层研发了小脑控制器Xyber-Edge与域控制器Xyber-DCU [14](https://m.36kr.com/p/3261349018468489)；在核心具身大模型层面，智元不仅于2025年4月与Physical Intelligence开展跨本体策略合作，更于2026年9月10日重磅发布了自研具身世界动作模型 GE-Act 2.0（World Action Model），该模型基于高达30,000小时的真机操作数据进行预训练，系统性验证了通用机器人操作领域的Scaling Laws [4](https://exponentialindustry.com/ontology/physical-ai-robotics/)。同时，公司通过开源软件框架AIMA及全栈开源机器人图纸构建开发者生态 [14](https://m.36kr.com/p/3261349018468489)。

在产品与商业化进度上，智元构建了业内最庞大的“双足+轮式+四足”四大产品系列（远征、灵犀、精灵、绝尘），精准卡位不同下游场景 [14](https://m.36kr.com/p/3261349018468489)。其中，作为工业与商业旗舰的远征系列涵盖了初代远征A1（身高175cm、49自由度、单臂负载5kg）、主打展厅导览与营销客服交互服务的全尺寸双足机器人远征A2（配备360°激光雷达与6颗高清相机实现全景无盲区语义避障）、专为柔性智造上下料与端子插接设计的四轮四驱双臂机器人远征A2-W（支持热插拔换电与数据积累持续优化），以及双臂采用双速比减速关节模组、腿部直线推杆电机具备8800N推力、全工作空间可搬运40kg重物的重载特种双足机器人远征A2-Max [14](https://m.36kr.com/p/3261349018468489)。面向轻量化、数采与开源生态的灵犀系列则包括全栈开源的灵犀X1（采用串并联混合构型手臂与差分驱动双肩关节，单臂仅重2.5kg，内置“机-机模式”可将智能手机直接化身为机器人大脑）、低成本专业真机数据采集机器人灵犀X1-W（专供预训练阶段真机数采以大幅降低数据获取成本），以及2025年3月发布的28自由度双足交互人形机器人灵犀X2（配备柔性外壳与裸眼3D，支持奔跑、跳跃、骑车及简单任务零样本泛化，瞄准“保安、保姆、保洁”等家庭陪伴与康养场景） [14](https://m.36kr.com/p/3261349018468489)。此外，精灵系列（G1轮式机器人）重点布局商业零售与工业数采，绝尘系列则覆盖中大型商业清洁场景 [62](https://pdf.dfcfw.com/pdf/H3_AP202507221713451794_1.pdf?1753180160000.pdf)。商业化交付上，智元于2024年率先突破1,000台量产下线大关，其远征A2-W签下了国内首个工业领域具身机器人规模化商业订单（单日负责500台以上产能的原材料配送与空箱回收） [64](https://finance.sina.com.cn/jjxw/2026-08-05/doc-inimfwqp4650448.shtml)。2025年，智元机器人实现营业收入突破10亿元人民币，并将2026年营收目标锁定在40亿元人民币；2026年3月28日，来自全球34个国家的2,500名合作伙伴出席了智元2026年度战略大会 [66](https://finance.ifeng.com/c/8vRPAPwwHEL)。

在团队与融资情况方面，智元成立于2023年2月，由前华为“天才少年”、B站知名科技UP主彭志辉（“稚晖君”）联合创立，法定代表人及实际控制人为前华为高管邓泰华，合伙人兼营销服副总裁为姜青松 [14](https://m.36kr.com/p/3261349018468489)。值得关注的是，智元核心团队在三年间经历了至少三次结构性演进：2024年突破千台量产后早期偏重硬件本体研发的成员离开；2025年引入具身大脑学者罗剑岚（2026年其岗位再次调整）；2025年之后具备强商业化销售背景的高管全面进入核心决策层，折射出公司从“技术极客造机”向“规模化商业交付”的战略重心迁移 [64](https://finance.sina.com.cn/jjxw/2026-08-05/doc-inimfwqp4650448.shtml)。融资方面，智元成立以来累计完成超过12轮融资，股东囊括腾讯、比亚迪、高瓴创投、红杉中国、京东、上汽及北汽等顶级资本 [67](https://www.lanjinger.com/d/1776476087113121960)；公司于2025年11月完成股份制改造，估值从2024年的70亿元、2026年初的150亿元一路飙升，至2026年10月中旬已完成新一轮10亿至15亿元融资的收尾工作，最新投后估值高达约500亿元人民币 [63](https://finance.sina.com.cn/wm/2024-09-01/doc-incmscvm8749778.shtml)。

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

### 全球主流具身智能机器人核心硬件指标与量产部署规模对比

末端灵巧度：单手主动/被动自由度对比

单位：自由度 (DoF)

负载作业能力：双臂/整机最大常规作业负载

单位：千克 (kg)

实景落地规模：已验证量产出货及产线部署机群

单位：台 (Units)

在末端灵巧度上，1X NEO（25 DoF）与Tesla Optimus Gen 3、Apptronik Apollo 2（均为22 DoF）处于第一梯队；在工业重载能力上，银河通用Galbot S1（50 kg）与智元远征A2-Max（40 kg）显著领先；而在量产交付规模上，**宇树科技** （2025年出货超5,500台）与**Tesla Optimus** （产线部署超1,000台）已拉开规模化差距。

数据来源: [21世纪经济报道](https://m.21jingji.com/article/20260807/herald/73fd8031f9dbf944f4928435d23374d4.html)、[iFactory (Tesla Optimus)](https://ifactoryapp.com/industries/automotive-manufacturing/tesla-optimus-fremont-gen-3-humanoid-2026)、[iFactory (Apptronik)](https://ifactoryapp.com/industries/automotive-manufacturing/apollo-mercedes-apptronik-humanoid-automotive)、[东方财富网 (银河通用)](https://caifuhao.eastmoney.com/news/20260305164448808529560)、[36氪 (智元机器人)](https://m.36kr.com/p/3261349018468489)、[ValueAdd VC (Figure AI)](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)、[维基百科 (1X NEO)](https://en.wikipedia.org/wiki/1X_Technologies)、[OptimusK](https://optimusk.blog/blog/what-is-tesla-optimus/)

<!-- /figure 2 -->

## 路线三：仿真合成数据驱动与手眼脑端到端协同路线

在水平大模型派与全栈双足派激烈交锋之际，产业界日益意识到一个严峻的共性瓶颈：真实世界物理交互数据的极度匮乏 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。相比于大语言模型可直接抓取互联网数万亿Token文本，全球现存的真机遥操作数据总量仅在数十万小时级别，且人工穿戴动捕设备或遥操作采集不仅成本高昂、动作延迟大，更无法在真实工厂中遍历粉尘、震动、光照剧变或易碎品跌落等极端长尾工况 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。为此，第三条技术路线应运而生——以百亿级高保真物理仿真合成数据（Sim-to-Real）为主导，同时在本体形态上摒弃早期华而不实的双足跑跳执念，坚持“大脑优先、身体务实”，全力攻克“手、眼、脑”的端到端生产力协同 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。

### 银河通用：百亿级虚实融合数据集与打通大脑至神经控制的端到端落地

银河通用（Galbot）是全球范围内将“合成数据驱动+手眼脑端到端协同+轮式/重载务实本体”路线推向极致并实现大规模商业闭环的代表性独角兽 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。在技术路径上，针对当前业界普遍将大脑（高层任务规划）、小脑（全身运动控制）与手部（末端灵巧操作）割裂开发、模块间接口标准不一且信息逐层衰减导致响应迟滞的痛点，银河通用自主研发了全球首个且目前唯一彻底打通“大脑—小脑—神经控制”全链路的端到端具身大模型“银河星脑”（AstraBrain），将高层多模态视觉语义感知与底层毫秒级实时力控反馈深度融合，实现了全身协调移动与全手精细操作的丝滑配合 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。与此同时，为解决端到端大模型的数据饥渴，公司开创了数据基建“银河星坊”（AstraSynth），确立了“以合成仿真数据为主、真机数据为辅”的虚实融合训练范式，在高精度物理仿真环境中自动生成涵盖海量几何形状、材质反射率与物理动力学特性的百亿级具身智能数据集，使机器人在虚拟世界中遍历极端边缘场景，随后仅需极少量真机数据微调即可完成Sim-to-Real实战迁移 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。据披露，该范式的训练效率比依赖纯真机遥操作的特斯拉高出1,000倍，基于该数据集训练的模型在真实泛化抓取任务中的成功率高达99% [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。

在产品进度上，银河通用拒绝在早期盲目跟风双足后空翻，而是推出了主打泛化灵巧操作的轮式双臂人形机器人 Galbot G1（单台售价约70万元人民币）以及行业首款工规级重载具身机器人 Galbot S1（单台售价约105万元人民币） [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。在2026年央视春晚舞台上，Galbot G1作为首个“自主干活机器人”与演员沈腾、马丽同台，在无预设程序、面对随机摆放物品与舞台灯光变化的真实环境下，依靠“银河星脑”实时决策，自主完成了盘核桃、捡拾细小玻璃碎片、货架精准取物、叠衣理物与串制烤肠等极高难度的精细灵巧作业 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。而针对工业痛点推出的Galbot S1则具备高达50公斤的双臂最大负载，支持自主换电，可在高粉尘、强震动与大温差的严苛工业工况下连续稳定运行 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。

在商业化进度上，银河通用围绕“不追求机器人会做100件事，而是把10件事做到工业级标准”的策略，在三大场景实现了深度商业化落地 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。在工业制造领域，银河通用是迄今唯一在宁德时代（CATL）电池工厂实现常态化全自主作业的人形机器人企业（并于2026年9月中标宁德时代2.36亿元人民币项目），同时与德国博世（Bosch）、丰田汽车、北汽集团、上汽集团达成深度合作，累计订单达数千台，并于2025年12月与百达精工签署了部署超1,000台机器人的战略协议 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。在新零售与即时零售领域，公司首创由Galbot独立完成迎宾、点单、支付、取货全流程的“银河太空舱”智能零售便利店，上线半年内已在北京颐和园、王府井、上海白玉兰、深圳前海等国内20余个核心城市落地超100家，实现全球首个百台级机器人自主运营零售网络，同时在24个城市落地单店管理超5,000种SKU、7×24小时不间断运营逾一年的智慧零售药房与即时零售仓 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。在医疗康养领域，公司已与宣武医院、华西医院等三甲医院合作推进病房夜间查房、量血压及认知测试试点 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。然而，随着估值飙升，2026年下半年市场亦出现了针对其商业化成色的审视与争议，主要聚焦于其核心大客户（如宁德时代、美团、车企）与战略股东高度重合，以及已验证交付数百台的账面收入与逾200亿估值之间的倍数落差，这在IPO审核趋严的背景下将成为其必须跨越的独立商业化考题 [24](https://m.36kr.com/p/3978672823417862)。

在团队与融资情况方面，银河通用成立于2023年5月，由极具互补性的“90后顶尖学者+85后工业老兵”双核驱动：创始人兼CTO王鹤（1992年生）本科毕业于清华大学电子系，于斯坦福大学师从美国三院院士Leonidas J. Guibas攻读博士，2021年回国创建北京大学前沿计算研究中心EPIC Lab及智源研究院具身智能研究中心，是全球最早开展端到端具身大模型研究的学者之一；联合创始人姚腾洲则毕业于北航机器人研究所（师从王田苗教授），曾任工业机器人巨头ABB上海研发中心核心研发人员，具备深厚的硬件工程化与量产经验 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。资本市场上，银河通用在不到三年内上演了“每半年一轮、累计融资超69.6亿元（约70亿元人民币）”的资本闪电战，稳居中国具身智能累计融资额榜首 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)：继2023年6月经纬、蓝驰种子轮，2024年6月美团、北汽、启明、IDG等7亿元天使轮，2024年11月上汽、香港投资管理公司（HKIC）、深创投等5亿元A轮，以及2025年6月宁德时代领投的超11亿元融资后，公司于2025年12月完成由中国移动链长基金领投、中金资本、中科院基金及新加坡与中东主权资本参投的超3亿美元（约21.6亿元人民币）融资，投后估值达30亿美元（超200亿元人民币） [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)；2026年3月，公司再获25亿元人民币巨额注资，国家大基金三期（通过国家人工智能产业基金首次出手具身智能）、中国石化、中信集团、中国银行等“国家队”超级央企悉数入局 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。

## 路线四：高动态本体运控筑底与大行为模型渐进融合路线

第四条技术路线起源于经典机器人学与现代强化学习的深度结合。该路线的代表企业大多在具身大模型浪潮爆发前便已深耕足式与人形机器人多年，其核心逻辑是：物理世界中一切操作的前提是机器人具备极高可靠性的移动能力、全身动态平衡能力（“强小脑”）以及可规模化制造、高功率密度且成本可控的机电本体 [16](https://www.huxiu.com/article/4884048.html)。在率先筑牢硬件与运动控制护城河后，这些企业正通过引入外部VLA大模型合作或自研大行为模型（LBM），完成从“四肢发达的运动机器”向“手脑协同的通用生产力工具”的跃迁 [3](https://www.tri.global/news/ai-powered-robot-boston-dynamics-and-toyota-research-institute-takes-key-step-towards-general)。

### 宇树科技：极致本体降本、强化学习运控与科创板首股的商业化实证

宇树科技（Unitree Robotics）是全球高动态本体与运动控制路线的绝对龙头，也是目前全球极少数实现数千台级人形机器人规模化交付与高额净利润的整机企业 [16](https://www.huxiu.com/article/4884048.html)。在技术路径与产品进度上，宇树的核心壁垒在于全自研高能量密度电机、减速器、控制器、3D激光雷达等核心零部件的垂直整合制造能力，以及基于深度强化学习与模型预测控制的全身高动态运动控制算法 [16](https://www.huxiu.com/article/4884048.html)。继2021年凭消费级四足机器狗Go1破圈后，宇树于2023年8月发布首款全尺寸通用人形机器人 H1（并在2025年央视春晚实现16台H1与真人同台集群舞蹈演出），更于2024年5月推出了起售价仅9.9万元人民币（国际售价约12,698英镑）的轻量化人形机器人 G1（后续亦推出H2等型号），以极具侵略性的性价比彻底击穿了全球人形机器人硬件的价格底线 [19](https://humanoidrobotsuk.com/robots/atlas)。针对市场对其“擅长本体与运动控制、但具身大模型大脑相对薄弱”的评价，宇树在2026年8月IPO战略配售中正式引入国产AI大模型领军企业深度求索（DeepSeek）（获配1.41亿元并锁定36个月），全力打通前沿大模型与高动态机器人本体的技术协同 [9](https://news.pedaily.cn/202608/567833.shtml)。

在商业化与财务进度上，宇树科技交出了全球人形机器人行业最硬核的财务答卷：根据其招股书披露，2025年宇树科技全年人形机器人出货量突破5,500台，产销率超过95% [16](https://www.huxiu.com/article/4884048.html)；2025年全年实现营业收入17.08亿元人民币（其中2025年前九个月人形机器人收入达5.95亿元，占主营业务收入的51.53%，历史上首次超越四足机器狗成为第一大收入来源），主营业务毛利率从2022年的44.18%大幅攀升至60.13%；2025年实现归母净利润2.78亿元，剔除3.49亿元股份支付费用后的扣非归母净利润高达5.91亿元人民币（约6亿元），扣非净利率高达34.77%（横向对比同业披露数据：优必选2025年扣非净利率为-35.71%，越疆为-25.05%，乐聚智能为-30.07%） [16](https://www.huxiu.com/article/4884048.html)。2026年5月31日，宇树亚洲首家具身智能体验馆在上海开业 [73](https://m.thepaper.cn/newsDetail_forward_33784711)。然而，财务数据亦揭示了成长的隐忧：2026年第一季度，宇树营收同比增速从此前高达332.64%回落至68.49%，一季度扣非净利润同比下滑52.55%，主因是登上2026年春晚等营销投入推动2026Q1销售费用同比激增133.3%至1.4亿元 [75](https://www.tmtpost.com/8108156.html)。这深刻印证了行业的核心矛盾——宇树凭借极致的性价比横扫了全球高校科研、开发平台与商业展演市场，但“把机器人卖出去”与“让机器人在工厂产线真正替代人工成为生产力”依然是两个阶段的命题 [9](https://news.pedaily.cn/202608/567833.shtml)。

在团队与资本市场进展方面，宇树由1990年出生的创始人王兴兴（毕业于浙江理工大学及上海大学）于2016年8月在杭州创立，核心管理团队11人平均年龄仅40.73岁，全员深耕研发与销售一线 [16](https://www.huxiu.com/article/4884048.html)。历经十年10轮融资（美团持股9.65%为第一大外部机构股东，红杉中国持股7.11%，经纬、深创投、顺为、腾讯、阿里、中国移动等在列），宇树科技（688836.SH）从2026年3月20日IPO获受理到2026年8月19日正式登陆上海证券交易所科创板仅耗时152天，成为万众瞩目的A股“人形机器人第一股” [73](https://m.thepaper.cn/newsDetail_forward_33784711)。公司以150.80元/股发行4,044.64万股，募集资金总额达60.99亿元，发行总市值定格于609.93亿元人民币（对应静态市盈率219.23倍、市销率35.89倍，全国社保基金三大组合、DeepSeek、中石油昆仑资本、南方电网、腾讯等悉数参与战略配售；至2026年9月其二级市场估值一度折合达约290亿美元） [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)。王兴兴直接及间接合计持股市值超183亿元，并公开承诺将其通过员工持股平台间接持有的近58亿元市值股份在上市满三年后全部分批用于核心员工股权激励 [74](https://m.21jingji.com/article/20260807/herald/73fd8031f9dbf944f4928435d23374d4.html)。

### 波士顿动力与Apptronik：顶级机械工程本体与外部前沿大模型深度耦合

在欧美市场，拥有深厚机械工程与航天实验室积淀的波士顿动力（Boston Dynamics）与Apptronik，不约而同地选择了“打造世界级高可靠本体+结盟顶级外部AI实验室（TRI / Google DeepMind）”的技术演进路径 [3](https://www.tri.global/news/ai-powered-robot-boston-dynamics-and-toyota-research-institute-takes-key-step-towards-general)。

波士顿动力（现代汽车集团控股）于2024年4月正式退役了研发长达11年的液压版Atlas，全面转向全电驱平台 Electric Atlas（身高150厘米，体重75公斤，拥有超越人类生理极限的360°关节旋转与180°腰部旋转能力，配备双目HDR立体相机与7自由度多策略灵巧夹爪） [19](https://humanoidrobotsuk.com/robots/atlas)。在技术路径上，为解决传统手工编程无法扩展复杂操作技能的难题，波士顿动力由Scott Kuindersma领衔，与丰田研究院（Toyota Research Institute, TRI，由Russ Tedrake博士领衔）深度合作，于2025年8月首次在Electric Atlas上成功验证了大行为模型（Large Behavior Model, LBM） [3](https://www.tri.global/news/ai-powered-robot-boston-dynamics-and-toyota-research-institute-takes-key-step-towards-general)。该LBM直接复用机器人遥操作控制接口，以30Hz频率接收视觉图像与历史观测状态，每次推理预测长度为48步（对应1.6秒）的动作块（Action-chunk），在无需编写任何一行新代码的情况下，仅凭单一神经网络策略便实现了双足行走、下蹲、弯腰与双臂部件分拣、倾倒、叠衣服等长程全身移动操作（Whole-body Locomotion and Manipulation）的无缝融合，甚至在研究人员故意移走料箱或用曲棍球杆干扰时能实时自主调整步态与手部轨迹 [3](https://www.tri.global/news/ai-powered-robot-boston-dynamics-and-toyota-research-institute-takes-key-step-towards-general)。2026年，波士顿动力进一步与Google DeepMind建立全新基础AI合作伙伴关系 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。目前Electric Atlas仍定位于高规格研发与工业验证平台（单机造价高达数十万英镑，暂未面向大众商业发售），已在现代汽车工厂内开展汽车悬架支柱（Struts）自主抓取与排序上架实测 [19](https://humanoidrobotsuk.com/robots/atlas)。

与波士顿动力同源的 Apptronik 则于2016年衍生自得克萨斯大学奥斯汀分校（UT Austin）以人为中心机器人实验室，核心团队由CEO Jeff Cardenas及当年参与研发NASA“女武神”（Valkyrie）太空双足机器人的核心工程师组成，目前拥有约300名员工 [6](https://dealroom.co/news/125782-apptronik-raises-520m-at-5-5b-valuation-to-scale-humanoid-robot-apollo/)。在技术路径与产品进度上，Apptronik将其航天级可靠性工程倾注于通用人形机器人 Apollo 及最新迭代的 Apollo 2 之上：整机最大负载达25公斤（高于Figure 03与Optimus的20公斤），搭载22自由度五指灵巧手（SharpaWave/Inspire），并独创了免工具快速拆换模块化架构（手臂、手部、躯干可在20分钟内现场更换完毕，无需返厂维修）以及小于5分钟的热插拔电池系统，精准击中了工业产线对停机维护时间（Downtime）极度敏感的痛点 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。在“大脑”端，Apptronik深度绑定Google DeepMind，成为 Gemini Robotics 2 全身控制VLA与多机协作模型的标杆硬件载体 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。

在商业化与融资情况方面，Apptronik已与梅赛德斯-奔驰（Mercedes-Benz）、物流巨头GXO Logistics及全球电子代工巨头捷普（Jabil）展开实质性试点：奔驰不仅向其注资数千万欧元，更在德国柏林数字工厂园区与匈牙利凯奇凯梅特工厂部署Apollo进行产线物料配送、组件质检及NVIDIA Omniverse数字孪生仿真与AR遥操作数采；GXO在2026年中期已实际运行Apollo 2并建立“Robot Park”数据采集场；Jabil则兼具客户与代工伙伴双重身份，在自家产线测试Apollo的同时为其提供跨全球100余个基地的规模化代工能力（构建“Apollo制造Apollo”闭环） [20](https://ifactoryapp.com/industries/automotive-manufacturing/apollo-mercedes-apptronik-humanoid-automotive)。不过，奔驰等合作方预计Apollo实现真正的大规模成熟商业部署仍需等到2027至2029年，投资人预期其未来商业模式将采用约8万美元/年的服务订阅制或5万至8万美元的整机售价 [20](https://ifactoryapp.com/industries/automotive-manufacturing/apollo-mercedes-apptronik-humanoid-automotive)。融资方面，继2025年2月至3月完成4.03亿至4.15亿美元A轮融资后，Apptronik于2026年2月11日完成了高达5.2亿美元的Series A-X扩充轮融资，使整个A轮系列总融资额突破9.35亿美元（历史累计融资达10亿至13亿美元），投后估值翻了三倍达到53亿至55亿美元，领投方包括B Capital、Alphabet（Google/GV）与梅赛德斯-奔驰，卡塔尔投资局（QIA）、AT&T Ventures、约翰迪尔（John Deere）及PEAK6共同参投 [6](https://dealroom.co/news/125782-apptronik-raises-520m-at-5-5b-valuation-to-scale-humanoid-robot-apollo/)。

### 优必选、逐际动力与星尘智能：双足总装实训、全地形运控与绳驱机构创新

在中国市场，围绕本体运动控制与新型传动机构创新的代表性企业同样在2025至2026年取得了显著突破。作为港股上市的“人形机器人老兵”，优必选（UBTECH）依托深厚的伺服驱动器与双足步态算法积累，将其工业人形机器人 Walker S 与 Walker S1 深度锚定在新能源汽车总装车间，于2025年实现小批量商业交付并进入蔚来（NIO）、东风等车企总装产线执行车门锁质检、零件安装与SPS物料自动化分拣实训 [17](https://pdf.dfcfw.com/pdf/H3_AP202605071822028328_1.pdf?1778171901000.pdf)。据优必选首席品牌官谭旻披露，目前人形机器人在产线上的平均生产效率约为人类工人的30%至40%，预计到2027年初可提升至80%左右的规模化替代临界点，公司2026年目标出货量设定为3,000台，但高昂的研发与市场投入使其2025年扣非净利率仍处于-35.71%的亏损状态 [17](https://pdf.dfcfw.com/pdf/H3_AP202605071822028328_1.pdf?1778171901000.pdf)。

同处粤港澳大湾区的逐际动力（LimX Dynamics）由南方科技大学教授张巍于2022年创立，拒绝同质化内卷，专注于全地形高动态全身运动控制与具身“新物种”研发 [10](https://m.36kr.com/p/3668859815158405)。其多形态双足机器人 TRON 1 已完成全球多国商业交付，跑通了从设计、量产到销售的商业化闭环；全尺寸人形机器人 CL-1 则凭借高性能全身运控与实时目标感知，实现了大负载、大范围的连续搬运作业 [88](https://m.thepaper.cn/newsDetail_forward_30320504)。在资本端，作为“深圳八大金刚”之一，逐际动力于2026年2月完成2亿美元B轮融资，随后于2026年7月再获近2亿美元Pre-IPO轮融资，半年内狂揽4亿美元，投后估值跃升至150亿元人民币 [86](https://m.36kr.com/p/3957428318928264)。

与此同时，由前腾讯Robotics X实验室核心专家来杰创立的星尘智能（Astribot）在硬件本体路径上独树一帜，开创并量产了全球首款绳驱（Tendon-driven）AI机器人 Astribot S1 [18](https://feng.ifeng.com/c/8xCD4divDk7)。不同于传统刚性齿轮减速器关节，绳驱机构高度模拟人类生物肌腱的传动方式，具备极高的比功率、低运动惯量与天生的柔顺力控安全性，为VLA模仿学习提供了极高质量的同构数采与高动态灵巧执行载体；星尘智能近期已完成由投控东海（深投控）等参投的10亿元规模新一轮融资，最新估值同样达到150亿元人民币，稳居中国具身智能第一梯队 [18](https://feng.ifeng.com/c/8xCD4divDk7)。

## 全球具身智能资本版图、商业化瓶颈与二阶演进洞察

纵观2026年全球具身智能的竞争格局，技术路线的演进与资本估值的定价机制正发生深刻的重构。一级与二级市场对头部企业的定价已不再局限于当期硬件销售利润，而是对未来万亿级通用劳动力替代市场（及AI物理世界入口平台价值）的提前折现 [27](https://themimic.io/articles/physical-intelligence-1b-funding-humanoid-robots-2026)。

<!-- figure 3: interactive chart embedded in the report; its text content follows -->

Embodied AI Market Intelligence

### 全球具身智能头部企业最新估值与累计融资规模全景对比（2026）

统一按十亿美元（USD $B）计量，并标注各企业核心技术路线、关键融资轮次与溢价特性。

技术路线交互筛选： 点击路线标签可高亮对应梯队企业

PANEL 1

#### 最新确认投后估值 / 发行市值 (单位: 10亿美元 $B)

X轴上限: $45B

PANEL 2

#### 累计已披露融资金额 / IPO募资规模 (单位: 10亿美元 $B)

X轴上限: $2.5B

最高估值倍数标的

Skild AI & PI

无硬件资产，单依靠纯脑模型与ARR跨过140亿与56亿估值

资本募集最密集

Figure AI ($1.9B)

垂直整合需自建工厂与全链条研发，单C轮超10亿美元

中国梯队IPO破冰

宇树科技 (~$8.6B)

科创板发行市值610亿元且率先盈利，募资近61亿元

全球具身智能资本呈现极度头部化集聚：**Figure AI** 以390亿美元估值领跑全球；纯软件大脑赛道中，**Skild AI** （140亿美元）与**Physical Intelligence** （确认56亿美元，洽谈110亿美元）获得极高平台溢价；中国市场则形成了以**宇树科技** （科创板发行市值约610亿元/86亿美元）、**智元机器人** （约500亿元/70亿美元）与**银河通用** （超200亿元/30亿美元）为首的百亿独角兽集群。

数据来源： [Value Add VC (Figure)](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)· [Skild AI 官方博客](https://www.skild.ai/blogs)· [21世纪经济报道 (宇树科技IPO)](https://m.21jingji.com/article/20260807/herald/73fd8031f9dbf944f4928435d23374d4.html)· [财经网 / 智元机器人](https://c.m.163.com/news/a/L96SCAM505118I96.html)· [Tech Funding News (1X)](https://techfundingnews.com/softbank-in-talks-to-buy-majority-stake-in-1x-at-6b-valuation/)· [Value Add VC (PI)](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)· [Multiples VC (Apptronik)](https://multiples.vc/private-comps/apptronik)· [东方财富网 (银河通用)](https://caifuhao.eastmoney.com/news/20260305164448808529560)· [具身快讯 (逐际动力)](https://www.airobo.run/2026/08/20/airobo-news-65d84f013845/)· [凤凰科技 (星尘智能)](https://feng.ifeng.com/c/8xCD4divDk7)

<!-- /figure 3 -->

为全面梳理全球具身智能四大技术路线的核心代表企业，下表从所属路线、核心技术路径、旗舰产品进度、商业化落地进展、最新融资与估值以及核心团队背景六个维度进行了全景式对齐：

| 公司名称 | 所属技术路线 | 核心技术路径 | 旗舰产品进度 | 商业化落地进展 | 最新融资与估值情况（截至2026.10） | 核心团队与创始人背景 |
| --- | --- | --- | --- | --- | --- | --- |
| **Physical Intelligence (π\pi)** | 路线一：跨本体通用大模型 | 流匹配（Flow Matching）连续动作生成、Recap在线强化学习、多尺度具身记忆（MEM）、RL Tokens、第一视角人类视频迁移 | π0\pi_0、π0.6∗\pi^*_{0.6}、π0.7\pi_{0.7}（实现未见软硬件组合的组合泛化，驱动5+异构平台） | 定位第三方硬件“物理智能层”；与Weave（叠衣）、Ultra（工业包装）、智元机器人合作部署测试；暂未披露规模化营收 | 累计披露融资约11亿美元；2025.11获CapitalG领投6亿美元B轮（估值**56亿美元** ）；2026.03洽谈10亿美元新融资（拟估值**110亿美元+** ），投资方含Bezos、OpenAI、Thrive、NVentures | CEO Karol Hausman（前DeepMind资深科学家）、总裁Lachy Groom（前Stripe高管）、UC Berkeley教授Sergey Levine、Stanford教授Chelsea Finn等7位顶级学者联创 [11](https://www.roboticscenter.ai/companies/physical-intelligence) |
| **Skild AI** | 路线一：跨本体通用大模型 | 全向跨本体（Omni-bodied）通用机器人基础模型，一套权重驱动四足、双足与机械臂 | Skild Brain通用大脑模型 | 收购Zebra机器人业务；部署60+客户现场（富士康Blackwell机柜、住友线束、三井厨房）；10个月内**ARR突破1亿美元** | 2024.07获3亿美元A轮；2026.01完成软银领投14亿美元C轮，估值超**140亿美元** （三星、LG、施耐德、Bezos参投） | 卡内基梅隆大学（CMU）教授Deepak Pathak与Abhinav Gupta联合创立 [4](https://exponentialindustry.com/ontology/physical-ai-robotics/) |
| **Google DeepMind** | 路线一：跨本体通用大模型 | 云端具身推理（ER 2）+ 全身控制VLA（Robotics 2）+ 端侧小样本快速迁移（On-Device 2）三层协同架构 | Gemini Robotics 2模型家族（2026.07发布，首次实现从脚到22自由度五指手全身控制） | ER 2通过Google AI Studio开放API；VLA赋能Apptronik、波士顿动力、Agility、Franka等硬件伙伴 | Alphabet内部核心AI研发部门（通过GV与CapitalG外部重仓Apptronik与PI） | 机器人副总裁Carolina Parada、Steven Hansen、Peng Xu等领衔 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai) |
| **NVIDIA** | 路线一：物理世界模型与算力底座 | Cosmos物理世界基础模型（生成式物理合成视频）+ Project GR00T开源人形模型 + Isaac Sim/Lab仿真 + Jetson Thor芯片 | Cosmos 3 Edge、GR00T N1.6（基于Qwen3-VL架构骨干）、Jetson Thor（800 TFLOPS） | 向全球几乎所有主流具身智能企业提供训练GPU、仿真软件栈与机载边缘推理芯片 | 上市巨头生态赋能；旗下NVentures广泛投资Figure AI（拟追加10亿美元）、PI等核心玩家 | 机器人研究团队含Yuke Zhu等知名学者与Isaac工程团队 [4](https://exponentialindustry.com/ontology/physical-ai-robotics/) |
| **Figure AI** | 路线二：软硬一体垂直整合 | 终止OpenAI合作转向全自研Helix端到端VLA神经网络；签约Nscale部署10万张NVIDIA GPU；自建BotQ制造工厂 | Figure 01 -> Figure 02 -> **Figure 03** （2025.10发布，16自由度手）；BotQ规划首期年产1.2万台，四年目标10万台 | 2025.01起产生营收；宝马斯帕坦堡工厂产线常态化部署；签下Catalyst Brands 4,000万美元合同；已部署约**740台机器人** （超越660名员工数） | 累计融资约19亿-25亿美元；2025.09完成超10.6亿-15亿美元C轮，估值达**390亿-395亿美元** （Parkway领投，微软、NVIDIA、Bezos、Brookfield参投） | 连续创业者Brett Adcock（曾创立Vettery、Archer Aviation、Hark）于2022年创立并自资1亿美元种子轮，持股约50% [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive) |
| **Tesla (Optimus)** | 路线二：软硬一体垂直整合 | 复用FSD纯视觉端到端神经网络（像素直接映射关节指令）+ 自研AI5推理芯片 + Grok语音编排 + 车队学习飞轮 | **Optimus Gen 3 (V3)** （2026.01启动量产，22自由度50执行器腱绳灵巧手，1.73m/57kg，20kg负载/150kg硬拉） | 弗里蒙特与得州工厂内部部署**超1,000台** 执行电芯分拣与120磅电池托盘搬运；2026年下单1.5万台零件（年底周产目标2,500台），目标售价2-3万美元 | 特斯拉资产负债表内生支持（2026年全公司CapEx维持200亿美元规模） | Elon Musk领衔，特斯拉Autopilot视觉AI与Optimus硬件工程团队协同研发 [15](https://ifactoryapp.com/industries/automotive-manufacturing/tesla-optimus-fremont-gen-3-humanoid-2026) |
| **1X Technologies** | 路线二：软硬一体垂直整合 | 仿生肌腱驱动轻量化柔顺控制架构 + 早期家庭部署采集非结构化真实长尾数据训练端到端自主模型 | 家庭双足人形机器人 **NEO** （2026.07公布25自由度灵巧手，目标售价2万美元）+ 轮式机器人 **EVE** ；海沃德工厂投建 | EVE在安防与物流商用；与IFS开展工业AI合作；NEO处于早期家庭领养数采测试阶段 | 历史融资约8亿美元（OpenAI早期领投）；2025.09曾寻100亿美元估值；2026.08软银洽谈以**60亿美元** 估值收购控股权 | 挪威机器人专家Bernt Øivind Børnich于2014年创立（前身为Halodi Robotics） [22](https://en.wikipedia.org/wiki/1X_Technologies) |
| **智元机器人 (AgiBot)** | 路线二：软硬一体垂直整合 | 自研PowerFlow关节与19自由度视触觉手 + 3万小时真机预训练世界动作模型 **GE-Act 2.0**  + AIMA开源生态 | 远征A1/A2/A2-W（轮式）/A2-Max（40kg重载）、灵犀X1（全栈开源）/X1-W/X2、精灵G1、绝尘系列 | 2024年下线超千台；A2-W签国内首个工业规模化商业单；**2025年营收超10亿元，2026年目标40亿元** ；2025.11完成股改 | 累计超12轮融资；2026.10完成新一轮10-15亿元融资收尾，最新估值约**500亿元人民币** （腾讯、比亚迪、高瓴、红杉、京东、上汽参投） | 前华为“天才少年”彭志辉（稚晖君）联合创立，前华为高管邓泰华为实控人，姜青松任营销服副总裁 [4](https://exponentialindustry.com/ontology/physical-ai-robotics/) |
| **银河通用 (Galbot)** | 路线三：仿真合成数据端到端 | “银河星坊”AstraSynth百亿级虚实融合合成数据集（Sim-to-Real效率超特斯拉千倍）+ “银河星脑”AstraBrain打通大脑-小脑-神经控制端到端模型 | 轮式双臂人形 **Galbot G1** （售价约70万，2026春晚自主盘核桃/串烤肠）+ 工业重载 **Galbot S1** （50kg负载，售价约105万） | 唯一在宁德时代电池厂常态化自主作业（中标2.36亿项目），签博世、丰田、百达精工（千台协议）；20+城落地超100家“银河太空舱”无人便利店及24城智慧药房 | 累计融资**近70亿元人民币** （国内第一）；2025.12获中移动领投超3亿美元（估值**30亿美元/超200亿人民币** ）；2026.03再获大基金三期、中石化等**25亿元** 融资 | 清华/斯坦福博士、北大EPIC Lab主任王鹤（90后CTO）与北航/前ABB研发骨干姚腾洲联合创立 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560) |
| **宇树科技 (Unitree)** | 路线四：高动态运控+大模型融合 | 全自研高功率密度关节电机/激光雷达 + 强化学习/MPC高动态全身运动控制；引入DeepSeek战略协同大模型大脑 | 四足Go1/Go2/B2；全尺寸人形 **H1** 、高性价比人形 **G1** （9.9万元起售）、H2 | **2025年人形机器人出货超5,500台** （营收占比超51%首超四足）；2025年总营收**17.08亿元** ，毛利率60.13%，**扣非净利润5.91亿元** | **2026年8月19日登陆上交所科创板（688836.SH）** ，募资60.99亿元，发行市值**609.93亿元人民币** （美团、红杉、DeepSeek、社保基金等在列） | 90后创始人王兴兴于2016年创立，直接及间接持股超32%（持股市值超183亿元） [16](https://www.huxiu.com/article/4884048.html) |
| **Boston Dynamics & TRI** | 路线四：高动态运控+大模型融合 | 全电驱超人类灵活度本体 + MPC/强化学习 + 联合丰田研究院（TRI）开发**大行为模型（LBM）**实现全身移动操作单一策略控制 | **Electric Atlas** （身高1.5m/75kg，360°关节旋转，7自由度夹爪，30Hz视觉输入预测48步动作块） | Spot与Stretch已商业化；Electric Atlas目前作为高端研发与验证平台在现代汽车工厂开展零件分拣实测 | 现代汽车集团控股支持；与TRI及Google DeepMind深度研发结盟 | 波士顿动力Scott Kuindersma与TRI Russ Tedrake教授联合指导LBM项目 [3](https://www.tri.global/news/ai-powered-robot-boston-dynamics-and-toyota-research-institute-takes-key-step-towards-general) |
| **Apptronik** | 路线四：高可靠本体+外部大模型 | 源自NASA Valkyrie的模块化免工具快换硬件架构（20分钟维修恢复）+ 深度集成 **Google DeepMind Gemini Robotics 2**  大脑 | **Apollo**  与 **Apollo 2** （25kg负载，22自由度灵巧手，小于5分钟热插拔换电） | 在梅赛德斯-奔驰（柏林与匈牙利工厂）、GXO Logistics及代工巨头Jabil开展产线试点与Robot Park数采；预计2027-2029年大规模商用 | 2026.02完成5.2亿美元A-X轮，A轮系列总额超**9.35亿美元** （累计融资10-13亿美元），估值**53亿-55亿美元** （B Capital、Google、奔驰、QIA参投） | CEO Jeff Cardenas及UT Austin人类中心机器人实验室（NASA Valkyrie团队）于2016年创立 [6](https://dealroom.co/news/125782-apptronik-raises-520m-at-5-5b-valuation-to-scale-humanoid-robot-apollo/) |
| **优必选 / 逐际动力 / 星尘智能** | 路线四：本体运控与传动创新 | 优必选：伺服驱动与双足稳定步态；逐际动力：全地形高动态运控；星尘智能：全球首创量产**绳驱（肌腱仿生）**力控传动 | 优必选：**Walker S / S1** ；逐际动力：双足**TRON 1** 、全尺寸人形**CL-1** ；星尘智能：绳驱机器人**Astribot S1** | 优必选：进蔚来/东风实训（效率达人工30-40%，2026目标出货3,000台）；逐际动力：TRON 1全球商业交付闭环；星尘智能：绳驱量产交付 | 优必选：港股上市（2025扣非净利率-35.71%）；逐际动力：半年融资4亿美元，估值**150亿元** ；星尘智能：新一轮融资10亿元，估值**150亿元** | 优必选：谭旻、焦继超等高管团队；逐际动力：南科大教授张巍创立；星尘智能：前腾讯Robotics X专家来杰创立 [17](https://pdf.dfcfw.com/pdf/H3_AP202605071822028328_1.pdf?1778171901000.pdf) |

基于上述全局数据与产业演进态势，可提炼出决定未来三至五年全球具身智能竞争终局的三大深层演进规律：

### 一阶与二阶数据范式博弈：从暴力遥操作向虚实融合、人类视频自监督与在线强化学习跃迁

当前具身智能行业的最大共识在于模型架构已初步收敛于VLA与世界模型，但最大分歧在于如何跨越“物理数据鸿沟” [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。以Tesla、Figure及智元机器人为代表的垂直整合派，正通过千台级自有或合作产线机群与大规模人工遥操作构建高达数万小时的真机操作数据集（如智元GE-Act 2.0基于3万小时真机数据验证Scaling Laws） [4](https://exponentialindustry.com/ontology/physical-ai-robotics/)。然而，纯真机遥操作存在显著的边际成本递增与人类操作速度上限约束 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。为此，2026年的前沿技术突破正指向三条低成本破局路径：其一是以银河通用AstraSynth与NVIDIA Cosmos/Isaac为代表的物理对齐合成数据范式，通过在虚拟空间遍历百亿级长尾场景将真机数据需求压缩两个数量级以上 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)；其二是以Physical Intelligence在$\pi^*_{0.6}$与RL Tokens中验证的在线强化学习微调（Online RL Post-Training），让机器人在自主练习中从自身错误学习，从而在推理速度和接触精度上超越人类遥操作员的生理极限 [21](https://www.humanoidsdaily.com/companies/physical-intelligence)；其三则是大规模模型在达到特定参数阈值后涌现出的无标定人类第一视角视频迁移能力，一旦该能力彻底成熟，互联网上海量的人类日常劳作视频将直接转化为机器人动作先验，彻底重塑行业的数据护城河结构 [21](https://www.humanoidsdaily.com/companies/physical-intelligence)。

### 价值链分配与生态终局博弈：PC与智能手机式的水平解耦还是智能汽车式的垂直闭环

资本市场目前同时给予了水平大脑公司（Skild AI估值140亿美元、Physical Intelligence估值56亿至110亿美元）与全栈垂直整合公司（Figure估值390亿美元、智元估值500亿元人民币）极高的溢价，这实际上隐含了两套截然不同的终局假设 [7](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)。水平赋能派押注的是重演PC时代与智能手机时代的历史：硬件本体因中国供应链（如宇树科技将人形整机价格压至9.9万元、智元开源灵犀X1）的极致降本而迅速商品化，软件模型层凭借跨本体泛化能力通吃全球利润 [12](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)。然而，物理世界的动力学交互远比二维屏幕的信息交互复杂——不同机器人的关节间隙、线缆柔顺度、传动延迟与22至25自由度灵巧手的触觉反馈高度异构，这导致通用大脑在跨本体迁移时往往面临严峻的精度折损（如Gemini Robotics 2在精细拧入灯泡和清扫任务上仅30%余的成功率） [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。因此，在2026至2028年的中早期商业化阶段，像Figure、Tesla、银河通用这样能够针对特定本体与特定工业场景进行“端到端模型+专用硬件构型”联合调优的垂直整合或半整合企业，在作业节拍、成功率与工程可靠性上展现出更强的商业交付确定性；而以Skild AI（10个月ARR破1亿美元）与Apptronik+DeepMind联盟为代表的“强泛化大脑+模块化标准硬件”模式，则正在标准化程度较高的物流分拣、机柜装配与线束作业中快速撕开水平化商业变现的裂口 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。

### 商业化跨越鸿沟的硬约束：从情绪与科研价值向80%人工效率临界点的惊险一跃

2026年全球具身智能产业最核心的二阶财务信号，体现在宇树科技、银河通用与Figure AI三家领军企业的商业化结构对比之中。宇树科技凭借近17亿元营收与近6亿元扣非净利润成功登陆科创板，证明了高性价比运动本体在科研教育、商业展演与开发者生态中的巨大吸金能力，但其2026年一季度销售费用激增与利润增速回落亦发出预警：单纯依赖B端展演、注意力经济与高校采购存在明显的市场饱和天花板 [16](https://www.huxiu.com/article/4884048.html)。真正能够支撑数千亿乃至万亿市值的唯有工业制造、仓储物流与商业服务中的严肃生产力替代 [1](https://caifuhao.eastmoney.com/news/20260305164448808529560)。目前，即便在宝马、奔驰、蔚来、宁德时代与特斯拉超级工厂的标杆试点中，双足人形机器人的综合产线作业效率普遍仍处于人类熟练工人的30%至40%区间，且面临续航时间（普遍4至8小时）、高自由度灵巧手寿命及非标异常处理（Intervention Rate）的严峻挑战 [13](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)。由此可见，2026年底至2027年将是全球具身智能商业化验证的决战窗口：谁能率先通过轮式双臂或双足全身VLA协同将单工位连续无故障作业效率提升至人类工人的80%以上，并将整机BOM成本压缩至2万至5万美元（15万至35万元人民币）的工业投资回报率（ROI）平衡线以内，谁就能率先脱离“股东即客户”的早期关联交易温室，真正开启全球通用具身劳动力的大规模替代浪潮 [23](https://optimusk.blog/blog/what-is-tesla-optimus/)。

## Sources used in the report

1. [三年融资70亿估值200亿，银河通用携“国家队”掀起具身智能资本狂潮](https://caifuhao.eastmoney.com/news/20260305164448808529560)
2. [重磅发布｜具身智能领域十大科技进展（2025-2026）](https://www.industrysourcing.cn/article/477359)
3. [AI-Powered Robot by Boston Dynamics and Toyota Research](https://www.tri.global/news/ai-powered-robot-boston-dynamics-and-toyota-research-institute-takes-key-step-towards-general)
4. [Physical AI & Embodied Robotics - Exponential Industry](https://exponentialindustry.com/ontology/physical-ai-robotics/)
5. [The Industrialization of Embodied Robotic Intelligence - Medium](https://medium.com/cathay-innovation/the-industrialization-of-embodied-robotic-intelligence-6d54374ed8f3)
6. [Apptronik raises $520M at $5.5B valuation to scale humanoid robot](https://dealroom.co/news/125782-apptronik-raises-520m-at-5-5b-valuation-to-scale-humanoid-robot-apollo/)
7. [Figure AI: Inside the $39B Humanoid Robotics Company](https://valueaddvc.com/blog/figure-ai-humanoid-robotics-company-deep-dive)
8. [2026年具身智能产业发展研究报告（附下载） - 智教新媒](https://www.iedumedia.com/news/newsinfo/1695)
9. [宇树上市610亿后，王兴兴想让机器人长出大脑 - 投资界](https://news.pedaily.cn/202608/567833.shtml)
10. [逐际动力创始人张巍：不跟风、不内卷，我们在「造新物种」 - 36氪](https://m.36kr.com/p/3668859815158405)
11. [Physical Intelligence (π) — Complete Profile & Analysis 2026](https://www.roboticscenter.ai/companies/physical-intelligence)
12. [Physical Intelligence: $5.6B Now, $11B Round in Talks](https://valueaddvc.com/blog/physical-intelligence-valuation-2026-robot-foundation-models)
13. [Gemini Robotics 2: Google DeepMind's Humanoid Robot AI - Blog](https://blog.robozaps.com/b/gemini-robotics-2-humanoid-robot-ai)
14. [智元机器人深度拆解：人形机器人独角兽进化论 - 36氪](https://m.36kr.com/p/3261349018468489)
15. [Tesla Optimus at Fremont: Gen 3 Humanoid Deployment & Mass](https://ifactoryapp.com/industries/automotive-manufacturing/tesla-optimus-fremont-gen-3-humanoid-2026)
16. [宇树的悬念还在后面 - 虎嗅网](https://www.huxiu.com/article/4884048.html)
17. [2026 年智能机器人行业深度分析报告](https://pdf.dfcfw.com/pdf/H3_AP202605071822028328_1.pdf?1778171901000.pdf)
18. [星尘智能完成新一轮融资，公司估值达150亿元 - 凤凰网](https://feng.ifeng.com/c/8xCD4divDk7)
19. [Boston Dynamics Atlas (Electric) - UK Humanoid Robot](https://humanoidrobotsuk.com/robots/atlas)
20. [Apollo at Mercedes-Benz: Apptronik's Humanoid Auto ... - iFactory AI](https://ifactoryapp.com/industries/automotive-manufacturing/apollo-mercedes-apptronik-humanoid-automotive)
21. [Physical Intelligence — company profile, robots and news](https://www.humanoidsdaily.com/companies/physical-intelligence)
22. [1X Technologies - Wikipedia](https://en.wikipedia.org/wiki/1X_Technologies)
23. [What Is Tesla Optimus? Complete Guide (2025–2026) - optimusk.blog](https://optimusk.blog/blog/what-is-tesla-optimus/)
24. [银河通用：成立34个月、6轮融资70亿——具身智能赛道「资金收割机](https://m.36kr.com/p/3978672823417862)
25. [Large Behavior Models and Atlas Find New Footing | Boston](https://bostondynamics.com/blog/large-behavior-models-atlas-find-new-footing/)
26. [Apptronik Apollo Review 2026: Price, Apollo 2 & Deployments - Blog](https://blog.robozaps.com/b/apptronik-apollo-review)
27. [Physical Intelligence Is Raising Another $1B - The Mimic](https://themimic.io/articles/physical-intelligence-1b-funding-humanoid-robots-2026)
28. [Physical Intelligence Raises $400 Million At $2.4 Billion Valuation](https://pulse2.com/physical-intelligence-raises-400-million-at-2-4-billion-valuation-to-develop-ai-for-robotics/)
29. [Who owns Physical Intelligence (Pi)? Ownership structure explained](https://www.revenuememo.com/p/who-owns-physical-intelligence)
30. [Physical Intelligence eyes $1B raise at $11B valuation, Founders](https://techfundingnews.com/physical-intelligence-1b-raise-11b-valuation-founders-fund-lightspeed/)
31. [Blog | Skild AI](https://www.skild.ai/blogs)
32. [NVIDIA Isaac AI robot development platform](https://developer.nvidia.com/isaac)
33. [Gemini Robotics - Wikipedia](https://en.wikipedia.org/wiki/Gemini_Robotics)
34. [Google DeepMind's Robotics Lead on Gemini Physical AI Push](https://www.automate.org/robotics/industry-insights/rip-it-up-and-start-again-google-deepmind-vp-on-rewriting-the-rules-of-robotics)
35. [Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)
36. [Gemini Robotics 2: The AI That Gives Robots a Brain - Labellerr](https://www.labellerr.com/blog/gemini-robotics-2-google-deepmind/)
37. [Gemini Robotics 2 - Google DeepMind](https://deepmind.google/models/gemini-robotics/vla/)
38. [Gemini Robotics On-Device 2 - Google DeepMind](https://deepmind.google/models/gemini-robotics/on-device/)
39. [NVIDIA Details Open-Source GR00T N1 Foundation Model and](https://www.humanoidsdaily.com/news/nvidia-details-open-source-gr00t-n1-foundation-model-and-hover-controller-for-humanoids)
40. [Physical AI in 2026: Definition, VLA Models, Data & Build Workflow](https://www.roboticscenter.ai/blog/physical-ai-2026-guide)
41. [Nvidia Isaac GR00T Developer Guide for Humanoid Robot](https://www.facebook.com/NVIDIARobotics/videos/want-to-learn-how-to-develop-a-humanoid-robot-end-to-end-heres-a-developer-guide/1866019701398646/)
42. [Develop Humanoid Robot Policies End-to-End with NVIDIA Isaac](https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/)
43. [VLA Models Compared: GR00T, Gemini Robotics, Pi0 (2026)](https://iotdigitaltwinplm.com/vla-models-comparison-groot-gemini-robotics-pi0-2026/)
44. [Figure AI valuation, funding & news | Sacra](https://sacra.com/c/figure-ai/)
45. [Nvidia Reportedly Eyes Another $1B Investment in Figure AI's](https://www.eweek.com/news/nvidia-figure-ai-1-billion-investment-humanoid-robots/)
46. [Figure AI Stock: $39B Valuation — Is It a Buy? | TSG Invest](https://tsginvest.com/figure-ai/)
47. [Figure AI • Pre-IPO Unicorns - HUDSONPOINT capital](https://hudsonpoint.com/pre-ipo/figure-ai)
48. [Research Figure AI's founding story, leadership team, funding](https://www.useluminix.com/reports/company-overviews/figure-robotics-company-overview-may-2026/source/0)
49. [Brett Adcock - Forbes](https://www.forbes.com/profile/brett-adcock/)
50. [Figure AI: Funding, Team & Investors | Startup Intros](https://startupintros.com/orgs/figure-ai)
51. [Figure AI - Company Profile, Milestones & Funding - Venture Atlas](https://www.ventureatlas.org/company/figure-ai)
52. [Brett Adcock's Stealthy AI Startup Hark Raises $700 Million at a $6](https://fundraiseinsider.com/blog/brett-adcocks-stealthy-ai-startup-hark-raises-700-million-at-a-6-billion-valuation/)
53. [Tesla Optimus (Gen 3) - Robot Details, Use Case and Specifications](https://www.aparobot.com/robots/tesla-optimus)
54. [From Stage Prop to Factory Floor: Optimus Gen 3 Begins Real Work](https://www.teslaacessories.com/nb/blogs/news/from-stage-prop-to-factory-floor-optimus-gen-3-begins-real-work-at-giga-texas)
55. [Tesla Optimus: generations, specs and latest news | Humanoids Daily](https://www.humanoidsdaily.com/robots/tesla-optimus)
56. [Tesla Optimus Review (2026): Capabilities & Availability](https://antonrobots.com/tesla-optimus-review/)
57. [8 Physical AI Startups to Watch: Figure, Apptronik & the Robot](https://unicornscreener.vc/blog/8-physical-ai-startups-racing-to-build-the-robot-economy)
58. [1X Technologies Company Profile: Founders, Funding, Humanoid](https://embodyvc.com/companies/1x-technologies/)
59. [Humanoid Robots 2026: Deployments, Cost, TAM - Analysis Atlas](https://analysis-atlas.com/research/humanoid-robotics-commercialization-market/)
60. [1X - 2026 Company Profile, Team, Funding, Competitors & Financials](https://tracxn.com/d/companies/1x/__LHsrSyi_fXuqm41b2urwiNEhmn9qEjCh1Md-w2ep8KE)
61. [SoftBank in talks to buy majority stake in 1X at $6B valuation](https://techfundingnews.com/softbank-in-talks-to-buy-majority-stake-in-1x-at-6b-valuation/)
62. [智元](https://pdf.dfcfw.com/pdf/H3_AP202507221713451794_1.pdf?1753180160000.pdf)
63. [90后华为天才少年做机器人，一年估值70亿 - 新浪财经](https://finance.sina.com.cn/wm/2024-09-01/doc-incmscvm8749778.shtml)
64. [智元机器人的百亿人才局：一个华为系掌舵的资本化“产业实验体”](https://finance.sina.com.cn/jjxw/2026-08-05/doc-inimfwqp4650448.shtml)
65. [密集对外投资、规模化商业签单！智元机器人的商业化新突破 - 财联社](https://www.cls.cn/detail/2112128)
66. [两年三次募资，协作机器人第一股越疆科技从港回A - 财经](https://finance.ifeng.com/c/8vRPAPwwHEL)
67. [智元机器人：一场华为式创业的赌局 - 蓝鲸财经](https://www.lanjinger.com/d/1776476087113121960)
68. [拆解智元：一台机器人，三份收入，一张资本网 - ME News](https://www.me.news/contents/282700)
69. [智元启动新一轮融资，估值约500亿元 - 网易新闻](https://c.m.163.com/news/a/L96SCAM505118I96.html)
70. [银河通用的200亿估值，是订单堆的还是资本堆的？ - 虎嗅网](https://www.huxiu.com/article/4894444.html)
71. [讯飞、美团押注的人形机器人公司，估值200亿，超越宇树 - AgeClub](https://m.ageclub.net/article-detail/7856)
72. [银河通用200亿估值背后：为什么"不那么复杂"的场景反而能赢？](https://finance.sina.com.cn/cj/2025-12-19/doc-inhckerz7419070.shtml)
73. [重估宇树 - 澎湃新闻](https://m.thepaper.cn/newsDetail_forward_33784711)
74. [宇树科技610亿估值落地，又一场顶级财富盛宴来了 - 21财经](https://m.21jingji.com/article/20260807/herald/73fd8031f9dbf944f4928435d23374d4.html)
75. [宇树科技IPO，五个关键判断-钛媒体官方网站](https://www.tmtpost.com/8108156.html)
76. [宇树会破发吗？王兴兴回应了 - 量子位](https://www.qbitai.com/2026/08/470307.html)
77. [宇树今日登科技陆科创板A股“人形机器人第一股”来了](https://jrj.sh.gov.cn/ZXYW178/20260819/754240ae6aa1482097d92a380fb45086.html)
78. [Toyota and Boston Dynamics Collaborate on an AI Robot](https://www.valleyhitoyota.com/toyota-and-boston-dynamics-collaborate-on-an-ai-robot/)
79. [Boston Dynamics Atlas Humanoid Completes Tasks With Embodied AI](https://www.automate.org/robotics/industry-insights/man-with-hockey-stick-cant-stop-boston-dynamics-atlas-from-completing-complex-tasks/aph)
80. [Apptronik Closes Over $935 Million Series A](https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a)
81. [Apptronik valuation, funding & news | Sacra](https://sacra.com/c/apptronik/)
82. [Insights: How To Invest In Apptronik Stock Pre-IPO - Forge Global](https://forgeglobal.com/insights/how-to-invest-in-apptronik-stock-pre-ipo/)
83. [Apptronik Valuation, Funding & Investors - Multiples.vc](https://multiples.vc/private-comps/apptronik)
84. [Apptronik — company profile, robots and news | Humanoids Daily](https://www.humanoidsdaily.com/companies/apptronik)
85. [图解2025｜人形机器人跑起来了，中国科技产业迈出坚实一步](https://m.thepaper.cn/newsDetail_forward_32077445)
86. [985教授们集体创业做具身智能，今年已拿下超百亿元融资 - 36氪](https://m.36kr.com/p/3957428318928264)
87. [AI 驱动具身智能，打造物理世界的AGI 泛化基座 - 逐际动力](https://www.limxdynamics.com/zh/news/BK000060)
88. [机器人创企半年融资5亿，阿里、蔚来、上汽都投了 - 澎湃新闻](https://m.thepaper.cn/newsDetail_forward_30320504)
89. [深圳70+人形机器人产业链企业一览](https://www.aibangbots.com/a/2005)
90. [估值达150亿元！深圳人形机器人公司，被中东、欧美资本抢着投 - 搜狐](https://m.sohu.com/a/1050303088_115433?scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334)
91. [百亿级具身智能独角兽逐际动力成为中国机器人产业 ... - AIROBO.RUN](https://www.airobo.run/2026/08/20/airobo-news-65d84f013845/)
92. [Tesla Optimus Review 2026: Price, Gen 2 & Is It For Sale Yet? - Blog](https://blog.robozaps.com/b/tesla-optimus-gen-2-review)
