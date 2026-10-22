# Anthropic MCP Streamable HTTP 传输协议工程实现与架构演进深度研究报告

## 协议演进背景与单端点架构范式重构

模型上下文协议（Model Context Protocol, MCP）作为连接大语言模型（LLM）与外部工具、数据源及上下文环境的标准化接口，其底层传输层（Transport Layer）的架构设计直接决定了智能体系统在企业级云原生环境中的可扩展性、网关兼容性与连接可靠性 [1](https://aipx.app/technologies/mcp-streamable-http)。在 MCP 规范演进历程中，Anthropic 推动了从早期双端点 `HTTP+SSE`（协议版本 `2024-11-05`）向单端点 `Streamable HTTP`（协议版本 `2025-03-26` 引入，并在 `2026-07-28` 版本完成无状态化重构）的根本性架构跃迁 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。

在 `2024-11-05` 规范定义的 `HTTP+SSE` 传输模型下，客户端与远程服务端的通信必须在两个独立的 HTTP 端点上同时维护两条生命周期迥异的网络连接 [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/)。客户端首先通过 `HTTP GET` 连接服务端的 `/sse` 端点以建立持久化 Server-Sent Events（SSE）下行流；服务端随后在该流的首个事件中下发 `endpoint` 事件，告知客户端包含专属会话标识的指令上行地址（例如 `/messages?client_id=...`）；此后客户端必须通过独立的 `HTTP POST` 请求向 `/messages` 发送所有 JSON-RPC 指令，而响应报文与通知则异步通过初始的 `/sse` 通道回传 [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/)。

这种读写分离的双通道架构在生产工程实践中暴露出严重的结构性缺陷。首先，服务端必须在进程内存中维护跨端点的连接状态映射表（In-Memory Session State），这种强制性的有状态绑定导致请求无法经过标准的无状态七层负载均衡器（L7 Gateway）自由分发，任何容器扩缩容或网关重路由均会造成上下文断裂 [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/)。其次，企业级代理与中间件（如 Envoy、Nginx、Cloudflare 边缘节点及云厂商 ALB）普遍对空闲长连接施加严格的超时裁剪策略，强制前置的 `/sse` 握手机制极易因公网抖动而中断，且缺乏原生的断线重连与事件重放机制 [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/)。此外，在 AWS Lambda、Cloudflare Workers 或 Azure Container Apps 等按需唤醒的无服务器（Serverless）计算架构中，维持常驻的 `/sse` 监听连接在计费模型与容器生命周期管理上完全不可行 [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/)。最后，客户端协议栈必须先解析控制流事件以完成动态路由发现，随后才能发起业务调用，这违背了标准 HTTP 请求-响应的自包含语义并大幅增加了客户端的实现复杂度 [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/)。

为彻底解决上述工程痛点，MCP `2025-03-26` 规范正式引入 `Streamable HTTP`（传输标识符为 `streamable-http`）以替代被弃用的 `HTTP+SSE` [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。`Streamable HTTP` 将所有客户端到服务端的通信收敛至单一的统一 HTTP 端点（通常命名为 `/mcp` 或 `/message`），使流量能够无缝穿过标准七层网关并分发至后端的无状态 MCP 服务集群 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。客户端通过标准 `HTTP POST` 直接向该统一端点发送 JSON-RPC 消息，由服务端根据当次交互的实际计算特征，在单次请求生命周期内动态决定是直接返回 `200 OK (application/json)` 标准响应，还是将该次 `POST` 响应原地升级（Upgrade）为作用域仅限于当前请求的 `200 OK (text/event-stream)`（SSE）流 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。

随着协议演进至最新的 `2026-07-28` 规范版本（对应 SEP-1442、SEP-2243、SEP-2322 与 SEP-2575 提案），`Streamable HTTP` 进一步剥离了 `2025-03-26` 过渡期残留的有状态会话耦合，确立了默认全无状态（Stateless by Default）的现代工程架构 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。在 `2026-07-28` 架构下，协议不再依赖隐式的会话级 `GET` 反向通道下发服务端请求，而是通过多轮往返请求（Multi Round-Trip Requests, MRTR）模式处理人机交互（Elicitation）、根目录查询（Roots）及采样（Sampling），并通过显式的 `subscriptions/listen` 请求流承载服务端变更通知，同时将核心 JSON-RPC 元数据镜像至 HTTP 标准请求头以赋能云原生网关路由 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。

为清晰界定不同协议世代在工程实现上的边界，下表对 MCP 三代 HTTP 传输规范的核心技术特征进行了结构化对比：

| 架构维度 | HTTP + SSE (`2024-11-05`) | Streamable HTTP 有状态期 (`2025-03-26`) | Streamable HTTP 现代无状态期 (`2026-07-28`) |
| --- | --- | --- | --- |
| **服务端暴露端点** | 双端点：`/sse`（下行事件流）与 `/messages`（上行指令） [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/) | 单一统一端点（如 `/mcp`），支持 `POST`、`GET`、`DELETE`[cite: 22, 23, 24] | 单一统一端点（如 `/mcp`），全通信收敛为 `POST` 请求 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) |
| **端点发现机制** | 强制通过 `/sse` 首帧 `endpoint` 事件动态下发 POST URI [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/) | 无需发现，客户端直接向 `/mcp` 发送请求 [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/) | 无需发现，客户端直接向 `/mcp` 发送请求 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) |
| **会话状态与能力协商** | 强依赖内存长连接状态，无法无状态化 [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/) | 通过 `initialize` 握手生成 `Mcp-Session-Id`；支持可选无状态模式 [2](https://glama.ai/blog/2026-01-02-what-is-streamable-http-in-mcp) | 默认全无状态（SEP-1442）；客户端在每次请求体中声明 `clientCapabilities`[cite: 7, 20, 25] |
| **服务端主动调用客户端** | 通过 `/sse` 下发请求，客户端向 `/messages` POST 响应 [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/) | 通过独立 `GET /mcp` SSE 流或升级流下发请求，依赖 `Mcp-Session-Id` 拼接响应 [24](https://github.com/modelcontextprotocol/typescript-sdk/issues/451) | 采用 MRTR（SEP-2322）模式：返回 `InputRequiredResult`，由客户端携带 `inputResponses` 重试 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) |
| **服务端变更通知机制** | 混杂于全局 `/sse` 连接中推送 [8](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/) | 客户端发起空 `GET /mcp` 维持 `_GET_stream` 独立长连接接收通知 [16](https://github.com/modelcontextprotocol/typescript-sdk/issues/220) | 客户端显式发送 `POST subscriptions/listen` 过滤订阅，响应流携带 `_meta.subscriptionId`[cite: 4, 21, 28, 29] |
| **七层网关可观测性** | 网关仅见 `/messages` 路径，必须反序列化 JSON 体才能获知方法名 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) | 依赖 `Mcp-Session-Id` 路由，方法与工具名仍隐藏在 JSON-RPC 载荷中 [2](https://glama.ai/blog/2026-01-02-what-is-streamable-http-in-mcp) | 强制执行 SEP-2243：将方法名、资源/工具名及指定参数镜像至 `Mcp-Method`、`Mcp-Name`、`Mcp-Param-*` 请求头 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) |

## 核心通信机制与底层报文流转规范

在工程落地层面，`Streamable HTTP` 的核心设计在于将复杂的双向异步智能体交互解构为符合标准 HTTP 语义的报文流。服务端作为一个独立运行的进程，通过单一 MCP 端点并发处理来自多个客户端的连接请求 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。

### 单端点动态响应升级机制

客户端发起的所有 JSON-RPC 请求（Request）或通知（Notification）均作为独立的 `HTTP POST` 请求发送至 `/mcp` 端点，现代规范明确禁止客户端在请求体中发送 JSON-RPC Response，也不再推荐使用导致反序列化与类型判别模糊的 JSON-RPC Batch 数组 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。在每一次 `POST` 调用中，客户端必须在 HTTP 请求头中显式携带 `Accept: application/json, text/event-stream` 以及 `Content-Type: application/json` [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。这一双 MIME 类型声明是协议层的硬性契约，它赋予了服务端在运行时根据工具执行耗时与流式反馈需求，单方面决定响应格式的自由度 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。

当服务端接收到 `POST` 请求后，其内部状态机根据报文类型与执行逻辑分化为三种处理路径。在第一种路径下，若请求体为不包含 `id` 字段的客户端 JSON-RPC 通知（如 `notifications/initialized` 或 `notifications/cancelled`），服务端在校验并接纳后必须立即返回状态码 `202 Accepted` 且响应体严格为空（No Body）；若服务端拒绝或无法解析该通知，则必须返回 `400 Bad Request` 等 4xx 错误状态码，并可在响应体中附带一个 `id` 为 `null`（或无 `id`）的 JSON-RPC Error 对象 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。在第二种路径下，当客户端发起 `tools/list`、`prompts/get` 或轻量级 `tools/call` 请求，且服务端无需在执行期间推送中间进度或日志时，服务端直接走同步单次 JSON 响应（Simple Response），返回 `200 OK` 与 `Content-Type: application/json` [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。此处的工程规范要求响应体必须是一个完整封装的 `JSONRPCResponse` 对象（即包含 `"jsonrpc": "2.0"`、`"id"` 与 `"result"` 字段），绝对不能直接返回裸露的 `Result` 业务数据结构 [34](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1398)。在第三种路径下，当 `tools/call` 触发长耗时任务（如代码沙箱执行、自动化云部署或深度检索），需要向客户端实时反馈进度条（`notifications/progress`）或调试日志（`notifications/message`）时，服务端返回 `200 OK` 并将响应头设为 `Content-Type: text/event-stream` [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。此时连接原地升级为一条作用域严格限定于当前请求（Scoped to this request）的 SSE 流 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。服务端在该流中依次推入关联于当前请求的 JSON-RPC 通知事件，最后推入携带最终结果的 `JSONRPCResponse` 事件，随后立即由服务端主动关闭该 SSE 流 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。这种“按请求开启、用完即关”的短生命周期流设计，既保留了实时流式体验，又彻底规避了全局长连接导致的负载均衡器粘滞问题 [7](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/282)。

### 多轮往返请求模式（MRTR）与零信任状态机实现

在标准 HTTP 拓扑中，服务端拥有固定 URI 而客户端通常位于 NAT、防火墙或浏览器沙箱之后，服务端无法主动向客户端发起反向 HTTP 连接 [36](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-streamablehttp-transport)。在 `2025-03-26` 版本中，若服务端在执行工具期间需要向客户端请求信息——例如发起用户表单确认（Elicitation, `elicitation/create`）、获取工作区根目录（Roots, `roots/list`）或借用客户端大模型进行采样生成（Sampling, `sampling/createMessage`）——服务端必须将原本单向的 SSE 流作为反向通道下发 JSON-RPC Request，再挂起当前协程等待客户端通过另一个 `HTTP POST` 回传 JSON-RPC Response，最后利用 `Mcp-Session-Id` 将两个跨连接的异步操作缝合在一起 [11](https://gofastmcp.com/deployment/http)。这种设计不仅在多副本 Kubernetes 集群中极难实现（回调 POST 极易落到未持有挂起协程的其他 Pod 上），而且迫使基础设施维护昂贵的有状态会话 [9](https://github.com/modelcontextprotocol/typescript-sdk/issues/340)。

为此，MCP `2026-07-28` 规范正式确立了多轮往返请求（Multi Round-Trip Requests, MRTR / SEP-2322）模式，将服务端到客户端的反向调用彻底改造为客户端驱动的“中断-续传（Continuation）”状态机 [3](https://ai.engineer/topics/model-context-protocol)。当服务端在处理 `tools/call`、`prompts/get` 或 `resources/read`（假设初始请求 JSON-RPC `id: 1`）过程中发现缺少必要信息时，服务端不再挂起连接等待回调，而是直接结束当前 HTTP 响应，返回一个类型为 `InputRequiredResult` 的结果对象 [3](https://ai.engineer/topics/model-context-protocol)。该对象包含 `inputRequests` 与可选的 `requestState` 两个核心字段：其中 `inputRequests` 是一个由服务端分配唯一键名（Key）的键值映射表（Map），其值为具体的服务端请求对象（仅限 `ElicitRequest`、`ListRootsRequest` 或 `CreateMessageRequest`；需要注意 `sampling/createMessage` 在 `2026-07-28` 规范中已被标记为弃用，保留至少 12 个月兼容期，推荐新系统直接调用模型供应商 API，但存量集成仍通过 MRTR 承载）；而 `requestState` 则是一个不透明字符串（Opaque Blob），用于序列化服务端在中断点的执行上下文 [3](https://ai.engineer/topics/model-context-protocol)。

客户端收到 `InputRequiredResult` 后，在本地完成相应的信息采集——例如弹出 Form 模式表单收集非敏感结构化参数（规范严禁在 Form 模式中索要密码、访问令牌、API 密钥或支付凭证），或引导用户通过 URL 模式完成外部授权，或查询本地 Roots 权限 [3](https://ai.engineer/topics/model-context-protocol)。随后，客户端必须使用全新的 JSON-RPC `id`（如 `id: 2`）重新向 `/mcp` 发起原始请求 [3](https://ai.engineer/topics/model-context-protocol)。重试请求的 `params` 在保留原始调用参数的基础上，追加 `inputResponses` 映射表（键名与 `inputRequests` 严格一一对应，值为 `ElicitResult`、`ListRootsResult` 等）并原样回传（Echo）`requestState` 字符串 [3](https://ai.engineer/topics/model-context-protocol)。若用户在客户端拒绝或取消了交互，由于服务端并未阻塞等待，客户端无需发送错误回包，直接放弃重试即可；反之，若客户端重试时遗漏了部分必填的 `inputRequests` 项，服务端应再次返回新的 `InputRequiredResult` 继续追问，而非直接报错中断 [27](https://modelcontextprotocol.io/specification/draft/basic/patterns/mrtr)。

在工程实现中，由于 `requestState` 经由客户端回传，服务端必须将其视为不可信的攻击者可控输入（Attacker-Controlled Input） [3](https://ai.engineer/topics/model-context-protocol)。若服务端直接反序列化明文 `requestState`，恶意或被劫持的客户端可通过篡改状态字段绕过权限校验、重放跨会话指令或破坏服务端业务逻辑 [27](https://modelcontextprotocol.io/specification/draft/basic/patterns/mrtr)。因此，生产级服务端实现必须对 `requestState` 实施加密与完整性签名（如使用 AES-GCM 或 HMAC-SHA256），并在载荷中强制绑定调用者主体身份（Principal ID）、原始请求方法与参数哈希、短期过期时间戳（Expiry）以及一次性防重放随机数（Single-use Nonce），在每次续传请求到达时执行严格的零信任复核 [3](https://ai.engineer/topics/model-context-protocol)。

### 服务端变更通知流（`subscriptions/listen`）

针对工具列表动态增删（`notifications/tools/list_changed`）、提示词变更或资源内容更新（`notifications/resources/updated`）等服务端主动推送场景，现代规范（SEP-2575）废弃了 `2025-03-26` 时期语义模糊的空 `GET /mcp` 监听流，转而引入显式的 `POST subscriptions/listen` 协议方法 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。需要接收变更通知的客户端向 `/mcp` 端点发送 `POST subscriptions/listen` 请求，并在参数中声明订阅过滤器（例如指定 `tools_list_changed=True` 或传入关注的 `resource_subscriptions` URI 列表） [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。

服务端在校验客户端访问令牌对目标 URI 的读取权限后，会将该请求的 SSE 响应流长期保持开启 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。在底层帧协议上，流建立后的第一帧必须立即下发 `notifications/subscriptions/acknowledged` 事件，向客户端确认订阅流已就绪 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。此后，流上推送的每一条通知帧均必须在 `_meta` 字段中携带开启该流的原始请求 ID（如客户端生成的 `"listen-1"`），其标准格式为 `"_meta": {"io.modelcontextprotocol/subscriptionId": "<listen_request_id>"}` [28](https://py.sdk.modelcontextprotocol.io/handlers/subscriptions/)。工程设计上必须明确的是，`subscriptions/listen` 响应流仅作为“缓存失效信令（Cue to Refetch）”而非业务数据载体，且绝不是历史事件重放日志（Replay Log）——连接断开期间发生的事件不会被队列缓存，客户端收到变更事件后必须主动重新调用 `tools/list` 或 `resources/read` 拉取最新全量状态 [28](https://py.sdk.modelcontextprotocol.io/handlers/subscriptions/)。当服务端需要主动优雅终止订阅流时，会将原始 `subscriptions/listen` 请求的 JSON-RPC Result 作为最后一帧发出，随后关闭连接 [28](https://py.sdk.modelcontextprotocol.io/handlers/subscriptions/)。

### 请求元数据 HTTP 头镜像规范（SEP-2243）

在大型企业微服务网格中，API 网关、七层负载均衡器与 OpenTelemetry 可观测性组件通常不具备解析或解压缩 HTTP 请求体以提取 JSON-RPC 字段的能力，或者在高吞吐场景下解析请求体的 CPU 开销过高 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。为此，`Streamable HTTP` 规范（通过 SEP-2243 标准化）强制要求客户端将关键请求元数据镜像至 HTTP 请求头中，同时支持服务端通过 JSON Schema 扩展注解提取业务参数 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。

在基础协议头方面，客户端必须在每个 `POST` 请求中携带 `Mcp-Method`（其值严格对应 JSON-RPC 请求体中的 `method`，如 `tools/call`）与 `MCP-Protocol-Version`（其值必须与请求体中的 `io.modelcontextprotocol/protocolVersion` 严格一致，否则服务端必须返回 `400 Bad Request`；若版本不受支持则返回 `UnsupportedProtocolVersionError`） [18](https://github.com/modelcontextprotocol/typescript-sdk/issues/2176)。当调用涉及具体目标名称或资源 URI 时（涵盖 `tools/call` 与 `prompts/get` 中的 `params.name`，以及 `resources/read`、`resources/subscribe` 与 `resources/unsubscribe` 中的 `params.uri`），客户端还必须在请求头中附带 `Mcp-Name` [18](https://github.com/modelcontextprotocol/typescript-sdk/issues/2176)。此外，在 `2026-07-28` 无状态规范下，客户端在每次请求体中通过 `io.modelcontextprotocol/clientCapabilities` 按请求（Per-request）声明自身能力，并通过 `io.modelcontextprotocol/clientInfo` 报告客户端软件名称与版本（仅作日志与调试用途，服务端严禁将其用于安全决策） [25](https://modelcontextprotocol.io/specification/2026-07-28/schema)。

在工具参数头映射方面，服务端在定义工具的 `inputSchema`（默认遵循 JSON Schema `2020-12` 规范）时，可在特定属性上声明 `x-mcp-header` 扩展注解，指示客户端将该参数值同步镜像至 `Mcp-Param-<HeaderName>` 请求头中 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。为防范 HTTP 响应拆分与头部注入攻击（Header Injection），规范对此施加了严苛的工程约束：`x-mcp-header` 仅允许应用于基本类型（`string`、`integer`、`boolean`），严禁应用于浮点数类型（`number`）或复杂对象与数组 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。在类型转换与编码时，`string` 保持原值，`integer` 必须转换为十进制字符串表示（如 `"42"` 或 `"-7"`），`boolean` 必须强制转换为全小写 `"true"` 或 `"false"` [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。同时，同一 `inputSchema` 内所有 `x-mcp-header` 名称必须在大小写不敏感（Case-insensitively）的前提下保持唯一，且转换后的参数值严禁包含任何控制字符（特别是回车符 `CR \r` 与换行符 `LF \n`），客户端在写入请求头前必须执行安全编码校验 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。

<!-- figure 1: interactive chart embedded in the report; its text content follows -->

### Streamable HTTP 线网层交互流与 **Header Mirroring**  契约仿真器

RFC 级微架构解构 · SEP-2243 标头镜像 · SEP-2322 MRTR 多轮状态 · SEP-2575 订阅流

选择线网交互模式 (Wire Message Pattern)

✦

1. 同步 JSON 响应 · 协议运作机制 客户端发起单次 HTTP POST 请求执行工具，服务端完成计算后直接以 HTTP 200 及 application/json 单对象应答。

2 轮报文交换

交互时序与封包流 (Wire Interaction Steps) Step 1 of 2

STEP 01 Client

Client POST

Initiate Request  REQ

STEP 02 Server

Server 200 OK

Direct JSON  RES

POST /mcp HTTP Wire Headers

Client ➔ Server

标头名 (Header Key) 线路值 (Wire Value)

Host:api.mcp-hub.internal:8080

Content-Type:application/json

Accept:

application/json, text/event-stream 强制双通支持

Origin:

https://agent.enterprise.internal DNS Rebinding 校验

MCP-Protocol-Version:2026-07-28

Mcp-Method: SEP-2243 镜像头

tools/call

Mcp-Name: SEP-2243 镜像头

query_database

Mcp-Param-cluster: SEP-2243 镜像头

prod-eu-db1

💡 SEP-2243 标头镜像价值： 当前请求包含 **Mcp-Method**  / **Mcp-Name**  / **Mcp-Param-***  镜像头！现代 API 网关可在毫秒内按 HTTP Header 执行路由限流，规避解析大体积 JSON Body 的巨额 CPU 消耗。

JSON-RPC 2.0 Request Envelope

application/json

```
{
  "jsonrpc": "2.0",
  "id": "call-901",
  "method": "tools/call",
  "params": {
    "name": "query_database",
    "arguments": {
      "cluster": "prod-eu-db1",
      "sql": "SELECT count(*) FROM billing_ledger WHERE year = 2026;"
    },
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientInfo": {
        "name": "EnterpriseAgentRunner",
        "version": "2.4.0"
      }
    }
  }
}
```

⚙️ 客户端必须在 Accept 头同时声明 application/json 与 text/event-stream，以赋予服务端按需选择流式或同步返回的自主权。

Streamable HTTP 状态码规约与故障转移矩阵 (7 大核心状态) 点击任意卡片查看容灾与修复契约

202

Accepted

收到有效的

400

Bad Request

缺少

403

Forbidden

Origin

404

Not Found

Mcp-Session-Id

405

Method Not Allowed

客户端使用

406

Not Acceptable

Accept

415

Unsupported Media

请求的

202 Accepted 收到有效的 JSON-RPC Notification (无 id 请求)

客户端发送的通知无需等待执行结果。服务端若成功校验接纳，必须返回 202 Accepted 且响应体必须为空 (No body)。

客户端动作 (Client Recovery) 无阻塞状态，客户端继续向后执行后续调度流水线。

交互式 MCP Streamable HTTP 传输协议仿真器。点击选择不同的交互模式，即可实时观察底层 HTTP 请求头、JSON-RPC 请求/响应载荷、SEP-2243 头部镜像（Header Mirroring）以及服务端状态机在同步调用、SSE 进度流、MRTR 多轮会话及变更订阅下的精确线网行为。

数据来源: [MCP Streamable HTTP 规范](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http), [SEP-2322 MRTR 提案](https://modelcontextprotocol.io/seps/2322-MRTR), [TypeScript SDK (SEP-2243)](https://github.com/modelcontextprotocol/typescript-sdk), [Python SDK StreamableHTTP](https://github.com/modelcontextprotocol/python-sdk)

<!-- /figure 1 -->

为确保网关与服务端研发团队在实现协议解析器时的严谨性，下表汇总了 `Streamable HTTP` 规范中所有关键 HTTP 状态码与请求头的工程语义及强制校验逻辑：

| 类别 | 标识符 / 状态码 | 触发条件与协议约束 | 服务端 / 客户端强制行为规范 |
| --- | --- | --- | --- |
| **HTTP 请求头** | `Accept` | 客户端每次发起 `POST /mcp` 请求时必须包含 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) | 必须同时列出 `application/json` 和 `text/event-stream`，缺一不可 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) |
| **HTTP 请求头** | `Mcp-Method` | SEP-2243 强制标准头，每次 `POST` 请求必传 [18](https://github.com/modelcontextprotocol/typescript-sdk/issues/2176) | 镜像 JSON-RPC 请求体中的 `method` 字段；严格模式下缺失则返回 `400`[cite: 18] |
| **HTTP 请求头** | `Mcp-Name` | 当请求包含 `params.name` 或 `params.uri` 时必传 [18](https://github.com/modelcontextprotocol/typescript-sdk/issues/2176) | 供七层网关识别具体调用的工具名（`tools/call`）、提示词或资源 URI [18](https://github.com/modelcontextprotocol/typescript-sdk/issues/2176) |
| **HTTP 请求头** | `Mcp-Param-*` | 工具 `inputSchema` 属性包含 `x-mcp-header` 注解时触发 [30](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/protocol-eras) | 仅支持 `string`、`integer`、`boolean`；严禁包含 `\r`、`\n` 控制字符 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) |
| **HTTP 请求头** | `Mcp-Session-Id` | 2025 有状态模式下由服务端在 `initialize` 响应头中签发 [24](https://github.com/modelcontextprotocol/typescript-sdk/issues/451) | 客户端后续请求须全程携带；浏览器跨域场景必须在 CORS `exposedHeaders` 中暴露 [24](https://github.com/modelcontextprotocol/typescript-sdk/issues/451) |
| **HTTP 状态码** | `202 Accepted` | 客户端发送合法的 JSON-RPC Notification（无 `id`） [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) | 服务端必须返回空响应体（No Body），不得返回 JSON 对象 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) |
| **HTTP 状态码** | `400 Bad Request` | JSON-RPC 格式错误、缺失必填头或协议版本头与请求体不一致 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) | 客户端视为请求构造错误，不应盲目重置会话，而应报错或修正参数 [46](https://github.com/modelcontextprotocol/python-sdk/issues/1727) |
| **HTTP 状态码** | `403 Forbidden` | 请求包含非法的 `Origin` 头（DNS 重绑定攻击防护触发） [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) | 服务端必须拒绝连接并返回 `403`；响应体可包含无 `id` 的 JSON-RPC Error [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) |
| **HTTP 状态码** | `404 Not Found` | 客户端携带了未知、已过期或已销毁的 `Mcp-Session-Id`[cite: 46, 47] | 客户端收到 `404` 后必须丢弃旧 Session ID 并重新发送无 ID 的 `InitializeRequest`[cite: 46] |
| **HTTP 状态码** | `405 Method Not Allowed` | 客户端发送 `PUT`/`PATCH`，或在不支持独立 SSE 流的服务器上发送 `GET /mcp`[cite: 24, 48] | 服务端必须显式返回 `405`（附 `Allow: GET, POST, DELETE`），避免客户端初始化挂起 [24](https://github.com/modelcontextprotocol/typescript-sdk/issues/451) |
| **HTTP 状态码** | `406 Not Acceptable` | 客户端 `Accept` 头未同时包含 JSON 与 SSE 两种媒体类型 [33](https://github.com/modelcontextprotocol/python-sdk/issues/1363) | 服务端拒绝处理请求并快速返回；需注意异步流关闭竞态 [33](https://github.com/modelcontextprotocol/python-sdk/issues/1363) |

## 官方 SDK 工程实现方案与核心代码架构

在实际工程落地中，Anthropic 与开源社区维护的官方多语言 SDK（涵盖 TypeScript、Python、C# 与 Go）已围绕 `Streamable HTTP` 构建了完备的分层传输抽象 [2](https://glama.ai/blog/2026-01-02-what-is-streamable-http-in-mcp)。不同技术栈在底层 I/O 模型（如 Node.js Streams、Web Standard Fetch API、Python ASGI 与 `anyio` 内存通道）上的差异，决定了各自独特的工程实现范式。

### TypeScript SDK 架构与工程实现方案

TypeScript SDK（`@modelcontextprotocol/sdk` 及 v2 模块化包 `@modelcontextprotocol/server`、`@modelcontextprotocol/express`、`@modelcontextprotocol/hono`）在传输层采用了双层适配器架构 [23](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/legacy-routing/README.md)。其底层核心引擎为 `WebStandardStreamableHTTPServerTransport`，完全基于 W3C Web Standard 的 `Request`、`Response` 与 `ReadableStream` API 构建，原生兼容 Cloudflare Workers、Deno、Bun 以及 Hono 等现代边缘计算运行时，并在内部集成了 `maxBodyBytes` 请求体大小防护守卫以抵御内存耗尽型拒绝服务攻击 [23](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/legacy-routing/README.md)。在其之上，`NodeStreamableHTTPServerTransport`（在主包中亦导出为 `StreamableHTTPServerTransport`）封装了针对 Node.js 标准 `http.IncomingMessage` 与 `http.ServerResponse`（以及 Express 框架 `req`/`res`）的流式桥接逻辑 [24](https://github.com/modelcontextprotocol/typescript-sdk/issues/451)。

在 TypeScript 工程实现中，最关键的架构铁律是严禁跨请求或跨会话复用同一个 `McpServer` 或 `StreamableHTTPServerTransport` 实例 [51](https://github.com/modelcontextprotocol/typescript-sdk/releases)。在早期 SDK 版本中，`McpServer.connect(transport)` 会静默覆盖实例内部的 `this._transport` 引用而不会抛出警告，这导致并发会话 A 在会话 B 调用 `connect()` 后立即因底层流中断而抛出 `AbortError: This operation was aborted`，或者在客户端（如 Cursor、Claude Code）断线重连发送第二次 `initialize` 请求时触发 `-32600 Invalid Request: Server already initialized` 错误 [53](https://github.com/modelcontextprotocol/typescript-sdk/issues/1400)。在最新发布的 SDK 版本中，`Server.connect()` 已强制要求单次连接绑定（在已连接状态下再次调用会直接拒绝），且 `registerTool` 完成了工具 Schema 的惰性转换优化（PR #2889），不再在注册时预先转换所有 Schema，从而使得按请求（Per-Request）动态实例化 `McpServer` 与 `Transport` 的 CPU 与内存开销降至极低水平 [51](https://github.com/modelcontextprotocol/typescript-sdk/releases)。此外，在 Schema 校验库依赖上，早期 SDK（如 `v1.12.0`）仅支持 Zod v3，若宿主项目安装 Zod v4 会导致工具 Schema 静默解析失败并在调用 `tools/call` 时返回 `-32601 Method not found`；该兼容性问题已在 SDK `v1.22.0+`（通过 `zod-compat.ts`）中彻底解决，生产环境应确保使用新版 SDK 并注意区分规范中的复数方法名 `tools/call` [44](https://github.com/modelcontextprotocol/typescript-sdk/issues/553)。

对于需要同时服务 `2026-07-28` 现代无状态客户端与 `2025-03-26` 存量有状态客户端的企业级网关，官方架构支持通过 `createMcpHandler` 配合 `isLegacyRequest` 谓词在单一端口上实现双代际流量分流（Dual-Era Routing），或按无状态/有状态端点分别挂载 [23](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/legacy-routing/README.md)。以下为基于 Express 的无状态高并发模式生产级实现代码：

TypeScript

```
import express, { Request, Response } from 'express';
import cors from 'cors';
import { randomUUID } from 'node:crypto';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { isInitializeRequest } from '@modelcontextprotocol/sdk/types.js';
import { z } from 'zod';

const app = express();
app.use(express.json({ limit: '4mb' }));

// 1. 浏览器端跨域支持：必须通过 exposedHeaders 显式暴露 Mcp-Session-Id
app.use(cors({
  origin: ['https://claude.ai', 'https://app.internal.corp'],
  allowedHeaders: [
    'Content-Type', 'Accept', 'Authorization',
    'mcp-session-id', 'mcp-protocol-version',
    'mcp-method', 'mcp-name', 'last-event-id'
  ],
  exposedHeaders: ['Mcp-Session-Id'],
}));

// 工厂函数：由于 SDK 已优化 registerTool 的 Schema 惰性解析，按请求/按会话创建实例开销极低
function buildMcpServer(): McpServer {
  const server = new McpServer({
    name: 'enterprise-deployment-mcp',
    version: '2.1.0',
  });

  // 注册支持流式进度通知的工具
  server.registerTool(
    'deploy_cluster',
    {
      title: 'Deploy Cloud Cluster',
      inputSchema: {
        environment: z.enum(['staging', 'production']).describe('Target environment'),
        region: z.string().describe('Cloud region code'),
      },
    },
    async ({ environment, region }, { sendNotification }) => {
      // 发送请求作用域内的中间进度通知（当响应为 SSE 流时实时下发）
      await sendNotification({
        method: 'notifications/message',
        params: { level: 'info', data: `Initializing deployment in ${region} (${environment})...` },
      });

      return {
        content: [{ type: 'text', text: `Cluster successfully deployed to ${region} in ${environment}.` }],
      };
    }
  );

  return server;
}

// ---------------------------------------------------------------------------
// 模式 A：无状态（Stateless）高并发实现 —— 每次请求创建独立的 Server 与 Transport
// 完美契合 Serverless、Kubernetes 多副本水平扩展及 2026-07-28 规范
// ---------------------------------------------------------------------------
app.post('/mcp/stateless', async (req: Request, res: Response) => {
  const server = buildMcpServer();
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: undefined, // 显式禁用 Session ID，进入无状态模式
    enableJsonResponse: false,     // 设为 false 允许按需升级为请求级 SSE 流；设为 true 则强制纯 JSON 但丢弃通知
    enableDnsRebindingProtection: true,
    allowedHosts: ['127.0.0.1:3000', 'mcp.internal.corp'],
    allowedOrigins: ['https://claude.ai', 'https://app.internal.corp'],
  });

  res.on('close', () => {
    transport.close();
    server.close();
  });

  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});

// 无状态端点显式拒绝独立 GET SSE 流，按规范必须返回 405 Method Not Allowed（防止客户端报 404 挂起）
app.get('/mcp/stateless', (_req: Request, res: Response) => {
  res.writeHead(405, { Allow: 'POST' }).end(JSON.stringify({
    jsonrpc: '2.0',
    error: { code: -32000, message: 'Method not allowed: Stateless endpoint does not support standalone GET SSE.' },
    id: null,
  }));
});

```

当服务端需要兼容 `2025-03-26` 规范的持久会话特性或支持网络闪断后的 SSE 事件重放（Resumability / SEP-1699）时，工程上需配置 `sessionIdGenerator` 并注入自定义的 `EventStore` 实现 [24](https://github.com/modelcontextprotocol/typescript-sdk/issues/451)。当客户端断线重连并在请求头中附带 `Last-Event-ID` 时，`StreamableHTTPServerTransport` 会自动调用 `eventStore.replayEventsAfter(lastEventId, { send })` 将断连期间积压的 JSON-RPC 消息重新推入新的 SSE 响应流中 [11](https://gofastmcp.com/deployment/http)。需要注意的是，SDK 默认将独立 `GET` 流的 `streamId` 硬编码为 `_GET_stream`，因此在多租户共享存储实现中必须结合会话上下文进行隔离 [24](https://github.com/modelcontextprotocol/typescript-sdk/issues/451)：

TypeScript

```
import { EventStore, StreamId, EventId } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { JSONRPCMessage } from '@modelcontextprotocol/sdk/types.js';

// 自定义分布式 EventStore 接口实现（生产环境底层可对接 Redis Streams 或 MongoDB）
class RedisBackedEventStore implements EventStore {
  private memoryBuffer = new Map<EventId, { streamId: StreamId; message: JSONRPCMessage; timestamp: number }>();

  async storeEvent(streamId: StreamId, message: JSONRPCMessage): Promise<EventId> {
    const eventId = `${streamId}::${Date.now()}::${randomUUID()}`;
    this.memoryBuffer.set(eventId, { streamId, message, timestamp: Date.now() });
    return eventId;
  }

  async replayEventsAfter(
    lastEventId: EventId,
    { send }: { send: (eventId: EventId, message: JSONRPCMessage) => Promise<void> }
  ): Promise<StreamId> {
    const anchor = this.memoryBuffer.get(lastEventId);
    if (!anchor) throw new Error(`Unknown Last-Event-ID: ${lastEventId}`);

    for (const [eid, record] of this.memoryBuffer.entries()) {
      if (record.streamId === anchor.streamId && record.timestamp > anchor.timestamp) {
        await send(eid, record.message);
      }
    }
    return anchor.streamId;
  }
}

// 会话路由表：每个 Session 必须独占一对 (McpServer, StreamableHTTPServerTransport)
const activeTransports = new Map<string, StreamableHTTPServerTransport>();
const sharedEventStore = new RedisBackedEventStore();

app.all('/mcp/stateful', async (req: Request, res: Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined;

  if (req.method === 'POST') {
    let transport = sessionId ? activeTransports.get(sessionId) : undefined;

    if (!transport) {
      // 若客户端未携带 Session ID 且当前报文为 InitializeRequest，则初始化新会话
      if (!sessionId && isInitializeRequest(req.body)) {
        transport = new StreamableHTTPServerTransport({
          sessionIdGenerator: () => randomUUID(),
          eventStore: sharedEventStore,
          onsessioninitialized: (newSid: string) => {
            activeTransports.set(newSid, transport!);
          },
        });
        transport.onclose = () => {
          if (transport?.sessionId) activeTransports.delete(transport.sessionId);
        };
        const server = buildMcpServer();
        await server.connect(transport);
      } else {
        // 关键规范要求：若客户端携带了未知或已过期的 Mcp-Session-Id，必须返回 404 Not Found
        // 客户端收到 404 后会自动丢弃旧会话并重新发起 InitializeRequest
        const statusCode = sessionId ? 404 : 400;
        res.status(statusCode).json({
          jsonrpc: '2.0',
          error: { code: -32000, message: sessionId ? 'Session not found' : 'Bad Request: Server not initialized' },
          id: null,
        });
        return;
      }
    }
    await transport.handleRequest(req, res, req.body);
  } else if (req.method === 'GET' || req.method === 'DELETE') {
    // 处理 2025 规范下的独立 GET SSE 监听流与 DELETE 会话销毁请求
    if (!sessionId || !activeTransports.has(sessionId)) {
      res.status(404).send('Session not found');
      return;
    }
    const transport = activeTransports.get(sessionId)!;
    await transport.handleRequest(req, res);
  } else {
    res.writeHead(405, { Allow: 'GET, POST, DELETE' }).end();
  }
});

```

### Python SDK（`FastMCP` 与 `StreamableHTTPSessionManager`）工程实现方案

在 Python 技术栈中，MCP 官方 SDK（`mcp`）及高层框架 `FastMCP` 基于 ASGI 规范（Starlette、FastAPI 与 Uvicorn）以及 `anyio` 结构化并发原语（`TaskGroup` 与 `MemoryObjectSendStream` / `MemoryObjectReceiveStream`）构建了 `Streamable HTTP` 传输层 [11](https://gofastmcp.com/deployment/http)。其核心生命周期协调器为 `StreamableHTTPSessionManager`（位于 `mcp.server.streamable_http_manager`），而单会话报文收发则由 `StreamableHTTPServerTransport`（位于 `mcp.server.streamable_http`）负责 [46](https://github.com/modelcontextprotocol/python-sdk/issues/1727)。

在将多个 `FastMCP` 服务挂载至现有的企业级 FastAPI 或 Starlette 主应用时，最核心的工程要求是必须通过 `contextlib.AsyncExitStack` 将所有子 MCP 应用的 `session_manager.run()`（或 `http_app().lifespan`）注入主 ASGI 应用实例的 `lifespan` 上下文中 [59](https://github.com/modelcontextprotocol/python-sdk/issues/756)。如果开发者仅调用了 `app.mount()` 而遗漏了 `lifespan` 上下文传递，`StreamableHTTPSessionManager` 内部的 `anyio` 任务组将处于未初始化状态，导致任何进入 `/mcp` 的 HTTP 请求直接崩溃并抛出 `RuntimeError: Task group is not initialized. Make sure to use run().`；同时，单个 `StreamableHTTPSessionManager` 实例的 `.run()` 方法在其生命周期内仅允许调用一次，在 Serverless 热容器复用场景下必须避免重复调用同一实例的启动方法 [60](https://github.com/modelcontextprotocol/python-sdk/issues/713)。

以下为结合 FastAPI 多服务挂载、无状态水平扩展模式与健康检查路由的 Python 生产级工程代码：

Python

```
import contextlib
from fastapi import FastAPI
from starlette.responses import JSONResponse
import uvicorn
from mcp.server.fastmcp import FastMCP

# 1. 初始化无状态 Streamable HTTP MCP 服务实例
# stateless_http=True 使得每个请求独立创建临时传输上下文，彻底消除负载均衡器会话粘滞需求
# json_response=False（默认）保留按需返回 SSE 流以推送进度与日志的能力
analytics_mcp = FastMCP(
    name="AnalyticsMCPServer",
    stateless_http=True,
    json_response=False,
)

@analytics_mcp.tool(description="Execute SQL aggregation query on analytical warehouse")
async def run_warehouse_query(sql: str) -> str:
    return f"Executed query successfully: {sql}"

inventory_mcp = FastMCP(
    name="InventoryMCPServer",
    stateless_http=True,
    json_response=False,
)

@inventory_mcp.tool(description="Check real-time stock level for SKU")
async def check_sku_stock(sku_id: str) -> dict:
    return {"sku_id": sku_id, "available": 420, "warehouse": "us-east-1"}

# 2. 聚合多个 MCP 实例的 ASGI Lifespan，确保每个 StreamableHTTPSessionManager 的 anyio TaskGroup 正确启动与优雅关闭
@contextlib.asynccontextmanager
async def combined_mcp_lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(analytics_mcp.session_manager.run())
        await stack.enter_async_context(inventory_mcp.session_manager.run())
        yield

# 3. 构建主 FastAPI 宿主应用并挂载子服务
app = FastAPI(title="Enterprise MCP Gateway", lifespan=combined_mcp_lifespan)

@app.get("/healthz")
async def health_check():
    return JSONResponse({"status": "healthy", "transport": "streamable-http"})

# 挂载后访问端点分别为 /analytics/mcp 与 /inventory/mcp
app.mount("/analytics", analytics_mcp.streamable_http_app())
app.mount("/inventory", inventory_mcp.streamable_http_app())

if __name__ == "__main__":
    # 本地运行时绑定 127.0.0.1 以防范局域网重绑定风险
    uvicorn.run(app, host="127.0.0.1", port=8000)

```

对于采用 `2026-07-28` 规范（Python SDK v2）并需要实现跨进程 `subscriptions/listen` 变更通知扇出（Fan-out）的集群系统，服务端工程实现只需实现 `SubscriptionBus` 抽象接口并将其传入 `MCPServer(subscriptions=...)`（或在底层组装 `ListenHandler(bus)` 并注册至 `on_subscriptions_listen` 插槽） [21](https://deepwiki.com/modelcontextprotocol/python-sdk/3.3-handling-server-notifications-and-subscriptions)。当工具内部调用 `await ctx.notify_tools_changed()`、`await ctx.notify_prompts_changed()` 或 `await ctx.notify_resources_changed()` 时，SDK 会自动完成首帧确认、`io.modelcontextprotocol/subscriptionId` 元数据打标及 URI 过滤，而自定义的 `SubscriptionBus` 仅负责在进程间通道上传输四个轻量级的强类型 `ServerEvent` 数据类，在架构上做到了业务通知与底层 JSON-RPC 协议帧的彻底解耦 [21](https://deepwiki.com/modelcontextprotocol/python-sdk/3.3-handling-server-notifications-and-subscriptions)。

### C# 与 Go SDK 的工程架构设计对比

除 TypeScript 与 Python 外，微软主导的官方 C# SDK（`ModelContextProtocol.AspNetCore` v2.0）与官方 Go SDK（`v0.3.0+`）也提供了极具代表性的强类型工程实现 [22](https://github.com/modelcontextprotocol/csharp-sdk/discussions/549)。C# SDK 将核心包拆分为轻量的 `ModelContextProtocol.Core` 与专职处理 `Streamable HTTP` 的 `ModelContextProtocol.AspNetCore`（Apps 与 Tasks 特性则作为独立可选扩展包提供） [50](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/)。在 ASP.NET Core 路由中，开发者通过 `endpoints.MapMcp()` 自动注册 `GET`、`POST`、`DELETE` 请求委托，并可选择同时映射 `/sse` 与 `/message` 以保持向后兼容 [22](https://github.com/modelcontextprotocol/csharp-sdk/discussions/549)。在实现 `2026-07-28` 的 MRTR 多轮交互时，C# SDK 采用了异常控制流模式：工具方法无需手动拼装复杂的 JSON 结构，只需直接抛出 `throw new InputRequiredException(...)`，通过工厂方法 `InputRequest.ForElicitation(...)` 或 `InputRequest.ForSampling(...)` 构造输入需求并传入 `requestState` 字符串，框架底层即会自动捕获该异常并序列化为符合规范的 `InputRequiredResult` 报文返回给客户端 [50](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/)。与此同时，Go SDK 则通过 `StreamableServerTransport` 与 `StreamableClientTransport` 原生支持单次 `application/json` 响应、可配置的 `EventStore` 事件重放以及无状态流式会话模式（Stateless Streamable Sessions） [49](https://github.com/modelcontextprotocol/go-sdk/issues/10)。

### 客户端接入工程与 Claude Code 协议协商机制

在客户端侧，无论是自研 Agent 宿主应用还是接入 Anthropic 官方的 Claude Code 与 Claude Desktop，工程实现均围绕协议版本探测、身份认证注入与自动降级回退展开 [2](https://glama.ai/blog/2026-01-02-what-is-streamable-http-in-mcp)。使用 TypeScript 的 `StreamableHTTPClientTransport` 或 Python 的 `streamablehttp_client` 时，客户端通过构造参数（如 `requestInit.headers`）注入 `Authorization: Bearer <token>` 等安全头，并严格遵循同源重定向安全策略——客户端默认仅跟随同源（相同 scheme、host 与 port，或同主机从 `http` 升级至 `https`）的重定向，若部署环境存在跨主机重定向，必须显式配置 `redirectPolicy: 'follow'`，否则请求将在浏览器或客户端中被拦截以防凭证泄露 [2](https://glama.ai/blog/2026-01-02-what-is-streamable-http-in-mcp)。针对线上可能未知协议版本的远端服务器，标准客户端兼容性策略是优先使用 `StreamableHTTPClientTransport` 向目标 URI 发起携带 `InitializeRequest` 的 `HTTP POST` 请求；若捕获到 `4xx` 错误（如旧版 SSE 服务器对未预期的 POST 返回错误），则自动回退至 `SSEClientTransport` 发起 `GET` 握手 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。此外，在网关代理多个下游 Worker 的高吞吐场景中，现代 TypeScript SDK 支持 `connect({ prior })` 网关模式，即仅对远端执行一次探测握手，随后让所有工作协程复用协商结果实现零往返（Zero-round-trip）连接建立 [56](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/README.md)。

在 Anthropic 官方终端智能体工具 Claude Code 中，系统已原生支持通过命令 `claude mcp add --transport http <name> <url> --header "Authorization: Bearer ..."` 或 `claude mcp add-json` 接入远程 `Streamable HTTP` 服务器（注意 JSON 配置中若包含 `url` 则必须显式指定 `"type": "http"`，否则会被默认当作 `stdio` 解析而失败），并提供 `local`、`project`（生成团队共享的 `.mcp.json`）与 `user` 三级配置作用域 [14](https://code.claude.com/docs/en/mcp)。自 Claude Code `v2.1.265` 起，指定 `--transport http` 时客户端会自动尝试 `Streamable HTTP` 并在服务端不支持时透明降级切换为 `SSE` [14](https://code.claude.com/docs/en/mcp)。为优化终端启动延迟，Claude Code 实现了工具发现缓存与首用惰性连接机制（Connects on First Use）：启动时直接从上一会话保存的发现缓存中加载工具列表（工具命名空间统一映射为 `mcp__<serverName>__<toolName>`），直到大模型在对话中首次调用某工具时才真正发起 HTTP 连接，并在首次连接尝试期间提供最长 10 秒的请求挂起等待窗口 [14](https://code.claude.com/docs/en/mcp)。

## 分布式多节点部署拓扑与生产级避坑指南

当企业将 MCP Server 从本地 `stdio` 子进程迁移至基于 `Streamable HTTP` 的远程云原生集群时，配置参数的选择与分布式状态同步直接决定了系统的功能完整性与运行时稳定性 [36](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-streamablehttp-transport)。

### 核心配置项权衡分析（`stateless_http` 与 `json_response`）

在官方 SDK（如 Python `FastMCP` 与 TypeScript `StreamableHTTPServerTransport`）中，两个核心布尔开关控制着传输层的底层行为：`stateless_http`（TS 中对应 `sessionIdGenerator: undefined`）用于控制连接状态管理，`json_response`（TS 中对应 `enableJsonResponse`）用于控制响应格式处理 [24](https://github.com/modelcontextprotocol/typescript-sdk/issues/451)。默认情况下两者均为 `false`，但在特定网关受限场景下强制开启这两个选项会导致显著的协议能力变化 [36](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-streamablehttp-transport)。

具体而言，当启用 `enableJsonResponse: true`（或 `json_response=True`）时，服务端将强制以单次 `Content-Type: application/json` 响应所有 `POST` 请求，彻底关闭 SSE 流升级通道 [24](https://github.com/modelcontextprotocol/typescript-sdk/issues/451)。根据 TypeScript SDK `streamableHttp.ts` 的底层设计，开启该模式是专为极简无状态 RPC 场景准备的，此时 `send()` 方法会直接丢弃所有与当前请求关联的中间通知（如 `notifications/progress` 进度条更新与 `notifications/message` 实时日志），而非将通知与最终结果打包为 JSON 数组返回，这会导致客户端界面上的进度条消失且实时日志停止工作 [36](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-streamablehttp-transport)。而在启用 `stateless_http: true`（或 `sessionIdGenerator: undefined`）但保留 `enableJsonResponse: false` 时，虽然在 `2025-03-26` 规范下因缺失 `Mcp-Session-Id` 与持久反向通道而无法发起服务端 Push 式的采样（Sampling）与询问（Elicitation），但在单次工具调用内部依然可以升级 SSE 流推送实时进度通知 [7](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/282)。当进一步升级至 `2026-07-28` 规范后，借助 MRTR（SEP-2322）与单请求 SSE 流，无状态服务器既能保持零会话亲和性的水平扩展能力，又能完整支持多轮 Elicitation、Roots 查询以及单次请求内的实时进度流推送 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。

<!-- figure 2: interactive chart embedded in the report; its text content follows -->

MCP Cloud Architecture Guide  Production Engineering Scorecard

### Streamable HTTP Production Deployment Topologies and **Capability Trade-Off**  Matrix

Anthropic MCP Streamable HTTP 协议在生产环境（K8s 集群与云原生网关）落地决策全景指南：涵盖协议能力边界、三大多节点部署拓扑、以及高频 SDK 运行时避坑方案。

#### 1 配置模式与协议世代能力权衡矩阵 (Capability Matrix)

点击行可高亮查看架构边界与风险建议

| 部署配置与世代 | 进度与日志通知
Progress / Logging | 服务端主动请求
Elicitation / Roots | 变更订阅推送
Change Subscriptions | 零粘性水平扩容
Stateless Scaling | Serverless 冷启动
Cold-Start |
| --- | --- | --- | --- | --- | --- |
| 有状态 + SSE 2025 Default: `stateless_http=false` | ● 原生支持 | ● 原生支持 | ● 长连推送 | ✕ 需会话粘性 | ▲ 较差 (需保活) |
| 早期无状态 + SSE 2025 Era: `stateless_http=true` | ▲ 仅限单请求内 | ✕ 不支持反向 | ✕ 无法主动推 | ● 任意节点可达 | ● 良好 (即用即停) |
| 纯 JSON 模式 `enableJsonResponse: true` | ✕ 静默完全丢弃 | ✕ 完全不支持 | ✕ 完全不支持 | ● 标准 REST 体验 | ★ 极致轻量秒开 |
| 现代无状态 + MRTR 2026 推荐  Multi-Round-Trip + requestState | ● 单请求流式推送 | ★ inputRequired 往返 | ★ EventBus 订阅 | ★ One Server / Req | ★ 极致 (#2889惰性优化) |

🌟

现代无状态 + MRTR (2026-07-28 Era) 推荐标准： 终极推荐实践：通过 Multi-round-trip 和 requestState 实现无状态工具多轮交互，通过 inputRequired 替代传统反向 RPC push，单请求按需创建 McpServer 实例（#2889 优化后转换耗时微秒级），兼顾 100% 弹性与协议全功能。

#### 2 多节点 Kubernetes 集群部署拓扑架构 (Deployment Topologies)

对比三种跨 Pod 流量路由模式与后端状态协调方案

KUBERNETES INGRESS & CLUSTER POD TRAFFIC FLOW

MCP Client

Claude / Agent

mcp-session-id

Stateless Mode

K8s Ingress

Load Balancer

Round-Robin

无粘性转发

Req 1 & 2

Pod A (Node 1)

Req 1: /initialize (OK)

单例 / 逐请求隔离

Pod B (Node 2)

Req 2: /tools/call

依赖水合 / 独立运行

External Store / Bus

Redis / EventStore

sessionId & event-log

水合已就绪

核心配置规范 (TypeScript SDK) createMcpHandler

```
// Pattern 1: One server and transport per request
app.post('/mcp', async (req, res) => {
  const server = buildServer(); // Factory creates fresh McpServer
  const transport = new WebStandardStreamableHTTPServerTransport({
    sessionIdGenerator: undefined // stateless mode
  });
  await server.connect(transport);
  await transport.handlePostMessage(req, res);
});
```

**流转说明：** 每个 HTTP 请求由负载均衡器分发到任意 Pod。每个请求内部构建独立的 McpServer 实例与无状态 Transport。完全无需 Session 亲和性，天然支持无限弹性横向伸缩。

生产架构多维打分 (Architecture Trade-offs) 满分 100 分

当前拓扑评分

#### 3 生产级 SDK 运行时高频踩坑与排查全解 (Runtime Diagnostics)

收录 TypeScript 与 Python SDK 在多会话、并发及 ASGI 集成中的典型错误与权威代码修复

TS SDK Issue #1405

会话静默崩溃

##### Server.connect() 单例覆写导致会话静默中断

**现象：** 多个客户端 Session 共享同一个 Server 实例时，调用 `server.connect(transportB)` 会静默覆写 `_transport`，导致 Session A 崩溃并抛出 AbortError: This operation was aborted。

根因：Server 内部仅支持维护单个活动 Transport。并发 HTTP 场景中复用 Server 实例造成引用破坏。

✓ 官方权威修复方案 (#2918)：

```
// 采用 One Server Per Request 架构
const handler = createMcpHandler(async () => {
  const server = new McpServer({ name: 'my-agent' });
  registerTools(server); // 惰性转换无需担心开销
  return server;
});
```

TS SDK Issue #1658 / #55

多节点 K8s 陷阱

##### 跨 Pod 转发时 _initialized 私有字段导致 400/404 拒绝

**现象：** 客户端首个握手请求由 Pod A 处理生成 `mcp-session-id`，第二个请求命中 Pod B 时因本地未水合被直接判定非法。

根因：`_initialized` 与 `sessionId` 是底层 Transport 私有字段，未暴露公共的预水合构造接口。

✓ 生产修复对策：

```
// 显式传入 resumeSessionId 跳过握手校验
new StreamableHTTPServerTransport({
  sessionIdGenerator: () => mcpSessionId,
  resumeSessionId: mcpSessionId // 标记已处于已初始化状态
}); // 或生产全面改用模式 1 纯无状态架构
```

TS SDK Issue #866 / #1309

特性静默丢失

##### enableJsonResponse: true 静默丢弃进度条与通知

**现象：** 开启纯 JSON 响应模式后，客户端调用耗时 Tool 时，进度条彻底消失，服务器下发的 `notifications/progress` 在客户端收不到。

根因：SDK 设计如此（PR #299）。纯 JSON 响应单次往返即关闭，内部 `send()` 丢弃所有关联 Notification。

✓ 生产修复对策：

```
// 严禁对需进度汇报的工具启用 enableJsonResponse
// 生产推荐保持 text/event-stream 响应格式：
const transport = new WebStandardStreamableHTTPServerTransport();
// 仅单请求保持流式返回，兼顾无状态与通知完整性
```

Python SDK Issue #713

ASGI 启动失败

##### FastMCP 挂载 FastAPI 报 Task group not initialized

**现象：** 调用 `app.mount("/mcp", mcp.streamable_http_app())` 时，请求抛出 RuntimeError: Task group is not initialized. Make sure to use run()。

根因：`StreamableHTTPSessionManager` 强依赖 AnyIO 任务组。直接挂载未将 MCP 的 lifespan 传递给 ASGI 根应用。

✓ 官方推荐规范写法：

```
# 单 MCP 应用：传递 lifespan
app = FastAPI(lifespan=mcp_app.lifespan)
# 多 MCP 挂载：使用 contextlib.AsyncExitStack 组合
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncExitStack() as stack:
        await stack.enter_async_context(mcp1.lifespan(app))
        yield
```

Python SDK Issue #756

内存无界泄露

##### stateless_http=True 模式下任务组协程泄露

**现象：** 在高并发请求下，`session_manager._task_group._tasks` 数量随着请求持续线性增长（23 → 27 → 31...），内存永不释放。

根因：`_handle_stateless_request()` 启动的 3 个后台协程退出依赖 Stream 关闭，但 Transport 未主动 close。

✓ 生产补丁与规避方案：

```
# 确保在 request 结束上下文强制 close stream
try:
    await http_transport.connect()
finally:
    # 显式关闭流，触发 _receive_loop 退出
    http_transport._read_stream_writer.close()
    http_transport._write_stream.close()
```

Python SDK #1363 / #2150 / #1727

竞态与停机挂起

##### 快速失败 ClosedResourceError 与停机挂起

**现象：** 客户端 Accept 头错误导致快速 406 失败时抛出 anyio.ClosedResourceError；容器优雅关机时 EventSourceResponse 挂起。

根因：checkpoint 竞态读取已关闭 Stream；terminate 时漏关 `_sse_stream_writers`；未知 session 误返 400 而非 404。

✓ 生产韧性防御对策：

```
# 1. 忽略快速退出流竞态
except anyio.ClosedResourceError: pass
# 2. 关机阶段同步强制清空 SSE 流
for w in self._sse_stream_writers: w.close()
# 3. 未知 Session 严格返回 404 触发客户端 re-init
```

Production engineering scorecard for MCP Streamable HTTP deployments. The top layer maps protocol capabilities across configuration modes; the middle layer contrasts the three multi-node cluster topologies; the bottom layer diagnoses high-frequency SDK runtime failures and their canonical engineering fixes.

Data sources: [Claude Academy](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-streamablehttp-transport), [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk), [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

<!-- /figure 2 -->

### 多节点集群（Multi-Node Kubernetes）三种部署拓扑方案

在生产级 Kubernetes 或多实例容器环境中，由于负载均衡器默认采用轮询（Round-Robin）或最少连接策略分发每个独立的 `HTTP POST` 请求，单机内存字典（如 `const transports = {}`）无法跨 Pod 共享 [9](https://github.com/modelcontextprotocol/typescript-sdk/issues/340)。根据官方 SDK 架构指南与工程实践，多节点部署共有三种标准实现方案 [56](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/README.md)。

#### 拓扑一：全无状态按请求隔离模式

全无状态按请求隔离模式（Stateless Per-Request Mode）是 `2026-07-28` 规范及现代云原生部署的首选拓扑 [7](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/282)。服务端将 `sessionIdGenerator` 设为 `undefined`（或启用 `stateless_http=True`），并在每次收到 HTTP 请求时在路由处理器内部动态创建全新的 `McpServer` 与 `Transport` 实例，请求处理完毕后立即销毁以实现完全隔离并避免并发请求 ID 冲突 [11](https://gofastmcp.com/deployment/http)。跨请求的业务连续性完全交由客户端在每次请求体中声明的 `clientCapabilities` 以及 MRTR 模式下的加密 `requestState` 承载 [25](https://modelcontextprotocol.io/specification/2026-07-28/schema)。在该拓扑下，集群中的任意 Pod 均可无差别处理任意请求，无需维护 Redis 会话存储或网关粘滞会话配置 [11](https://gofastmcp.com/deployment/http)。

#### 拓扑二：外部持久化存储与会话水合模式

当系统必须运行在 `2025-03-26` 有状态会话模式下，且不允许在负载均衡器层开启会话亲和性（Sticky Sessions）时，需采用外部持久化存储模式（Persistent Storage Mode），使用外部数据库（如 Redis、ValKey 或 MongoDB）存储会话状态与 `EventStore` 事件流 [37](https://github.com/modelcontextprotocol/typescript-sdk/issues/1658)。在此模式下，工程实现曾面临一个典型的底层 SDK 架构挑战（TypeScript SDK Issue #1658）：当客户端发送首个 `initialize` 请求命中 Pod A 时，Pod A 生成 `mcp-session-id` 并将其存入外部数据库；但当客户端紧接着发送 `notifications/initialized` 或 `tools/call` 命中 Pod B 时，由于 `WebStandardStreamableHTTPServerTransport` 将 `sessionId` 与 `_initialized` 状态作为私有实例字段锁死在 Pod A 的内存中，Pod B 新建的 Transport 实例因未经历 `initialize` 握手，其私有方法 `validateSession()` 必然校验失败并拒绝请求 [9](https://github.com/modelcontextprotocol/typescript-sdk/issues/340)。

针对这一跨节点状态断裂问题，工程上必须实施会话水合（Session Hydration）方案：当 Pod B 收到携带已知 `mcp-session-id` 的请求并从外部存储确认该会话有效后，通过 SDK 提供的多节点会话恢复机制（如传入预初始化构造参数 `resumeSessionId: mcpSessionId` 与 `sessionIdGenerator: () => mcpSessionId` 跳过初始化握手检查；在旧版 SDK 中则需在工厂层直接水合内部 `_webStandardTransport.sessionId` 与 `_initialized = true` 字段），从而在任意无状态工作节点上动态重建出已处于初始化状态的 Transport 实例，并挂载共享的分布式 `EventStore` [37](https://github.com/modelcontextprotocol/typescript-sdk/issues/1658)。

#### 拓扑三：本地状态加消息总线路由模式

当服务端持有无法序列化的重型本地资源（如驻留内存的浏览器 Playwright 实例、本地数据库连接池或活跃的 `subscriptions/listen` SSE 长连接流）时，需采用本地状态加消息总线路由模式（Local State with Message Routing） [10](https://github.com/modelcontextprotocol/typescript-sdk/issues/330)。在此拓扑下，每个节点在本地内存中维护活跃的 `StreamableHTTPServerTransport` 实例，前端七层网关根据 HTTP 请求头中的 `Mcp-Session-Id` 执行一致性哈希路由（Consistent Hashing），或者在请求落入其他 Pod 以及触发全局资源变更时，通过 Redis Pub/Sub 驱动的 `SubscriptionBus` / `ServerEventBus` 将消息跨节点路由至持有目标 SSE 写入流的 Pod 内存中进行下发 [28](https://py.sdk.modelcontextprotocol.io/handlers/subscriptions/)。

### 生产环境高频工程故障诊断与修复方案

通过对官方 TypeScript 与 Python SDK 代码库及生产工单的深度剖析，下表汇总了 `Streamable HTTP` 工程落地中最易触发的七类底层故障、触发机理及其标准修复方案：

| 故障域与 SDK 平台 | 故障现象与底层触发机理 | 生产级工程修复方案 |
| --- | --- | --- |
| **TypeScript SDK** ：多会话并发静默中断与重连 `-32600` 报错 [53](https://github.com/modelcontextprotocol/typescript-sdk/issues/1400) | 在全局作用域创建单一 `McpServer` 或 `Transport` 并复用于多个连接；新连接调用 `server.connect()` 覆盖内部 `_transport` 指针，导致存量连接抛出 `AbortError`，或二次 `initialize` 报 `Server already initialized` [53](https://github.com/modelcontextprotocol/typescript-sdk/issues/1400)。 | 遵循 One Server Per Request/Session 原则：无状态模式下于路由处理器内部按请求新建 `McpServer` 与 `Transport`；有状态模式下按 `mcp-session-id` 独立实例化对象对，并升级至最新 SDK 利用惰性 Schema 转换降低开销 [51](https://github.com/modelcontextprotocol/typescript-sdk/releases)。 |
| **TypeScript SDK** ：客户端 SSE 断线重连过早放弃与空 ID 失效 [51](https://github.com/modelcontextprotocol/typescript-sdk/releases) | `StreamableHTTPClientTransport` 在旧版中对 GET-SSE 流硬编码了 2 次重连上限，耗尽后静默结束；当 SSE 事件包含显式空字符串 `id` 时，因采用真值判断（`if (event.id)`）导致恢复令牌未更新；或 50MB 大型单事件 SSE 响应解析缓慢（耗时达 13 秒） [51](https://github.com/modelcontextprotocol/typescript-sdk/releases)。 | 升级 TypeScript SDK 至包含 PR #2846 的最新版本（50MB 工具结果 SSE 传输已优化至 1 秒以内），合理配置 `reconnectionOptions`，并修复空 `event.id` 恢复令牌回调逻辑 [51](https://github.com/modelcontextprotocol/typescript-sdk/releases)。 |
| **Python SDK** ：无状态模式后台任务内存泄漏（Issue #756） [59](https://github.com/modelcontextprotocol/python-sdk/issues/756) | 在早期 `1.x` 版本中，`StreamableHTTPSessionManager._handle_stateless_request()` 每次请求派生 `run_stateless_server`、`_receive_loop`、`message_router` 三个后台协程，但退出时未关闭底层内存流，导致 `_task_group._tasks` 无限增长；有状态模式下若缺失空闲会话清理也会泄漏内存 [59](https://github.com/modelcontextprotocol/python-sdk/issues/756)。 | 升级 `mcp` SDK 至包含流清理与空闲会话超时（Idle Session Timeout）机制的最新版本；确保无状态请求处理完毕后调用 `http_transport.terminate()` 关闭内存通道 [47](https://github.com/modelcontextprotocol/python-sdk/issues/2150)。 |
| **Python SDK** ：请求头校验快速失败引发 `ClosedResourceError` 竞态（Issue #1363） [33](https://github.com/modelcontextprotocol/python-sdk/issues/1363) | 当客户端发送缺失双 `Accept` 头的请求触发 `406 Not Acceptable` 快速返回时，连接立即关闭，但后台 `message_router` 协程尚处于 `anyio` `checkpoint()` 挂起状态，恢复执行读取已关闭流时抛出 `anyio.ClosedResourceError` [33](https://github.com/modelcontextprotocol/python-sdk/issues/1363)。 | 在 `message_router` 循环中捕获并忽略 `anyio.ClosedResourceError` 异常；同时确保所有客户端及网关健康检查探针严格携带完整的 `Accept: application/json, text/event-stream` 头 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。 |
| **Python SDK** ：服务停机时活跃 SSE 连接挂起无法退出（Issue #2150） [47](https://github.com/modelcontextprotocol/python-sdk/issues/2150) | `StreamableHTTPSessionManager` 停机时直接调用 `tg.cancel_scope.cancel()`，而 `terminate()` 仅清理了 `_request_streams` 却遗漏了 `_sse_stream_writers`，导致 `EventSourceResponse` 持续阻塞等待 `sse_stream_reader` [47](https://github.com/modelcontextprotocol/python-sdk/issues/2150)。 | 在调用任务组 `cancel()` 之前，遍历所有活跃会话并使用 `anyio.move_on_after()` 保护执行 `terminate()`，同步调用 `self._sse_stream_writers` 中所有 `MemoryObjectSendStream` 的 `.close()` 方法 [47](https://github.com/modelcontextprotocol/python-sdk/issues/2150)。 |
| **Python / TS 跨端交互** ：会话过期后客户端（如 Claude.ai）拒绝重新初始化（Issue #1727） [46](https://github.com/modelcontextprotocol/python-sdk/issues/1727) | 当服务端重启或清理空闲会话后，客户端携带旧 `Mcp-Session-Id` 发起请求；若服务端错误返回 `400 Bad Request`，客户端会判定为请求语法错误并终止重试，而非重新握手 [46](https://github.com/modelcontextprotocol/python-sdk/issues/1727)。 | 严格区分状态码语义：凡是提供了 `Mcp-Session-Id` 但服务端查无此会话的场景，必须返回 `404 Not Found`，以触发客户端协议栈自动发起新的无 ID `InitializeRequest` [46](https://github.com/modelcontextprotocol/python-sdk/issues/1727)。 |
| **安全与网络层** ：DNS 重绑定攻击与本地开发容器跨域拦截（Issue #574） [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http) | 恶意网页通过 DNS 重绑定访问开发者本地运行的 MCP Server；或在使用 GitHub Codespaces / Ngrok 隧道转发时因 `Host` / `Origin` 头不匹配被拒绝 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。 | 本地监听优先绑定 `127.0.0.1` 而非 `0.0.0.0` [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)；开启 `enableDnsRebindingProtection: true`（TS）或 `host_origin_protection=True`（Python），将合法隧道域名显式加入 `allowedHosts` 与 `allowedOrigins`，对非法 `Origin` 严格返回 `403 Forbidden` [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。 |

## 架构选型建议与演进结论

综合对 Anthropic MCP `Streamable HTTP` 规范（从 `2025-03-26` 至 `2026-07-28`）及多语言 SDK 底层实现的深度剖析，企业在构建生产级远程 MCP 基础设施时，应当从协议代际选型、流控配置以及网关治理三个维度确立清晰的技术路线。

在协议代际与状态管理维度，新建的远程 MCP Server 应全面拥抱 `2026-07-28` 默认无状态与 MRTR 架构范式，摒弃依赖 `Mcp-Session-Id` 内存映射与独立 `GET` SSE 反向通道的传统有状态设计，直接采用按请求动态实例化的无状态 `Streamable HTTP` 模式 [7](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/282)。对于需要执行中途人机确认（Elicitation）或工作区查询（Roots）的复杂工具，工程团队应统一通过 MRTR（即返回 `InputRequiredResult` 并配合加密签名与主体绑定的 `requestState`）实现跨请求的上下文接力；而对于需要向客户端推送目录或资源变更的场景，则通过无状态重拉信令流 `subscriptions/listen` 结合分布式 `SubscriptionBus` 实现，从而在零粘滞会话的前提下达成云原生集群的无限水平扩展 [3](https://ai.engineer/topics/model-context-protocol)。

在传输层流控配置维度，工程实践应保留请求级 SSE 动态升级能力，谨慎启用强制纯 JSON 模式。在配置 `StreamableHTTPServerTransport` 或 `FastMCP` 参数时，建议保持 `enableJsonResponse: false`（Python `json_response=False`）的默认设置 [24](https://github.com/modelcontextprotocol/typescript-sdk/issues/451)。这一配置不仅允许轻量级同步工具直接返回高效的 `application/json` 响应，同时保留了长耗时工具在单一 `POST` 请求生命周期内原地升级为 `text/event-stream` 以推送实时进度条与诊断日志的能力，有效避免因盲目开启 `enableJsonResponse: true` 导致客户端进度反馈与可观测性日志被 SDK 静默丢弃 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。

在企业级网关治理与安全加固维度，架构师应依托 SEP-2243 请求头镜像规范构建零请求体解析的七层智能体网关。通过强制校验并提取 HTTP 请求头中的 `Mcp-Method`、`Mcp-Name`、`MCP-Protocol-Version` 以及基于 `x-mcp-header` 映射的 `Mcp-Param-*`，企业可以在不反序列化 JSON-RPC 请求体的情况下，直接在 Envoy、Nginx 或 API Gateway 边缘节点实施工具级细粒度 RBAC 鉴权（结合 OAuth 2.1 与 `verifyAccessToken` 的 `expectedResource` 受众校验）、租户级限流配额、智能分片路由与 OpenTelemetry 全链路追踪 [4](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)。对于线上存量混合客户端环境，则可在入口层通过 `isLegacyRequest` 谓词路由或客户端 `POST`-to-`GET` 自动降级回退机制，实现从早期有状态传输向现代全无状态 `Streamable HTTP` 架构的平滑演进 [14](https://code.claude.com/docs/en/mcp)。

## Sources used in the report

1. [MCP Streamable HTTP - AIPX — AI Product Architect](https://aipx.app/technologies/mcp-streamable-http)
2. [Streamable HTTP Client Examples | Glama](https://glama.ai/blog/2026-01-02-what-is-streamable-http-in-mcp)
3. [Model Context Protocol: A Shared Interface Between AI Applications](https://ai.engineer/topics/model-context-protocol)
4. [Streamable HTTP - What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http)
5. [Best Platforms for Streamable HTTP MCP Servers in 2026 - Modal](https://modal.com/resources/best-platforms-streamable-http-mcp-servers)
6. [MCP Stdio vs Streamable HTTP for Enterprise Deployments](https://www.truefoundry.com/blog/mcp-stdio-vs-streamable-http-enterprise)
7. [Streamable HTTP - session management inconsistency · Issue #282](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/282)
8. [Understanding MCP Recent Change Around HTTP+SSE](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse/)
9. [sdk/server/streamableHttp.js cannot support stateless mode #340](https://github.com/modelcontextprotocol/typescript-sdk/issues/340)
10. [Both SSE and StreamableHttp transport require sticky sessions #330](https://github.com/modelcontextprotocol/typescript-sdk/issues/330)
11. [HTTP Deployment - FastMCP](https://gofastmcp.com/deployment/http)
12. [azure-docs/articles/container-apps/tutorial-mcp-server-python.md at](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/container-apps/tutorial-mcp-server-python.md)
13. [modelcontextprotocol/docs/registry/remote-servers.mdx at main](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/registry/remote-servers.mdx)
14. [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)
15. [Simple MCP Streamable HTTP Server](https://mcp.so/servers/simple-mcp-streamable-http-server)
16. [Support for "Streamable HTTP" Transport · Issue #220 - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/issues/220)
17. [Overview - What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports)
18. [fix: Send required Mcp-Method/Mcp-Name headers per SEP-2243](https://github.com/modelcontextprotocol/typescript-sdk/issues/2176)
19. [SEP-2322: Multi Round-Trip Requests - Model Context Protocol](https://modelcontextprotocol.io/seps/2322-MRTR)
20. [SEP-1442: Make MCP Stateless (by default) - GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1442)
21. [Handling Server Notifications & Subscriptions - DeepWiki](https://deepwiki.com/modelcontextprotocol/python-sdk/3.3-handling-server-notifications-and-subscriptions)
22. [How to create Streamable HTTP server? #549 - GitHub](https://github.com/modelcontextprotocol/csharp-sdk/discussions/549)
23. [typescript-sdk/examples/legacy-routing/README.md at main - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/legacy-routing/README.md)
24. [Subclassing McpServer causes tool invocation issues #451 - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/issues/451)
25. [Schema Reference - What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/specification/2026-07-28/schema)
26. [[Confused] Server-to-client request/response in Streamable HTTP](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1077)
27. [Multi Round-Trip Requests - Model Context Protocol](https://modelcontextprotocol.io/specification/draft/basic/patterns/mrtr)
28. [Subscriptions - MCP Python SDK](https://py.sdk.modelcontextprotocol.io/handlers/subscriptions/)
29. [Subscriptions - What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/specification/draft/basic/patterns/subscriptions)
30. [Protocol eras - Model Context Protocol](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/protocol-eras)
31. [Multiple MCPClients connecting to one MCPServer over Streamable](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1677)
32. [Feedback on Streamable HTTP Transport #866 - GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/866)
33. [Race Condition in StreamableHTTP Transport Causes ... - GitHub](https://github.com/modelcontextprotocol/python-sdk/issues/1363)
34. [Streamable HTTP: clarification for error cases and application/json](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1398)
35. [Simplify Streamable HTTP to use Standard HTTP Protocol / Methods](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/236)
36. [The StreamableHTTP transport · Model Context Protocol](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-streamablehttp-transport)
37. [StreamableHTTPServerTransport has no public API to reconstruct a](https://github.com/modelcontextprotocol/typescript-sdk/issues/1658)
38. [Roots - Model Context Protocol](https://modelcontextprotocol.io/specification/draft/client/roots)
39. [Understanding MCP clients - Model Context Protocol](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts)
40. [Sampling - What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/specification/draft/client/sampling)
41. [What Is Multi Round-Trip Requests? Definition & Examples](https://nhimg.org/glossary/multi-round-trip-requests/)
42. [Tools - Model Context Protocol](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
43. [tools.mdx - modelcontextprotocol - GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/server/tools.mdx)
44. [tool/call results in 'Method not found' with ... - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/issues/553)
45. [GitHub - mcp-auth/mcp-typescript-sdk](https://github.com/mcp-auth/mcp-typescript-sdk)
46. [StreamableHTTPSessionManager returns 400 instead of 404 for](https://github.com/modelcontextprotocol/python-sdk/issues/1727)
47. [Active Streamable HTTP sessions are not terminated during shutdown](https://github.com/modelcontextprotocol/python-sdk/issues/2150)
48. [Streamable HTTP error: Failed to open SSE stream: Not ... - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/issues/1150)
49. [Streamable HTTP support · Issue #10 · modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk/issues/10)
50. [Announcing v2.0 of the official MCP C# SDK - .NET Blog](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/)
51. [Releases · modelcontextprotocol/typescript-sdk - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/releases)
52. [server: add maxBodyBytes guard to ... - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/actions/runs/21784534873)
53. [Issue #1400 · modelcontextprotocol/typescript-sdk - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/issues/1400)
54. [bug(server): connect() silently overwrites transport, breaking](https://github.com/modelcontextprotocol/typescript-sdk/issues/1405)
55. [Build your first MCP server for Claude - Claude.ai Documentation](https://claude.com/docs/connectors/building/quickstart)
56. [typescript-sdk/examples/README.md at main - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/examples/README.md)
57. [Horizontal Scalability for stateful streamable HTTP #843 - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/issues/843)
58. [Streamable HTTP: pre-existing hardening items from the #2547](https://github.com/modelcontextprotocol/typescript-sdk/issues/2562)
59. [Stateless Mode memory leak #756 - python-sdk - GitHub](https://github.com/modelcontextprotocol/python-sdk/issues/756)
60. [how to manage multi streamable http server lifespan #713 - GitHub](https://github.com/modelcontextprotocol/python-sdk/issues/713)
61. [Deploy docs: reused-process runtimes (Lambda) hit the single-use](https://github.com/modelcontextprotocol/python-sdk/issues/3590)
62. [StreamableHTTPClientTransport not passing headers along on](https://github.com/modelcontextprotocol/typescript-sdk/issues/495)
63. [Best Claude Code MCP Servers: 8 Workflow-Based Picks 2026](https://www.tinyfish.ai/blog/best-mcp-servers-for-claude-code)
64. [Claude Code - Nautobot MCP Server Documentation](https://docs.nautobot.com/projects/nautobot-mcp-server/en/stable/user/claude_code/)
65. [Issue #866 · modelcontextprotocol/typescript-sdk - GitHub](https://github.com/modelcontextprotocol/typescript-sdk/issues/866)
66. [[horizontal scaling] How to actually build session persistence in](https://github.com/modelcontextprotocol/python-sdk/issues/880)
67. [2-retry SSE reconnect ceiling + silent-success after exhaustion](https://github.com/modelcontextprotocol/typescript-sdk/issues/2098)
68. [[v2] Streamable HTTP client does not clear stale resumption token](https://github.com/modelcontextprotocol/typescript-sdk/issues/2769)
69. [StreamableHttpClientTransport: maxRetries=0 leads to infinite retry](https://github.com/modelcontextprotocol/typescript-sdk/issues/1179)
70. [Add idle session timeout to StreamableHTTPSessionManager](https://github.com/modelcontextprotocol/python-sdk/actions/runs/22136216576)
71. [Potential memory leak in StreamableHTTPSessionManager due to](https://github.com/modelcontextprotocol/python-sdk/issues/1283)
72. [ClosedResourceError when using FastMCP(..., stateless_http=True](https://github.com/modelcontextprotocol/python-sdk/issues/1658)
73. [missing origin header in requests · Issue #574 - GitHub](https://github.com/modelcontextprotocol/inspector/issues/574)
