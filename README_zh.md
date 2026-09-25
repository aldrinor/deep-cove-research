<!-- 由 data/deep-cove-research.jsonl 生成；请勿手动编辑。 -->

<h1 align="center">deep-cove-research</h1>

<p align="center">
  专有深度研究系统。<br>
  本仓库发布其在 DeepResearch Bench 上的全部 100 篇报告（由 GPT-5.6 Luna 以最高推理设置撰写）。
</p>

<p align="center">
  <a href="https://github.com/Ayanami0730/deep_research_bench"><img src="assets/badges/benchmark.svg" height="20" alt="基准：DeepResearch Bench，100 个任务"></a>
  <a href="reports/README.md"><img src="assets/badges/reports.svg" height="20" alt="报告：中文 50 篇、英文 50 篇"></a>
  <a href="LICENSE"><img src="assets/badges/license.svg" height="20" alt="许可：专有"></a>
</p>

<p align="center">
  <a href="#reports">报告</a> · <a href="#how-it-works">工作流程</a> · <a href="#data">数据</a> · <a href="#reproducing-the-evaluation">复现评测</a> · <a href="#citation">引用</a>
  &nbsp;|&nbsp; <a href="README.md">English</a> · <b>中文</b>
</p>

## <a name="reports"></a>报告

每篇报告都有独立页面：基准题目，以及与提交内容完全一致的报告原文。

**[浏览全部 100 篇报告 →](reports/README.md)**

<details>
<summary>按任务编号跳转到报告</summary>

<table>
  <tr><th rowspan="5">中文</th><td align="center"><a href="reports/zh/001.md">001</a></td><td align="center"><a href="reports/zh/002.md">002</a></td><td align="center"><a href="reports/zh/003.md">003</a></td><td align="center"><a href="reports/zh/004.md">004</a></td><td align="center"><a href="reports/zh/005.md">005</a></td><td align="center"><a href="reports/zh/006.md">006</a></td><td align="center"><a href="reports/zh/007.md">007</a></td><td align="center"><a href="reports/zh/008.md">008</a></td><td align="center"><a href="reports/zh/009.md">009</a></td><td align="center"><a href="reports/zh/010.md">010</a></td></tr>
  <tr><td align="center"><a href="reports/zh/011.md">011</a></td><td align="center"><a href="reports/zh/012.md">012</a></td><td align="center"><a href="reports/zh/013.md">013</a></td><td align="center"><a href="reports/zh/014.md">014</a></td><td align="center"><a href="reports/zh/015.md">015</a></td><td align="center"><a href="reports/zh/016.md">016</a></td><td align="center"><a href="reports/zh/017.md">017</a></td><td align="center"><a href="reports/zh/018.md">018</a></td><td align="center"><a href="reports/zh/019.md">019</a></td><td align="center"><a href="reports/zh/020.md">020</a></td></tr>
  <tr><td align="center"><a href="reports/zh/021.md">021</a></td><td align="center"><a href="reports/zh/022.md">022</a></td><td align="center"><a href="reports/zh/023.md">023</a></td><td align="center"><a href="reports/zh/024.md">024</a></td><td align="center"><a href="reports/zh/025.md">025</a></td><td align="center"><a href="reports/zh/026.md">026</a></td><td align="center"><a href="reports/zh/027.md">027</a></td><td align="center"><a href="reports/zh/028.md">028</a></td><td align="center"><a href="reports/zh/029.md">029</a></td><td align="center"><a href="reports/zh/030.md">030</a></td></tr>
  <tr><td align="center"><a href="reports/zh/031.md">031</a></td><td align="center"><a href="reports/zh/032.md">032</a></td><td align="center"><a href="reports/zh/033.md">033</a></td><td align="center"><a href="reports/zh/034.md">034</a></td><td align="center"><a href="reports/zh/035.md">035</a></td><td align="center"><a href="reports/zh/036.md">036</a></td><td align="center"><a href="reports/zh/037.md">037</a></td><td align="center"><a href="reports/zh/038.md">038</a></td><td align="center"><a href="reports/zh/039.md">039</a></td><td align="center"><a href="reports/zh/040.md">040</a></td></tr>
  <tr><td align="center"><a href="reports/zh/041.md">041</a></td><td align="center"><a href="reports/zh/042.md">042</a></td><td align="center"><a href="reports/zh/043.md">043</a></td><td align="center"><a href="reports/zh/044.md">044</a></td><td align="center"><a href="reports/zh/045.md">045</a></td><td align="center"><a href="reports/zh/046.md">046</a></td><td align="center"><a href="reports/zh/047.md">047</a></td><td align="center"><a href="reports/zh/048.md">048</a></td><td align="center"><a href="reports/zh/049.md">049</a></td><td align="center"><a href="reports/zh/050.md">050</a></td></tr>
  <tr><th rowspan="5">英文</th><td align="center"><a href="reports/en/051.md">051</a></td><td align="center"><a href="reports/en/052.md">052</a></td><td align="center"><a href="reports/en/053.md">053</a></td><td align="center"><a href="reports/en/054.md">054</a></td><td align="center"><a href="reports/en/055.md">055</a></td><td align="center"><a href="reports/en/056.md">056</a></td><td align="center"><a href="reports/en/057.md">057</a></td><td align="center"><a href="reports/en/058.md">058</a></td><td align="center"><a href="reports/en/059.md">059</a></td><td align="center"><a href="reports/en/060.md">060</a></td></tr>
  <tr><td align="center"><a href="reports/en/061.md">061</a></td><td align="center"><a href="reports/en/062.md">062</a></td><td align="center"><a href="reports/en/063.md">063</a></td><td align="center"><a href="reports/en/064.md">064</a></td><td align="center"><a href="reports/en/065.md">065</a></td><td align="center"><a href="reports/en/066.md">066</a></td><td align="center"><a href="reports/en/067.md">067</a></td><td align="center"><a href="reports/en/068.md">068</a></td><td align="center"><a href="reports/en/069.md">069</a></td><td align="center"><a href="reports/en/070.md">070</a></td></tr>
  <tr><td align="center"><a href="reports/en/071.md">071</a></td><td align="center"><a href="reports/en/072.md">072</a></td><td align="center"><a href="reports/en/073.md">073</a></td><td align="center"><a href="reports/en/074.md">074</a></td><td align="center"><a href="reports/en/075.md">075</a></td><td align="center"><a href="reports/en/076.md">076</a></td><td align="center"><a href="reports/en/077.md">077</a></td><td align="center"><a href="reports/en/078.md">078</a></td><td align="center"><a href="reports/en/079.md">079</a></td><td align="center"><a href="reports/en/080.md">080</a></td></tr>
  <tr><td align="center"><a href="reports/en/081.md">081</a></td><td align="center"><a href="reports/en/082.md">082</a></td><td align="center"><a href="reports/en/083.md">083</a></td><td align="center"><a href="reports/en/084.md">084</a></td><td align="center"><a href="reports/en/085.md">085</a></td><td align="center"><a href="reports/en/086.md">086</a></td><td align="center"><a href="reports/en/087.md">087</a></td><td align="center"><a href="reports/en/088.md">088</a></td><td align="center"><a href="reports/en/089.md">089</a></td><td align="center"><a href="reports/en/090.md">090</a></td></tr>
  <tr><td align="center"><a href="reports/en/091.md">091</a></td><td align="center"><a href="reports/en/092.md">092</a></td><td align="center"><a href="reports/en/093.md">093</a></td><td align="center"><a href="reports/en/094.md">094</a></td><td align="center"><a href="reports/en/095.md">095</a></td><td align="center"><a href="reports/en/096.md">096</a></td><td align="center"><a href="reports/en/097.md">097</a></td><td align="center"><a href="reports/en/098.md">098</a></td><td align="center"><a href="reports/en/099.md">099</a></td><td align="center"><a href="reports/en/100.md">100</a></td></tr>
</table>

</details>

**节选**：任务 [016](reports/zh/016.md) 的报告

> 截至2026年9月13日，非接触式感知不存在跨任务通用的“最高准确率算法”。如果按任务分别判断：面部视频生命体征以 PhysNeXt、FreqPhys、physFSUNet 等双流、频域约束或差分帧融合模型最具竞争力；Wi-Fi 手势识别以 Wi-CBR 在 Widar3.0 上的跨位置、跨方向和跨环境结果最完整；毫米波生命体征则以具备空间分离和抗杂波能力的多主体 FMCW-MIMO 框架更适合真实共享空间。热成像姿态、LiDAR 动作识别和多模态缺失输入，分别由 YOLO11-pose、LiDAR 图谱方法以及 PTA、X-Fi、FlexPose 等代表。

## <a name="how-it-works"></a>工作流程

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/pipeline-zh-dark.svg">
    <img src="assets/pipeline-zh-light.svg" width="100%" alt="从左到右六个阶段：规划、检索、阅读、提取、覆盖检查、撰写。撰写阶段使用 GPT-5.6 Luna 的最高推理设置。">
  </picture>
</p>

<sub>**图 1.** deep-cove-research 处理每个问题的六个阶段。</sub>

对于每个问题，deep-cove-research 会：

1. 规划研究：明确需要回答什么，以及报告应如何组织；
2. 检索开放网络与学术文献；
3. 阅读所选来源的全文；
4. 从中提取带引用的发现；
5. 对照问题的要求检查覆盖情况；
6. 撰写长篇报告。

报告由 **GPT-5.6 Luna** 以最高推理设置撰写。

## <a name="report-statistics"></a>报告统计

| | 中文（001–050） | 英文（051–100） | 全部 100 篇 |
|:--|--:|--:|--:|
| 长度中位数（字符） | 29,832.5 | 91,564 | 50,479 |
| 最短 – 最长（字符） | 12,558 – 48,775 | 52,183 – 124,994 | 12,558 – 124,994 |
| 长度中位数（英文词数） | – | 12,238 | – |
| 每篇来源链接数中位数 | 58 | 61 | 58.5 |
| 每篇不同来源数中位数 | 38.5 | 43 | 41 |
| 全部报告的不同来源网址 | 1,935 | 2,078 | 4,007 |
| 章节数中位数（二级标题） | 8 | 9 | 8.5 |
| 含表格的报告 | 50 / 50 | 50 / 50 | 100 / 100 |

字符数为报告文本的 Unicode 字符数；词数按空白分隔计数，仅统计英文报告。来源链接为报告正文中链接或嵌入的网址，按出现次数计；不同来源数为单篇报告中不重复网址的数量。“全部报告的不同来源网址”按列去重；有 6 个网址同时出现在中文与英文报告中，因此“全部”一列小于两种语言之和。

## <a name="data"></a>数据

```text
deep-cove-research/
├── README.md                      概览（英文）
├── README_zh.md                   概览（中文）
├── data/
│   ├── README.md                  字段说明
│   └── deep-cove-research.jsonl   提交的 100 篇报告，官方格式
├── reports/
│   ├── README.md                  全部 100 篇报告的索引
│   ├── zh/001.md … 050.md         中文报告，每篇一页
│   └── en/051.md … 100.md         英文报告，每篇一页
├── assets/                        徽章与图（SVG）
├── CITATION.cff                   引用信息
└── LICENSE                        条款（专有）
```

- [`data/deep-cove-research.jsonl`](data/deep-cove-research.jsonl)：共 100 行，每行一个 JSON 对象（UTF-8），采用 DeepResearch Bench 官方格式，字段为 `id`、`prompt` 和 `article`。任务 1–50 为中文，51–100 为英文。文件大小 8,010,129 字节；SHA-256 `2578948bbb4555c30c3dc9c1bc245a59e2c1575f0c2a8fd5c3f7c3ccad3c12e3`。字段说明见 [data/README.md](data/README.md)。
- [`reports/`](reports/README.md) 中的每个页面都逐字节包含对应报告的 `article` 文本，并注明该文本的 SHA-256。

## <a name="reproducing-the-evaluation"></a>复现评测

1. 从 [DeepResearch Bench 仓库](https://github.com/Ayanami0730/deep_research_bench) 获取官方评测代码，并切换到提交 `852f4022`。
2. 将本仓库的 `data/deep-cove-research.jsonl` 复制到该代码目录下，路径为 `data/test_data/raw_data/deep-cove-research.jsonl`。
3. 在 `run_benchmark.sh` 的 `TARGET_MODELS` 中加入 `deep-cove-research`。
4. 按基准 README 的说明配置评测模型的访问，并保持默认评测设置。
5. 运行 `run_benchmark.sh`。RACE 汇总结果写入 `results/race/deep-cove-research/race_result.txt`。

## <a name="citation"></a>引用

如引用这些报告，请同时引用本仓库与 DeepResearch Bench 论文。

**本仓库**

```bibtex
@misc{deepcoveresearch2026,
  title = {deep-cove-research: DeepResearch Bench Reports},
  author = {{deep-cove-research}},
  year = {2026},
  howpublished = {\url{https://github.com/aldrinor/deep-cove-research}},
  note = {100 reports (50 Chinese, 50 English)},
}
```

**DeepResearch Bench**

```bibtex
@inproceedings{ICLR2026_465f22be,
  author = {Du, Mingxuan and Xu, Benfeng and Zhu, Chiwei and Zhang, Licheng and Wang, Xiaorui and Mao, Zhendong},
  booktitle = {International Conference on Learning Representations},
  editor = {C. Vondrick and B. Hariharan and C. Raffel and L. Pinto and D. Yang and A. Faust},
  pages = {42414--42448},
  title = {DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents},
  url = {https://proceedings.iclr.cc/paper_files/paper/2026/file/465f22be10e07b301c6ed58f0472f704-Paper-Conference.pdf},
  volume = {2026},
  year = {2026},
}
```

## <a name="license"></a>许可

专有。本仓库中的报告 © 2026 deep-cove-research，保留所有权利；详见 [LICENSE](LICENSE)。报告页面与 `prompt` 字段中的基准题目属于 DeepResearch Bench，归其作者所有。

## <a name="contact"></a>联系方式

aor@cpolartechnologies.com

## <a name="acknowledgements"></a>致谢

感谢 DeepResearch Bench 团队（Mingxuan Du、Benfeng Xu、Chiwei Zhu、Licheng Zhang、Xiaorui Wang、Zhendong Mao）提供基准、官方评测代码与排行榜。
