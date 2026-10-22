# 全球量子网络研究课题组格局与十大最具引领潜力课题组评估（2026年10月版）

**核心结论：截至2026年10月，最有可能引领未来量子网络发展的课题组是中国科学技术大学潘建伟团队（含张强、包小辉、彭承志等子团队）和荷兰QuTech/代尔夫特理工大学的Hanson–Wehner团队。两者分列第一、二位，哈佛大学Lukin组（与AWS深度绑定）列第三。** 中科大的优势在于“天地一体”规模、存储型中继里程碑与国家级持续投入；QuTech的优势在于全栈（硬件+协议栈+操作系统）与欧盟量子互联网联盟（QIA）的牵头地位。第4–10位依次为：因斯布鲁克Northup/Lanyon离子网络组、牛津Lucas离子组、清华段路明组、慕尼黑Rempe/Weinfurter原子网络集群、美国NSF量子网络中心（Guha，现总部马里兰）、加州理工Faraon稀土组、ICFO de Riedmatten固态存储组。

## TL;DR

- **第一梯队（综合分≥85）：** 中科大潘建伟团队（95.0）、QuTech Hanson–Wehner（90.0）、哈佛Lukin（86.5）。三者均在2024–2026年于Nature/Science发表网络级里程碑，并各自绑定国家级或产业级的持续资金。QIA于2026年10月获欧盟委员会4750万欧元（42个月）新资助；\[1\]中科大则依托合肥国家实验室与国家广域量子骨干网（据科学网2025年6月报道，已建成约1.2万公里）。
- **第二梯队（约66–79分）：** 以“离子/原子节点+分布式量子计算”为主线，代表包括因斯布鲁克（QIA原型网络落地地，获540万欧元）、牛津（2025年Nature首次跨光网络链路的分布式量子算法）、清华段路明（多路复用离子节点）、慕尼黑（单原子33 km/101 km）。另有偏架构与理论的美国CQN（2026年获1860万美元四年续期，覆盖2026年9月至2030年8月）、偏固态存储的加州理工Faraon和ICFO。
- **判断：** 未来5–10年的竞争焦点将从“比距离”转向三件事：存储寿命超过纠缠建立时间的可级联中继段、多节点可编程全栈网络、QPU间互联。押注单一物理平台风险高，具备“平台+协议栈+现场光纤+产业伙伴”四要素的团队最可能胜出。

---

## 一、评估方法与评分框架

### 1.1 维度与权重

| 维度 | 权重 | 评估要点 |
|---|---|---|
| A. 学术产出与里程碑（期刊/会议等级） | 25% | 2021–2026年Nature/Science/Nature Physics/Nature Photonics/PRL/PRX/PRX Quantum旗舰论文；是否创造“首次”或纪录 |
| B. 领军人物与团队梯队 | 15% | 院士/讲席/大奖、平台专长、跨学科（物理+网络+工程）、是否已形成“学派”（弟子独立成组或创业） |
| C. 经费规模与稳定性 | 15% | 公开金额、持续性、是否有国家实验室/旗舰计划托底 |
| D. 纵向项目与国家战略牵引 | 10% | 是否牵头国家级/跨国联盟（QIA、NSF ERC、UK Hub、国家重大专项） |
| E. 横向项目与产业转化 | 10% | 与运营商/云厂商/设备商的联合实验、衍生企业、技术转让 |
| F. 网络规模与工程成熟度 | 15% | 节点数、现场光纤/卫星链路、距离、速率、保真度、TRL |
| G. 近两年势头（2024–2026） | 10% | 新成果密度、新资助、人员流动 |

每个维度按1–10分打分，加权后乘以10得到百分制综合分。

### 1.2 数据来源与局限

- 主要依据：论文原文与出版社页面（Nature、Science/Science Advances、APS、npj）、arXiv预印本、大学与研究机构新闻稿、资助方公告（UKRI、NSF、欧盟/QIA、JST/内阁府）、企业公告，以及少量行业媒体报道。凡来自二手来源的数据，文中均已注明。
- **局限一：** 多数课题组的经费与人员规模**未公开**。中国合肥国家实验室和“科技创新2030—量子通信与量子计算机”重大项目（2021ZD03xxxxx）均无公开预算，美国、欧洲单个PI的经费总额也很少公开。因此维度C部分依赖可观察的代理指标，如是否牵头大型联盟、是否依托国家实验室。
- **局限二：** 我们未能系统获取各PI的Google Scholar h指数，故未把h指数作为硬性计分项。
- **局限三：** 评分本身含主观判断，权重变化会改变第4–10名的相对位置。第4–7名分差仅约5分，应视为同一梯队。

---

## 二、全球量子网络研究格局总览

### 2.1 按地区

**欧洲：协同最好、全栈最完整。**
- 欧盟量子旗舰下的QIA由QuTech的Stephanie Wehner任主任；据Qblox与因斯布鲁克大学2026年10月的发布，QIA是由代尔夫特理工牵头、50余家欧洲机构组成的伙伴关系。第一阶段（SGA1）从2022年10月持续到2026年3月。\[1\]2026年10月，QIA获得SGA2资助4750万欧元，为期42个月，目标是建成“完整、可编程、可运行应用”的全栈量子互联网原型，并演示用量子中继连接两个城域网。\[2\]\[3\]
- 原型网络落地因斯布鲁克：采用囚禁离子节点组成两个城域网；按Tracy Northup对奥地利广播公司蒂罗尔台（ORF Tirol，2026年10月）的说法，将把两个城域级离子阱量子计算机网络跨越数百公里连接起来，初期链路为实验室内的盘纤。因斯布鲁克大学与AQT获得其中540万欧元。Fraunhofer ILT负责低噪声量子频率转换，并在亚琛提供基于NV节点的开放测试平台ALICE。\[4\]
- 英国于2024–2025年启动集成量子网络（IQN）枢纽，由Heriot-Watt大学Gerald Buller牵头，汇集12所合作大学、NPL、STFC RAL Space及40余家产业伙伴。\[5\]
- 德国以慕尼黑（MPQ/LMU/MCQST）为单原子网络重镇；瑞士ETH在超导微波链路上领先；西班牙ICFO与日内瓦在稀土固态存储上领先。

**北美：顶尖PI密度最高，产业绑定最深。**
- 哈佛Lukin组与AWS量子网络中心联合完成波士顿35 km部署光纤双节点网络（Nature 2024）。\[6\]\[7\]
- 加州理工Faraon组在Nature 2025实现稀土多发射体节点的复用纠缠；\[8\]\[9\]\[10\]普林斯顿Thompson组在PRX 2025实现电信波段单铒离子自旋–光子纠缠。\[11\]\[12\]
- NSF量子网络工程研究中心（CQN）于2020年以亚利桑那大学为总部启动（首期2600万美元），2026年8月获1860万美元四年续期（2026年9月至2030年8月），总部迁至马里兰大学，仍由Saikat Guha领导。
- 芝加哥/阿贡、Stony Brook/布鲁克海文、橡树岭等国家实验室测试床亦在运行。受检索预算所限，本报告未逐一核实其2025–2026年最新进展，详见“注意事项”。

**中国：规模与工程化全球第一，存储型中继正快速追赶。**
- 中科大潘建伟团队覆盖面最全：卫星（墨子号、济南一号）、光纤骨干（京沪干线、国家广域骨干网）、双场QKD纪录、冷原子存储型中继。
- 济南一号微纳卫星的实时QKD发表于Nature 2025，实现北京—南非斯泰伦博斯1.29万公里的密钥共享。\[13\]\[14\]
- 2026年，团队在Nature发表“量子中继构建模块”：10 km光纤上存储器–存储器纠缠的相干时间（550±36 ms）首次超过平均纠缠建立时间（450 ms）。\[15\]\[16\]\[17\]同年又在PRL发表420 km光纤连接的原子系综存储器纠缠。\[18\]
- 清华段路明组在离子网络节点上形成独立的技术路线。
- 产业侧：据国资委通报，中电信量子集团于2023年5月在合肥成立，注册资本30亿元，为中国电信股份有限公司全资子公司；据21世纪经济报道（2025年1月），该集团认购国盾量子17.75亿元股份，直接持股21.86%，并通过与科大控股、彭承志的一致行动协议控制国盾量子40.43%的表决权。

**亚太其他：**
- 日本以NICT东京QKD网络（2010年起运行，覆盖东京中心约100 km范围）为工程基础。\[19\]登月计划目标6支持了大阪大学山本俊（Yamamoto Takashi）、横滨国立大学小坂英男（Kosaka Hideo）、庆应义塾大学永山翔太（Nagayama Shota）/Rodney Van Meter等网络类项目。\[20\]\[21\]2025年10月公布的第二阶段中，唯一的网络型项目是山本俊的“容错网络型量子计算机”。\[22\]
- 新加坡CQT/SpeQtral、澳大利亚ANU、韩国KIST/ETRI、印度RRI等也有布局，但本次检索未获取足以支撑进入前十的2024–2026年旗舰成果。

### 2.2 按技术路线

| 技术路线 | 代表团队 | 2024–2026年代表性节点事件 | 成熟度判断 |
|---|---|---|---|
| 固态色心节点（NV/SiV） | QuTech Hanson；哈佛Lukin；斯图加特Wrachtrup | Delft–海牙25 km部署光纤预示纠缠（Sci. Adv. 2024）；\[23\]\[24\]波士顿35 km SiV双节点（Nature 2024）；QNodeOS（Nature 2025） | 城域双节点已成；多节点+城域仍是难点 |
| 囚禁离子节点 | 因斯布鲁克Northup/Lanyon；牛津Lucas；清华段路明；杜克/马里兰（IonQ系） | 牛津分布式量子计算（Nature 2025）；因斯布鲁克50 km中继节点（PRL 2023）与101 km离子–光子纠缠（PRX Quantum 2024）；\[25\]\[26\]清华12 km级多路复用节点、1.2 km离子–离子复用纠缠\[10\]\[27\] | 门保真度最高；距离靠频率转换；最适合QPU互联+城域 |
| 中性原子/腔QED | MPQ Rempe；LMU Weinfurter；（芝加哥Bernien、伊利诺伊Covey等） | 33 km单原子纠缠（Nature 2022）；24 km部署光纤原子–光子纠缠（PRL）；三节点单原子纠缠预印本（2026）\[28\]\[29\]\[30\] | 可与原子阵列计算机结合，潜力大 |
| 冷原子系综存储 | 中科大包小辉/潘建伟；清华段路明（早期） | 城域存储器–存储器纠缠（Nature 2024）；“寿命>建立时间”构建模块（Nature 2026）；\[17\]420 km（PRL 2026） | 当前最接近“可级联中继段” |
| 稀土掺杂固态 | ICFO de Riedmatten；加州理工Faraon；普林斯顿Thompson；日内瓦Afzelius；ANU | 稀土多发射体复用纠缠（Nature 2025）；按需自旋波存储预示纠缠（PRX 2025）；Er:CaWO₄电信波段自旋–光子纠缠（PRX 2025）\[10\]\[31\]\[32\] | 多模复用最强；单体节点处理能力较弱 |
| QKD骨干与卫星 | 中科大；东芝欧洲剑桥实验室；日内瓦/IDQ；NICT；帕多瓦；滑铁卢IQC | 济南一号1.29万公里（Nature 2025）；东芝254 km商用网双场QKD（Nature 2025）\[33\] | 已商用；当前增长点为与经典网络融合 |
| 超导微波互联 | ETH Wallraff；MIT Oliver；耶鲁 | 30 m低温链路无漏洞贝尔检验（Nature 2023）；模块化低温链路（arXiv 2026）\[34\]\[35\]\[36\] | 机房尺度；需微波–光转换才能走出机房 |
| 架构/协议/理论 | QuTech Wehner；CQN（Guha、Towsley）；庆应Van Meter；约克Pirandola | QNodeOS；IETF QIRG多平面架构草案；CQN续期 | 决定“谁定义量子互联网标准” |

---

## 三、重点课题组画像

> 说明：“已核实”指本次研究从原始论文或官方发布中直接获得；“未公开”指未检索到可靠数字。

### 3.1 中国科学技术大学 潘建伟团队（合肥国家实验室；张强、包小辉、彭承志、廖胜凯等）

- **领导者：** 潘建伟，中国科学院院士，量子光学与量子信息学科带头人。核心子团队分工如下：
  - 张强：光纤QKD与中继；
  - 包小辉：冷原子存储型中继；
  - 彭承志、廖胜凯：卫星量子通信；
  - 陆朝阳：光量子计算与光源。
  团队已形成全球规模最大、分工最细的“学派”式体系，弟子遍布中科大、济南量子技术研究院、清华等。
- **代表性成果（期刊等级）：**
  - Nature 2021：4600 km天地一体化量子通信网络；
  - PRL 2023：双场QKD突破1000 km光纤；\[37\]
  - Nature 2024：城域存储器–存储器纠缠；\[38\]\[39\]
  - Nature 2025（3月）：济南一号微纳卫星与多个移动地面站实时QKD，北京—斯泰伦博斯1.29万公里；\[13\]
  - Nature 2026（arXiv 2602.08472，Wen-Zhao Liu等29位作者）：10 km光纤上纠缠相干时间550±36 ms，超过450 ms的平均建立时间，并据此演示长距离设备无关QKD（DI-QKD）。\[16\]\[17\]Hanson与Northup在Nature配发评论，称这是首次在长距离链路上实现“纠缠生成快于衰减”。\[15\]
  - PRL 2026（8月）：两原子系综存储器经420 km光纤纠缠。需注意，两端节点位于同一实验室，光纤为盘纤，独立评论认为不宜直接称为“中继段”。\[18\]
- **经费与纵向项目：**
  - 合肥国家实验室为中央预算单位，具体预算**未公开**。其招聘公告显示：本部占地730亩，在北京、上海、济南、深圳设基地；实验型人才启动经费可达“国家支持200–300万元+实验室600万元”。\[40\]
  - “科技创新2030—量子通信与量子计算机”重大项目（编号2021ZD03…）金额**未公开**。
  - 安徽省与合肥市自2017年起累计安排近300亿元，支持量子信息、聚变能源、深空探测三大领域。\[41\]此为区域代理数，并非量子专项。
- **横向项目与产业转化：**
  - 国盾量子源自中科大，现由中电信量子集团控制：该集团2023年5月成立，注册资本30亿元，为中国电信全资子公司（国资委通报）；据21世纪经济报道（2025年1月），其认购国盾量子17.75亿元股份，直接持股21.86%，并通过与科大控股、彭承志的一致行动协议控制40.43%表决权。国盾为济南一号实验提供小型移动地面站，并支撑中国电信在40余座重点城市的量子城域网（据二手财报摘要）。
  - 据运营方国科量子，国家广域量子保密通信骨干网一期（总长超过1万公里）于2022年9月建成、同年12月通过验收；科学网2025年6月报道，我国已建成约1.2万公里量子保密通信骨干网，覆盖粤港澳、京津冀、长三角、成渝等区域，另有2颗在轨量子卫星。合肥量子城域网服务500余家党政机关。
  - 有二手资料称CN-QCN已达145个节点、超过1万公里（npj Quantum Information 2025），\[42\]本报告未独立核实节点数。
- **2024–2026动态：** 潘建伟2024年10月称将于2025年发射2–3颗低轨量子卫星，并于2027年左右发射高轨量子卫星，组成星座。**截至本报告，\[43\]未检索到2025年低轨星已发射的权威确认，应视为计划。** 另有维基资料称墨子号于2026年1月再入大气层，\[44\]未获一手来源证实。
- **优势：** 全链条（卫星—骨干—城域—存储中继—光源）、工程化能力、国家级持续投入、产业闭环。
- **风险：** 国际合作受地缘政治限制（不过与南非斯泰伦博斯的合作说明“南南合作”通道仍在）；冷原子系综路线在可集成性上不及固态与离子路线；部分纪录型实验为实验室内盘纤，外推到现场仍需验证。

### 3.2 荷兰 QuTech / 代尔夫特理工大学（Ronald Hanson、Stephanie Wehner、Tim Taminiau）

- **领导者：**
  - Hanson：金刚石NV中心网络开创者，2015年完成首个无漏洞贝尔检验。
  - Wehner：代尔夫特理工量子计算机科学教授、QIA主任，兼具理论计算机科学与网络协议背景。\[45\]
  这种“物理+计算机科学”的双核结构在全球罕见。
- **代表性成果：**
  - Science 2021：首个三节点固态量子网络；\[46\]
  - Nature 2022：非相邻节点间的量子隐形传态；\[46\]
  - Science Advances 2024：Delft–海牙两节点独立运行，经25 km部署光纤（KPN提供光纤与站点）实现预示纠缠，号称量子处理器间的距离纪录；\[23\]\[24\]
  - Nature 2025：首个量子网络操作系统QNodeOS，与因斯布鲁克、INRIA、CNRS合作，并在Delft与因斯布鲁克的处理器上运行。\[45\]\[47\]
- **经费与纵向项目：** QIA SGA2于2026年10月获4750万欧元（42个月），SGA1覆盖2022年10月至2026年3月。QIA资助编号包括H2020 820445、Horizon Europe 101080128/101102140。\[1\]QuTech由代尔夫特理工与TNO共建，并受Quantum Delta NL国家计划支持。具体组内经费**未公开**。
- **横向项目：** KPN（光纤与站点）；Fraunhofer ILT、OPNT、Element Six、Toptica（Delft–海牙链路合作方）；\[24\]\[48\]富士通（QNodeOS论文致谢中的联合项目）。\[49\]衍生/关联企业包括Q*Bird、QphoX等，本报告未逐一核实。“Quantum Network Explorer”演示平台已向外部开放。\[47\]
- **优势：** 唯一同时拥有多节点固态硬件、网络协议栈/操作系统、欧盟联盟牵头权的团队。
- **风险：** 原型网络硬件主体落在因斯布鲁克的离子平台，NV路线自身的速率与多节点扩展仍受限；距离指标落后于中科大。

### 3.3 哈佛大学 Mikhail Lukin组（联合Marko Lončar、Hongkun Park；AWS量子网络中心）

- **领导者：** Lukin为哈佛Joshua and Beth Friedman大学教授、\[50\]哈佛量子计划联合主任，美国国家科学院院士。其研究横跨里德堡原子阵列量子计算（QuEra）与色心量子网络两大方向。
- **代表性成果：**
  - Nature 2020：存储增强量子通信；
  - Nature 2024：SiV纳米光子节点与电信光纤网络集成，经40 km盘纤及波士顿城区35 km部署光纤回路（损耗17 dB）实现核自旋存储器纠缠；\[51\]\[52\]\[53\]\[54\]
  - Science 2025：基于固态量子比特的通用分布式盲量子计算。\[55\]
  另据学位论文，²⁹Si核自旋存储相干时间超过2秒。\[56\]
- **经费：** 作为NSF CQN核心伙伴；AWS提供工程团队与联合研究，具体金额**未公开**。
- **横向项目：** AWS量子网络中心（论文共同作者含AWS研究员），\[6\]这是全球最典型的“大学–云厂商”量子网络横向合作。
- **人才流动：** 加州理工Faraon组的Andrei Ruskuc博士毕业后赴哈佛做博士后，\[57\]显示人才向哈佛集聚。
- **风险：** SiV需毫开级制冷，节点工程复杂度高；与AWS的合作偏中长期研发，现场测试床仍限于双节点。

### 3.4 因斯布鲁克大学 / IQOQI（Tracy Northup、Ben Lanyon；Rainer Blatt传统）

- **代表性成果：**
  - PRL 2023：离子阱电信波段中继节点，将两段25 km纠缠交换为50 km；\[26\]\[58\]
  - PRL 2023：相距230 m的离子比特纠缠；\[59\]\[60\]
  - PRX Quantum 2024：多模离子–光子纠缠传输101 km；\[25\]\[39\]
  - 参与QNodeOS（Nature 2025）。\[47\]
- **经费与纵向项目：** QIA SGA2中，因斯布鲁克大学与AQT获540万欧元，用于把三台离子量子计算机组网，并借助量子中继把两个城域网连接起来；Northup对ORF Tirol（2026年10月）表示两网相距数百公里，初期链路为实验室内的盘纤。**QIA原型网络落地因斯布鲁克**，这是2026年最重要的新增信号。
- **横向项目：** AQT（Alpine Quantum Technologies，Blatt系衍生企业）提供离子硬件。\[61\]
- **风险：** 团队规模与工程化能力需在3.5年内完成大跃升；两城域网的选址与光纤资源尚待落实。

### 3.5 牛津大学 David Lucas组（离子阱量子计算与网络）

- **领导者：** Lucas教授，曾任英国量子计算与模拟枢纽首席科学家。\[62\]
- **代表性成果：**
  - Nature 2022：纠缠光学原子钟组成的初级量子网络；\[25\]
  - Nature 2025（D. Main等）：首次通过光子网络接口把两台离子处理器连成全连接量子计算机，演示量子逻辑门的隐形传态与Grover算法；\[25\]\[63\]\[64\]\[65\]
  - PRX Quantum（即将发表）：光子介导纠缠中反冲误差的校正。\[66\]
  实验系统为“Alice/Bob”双节点，锶离子负责通信、钙离子负责存储与处理。\[66\]
- **经费与纵向项目：** 英国NQTP第三期QCI3枢纽（牛津牵头）与IQN枢纽（牛津为成员）；\[67\]EPSRC“分布式量子计算”项目（EP/W032643/1）相关。\[68\]组内总经费**未公开**。
- **横向项目：** 牛津系衍生企业Oxford Ionics（Chris Ballance等创立）。**据IonQ向美国SEC提交的8-K附件99.1，IonQ于2025年6月9日宣布以10.75亿美元收购Oxford Ionics（约10.65亿美元股票加约1000万美元现金），交易于2025年9月正式完成；牛津物理系称其为牛津量子计算衍生企业迄今最高价值的收购。**
- **风险：** 目前节点间仅为数米光纤，城域化尚未展开；核心人才可能被产业吸走。

### 3.6 清华大学 段路明组（交叉信息研究院；合肥国家实验室）

- **领导者：** 段路明，清华大学C.C. Yao讲席教授。\[69\]他是DLCZ量子中继方案（Nature 2001）的提出者之一，也曾与Monroe合著离子量子网络综述（Rev. Mod. Phys.）。\[60\]
- **代表性成果：**
  - Nature Photonics 2021：存储增强的中继段连接标度；\[70\]
  - PRL 2025：无串扰双离子网络节点；\[71\]\[72\]
  - Nature Physics 2025：可扩展量子网络节点中的混合纠缠与比特翻转纠错；\[71\]
  - Science Advances 2025：功能完备的双类型离子网络节点（离子–光子纠缠保真度93.3%）；\[73\]
  - Nature Communications 2025：5离子混合复用节点，存储相干时间366 ms，超过12 km光纤预期纠缠建立时间234 ms，为离子节点在城域尺度上首次做到这一点；\[25\]\[27\]
  - arXiv 2025：10个时间模式复用，离子–离子纠缠速率提升4.59倍，1.2 km光纤上保真度95.9%。\[10\]\[59\]\[74\]
- **经费与纵向项目：** 科技创新2030重大项目（2021ZD0301604、2021ZD0301102）、清华大学自主科研计划、教育部经费；\[10\]作者单位含合肥国家实验室。\[75\]金额**未公开**。
- **横向项目：** 华翊量子（HYQ Co., Ltd.）作为作者单位出现，\[74\]为离子量子计算产业化载体。
- **风险：** 节点间距离尚在公里级，需要现场光纤与频率转换的工程化突破。

### 3.7 慕尼黑原子量子网络集群（MPQ Gerhard Rempe、LMU Harald Weinfurter；MCQST）

- **代表性成果：**
  - Science 2021：远程量子网络模块间的量子逻辑门（Rempe）；\[39\]
  - Nature 2022：单原子经33 km电信光纤纠缠（Weinfurter）；\[30\]\[65\]
  - PRX Quantum 2024：长寿命存储，原子–光子纠缠传输101 km；\[30\]\[76\]
  - PRL 2025：预示式原子–光子纠缠源（Rempe）；\[30\]\[77\]
  - PRL（2026）：经24 km部署光纤分发原子与近可见光子的纠缠（两组合作）；\[28\]\[29\]\[30\]
  - arXiv 2026：三个远程单原子节点高效纠缠（三比特纠缠生成效率0.16%）。\[28\]\[59\]
- **经费：** 德国联邦教研部（BMBF）QR.X/QR.N等中继联合项目、德国卓越集群MCQST、马普学会。具体金额**未公开**。
- **风险：** 产业化与衍生企业偏弱；德国联邦层面的量子通信资金分散在多个联合体。

### 3.8 美国NSF量子网络工程研究中心（CQN；Saikat Guha，现马里兰大学）

- **领导者：** Saikat Guha，量子信息论与量子光学交叉背景，现任CQN主任、马里兰大学电子与计算机工程系Clark杰出讲席教授（Maryland Today，2026年8月5日）。
- **经费：** 2020年NSF资助2600万美元（5年，另有2460万美元续期选项），总部设在亚利桑那大学，核心伙伴为哈佛、MIT、耶鲁。\[78\]\[79\]2026年8月获1860万美元四年续期，期限为2026年9月至2030年8月（PhoQuS/马里兰大学，2026年8月18日），总部迁至马里兰大学。CQN是NSF ERC历史上首个量子技术中心。
- **研究定位：** 容错量子中继与路由器、与经典互联网兼容的架构、量子网络的社会与经济研究。\[80\]中心在亚利桑那建有测试床，\[81\]与UMass的Don Towsley等在网络理论与协议上合作密切。
- **评价：** 在架构、理论和人才培养上影响大，但旗舰实验成果主要通过合作方（如哈佛Lukin组）实现。

### 3.9 加州理工学院 Andrei Faraon组（稀土离子纳米光子学）

- **领导者：** Faraon，William L. Valentine应用物理与电子工程讲席教授。\[9\]
- **代表性成果：** Nature 2025，以YVO₄中多个稀土离子耦合纳米光子腔构成双节点网络（每节点约20个量子比特），首次在单自旋量子比特网络中实现纠缠多路复用，并制备三离子W态。\[10\]\[82\]Faraon称该平台可扩展到“每节点数百个量子比特”。\[9\]\[57\]\[83\]
- **经费：** IQIM等，具体**未公开**。
- **风险：** 尚无现场光纤测试；骨干成员流向哈佛等机构。

### 3.10 ICFO Hugues de Riedmatten组（固态与原子量子光子学）

- **领导者：** de Riedmatten，ICREA研究教授。
- **代表性成果：**
  - Nature 2021：电信预示的多模固态存储器纠缠；\[31\]\[84\]
  - Nature Communications 2023：长距离复用隐形传态至固态比特；\[84\]
  - PRX 2025：按需自旋波固态存储器的预示纠缠，面向复用量子网络链路；\[31\]\[53\]
  - PRL 2025：腔增强自旋波固态存储；\[31\]\[53\]
  - npj Quantum Information 2025：10单元独立可控固态存储阵列。\[85\]
- **经费：** 欧盟旗舰/QIA、西班牙与加泰罗尼亚政府，具体**未公开**。
- **风险：** 吸收型存储需要外部纠缠光源，节点缺乏本地处理能力。

### 3.11 其他重点团队（未进前十或为产业参照）

**东芝欧洲剑桥研究实验室（Andrew Shields，产业团队）**
- 双场QKD的发明者（Nature 2018）。\[86\]\[87\]
- 2021年在Nature Photonics报道600 km以上量子链路。\[88\]
- 2025年在Nature报道在德国商用电信网上完成254 km双场QKD（法兰克福—克尔，中继站位于Kirchfeld，3节点星形，损耗56 dB，密钥率110 bit/s）。合作方包括GÉANT、PSNC、Anglia Ruskin大学；不同来源分别称网络由德国电信或GÉANT提供，存在表述差异。\[33\]\[89\]\[90\]
- 2025年12月与Quantum Corridor在芝加哥—印第安纳州哈蒙德之间21.8 km商用光纤上实现平均约1.5 Mbps的密钥率。\[91\]
- 若论“相干量子通信的工程化”，东芝在全球首屈一指。但它属企业团队，按本报告规则不进入课题组前十。

**ETH Zürich Andreas Wallraff组**
- 30 m低温微波链路连接两台稀释制冷机，完成超导电路无漏洞贝尔检验（Nature 2023）。\[34\]\[35\]\[36\]
- 2026年在arXiv发表模块化低温链路的工程论文，全链路基础温度低于50 mK。\[92\]
- 这是超导QPU机房级互联的标杆，但难以走出机房。

**普林斯顿 Jeff Thompson组**
- Er³⁺在硅纳米腔中直接于1532.6 nm实现自旋–光子纠缠（PRX 2025）。\[11\]\[12\]
- 该路线可利用硅光子工艺，具备晶圆级扩展前景，是“潜力股”。\[93\]

**英国IQN枢纽（Heriot-Watt Gerald Buller）**
- 总规模超过4200万英镑，其中UKRI出资1950万英镑，40余家产业伙伴出资超过2000万英镑。UKRI公告另列“东道大学与伙伴支持3170万英镑”，\[67\]口径不同。
- 伙伴包括BT、Toshiba Europe、Airbus、NCSC等。\[94\]\[95\]
- Heriot-Watt拥有用于卫星接收的光学地面站（HOGS）。\[96\]

**日本：** NICT东京QKD网络（2010年起；参与方含NEC、东芝、三菱电机、NTT；2025年9月与东芝、NEC完成QKD与400G/800G数据在IOWN APN测试环境中的复用演示）。\[97\]\[98\]登月目标6网络类项目：山本俊（大阪）“联网量子计算机的量子网络空间”（JPMJMS2066，2020–2025）、小坂英男（横滨国大）“量子接口”、永山翔太/Van Meter（庆应）“可扩展鲁棒集成量子通信系统”（新川崎4节点星形测试床）。\[99\]\[100\]\[101\]\[102\]登月计划整体基金为1480亿日元（含全部目标），\[103\]单项目金额**未公开**。

**其他：** 日内瓦（Gisin/Zbinden/Afzelius，IDQ源头）、巴黎（Diamanti、Laurat/Welinq）、哥本哈根NBI（Lodahl、Sørensen）、帕多瓦（Villoresi/Vallone）、滑铁卢IQC（Jennewein，QEYSSat）、斯泰伦博斯（与中科大合作的南半球首个量子卫星链路）、\[104\]芝加哥/阿贡（Awschalom）、MIT（Englund、Oliver）、斯坦福（Vučković）、新加坡CQT（Kurtsiefer、Ling）。均为重要力量，但本轮未获得足以进入前十的2024–2026年网络级旗舰证据。

---

## 四、横向比较总表

| 课题组 | 主平台 | 2024–2026旗舰论文（期刊） | 最大现场/网络规模 | 领军荣誉/头衔 | 经费（公开部分） | 纵向牵头 | 横向/产业 |
|---|---|---|---|---|---|---|---|
| 中科大潘建伟 | 冷原子存储、光纤QKD、卫星 | Nature 2024、Nature 2025、Nature 2026、PRL 2026 | 1.29万公里星地；约1.2万公里骨干网 | 中科院院士 | 国家实验室预算未公开；皖/合近300亿元（三领域） | 国家重大专项、合肥国家实验室 | 国盾量子/中电信量子（注册资本30亿元；控制国盾40.43%表决权） |
| QuTech Hanson–Wehner | NV色心+协议栈 | Sci. Adv. 2024、Nature 2025 | Delft–海牙25 km | QIA主任 | QIA SGA2 4750万欧元（全联盟） | QIA协调方 | KPN、富士通、Fraunhofer |
| 哈佛Lukin | SiV色心 | Nature 2024、Science 2025 | 波士顿35 km | 大学教授、NAS院士 | 未公开 | CQN核心伙伴 | AWS量子网络中心 |
| 因斯布鲁克Northup/Lanyon | 囚禁离子+腔 | PRL 2023、PRX Quantum 2024、Nature 2025（合作） | 50 km中继节点；101 km离子–光子\[25\]\[26\] | — | 540万欧元（QIA SGA2，含AQT） | QIA原型落地方 | AQT |
| 牛津Lucas | 囚禁离子 | Nature 2025 | 实验室双节点（米级） | 原量子计算枢纽首席科学家 | 未公开 | QCI3、IQN成员 | Oxford Ionics（2025年9月被IonQ以10.75亿美元收购） |
| 清华段路明 | 囚禁离子 | Nat. Phys. 2025、PRL 2025、Sci. Adv. 2025、Nat. Commun. 2025 | 12 km级节点；1.2 km离子–离子\[10\]\[27\] | C.C. Yao讲席 | 未公开 | 2030重大专项 | 华翊量子 |
| 慕尼黑Rempe/Weinfurter | 单原子+腔 | PRL 2025、PRL 2026、arXiv 2026 | 24 km部署光纤；33/101 km\[29\]\[30\] | MPQ所长、LMU教授 | 未公开 | BMBF中继联合体、MCQST | 较弱 |
| CQN（Guha） | 架构/光子/理论 | 多为合作成果 | 亚利桑那测试床 | Clark杰出讲席 | 2600万+1860万美元 | NSF ERC | 多家初创与企业伙伴 |
| 加州理工Faraon | 稀土纳米光子 | Nature 2025 | 实验室双节点 | Valentine讲席 | 未公开 | IQIM | — |
| ICFO de Riedmatten | 稀土固态存储 | PRX 2025、PRL 2025、npj QI 2025 | 城域光–物质纠缠传输（2023）\[25\]\[84\] | ICREA教授 | 未公开 | QIA成员 | — |

---

## 五、十大最具引领潜力课题组：排名与评分

| 排名 | 课题组 | A 产出(25%) | B 团队(15%) | C 经费(15%) | D 纵向(10%) | E 横向(10%) | F 规模(15%) | G 势头(10%) | **综合分** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 中科大潘建伟团队 | 10 | 9 | 9 | 10 | 9 | 10 | 9 | **95.0** |
| 2 | QuTech Hanson–Wehner | 10 | 9 | 9 | 9 | 8 | 8 | 9 | **90.0** |
| 3 | 哈佛Lukin（+AWS） | 10 | 10 | 8 | 7 | 9 | 7 | 8 | **86.5** |
| 4 | 因斯布鲁克Northup/Lanyon | 8 | 8 | 8 | 8 | 7 | 7 | 9 | **78.5** |
| 5 | 牛津Lucas | 9 | 8 | 7 | 7 | 9 | 6 | 8 | **78.0** |
| 6 | 清华段路明 | 8 | 9 | 8 | 8 | 7 | 6 | 8 | **77.5** |
| 7 | 慕尼黑Rempe/Weinfurter | 8 | 9 | 7 | 7 | 5 | 7 | 7 | **73.5** |
| 8 | NSF CQN（Guha） | 7 | 8 | 7 | 8 | 7 | 5 | 7 | **69.5** |
| 9 | 加州理工Faraon | 8 | 8 | 6 | 6 | 6 | 5 | 8 | **68.5** |
| 10 | ICFO de Riedmatten | 7 | 8 | 6 | 7 | 5 | 6 | 7 | **66.5** |

### 入选理由与短板

1. **中科大潘建伟团队：** 唯一同时在卫星、骨干网、存储型中继三条线上处于世界前列的团队。2026年的“寿命超过建立时间”成果解决了中继可级联的前提条件，加上星座计划，使其最有可能率先实现洲际纠缠网络。**短板：** 国际合作受限；冷原子系综的集成度不高；部分纪录为实验室盘纤。
2. **QuTech：** 拥有协议栈、操作系统和联盟牵头权，最可能定义“量子互联网怎么编程”。SGA2的4750万欧元为其提供到2030年前后的稳定窗口。**短板：** NV平台的速率与扩展性有限，原型网络的硬件主体转向离子平台。
3. **哈佛Lukin：** 物理创新力与产业绑定（AWS）兼具，SiV+核自旋存储是目前固态平台中最接近中继节点的方案之一。**短板：** 制冷与工程复杂度高，现场规模仍为双节点。
4. **因斯布鲁克：** 承载QIA原型网络，未来3.5年将获得全球最集中的“离子城域网+中继”工程资源，上升斜率最大。**短板：** 执行风险高。
5. **牛津：** 分布式量子计算的首个实证，对“量子网络=量子计算机扩展方式”这一叙事贡献最大。**短板：** 距离维度弱；人才与知识产权流向产业。
6. **清华段路明：** 在“存储寿命超过城域纠缠建立时间”的离子节点指标上与欧美并跑，并在复用技术上领先。**短板：** 缺少现场光纤测试。
7. **慕尼黑：** 单原子网络的“原产地”，三节点单原子纠缠（2026）显示其仍在前沿。**短板：** 产业化弱。
8. **CQN：** 美国唯一以“量子互联网”为使命的国家级工程中心，续期保障到2030年。**短板：** 自有旗舰实验较少。
9. **加州理工Faraon：** 复用是突破速率瓶颈的关键，稀土多发射体节点路线独特。**短板：** 未出实验室。
10. **ICFO：** 多模固态存储在欧洲独树一帜，是QIA中继的潜在核心器件提供方。**短板：** 节点处理能力弱。

### 值得关注的潜力股

- **普林斯顿Thompson组：** 硅基铒离子路线可与硅光子工艺兼容。
- **ETH Wallraff组：** 超导QPU机房级互联的标杆，综合分约65.5。
- **英国IQN枢纽/Heriot-Watt：** 拥有超过4200万英镑与40余家产业伙伴。
- **庆应Van Meter与大阪山本俊：** 日本网络架构与登月第二阶段的网络型量子计算机项目。
- **东芝欧洲剑桥实验室：** 产业参照，相干量子通信工程化水平全球领先。

---

## 六、结论与展望

1. **技术路线判断（5–10年）：**
   - QKD已进入“与经典光网融合+卫星组网”的商用阶段，中国与东芝/日本主导这一赛道。
   - 纠缠型量子互联网的关键门槛（存储寿命超过建立时间、多节点可编程、跨城域中继）在2024–2026年被逐一攻破，但尚未在同一系统中同时实现。
   - 我们判断，**首个“两城域网+中继”的可编程纠缠网络最可能在2029–2030年间出现**，候选为QIA因斯布鲁克原型和中科大体系。这是基于当前计划的推断，并非既成事实。
2. **平台判断：** 离子平台在“网络+计算”的结合上最有优势（因斯布鲁克、牛津、清华三家入选前十）；色心与稀土平台在集成与复用上有长期潜力；冷原子系综在中继段指标上目前领先。
3. **政策与资金趋势：**
   - 欧盟从联盟研究转向“试点设施与开放基础设施”（QIA SGA2）；
   - 英国以枢纽模式加大产业配资；
   - 美国以NSF ERC续期和DOE国家实验室测试床支撑研究，同时更依赖AWS等企业；
   - 中国以国家实验室和运营商（中国电信）双轮驱动；
   - 日本登月计划第二阶段把网络并入“网络型容错量子计算机”的叙事。
4. **建议：** 寻求合作或访学时：
   - 关注“全栈+协议”，首选QuTech/QIA；
   - 关注“规模化与工程”，首选中科大；
   - 关注“网络即计算扩展”，可选牛津、因斯布鲁克、清华；
   - 关注“下一代器件”，可选加州理工、普林斯顿、ICFO。

---

## 注意事项

- 维度C与E中大量数据**未公开**，评分依赖代理指标。第4–10名分差较小，应视为同一梯队。
- 以下内容为计划或预测，尚未发生：中国2025年低轨量子卫星、2027年高轨卫星；QIA“可能成为全球首个”全栈原型；Faraon“每节点数百量子比特”。
- 以下信息未获一手核实：墨子号2026年1月再入大气层；CN-QCN节点数145。
- 受检索预算所限，芝加哥/阿贡、橡树岭、Stony Brook、新加坡、韩国、印度、澳大利亚等团队的2025–2026年最新进展未逐一核实，可能被低估。
- 不同来源的数据存在口径差异：骨干网长度有“一期超过1万公里”与“约1.2万公里（2025）”两种说法；IQN枢纽经费有“超过4200万英镑”与“3170万英镑伙伴支持”两种说法。本报告已分别注明。

## 資料來源

1. [QIA Enters Phase to Build Full-Stack Quantum Networks - Quantum Internet Alliance](https://quantuminternetalliance.org/2026/10/01/qia-enters-phase-to-build-full-stack-quantum-networks/)
2. [QIA enters new phase to build full-stack quantum networks](https://qt.eu/news/2026/2026-10-08_QIA-enters-new-phase-to-build-full-stack-quantum-networks)
3. [Quantum Internet Alliance To Build Full-stack Quantum Networks](https://quantumzeitgeist.com/qia-quantum-internet-alliance-full-stack/)
4. [QIA Enters Phase to Build Full-Stack Quantum Networks - Fraunhofer ILT](https://www.ilt.fraunhofer.de/en/press/press-releases/2026/10-12-qia-fraunhofer-ilt.html)
5. [New UK Quantum Hub launches to pioneer secure networks and advance the quantum internet](https://www.hw.ac.uk/news/2025/new-uk-quantum-hub-launches-to-pioneer-secure-networks-and-advance-the-quantum-internet)
6. [Entanglement of nanophotonic quantum memory nodes in a telecom network](https://www.nature.com/articles/s41586-024-07252-z)
7. [Scientists Step Toward Quantum Internet With Experiment Under the Streets of Boston](https://singularityhub.com/2024/05/16/scientists-step-towards-quantum-internet-with-experiment-under-the-streets-of-boston/)
8. [Multiplexed entanglement of multi-emitter quantum network nodes](https://www.nature.com/articles/s41586-024-08537-z)
9. [Multiplexing Entanglement in a Quantum Network](https://iqim.caltech.edu/2025/02/26/multiplexing-entanglement-in-a-quantum-network/)
10. [Multiplexed ion-ion entanglement over \$1.2\$ kilometer fibers](https://arxiv.org/pdf/2510.20392)
11. [Spin-Photon Entanglement of a Single Er3+ Ion in the Telecom Band - Princeton University](https://collaborate.princeton.edu/en/publications/spin-photon-entanglement-of-a-single-er3-ion-in-the-telecom-band/)
12. [Physics - Erbium Ions Apply for Quantum Repeater Job](https://physics.aps.org/articles/v18/s41)
13. [World's first quantum microsatellite demonstrates secure communication with multiple ground stations](https://phys.org/news/2025-03-world-quantum-microsatellite-communication-multiple.html)
14. [USTC Demonstrates Successful Satellite-Enabled Quantum Key Distribution ----Chinese Academy of Sciences](https://english.cas.cn/head/202503/t20250319_908294.shtml)
15. [USTC Demonstrates First Scalable Quantum Repeater Building Block](https://postquantum.com/quantum-research/ustc-scalable-quantum-repeater/)
16. [www.arxiv.org](https://www.arxiv.org/pdf/2602.08472)
17. [arxiv.org](https://arxiv.org/abs/2602.08472)
18. [USTC 420 km Quantum Memory Entanglement Record](https://postquantum.com/quantum-research/420-km-quantum-memory-entanglement/)
19. [Quantum Cryptography and Physical Layer Cryptography](https://www.nict.go.jp/en/quantum/about/crypt/english.html)
20. [ムーンショット型研究開発事業 令和3 年度プログラム自己評価（年次評価）について（目標6） (1) 目的](https://www.jst.go.jp/moonshot/program/pdf/ms6_r3_jiko_pg.pdf)
21. [目標６ 「2050年までに、経済・産業・安全保障を飛躍的に 発展させる誤り耐性型汎用量子コンピュータを実現」 戦略推進会議 令和５年11月9日](https://www8.cao.go.jp/cstp/moonshot/senryakusuishin/11th/paper2_2.pdf)
22. [ムーンショット目標６ 2050年までに、経済・産業・安全保障を飛躍的に発展させる誤り耐性型汎用量子コンピュータを実現- 科学技術・イノベーション - 内閣府](https://www8.cao.go.jp/cstp/moonshot/sub6.html)
23. [Metropolitan-scale heralded entanglement of solid-state qubits](https://www.science.org/doi/10.1126/sciadv.adp6442)
24. [A rudimentary quantum network link between Dutch cities](https://www.tudelft.nl/en/2024/tu-delft/a-rudimentary-quantum-network-link-between-dutch-cities)
25. [Metropolitan entanglement distribution between an atom and a near-visible photon](https://arxiv.org/pdf/2607.08513)
26. [Telecom-Wavelength Quantum Repeater Node Based on a Trapped-Ion Processor](https://link.aps.org/doi/10.1103/PhysRevLett.130.213601)
27. [A metropolitan-scale trapped-ion quantum network node with hybrid multiplexing enhancements](https://arxiv.org/pdf/2503.13898)
28. [Gerhard Rempe's research works](https://www.researchgate.net/scientific-contributions/Gerhard-Rempe-7726014)
29. [Harald Weinfurter's research works](https://www.researchgate.net/scientific-contributions/Harald-Weinfurter-39718309)
30. [Metropolitan Entanglement Distribution between an Atom and a Near-Visible Photon](https://journals.aps.org/prl/abstract/10.1103/94hz-xtht)
31. [Hugues de Riedmatten - Quantum Photonics with Solids and Atoms](https://www.icfo.eu/research-group/19/qpsa/publications/)
32. [Jeff THOMPSON](https://www.researchgate.net/scientific-contributions/Jeff-D-Thompson-2160306994)
33. [Quantum Network Goes the Distance Using Existing Telecom Infrastructure](https://thequantuminsider.com/2025/04/24/quantum-network-goes-the-distance-using-existing-telecom-infrastructure/)
34. [Entangled quantum circuits](https://ethz.ch/en/news-and-events/eth-news/news/2023/05/entangled-quantum-circuits.html)
35. [A Modular Cryogenic Link for Microwave Quantum CommunicationOver Distances of Tens of Meters](https://arxiv.org/html/2604.15971)
36. [Deterministic Quantum Communication Between Fixed-Frequency Superconducting Qubits via Broadband Resonators](https://arxiv.org/pdf/2512.08328)
37. [Reference-Beam Attacks against Twin-Field Quantum Key Distribution using Optical Injection Locking](https://arxiv.org/pdf/2508.21763)
38. [Creation of memory–memory entanglement in a metropolitan quantum network](https://ouci.dntb.gov.ua/en/works/4w0OLBZl/)
39. [Entangling quantum memories over 420 km in fiber](https://arxiv.org/pdf/2504.05660)
40. [中国科学院量子信息与量子科技创新研究院合肥国家实验室2024年招聘海外优秀青年人才启事-高校人才网|高才网](https://www.gaoxiaojob.com/announcement/detail/278924.html)
41. [财政向“新”而行 发展以“质”致远——安徽财政大力支持科技创新发展综述\_芜湖市财政局](https://czgz.wuhu.gov.cn/xwzx/btdtai/8725685.html)
42. [China's Quantum Networking and QKD — World's Most Ambitious Quantum Communication Program](https://postquantum.com/china-quantum-ambition/china-quantum-networking-qkd/)
43. [潘建伟：明年计划发射2-3颗低轨卫星，10年内建成量子星座](https://www.guancha.cn/industry-science/2024_10_04_750682.shtml)
44. [量子科学实验卫星 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E9%87%8F%E5%AD%90%E7%A7%91%E5%AD%A6%E5%AE%9E%E9%AA%8C%E5%8D%AB%E6%98%9F)
45. [QuTech researchers present operating system for quantum networks - Delta](https://delta.tudelft.nl/en/article/qutech-researchers-present-operating-system-for-quantum-networks)
46. [A resource- and computationally-efficient protocol for multipartite entanglement distribution in Bell-pair networks](https://arxiv.org/pdf/2412.04252)
47. [First operating system for quantum networks](https://www.sciencedaily.com/releases/2025/03/250312123858.htm)
48. [Quantum Internet Between Two Dutch Cities 25km Apart.](https://quantumzeitgeist.com/quantum-internet-between-two-dutch-cities-25km-apart/)
49. [Nature](https://www.nature.com/articles/s41586-025-08704-w.pdf)
50. [A simple quantum internet with significant possibilities](https://www.sciencedaily.com/releases/2024/05/240515122712.htm)
51. [par.nsf.gov](https://par.nsf.gov/servlets/purl/10512790)
52. [par.nsf.gov](https://par.nsf.gov/search/author:%22Sutula,%20M%22)
53. [Long-lived telecom-heralded single-photon storage in an absorptive spin-rephased quantum memory](https://arxiv.org/pdf/2609.02579)
54. [Heralded entanglement of on-demand spin-wave solid-state quantum memories for multiplexed quantum network links](https://arxiv.org/pdf/2501.04131)
55. [A high-performance quantum memory for quantum interconnects](https://arxiv.org/pdf/2603.01156)
56. [Nuclear Spin Memories for Silicon-Vacancy Quantum Network Nodes - INSPIRE](https://inspirehep.net/literature/3185563)
57. [Engineers achieve multiplexing entanglement in quantum network](https://phys.org/news/2025-02-multiplexing-entanglement-quantum-network.html)
58. [Quantum Repeater Goes the Distance - Physics (APS)](https://physics.aps.org/articles/v16/84)
59. [A Cavity-Interfaced Register of Trapped-Ion Qubits with Multi-Second Coherence](https://arxiv.org/pdf/2608.22030)
60. [Generation of multipartite photonic entanglement using a trapped-ion quantum processing node](https://arxiv.org/pdf/2510.15693)
61. [Quantum internet prototype takes shape in Innsbruck](https://www.aqt.eu/quantum-internet-prototype-takes-shape-in-innsbruck)
62. [Paving the way to quantum supercomputers](https://www.sciencedaily.com/releases/2025/02/250205130938.htm)
63. [Quantum algorithm distributed across multiple processors for the first time—paving the way to quantum supercomputers](https://phys.org/news/2025-02-quantum-algorithm-multiple-processors-paving.html)
64. [Oxford University Team Makes Connections to Build a Quantum Supercomputer](https://thequantuminsider.com/2025/02/10/oxford-university-team-makes-connections-to-build-a-quantum-supercomputer/)
65. [Quantum repeater segment with free-space coupled co-trapped ions using telecom photon interference](https://arxiv.org/pdf/2606.12313)
66. [Quantum Networking](https://www.physics.ox.ac.uk/research/group/ion-trap-quantum-computing/research-areas/quantum-networking)
67. [Five hubs launched to ensure the UK benefits from quantum future](https://www.ukri.org/news/five-hubs-launched-to-ensure-the-uk-benefits-from-quantum-future/)
68. [A Multilevel Framework for Partitioning Quantum Circuits](https://arxiv.org/pdf/2503.19082)
69. [Luming Duan on alphaXiv](https://www.alphaxiv.org/@luming-duan)
70. [Experimental demonstration of memory-enhanced scaling for entanglement connection of quantum repeater segments — Quantum Computing](https://awesomepapers.io/quantum-computing/papers/2101.08541)
71. [Luming Duan](https://www.sciencedirect.com/author/7201932853/luming-duan)
72. [Chinese scientists realize crosstalk-avoided quantum network node - Chinadaily.com.cn](https://www.chinadaily.com.cn/a/202401/24/WS65b0cc10a3105f21a507e1aa.html)
73. [Realization of a functioning dual-type trapped-ion quantum network node](https://www.science.org/doi/10.1126/sciadv.aeb4076)
74. [Multiplexed ion-ion entanglement over \$1.2\$ kilometer fibers](https://www.alphaxiv.org/abs/2510.20392)
75. [Realization of a functioning dual-type trapped-ion quantum network node](https://arxiv.org/html/2506.23562)
76. [Members](https://www.mcqst.de/about/members/harald-weinfurter.html)
77. [Publications](https://www.munich-quantum-center.de/publications/)
78. [Center for Quantum Networks](https://cqn-erc.org/about/about-cqn/)
79. [Center for Quantum Networks: UArizona Leads Quantum Internet Advancements](https://news.arizona.edu/resources-media/university-experts/center-quantum-networks)
80. [PhoQuS to lead \$18.6 Million Center for Quantum Networks Renewal](https://phoqus.us/2026/08/18/CQN.html)
81. [Center for Quantum Networks (CQN) University of Arizona (lead institution)](https://erc-assoc.org/media/74)
82. [Coherent control of interacting solid-state spins below the diffraction limit](https://arxiv.org/pdf/2508.09122)
83. [Multiplexed Entanglement of Multi-emitter Quantum Network Nodes](https://www.alphaxiv.org/abs/2402.16224)
84. [Transmission of light-matter entanglement over a metropolitan network](https://arxiv.org/pdf/2304.05416)
85. [A solid-state temporally multiplexed quantum memory array at the single-photon level](https://www.nature.com/articles/s41534-025-01042-9)
86. [Toshiba brings quantum comms to the telecom network, Security](https://www.telecomtv.com/content/security/toshiba-brings-quantum-comms-to-the-telecom-network-52906/)
87. [Toshiba breakthrough brings quantum communications to existing national-scale telecommunications infrastructure - Toshiba Quantum Technology](https://www.toshiba.eu/quantum/news/toshiba-breakthrough-on-national-quantum-networking/)
88. [Toshiba team extends quantum link range past 600km](https://optics.org/news/12/6/11)
89. [Toshiba executes long-distance quantum key distribution using commercial fibre](https://www.techmonitor.ai/hardware/quantum/toshiba-quantum-key-distribution-commercial-fibre)
90. [Toshiba Europe, GÉANT, PSNC and Anglia Ruskin University announce the first demonstration of Quantum Key Distribution within commercial telecommunication networks - GÉANT Network](https://network.geant.org/toshiba-europe-geant-psnc-and-anglia-ruskin-university-announce-the-first-demonstration-of-quantum-key-distribution-within-commercial-telecommunication-networks/)
91. [Quantum Corridor, Toshiba Demonstrate Cross-state Quantum Key Distribution Over Live Commercial Metro Fiber Network](https://thequantuminsider.com/2025/12/09/quantum-corridor-toshiba-demonstrate-cross-state-quantum-key-distribution-over-live-commercial-metro-fiber-network/)
92. [A Modular Cryogenic Link for Microwave Quantum Communication Over Distances of Tens of Meters](https://arxiv.org/html/2604.15971v1)
93. [Spin-Photon Entanglement of a Single Er 3 + Ion in the Telecom Band (Journal Article)](https://www.osti.gov/pages/biblio/2539957-spin-photon-entanglement-single-er-ion-telecom-band)
94. [UK Launches \$54M Integrated Quantum Networks Hub to Develop Advanced Quantum Network Infrastructure](https://thequantuminsider.com/2025/04/10/uk-launches-54m-integrated-quantum-networks-hub-to-develop-advanced-quantum-network-infrastructure/)
95. [Integrated Quantum Networking (IQN) Hub: pioneering a ‘near-unhackable’ internet](https://www.hw.ac.uk/research-enterprise/innovation/innovation-case-studies/integrated-quantum-networking)
96. [Quantum communication and networking](https://www.hw.ac.uk/research-enterprise/research/quantum-sciences/quantum-communication-and-networking)
97. [Tokyo QKD Network and beyond](https://www.itu.int/en/ITU-T/Workshops-and-Seminars/2023/0724/Documents/Kenyoshi.pdf)
98. [World’s First Integrated System for Quantum Key Distribution and High-Speed Data Transmission in a Large-Capacity Optical Transmission System Demonstration Environment for IOWN Open APN](https://www.nict.go.jp/en/press/2025/09/16-1.html)
99. [NAGAYAMA Shota Project｜Moonshot R&D - Goal 6](https://www.jst.go.jp/moonshot/en/program/goal6/6C_nagayama.html)
100. [Quantum Internet Testbed Efforts in Japan (overview) Shota Nagayama](https://www.ietf.org/proceedings/116/slides/slides-116-qirg-quantum-internet-testbed-efforts-in-japan-overview-00.pdf)
101. [Quantum interface development for quantum computer network construction --Moonshot](https://moonshot.ynu.ac.jp/en/study/moonshot.html)
102. [目標6 山本 俊PM プロジェクト紹介｜ムーンショット型研究開発事業](https://www.jst.go.jp/moonshot/program/goal6/66_yamamoto.html)
103. [内閣府の取り組み 令和５年９月21日 内閣府 科学技術・イノベーション推進事務局 資料3-1](https://www8.cao.go.jp/cstp/ryoshigijutsu/16kai/siryo3-1.pdf)
104. [South Africa and China establish record-breaking 12,900 km ultra-secure quantum satellite link](https://www.su.ac.za/en/node/19887)