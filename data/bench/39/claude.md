# 不同类型游戏用户画像分析报告（2024–2026，中国为主、海外对照）

**一句话结论：**  中国玩家盘子已经见顶。2025年游戏用户6.83亿，同比只增1.35%。 [xinhuanet](http://www.xinhuanet.com/20251219/71b9f7db89c84eee968cddeeeb86baf1/c.html)增量主要来自三类人：36岁以上的小游戏用户、女性玩家，以及跨端的老玩家。所以立项最该先判断的，是你在争夺哪一层人群、他们愿意用什么方式付费，题材本身反而排在后面。同一品类在中国和海外的画像差异，往往比品类之间的差异还大。

## TL;DR

- **人群结构已经分层。**  手游APP偏年轻：35岁及以下占63.7%。微信小游戏偏中年：36岁及以上占54.7%（QuestMobile 2026年5月数据）。两边用户重合度"不足10%"（微信小游戏产品总监李卿，2025），同一个品类做APP和做小游戏，实际上面对两拨不同的人。
- **品类画像的核心差异在动机和付费结构。**  SLG是30–39岁男性、重度大R。二次元是24岁以下、男性为主的内容消费者。消除和模拟经营女性占比可达约70%。MOBA和派对游戏性别最均衡。AAA单机买断以18–35岁男性为主。 [digitaling](https://www.digitaling.com/articles/1412543.html) [gameinformer](https://gameinformer.com/b/news/archive/2017/01/21/study-breaks-down-game-genre-playerbases-by-gender.aspx)[donews](https://www.donews.com/news/detail/1/6196437.html)
- **对开发者的建议。**  先选人群，再选玩法。用TapTap预约、Steam愿望单和小规模CPI测试来验证画像，不要只靠行业平均数。公开的分品类基准，本身大多带有幸存者偏差和样本偏差。

---

## 研究范围与假设（按最佳判断设定）

- **市场：**  以中国国内为主，系统对照北美/欧洲、日本、韩国、东南亚，拉美和中东北非略提。
- **平台：**  手游（APP与小程序）、PC（Steam与国内客户端）、主机。
- **品类：**  共13大类，另附恐怖、女性向/乙游和银发玩家。
- **数据口径：**  每个数字都标注年份和来源类型（调研/遥测/社媒监测/行业经验）。没有公开硬数据的地方标为"估计"或"经验区间"。

## 核心结论（给开发者的10条可执行要点）

1. **国内已是存量市场。**  2025年中国游戏收入3507.89亿元（+7.68%），用户6.83亿（+1.35%），收入增速远高于用户增速。这意味着增长主要靠提高ARPU和长线运营，不再靠拉新。 [xinhuanet](http://www.xinhuanet.com/20251219/71b9f7db89c84eee968cddeeeb86baf1/c.html)
2. **小游戏是一个独立的人群池，不只是一个渠道。**  2025年小程序游戏收入535.35亿元（+34.39%），其中广告变现占31.89%。微信小游戏MAU在2026年5月达6.54亿（+32.7%），用户偏中年：2026微信小游戏开发者大会官方口径为24岁以下占10%、24–40岁占50%、40岁以上占40%，女性47%。想做IAA+IAP混合变现，首选这里。 [sina](https://finance.sina.com.cn/roll/2025-12-19/doc-inhcipum2338201.shtml?froms=ggmp)
3. **女性玩家接近半数，但集中在特定品类。**  消除、模拟经营、乙游、派对UGC的女性占比最高，硬核射击和体育最低（Quantic Foundry样本中不足5%）。只给产品"加个女性皮肤"是没用的，必须在动机层面匹配。 [nugamers](https://nugamers.eu/wp-content/uploads/2024/10/women-in-gaming-part1.pdf)
4. **年龄是预测动机最强的变量。**  竞争（Competition）动机随年龄下降最快，13–35岁降幅最大；36岁以上玩家的首要动机变为幻想（Fantasy）和收集完成（Completion）。所以面向30+人群的产品，应该做低对抗、重养成、重社交合作。 [quanticfoundry](https://quanticfoundry.com/2016/08/11/appeal-of-competition/) [quanticfoundry](https://quanticfoundry.com/2016/12/15/primary-motivations/)
5. **SLG的"中年男性大R"画像正在被休闲化稀释。**  《三国：冰河时代》女性占比超过30%，传统SLG约15%；率土"青春服"把18–30岁玩家拉到60%以上。真正决定收入的仍是大R，但获客侧必须靠休闲化入口。 [sohu](https://www.sohu.com/a/1050588155_118576) [163](https://www.163.com/dy/article/K29MPDNL0546AIJW.html)
6. **二次元赛道在收缩，用户高度集中。**  核心二次元用户0.92亿，男性63%，24岁以下57.5%（QuestMobile 2025）。2025年产业报告也指出二次元游戏继续下行、多数新品未达预期。新品要么做出差异化内容，要么考虑出海日本。 [digitaling](https://www.digitaling.com/articles/1412543.html) [oeeee](https://m.mp.oeeee.com/a/BAAFRD0000202512191496303.html)
7. **射击品类在国内已分化为两种人群。**  《三角洲行动》七成以上是35岁以下男性，偏硬核；《和平精英》性别均衡，深耕下沉市场。立项时要先想清楚：你要的是硬核战术玩家，还是全民社交玩家？ [qq](https://news.qq.com/rain/a/20260721A0573A00)
8. **主机和单机在国内是增速最快的小池子。**  2025年国内主机收入83.62亿元，同比+86.33%，但体量只有移动端的约3%。这块适合买断制精品和全球发行，不适合国内买量。 [baidu](https://baike.baidu.com/item/2025%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%B8%B8%E6%88%8F%E4%BA%A7%E4%B8%9A%E6%8A%A5%E5%91%8A/67101368)
9. **留存基准要分平台、分地区看。**  GameAnalytics 2025年中位数为D1约22%、D7不到4%，亚洲D7中位数只有2.68%。业内流传的"次留40%"大多出自头部产品，不能当作及格线。 [gameanalytics](https://www.gameanalytics.com/reports/2026-mobile-pc-gaming-benchmarks)[investgame](https://investgame.net/wp-content/uploads/2026/01/2026-01-27-2026-mobile-pc-benchmarks_compressed.pdf)
10. **获客成本差距极大。**  美国策略/RPG的iOS CPI约5.5–6美元，休闲Android在Liftoff全球口径统计中低至0.14美元。重度品类回本靠iOS和T1国家，泛用户品类靠短视频素材和小游戏裂变。

---

## 一、大盘与玩家基础画像

### 1.1 中国（2025年，中国音数协游戏工委/伽马数据《2025年中国游戏产业报告》）

| 指标 | 数值 | 同比 |
| --- | --- | --- |
| 实际销售收入 | 3507.89亿元 | +7.68% |
| 用户规模 | 6.83亿 | +1.35% [fujian](https://swt.fujian.gov.cn/xxgk/jgzn/jgcs/fwyfzc/dtzx_460/202512/t20251226_7061383.htm) |
| 移动游戏 | 2570.76亿元（占73.29%） | +7.92% [tgbus](https://m.tgbus.com/news/238822)[oeeee](https://m.mp.oeeee.com/a/BAAFRD0000202512191496303.html) |
| 客户端游戏 | 781.6亿元 | +14.97% |
| 主机游戏 | 83.62亿元 | +86.33% [baidu](https://baike.baidu.com/item/2025%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%B8%B8%E6%88%8F%E4%BA%A7%E4%B8%9A%E6%8A%A5%E5%91%8A/67101368) |
| 小程序游戏 | 535.35亿元（内购68.11%/广告31.89%） | +34.39% [sina](https://finance.sina.com.cn/roll/2025-12-19/doc-inhcipum2338201.shtml?froms=ggmp) |
| 网页游戏 | 43.25亿元 | -6.74% [oeeee](https://m.mp.oeeee.com/a/BAAFRD0000202512191496303.html) |
| 自研游戏海外收入 | 204.55亿美元 | +10.23% [baidu](https://baike.baidu.com/item/2025%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%B8%B8%E6%88%8F%E4%BA%A7%E4%B8%9A%E6%8A%A5%E5%91%8A/67101368) |

- **小游戏爆发：**  伽马数据统计，2024年小程序游戏市场398.36亿元（+99.18%），2022–2024年复合增长率182.3%。 [gelonghui](https://m.gelonghui.com/p/1484955)
- **APP与小游戏的人群分化（QuestMobile）：**
    - 2025年8月：手游APP用户中30岁以下占50.4%；微信小游戏用户中40岁以上占42.1%，三线及以下城市占58.4%。 [donews](https://www.donews.com/news/detail/1/6196437.html)
    - 2026年5月：手游APP中35岁及以下占63.7%，三线及以下城市近五成；微信小游戏中36岁及以上占54.7%，而一线、新一线、二线城市占比升至57%。 [36kr](https://36kr.com/p/3904748532450950)
    - 两期数据显示，小游戏正在向高线城市和高消费人群扩张。两期的城市口径可能不同，比较时需谨慎。
- **使用强度（QuestMobile 2026年5月）：**  手游APP人均每天打开23.8次、使用111.2分钟；微信小游戏人均每天23.6分钟（+10.3%），单次时长在增加，用户行为在向中重度游戏倾斜。 [36kr](https://36kr.com/p/3904748532450950)
- **人群重合度：**  微信小游戏产品总监李卿在2025微信小游戏开发者大会（2025年6月）群访中表示："小游戏与APP游戏的用户重合度，不足10%……玩小游戏的人和玩APP的人是两拨人。"另据财联社报道，整体重合度"不过五成"，10%指的是重度游戏。
- **女性玩家：**
    - 伽马数据：2024年女性向游戏市场80亿元，同比+124.1%；25.94%的受访者对女性向/恋爱玩法感兴趣。 [gelonghui](https://m.gelonghui.com/p/1484955)
    - 业内媒体引用的2025年产业年会数据称，女性占网络游戏用户约48%（二手转述，需核实原报告）。 [qq](https://news.qq.com/rain/a/20260225A060QY00)
    - 《女性向游戏调研报告》（2025年12月18日，中国音数协副秘书长唐贾军在中国游戏产业年会上发布）："有61.3%的受访玩家为单身"，受访者"以学历较高的90后、00后青年女性为主"，多为学生和职员。
- **核心用户（QuestMobile 2025年12月）：**  核心用户数前五为《开心消消乐》《王者荣耀》《三角洲行动》《和平精英》《金铲铲之战》；微信小游戏MAU前十均超过1200万，塔防、策略、消除、益智休闲四类主导。 [gamelook](http://www.gamelook.com.cn/2026/03/589129/)

### 1.2 全球与主要海外市场

- **全球（Newzoo 2025）：**
    - 收入188.8亿美元（+3.4%），后上调为约1970亿美元（+7.5%）。 [gamesmarket](https://www.gamesmarket.global/newzoo-report-global-gaming-revenue-is-expected-to-reach-dollar1888-billion-in-2025-with-growth-set-to-continue-f4d9c4b86e8410e860dcca74905b3197/)[g-mnews](https://g-mnews.com/en/global-games-market-to-reach-usd-197-billion-in-2025-exceeding-previous-forecasts/)
    - 玩家约35.78亿，其中移动29.85亿、PC 9.36亿、主机6.45亿；亚太占53%的玩家和46%的收入。 [Substack](https://gamedevreports.substack.com/p/newzoo-the-games-market-in-2025)
    - 付费玩家16亿（占44%），年均每付费玩家消费约119.7美元。 [g-mnews](https://g-mnews.com/en/global-games-market-to-reach-usd-197-billion-in-2025-exceeding-previous-forecasts/)
    - 中国（498亿美元）和美国（496亿美元）合计约占50%。 [gamesmarket](https://www.gamesmarket.global/newzoo-report-global-gaming-revenue-is-expected-to-reach-dollar1888-billion-in-2025-with-growth-set-to-continue-f4d9c4b86e8410e860dcca74905b3197/)
    - Alpha世代（2010年后出生）在PC端占比上升；拉美玩家增速最快（+5.3%）。 [icon-era](https://icon-era.com/statistics/video-game-statistics/)[Substack](https://gamedevreports.substack.com/p/newzoo-the-games-market-in-2025)
- **美国（ESA Essential Facts）：**
    - 2025年：2.051亿人玩游戏，平均年龄36岁，女性47%、男性52%，一半玩家在35岁以上；5–12岁儿童83%每周玩游戏；82%玩游戏的父母会和孩子一起玩。 [cepro](https://www.cepro.com/news/esa-essential-facts-about-u-s-video-game-industry-report-finds-60-of-adults-are-gamers/618975/)[theesa](https://www.theesa.com/annual-esa-study-reveals-video-games-universal-appeal-across-generations/)
    - 2026年：2.123亿人，平均年龄37岁。 [gamesbeat](https://gamesbeat.com/average-age-of-gamers-hits-37-while-67-of-americans-play-esa-ceo-interview/)
- **全球调研（ESA Power of Play 2025，覆盖21–22国、24,216名16岁以上玩家）：**
    - 平均年龄41岁，男51%、女48%。 [techspot](https://www.techspot.com/news/109812-esa-report-shows-average-gamer-41-ndash-nearly.html)[Substack](https://gamedevreports.substack.com/p/esa-global-video-games-report-2025)
    - 主力平台：手机55%、PC 21%、主机21%。 [Substack](https://gamedevreports.substack.com/p/esa-global-video-games-report-2025)
    - 女性更多用手机（64%对男性46%），更偏益智（62%对39%）。 [Substack](https://gamedevreports.substack.com/p/esa-global-video-games-report-2025)
- **日本（《Fami通游戏白书2026》）：**  2025年国内游戏市场2兆5885亿日元（+8.0%），游戏人口5639.3万（+3.0%）。 [kendama-games](https://kendama-games.jp/column/2026-10-11-japan-game-market-2025-volume-or-price/)主机和PC小幅增长，移动端下滑。 [famitsu](https://www.famitsu.com/article/202608/83758)2025年家用游戏店头市场4181亿日元（同比138.8%，Switch 2效应）。 [prtimes](https://prtimes.jp/main/html/rd/p/000018625.000007006.html)
- **韩国（KOCCA）：**
    - 《2025游戏使用者实态调查》：游戏使用率降至50.2%（-9.7个百分点），是2015年调查以来最低， [gamegeneration](https://www.gamegeneration.or.kr/article/045a8130-7f48-467e-8fdf-3d9c7f8aff47)调查设计有调整。玩家中手机使用率89.1%、PC 58.1%（+4.3个百分点）、主机28.6%。10代使用率80.9%，60代只有23.1%。 [daum](https://v.daum.net/v/20251218134801865)[gamegeneration](https://www.gamegeneration.or.kr/article/045a8130-7f48-467e-8fdf-3d9c7f8aff47)
    - 2024年调查：47.2%的玩家近一年去过PC房，去PC房的主要动机是和朋友一起玩。 [ilovepcbang](https://www.ilovepcbang.com/news/articleView.html?idxno=111967)
    - 《2025大韩民国游戏白书》：2024年产业规模23.85万亿韩元，其中移动59.0%、PC 25.2%、主机5.0%。 [zdnet](https://zdnet.co.kr/view/?no=20260325142500)
- **东南亚（Niko Partners，SEA-6）：**
    - 2024年：玩家2.8582亿，收入53.7亿美元，年ARPU 18.80美元。 [nikopartners](https://nikopartners.com/sea-of-opportunities-exploring-the-rise-of-southeast-asia-video-games-market/)
    - 2025年：收入约56.3亿美元（+4.7%）；预计2026年玩家超过3亿。印尼玩家超过1.26亿。 [Substack](https://gamedevreports.substack.com/p/niko-partners-southeast-asias-gaming)[nikopartners](https://nikopartners.com/7-billion-in-2030-opportunities-in-southeast-asias-video-game-markets/)
    - 52%的玩家看游戏直播；MOBA主导（印尼、马来西亚、菲律宾以《Mobile Legends》为主，泰国、越南以《传说对决》为主）。 [nikopartners](https://nikopartners.com/sea-of-opportunities-exploring-the-rise-of-southeast-asia-video-games-market/)
    - 不付费玩家比例在各国上升10–20个百分点。 [nikopartners](https://nikopartners.com/sea-of-opportunities-exploring-the-rise-of-southeast-asia-video-games-market/)
    - 移动端收入占比：Niko 2023年口径为66.4%，Newzoo 2024年口径为73%； [pocketgamer](https://www.pocketgamer.biz/the-state-of-southeast-asias-games-industry-in-2025/)[Substack](https://gamedevreports.substack.com/p/niko-partners-the-6-largest-gaming)两者市场口径不同，不宜混用。

---

## 二、动机框架速查（贯穿各品类）

- **Quantic Foundry 12项动机：**  破坏、刺激、竞争、社区、挑战、策略、收集完成、力量（养成）、幻想、故事、设计（自我表达）、探索。
- **关键规律（Quantic Foundry，样本偏核心玩家）：**
    - 竞争动机随年龄下降最快，13–35岁之间降幅最大。
    - 36岁以上玩家的首要动机为幻想和收集完成，刺激和挑战最低。 [medium](https://medium.com/ironsource-levelup/gamer-motivations-4-surprising-findings-5f705c212a93)
    - 策略是对年龄最不敏感的动机，但9年来整体下降最多，年轻群体降得最明显。 [quanticfoundry](https://quanticfoundry.com/2024/05/21/strategy-decline/)[playerdriven](https://playerdriven.io/desk/quantic-foundry-s-nick-yee-on-gamer-motivations-part-2)
    - 中国玩家的动机受年龄和性别影响小于美国玩家，同质性更高。 [medium](https://medium.com/ironsource-levelup/gamer-motivations-4-surprising-findings-5f705c212a93)
    - 女性和年长玩家更偏好第三人称视角。 [quanticfoundry](https://quanticfoundry.com/2023/01/27/perspective/)
- **女性占比按品类（Quantic Foundry，2017年，样本女性18.5%，偏核心玩家）：**
    - 消除（Match-3）和家庭/农场模拟约69%。出自Quantic [gameinformer](https://gameinformer.com/b/news/archive/2017/01/21/study-breaks-down-game-genre-playerbases-by-gender.aspx) Foundry 2017年1月19日博文《Beyond 50/50》（约27万名玩家样本），原文定义："在数据中提到Match-3游戏的玩家里，69%是女性"。
    - 休闲益智42%，氛围探索41%，奇幻MMO 36%。 [gameinformer](https://gameinformer.com/b/news/archive/2017/01/21/study-breaks-down-game-genre-playerbases-by-gender.aspx)
    - 战术射击和体育游戏不足5%，体育仅2%。 [quanticfoundry](https://quanticfoundry.com/2017/01/19/female-gamers-by-genre/)[nugamers](https://nugamers.eu/wp-content/uploads/2024/10/women-in-gaming-part1.pdf)
    - 单款游戏：LoL 14%，Dota 2 6%，守望先锋16%。 [ddmagency](https://www.ddmagency.com/news/female-gamers-genre/)
    - 这组数据较旧，绝对值偏低，但品类之间的相对排序至今仍有参考价值。
- **Bartle映射（经验判断）：**  MOBA/射击偏杀手型和成就型；MMO/SLG偏社交型和成就型；开放世界偏探索型；派对/UGC偏社交型和探索型。

---

## 三、分品类用户画像

> 说明：各品类的"人口统计"优先使用中国数据，海外作对照。D1/D7和付费率在没有公开分品类统计时，标注为"经验区间（估计）"，需要用自有数据校准。

### 3.1 MOBA（王者荣耀 / LoL / Mobile Legends）

- **人口统计：**
    - 中国手游MOBA是性别最均衡的竞技品类。极光2017年数据显示《王者荣耀》女性占54.1%（较早数据）；2026年QuestMobile显示其核心用户渗透率超过35%。 [pingwest](https://www.pingwest.com/w/127261)[36kr](https://36kr.com/p/3904748532450950)
    - 东南亚MOBA是第一大品类，《Mobile Legends》M6世界赛峰值观看412万。 [nikopartners](https://nikopartners.com/sea-of-opportunities-exploring-the-rise-of-southeast-asia-video-games-market/)
    - PC端LoL女性约14%（Quantic Foundry），明显比手游男性化。 [ddmagency](https://www.ddmagency.com/news/female-gamers-genre/)
- **动机：**  竞争、挑战、社区（开黑）。女性玩家入坑多因社交，选英雄更看外形（企鹅智酷2017：17.8%对男性6.3%）。 [jiemian](https://www.jiemian.com/article/1535181.html)
- **行为：**  碎片化单局（约15–20分钟），晚间高峰，强社交链；核心用户粘性极高，长线留存靠好友关系。
- **付费：**  公平竞技前提下，靠皮肤/外观和通行证变现；付费率高，ARPPU中等，鲸鱼集中度低于SLG和二次元。
- **获客：**  不靠买量，靠社交关系链（微信/QQ）、电竞和直播（KPL、MPL）。
- **对开发者的启示：**  存量被头部锁死，新品很难撼动；真正的机会在细分变体（3v3、休闲MOBA、IP化）和出海东南亚/拉美。设计上要守住"外观付费、不卖数值"的底线。

### 3.2 射击 / 战术射击 / 大逃杀（和平精英、三角洲行动、CS2、Valorant、COD、Fortnite）

- **人口统计：**
    - 《三角洲行动》七成以上为35岁以下男性；《和平精英》性别均衡、深耕下沉市场（QuestMobile 2026）。 [qq](https://news.qq.com/rain/a/20260721A0573A00)
    - 海外战术射击女性不足5%（Quantic Foundry）；PC射击2025年全球收入约90亿美元（Newzoo）。 [Substack](https://gamedevreports.substack.com/p/newzoo-the-games-market-in-2025)[nugamers](https://nugamers.eu/wp-content/uploads/2024/10/women-in-gaming-part1.pdf)
- **动机：**  竞争、刺激、破坏、挑战。女性更偏奇幻和近战武器，对枪械类兴趣较低（Quantic Foundry）。 [quanticfoundry](https://quanticfoundry.com/2017/02/09/theme-and-weapon/)
- **行为：**  长时段多局；搜打撤类玩法单局20–40分钟，偏周末和晚间。
- **付费：**
    - 皮肤、通行证、抽奖箱是主流；《三角洲行动》引入可交易的经济系统。 [zhihu](https://zhuanlan.zhihu.com/p/1971950454708639248)
    - 2025年射击品类移动端IAP增长约8.26亿美元（行业媒体转述Sensor Tower口径，需核实）。
- **获客：**  直播、主播、电竞，B站和抖音的高光剪辑；海外靠Twitch、YouTube、Discord。
- **对开发者的启示：**  硬核向做PC+手游跨端和反作弊；全民向做社交、低门槛和下沉市场。Newzoo指出Steam玩家越来越偏向非竞技的PvE，"PvE射击/合作撤离"是一个空档。 [games](https://games.gg/news/newzoo-2025-game-market-report/)

### 3.3 RPG / MMORPG / ARPG（梦幻西游、逆水寒、Diablo、PoE）

- **人口统计：**  国内端游MMO用户以25–40岁男性为主，老牌IP（如梦幻西游）用户偏中年、高线城市（估计）。奇幻MMO女性占比约36%，高于科幻MMO（Quantic Foundry）。新IP的卡通化可以拓宽人群：《洛克王国：世界》以35岁以下为主，女性占比高于MMORPG行业平均（QuestMobile [gameinformer](https://gameinformer.com/b/news/archive/2017/01/21/study-breaks-down-game-genre-playerbases-by-gender.aspx)[nugamers](https://nugamers.eu/wp-content/uploads/2024/10/women-in-gaming-part1.pdf) 2026）。 [qq](https://news.qq.com/rain/a/20260721A0573A00)
- **动机：**  力量（养成）、社区（公会）、收集完成、幻想；ARPG另加挑战和破坏。
- **行为：**  会话长、日常任务驱动；端游有赛季性；RPG有"降肝减氪"需求（伽马数据2025趋势报告）。 [sohu](https://www.sohu.com/a/838960451_121840847)
- **付费：**
    - 2025年RPG是移动端IAP下滑最明显的品类之一（AppMagic）：美国Google Play上RPG付费用户D90 ARPPU同比下降42%，App Store则上升。 [Substack](https://gamedevreports.substack.com/p/appmagic-mobile-games-monetization?open=false)
    - 首充均价：Google Play 8.3美元，App Store 17.9美元（AppMagic）。 [Substack](https://gamedevreports.substack.com/p/appmagic-mobile-games-monetization)
    - 业内数据称RPG/策略付费转化率约1.5%（Segwise口径）。 [juegostudio](https://www.juegostudio.com/blog/arpdau-benchmarks-by-game-genre)
- **获客：**  CPI高（美国iOS约6美元、Android约4.5美元，Business of Apps）；国内靠买量加明星/IP。 [playio](https://blog.playio.co/game-cpi-strategy)
- **对开发者的启示：**  传统MMO数值付费在收缩，转向外观付费、多端互通和社交轻量化（如逆水寒式"不卖数值"）；ARPG可走Steam买断加赛季制。

### 3.4 二次元 / Gacha（原神、星铁、明日方舟、FGO、赛马娘、鸣潮）

- **人口统计：**
    - 中国核心二次元用户0.92亿，男性63%，24岁以下57.5%，25–30岁13.6%；泛二次元3.51亿（QuestMobile 2025年8月）。用户集中在一二线城市。 [digitaling](https://www.digitaling.com/articles/1412543.html) [sohu](https://www.sohu.com/a/455398499_121048390)
    - 日本：米哈游系玩家平均26岁，男女约6:4（XTrend 2025上半年）。日本二次元手游整体为20–35岁、男性为主。 [qq](https://news.qq.com/rain/a/20250716A0A6DU00)[gamelook](http://www.gamelook.com.cn/2025/07/574747/)
- **动机：**  故事、幻想、收集完成、设计（角色审美），社交弱、内容消费强。 [sohu](https://www.sohu.com/a/455398499_121048390)
- **行为：**  版本驱动（约6周一版），版本初期活跃高峰明显；多款二次元游戏并行游玩很常见。 [sohu](https://www.sohu.com/a/455398499_121048390)
- **付费：**  角色/武器抽卡，付费率和ARPPU都高，鲸鱼集中度高，"为爱付费"。谷子（周边）经济兴趣用户中女性占54.1%，二次元的衍生消费由女性驱动。 [digitaling](https://www.digitaling.com/articles/1412543.html)
- **获客：**  B站、TapTap、微博、小红书，PV和KOL二创；对传统买量依赖较低，依赖口碑和预约量。 [sohu](https://www.sohu.com/a/455398499_121048390)
- **2025年市场：**  产业报告指出二次元游戏继续下行，多数新品未达预期。 [oeeee](https://m.mp.oeeee.com/a/BAAFRD0000202512191496303.html)
- **对开发者的启示：**  不要做"又一个原神"。可以考虑差异化题材、轻量化（降肝）、男性向/女性向细分，或者以日本为首发市场。美术和角色是第一转化要素。

### 3.5 SLG / 4X / 塔防 / RTS（率土之滨、三国志·战略版、ROK、无尽冬日、Last War、COC；PC文明/P社）

- **人口统计：**
    - 腾讯广告2022白皮书：国内SLG用户约6490万，男性88%，26–30岁居多，本科以上57%，半数已婚已育，60%以上家庭月收入超过1.5万元。 [sina](https://finance.sina.cn/tech/2022-11-07/detail-imqqsmrp5166876.d.html?oid=3831854140972787&vt=4&wm=4007)
    - DataEye：三国SLG买量素材86.74%面向男性，30–39岁占39.57%。 [donews](https://www.donews.com/news/detail/4/3126790.html)
    - 海外休闲SLG（WOS/Last War）主打25–45岁泛用户（行业分析，估计）。 [kchuhai](https://www.kchuhai.com/report/view-67391.html)
- **动机：**  策略、力量、社区（联盟）、竞争（国战）。36岁以上玩家的动机与之高度契合。
- **行为：**  碎片化多次登录加长期赛季；SLG玩家对品类忠诚，70%玩过多款SLG，人均一年玩5.1款（腾讯广告2022）。 [sina](https://finance.sina.cn/tech/2022-11-07/detail-imqqsmrp5166876.d.html?oid=3831854140972787&vt=4&wm=4007)
- **付费：**  典型大R结构。Last War美国iOS ARPDAU 2.47美元，WOS为1.08美元（Sensor Tower）。策略品类付费用户D90消费是博彩类的2倍，App [qq](https://news.qq.com/rain/a/20250209A0003L00) Store ARPPU可达Google Play的4–8倍（AppMagic 2025）。Last [Substack](https://gamedevreports.substack.com/p/appmagic-mobile-games-monetization) War 2024年收入超过11亿美元（Sensor Tower）。 [qq](https://news.qq.com/rain/a/20250209A0003L00)
- **获客：**  "副玩法素材"是核心手段。Last War的数字射击小游戏素材占其多渠道展示量的50%以上（Sensor Tower）。美国CPI约iOS [jiemian](https://www.jiemian.com/article/12347420.html) 5.5、Android 4.0美元（Business of Apps）。Liftoff《2025 [playio](https://blog.playio.co/game-cpi-strategy) Casual Gaming Apps Report》显示策略类iOS D30 ROAS达60%，在各品类中仅次于体育（80%）和儿童（68%）。
- **对开发者的启示：**  前期用休闲/模拟经营包装降低门槛，中后期再导入SLG核心；小游戏渠道（《三国：冰河时代》累计用户4.3亿，女性超30%）是国内SLG的新增量。PC策略（P社、文明）是另一群高学历、对年龄不敏感的Steam买断用户。 [sohu](https://www.sohu.com/a/1050588155_118576)

### 3.6 休闲：消除 / 益智 / 合成 / 超休闲 / 小游戏

- **人口统计：**
    - 消除类女性约69%（Quantic Foundry 2017，约27万名玩家样本）；《开心消消乐》女性超过七成（QuestMobile 2025）。
    - 微信小游戏用户偏中年：QuestMobile口径为2026年36岁以上占54.7%；2026微信小游戏开发者大会官方口径为24岁以下10%、24–40岁50%、40岁以上40%，女性47%、男性53%。抖音小游戏以棋牌和益智休闲为主（《开运麻将》MAU 5623万，2025年8月）。
    - 46岁以上男性偏好斗地主和掼蛋类（QuestMobile 2025）。 [zhihu](https://zhuanlan.zhihu.com/p/1918322589073375957)
- **动机：**  收集完成、放松、轻挑战；Bartle上偏低对抗、低社交压力。
- **行为：**  一天多次短会话。GameAnalytics显示棋牌、卡牌、益智、博彩类中长期留存最好，街机类D1最好但长线差。 [Substack](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks)
- **付费：**  超休闲靠IAA，生命周期ARPU约0.86美元；消除约2.99美元；派对类约4.90美元（Appodeal 2025）。 [juegostudio](https://www.juegostudio.com/blog/arpdau-benchmarks-by-game-genre)国内小游戏广告收入占比31.89%（2025）。 [sina](https://finance.sina.com.cn/roll/2025-12-19/doc-inhcipum2338201.shtml?froms=ggmp)
- **获客：**  抖音、快手素材加微信社交裂变；休闲CPI为iOS 1.41美元、Android 0.14美元（Liftoff与Singular《2025 Casual Gaming Apps Report》，全球口径，统计期2024年2月至2025年2月）。混合休闲Android CPI从0.54美元涨至0.95美元（Adjust）。 [foxdata](https://foxdata.com/en/blogs/2026-mobile-game-user-acquisition-cost-benchmarks-how-much-should-you-spend/)
- **对开发者的启示：**  小游戏优先做IAA+IAP混合变现，前30秒决定留存；面向中老年要用大字体、低操作、强反馈，面向女性要做装扮、收集和叙事。

### 3.7 模拟经营 / 生活模拟 / 种田 / Cozy（星露谷、动森、模拟人生、桃源深处有人家）

- **人口统计：**  家庭/农场模拟女性约69%，非二元性别玩家比例也最高（Quantic Foundry）；国内女性对模拟经营偏好明显（QuestMobile [gameinformer](https://gameinformer.com/b/news/archive/2017/01/21/study-breaks-down-game-genre-playerbases-by-gender.aspx)[quanticfoundry](https://quanticfoundry.com/2017/01/19/female-gamers-by-genre/) 2025）。日本主机端（动森，日本国内累计802万份）覆盖全年龄。 [donews](https://www.donews.com/news/detail/1/6196437.html) [famitsu](https://www.famitsu.com/article/202508/49165)
- **动机：**  设计（自我表达）、收集完成、放松、幻想；低竞争。
- **行为：**  规律性的每日登录，"情绪陪伴"价值突出（伽马数据把情绪价值列为付费驱动因素）。 [gelonghui](https://m.gelonghui.com/p/1484955)
- **付费：**  手游以装扮/外观加小额IAP和激励广告为主；PC/主机以买断为主。
- **获客：**  小红书、B站、抖音的"治愈"内容；Steam愿望单和Next Fest效果好。
- **对开发者的启示：**  美术风格和"氛围感"就是卖点，适合中小团队做Steam买断，或做小游戏轻度版本。

### 3.8 开放世界 / AAA单机叙事（黑神话：悟空、艾尔登法环、塞尔达、GTA、博德之门3）

- **人口统计：**
    - 《黑神话：悟空》社媒讨论用户中男性约73%，24–29岁约35%，18–23岁和30–39岁各约28%（数说故事社媒监测，并非玩家实测）。 [datastory](https://www.datastory.com.cn/details/1116)
    - 美国主机玩家平均年龄更高（ESA整体平均36–37岁）。 [gamesbeat](https://gamesbeat.com/average-age-of-gamers-hits-37-while-67-of-americans-play-esa-ceo-interview/)[theesa](https://www.theesa.com/annual-esa-study-reveals-video-games-universal-appeal-across-generations/)
- **动机：**  故事、探索、幻想、挑战（魂类）、设计。
- **行为：**  首发集中爆发、长尾衰减；Newzoo统计2021–2024年，2–3月发售的单机比8–11月发售的平均多34%的玩家。 [Substack](https://gamedevreports.substack.com/p/newzoo-the-games-market-in-2025)
- **付费：**  买断加DLC，价格敏感度中等，"文化认同"可显著提高转化。
- **获客：**  预告片、B站和YouTube评测、主播首发直播、Steam愿望单。国内主机市场增速很高（+86.33%）但基数小。 [baidu](https://baike.baidu.com/item/2025%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%B8%B8%E6%88%8F%E4%BA%A7%E4%B8%9A%E6%8A%A5%E5%91%8A/67101368)
- **对开发者的启示：**  本土文化题材有溢价，但必须全球发行才能回本；黑神话之后国内资本对单机更友好，可用PC优先、主机跟进的节奏控制风险。

### 3.9 卡牌 / CCG / 自走棋 / Roguelike构筑（炉石、Marvel Snap、杀戮尖塔、Balatro、三国杀、金铲铲）

- **人口统计：**  国内自走棋以《金铲铲之战》为头部（核心用户数排前五，QuestMobile 2025年12月），用户偏年轻男性（估计）。Roguelike构筑在Steam上以20–35岁的PC核心玩家为主（估计）。 [gamelook](http://www.gamelook.com.cn/2026/03/589129/)
- **动机：**  策略、挑战、收集完成、竞争（排位）。
- **行为：**  单局短（Snap约3分钟，自走棋约30分钟）；GameAnalytics显示卡牌类中长期留存好。 [Substack](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks)
- **付费：**  CCG靠卡包和通行证；自走棋靠外观；Roguelike靠买断（低价、高口碑）。
- **对开发者的启示：**  独立团队可走"低价买断加口碑"（Balatro式），重点是"再来一局"的循环；F2P CCG的门槛高，需要IP加持。

### 3.10 体育 / 竞速（EA Sports FC、NBA 2K、eFootball、Forza、跑跑卡丁车）

- **人口统计：**  体育游戏女性仅约2%，是所有品类中最低（Quantic Foundry）；主机体育游戏2025年全球收入约106亿美元（Newzoo）。 [Substack](https://gamedevreports.substack.com/p/newzoo-the-games-market-in-2025)[quanticfoundry](https://quanticfoundry.com/2017/01/19/female-gamers-by-genre/)
- **动机：**  竞争、收集（球员卡）、刺激。
- **付费：**  年货买断加卡包（Ultimate Team）；Liftoff《2025 Casual Gaming Apps Report》显示体育类iOS D30 ROAS在各品类中最高（80%）。
- **获客：**  依赖官方授权IP，赛季和真实赛事节点带来明显的季节性（世界杯、NBA赛季）。
- **对开发者的启示：**  没有授权很难做；国内可做休闲竞速或卡通体育，面向更广泛的人群。

### 3.11 派对 / 社交 / UGC平台（蛋仔派对、元梦之星、Roblox、Among Us、鹅鸭杀）

- **人口统计：**
    - 《蛋仔派对》全球注册用户超过7亿、月活超过1亿、UGC开发者超过5000万（2026年创作者大会）。 [zgeo](https://www.zgeo.com.cn/news/netease-eggy-party-ai-ugc-platform-deepseek)[firecat-web](https://www.firecat-web.com/daily-news/12139)早期抖音画像女性约60–65%（2023年行业媒体观测）。 [yfchuhai](https://www.yfchuhai.com/article/10848.html)
    - 《鹅鸭杀》手游以35岁以下男性为主（QuestMobile 2026）。 [qq](https://news.qq.com/rain/a/20260721A0573A00)
    - Roblox：2025年Q2 DAU 1.118亿，13岁以上占64%；完成年龄验证的用户中，13岁以下35%、13–17岁38%、18岁以上27%，18岁以上增长最快（Roblox官方，2026）。 [shanethegamer](https://www.shanethegamer.com/research/roblox-player-count/)[shanethegamer](https://www.shanethegamer.com/research/roblox-statistics/)
- **动机：**  社区、设计（创作）、探索、轻竞争。
- **付费：**  外观加创作者分成（蛋仔年度激励分成超过2亿元）； [zgeo +2](https://www.zgeo.com.cn/news/netease-eggy-party-ai-ugc-platform-deepseek)Roblox靠虚拟货币。
- **获客：**  短视频二创、主播、学生社交链；寒暑假季节性明显。 [sohu](https://m.sohu.com/a/1056102436_122588926/?pvid=000115_3w_a)
- **对开发者的启示：**  平台头部已锁定，中小团队的机会在于成为平台上的创作者，或做小型联机社交推理游戏（Steam/小游戏）；未成年人合规是必修课。

### 3.12 沙盒 / 生存 / 建造（我的世界、幻兽帕鲁、Rust、ARK）

- **人口统计：**  我的世界覆盖儿童到青年；Rust/ARK以18–35岁男性PC玩家为主（估计）。幻兽帕鲁在2024年对PC端增长贡献显著（Newzoo）。 [glodomtec](https://www.glodomtec.com/en/News/info.aspx?itemid=2221)
- **动机：**  探索、设计、社区（服务器）、挑战（生存）。
- **付费：**  PC买断加DLC；国内版我的世界采用F2P加资源市场。
- **对开发者的启示：**  合作生存和"缝合创新"在Steam成功率较高；服务器社区运营决定长线表现。

### 3.13 放置 / 节奏音游 / 格斗（简述）

- **放置：**  偏25–40岁上班族（估计），动机为力量养成和收集，会话极短。业内引用的全球混合口径CPI中，放置RPG约3.19美元，属于偏贵品类（Segwise转述）。 [segwise](https://segwise.ai/blog/cpi-ipm-roas-benchmarks-optimizing-ad-spend)
- **节奏音游：**  二次元重叠度高，偏学生，女性比例高于动作游戏（估计）。
- **格斗：**  Tekken官方公布女性约23%（Quantic Foundry引用）， [quanticfoundry](https://quanticfoundry.com/2017/01/19/female-gamers-by-genre/)核心玩家年龄偏大、竞争动机强、社区以赛事为中心。
- **附：恐怖游戏** 偏年轻、靠主播效应传播；**乙游/女性向** 以《恋与深空》为头部（活跃率64.8%），据《女性向游戏调研报告》（2025年12月），61.3%的受访玩家为单身，多为学生和职员，情绪价值驱动付费；**银发玩家** 集中在棋牌、消除、微信小游戏（46岁以上男性偏好掼蛋/斗地主），ESA 2025显示美国近一半婴儿潮一代每周玩游戏。 [theesa](https://www.theesa.com/annual-esa-study-reveals-video-games-universal-appeal-across-generations/)

---

## 四、分品类总对比矩阵

| 品类 | 核心年龄 | 性别（男:女） | 主平台 | 会话时长 | 留存特征 | 付费率 | ARPPU | 主要变现 | 核心动机 | 最佳获客渠道 | 中外关键差异 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MOBA | 16–30 | 国内手游约1:1；PC端LoL约86:14 | 手游/PC | 15–20分钟/局 | 长线强（社交链） | 高 | 中 | 皮肤/通行证 | 竞争、社区 | 社交链、电竞 | 中国/东南亚手游化且均衡，欧美PC化且男性为主 |
| 射击/大逃杀 | 16–35 | 硬核7:3以上；全民向较均衡 | PC/手游/主机 | 20–40分钟 | 中高 | 中高 | 中 | 皮肤/通行证/交易 | 竞争、刺激 | 直播、短视频 | 国内搜打撤爆发；欧美主机COD/Fortnite |
| MMO/ARPG | 25–40 | 约7:3（奇幻MMO女性约36%） | 端游/手游 | 60分钟以上 | 中长 | 中 | 高 | 数值→外观转型 | 力量、社区 | 买量、IP | 韩国MMO+PC房文化；欧美ARPG买断+赛季 |
| 二次元 | 16–28 | 约63:37（中国核心）；日本约6:4 | 手游/PC | 20–40分钟 | 版本脉冲 | 高 | 很高 | 抽卡 | 故事、收集、幻想 | B站、TapTap、KOL | 日本付费意愿最高；国内赛道收缩 |
| SLG/4X | 26–45 | 约85–88:12–15（休闲SLG女性可超30%） | 手游/小游戏 | 多次碎片 | 赛季型 | 低到中 | 极高（大R） | VIP/数值/礼包 | 策略、力量 | 副玩法买量、小游戏 | 海外休闲SLG领跑；国内三国题材主导 |
| 消除/益智/小游戏 | 30–55 | 约30:70（消除） | 手游/小游戏 | 3–10分钟×多次 | 长线稳 | 低 | 低到中 | IAA+IAP | 收集完成、放松 | 抖音、微信裂变 | 国内小游戏偏中年；欧美Royal Match靠IAP |
| 模拟经营/Cozy | 20–40 | 约30:70 | 手游/PC/Switch | 中短 | 稳 | 中 | 中 | 外观/买断 | 设计、完成 | 小红书、Steam | 日本Switch全年龄；国内手游化 |
| AAA单机 | 18–39 | 约73:27（黑神话社媒） | PC/主机 | 长 | 首发脉冲 | 买断 | 一次性 | 买断+DLC | 故事、探索、挑战 | 预告片、主播、愿望单 | 国内主机小但增速最快 |
| 卡牌/自走棋/Roguelike | 18–35 | 偏男 | 手游/PC | 3–30分钟 | 好 | 中 | 中 | 卡包/外观/买断 | 策略、挑战 | 主播、Steam口碑 | 国内自走棋手游化；海外独立买断 |
| 体育/竞速 | 18–40 | 约98:2（体育） | 主机/手游 | 中 | 赛季型 | 中高 | 高 | 买断+卡包 | 竞争、收集 | IP、赛事节点 | 欧美主机年货；国内授权受限 |
| 派对/UGC | 8–25 | 偏女或均衡 | 手游/PC | 短到中 | 依赖内容供给 | 中 | 低到中 | 外观+创作者分成 | 社区、设计 | 短视频、学生链 | Roblox低龄化正逐步老化；蛋仔偏女性 |
| 沙盒/生存 | 10–35 | 偏男 | PC/全平台 | 长 | 依赖服务器 | 买断为主 | 中 | 买断/资源市场 | 探索、设计 | Steam、主播 | 国内MC为F2P运营 |

> 年龄和性别栏中，未标出处的数字均为基于上文来源的估计区间；留存、付费率和ARPPU是相对档位，不是统计值。

**通用留存基准（GameAnalytics 2025，移动端，全品类）：**

| 分位 | D1 | D7 | D28/D30 |
| --- | --- | --- | --- |
| 中位数P50 | 约22% | 略低于4% | 约0.7–0.8% [gameanalytics](https://www.gameanalytics.com/reports/2026-mobile-pc-gaming-benchmarks) |
| 前25% | 25–27%（Android）/31–33%（iOS） | 7–8% | 3%左右 [digitalmindsbpo](https://digitalmindsbpo.com/blog/mobile-game-retention-benchmarks/)[Substack](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks) |
| 前10% | 约40% | 11–12% | — |
| 前1% | 64–68% | >25% | 13–15% [gameanalytics](https://www.gameanalytics.com/reports/2026-mobile-pc-gaming-benchmarks) |

- **PC端：**  D1整体低于移动端，前25%约15–16%。 [Substack](https://gamedevreports.substack.com/p/gameanalytics-mobile-and-pc-game)
- **地区差异：**  D7中位数北美4.97%，亚洲2.68%。 [investgame](https://investgame.net/wp-content/uploads/2026/01/2026-01-27-2026-mobile-pc-benchmarks_compressed.pdf)
- **口径冲突：**  Sensor Tower口径的中重度产品为D1 44–45%、D30 11–12%（二手转述），明显高于上表，原因是它统计的是已规模化的头部产品，存在幸存者偏差。立项时，建议把GameAnalytics的P75–P90当作"可上线"门槛。 [appagent](https://appagent.com/blog/mobile-game-retention-benchmarks/)

**CPI参考（美国为主）：**

| 品类 | iOS | Android | 来源 |
| --- | --- | --- | --- |
| 休闲（整体） | 1.41美元 | 0.14美元 | Liftoff 2025（全球口径，2024.2–2025.2） |
| 益智 | 约3.00美元 | 约2.00美元 | Business of Apps |
| 策略 | 约5.50美元 | 约4.00美元 | Business of Apps |
| RPG | 约6.00美元 | 约4.50美元 | Business of Apps |
| 博彩 | 21.03美元 | — | Liftoff 2025 |

- **地区CPI（Business of Apps 2024，经Udonis转引）：**  北美iOS 5.28美元/Android 5.00美元，EMEA iOS 1.03美元/Android 0.98美元，亚太iOS 0.93美元/Android 0.83美元，拉美iOS 0.34美元/Android 0.32美元。
- **预算分布：**  AppsFlyer称2025年约50%的UA预算投向美国。 [maf](https://maf.ad/en/blog/the-cost-of-user-acquisition/)
- **国内：**  公开的CPA/CPI数据多以DataEye、AppGrowing的素材量形式出现，单价数据很少公开；建议直接用小额测试获取。

---

## 五、地区差异：同一品类，不同的人

- **中国：**
    - 未成年人防沉迷（仅限周五、六、日及法定节假日20–21点）压低了未成年人的活跃度，使APP端画像向18–35岁集中。
    - 版号常态化（2026年上半年批了917个，同比+21.1%）带来新品供给回升。 [36kr](https://36kr.com/p/3904748532450950)
    - 微信/抖音小游戏的生态独一无二，造就了中年和下沉的IAA人群。
    - 女性向和二次元的内容消费强，但二次元赛道在收缩。
- **美国/欧洲：**  玩家平均年龄36–41岁，性别接近对半； [theesa](https://www.theesa.com/annual-esa-study-reveals-video-games-universal-appeal-across-generations/)[techspot](https://www.techspot.com/news/109812-esa-report-shows-average-gamer-41-ndash-nearly.html)主机和PC买断与F2P并存；获客靠Meta/Google/TikTok加Steam；用户付费意愿高，CPI也最高。
- **日本：**  主机强（Switch系）、gacha文化成熟、二次元付费意愿全球最高；2025年游戏人口回升到5639万，移动端反而下滑。 [famitsu](https://www.famitsu.com/article/202608/83758)
- **韩国：**  游戏使用率连续下降（2025年为50.2%）且人群老化，60代只有23.1%；PC在回升（58.1%）， [daum](https://v.daum.net/v/20251218134801865)[gamegeneration](https://www.gamegeneration.or.kr/article/045a8130-7f48-467e-8fdf-3d9c7f8aff47)PC房以社交为核心； [ilovepcbang](https://www.ilovepcbang.com/news/articleView.html?idxno=111967)MMO和数值付费传统深厚。
- **东南亚：**  移动优先、低ARPU（年均约18.8美元）、MOBA和射击主导、直播观看率高，电子钱包和第三方支付占比上升。 [nikopartners](https://nikopartners.com/sea-of-opportunities-exploring-the-rise-of-southeast-asia-video-games-market/)适合用量大、低价、电竞化的产品切入。
- **拉美/中东：**  拉美玩家增速全球最快（Newzoo +5.3%）， [icon-era](https://icon-era.com/statistics/video-game-statistics/)CPI最低；中东D1/D7留存最高（GameAnalytics 2024：D1 22.64%、D7 4.91%）， [Substack](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks)付费能力强。

---

## 六、2024–2026年正在重塑画像的趋势

1. **多端互通：**  产业报告把"多端互通"列为2025年用户增长原因之一，客户端收入因此增长14.97%。同一个玩家在手机、PC、主机之间切换已成为常态。 [xinhuanet](http://www.xinhuanet.com/20251219/71b9f7db89c84eee968cddeeeb86baf1/c.html)[oeeee](https://m.mp.oeeee.com/a/BAAFRD0000202512191496303.html)
2. **小游戏和混合变现：**  小游戏人群向高线城市和中重度品类延伸（SLG、塔防），IAA+IAP成为默认配置。 [gamelook](http://www.gamelook.com.cn/2026/03/589129/)[36kr](https://36kr.com/p/3904748532450950)
3. **女性向和情绪价值：**  女性向市场翻倍增长，但高度集中。2025年《恋与深空》约占iOS女性向收入的一半（第三方估算）。 [zhihu](https://zhuanlan.zhihu.com/p/1997962293305157577)
4. **国产单机复兴：**  主机收入连续三年高速增长，黑神话带来大量"首次购买主机/3A的玩家"（定性判断）。 [baidu](https://baike.baidu.com/item/2025%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%B8%B8%E6%88%8F%E4%BA%A7%E4%B8%9A%E6%8A%A5%E5%91%8A/67101368)
5. **玩家老化：**  美国平均年龄从36岁升至37岁，韩国60代使用率低、10代高；中国的增量来自36岁以上的小游戏用户。 [gamesbeat](https://gamesbeat.com/average-age-of-gamers-hits-37-while-67-of-americans-play-esa-ceo-interview/)[theesa](https://www.theesa.com/annual-esa-study-reveals-video-games-universal-appeal-across-generations/) [gamegeneration](https://www.gamegeneration.or.kr/article/045a8130-7f48-467e-8fdf-3d9c7f8aff47)
6. **Alpha世代和UGC：**  Roblox 18岁以上群体增长最快，平台在"长大"；蛋仔等国内UGC平台建立了创作者经济。 [shanethegamer](https://www.shanethegamer.com/research/roblox-statistics/) [firecat-web](https://www.firecat-web.com/daily-news/12139)
7. **AI内容：**  蛋仔派对接入大模型辅助UGC创作；Quantic [zgeo](https://www.zgeo.com.cn/news/netease-eggy-party-ai-ugc-platform-deepseek)[firecat-web](https://www.firecat-web.com/daily-news/12139) Foundry调研显示，玩家整体对生成式AI态度负面，而且态度随性别、年龄、动机不同而差异明显。宣传时要谨慎。 [quanticfoundry](https://quanticfoundry.com/2024/05/21/strategy-decline/)
8. **短视频驱动发现：**  "副玩法素材"（Last War）和抖音小游戏"内容种草→即点即玩"的闭环，正在重塑获客方式。 [jiemian](https://www.jiemian.com/article/12347420.html)[36kr](https://36kr.com/p/3518304729176969)
9. **订阅和掌机：**  Game Pass和Steam Deck扩大了PC/主机的轻度游玩场景，在国内影响有限（数据稀缺）。

---

## 七、方法论说明与数据局限

- **遥测数据：**  QuestMobile（APP和小程序的监测样本）、GameAnalytics（11,600款接入其SDK的游戏，偏中小开发者）、 [Substack](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks)Sensor Tower/AppMagic（估算值）。
- **调研数据：**  ESA（YouGov，5,000人，加权）、ESA Power of Play（24,216人）、KOCCA（约1万人）、Quantic Foundry（自选样本，偏核心玩家，女性仅18.5%，部分数据为2016–2017年）、 [quanticfoundry +2](https://quanticfoundry.com/2017/01/19/female-gamers-by-genre/)伽马数据用户调研。
- **社媒监测数据：**  黑神话的画像来自社媒讨论者，不等于实际购买者。 [digitaling](https://www.digitaling.com/articles/1255330.html)
- **陈旧数据：**  王者荣耀的极光数据（2017年）和腾讯广告SLG白皮书（2022年）较早，只作方向参考。
- **数据空白：**  国内主机玩家画像、国内分品类CPI、公开的分品类D1/D7都缺乏权威统计；本报告矩阵中的相关栏目为估计档位。
- **数据冲突：**  Newzoo 2025全球收入有188.8亿美元和约1970亿美元两个版本（年中上调）； [gamesmarket](https://www.gamesmarket.global/newzoo-report-global-gaming-revenue-is-expected-to-reach-dollar1888-billion-in-2025-with-growth-set-to-continue-f4d9c4b86e8410e860dcca74905b3197/)[g-mnews](https://g-mnews.com/en/global-games-market-to-reach-usd-197-billion-in-2025-exceeding-previous-forecasts/)东南亚移动端占比Niko为66.4%、Newzoo为73%； [pocketgamer](https://www.pocketgamer.biz/the-state-of-southeast-asias-games-industry-in-2025/)[Substack](https://gamedevreports.substack.com/p/niko-partners-the-6-largest-gaming)女性占比ESA为47%、Quantic Foundry为18.5%（样本差异）。 [quanticfoundry](https://quanticfoundry.com/2017/01/19/female-gamers-by-genre/)[theesa](https://www.theesa.com/annual-esa-study-reveals-video-games-universal-appeal-across-generations/)本报告均列出区间并说明原因。

---

## 八、建议的下一步（验证你自己项目的画像）

1. **先写"反画像"：**  明确不服务谁（如"不服务追求PvP排位的玩家"），倒推玩法边界。
2. **动机验证：**  让测试玩家完成Quantic Foundry Gamer Motivation Profile（免费、约5分钟），对照目标品类的动机分布，看核心循环是否匹配。 [quanticfoundry](https://quanticfoundry.com/2017/01/19/female-gamers-by-genre/)
3. **国内预约测试：**  在TapTap、B站、好游快爆开预约页，用不同美术和卖点做A/B，统计预约转化和评论关键词；同步在小红书、抖音做素材冷启动。
4. **Steam验证：**  商店页上线后积累愿望单，参加Steam Next Fest并观察Demo游玩时长；用GameDiscoverCo等公开数据对照同类产品的愿望单转化。
5. **买量CPI测试：**  每个市场、每套素材先投1–3千美元（或等值人民币），测CPI、IPM和D1；SLG/RPG同时测"副玩法素材"与"真实玩法素材"的人群差异和D7付费。
6. **小游戏双轨：**  有条件的话，先用微信/抖音小游戏版本验证IAA留存和中年人群反应，再决定是否做APP版本。
7. **埋点基线：**  接入GameAnalytics或数数科技（ThinkingData）等工具，以P75作为及格线、P90作为放量线，按地区和平台拆分对标。
8. **出海选址：**  按画像匹配市场。二次元优先日本，休闲SLG优先美国、日本、韩国，MOBA/射击优先东南亚和拉美，Cozy/买断优先Steam全球。