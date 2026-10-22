# 人工智能与教育的双向关系：应用现状、落地场景、挑战与AI顶尖人才培养体系研究报告（截至2026年10月）

**核心结论：AI在教育中已从"试点"进入"规模化普及"阶段，但只有"教师减负"和"有设计护栏的AI辅导"两类场景拿得出较扎实的实证效果；与此同时，中国已成为全球顶尖AI人才的最大"产地"和第一大"工作地"，下一步强化的关键不在于继续扩张专业数量，而在于数学物理基础、算力可及性、本科科研与产业前沿课程这几块"质量短板"。**

## TL;DR

- **应用现状**：学生端使用几乎普及（英国本科生95%使用AI、94%用于考核作业；斯坦福HAI《AI Index 2026》教育章指出，"五分之四的美国高中生和大学生用AI做功课"），教师端约六成美国教师用过AI、每周使用者自报每周节省5.9小时；但制度跟不上——同一报告称美国仅一半初高中有AI政策、只有6%的教师认为政策清晰。中国以2026年4月五部门《"人工智能+教育"行动计划》为纲，2025—2026学年起在中小学推行AI教育。
- **落地与效果**：证据呈"设计决定成败"的格局——哈佛物理课定制AI导师（随机交叉试验，194人）学习增益超过主动学习课堂的两倍，世界银行尼日利亚6周试点提升0.31个标准差；但无护栏的GPT-4在土耳其高中数学实验中撤除后使成绩下降17%，田纳西州18所初中两年期Khanmigo随机试验的效果仅0.06—0.08个标准差，与"不带AI的Khan Academy练习"相当。规模化落地的瓶颈是学生的有效参与，而不是技术本身。
- **人才培养**：卡内基国际和平基金会2026年9月数据显示，NeurIPS 2025顶尖作者中57%本科在中国就读（美国仅13%），在中国工作者占41%、首次超过美国（34%），北京大学居机构第一。中国已形成"621所高校设AI本科专业＋近百所AI学院＋'101计划'核心课程＋姚班/通班等拔尖班"的体系；强化方向应是"少而精"的拔尖通道、国家级教育算力平台、本科科研与产学联合培养、以及K-12数学与计算思维的扎实化。

## 一、AI在教育领域的应用现状

### 1.1 主要应用方向与成熟度

| 方向 | 典型形态 | 成熟度判断 |
|---|---|---|
| 教师备课与行政辅助 | 生成教案、习题、分层材料、评分量规、家校沟通 | 已规模化，自报省时明确 |
| 智能辅导（AI tutor） | Khanmigo、Claude学习模式、学习机"AI 1对1" | 快速普及，效果高度依赖设计 |
| 个性化/自适应学习 | 学习路径推荐、知识图谱诊断、学习机 | 前代自适应系统证据较多，生成式版本证据仍少 |
| 自动批改与评估 | 作文/口语评分、编程自动评测、智能阅卷 | 客观题与语言测评成熟；高利害评分受监管 |
| 语言学习 | Duolingo类对话练习、口语测评 | 规模化，商业模式成熟 |
| 学习分析与教育治理 | 学情分析、课堂行为分析、就业匹配、招生 | 中国大力推进；欧盟将招生/评分列为高风险 |
| 特殊教育/无障碍 | 语音转写、朗读、智能辅具 | 潜力大，系统性研究不足 |
| 虚拟仿真实验 | 强交互仿真、未来实训中心 | 职业教育与工科较成熟 |

### 1.2 使用率与采用数据（事实）

- **英国高校学生**：HEPI与Kortext《Student Generative AI Survey 2026》（Savanta于2025年12月调查1,054名全日制本科生）显示，\[1\]95%的学生至少以一种方式使用AI，94%用生成式AI辅助考核作业（2024年为53%左右、2025年为89%—92%）；\[2\]\[3\]直接把AI生成文本放进作业的比例从2024年的3%、2025年的8%升至12%。\[4\]但只有36%的学生认为学校鼓励使用AI，38%表示学校提供了AI工具；49%认为AI改善了学习体验；\[5\]42%表示害怕被指控作弊而减少使用。\[3\]
- **美国K-12教师**：盖洛普与沃尔顿家族基金会2025年6月发布的调查（2,232名公立学校教师）显示，2024—25学年60%的教师用过AI，32%至少每周使用；每周使用者自报平均每周节省5.9小时，约合一学年六周。但仅19%的教师所在学校有AI政策，68%未接受过AI培训。\[6\]\[7\]需注意，5.9小时为教师自报估计，且只适用于每周使用者这一自选择群体。\[7\]\[8\]
- **美国学生整体**：斯坦福HAI《AI Index 2026》教育章指出，约五分之四的美国高中生和大学生用AI完成学业任务，但只有约一半的初高中有AI政策，仅6%的教师认为政策清晰；2024—2025年美国四年制大学计算机专业本科入学下降11%，而AI相关软件类硕士毕业生在2023—2024年增长17%。\[9\]
- **全球课程层面**：同一报告估计93%的国家在中小学开设计算机科学，但只有30%将其列为必修；中国和阿联酋从2025—26学年起强制推行AI教育。\[10\]

### 1.3 代表性产品与平台

**国际：**
- **OpenAI ChatGPT Edu**：2024年5月30日推出。2025年2月4日，加州州立大学（CSU）系统宣布向23个校区的46万余名学生和6.3万余名教职工部署，OpenAI称之为"全球单一机构最大规模的ChatGPT部署"。据EdSource\[11\]\[12\] 2026年5月21日报道，CSU发言人确认学校将续约三年、每年支付1,300万美元，覆盖47万余名学生和6.3万名教职工（此前18个月合同为1,700万美元），且合同"可提前通知按年取消"；但教师群体曾在2026年1月请愿要求取消合同——可见成本与学术理念上的争议并未消失。
- **Anthropic Claude for Education**：2025年4月2日发布，核心是"学习模式"（Learning mode），以苏格拉底式提问引导推理而非直接给答案；首批合作方包括东北大学、伦敦政治经济学院和尚普兰学院，并与Canvas（Instructure）、Internet2集成；2025年8月学习模式扩展到所有Claude用户。\[13\]\[14\]\[15\]\[16\]
- **Google Gemini for Education**：2025年6月ISTE大会宣布，作为核心服务免费纳入所有Google Workspace for Education版本，并向全年龄段学生开放Gemini应用；Google自称2025年已在美国1,000余所高校覆盖逾1,000万名学生（企业自报数据）。\[17\]\[18\]\[19\]
- **Microsoft Copilot**：2025年起向13岁以上学生开放Copilot Chat；2026年5月推出面向学生的"Study\[20\] and Learn"学习教练智能体，并入Microsoft 365 Education无额外收费。\[21\]\[22\]
- **Khan Academy Khanmigo**：据可汗学院首席学习官Kristen DiCerbo介绍，合作学区的Khanmigo学生和教师用户从2023—24学年约6.8万人增至2024—25学年逾70万人，合作学区从45个扩展到380多个；2025—26学年可汗学院又在5个美国学区约5,100名学生中试点"重构版"Khan Academy。
- **Coursera/edX、Duolingo**等平台已普遍嵌入AI对话练习、AI助教和自动反馈功能。

**中国：**
- **国家智慧教育公共服务平台**：2025年上线"2.0智能版"；教育系统上线计算机、化学、材料学等13个学科的垂直大模型。\[23\]\[24\]
- **AI学习机赛道**：IDC数据显示，2025年第二季度中国学习平板出货量154万台、同比增长44.6%，科大讯飞当季销售额居行业第一；行业汇总数据称2025年中国学习平板全渠道销量632.1万台、销售额199.1亿元，作业帮以约28.8%（洛图科技）的全渠道销量份额居首，学而思、科大讯飞分别在高端价位段领先。艾媒咨询估计2024年中国智能学习机市场规模270.72亿元。上述均为行业咨询机构数据，口径不一，宜视为量级参考。\[25\]\[26\]\[27\]
- **其他**：网易有道、百度、字节跳动（豆包等）、腾讯等以大模型能力切入答疑、作文批改、口语陪练；"双减"后转型的教培公司（作业帮、学而思、猿辅导）与科技公司（科大讯飞、百度）形成"内容派"与"技术派"的竞争格局。\[28\]

### 1.4 主要国家/地区政策

**中国（政策密度全球最高）：**
- 2025年4月，教育部等九部门《关于加快推进教育数字化的意见》提出加快建设人工智能教育大模型、推动大模型与教育教学深度融合。\[29\]
- 2025年发布《中小学人工智能通识教育指南（2025年版）》《中小学生成式人工智能使用指南（2025年版）》《职业院校人工智能应用指引》《教师生成式人工智能应用指引（第一版）》；《关于加强中小学人工智能教育的通知》明确2030年前在中小学基本普及人工智能教育；发布758项职业教育专业教学标准，将数字化和人工智能纳入教学内容。\[24\]\[30\]
- 2025年教育部在17个省市和18所高校启动人工智能赋能教育试点，北京、上海、广东等11个地方出台专门文件；2025年8月26日国务院印发《关于深入实施"人工智能+"行动的意见》。\[31\]\[32\]\[33\]\[34\]
- **2026年4月2日**，教育部、国家发展改革委、工业和信息化部、科技部、国家数据局五部门印发《"人工智能+教育"行动计划》（教科信〔2026〕1号），目标是到2030年构建"纵向贯通、横向联通的人工智能全学段教育和全社会通识教育体系"。主要内容包括：推动AI成为高校公共基础课；将AI纳入教师资格考试和认证；建设国家教育智能算力服务平台；分教育阶段研发AI教育大模型；推动智能命题、组卷、监考、评卷；以及实施AI领域高技能人才集群培养计划。\[35\]

**美国：**
- 2025年4月23日第14277号行政令《推进面向美国青少年的人工智能教育》设立白宫AI教育工作组（由科技政策办公室主任担任主席），设立"总统AI挑战赛"，推动教师AI培训、高中AI双学分课程和AI相关注册学徒制，并调用NSF等资助的国家AI研究院资源支持K-12。挑战赛于2025年8月启动，据报道2027届已更名为"总统超级智能挑战赛"。\[36\]\[37\]\[38\]\[39\]
- 美国体制以州为主：AI Index 2026统计，17个州明确计算机科学是AI的基础，仅5个州为AI教育划拨专门的教师培训经费，州级指南大多不具约束力。\[40\]

**欧盟：**
- 《AI法案》第5条第1款(f)项自2025年2月2日起禁止在教育机构使用情绪识别系统，第4条"AI素养"义务同日生效。\[41\]\[42\]
- 附件三第3点把四类教育用途列为高风险：(a)招生/录取/分配，(b)学习成果评估，(c)评定受教育层级，(d)考试中监测违规行为（监考）。高风险义务原定2026年8月2日适用；欧洲议会2026年6月通过的"数字综合法案"（Digital\[43\] Omnibus）拟推迟至2027年12月2日，尚需理事会最终通过。\[42\]

**联合国教科文组织**：2023年发布《教育与研究中的生成式人工智能指南》，建议在课堂中使用生成式AI的最低年龄为13岁，并强调以人为本、数据保护与教师能动性。

**韩国（反面教材）**：2025年3月在小学3—4年级及初高中英语、数学、信息课推出AI数字教科书（共审批76种）；但因准备不足、教师负担和隐私问题，学校采用率仅约三成。2025年8月4日国会修法，把AI教科书从"教科书"降为"教育资料"，失去免费供给的法律依据；审计机构随后指出试点、实地测试和成本论证不足。\[44\]\[45\]\[46\]\[47\]

**日本、英国、新加坡**：以发布指南和"有条件使用"为主——日本文部科学省发布了初中等教育生成式AI使用指南（2024年修订为2.0版），英国教育部发布了生成式AI产品安全期望——整体比中国更审慎、比美国更集中。

## 二、实际能落地的场景：证据分级

### 2.1 证据最强：已规模化且有实证的场景

**（1）教师减负与备课辅助。** 这是采用率最高、阻力最小的场景。盖洛普数据显示，教师最常用AI备课（37%每月至少使用一次）、制作练习（33%）、改编材料（28%），64%认为改编后的材料质量更好；中国五部门行动计划也把"人机共创备课"、智能批改与答疑列为重点。判断：**这是当前最确定能落地的场景**，但收益基于自报，需警惕"核查成本"抵消部分节省的时间。\[8\]\[35\]\[48\]\[49\]

**（2）设计良好的AI辅导——效果在受控条件下显著。**
- **哈佛物理课随机对照试验**（Kestin、Miller等，《Scientific Reports》2025年6月）：2023年秋，在哈佛最大的入门物理课Physical Sciences 2中，194名学生采用随机交叉设计，一个主题由定制AI导师"PS2 Pal"在家学习，另一个主题在主动学习课堂学习。结果AI组学习增益中位数超过课堂组的两倍，用时中位数约49分钟（课堂60分钟），投入度和动机评分也更高。局限：仅两个短主题、短期测验，且AI导师经过精心的教学法设计（分步引导、不直接给答案）。\[50\]\[51\]\[52\]\[53\]
- **世界银行尼日利亚试点**（世界银行政策研究工作论文第11125号，2025年5月）：埃多州高一学生课后使用基于GPT-4的Microsoft Copilot学习英语，6周12次课，在教师引导下进行。综合测评提高0.31个标准差，英语（主要指标）提高0.23个标准差，学校期末英语考试提高约0.21个标准差，相当于1.5—2年"常规学校教育"的收获，跻身最具成本效益的干预之列。局限：时间短、有教师监督、依赖机房与网络。\[54\]\[55\]\[56\]

**（3）语言学习与自动测评**（口语评分、作文反馈）：技术成熟、商业闭环清晰。中国学习机和讯飞的考试测评能力即属此类。

### 2.2 证据混合：规模化但效果有限或不确定

- **Khanmigo两年期大规模随机试验**（Oreopoulos与Low，Annenberg研究所EdWorkingPaper 26-1551，2026年8月）：田纳西州汉密尔顿县18所初中在补救性数学时段使用"只引导、不给答案"的Khanmigo，每学期提升1.3个全国百分位，约合每学年0.06—0.08个标准差；按全年积极参与推算的效果为0.14个标准差。**但这一增益与不带AI的Khan Academy练习相近**："AI导师本身"并未带来额外效果。原因在于参与度：96%的学生至少用过一次，但中位数学生只在三分之一的练习日发消息，在出错的练习时段中只有17%会求助，仅14.5%的消息包含数学问题或推理步骤。**这是迄今规模最大、周期最长的公立学校AI辅导实验，其结论应当成为政策制定的基准：瓶颈在于"让学生真正用"，而不在于"给学生开通"。**\[57\]
- **AI学习机**：销量高速增长，但目前缺乏独立的随机对照效果评估，多为厂商自报的提分案例。

### 2.3 仍在试点或存在明显炒作的场景

- 全自动"AI教师"替代课堂授课、基于情绪/注意力识别的课堂监控（欧盟已明令禁止）、高利害考试的全自动评分、"AI数字教科书"一刀切推广（韩国已失败）。\[58\]
- 中国行动计划提出的"智能学伴""学生数字档案""教育智能大脑"等，目前仍以试点和标杆项目为主，效果评估尚未公开。\[35\]

### 2.4 分学段典型案例

| 学段 | 国际 | 中国 |
|---|---|---|
| K-12 | Khanmigo学区部署；尼日利亚课后AI辅导；美国总统AI挑战赛 | 2025—26学年起中小学AI通识教育；学习机家庭使用；17省市AI赋能教育试点 |
| 高等教育 | CSU全系统ChatGPT Edu；东北大学/LSE用Claude for Education；哈佛PS2 Pal | 清华100门"AI赋能教学试点课程"；浙大"万门AI赋能课"；复旦首批100门AI大课和23个"X+AI"双学士学位项目 |
| 职业教育/企业培训 | 美国行政令推动AI注册学徒制；企业用Copilot做内训 | 758项职教专业教学标准纳入AI；《职业院校人工智能应用指引》；AI高技能人才集群培养计划 |

## 三、AI在教育领域面临的挑战

### 3.1 学习效果的"双刃剑"：认知卸载 vs. 学习增益（争议焦点，正反证据并列）

**负面证据：**
- **Bastani等（《美国国家科学院院刊》PNAS，2025年6月）**：在土耳其一所高中约千名学生的数学实地实验中，类ChatGPT界面的"GPT Base"提升了练习表现，**但撤除后学生成绩比从未使用者低17%**；学生把GPT-4当"拐杖"。带教学护栏的"GPT Tutor"基本消除了这一负面效应。\[59\]
- **MIT媒体实验室"Your Brain on ChatGPT"**（Kosmyna等，2025年，arXiv预印本）：54名学生用脑电（EEG）记录写作，ChatGPT组的大脑连接最弱、对自己文章的回忆最差、所有权感最低，作者称之为"认知债务"；先独立写作、后用AI的顺序表现更好。**但这是未经同行评审的小样本预印本，已遭到方法学质疑，不宜被引为"AI损害大脑"的定论。**\[60\]\[61\]

**正面证据**：哈佛PS2 Pal、世界银行尼日利亚试点（见上）。

**综合判断**：证据一致指向**"设计与使用方式决定效果"**——直接给答案的通用聊天机器人在练习场景中提高短期表现，却损害独立掌握；以提问引导、限制直接答案、结合教师监督的AI导师可以带来正向增益。但即使设计正确，学生不主动用（Khanmigo试验）也会使收益缩水。\[62\]

### 3.2 学术诚信与评价体系变革

HEPI数据显示，直接把AI文本放进作业的英国本科生比例三年内从3%升至12%；同时42%的学生因担心被误判作弊而减少使用AI——说明**AI检测器的不可靠正在制造双重伤害**。传统的课后论文、开放式作业已难以作为可信的考核方式，评价必须向过程性评价、口头答辩、课堂内写作和"允许AI但考核AI使用过程"的双轨模式转型。中国推动的"智能命题/监考/评卷"则面临与欧盟高风险规则相似的公平与可解释性问题。\[3\]

### 3.3 内容准确性与幻觉

通用大模型在学科细节、计算和引用上仍会出错，对低龄、低基础学生的风险最大（他们最难识别错误）。哈佛和Khanmigo等成功案例都依赖经过校验的内容和专门的教学提示，这也是中国行动计划强调"分教育阶段研发AI教育大模型、强化价值对齐与逻辑推理"的原因。\[35\]

### 3.4 数据隐私与儿童保护

- 韩国AI教科书项目被个人信息保护委员会认定存在数据保护违规，是其遭降级的原因之一。\[63\]
- 欧盟禁止教育场景的情绪识别；中国行动计划提出"建设学生数字档案""构建学生用户画像"，并已发布《智慧教育平台个人信息保护通用要求》行业标准。**用户画像与隐私保护之间的张力，是中国路线需要重点平衡的问题。**\[33\]\[35\]
- HEPI显示约15%的英国学生用AI寻求陪伴或缓解孤独，提示AI在青少年心理层面的影响需要专门治理。\[5\]

### 3.5 公平与数字鸿沟

- 尼日利亚试点证明AI可以惠及低资源地区，但前提是机房、电力和网络。\[56\]
- HEPI多年调查记录到AI使用存在性别和社会经济背景差异；美国约60%的高中开设计算机课，城乡之间也有差距（盖洛普：郊区教师AI使用率65%，城镇/农村为57%）。\[64\]\[65\]\[66\]
- 中国学习机价格从2,000元以下到1万元以上分层明显，作业帮等品牌下沉三四线城市；国家智慧教育平台和行动计划中"支持农村、边远地区学校利用国家平台开好AI课程"是对冲手段，但家庭端的硬件差距依然存在。\[26\]\[35\]\[67\]

### 3.6 教师培训与接受度

68%的美国教师未接受AI培训，仅6%认为学校政策清晰；HEPI显示只有36%的英国学生感到学校鼓励使用AI。中国行动计划要求制定教师智能素养标准、分层培训"全覆盖"，并将AI纳入教师资格考试——**方向正确，但"全覆盖培训"容易流于形式，关键在于学科化、情境化的示范课与教研。**\[5\]\[35\]

### 3.7 成本与商业模式

- 据EdSource援引CSU发言人确认，CSU首期18个月合同为1,700万美元，2026年续约为每年1,300万美元、为期三年；Khanmigo学区收费曾为每生每年约15—35美元（据媒体报道）；世界银行估计尼日利亚6周试点每生约48美元（二手转述，含义需谨慎）。\[54\]
- 韩国AI教科书的教训是：订阅制软件被纳入免费教科书体系后，财政与采购模式难以为继。\[68\]
- 中国"政府主导＋购买服务＋多元投入"的模式与家庭消费级学习机并行；学校端可持续付费的商业模式尚未成型。\[35\]

### 3.8 监管碎片化与对教师职业的影响

中国是自上而下的统一规划，美国以州为主且多为非约束性指南，欧盟以风险分级的硬法约束为主——三者路径差异显著。对教师职业而言，现有证据（盖洛普、Khanmigo试验）更支持"AI替代事务性工作、教师转向组织与督导"，而非"AI替代教师"；Khanmigo试验也说明，没有教师驱动，学生不会主动与AI进行深度对话。

## 四、教育如何支撑AI高尖端人才培养

### 4.1 全球AI顶尖人才格局（事实）

- **卡内基国际和平基金会《谁在全球AI人才竞赛中领先？》（AI Talent v3.0，Damien Ma、Binyi Yang，2026年9月23日）**：沿用MacroPolo方法，以NeurIPS 2025论文作者为样本（25,677名作者中10,280人有完整履历）。\[69\]
  - 本科在中国就读者占57%（比2022年上升11个百分点），美国仅13%。\[69\]
  - **在中国工作的比例为41%，首次超过美国的34%**（2022年为美国46%、中国27%）。\[69\]
  - 中国本科出身者留在中国工作的比例从57%升至69%；美国留存率为89%，欧洲60%，韩国77%。\[69\]
  - 美国净流入2,145人，中国净流出1,729人；在美的中国本科出身者与在华的美国本科出身者之比为30:1（2022年为46:1）。\[69\]
  - 机构排名：**北京大学居第一**（2022年第一为Google），KAIST升至第三，新加坡国立大学第13、南洋理工大学第16；苏黎世联邦理工和牛津跌出前列。\[69\]
  - 方法局限：样本只取有完整OpenReview自填履历者（非随机，略偏学术界）；国家归属按机构所在国；欧洲结论对样本敏感。\[69\]
- **MacroPolo《全球AI人才追踪2.0》（2023年数据）**：中国本科出身的顶尖AI研究者占比从2019年的29%升至2022年的47%；在美顶尖AI人才中，中美本科出身者合计占75%。\[70\]
- **DeepSeek案例（媒体报道，非正式统计）**：创始人梁文锋为浙江大学本硕；团队规模约140—160人，核心研发多为清华、北大等国内高校的应届毕业生和在读博士，海归比例很低。MLA架构、GRPO等关键成果有在读博士实习生参与。\[71\]\[72\]\[73\]\[74\]该案例说明**中国本土本硕博体系已能产出前沿模型的核心研发力量**，但团队成员的具体构成数据来自媒体整理，精度有限。

**解读**：中国在顶尖AI人才的"产量"上已领先，并正在扭转"为他人作嫁衣"的流失格局；美国的优势转向"吸引力与留存率"（89%）以及顶级实验室的集聚。双方都在为下一代人才"打地基"——中国强制推行K-12 AI教育，美国以行政令推进K-12 AI素养。

### 4.2 中国的培养政策与体系

**专业与学院扩张：**
- 自2018年《高等学校人工智能创新行动计划》设立人工智能本科专业（代码080717T）以来，截至2025年共有621所普通高校获批或备案该专业；据21世纪经济报道依据教育部名单统计，2024年度新增91个布点（第三方高绩统计为89个），连续多年居新增专业之首。
- 据第三方不完全统计，截至2025年8月底至少93所高校设立了人工智能学院，约25所高校设有AI领域博士学位授权点（后两项为第三方统计）。\[34\]

**"101计划"（课程质量工程）：**
- 教育部2024年启动人工智能领域"101计划"，由中国工程院院士、西安交通大学教授郑南宁牵头，清华、北大、西安交大等15所高校参与。\[75\]\[76\]
- 2025年7月18日发布12本核心课程教材（《人工智能概论》《数据科学基础》《机器学习方法与应用》《计算机视觉》《生成式人工智能》等），与15本参考教材、2本综合实验教材构成体系。\[75\]\[76\]
- 同时发布《高等学校人工智能专业人才培养战略研究报告暨核心课程体系》，含12门核心课程大纲和17所高校的培养方案。\[77\]

**"人工智能+X"与通识化：**
- 五部门行动计划要求AI成为高校公共基础课、打造"短实新"前沿课程、新设交叉学科专业，"整合高水平研究型大学、科技领军企业、国家实验室等力量"探索拔尖人才培养新模式；"智能科学与技术"已成为新增学科点较多的方向之一。\[34\]\[35\]
- 北师大2025年首设"人工智能教育"本科专业并推出"汉语言文学＋人工智能"双学士学位；同济大学在每个大类开设AI核心通识课、每个专业开设AI应用课。\[78\]\[79\]

**代表性高校培养体系：**

| 高校/项目 | 培养模式要点 |
|---|---|
| 清华大学"姚班"（计算机科学实验班） | 图灵奖得主姚期智2005年创办，2019年创办"智班"、2021年创办"量信班"；2022年三班合并，下设计算机科学、人工智能、量子信息三个方向，大一结束时自由选择；前两年强化数理与学科基础，后两年进入专业方向；全英文专业课，姚期智亲自制定方案并授课；截至2025年12月累计培养近1,200名学生、毕业近750人，其中6人获斯隆研究奖\[80\]\[81\]\[82\] |
| 北京大学/清华大学"通班"（通用人工智能实验班） | 2021年由朱松纯推动、两校联合创办；北大首届在元培学院招收26人，课程包括数学、物理、计算机核心课，7门AI核心课，4门AI与人文社科、艺术、哲学交叉课，3门AI系统实践课，并与研究生前沿课程贯通；北大同时设有智能学院和图灵班\[83\]\[84\] |
| 西安交通大学 | "101计划"牵头单位，依托人工智能学院与郑南宁团队，长期探索本硕博贯通的AI拔尖人才培养 |
| 浙江大学、上海交通大学、复旦大学 | 浙大推出AI教材、实训平台和"万门AI赋能课"；上海交大制定"AI+教育教学"行动规划；复旦设立23个"X+AI"双学士学位项目 |
| 南京大学、中国科学技术大学、哈尔滨工业大学、西安电子科技大学等 | 南大2018年较早设立实体AI学院；中国科大与科大讯飞共建实验室，体现产学研联合；西电2017年成立教育部直属高校首个实体AI学院 |

### 4.3 美国与其他国家的做法

- **卡内基梅隆大学（CMU）**：2018年5月宣布开设全美首个人工智能本科学位（B.S. in AI），同年秋季开课。课程包括数学统计、计算机、AI核心（约7门、66学分）、伦理，以及至少63学分的人文社科/艺术课；由计算机系、机器人研究所、机器学习系、语言技术研究所等六个单位联合授课，规划每年招收约30—35人——**"小规模、跨院系、强伦理"**。\[85\]\[86\]\[87\]\[88\]
- **MIT施瓦茨曼计算学院**：2018年10月宣布10亿美元投入（后称11亿美元），2019年开学，新增50个教职、使MIT的计算与AI学术力量"近乎翻倍"；核心理念是培养"计算双语者"（computing\[89\]\[90\]\[91\] bilinguals），通过"Common Ground"跨五个学院开设融合课程，并以SERC项目把伦理内容嵌入现有课程。时任校长Reif称之为"MIT自1950年代以来最深刻的重构"。\[90\]\[92\]
- **斯坦福HAI**（2019年成立）：在符号系统项目中设"以人为本AI"方向，开设Brynjolfsson、Norvig等人的跨学科课程，与教育学院联合资助30余项"AI+教育"研究，并面向高中生开展AI4ALL项目。\[93\]\[94\]\[95\]
- **国家层面**：NSF与农业部资助的国家AI研究院网络既做科研也承担人才培养，并被第14277号行政令指定支持K-12 AI教育；但AI\[36\] Index 2026指出美国本科计算机招生已出现下滑。\[96\]
- **韩国、新加坡**：KAIST在卡内基榜单中升至第三，韩国顶尖人才留存率77%；新加坡国立大学和南洋理工大学双双进入前20。两国以"少数旗舰校＋国家战略投入"实现了快速追赶。\[69\]
- **欧洲、印度**：卡内基报告认为欧洲在顶尖人才上"持续掉队"，印度占比下降2个百分点，且无机构进入前列。\[69\]

### 4.4 中美培养体系对比

| 维度 | 中国 | 美国 |
|---|---|---|
| 规模 | 621所高校设AI本科专业，体量全球最大 | AI本科专业较少，多以CS下设方向/辅修为主 |
| 顶层设计 | 国家级计划（101计划、行动计划）统一课程与教材 | 高校自主，联邦以资助和行政令引导 |
| 拔尖通道 | 姚班、通班、图灵班等"学堂班"，竞赛选拔＋小班＋名师 | 顶尖校的研究型本科、导师制和大规模本科科研（UROP类） |
| 产业衔接 | 校企联合实验室、企业导师；头部企业大量吸纳应届博士 | 顶级实验室与高校人员双聘、博士实习常态化 |
| 优势 | 生源规模、数理基础、政策执行力，近年留存率显著上升 | 国际人才吸引力、留存率89%、算力与资本 |
| 短板 | 部分院校"有专业无师资"，算力不均，课程同质化 | 本科CS招生下滑，K-12 AI内容缺乏、州际差异大，签证政策带来不确定性 |

### 4.5 当前培养体系的短板（判断）

1. **规模扩张快于质量**：621个布点中相当一部分缺乏具备一线研究经验的师资，"101计划"恰恰是为了弥补课程和教材的质量差距。
2. **算力不足**：大模型时代的本科与硕士训练需要GPU资源，普通院校难以负担。行动计划提出的国家教育智能算力服务平台是关键基础设施，但尚未建成。
3. **课程更新滞后**：前沿技术以月为单位迭代，教材以年为单位编写，"短实新"课程机制需要制度化。
4. **基础学科训练**：顶尖人才的共同特征是扎实的数学和物理基础（姚班、通班均以强数理为前两年核心），大规模扩张的AI专业容易"重工具、轻基础"。
5. **本科科研机会不均**：DeepSeek等案例显示在读博士、实习生能产出核心成果，但这类机会集中于少数顶尖校。
6. **K-12层面**：中国已强制推行AI教育，但教师能力与课时落实是难点；美国则缺乏AI专门课程内容。
7. **终身学习**：AI Index指出AI技能越来越多在正规教育之外获得（证书、在线学习、工作中），高校的继续教育与微证书体系尚未跟上。\[10\]

## 五、综合分析与展望

1. **"AI用于教育"与"教育培养AI"正在汇合**：中国行动计划把"学AI、用AI、创AI、护AI"统一规划，这是与美欧最大的不同；优势在执行速度，风险在于"重部署、轻评估"，韩国AI教科书就是前车之鉴。\[33\]
2. **证据格局已经清晰**：AI辅导"能有效"（哈佛、尼日利亚），但"规模化后效果收敛"（Khanmigo），"设计不当有害"（Bastani）。未来2—3年的关键不在于模型更强，而在于教学法设计、教师驱动的使用场景和评价方式的重构。
3. **人才竞争进入"留存与质量"阶段**：中国在产量和工作地上已领先，但美国在留存率、资本与算力生态上仍占优；未来的分水岭是谁能持续产出能够定义方向的原创性研究者，而不仅是大量合格的工程研究者。
4. **需要注意的不确定性**：欧盟高风险规则延期尚待理事会最终通过；美国联邦教育体制在变动；中国行动计划的大部分举措2026年才起步，效果有待评估。

## 六、强化教育对AI高尖端人才培养支撑作用的具体建议

**面向教育主管部门：**
1. **"量"转"质"**：暂停AI本科专业的低门槛扩张，对621个布点开展以师资、算力、课程为核心的专业评估，引导弱校转向"AI+行业"应用型方向，集中资源办好数十个拔尖通道。
2. **尽快建成国家教育智能算力平台**：为本科生和研究生按项目分配GPU时数（可参照"学分化算力券"），确保普通院校学生也能训练和微调模型。
3. **制度化"101计划"的快速更新机制**：核心教材每2—3年修订，前沿模块（大模型、智能体、具身智能）以"活页课程"形式每学期更新，由企业研究员与高校教师共同维护。
4. **把评估写进政策**：对行动计划中的智能学伴、学习机进校园、智能评卷等举措，要求以随机对照或准实验设计做独立评估并公开结果，避免重蹈韩国覆辙。

**面向高校：**
5. **强化数理基础**：拔尖班前两年保持高强度的数学（分析、线性代数、概率、优化）、物理和理论计算机训练；面向全校的AI通识课则以"理解原理＋负责任使用"为主。
6. **普及本科科研**：设立本科科研学分与经费，推广"导师组＋科研小组"模式；鼓励高年级本科生和硕士生到头部企业及国家实验室参与前沿项目（DeepSeek模式），并完善知识产权与学分认定。
7. **制度化产学研双向流动**：推广企业研究员兼职教授、高校教师企业访学、博士联合培养（校企双导师）；联合实验室需以人才培养产出（论文、开源、学生去向）考核，而非只看横向经费。
8. **深化交叉培养**：借鉴MIT"计算双语者"和复旦"X+AI"双学位，在AI for Science、AI与医学、AI与法律/伦理方向设立联合学位。
9. **改革考核方式**：在AI课程中采用"允许AI＋口试/现场编程/过程记录"的双轨评价，防止AI依赖侵蚀基础能力（Bastani实验的教训）。

**面向基础教育与终身学习：**
10. **K-12 AI教育"重思维、轻工具"**：小学以计算思维和数据素养为主，初中引入算法与模型原理，高中衔接数学建模与编程；明确禁止用"演示炫技课"充抵课时；为乡村学校提供基于国家平台的双师课堂。
11. **课堂AI工具默认采用"导师模式"**：在中小学推广不直接给答案、以提问引导的AI工具，把"有效使用率"（而非开通率）作为考核指标——这是Khanmigo试验最重要的政策启示。
12. **建设终身学习通道**：落实行动计划中的微专业、微证书和学分银行，面向在职工程师和教师提供与学历教育互认的AI进阶课程。\[35\]
13. **提升人才吸引力**：在顶尖AI人才回流趋势下（留存率从57%升至69%），以有竞争力的科研启动经费、算力保障和评价改革（降低"帽子"与论文数导向）留住并吸引一流青年研究者，同时保持国际学术交流的开放性。

## 七、注意事项与说明

- **数据口径**：使用率调查（HEPI、盖洛普、AI Index）多为自报，且各自对"使用"的定义不同；学习机市场数据来自IDC、洛图科技、奥维睿沃、艾媒咨询等机构，口径差异较大。
- **研究局限**：哈佛试验仅涉及两个物理主题且样本来自精英高校；尼日利亚试点仅6周；MIT脑电研究为未经同行评审的小样本预印本；Khanmigo田纳西试验是迄今最大的实验，但仅针对补救性数学。\[57\]\[61\]
- **人才数据**：卡内基AI Talent v3.0使用自填的OpenReview履历和AI辅助的数据处理，样本非随机；DeepSeek团队构成来自媒体整理而非官方披露。\[69\]
- **政策时效**：欧盟高风险条款延期、CSU合同金额、"总统超级智能挑战赛"更名等信息部分来自二手报道，须以官方最新文本为准。

## 資料來源

1. [AI Study Tools Statistics You Need to Know in 2026](https://aripsy.com/en/research/ai-study-tools-statistics-2026)
2. [Students Using AI Statistics (2026): 40+ Survey Findings](https://studycardsai.com/blog/students-using-ai-statistics)
3. [99 AI in Education Statistics for 2026 - MangoThrive](https://mangothrive.com/ai-in-education-statistics/)
4. [How Many Students Use AI in 2026? The Latest Statistics](https://www.fransizcarehberim.com/blog/students-ai-usage-statistics-2026)
5. [Student Generative Artificial Intelligence Survey 2026 - HEPI](https://www.hepi.ac.uk/reports/student-generative-ai-survey-2026/)
6. [Survey: Most teachers used AI and saved six hours of work a week](https://www.idahoednews.org/news/survey-most-teachers-used-ai-and-saved-six-hours-of-work-a-week/)
7. [AI and Teacher Workload: What the Gallup Survey Shows](https://zunkireelabs.com/blog/ai-teacher-workload-what-the-gallup-survey-shows/)
8. [AI in Education Statistics 2026: Students, Teachers, Rules](https://www.usecarly.com/blog/ai-in-education-statistics/)
9. [Education](https://hai.stanford.edu/ai-index/2026-ai-index-report/education)
10. [AI in Academia: What Stanford's 2026 AI Index Tells Us](https://wallyboston.com/ai-in-academia/)
11. [ChatGPT Is Rolling Out a New Version for Universities: Here’s What Your School Needs to Know](https://www.fisherphillips.com/en/insights/insights/chatgpt-is-rolling-out-a-new-version-for-universities)
12. [California State University to Become First AI-Powered University System in US with OpenAI](https://news.csun.edu/uncategorized/california-state-university-to-become-first-ai-powered-university-system-in-us-with-openai/)
13. [Anthropic takes on OpenAI and Google with new Claude AI features designed for students and developers](https://venturebeat.com/ai/anthropic-takes-on-openai-and-google-with-new-claude-ai-features-designed-for-students-and-developers)
14. [introducing claude for education](https://www.anthropic.com/news/introducing-claude-for-education?)
15. [Anthropic Claude for Education Brings AI to Universities](https://www.edtechinnovationhub.com/news/anthropic-launches-claude-for-education-with-campus-wide-ai-access-for-higher-ed)
16. [Anthropic Is Making It Easier to Learn How to Code](https://www.inc.com/ben-sherry/anthropic-is-making-it-even-easier-to-learn-how-to-code/91227443)
17. [New Gemini tools for students and educators](https://blog.google/products-and-platforms/products/education/gemini-iste-2025/)
18. [Gemini is now free and available for all students with new ‘Gemini for Education’ experience](https://chromeunboxed.com/gemini-is-now-free-and-available-for-all-students-with-new-gemini-for-education-experience/)
19. [How institutions worldwide used Google for Education tools in 2025](https://blog.google/products-and-platforms/products/education/google-for-education-year-in-review-2025/)
20. [AI features for educators coming to Microsoft 365 Copilot](https://www.microsoft.com/en-us/education/blog/2025/06/empowering-educators-with-ai-innovation-and-insights/)
21. [AI in education is changing fast: New Microsoft 365 Education experiences put learning first](https://www.microsoft.com/en-us/education/blog/2026/06/ai-in-education-is-changing-fast-new-microsoft-365-education-experiences-put-learning-first/)
22. [Study and Learn: AI built for your student](https://www.microsoft.com/en-us/education/blog/2026/05/study-and-learn-ai-built-for-your-student/)
23. [发布教育部等九部门《关于加快推进教育数字化的意见》并介绍贯彻落实考虑\[图文直播\] - 中华人民共和国教育部政府门户网站](http://www.moe.gov.cn/fbh/live/2025/56808/twwd/202504/t20250416_1187611.html)
24. [用好人工智能这把“钥匙” - 中华人民共和国教育部政府门户网站](http://www.moe.gov.cn/jyb_xwfb/xw_zt/moe_357/2026/2026_zt03/lhjy/lhsy/202603/t20260303_1429844.html)
25. [Q2学习机出货量增46%！IDC：科大讯飞AI学习机登顶市场销售额第一\_腾讯新闻](https://news.qq.com/rain/a/20250904A05WDA00)
26. [【月报】5月学习平板线上销量增长50.2%，作业帮、学而思、科大讯飞三强争霸\_腾讯新闻](https://news.qq.com/rain/a/20250625A04JDZ00)
27. [儿童智能学习设备调研报告：市场概况与核心产品分析|作业帮|全渠道|市场概况|步步高|知名企业|科大讯飞\_手机网易网](https://m.163.com/dy/article/KQQ2R77O0514R9KQ.html?clickfrom=subscribe&spss=adap_pc)
28. [学习机拼AI，谁是赢家？|猿辅导|AI|学而思\_新浪科技\_新浪网](https://finance.sina.com.cn/tech/roll/2025-07-01/doc-infcyazn3425896.shtml)
29. [教育部等九部门关于加快推进教育数字化的意见 - 中华人民共和国教育部政府门户网站](http://www.moe.gov.cn/srcsite/A01/s7048/202504/t20250416_1187476.html)
30. [中国智慧教育白皮书 （2025 年5 月） 中华人民共和国教育部](https://bm.cugb.edu.cn/jsfzzx/upload/resources/file/2025/05/26/266517.pdf)
31. [教育部等五部门联合印发《“人工智能+教育”行动计划》 - 安全内参](https://www.secrss.com/articles/89294)
32. [Q2学习机出货量增46%！IDC：科大讯飞AI学习机登顶市场销售额第一](https://www.qbitai.com/2025/09/328513.html)
33. [回顾2025｜教育数字化相关政策和大事-中国教育和科研计算机网CERNET](https://www.edu.cn/xxh/yc/202512/t20251231_2713557.shtml)
34. [国务院支持！近100所高校，成立“最火”学院！\_腾讯新闻](https://news.qq.com/rain/a/20250826A07N0100)
35. [教育部等五部门关于印发《“人工智能+教育”行动计划》的通知 - 中华人民共和国教育部政府门户网站](http://www.moe.gov.cn/srcsite/A16/s3342/202604/t20260410_1433240.html)
36. [Executive Order: Advancing Artificial Intelligence Education for American Youth](https://www.hklaw.com/en/insights/publications/2025/04/executive-order-advancing-ai-education-for-american-youth)
37. [Administration Issues EO to Advance AI in Classrooms](https://exceptionalchildren.org/blog/administration-issues-eo-advance-ai-classrooms)
38. [Promises and Progress: What Became of the AI Education and Workforce Executive Orders?](https://cset.georgetown.edu/article/promises-and-progress/)
39. [Melania Trump Launches 2027 Presidential Super Intelligence Challenge](https://www.thewellnews.com/white-house/melania-trump-launches-2027-presidential-super-intelligence-challenge/)
40. [AI in Academia: What Stanford’s 2026 AI Index Tells Us](https://medium.com/@wallyboston/ai-in-academia-what-stanfords-2026-ai-index-tells-us-88ee023aca3d)
41. [AI Act for Education and EdTech Compliance](https://www.legalithm.com/en/blog/ai-act-education-edtech-compliance-guide)
42. [EU AI Act for Schools: What "High-Risk" Means and What to Do About It - Lumination ai](https://lumination.ai/eu-ai-act-for-schools/)
43. [AI Act for Edtech: Assessment, Proctoring and Children's Data](https://www.a2estudiolegal.com/en/ai-act-edtech/)
44. [South Korea pulls plug on AI textbooks, leaving schools, companies without funding for them](https://www.thestar.com.my/aseanplus/aseanplus-news/2025/08/04/south-korea-pulls-plug-on-ai-textbooks-leaving-schools-companies-without-funding-for-them)
45. [South Korea’s AI Textbooks Ends in Disaster: What Failed?](https://www.itechguides.com/south-koreas-experiment-in-ai-textbooks-ends-in-disaster-but-not-for-the-reason-you-think/)
46. [South Korea's rushed AI textbook rollout failed its own...](https://vibegraveyard.ai/story/south-korea-ai-textbook-rushed-rollout/)
47. [South Korea removes legal status of AI digital textbooks - The Legal Wire](https://thelegalwire.ai/south-korea-removes-legal-status-of-ai-digital-textbooks/)
48. [How AI is giving teachers back six weeks of time each school year](https://www.yahoo.com/news/articles/ai-giving-teachers-back-six-130000111.html)
49. [AI Saves Teachers 6 Hours a Week. But 97% Don't Notice](https://mysummit.school/blog/en/ai-helps-instructors-research-2026/)
50. [What the Harvard AI Tutor Trial Really Showed (and What It Means for Question Banks)](https://www.iatrox.com/blog/harvard-ai-tutor-trial-what-it-showed-question-banks)
51. [What a Harvard experiment actually showed about AI tutors](https://barrisreview.com/blog/harvard-ai-tutor-rct/)
52. [How Harvard Made Physical Sciences 2 Easy for Half the Class - AI Tutor Platform & VR Labs](https://www.victoryxr.com/how-harvard-made-physical-sciences-2-easy-for-half-the-class/)
53. [Harvard study finds AI tutor beats in-class physics teaching - Mjengo Hub](https://mjengohub.co.ke/articles/news/harvard-study-finds-ai-tutor-beats-in-class-physics-teaching)
54. [AI Tutors: What the Randomized Trials Found, and What They Cost](https://metaroles.ai/posts/ai-tutors-trials)
55. [15e1ff08 15ae 4f7a b2a8 d146e6c113ee](https://openknowledge.worldbank.org/signposting/describedby/15e1ff08-15ae-4f7a-b2a8-d146e6c113ee)
56. [World Bank RCT finds AI tutoring boosts English learning outcomes in Nigeria • It Does What Now?](https://itdoeswhatnow.com/m/2025-02-18-world-bank-rct-finds-ai-tutoring-boosts-english/)
57. <https://edworkingpapers.com/sites/default/files/ai26-1551.pdf>
58. [EU AI Act training for education & vocational training](https://www.regulatoryai.eu/academy/sectors/education/)
59. [Generative AI without guardrails can harm learning: Evidence from high school mathematics - PubMed](https://pubmed.ncbi.nlm.nih.gov/40560616/)
60. [Massimo on X: "An MIT Media Lab study used EEG to track what happens in the brain when people write with ChatGPT rather than on their own. Fifty four students completed essay tasks while wearing electrode caps. One group used ChatGPT, one used a search engine, and one used no tools. Across sessions… / X](https://x.com/Rainmaker1973/status/2094076181658112058)
61. [AI Cognitive Debt and ChatGPT - What the MIT Study Says](https://learn.senwitt.com/research/cognitive-debt/)
62. [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://www.researchgate.net/publication/393011815_Generative_AI_without_guardrails_can_harm_learning_Evidence_from_high_school_mathematics)
63. [South Korea's Privacy Regulator Helps Unwind the National AI Digital Textbook Rollout · Evidoria](https://evidoria.eu/practice/south-koreas-privacy-regulator-helps-unwind-the-national-ai-digital-textbook-rollout/)
64. [Written evidence by Dr Sayed Elhoushy and Dr Jasmine Mohsen (AIE0098)](https://committees.parliament.uk/writtenevidence/164935/pdf/)
65. [Stanford AI Index 2026 shows AI adoption pressure on education and jobs](https://www.edtechinnovationhub.com/news/ai-adoption-accelerates-as-stanford-report-highlights-pressure-on-education-jobs-and-infrastructure)
66. [How Teachers Use AI: 2026 Stats—60% Use It (Gallup, RAND)](https://theagentalmanac.com/articles/how-real-teachers-use-ai-2026)
67. [學習機拼AI,誰是贏家?|科大訊飛|學而思|硬件|百度|学习机\_新浪新闻](https://k.sina.cn/article_7857141524_1d452771401901yqws.html?from=tech)
68. [Korea undermines its own AI goals by downgrading digital textbooks](https://www.koreajoongangdaily.com/opinion/korea-undermines-its-own-ai-goals-by-downgrading-digital-textbooks/12298226)
69. [Who’s Ahead in the Global AI Talent Race?](https://carnegieendowment.org/features/whos-ahead-in-the-global-ai-talent-race)
70. [Study Finds US Remains a Magnet for World's Best and Brightest AI Talent, but More Global Talent are Staying Home Instead of Going Abroad - Paulson Institute](https://www.paulsoninstitute.org/press_release/study-finds-us-remains-a-magnet-for-worlds-best-and-brightest-ai-talent-but-more-global-talent-are-staying-home-instead-of-going-abroad/)
71. [DeepSeek 创始团队介绍 & 大模型降低算力和实现高质量模型效果的核心技术分析\_deepseek创建团队-CSDN博客](https://blog.csdn.net/universsky2015/article/details/145479083)
72. [起底DeepSeek团队：从蜗居出租屋到登顶排行榜，85后浙大硕士梁文锋带领本土年轻学霸，震动美国科技圈|AI\_新浪财经\_新浪网](https://finance.sina.com.cn/roll/2025-01-27/doc-inehkyex9369462.shtml)
73. [全网都在扒的DeepSeek团队，是清北应届生撑起一片天\_创事记\_新浪科技\_新浪网](https://finance.sina.com.cn/tech/csj/2025-01-06/doc-inecznxv3066739.shtml)
74. [警惕美国挖角DeepSeek - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com.cn/developer/news/2133286)
75. [教育部人工智能领域“101计划”建设成果发布-中国社会科学网](https://www.cssn.cn/skgz/bwyc/202507/t20250719_5886998.shtml)
76. [人工智能“101计划”核心教材发布|人工智能\_新浪财经\_新浪网](https://finance.sina.com.cn/jjxw/2025-07-23/doc-infhnqmp3489184.shtml)
77. [教育部人工智能领域 “101计划”教材正式发布！ —教育在线](https://news.eol.cn/yaowen/202507/t20250721_2682111.shtml)
78. [官宣！大学新增“人工智能教育”专业，学什么？](https://www.dutenews.com/n/article/8806669)
79. [15所高校入选教育部重磅计划！何为人工智能“101计划”](https://www.acabridge.cn/news/202408/t20240807_2628125.shtml)
80. [2024 年清华学堂计算机科学实验班（姚班）报考指南 世界著名计算机科学家、2000 年图灵奖得主姚期智院士分别于2005 年、2019 年和2021](https://m.join-tsinghua.edu.cn/qinghuadaxue2024nianyaobanbaokaozhinan.pdf)
81. [清华姚班修改本科培养模式：姚班、智班、量信班全合并-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2082353)
82. [姚班培养-清华大学交叉信息研究院](https://iiis.tsinghua.edu.cn/ybbks/ybpy.htm)
83. [北大和清华联合建立通用人工智能实验班-北大教育基金会](https://www.pkuef.org/old/info/1175/6275.htm)
84. [北大清华合力打造通用人工智能实验班-CSDN博客](https://blog.csdn.net/zandaoguang/article/details/116213335)
85. [Carnegie Mellon University starts first AI degree program in U.S.](https://venturebeat.com/ai/carnegie-mellon-university-starts-first-ai-degree-program-in-u-s)
86. [Undergraduate Artificial Intelligence Program \< Carnegie Mellon University](http://coursecatalog.web.cmu.edu/previous/2018-2019/schoolofcomputerscience/artificialintelligence/)
87. [Artificial Intelligence Program \< Carnegie Mellon University](https://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/artificialintelligence/)
88. [Carnegie Mellon University](https://www.cmu.edu/ambassadors/june-2018/ai-major.html)
89. [The Institute launches a college](https://www.technologyreview.com/2018/12/19/138376/the-institute-launches-a-college/)
90. [A step into the future: The MIT Stephen A. Schwarzman College of Computing](https://reif.mit.edu/speeches-writing/step-future-mit-stephen-schwarzman-college-computing)
91. [MIT Reshapes Itself to Shape the Future](https://computing.mit.edu/about/history)
92. [Educating Computing Bilinguals](https://computing.mit.edu/academics/educating-computing-bilinguals)
93. [Human-Centered Artifical Intelligence](https://momentum.stanford.edu/initiatives/human-centered-artificial-intelligence)
94. [Stanford Students](https://hai.stanford.edu/education/courses)
95. [AI + Education • Stanford Accelerator for Learning](https://acceleratelearning.stanford.edu/initiative/digital-learning/ai-and-education/)
96. [Only 6% of teachers say their school’s AI policy is clear](https://thenextweb.com/news/stanford-ai-index-2026-education)