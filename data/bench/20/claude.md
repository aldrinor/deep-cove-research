# MCP Streamable HTTP **工程实现方案研究报告(截至** 2026 **年** 9 **月)** 

截至 2026 年 9 月 24 日,Streamable HTTP 最新的规范性版本是 MCP 规范 2026-07-28 修订版(2026 年 7 月 28 日正式发布)。这一版把 GitHub Modelcontextproto... Streamable HTTP 从“有状态、双向、可恢复的 SSE 通道”重构为“无状态、逐请求自描述的 POST 通道”: `Mcp-Session-Id` 、独立 GET 流、服务器主动发请求和 `Last-Event-ID` 断点续传都已删除,改由 `_meta` 逐请求元数据、 `Mcp-Method` / `Mcp-Name` 路由头、MRTR(多轮往返请求)和 `subscriptions/listen` 取代。需要先说明:这不是 Niteagent +2 Anthropic 单独发布的东⻄。MCP 已于 2025 年 12 月 9 日捐赠给 Linux 基金会旗下的 Agentic AI Foundation(AAIF),2026-07-28 版由 MCP 项目维护者发布;Anthropic 这边与之最相关的是 Claude API 的 MCP connector(当前 beta 头为 `mcp-client-2025-11-20` ,另有 `mcp-client-2026-09-15` )。 claude Modelcontextproto... 

## TL;DR 

- **规范层** :Streamable HTTP 由 PR #206 在 2025-03-26 版引入,用来替代 HTTP+SSE。之后几版的主要变化:202506-18 删除 JSON-RPC batching,并强制 `MCP-Protocol-Version` 头;2025-11-25 加入 SSE priming 事件和服务器主动断开后的轮询(SEP-1699);2026-07-28 删除会话、GET 流和可恢复性,改为无状态设计(SEP2567/2575/2322/2243)。新项目应直接以 2026-07-28 为目标,同时保留对 2025 年各版客户端的兼容回退。 

- **实现层** :TypeScript SDK v1 的 `StreamableHTTPServerTransport` 靠 `_streamMapping` 、 `_requestToStreamMapping` 和 `EventStore` 实现流路由与断点续传。v2 的 `createMcpHandler(factory)` 改为逐请求构造服务器,默认 <mark>`legacy:`</mark> 

- <mark>`'stateless'` ,</mark> 同一端点可服务两个协议时代的客户端。Python SDK v2.0.0(2026-07-28)用 `MCPServer` 取代 

- FastMCP,同一个端点自动服务两个时代;v1 的 `StreamableHTTPSessionManager` 依然是旧协议客户端的核心。 

- **工程结论** :新服务一律按“每个请求新建 server + transport、无会话、round-robin 负载均衡”部署,跨调用状态放在显式句柄和外部存储里。TypeScript SDK 必须 ≥1.26.0,以修复 CVE-2026-25536 跨客户端数据泄漏;本地服务器必须启用 Host/Origin 校验,参⻅ CVE-2025-66414。SSE 链路要设置 `X-Accel-Buffering: no` 并发送 keep-alive 注释 行。 

## 1. **摘要** 

本报告从五个层面分析 MCP Streamable HTTP 传输:规范性文本、官方 SDK 源码与文档、官方公告、SEP 与 GitHub 设计讨论、第三方评论。行文中按这五类区分来源。主要结论如下。 

第一,时效上,“最新发布”对应 MCP 2026-07-28 规范。它的发布候选版(RC)于 2026 年 5 月 21 日锁定,给 SDK 维护者十 周验证窗口,正式版于 7 月 28 日发布。 Obot AI Modelcontextproto... MCP 官方博客称这一版是“the largest revision of the protocol since launch”。 Modelcontextproto...发布当天,四个 Tier 1 SDK(TypeScript、Python、Go、C#)都已支持,Rust SDK 以 beta 形式支持。 modelcontextproto... 

第二,设计上,Streamable HTTP 经历了两代。第一代(2025-03-26 至 2025-11-25)是“单端点 + 可选 SSE 升级 + 可选会话 + 可恢复流”:解决了 HTTP+SSE 双端点、必须⻓连接、不可恢复的问题,但有状态会话与负载均衡器的矛盾仍在。第二代(2026-07-28)从协议层彻底去掉状态,每个请求都能落在任意实例上。 Mcp Modelcontextproto... 

第三,实现上,官方 SDK 普遍采用“双时代并存”策略:同一 HTTP 端点先识别请求属于 2026 年的逐请求 `_meta` 模式还是 2025 年的 `initialize` 握手模式,再分派给不同处理器。v1 GitHub +3 时代的实现细节(流映射表、EventStore、会话表)在服务旧客户端时仍有意义,所以本报告对两代实现都做了分析。 

第四,安全上,已知的两个 SDK 级漏洞都直接与 Streamable HTTP 实现有关:DNS rebinding 防护默认关闭(CVE-202566414),以及共享 transport 实例导致 JSON-RPC ID 冲突、响应串到别的客户端(CVE-2026-25536)。 nist GitHub 后者恰好说明“有状态流映射”这种设计在无状态部署下有多脆弱,也从侧面佐证了 2026-07-28 版的方向。 

## 2. **背景与动机:为什么** HTTP+SSE **被替换** 

### 2.1 HTTP+SSE **(** 2024-11-05 **)的结构性问题** 

2024-11-05 版的 HTTP+SSE 传输需要两个端点:客户端先 GET 一个 SSE 端点,建立持久连接,服务器在第一个 `endpoint` 事件里告诉客户端 POST 消息该发到哪里;之后所有请求走 POST 端点,所有响应和通知都从那条 SSE ⻓连接回来。第三方 迁移指南把它概括为“两个端点、一条必需的持久连接、断流后没有定义好的恢复方式”(第三方评论,权威性较低)。 Fka Start Debugging Start Debugging 

厂商的实际运维反馈印证了这些问题。Atlassian 在弃用公告中说,HTTP+SSE 在网络抖动时很脆弱,SSE 会话难以干净恢复,常⻅报错如“No connection established for request ID”。它的 `/v1/sse` 端点只保留到 2026 年 6 月 30 日,之后要求迁移到 `/v1/mcp` (厂商官方公告)。 Atlassian Community 

### 2.2 PR #206 **的设计意图(设计讨论层)** 

Streamable HTTP 的原始提案是 modelcontextprotocol/specification 仓库的 PR #206,标题为“[RFC] Replace HTTP+SSE with new "Streamable HTTP" transport”,作者 Justin Spahr-Summers(@jspahrsummers),2025 年 3 月 17 日提出,3 月 24 日合并(共 24 个 commit)。PR github 描述说,它要在保留 HTTP+SSE 优点的同时解决其关键限制,并感谢了 Shopify、Pydantic、Cloudflare、LangChain、Vercel 和 Anthropic 团队。提案要点: GitHub 

- 所有 client→server 请求都可以被服务器“升级”为 SSE,用来发送通知和请求; GitHub 

- 服务器可以自行决定是否建立 session ID 来维持状态; GitHub 

- 客户端可以用一个空的 GET 主动打开 SSE 流; GitHub 

方案可以向后兼容实现,并且“allows servers to be fully stateless if desired”。 GitHub 

所以,“纯 HTTP 服务器按需升级到流式”是 Streamable HTTP 从一开始就有的核心诉求。当时也有人提议用 WebSocket 替代,被拒绝了。社区后来在 issue #493 中再次提出用 WebSocket 加无状态请求/响应来简化 HTTP 传输,理由是当时的方案“会话状态跨多条连接维护”,而且“同一结果有太多实现方式”(设计讨论层)。 GitHub 

### 2.3 **第一代设计遗留的问题:从** SEP-1335/1699 **到** “ **去状态化** ” 

2025-03-26 版虽然统一了端点,但仍然有三个问题: 

1. **⻓连接问题** :规范不允许服务器在计算结果期间关闭连接,服务器因此必须维持可能很⻓的连接。SEP-1335 和 SEP1699(作者 Jonathan Hefner)专⻔讨论了这一点。 GitHub 

2. **恢复盲区** :如果 SSE 流在发出第一个事件之前就断开,客户端没有 `Last-Event-ID` 可用,无法恢复(SEP-1335)。 GitHub 

3. **会话与负载均衡冲突** :2025 年 12 月 19 日的 MCP 官方博客《Exploring the Future of MCP Transports》(Transport WG 维护者 Kurtis Van Gent、Shaun Smith)写道,企业部署“scale to millions of daily requests”之后,早期采用者遇到了“make it difficult to leverage existing infrastructure patterns”的实际困难,并指出有状态连接会强制“sticky”路由,把流量钉在特定服务器上,从而“preventing effective auto-scaling”。原因是 MCP 原本是有状态协议,握手时确定的状态在整个连接期间固定,扩展就需要 sticky session 或分布式会话存储。博客提出的愿景是:“agentic applications are stateful, but the protocol itself doesn’t need to be”。同一篇博客还确认 MCP 仍只支持两种官方传输:本地用 STDIO,远程用 Streamable HTTP。 Modelcontextproto... 

Google 在开发者博客中说,它推动无状态传输是“born out of necessity”,并与 Hugging Face 等伙伴共同创立了 MCP Transports Working Group(厂商官方博客)。Microsoft Google Developers 的 App Service 文章给出了一个具体痛点:即使在 2025-11-25 的“stateless HTTP”模式下,每个连接仍以 `initialize` 握手开始,并返回一个 `Mcp-Session-Id` ,客户端要在后续每个请求里带上它,于是客户端被钉在签发这个 ID 的实例上(厂商官方博客)。 Microsoft Communi... 

## 3. **协议设计** 

### 3.1 **版本与治理现状** 

|**项目**|**事实**|**来源类型**|
|---|---|---|
|最新规范|2026-07-28(2026-07-28 正式发布;RC于 2026-05-21 锁定)<br>Modelcontextprotocol<br>GitHub|官方公告|
|性版本||/ 规范|
|前一版本|2025-11-25|规范|
|治理|2025-12-09 捐赠给AAIF(Linux 基金会下的directed fund,由Anthropic、Block、OpenAI共同创立,|官方公告|
||Google、Microsoft、AWS、Cloudflare、Bloomberg支持)<br>anthropic||
|版本号语|初版标识为 2024-11-05,Anthropic于 2024-11-25 公开发布<br>Wikipedia<br>Hidekazu-konishi|第三方时|
|义||间线|
|维护者|2026-07-28 发布文章署名为Lead MaintainersDavid Soria Parra、DenDelimarsky<br>modelcontextprotocol|官方公告|

注意:规范网站 `/specification/draft/...` 路径下的 Streamable HTTP ⻚面顶部已写明“Revision 2026-07-28 changed the behavior of Streamable HTTP”。本次查阅时,draft Model Context Prot... ⻚面内容与 2026-07-28 版一致,下文的规范性引用以它为准。 

### 3.2 2026-07-28 **版规范要点(规范性文本)** 

**端点与方法。** 服务器 MUST 提供一个只需支持 POST 的 MCP 端点(例如 `https://example.com/mcp` )。客户端发出的每条 Niteagent JSON-RPC 消息 MUST 是一个新的 HTTP POST,body MUST 是单个 JSON-RPC 请求或通知,客户端 MUST NOT 发送 JSON-RPC 响应。 modelcontextproto... 

**方法** / **头部** / **响应模式对照表(** 2026-07-28 **与** 2025-11-25 **对比):** 

|**维度**|2025-11-25**(第一代)**|2026-07-28**(第二代)**|
|---|---|---|
|POST|发送请求、通知或响应|只发送请求或通知|
|GET|可选,打开独立SSE流;不支持时回 405|已删除;只支持本版的服务器对GET回 405<br>Niteagent|
|DELETE|携带<br>`MCP-Session-Id` 终止会话;服务器可回<br>405|已删除;回 405<br>Niteagent|
|`Accept`|MUST同时列出<br>`application/json` 和<br>`text/event-stream` (GET只需<br>`text/event-stream` )|同左(POST)|
|通知的响<br>应|202Accepted,无body|同左|
|请求的响<br>应|`application/json` 单对象,或<br>`text/event-stream`|同左;SSE流只作用于该请求|
|会话头|`MCP-Session-Id` (在<br>`InitializeResult`<br>响应上分配)|已删除;忽略,也不签发|
|协议版本<br>头|`MCP-Protocol-Version` :握手后所有请求<br>MUST携带;缺失时SHOULD按 2025-03-26<br>处理;非法值回 400<br>sunpeak<br>ForgeCode|每个POST MUST携带,且MUST与<br>`_meta` 中的<br>`io.modelcontextprotocol/protocolVersion` 一致,否则回 400 +<br>`HeaderMismatch`|
|路由头|无|`Mcp-Method` (所有请求)、<br>`Mcp-Name`<br>(<br>`tools/call` 、<br>`resources/read` 、<br>`prompts/get` ),REQUIRED|
|参数镜像<br>头|无|`Mcp-Param-{Name}` ,由工具<br>`inputSchema` 中的<br>`x-mcp-header` 指定|
|`Last-`<br>`Event-ID`|通过GET恢复,按流重放|已删除;忽略|
|服务器→客<br>户端请求|可以在SSE流上发送|MUST NOT;改用MRTR的<br>`InputRequiredResult`|
|取消|断开连接不等于取消,须显式发<br>`CancelledNotification`|关闭SSE响应流MUST被视为取消<br>Niteagent|
|⻓期通知|GET流|`subscriptions/listen` 的POST响应流|

SSE **响应流语义(** 2026-07-28 **)。** 服务器 MAY 在最终响应之前发送与原请求相关的通知(如 `notifications/progress` 、 `notifications/message` ),MUST NOT 在流上发送独立的 JSON-RPC 请求;最终响应 SHOULD 终止该流。建立 SSE 流时服务器 SHOULD 加上 `X-Accel-Buffering: no` 响应头,防止 nginx 等反向代理缓冲。对于⻓期流(特别是 `subscriptions/listen` ),规范鼓励定期发送 SSE 注释行(如 `:\r\n` )作为 keep-alive,客户端必须 

### 忽略这些行。规范明确写道:“Resumable SSE streams via `Last-Event-ID` are not supported”。 Niteagent modelcontextproto... 

**错误码与状态码。** 请求了服务器不支持的版本时,回 `400` + `UnsupportedProtocolVersionError` ,并列出服务器支持的版本。方法不存在时回 `404` + JSON-RPC `-32601` ,body 用来区分这是现代服务器的 404,还是不托管现代端点的旧 HTTP+SSE 服务器的 404。头部校验失败时回 `400` + `-32020` ( `HeaderMismatch` )。按错误码分配政策, `-32000` ~ `-32019` 留给实现自定义, `-32020` ~ `-32099` 保留给规范,因此 `HeaderMismatch` 从 `-32001` 改为 `-32020` , `MissingRequiredClientCapability` 从 `-32003` 改为 `-32021` , `UnsupportedProtocolVersion` 从 `-32004` 改为 `-32022` 。 modelcontextproto... github 

**头部校验的安全含义。** 规范要求处理 body 的服务器 MUST 拒绝头部与 body 不一致的请求,目的是防止“负载均衡器按头路由、MCP 服务器按 body 执行”这种真相来源不一致引起的漏洞。依据镜像头做策略(如按租户限流)的中间层 SHOULD 先检查 `MCP-Protocol-Version` 是否属于要求头-体校验的版本;如果版本更旧或缺失,SHOULD 拒绝,不要信任未经校验的头。 `Mcp-Name` 和 `Mcp-Param-*` 的值如果含非 ASCII 字符、控制字符或首尾空白,MUST 用 `=?base64?...?=` 哨兵格式编码。 `x-mcp-header` 只能标注“静态可达”的原始类型属性(integer/string/boolean,不允许 number),不能穿过 `items` 、 `oneOf` 、 `$ref` 等。客户端 MUST 在 `tools/list` 结果中剔除违规的工具定义。 modelcontextproto... 

### 3.3 **消息流(按时序描述)** 

### **流程** A **:普通请求(** 2026-07-28 **)** 

Client → POST /mcp MCP-Protocol-Version: 2026-07-28 Mcp-Method: tools/call Mcp-Name: get_weather body: {id:1, method:"tools/call", params:{name, arguments, _meta:{protocolVersion, clientInfo, clientCapabilities}}} Server → 200 application/json {result...} (简单响应)或 → 200 text/event-stream event: notifications/progress ... event: JSON-RPC response(id:1)→ 关闭流(流式响应) 

### **流程** B **:服务器需要用户输入(** MRTR **,** SEP-2322 **)** 

Client → POST tools/call (id:1) Server → result: {resultType:"input_required", inputRequests:[elicitation/create ...], requestState?} Client → 收集输入 → POST tools/call (id:2, 原参数 + inputResponses) Server → result: {resultType:"complete", ...} 

所有结果现在都带必需字段 `resultType` ,取值为 `"complete"` 或 `"input_required"` 。客户端对不带该字段的旧服务器结果 MUST 当作 `"complete"` 。服务器如果要在重试之间关联某次 elicitation,就把自己的标识编码进 `requestState` 。 github 

### **流程** C **:变更通知(** **`subscriptions/listen` ,** SEP-2575 **)** 

Client → POST subscriptions/listen (选择 toolsListChanged / resourceSubscriptions 等) Server → SSE: notifications/subscriptions/acknowledged → SSE: notifications/tools/list_changed (带 io.modelcontextprotocol/subscriptionId) → ......一直保持到任一方关闭 

请求级通知(progress/message)不走 listen 流,只出现在对应请求的响应流上。 modelcontextproto... github 

**流程** D **:第一代会话生命周期(** 2025-11-25 **,旧客户端兼容仍会用到)** 

POST InitializeRequest → 响应头 MCP-Session-Id: 1868a90c... POST InitializedNotification (带会话头) → 202 POST 请求(带会话头) → JSON 或 SSE GET (带会话头) → 独立 SSE 流,承载与当前请求无 关的服务器请求/通知服务器终 止会话后 → 对该 ID 回 404 → 客户端 MUST 不带 ID 重新 initialize DELETE (带会话头) → 终止;服务器可回 405 表示不允许客户端终止 

2025-11-25 对会话 ID 的要求:SHOULD 全局唯一且密码学安全(如安全 UUID、JWT、哈希), GitHub MUST 只含可 ⻅ ASCII 字符(0x21~0x7E)。要求会话的服务器对不带 ID 的非初始化请求 SHOULD 回 400。 modelcontextproto... 

**流程** E **:第一代断点续传与轮询(** 2025-11-25 **)** 

- 服务器发起 SSE 流时 SHOULD 立即发送一个只含事件 ID、 `data` 为空的 priming 事件,让客户端有 `Last-Event-ID` 可用; modelcontextproto... 

- 发出带 ID 的事件后,服务器 MAY 随时关闭“连接”但不终止“流”,客户端 SHOULD 重连来“轮询”;服务器关闭前 SHOULD 发送 `retry` 字段,客户端 MUST 遵守; modelcontextproto... 

- 事件 ID MUST 在会话内(没有会话时在该客户端范围内)所有流中全局唯一,SHOULD 编码足够信息来识别所属的流; modelcontextproto... 

- 恢复一律通过带 `Last-Event-ID` 的 HTTP GET,不管原来的流是 POST 还是 GET 发起的;服务器 MUST NOT 重放本应投递到其他流的消息。也就是说,事件 ID 是“每条流内的游标”; modelcontextproto... 

- 服务器 MUST 把每条消息只发送到一条已连接的流上,不能广播。 modelcontextproto... 

### 3.4 **协议版本协商与向后兼容** 

2026-07-28 版没有握手:每个请求在 `_meta` 中声明版本,HTTP 头部携带同一个值;服务器 MUST 实现 `server/discover` ,客户端 MAY 预先调用它。同时支持新旧时代的客户端 Modelcontextproto... MAY 先发一个现代请求来探测:如果收到 400,SHOULD 先检查 body——body 是可识别的现代 JSON-RPC 错误(版本不支持、缺少能力、头校验失败),说明服务器是现代的,应按对方公布的 `supported` 版本重试;body 为空或无法识别时,才回退到 `initialize` 握 手。 Hidekazu-konishi +2 

与 2024-11-05 HTTP+SSE 的兼容逻辑保留下来:服务器可以同时托管旧的 SSE/POST 端点和新 MCP 端点。客户端先 POST;如果失败状态为 400、404 或 405,并且 body 不是现代错误,就发 GET,期待第一个事件是 `endpoint` ,收到则认定对方是旧传输。按 SEP-2596 的功能生命周期政策,HTTP+SSE 被正式归类为 Deprecated,新实现 SHOULD NOT 采 用。政策规定弃用窗口至少十二个月。 Modelcontextproto... 

### 3.5 **规范保证什么,不保证什么** 

- **保证** :请求与响应流一一对应(2026);关闭流等于取消(2026);头部与 body 一致(2026);每条消息只投递到一 条流(2025);按流重放、不跨流重放(2025)。 

- **不保证** :投递可靠性。2026-07-28 版明确规定,响应流断开会丢失正在进行的请求,客户端 MUST 以新的请求 ID 重新发出。 Niteagent github 规范没有定义幂等键,重试是否安全取决于工具本身(可参考工具注解中的 idempotent 等语义)。2025 版的重放也只是 MAY,服务器是否持久化事件、保存多久,由实现决定。 

## 4. **参考实现分析** 

### 4.1 TypeScript SDK 

**版本线(** SDK **文档层)。** `main` 分支现在是 v2,以拆分包形式发布 

( `@modelcontextprotocol/server` 、 `/client` 、 `/node` 、 `/express` 、 `/fastify` 、 `/hono` ),与 2026-07-28 规范一同发布为稳定版。v1 保留在⻓期 `v1.x` 分支上,v2 发布后至少再获得 6 个月的缺陷和安全修复。 `@modelcontextprotocol/sdk` GitHub github 1.30.x 是 v1 的最后一条线,只支持到 2025-11-25。GitHub GitHub GitHub 官方 Release 1.10.0 ⻚面 确认,1.10.0 是“the first release supporting the new Streamable HTTP transport from protocol version 2025-03-26”,它取代了 2024-11-05 的 SSE 传输。服务器端最初的实现是 PR #266(作者 ihrpr),基于 #230 的工作。评审中 Justin SpahrSummers 建议把 `sessionIdGenerator` 设计为“函数或 undefined”,只在收到 `InitializeRequest` 时调用。这就是后来“ `undefined` GitHub 即无状态”这一 API 语义的由来。 

v1 **服务器:** **`StreamableHTTPServerTransport` 内部结构(源码层,基于** issue #451 **引用的早期源码,约** v1.10 **~** 1.11 **)。** 

### ts 

class StreamableHTTPServerTransport implements Transport { private sessionIdGenerator: (() => string) | undefined; // undefined = 无状态 private _streamMapping = new Map<string, ServerResponse>(); // streamId → 响应流 private _requestToStreamMapping = new Map<RequestId, string>(); // JSON-RPC id → streamId private _requestResponseMap = new Map<RequestId, JSONRPCMessage>(); private _standaloneSseStreamId = '_GET_stream'; // 独立 GET 流的固定 key private _eventStore?: EventStore; ... } 

路由机制:一个包含请求的 POST 打开一条 SSE 流后,transport 为这条流生成 streamId,并把 POST 中每个请求的 id 映射到该 streamId。服务器发送响应或通知时,按“相关请求 id”(related request id)找到对应的流写出;与任何请求无关的消息写到 `_GET_stream` 。批中所有请求都有了响应后,流关闭。独立 GET 流用的是固定 key,所以每个会话只能有一条 GET 流。在当前 GitHub v1 版本中,第二条 GET 流被拒绝时的具体状态码(通常是 409 Conflict)未经本次源码核实。 

**架构演进(包文件层)。** 已发布的 v1.27.1 包中, `dist/cjs/server/webStandardStreamableHttp.js` 约 34.8 kB, `streamableHttp.js` 只有约 6.78 kB。这说明 unpkg Node 版 `StreamableHTTPServerTransport` 已变成 `WebStandardStreamableHTTPServerTransport` (基于 Web 标准 Request/Response)的一层薄包装,因此可以运行在 Workers、Deno、Bun 等运行时上。v1.25.1 Modelcontextproto...的 web-standard 实现会校验 `Accept` :POST 不同时接受 `application/json` 和 `text/event-stream` 时回 406,消息为“Not Acceptable: Client must accept both application/json and text/event-stream”。issue GitHub #1944 指出,即使设置了 `enableJsonResponse: true` ,只带 `Accept: application/json` 的请求也会被 406 拒绝,这比规范要求更严格。 GitHub 

### **构造选项(** SDK **文档** / **派生代码层)。** 

`sessionIdGenerator` 、 `onsessioninitialized` 、 `onsessionclosed` 、 `enableJsonResponse` 、 `eventStore` 、 `allowedHosts` 、 `allowedOrigins` 、 `enableDnsRebindingProtection` 、 `retryInterval` 。SDK GitHub glama 文档说明:把 `sessionIdGenerator` 设为 `undefined` 就是无状态模式,“simpler, but does not support resumability”; `enableJsonResponse: true` 返回纯 JSON,不开 SSE。已知行为缺陷:JSON GitHub 响应模式下,带关联请求 id 的进度通知会被 `send()` 直接丢弃(issue #866);另外没有公开 API 能从持久化数据重建一个带会话的 transport (issue #1658),用户只能改私有字段。这正是 GitHub GitHub v1 做水平扩展的主要障碍。 

### EventStore **接口(源码层)。** 

ts interface EventStore { storeEvent(streamId: StreamId, message: JSONRPCMessage): Promise<EventId>; replayEventsAfter(lastEventId: EventId, { send }: { send: (eventId: EventId, message: JSONRPCMessage) => Promise<void> } ): Promise<StreamId>; // 较新版本另有可选的 getStreamIdForEventId(eventId),用于冲突检测(DeepWiki 转述,权威性较低) } 

语义:每次写出 SSE 事件前先调用 `storeEvent` 得到事件 ID;客户端带 `Last-Event-ID` 重连时, `replayEventsAfter` 按原流重放,并返回该流的 streamId,transport 据此重新绑定映射。官方示例提供了进程内的 GitHub DeepWiki `InMemoryEventStore` ;生产环境中的 Redis 等外部实现需要自己编写,或使用社区库。 

v1 **客户端:** **`StreamableHTTPClientTransport` (源码层,已核实)。** 

ts 

const DEFAULT_STREAMABLE_HTTP_RECONNECTION_OPTIONS = { initialReconnectionDelay: 1000, maxReconnectionDelay: 30000, reconnectionDelayGrowFactor: 1.5, maxRetries: 2 }; 

即指数退避:1 s 起步,按 1.5 倍增⻓,封顶 30 s,默认最多重试 2 次。服务器通过 GitHub SSE `retry` 字段下发的间隔会记录在 `_serverRetryMs` 中。 `StartSSEOptions` GitHub 支持 `resumptionToken` 和 `onresumptiontoken` ,用于续接中断的⻓ 请求。解析器在 GitHub `if (event.id)` 的真值判断中更新 token,所以空 `id:` 清不掉过期 token(issue #2769)。已报告的问题:在 GitHub 1.29.0 中重试次数耗尽后,POST 仍能到达服务器,但响应丢失(issue #2098);每次重连成功后计数都会清零,所以对一个“连上就立刻断开”的服务器,客户端会以约每秒一次的频率无限重连(第三方仓库 issue)。官方文档建议在 GitHub GitHub `client.close()` 之前调用 `transport.terminateSession()` 。 GitHub 

### v2 **:** **`createMcpHandler` (** SDK **文档层)。** 

ts 

import { createMcpHandler, McpServer } from '@modelcontextprotocol/server'; const handler = createMcpHandler(() => new McpServer({ name: 'my-server', version: '1.0.0' }, { capabilities: { tools: {} } })); export default handler; // Web 标准运行时 // Node:app.all('/mcp', toNodeHandler(handler)) // 来自 @modelcontextprotocol/node 

- 工厂函数对每个请求构造一个服务器实例。默认 `legacy: 'stateless'` :2026-07-28 请求逐个服务,2025 时代的流量也用“既有的无状态惯用法”逐请求服务,实现“One factory, one endpoint, both eras”。 GitHub Modelcontextproto... 

- 已有的有状态 v1 部署可以用 `isLegacyRequest(request)` 把旧流量路由给原有的会话处理器,现代流量交给 

- `createMcpHandler(factory, { legacy: 'reject' })` 。 `isLegacyRequest` 只在请求没有逐请求 `_meta` 信封时返回 

- true。 GitHub 

- handler 只依赖 Web 标准,暴露 `{ fetch, close, notify, bus }` ;另有 `legacyStatelessFallback(factory)` 。v1 的“无状态 + 每请求新 transport”写法可以直接映射到默认入口。 GitHub Modelcontextproto... 

- 客户端 `ClientOptions.versionNegotiation` 有三种模式:不设或 `'legacy'` (默认,与 v1 逐字节相 

- 同); `'auto'` (先用 `server/discover` 探测,多一次往返后回退); `{ pin: '2026-07-28' }` (只走现代协议)。探测策略比较保守:HTTP 401/403 和 5xx 都不被当作“服务器属于哪个时代”的证据,会直接失败;HTTP 探测超时报 `RequestTimeout` ,不会误判为旧服务器;在 stdio 上探测则用一个短命的“兄弟进程”,因为基于官方 Rust SDK 

- (rmcp)的服务器收到 `initialize` 之前的任何请求就会退出。 modelcontextproto... 

- `@modelcontextprotocol/codemod` 提供 `v1-to-v2` 自动迁移。 GitHub 

### 4.2 Python SDK 

v1 **线:** **`StreamableHTTPSessionManager` (** API **文档层)。** 构造参数: 

|**参数**|**默认值**|**语义**|
|---|---|---|
|`app`|必填|低层<br>`Server` 实例|
|`event_store`|`None`|提供时启用可恢复连接;为None时仍跟踪会话,但不可恢复<br>modelcontextprotocol|
|`json_response`|`False`|用JSON代替SSE|
|`stateless`|`False`|True时每个请求创建全新 transport,不跟踪会话<br>modelcontextprotocol|
|`security_settings`|`None`|`TransportSecuritySettings` (DNSrebinding防护等)|
|`retry_interval`|`None`|写入SSE<br>`retry` 字段的毫秒数,用于轮询<br>modelcontextprotocol|
|`session_idle_timeout`|1800 秒|空闲(没有进行中的请求,也没有打开的GET流)超时后终止会话,之后该ID返回 404;None<br>表示禁用<br>modelcontextprotocol|
|`max_request_body_size`|4MiB|超限时在解析和建会话之前回 413<br>modelcontextprotocol<br>DeepWiki|
|`max_sessions`|10 000|达到上限时新会话得到 503;None表示不限<br>modelcontextprotocol|

文档强调:每个应用只应创建一个 `StreamableHTTPSessionManager` ; `run()` modelcontextproto...每个实例只能调用一 次,必须放在 Starlette lifespan 里( `async with session_manager.run(): yield` ),用来管理内部的 anyio task group。 `handle_request(scope,  receive, send)` 是 ASGI 入口,根据 stateless 设置分派。底层 Modelcontextproto... <mark>`StreamableHTTPServerTransport.__init__(mcp_session_id, is_json_response_enabled=False, event_store=None, security_settings=None, retry_interval=None)`</mark> , `Accept` 解析支持 RFC 7231 通配符( `*/*` 、 `application/*` 、 `text/*` )。PR Modelcontextproto... #3574 让无状态模式下 `_handle_get_request` 直接回 405,不再先检查 Accept 或建流。 GitHub 

内部机制上,服务器 transport 用 anyio memory object stream 把每个请求的响应分流到对应的 SSE 写出协程,GET 流使 用固定 key。这与 TypeScript 的 `_requestToStreamMapping` 思路相同;具体的字段名(如 `_request_streams` 、 `GET_STREAM_KEY` )未经本次源码核实。 

v2 **线(官方发布说明层)。** Python SDK v2.0.0 于 2026-07-28 发布: `FastMCP` 改名为 `MCPServer` ,装饰器 API 不变;低层 Modelcontextproto... `Server` 围绕共享 dispatcher 引擎重建;一个 `Client` 对象取代 v1 的“transport + ClientSession + initialize()”三层结构。同一个 `MCPServer` 可以在 Streamable HTTP 和 stdio 上同时服务 2026-07-28 与所有 2025 时代客户端,“with nothing to configure”; `Client(target)` GitHub DEV Community 会自动探测 `server/discover` ,并回退到握手。传输选项(host、port、 `stateless_http` 、 `json_response` 、路径、 `transport_security` )从构造函数移到了 `run()` 和 app builder 上, `mount_path` 被删除。官方文档提醒了两点:第一,2025 时代客户端仍会建立会话,仍需要原来的粘性;第二,MRTR 重试要跨 worker 携带密封的 `request_state` ,而默认密钥按进程生成,所以扩容部署必须传 `RequestStateSecurity(keys=[...])` 。v2.2.0 Modelcontextproto...的发布说明(#3395)规定,旧协议的有状态会话空闲 30 分钟后关闭,每个服务器最多 10 000 个会话,超过的新会话得到 503;保持 GET 流开启的客户端、无状态服务器和 2026-07-28 连接不受影响。Pydantic GitHub DEV Community 建议依赖 `mcp` 的库先加上限,例如 `mcp>=1.27,<2` 。 Pydantic 

最小无状态示例(v2,第三方博客给出、与官方 API 一致): DEV Community 

python from mcp.server.mcpserver import MCPServer mcp = MCPServer("units") @mcp.tool() def to_celsius(fahrenheit: float) -> float: return round((fahrenheit - 32) * 5 / 9, 2) mcp.run(transport="streamable-http", stateless_http=True, json_response=True) 

### 4.3 **其他官方** SDK 

|SDK|**状态(截至** 2026-09**)**|**值得注意的实现差异**|
|---|---|---|
|Go<br>(Google<br>维护)|v1.7.0 于 2026-07-28 发布,支持新规范<br>Google Developers|issue#1262:<br>`StreamableHTTPOptions` 没有keep-alive间隔,<br>transport 不做周期性写出,而<br>`http.Server.WriteTimeout` 在SSE响应<br>期间一直生效,⻓流会在第一条通知之前被掐断;相关修复还在<br>#1155/#1197、#1229/#1232 中讨论<br>GitHub|
|C#|Tier 1;beta为<br>`ModelContextProtocol`<br>2.0.0-preview.1<br>Modelcontextprotocol|必须显式设置<br>`StreamableHTTPOptions.Stateless = true` 才接受<br>2026-07-28,否则协商降到 2025-11-25;roots/sampling/logging标为<br>`[Obsolete]`<br>Modelcontextprotocol|
|Rust<br>(rmcp)|以beta形式支持新规范<br>modelcontextprotocol|旧版服务器收到<br>`initialize` 之前的请求就退出,影响客户端探测策略<br>modelcontextprotocol|
|Kotlin|实现了<br>`StreamableHttpServerTransport`<br>与<br>`EventStore` (PR#449)<br>github|为 priming事件新增<br>`JSONRPCEmptyMessage`<br>github|
|Ruby|官方SDK1.0.0 稳定版已发布<br>Modelcontextprotocol|底层<br>`json_rpc_handler`gem 按JSON-RPC规范支持batching,与<br>2025-06-18 删除batching有冲突(PR#416 讨论)<br>GitHub|
|Java、<br>Swift、<br>PHP|本次未取得一手状态信息|需要自行核实|

## 5. **部署与扩展模式** 

### 5.1 **三种架构及其取舍** 

|**模式**|**典型做法**|**得到**|**失去**|
|---|---|---|---|
|A. 有状态会|`sessionIdGenerator: () =>`|服务器主动请求、GET推送、断点续传|水平扩展要靠粘性或共享存储;实|
|话(2025|`randomUUID()` + 进程内 transport 表||例重启会丢会话;v1 没有公开的|
|协议)|+ 负载均衡粘性||transport 重建API|
|B. 2025 协|`sessionIdGenerator: undefined`|可以 round-robin|不能续传,GET流通常回 405,不|
|议的“无状|/<br>`stateless=True` ,每请求新||能做服务器主动请求;握手仍然存|
|态模式”|transport||在|
|C. 2026-|`createMcpHandler` /<br>`MCPServer`|任意实例处理任意请求,网关可按头路由,|列<br>断流即丢请求,必须重发;跨调用|
|07-28 原生|现代路径|表可缓存(<br>`ttlMs` /<br>`cacheScope` )|状态要显式句柄加外部存储;|
|无状态||Modelcontextprotocol|MRTR的<br>`requestState` 需要共<br>享密钥|

MCP 官方博客对模式 C 的建议是:如果需要跨调用状态,就由工具签发显式句柄(如 `basket_id` ),让模型在后续调用中作为普通参数传回。官方认为这比藏在传输元数据里的会话状态更好,因为模型能看到并组合这些句柄。Microsoft Modelcontextproto... modelcontextproto...的 App Service 实践给出了模式 B 向 C 过渡的具体配置:多实例扩容,设置 `clientAffinityEnabled: false` 关闭 ARR 亲和 cookie,确实需要共享状态时外置到 Azure Cache for Redis,再用 Application Insights 的 `cloud_RoleInstance` 验证流量分布。 Microsoft Communi... 

**建议:** 新服务直接采用模式 C。同一端点用 SDK 默认的 `legacy: 'stateless'` 或 Python v2 的自动双时代兼容,接住 2025 客户端。只有确实依赖服务器主动 sampling/elicitation 推送或 GET 推送的旧功能,才保留模式 A 的独立路由,用 `isLegacyRequest` 分流,并计划在十二个月弃用窗口内迁移。 

### 5.2 Serverless **与边缘** 

- Cloudflare **(厂商官方文档** / **博客)** :Agents SDK 提供 `createMcpHandler()` (无状态、不需要 Durable Objects)和 `McpAgent` (每个会话一个 Durable Object,自带 SQL 存储、支持 WebSocket Hibernation)。Cloudflare Cloudflare cloudflare 的 2026-07-28 博客称新规范“removes the need for McpAgent”, `/mcp` 端点同时接受新协 

- 议请求和 2025 客户端的无状态请求。官方文档已把 Cloudflare `McpAgent` 标为 deprecated、feature-frozen,建议尽快迁移到 `createMcpHandler` ;依赖会话状态、推送请求、独立流或重放的服务器需要分阶段迁移,双路由并行服务。文档还提到 Cloudflare 边缘有一个约 5 分钟的空闲流看⻔狗: `McpAgent` 的 GET 流在配置了 EventStore 时,靠客户端带 `Last-Event-ID` 重连来恢复。另外,文档特别提醒从 Cloudflare 1.26.0 之前升级的用户:放在全局作用域的 `McpServer` 或 transport 实例必须改为每请求新建(⻅ §6.3)。 Cloudflare 

- AWS **(官方公告引语)** :Amazon Bedrock AgentCore 已支持新规范的无状态核心;Tasks 扩展由 AWS 贡献。 Modelcontextproto... 

- Google:Go SDK 与 Google Cloud 生态同步支持;Google 博客称去状态化让“load balancing boring, autoscaling seamless”(厂商博客,带营销措辞)。 Google Developers 

- Vercel mcp-handler **、** AWS Lambda **、** Google Cloud Run **的具体实现** :本次没有取得一手资料,不作断言。从原理上讲,模式 C 与任何按请求计费的 FaaS 都天然兼容;模式 A 则需要外部会话存储,并受平台最大响应时⻓限制。 

### 5.3 SSE **运维要点** 

1. **代理缓冲** :设置 `X-Accel-Buffering: no` (2026 规范 SHOULD),并在 nginx 等代理上关闭 `proxy_buffering` 。第三方迁移指南把“新端点看起来坏了”归因于代理缓冲。 modelcontextproto... Start Debugging 

2. **空闲超时与心跳** :⻓流要定期发 `:` 注释行(2026 规范鼓励);服务器的写超时(如 Go 的 `WriteTimeout` )需要对 SSE 豁免或定期刷新,否则流会在第一条通知前被断开(Go SDK issue #1262)。 modelcontextproto... GitHub 

3. **连接数** :2025 协议下每个会话可能同时占用“1 条 GET 流 + N 条 POST 流”;2026 协议取消了 GET 流,只有 `subscriptions/listen` 这一条可选⻓流。 github 

4. **重连⻛暴** :TS v1 客户端默认最多重试 2 次,但成功后计数清零(⻅ §4.1);服务器用 GitHub `retry` 字段控制节奏,Python 文档要求 `session_idle_timeout` 明显大于 `retry_interval` ,防止在正常轮询间隙中误回收会话。 modelcontextproto... 

5. CORS:浏览器客户端探测新协议时,旧服务器的 CORS 白名单可能不包含 2026 新头( `Mcp-Method` 等),TS v2 在浏览器里遇到不透明的 CORS `TypeError` 时回退到旧时代。服务器侧要把新头加进 modelcontextproto... <mark>`AccessControl-Allow-Headers` ,</mark> 并在 `Access-Control-Expose-Headers` 中暴露 2025 协议需要读取的 `Mcp-Session-Id` 。 

### 5.4 **主要平台的采用情况(仅一手来源)** 

- Anthropic:Claude Messages API 的 MCP connector 当前 beta 头为 `mcp-client-2025-11-20` ,旧的 <mark>`mcp-client2025-04-04`</mark> 已弃用;服务器必须通过 HTTPS 公开,文档写明“supports both Streamable HTTP and SSE transports”,只支持工具调用,不能直连本地 STDIO; `mcp_servers` 定义连接 <mark>(</mark> <mark>`type:`</mark> 

- <mark>`"url"`</mark> 、 `url` 、 `name` 、 `authorization_token` ), `mcp_toolset` 配置工具的允许/禁止与 `defer_loading` ;使用 <mark>`mcpclient-2026-09-15`</mark> beta 头时,toolset 可以接受一份“固定的”服务器工具清单。Claude claude Agent SDK / Claude Code 用 `"type": "http"` 表示 Streamable HTTP,JSON 配置里也接受 `"streamable-http"` 别名;OAuth 流程由应 用自己完成,再把 token 放进 headers 传入。 Claude API Docs Claude Code Docs 

- Microsoft:Microsoft Foundry 的 toolbox 提供统一 MCP 端点(官方公告引语);App Service 发布了无状态扩展指南。 Microsoft Communi... modelcontextproto... 

- **其他** :MCP 官方发布文章收录了 Cloudflare、Figma、Supabase、Netlify、Honeycomb 等厂商的支持声明(厂商引语,属于营销性陈述)。Linear modelcontextproto...以 `https://mcp.linear.app/mcp` 为主端点, `/sse` 是弃用的回退端点。 Linear 

- OpenAI Agents SDK / Responses API:本次检索预算内没有取得一手文档,不作断言,需要另行核实。 

## 6. **安全** 

### 6.1 **传输层规范要求** 

2025-11-25 与 2026-07-28 两版一致:服务器 MUST 校验所有入站连接的 `Origin` 头以防 DNS rebinding, `Origin` 存在且非法时 MUST 回 403(403 的要求来自 2025-11-25 的 PR #1439);本地运行时 SHOULD 只绑定 127.0.0.1,不要绑定 0.0.0.0;SHOULD 对所有连接实施认证。2026 modelcontextproto...版增加了头-体一致性校验(§3.2),把它作为一道防线,防止网关与服务器“看到的真相不同”。 modelcontextproto... 

### 6.2 **授权框架与** HTTP **传输的关系** 

- 2025-06-18:MCP 服务器被归类为 OAuth Resource Server,通过 Protected Resource Metadata 发现授权服务器(PR #338);客户端 MUST 实现 RFC 8707 Resource Indicators,防止恶意服务器拿到访问令牌(PR #734)。 Modelcontextproto... 

- 2025-11-25:支持 OpenID Connect Discovery 1.0(PR #797);通过 `WWW-Authenticate` 实现增量授权(SEP835)。 Model Context Prot... 

- 2026-07-28:授权服务器 SHOULD 按 RFC 9207 返回 `iss` ,客户端 MUST 在兑换授权码前校验(SEP-2468,防 mixup 攻击);DCR 时声明 `application_type` (SEP-837);客户端凭据与签发它的 Modelcontextproto... issuer 绑 

- 定,不能跨授权服务器复用(SEP-2352);RFC 7591 Dynamic Client Registration 被正式弃用,改用 Client ID Metadata Documents(PR #2858)。 github modelcontextproto... 

- 与传输的交互:401 挑战通过 HTTP 状态码和 `WWW-Authenticate` 在同一个 MCP 端点上完成;无状态化以后,每个请求都独立携带 Bearer token,不再依赖会话绑定身份。第三方评论提醒:“Stateless MCP is a scalability fix, not a security fix”。提示词注入、供应链之类的威胁不受影响。 DEV Community 

### 6.3 **已知漏洞与修复** 

|**编号**|**影响范围**|**机制**|**修复**|
|---|---|---|---|
|CVE-|TS SDK< 1.24.0|`StreamableHTTPServerTransport` /<br>`SSEServerTransport` 默认不启用|1.24.0(PR#1205):据 2025-12-02|
|2025-||DNSrebinding防护;在localhost 运行、未认证、也没设置|发布的GitHub Advisory,只有通过|
|66414||`enableDnsRebindingProtection` 时,恶意网站可以绕过同源策略调用本|`createMcpExpressApp()` 创建、|
|/||地工具<br>GitHub|绑定localhost 的服务器默认启用该|
|GHSA-|||防护;使用自定义Express 配置的服|
|w48q-|||务器要自己加|
|cv73-|||`hostHeaderValidation()` 中间件|
|mx4w||||
|CVE-|PythonSDK<|HTTP类服务器默认不启用DNSrebinding防护|1.23.0:<br>`host` 为 127.0.0.1 或|
|2025-|1.23.0(GitHub||localhost 时,通过<br>`FastMCP()` 创|
|66416|Advisory,2025-||建的服务器默认启用该防护;直接使|
|/|12-02 发布)||用|
|GHSA-|||`StreamableHTTPSessionManager`|
|9h52-|||的服务器仍要自己配置|
|p55h-|||`TransportSecuritySettings`|
|vw2f||||
|CVE-|TS SDK1.10.0~|多个客户端复用同一个 transport 时,transport 内部的<br>`requestId →`|1.26.0:<br>`Protocol.connect()` 在|
|2026-|1.25.3;NVD于|`stream` 映射会被覆盖——SDK客户端的JSON-RPC id从 0 递增,不同客户|已连接时直接抛错,把静默串流变成|
|25536 /|2026-02-04 公|端的id必然重复——于是响应写到了别的客户端的HTTP流上;复用同一个|显式错误<br>GitHub|
|GHSA-|布,CVSS3.1 评|`McpServer` 时,进度通知、sampling和elicitation 也会串流<br>GitHub||
|345p-|分 7.1,CWE-362|||
|7cg4-||||
|v4c7||||
|CVE-|下游项目|创建 transport 时没有设置|应用层修复(示例:SDK修好了,应|
|2026-|`@zereight/mcp-`|`allowedHosts` /<br>`allowedOrigins` /<br>`enableDnsRebindingProtection` ,|用配置错误仍然会引入漏洞)|
|61568|`gitlab`|默认监听 127.0.0.1<br>GitLab||

**工程含义:** CVE-2026-25536 说明,v1 时代“有状态映射表 + 无状态部署”的组合本身就容易出错:开发者为了省开销在全局复用实例,结果破坏了隔离。2026-07-28 版让每个请求自带响应流、SDK 用工厂函数逐请求建实例,从结构上消除了这类问题。 **必须做的事** :TS 依赖锁定到 ≥1.26.0(v1 线)或迁移到 v2;本地 HTTP 服务器启用 Host/Origin 白名单,最好改用 stdio。 

## 7. **版本演进时间线** 

|**日期**|**事件**|**与**Streamable HTTP**的关系**|
|---|---|---|
|2024-11-<br>05 / 11-<br>25|初版规范 /Anthropic公开发布<br>MCP|定义HTTP+SSE双端点传输|
|2025-<br>03-17 →<br>03-24|PR#206 提出并合并|Streamable HTTP诞生;PR#228 曾要求必须支持JSON-RPC batching|
|2025-<br>03-26|规范修订版发布|引入Streamable HTTP,弃用HTTP+SSE;支持batching|
|2025-04|TS SDK PR#266、Python<br>SDK issue#443|参考实现落地(据GitHub官方Release⻚面,TS1.10.0 是首个支持Streamable HTTP的版<br>本)|
|2025-|规范修订版|删除JSON-RPC batching(PR#416,理由是实现两个SDK时“没有看到令人信服的用例”,|
|06-18||但有社区反对);HTTP下后续请求必须带<br>`MCP-Protocol-Version` (PR#548);授权改<br>为Resource Server 模型;新增elicitation(PR#382)<br>GitHub<br>Modelcontextprotocol|
|2025-08<br>/ 10|SEP-1335 /SEP-1699 提出|解决⻓连接与恢复盲区|
|2025-11-<br>25|规范修订版|允许服务器随时断开并让客户端轮询(SEP-1699);priming事件;恢复统一走GET;无效<br>Origin 回 403(PR#1439);实验性Tasks(SEP-1686)|
|2025-12-|MCP捐赠给AAIF|治理中立化|
|09|Modelcontextprotocol||
|2025-12-|《Exploringthe Futureof|公布去状态化路线;只保留两种官方传输<br>Modelcontextprotocol|
|19|MCP Transports》||
|2026-<br>02-04|CVE-2026-25536 公布<br>Vulnerablemcp|NVD记录:1.10.0~1.25.3 在多个客户端连接复用同一McpServer/transport 实例时发生跨客<br>户端响应泄漏(CVSS3.1 评分 7.1,CWE-362),1.26.0 修复|
|2026-|2026 路线图|四大优先领域中第一项是传输可扩展性<br>Modelcontextprotocol<br>Mcp|
|03-09|||
|2026-|2026-07-28RC锁定|十周验证窗口|
|05-21|Modelcontextprotocol||
|2026-|2026-07-28 正式发布|删除会话/GET/DELETE/续传/服务器请求;新增<br>`_meta` 、<br>`server/discover` 、|
|07-28||MRTR、<br>`subscriptions/listen` 、<br>`Mcp-Method` /<br>`Mcp-Name` /<br>`Mcp-Param-`<br>`*` 、<br>`ttlMs` /<br>`cacheScope` ;Tasks 移入扩展;HTTP+SSE按新政策归为Deprecated|
|2026-<br>08-22|路线图⻚面更新<br>Model Context Protocol|下一阶段的传输工作由KurtisVanGent、Nick Cooper 负责<br>Model Context Protocol|

## 8. **未决问题与进行中的讨论(截至** 2026-09 **)** 

1. **服务器主动事件** :新路线图(2026-08-22 更新)把 webhooks、channels 等服务器主动事件列为重点,目的是让客户端不必轮询结果。这项工作需要 Agents、Transports、Triggers & Events 三个工作组做组合评审。它将决定 Modelcontextproto... `subscriptions/listen` 之外还有没有更适合 serverless 的推送机制。 

2. **传输的** HTTP **语义化** :路线图称 2026-07-28 让远程服务器成了普通 HTTP 工作负载,今后会更多依赖头部和状态码来传递传输层信息。可以预期还会有更多“镜像到头部”的字段和状态码语义方面的 Model Context Prot... SEP。 

3. Tasks **扩展成熟化** :SEP-2663 把 `tasks/result` 阻塞模型改为 `tasks/get` 轮询加 `tasks/update` ,下一步是让它回到规范正文。这是“断流即丢请求”问题的官方答案:⻓任务应当 Modelcontextproto... Task 化。 

4. WebSocket / gRPC **等新传输** :社区多次提出(如 issue #493),维护者坚持只保留 stdio 和 Streamable HTTP 两种官方传输;有第三方报道提到 Modelcontextproto... Chenguangliang MCP Dev Summit 上讨论过 gRPC,但没有进入规范路线。本报告的判断:短期内不会新增官方传输。 Mcp 

5. SDK **层的未决缺陷** :Go SDK 缺少 keep-alive(#1262 等);TS v1 在 JSON-only Accept 下回 406(#1944)、重连语义有问题(#2098、#2769)。这些都属于 2025 协议兼容路径上的问题,会在十二个月弃用窗口内持续影响旧客户端。 

6. **弃用移除时间** :按 SEP-2596,2026-07-28 标为 Deprecated 的特性(HTTP+SSE、Roots、Sampling、Logging、 DCR)最早在 2026-07-28 之后至少十二个月才能移除。截至 Modelcontextproto... 2026 年 9 月,还没有任何特性按该政策被移除(第三方汇总,与官方政策一致)。 

## 9. **来源质量与时效性说明** 

- **关于** “Anthropic **最新发布** ”:没有找到 Anthropic 在 2026 年单独发布的“Streamable HTTP”公告。最可能的对应是 MCP 项目 2026-07-28 规范(Anthropic 员工担任 Lead Maintainer,但 MCP 已归 AAIF/Linux 基金会治理),或者 Claude API MCP connector 的 beta 迭代( `mcp-client-2025-11-20` 、 `mcp-client-2026-09-15` )。如果用户指的是 2025 年 3 月首次引入 Streamable HTTP,那么第 3.3 节流程 D/E 和第 4 节的 v1 分析就是对应内容。 

- **规范性文本** :直接取自 modelcontextprotocol.io 的 2026-07-28(draft 路径)Streamable HTTP ⻚面、2025-11-25 Transports ⻚面,以及 GitHub 上的 2026-07-28 changelog,可信度最高。2025-06-18 changelog 只核对了条目摘要。 

- SDK **源码** :TS v1 内部字段名来自 issue #451 引用的早期源码(约 v1.10~1.11)。当前 v1.27+ 的逻辑已移到 `webStandardStreamableHttp.ts` ,字段类型可能已改变。客户端重连默认值已经核实。第二条 GET 流的 409、 

- DELETE 返回 200、会话缺失/未知时的 400/404 文案、Python 内部字段名等,由于 GitHub 源文件无法直接抓取, **本次未能逐行核实** ,只作为背景理解,不能当作契约依赖。npm 上 `@modelcontextprotocol/sdk` 最新版为 1.30.1(来自 包列表)。 

- DeepWiki **等** AI **生成的代码解读** 权威性较低,只用于交叉印证(如 `getStreamIdForEventId` )。 

- **第三方博客** (dev.to、startdebugging、genalphai、bex.co、sunpeak 等)只用于补充背景,并已标注;其中关于 Cloudflare Agents SDK v0.20.0 弃用 `McpAgent` 的版本号来自第三方,Cloudflare 官方文档只确认了“deprecated and feature-frozen”。 Cloudflare Bex 

- **厂商引语** (Google、AWS、Cloudflare 等在 MCP 发布文章中的陈述)带有营销性质,性能或规模类表述(例如 Manufact 称包体积减少约 83%)没有经过独立验证。 

- **未覆盖项** :OpenAI Agents SDK / Responses API、Vercel mcp-handler、Java/Swift/PHP SDK 的现状,本次没有取得一手资料。 

- **时效** :所有结论以 2026 年 9 月 24 日为准。SDK 版本迭代很快(Python 在 2026 年 7~9 月已从 v2.0.0 发展到 v2.2.0),部署前请查阅对应 release notes。
