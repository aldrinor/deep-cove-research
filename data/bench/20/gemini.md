# **Anthropic Model Context Protocol (MCP)** 最新 **Streamable HTTP** 传输协议工程实现方案深度剖析 

## 引言：从有状态到无状态的架构演进与全景概览 

随着人工智能代理（ AI Agents ）与外部数据、工具集成的需求呈指数级增长， Anthropic 牵头开发的模型上下文协议（ Model Context Protocol, MCP ）已成为标准化大语言模型（ LLM ）与外部环境交互的核心通用协议。 MCP 的核心愿景是打造“AI 集成的 USB 接口”，通过统一的 JSON-RPC 2.0 消息格式，使各类 AI 应用能够无缝拔插到异构的数据源和工具链中<sup>1</sup> 。在 MCP 的早期迭代中，远程通信主要依赖于 HTTP + Server-Sent Events (SSE) 的双通道模式。该模式要求服务器在 /sse 端点维护一个长时间存活的 GET 连接用于单向消息推送，同时在 /message 端点接收客户端的 POST 请求<sup>4</sup> 。然而，这种有状态（ Stateful ）的设计在企业级分布式环境、负载均衡（ Load Balancing ）以及无服务器（ Serverless ）架构中引发了显著的扩展性瓶颈<sup>5</sup> 。由于会话状态与特定的服务器实例强绑定，任何网络闪断或容器自动缩放都会导致流中断，进而导致整个智能体工作流失败<sup>5</sup> 。 

为了彻底解决这一工程痛点并支撑千万级并发调用的企业级场景， Anthropic 在其 2026-07-28 发布的最新 MCP 规范中，全面重构了远程传输层，正式推出了无状态的 Streamable HTTP 传输协议（取代了 2024 年和 2025 年初期的有状态机制）<sup>8</sup> 。新的 Streamable HTTP 摒弃了强制性的长连接和协议级的 Mcp-Session-Id ，将所有的客户端与服务端交互整合为单一的 HTTP 端点，并通过“多轮往返请求”（ Multi Round-Trip Requests, MRTR ）机制优雅地解决了服务端反向发起请求（如人类在环确认、 LLM 采样）的难题<sup>9</sup> 。本研究报告将极其详尽地拆解 Streamable HTTP 的工程实现方案，涵盖其核心协议规范、网络架构演进、头部标准化、 MRTR 状态机流转，以及在 TypeScript 和 Python 生态中的 SDK 落地实践与代理网关配置。 

## 核心架构设计：单一端点与绝对无状态模型 

Streamable HTTP 传输模型的核心设计理念是“纯粹的 HTTP 化”与“绝对的无状态化”。在企业级部署中， stdio 传输模式虽然拥有极低的延迟（约 10 毫秒）和天然的进程隔离，但其“单用户单进程”的模型完全不适用于需要多租户共享内存状态（例如缓存 200MB 客户关系图谱）的广域网场景<sup>11</sup> 。 Streamable HTTP 正是为跨网络的企业级部署而生。在这一架构下， MCP 服务器作为一个独立进程运行，暴露唯一的 HTTP 端点（例如 https://api.example.com/mcp ），该端点严格仅接收 POST 请求（对于现代无状态客户端）<sup>8</sup> 。 

### 动态响应拓扑与连接生命周期 

客户端将每一个 JSON-RPC 请求或通知作为独立的 HTTP POST 报文发送<sup>8</sup> 。为了在不维持永久连接的前提下实现进度反馈， Streamable HTTP 采用了一种高度灵活的混合响应策略。服务器在接收到 POST 请求并完成鉴权后，会根据请求的执行性质动态决定响应的 Content-Type 。如果工具调用或资源读取可以立即同步完成，服务器会直接在 HTTP 200 OK 响应体中返回单个 application/json 格式的 JSON-RPC 响应对象<sup>8</sup> 。这种模式下的网络开销与传统的 RESTful API 完全一致。 

相对地，如果任务是长时间运行的（例如逐步返回的大规模数据搜索、长链条的推理任务，或需要 

不断下发 notifications/progress 进度通知），服务器则在当前 HTTP 请求的响应阶段，开启一个 Server-Sent Events (SSE) 流，将 Content-Type 设为 text/event-stream<sup>8</sup> 。这一流的生命周期极其短暂且严格闭环：它仅用于承载与当前触发该响应的 POST 请求强相关的通知消息，随后附带最终的 JSON-RPC 响应，响应送达后流即刻关闭<sup>8</sup> 。通过这种设计，服务器无需再为客户端分配和长期维持后台的 SSE 监听通道，所有的 SSE 都是请求作用域（ Request-Scoped ）内的按需建立，极大地释放了服务器的套接字资源。 

基础设施的安全与代理兼容性是 Streamable HTTP 落地时必须克服的障碍。规范对网络边界实施了严格要求。首先，为防御 DNS 重新绑定攻击（ DNS Rebinding Attacks ）， MCP 服务器在处理任何传入连接时，必须强制验证 Origin HTTP 头部。如果存在无效或不被信任的 Origin ，服务器必须 

立即以 HTTP 403 Forbidden 拒绝请求，且其响应体中可包含一个缺少 id 的 JSON-RPC 错误对象 8 。对于本地局域网环境运行的服务器，安全规范要求进程应当仅绑定至回环地址 127.0.0.1 ，而绝不可绑定至全网接口 0.0.0.0 ，从而避免被局域网内的恶意客户端横向探测与利用<sup>8</sup> 。此外，由于按需流式响应利用了分块传输编码（ Chunked Transfer Encoding ）和 SSE ， Nginx 、 Cloudflare 或企业内部的反向代理可能会对响应体进行缓冲，导致智能体的进度通知积压。因此，服务器实现中必须针对代理下发禁用缓冲的指令，如在响应头中显式添加 X-Accel-Buffering: no<sup>8</sup> 。为了防止中间网关因静默期而切断连接，服务器应周期性地向流中发送以冒号开头的 SSE 注释行（例如 :\r\n ）作为心跳保活信号（ Keep-Alives ），客户端在解析时被强制要求忽略这些无负载的注释行<sup>8</sup> 。在旧版协议中存在的 notifications/cancelled 客户端到服务端的通知仅在 stdio 中保留，在 Streamable HTTP 中，客户端直接断开 HTTP POST 请求底层的 TCP 连接（或关闭 SSE 响应流），服务器便应将其解释为取消信号，立即释放执行资源<sup>8</sup> 。 

## 协议深度重构：头部标准化与网关路由 **(SEP-2243)** 

为了使 API 网关（ Gateway ）、应用交付控制器（ ADC ）、 Web 应用防火墙（ WAF ）以及现代可观测性工具能够在不解析底层 JSON-RPC 负载（ Body ）的情况下对 MCP 流量进行精准路由、按量计费和限流， 2026 年的规范重构引入了 HTTP 头部标准化扩展（ SEP-2243 ）<sup>8</sup> 。这种元数据外提机制是企业级 API 设计的标准范式，使得底层网络设备可以高效工作。镜像元数据与严格的一致性校验 

客户端发送的每一次 HTTP POST 请求，都必须将其 JSON-RPC 负载中的核心元数据“镜像”提取到 HTTP 头部中<sup>8</sup> 。这种镜像机制并非可选，而是协议层面的强制要求。具体的映射与约束规则如表 1 所示。 

|必需头部名称|对应的**JSON-RPC**负载字<br>段|触发条件与描述|
|---|---|---|
|MCP-Protocol-Version|params._meta.io.modelcont<br>extprotocol/protocolVersion|必须存在于所有请求中（例<br>如2026-07-28）。若不支持<br>该版本，服务器返回400<br>Bad Request及<br>UnsupportedProtocolVersio<br>nError<sup>8</sup>。|
|Mcp-Method|method|必须存在于所有请求中，用<br>于指明当前操作类型（例如<br>tools/call, resources/read）<sup>8</sup><br>。|
|Mcp-Name|params.name或params.uri|当调用特定命名实体时必须<br>存在（例如tools/call,<br>prompts/get）<sup>8</sup>。|

为确保安全性，协议引入了严格的头部一致性验证机制。服务器在接收到请求时，必须校验 HTTP 

头部的值与 JSON-RPC 负载中的相应字段是否完全一致。如果一个恶意客户端试图在头部声明调用低权限工具以绕过网关路由，却在 Body 中试图执行高权限命令，服务器将会捕捉到这种不匹配，并必须立即返回 HTTP 400 Bad Request ，附带专用的 JSON-RPC 错误代码 -32020 (HeaderMismatch)<sup>8</sup> 。 

### 动态参数的 **Base64** 哨兵编码机制 **(x-mcp-header)** 

更为灵活的是， MCP 服务器可以通过在工具定义的 inputSchema 中扩展 x-mcp-header 属性，指示客户端将某些特定参数也提取至 HTTP 头部中。这在多租户环境中极具价值，例如将租户 ID 或特定的外部 API 密钥通过头部暴露给上游反向代理<sup>8</sup> 。此类自定义头部的格式为 Mcp-Param-{Name}: {Value}<sup>8</sup> 。 

然而， HTTP 头部对字符集有严格限制（必须符合 RFC 9110 规范，仅限可见 ASCII 字符 0x21–0x7E 和空格制表符，严禁包含 \r 、 \n 或 \0 等控制字符）<sup>8</sup> 。为此， Streamable HTTP 引入了一套严密的动态参数编码转换机制<sup>8</sup> 。对于原始类型，布尔值必须被转换为小写字符串 "true" 或 "false" ；整数被转换为十进制字符串（如 "42" ，且其范围限制在 JavaScript 安全整数内）；合法的 ASCII 字符串则保持原样<sup>8</sup> 。 

如果参数值包含非 ASCII 字符（如中文字符、 Emoji 表情）、包含前导或尾随空格，或者包含控制字符，客户端必须使用特殊的哨兵编码（ Sentinel Encoding ）对该值的 UTF-8 字节流进行 Base64 编码，其格式严格限定为： =?base64?{Base64EncodedValue}?=<sup>8</sup> 。为了避免混淆，即使是一个纯 ASCII 字符串，如果其内容恰好符合哨兵模式的字面量特征，客户端也必须对其进行二次 Base64 哨兵封装<sup>8</sup> 。服务器端在验证这些 Mcp-Param-* 及 Mcp-Name 头部时，被要求首先检查并剥离哨兵前缀，执行 Base64 解码，然后将解码后的原始值与 JSON-RPC 负载中的参数进行对比，任何解码失败或字符非法的请求均会触发 -32020 错误并被拦截<sup>8</sup> 。这一机制不仅确保了数据在复杂中间件链路中的无损传输，同时也杜绝了 HTTP 头部注入攻击（ Header Injection ）。 

## 无状态革命：多轮往返请求 **(MRTR / SEP-2322)** 

在 2026-07-28 版本重构之前，某些 MCP 核心功能严重依赖于长时间保持开启的 SSE 乃至 WebSocket 连接，尤其是客户端采样（ Sampling ，请求 LLM 生成补全）、根列表查询（ Roots ）和用户意图诱导（ Elicitation ，请求人类在环确认高危操作）。因为这些功能需要服务器向客户端“反向”发起请求，这在传统 HTTP 协议下是一个反向控制流难题<sup>9</sup> 。 

为了彻底移除服务器的内存状态负担， Anthropic 引入了多轮往返请求（ Multi Round-Trip Requests, 简称 MRTR ，规范号 SEP-2322 ），这构成了 Streamable HTTP 最为关键的范式转移<sup>10</sup> 。 **MRTR** 的状态机闭环流转 

在 MRTR 机制下，当客户端发起一个 HTTP POST 请求（如调用一个涉及核心数据库删除的工具 tools/call ）后，如果服务器发现执行该工具需要人类用户的明确授权，服务器不再挂起线程等待并通过独立流下发反向请求。相反，服务器直接终止当前的 HTTP 事务，向客户端返回一个类型为 input_required 的特殊响应对象（ InputRequiredResult ）<sup>8</sup> 。 

这个 InputRequiredResult 载荷中包含两个支撑无状态机制的关键字段：其一是 inputRequests ，这是一个包含了服务器具体需求的指令映射表（例如请求客户端立刻执行 elicitation/create 弹窗向用户确认）；其二是 requestState ，这是一个完全不透明（ Opaque ）的字节 Blob 。该 Blob 中封装了服务器未来恢复该工具调用所需的所有上下文，包括当前的执行代码指针、已经完成的部分计算结果、以及安全加密签名<sup>9</sup> 。 

客户端在收到此响应后，会在本地挂起原始逻辑流，弹窗询问用户或调用本地大语言模型生成下 

一步决策。一旦这些外部数据收集完毕，客户端会针对该工具发起一次全新的 **POST** 请求（且必须使用新的 **JSON-RPC ID** 以避免协议冲突）。在这次新请求的参数中，除了原有的参数外，客户端必须附加收集到的 inputResponses ，并将此前收到的 requestState 原封不动地带回<sup>8</sup> 。此时，负载均衡器可以将这个携带状态的重试请求发送到集群内的任意一个健康节点。该接收节点从中提取出 requestState ，解密验证无误后，瞬间恢复执行现场，执行删除操作，并返回最终具有 resultType: "complete" 的结果<sup>9</sup> 。这一全流程使得 MCP 服务器集群彻底摆脱了对 Redis 或 Memcached 等外部共享内存的依赖，实现了真正意义上的水平弹性伸缩<sup>20</sup> 。 

### 安全挑战与防重放机制 **(Replay Mitigation)** 

将应用状态卸载给不受信任的客户端虽然解决了服务器内存瓶颈，但却暴露了新的攻击面。恶意 

客户端可能会篡改 requestState 来绕过授权环节，或者截获一个合法的重试请求并进行重放攻击（ Replay Attacks ），试图导致服务器多次执行资金转账等高危操作<sup>22</sup> 。 

在工程实践中，服务器必须对 requestState 实施纵深防御策略。首先，状态 Blob 在发给客户端之前，服务器必须通过基于 HMAC 的加密算法对其进行签名保护，如果在重试请求中签名校验失败，必须立即终止执行<sup>22</sup> 。其次， requestState 内部必须强行嵌入发起操作的客户端身份标识（ Principal ）以及严格限制的生存时间戳（ TTL ）。如果重试请求中的认证身份与状态内封装的不符，或超过了容许的重试窗口，请求必须被丢弃<sup>22</sup> 。最后，为保证单次有效性（ Idempotency ），服务器后端应利用轻量级高可用的分布式去重缓存（如 Redis 短暂 Key ）记录已消费的原始请求 ID ，拒绝任何重复的 inputResponses 提交<sup>20</sup> 。 

## 核心语言 **SDK** 落地实践： **TypeScript** 与 **Python** 的架构重构 

为了支撑如此底层的网络模型变更， Anthropic 推出的官方 TypeScript 和 Python SDK 均在近期经历了彻底的代码库重构。特别是针对 Serverless 平台的适配， SDK 从底层抹除了对套接字状态的硬编码追踪<sup>24</sup> 。 

### **TypeScript SDK** ：向现代 **Web** 标准看齐的 **createMcpHandler** 

在早期的 TypeScript v1 版本（ @modelcontextprotocol/sdk ）中，开发者构建 Streamable HTTP 服务器需要手工实例化 StreamableHTTPServerTransport ，并通过在内存中维护复杂的 Map 结构来追踪每一个 Mcp-Session-Id 和底层的 SSE 发送流。一旦实例发生故障，内存态丢失将导致会话全部失效<sup>27</sup> 。 

在最新的 v2 架构（发布于 @modelcontextprotocol/server ）中，官方 SDK 直接废弃了内部的会话追踪，引入了面向 Serverless 范式的高阶工厂函数 createMcpHandler<sup>25</sup> 。这一设计将 MCP 抽象为了一个标准的 Web (Request) => Promise 函数，能够原生挂载至 Cloudflare Workers 、 Vercel 等 Fetch-compatible 边缘网络： 

<!-- Start of picture text -->
TypeScript<br>import { createMcpHandler, McpServer } from '@modelcontextprotocol/server';<br>import { toNodeHandler } from '@modelcontextprotocol/node';<br>import * as z from 'zod/v4';<br>//  核心范式：每次  HTTP  请求均触发工厂回调，做到绝对的无状态隔离<br>const handler = createMcpHandler(({ authInfo }) => {<br>const server = new McpServer({ name: 'enterprise-data-layer', version: '2.0.0' });<br>  server.registerTool(<br>'execute_transaction',<br>    { inputSchema: z.object({ amount: z.number() }) },<br>async (args) => {<br><!-- End of picture text -->

<!-- Start of picture text -->
//  依赖  authInfo  实现安全的租户级数据隔离<br>return { content: [{ type: "text", text: `Processed for ${authInfo?.clientId}` }] };<br>    }<br>  );<br>return server;<br>});<br>//  在  Node.js ( 如  Express  或原生  htp  t 模块 )  中通过  toNodeHandler  包装执行<br>const nodeHandler = toNodeHandler(handler);<br><!-- End of picture text -->

在这一范式下，工厂函数为每一个 _HTTP POST_ 请求创建一个全新的 McpServer 实例<sup>25</sup> 。由于框架假定实例会在请求结束后立即被垃圾回收，开发者被要求必须将连接池、 Token 验证器等持久化资源置于全局模块作用域，通过闭包传递给工具函数，以避免昂贵的实例化开销<sup>27</sup> 。同时，针对向后兼容性（ Backward Compatibility ），当配置了 legacy: 'stateless' 参数时， createMcpHandler 可以自动接管依然在发送旧版 initialize 握手请求的早期客户端（如 2025 年初的 Cursor 或 Claude Desktop 较早版本）。 SDK 采用无状态的方式模拟出握手响应，而不强求内存落地；反之，若配置为 legacy: 'reject' ，则服务器会果断拒绝任何非 2026-07-28 规范的调用，强制要求客户端升级<sup>26</sup> 。 

### **Python SDK** ：轻量级 **FastMCP** 与 **httpx2** 客户端注入 

在 Python 生态中， SDK (mcp) 被设计为通过高度集成的 FastMCP 提供类似 FastAPI 的开发者体验，极大降低了 Streamable HTTP 暴露的门槛<sup>29</sup> 。开发者通过装饰器定义工具和资源，而在启动时仅需配置传输层： 

<!-- Start of picture text -->
Python<br>from mcp.server.fastmcp import FastMCP<br>mcp = FastMCP(<br>    name="Logistics-AI-Gateway",<br>    host="127.0.0.1",<br>    port=8000<br>)<br>@mcp.tool(structured_output=True)<br>def query_inventory(sku: str) -> dict:<br>"""Fetch current inventory status."""<br>return {"sku": sku, "status": "in_stock", "qty": 42}<br>if __name__ == "__main__":<br>#  底层自动映射  HTTP  路由并处理  Streamable HTTP  特有的进度和事件流<br><!-- End of picture text -->

<mark>mcp.run(transport="streamable-htp"</mark> t <mark>, mount_path="/mcp")</mark> 

在客户端侧， Python SDK (mcp.client.streamable_http) 遵循依赖注入的设计模式。 SDK 本身并不内置 HTTP 客户端实现，而是提供 streamable_http_client 包装器，开发者必须自行维护和传入 httpx2.AsyncClient 实例<sup>31</sup> 。这种控制反转机制非常巧妙，使得上层企业应用可以完全接管请求的连接池、深层代理配置、自定义 Header （如企业防火墙特定的 Authorization: Bearer ）以及长轮询超时控制（如设置 timeout=httpx2.Timeout(30.0, read=300.0) ）<sup>31</sup> 。此外，该传输层实现了严格的安全重定向策略，仅追踪同源内的 HTTP 到 HTTPS 跳转或尾部斜杠重定向，拒绝任何可能导致数据泄露的跨源重定向<sup>31</sup> 。在错误处理方面，当遇到流中断时，底层 EventStore 能够尝试通过 replay_events_after 方法，依靠 Last-Event-ID 获取未送达的事件（尽管在最新的纯无状态实现中，重试已全面向 MRTR 转移）<sup>33</sup> 。 

## 企业级认证： **OAuth 2.1** 与 **RFC 9728** 保护资源元数据 

将大语言模型的工具层直接暴露于广域网，其安全风险是不可估量的。为此，最新的 Streamable HTTP 协议深度集成了一套基于 **OAuth 2.1** 与 **RFC 9728** (OAuth 2.0 Protected Resource Metadata) 的企业级鉴权工作流，这是 MCP 与传统简单的 API Key 认证最显著的分水岭<sup>1</sup> 。由于 MCP 的设计目标是让智能体能够按需发现和调用数以万计的异构系统，智能体无法提前预置每个系统的硬编码凭据，动态身份发现机制成为必需。 

标准化的鉴权发现流 

当一个未经授权的 AI 代理尝试向暴露的 /mcp 端点发送 POST 请求时， Streamable HTTP 服务器（借由如 mcp-auth 的集成包）会作为一台标准的 OAuth“资源服务器（ Resource Server ）”行事<sup>34</sup> 。此时，服务器拦截请求并返回标准的 HTTP 401 Unauthorized 状态码，在响应头中，服务器必须注入指向其受保护资源元数据的明确路径指针： WWW-Authenticate: Bearer 

resource_metadata="https://api.example.com/.well-known/oauth-protected-resource" [cite: 34, 36] 

智能体客户端捕获该 401 响应后，自动发起 GET 请求提取该 RFC 9728 元数据。这份 JSON 文档中声明了该 MCP 服务器信任的独立鉴权服务器（ Authorization Server ，例如企业的 Keycloak 或 Okta 集群），以及执行当前服务器内工具所必须申请的权限范围（ scopes_supported ，例如 mcp:tools:execute ）<sup>34</sup> 。 

接下来，智能体遵循 RFC 8414 标准解析鉴权服务器的元数据，并由于预先没有身份，采用动态客户端注册机制。 MCP 强烈推荐使用“客户端 ID 元数据文档（ Client ID Metadata Documents, CIMD ）”以替代复杂的 RFC 7591 注册。客户端将其自身的 HTTPS URL 作为 client_id ，鉴权服务器会直接抓取该 URL 验证应用的合法性并颁发凭证，实现了完全自动化的信任建立<sup>34</sup> 。最后，智能体必须通过包含证明密钥扩展（ PKCE ）的授权码模式（ Authorization Code Flow ），引导真实人类用户（ Human-in-the-loop ）在浏览器中完成同意，获取访问令牌（ Access Token ），将其置入 Authorization: Bearer 头部并重新发起 MCP 工具调用<sup>34</sup> 。此一闭环极大降低了零信任网络下 AI 工具集成的安全风险，并使得 verifyToken 等权限验证可以完全脱离业务代码，交由云原生的网关集中拦截处理<sup>35</sup> 。 

## 代理生态与协议选型博弈：为何弃用 **WebSockets** ？ 

随着 Streamable HTTP 的成熟，业界也随之诞生了 mcp-proxy 和 mcp-openapi-proxy 等关键中 

间件工具。这些代理不仅能够将内部的遗留 stdio 进程转译并多路复用到公网的 Streamable HTTP 端点，还通过 server/discover 端点集中聚合下层节点的能力暴露给外部大模型<sup>17</sup> 。针对不同的调用压力，这些代理实现了智能的自适应超时（ Adaptive Timeout ）：热点工具（并发 >20 ）限制在 5 分钟内执行，温点限制在 3 分钟，而冷点仅给 1 分钟<sup>17</sup> 。同时，网关层必须强制执行请求体大小限制（如 --maxBodySize 默认 10MB ）以防止恶意的超大负载击穿流处理器<sup>38</sup> 。在 MCP 标准演进期间，社区中曾爆发出关于传输层选型的激烈辩论。由于工具调用和大模型通信天然具有双向（ Bidirectional ）、低延迟的要求，部分开发者强烈建议将 WebSocket 作为官方首选网络层，批评 Streamable HTTP 过度复杂<sup>6</sup> 。然而， Anthropic 坚持用 Streamable HTTP 替代旧版的 SSE 并拒绝将 WebSocket 列为主线传输层。对比这两条技术路径，其工程权衡十分清晰： 

|评估维度|**WebSocket**协议|**Streamable HTTP**协议<br>**(2026**无状态规范**)**|
|---|---|---|
|认证与路由的标准化|鉴权手段受限。现代浏览器<br>及部分客户端框架无法在<br>WebSocket升级握手阶段附<br>加Authorization头部，常需<br>通过冗余的URL参数或在连<br>接建立后的第一次Payload<br>中传输Token，难以融入企<br>业网关的统一拦截链<sup>4</sup>。|极其标准。直接利用标准的<br>HTTP POST请求头，无缝融<br>入现有的WAF、ADC和零信<br>任网关，实施原生的HTTP<br>Bearer Auth<sup>4</sup>。|
|弹性扩展与内存状态|属于强状态协议（Stateful）。<br>客户端建立长连接后，整个<br>多轮对话的生命周期强绑定<br>在该服务器节点上。在云原<br>生自动扩容（Autoscaling）场<br>景下，无法做到即时驱逐或<br>跨节点负载均衡<sup>6</sup>。|绝对无状态（Stateless）。每<br>个tools/call请求都是相互<br>独立的，结合MRTR的状态<br>传递，负载均衡器可以将同<br>一个任务的不同步骤分发至<br>集群内任何空闲节点，大幅<br>降低分布式集群的管理复杂<br>度<sup>11</sup>。|
|基础设施兼容性|遇到深层企业级防火墙或某<br>些云提供商的陈旧代理网关<br>时，常常会遭遇HTTP<br>Upgrade失败、心跳探测不<br>均导致的强制超时切断<sup>40</sup>。|本质仍是纯粹的标准HTTP<br>POST/GET，无需特定的持续<br>保持策略，对全球所有云基<br>础设施完全透明。|

在面对海量企业级 AI 并发部署时，基于单向无状态请求的 HTTP 流能够将每一次推理或工具调用解构为完全隔离的无副作用操作，甚至能被直接持久化到事件流处理引擎（如 Apache Kafka ）中。这种解耦设计所带来的无穷运维弹性，是传统的双工长连接难以企及的。 

## 结语 

Anthropic 在最新版 Model Context Protocol 中大刀阔斧地推行 Streamable HTTP ，并引入具有 

革命性的多轮往返请求 (MRTR) ，标志着 AI 智能体的工具调用机制彻底跨越了本地受限、有状态耦合的极客实验阶段，正式踏入了可无限水平扩展、与现代云原生生态完美契合的企业级生产时代。 

通过将错综复杂的 SSE 长会话拆解转化为独立、纯净的 HTTP POST 端点调用，把身份认证委托给坚如磐石的 OAuth 2.1 鉴权网络，并将路由所需的核心元数据强制抽取到 HTTP 头部，最新规范确保了无论未来面临多大流量的 AI 代理高并发冲击，底层基础设施都能凭借现有的工具链提供无缝的弹性扩展与极高的安全性。这种坚决拥抱无状态互联网标准的设计哲学，将为下一代极度复杂的跨域多智能体协同、以及大规模人机深度在环（ Human-in-the-loop ）交互编排奠定最为坚实、也最具生命力的协议层根基。 

#### **Works cited** 

1. Unlocking Universal Data Access for AI with Anthropic's Model, <u>https://cube.dev/blog/unlocking-universal-data-access-for-ai-with-anthropics-m odel-context</u> 

2. How to Build a Custom MCP Server with TypeScript - freeCodeCamp, <u>https://www.freecodecamp.org/news/how-to-build-a-custom-mcp-server-withtypescript-a-handbook-for-developers/</u> 

3. Build an MCP Server in TypeScript: A Production Guide, <u>https://theroadtoenterprise.com/blog/build-mcp-server-typescript</u> 

4. SSE vs Streamable HTTP: Why MCP Switched Transport Protocols, <u>https://brightdata.com/blog/ai/sse-vs-streamable-http</u> 

5. Migrated MCP from SSE to Streamable HTTP - finally got multi-user, <u>https://www.reddit.com/r/ClaudeAI/comments/1qu43qt/migrated_mcp_from_sse_ to_streamable_http_finally/</u> 

6. Simplify HTTP transport with Websockets and stateless request, <u>https://github.com/modelcontextprotocol/modelcontextprotocol/issues/493</u> 

7. WebSockets and AI: Why LLMs Are Moving Beyond SSE, <u>https://websocket.org/guides/websockets-and-ai/</u> 

8. Streamable HTTP - What is the Model Context Protocol (MCP)?, <u>https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-h ttp</u> 

9. Stateless MCP: What the 2026-07-28 Spec Changes for Tool Builders, <u>https://skycloak.io/blog/stateless-mcp-2026-07-28-spec/</u> 

10. MCP Goes Stateless: What 2026-07-28 Changes | TensorFoundry, <u>https://tensorfoundry.io/blog/mcp-2026-07-28-stateless</u> 

11. MCP Stdio vs Streamable HTTP for Enterprise Deployments, 

   - <u>https://www.truefoundry.com/blog/mcp-stdio-vs-streamable-htpt</u> -enterprise 

12. Transports - What is the Model Context Protocol (MCP)?, <u>https://modelcontextprotocol.io/specification/2025-03-26/basic/transports</u> 

13. [docs?] nginx buffers query.live responses; needs X-Accel ... - GitHub, <u>https://github.com/sveltejs/kit/issues/15790</u> 

14. Releases · modelcontextprotocol/typescript-sdk - GitHub, <u>https://github.com/modelcontextprotocol/typescript-sdk/releases</u> 

15. SEP-2243: HTTP Header Standardization for Streamable HTTP, 

<u>https://modelcontextprotocol.io/seps/2243-http-standardization</u> 

16. MCP x-mcp-header Validation: Keep Bad Tool Schemas Out of tools, <u>https://dev.to/ssukhpinder/mcp-x-mcp-header-validation-keep-bad-tool-schema s-out-of-toolslist-3j3d</u> tps://mcp.avelino.run/guides/proxy-mode 

17. Proxy mode | mcp cli, https://mcp.avelino.run/guides/proxy-mode 

18. StreamableHTTP in depth · Model Context Protocol: Advanced topics, <u>https://academy.claude.com/courses/model-context-protocol-advanced-topics/s treamablehttp-in-depth</u> 

19. Announcing v2.0 of the official MCP C# SDK - .NET Blog, <u>https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csha rp-sdk/</u> 

20. Serverless MCP: Stateless Execution for Enterprise AI Tools - Workato, 

   - <u>https://www.workato.com/the-connector/serverless-mcp-for-enterprise-ai-tools/</u> 

21. Designing requestState for Multi Round-Trip Requests in MCP, tps://aaif.io/blog/designing-requeststate-for-multi-round-trip-requests 

   - <u>https://aaif.io/blog/designing-requeststate-for-multi-round-trip-requests</u> 

22. Implement SEP-2322: Multi Round-Trip Requests #2187 - GitHub, <u>https://github.com/modelcontextprotocol/typescript-sdk/issues/2187</u> 

23. How to Build and Deploy an MCP Server to Production (2026-07-28, <u>https://composio.dev/content/how-to-build-and-deploy-an-mcp-server-to-prod uction</u> 

24. python-sdk - MCP Servers on GitHub (24.2k ) | SkillsLLM, <u>https://skillsllm.com/skill/python-sdk</u> 

25. MCP v2 SDK: Build a Server in TypeScript - Agentailor, tps://blog.agentailor.com/posts/build-an-mcp-v2-server-typescript 

   - <u>https://blog.agentailor.com/posts/build-an-mcp-v2-server-typescript</u> 

26. Migrate Sessions to Stateless Requests with MCP 2026-07-28, <u>https://aaif.io/blog/migrate-sessions-to-stateless-requests-with-mcp-2026-07-2 8</u> 

27. Serve over HTTP | MCP TypeScript SDK, <u>https://ts.sdk.modelcontextprotocol.io/v2/serving/http.html</u> 

28. StreamableHTTPServerTransport has no public API to reconstruct a, <u>https://github.com/modelcontextprotocol/typescript-sdk/issues/1658</u> 

29. Practical Guide to MCP (Model Context Protocol) in Python, <u>https://dev.to/m_sea_bass/practical-guide-to-mcp-model-context-protocol-in-p ython-ijd</u> 

30. Building Production-Ready MCP Server with Streamable-HTTP, <u>https://medium.com/@nsaikiranvarma/building-production-ready-mcp-server-wi th-streamable-http-transport-in-15-minutes-ba15f350ac3c</u> 

31. Client transports - MCP Python SDK, <u>https://py.sdk.modelcontextprotocol.io/client/transports/</u> tps://py.sdk.modelcontextprotocol.io/client/ 

32. The Client - MCP Python SDK, <u>https://py.sdk.modelcontextprotocol.io/client/</u> 

33. streamable_http - MCP Python SDK, tps://py.sdk.modelcontextprotocol.io/v2/api/mcp/server/streamable_http/ tp/ 

   - <u>https://py.sdk.modelcontextprotocol.io/v2/api/mcp/server/streamable_http/</u> 

34. MCP Authentication: OAuth 2.1 in MCP Explained - Authgear, <u>https://www.authgear.com/post/mcp-authentication/</u> tps://mcp-auth.dev/docs 

35. Get started - MCP Auth, <u>https://mcp-auth.dev/docs</u> 

36. OAuth on MCP: The Comprehensive Implementation Guide - Permit.io, <u>https://www.permit.io/blog/oauth-on-mcp</u> 

37. Build with the TypeScript SDK - MCP Manager, <u>https://docs.mcpmanager.ai/build-your-own-mcp-server/typescript</u> 

38. punkpeye/mcp-proxy: A TypeScript streamable HTTP and ... - GitHub, <u>https://github.com/punkpeye/mcp-proxy</u> tps://pypi.org/project/mcp-openapi-proxy/ 

39. mcp-openapi-proxy - PyPI, <u>https://pypi.org/project/mcp-openapi-proxy/</u> 

40. Is SSE breaking your AI chat experience? Here are your alternatives, <u>https://ably.com/topic/sse-alternatives-ai-chat</u>
