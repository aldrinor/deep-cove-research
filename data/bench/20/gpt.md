# **Anthropic / MCP「Streamable HTTP」工程实现深度技术分析** 

## **执行摘要** 

截至 **2026 年 9 月 24 日** ，所谓 Anthropic 的“Streamable HTTP”更准确地说，是 **Model Context Protocol （MCP）的 HTTP 传输绑定** 。Anthropic 在 2024 年 11 月开源并发布 MCP；2025 年 3 月，MCP 用 Streamable HTTP 取代最初的“HTTP + SSE”传输；2025 年 12 月 Anthropic 又将 MCP 捐赠给 Linux Foundation 旗下 Agentic AI Foundation，因此今天的规范与官方 SDK 主要由 <mark>`modelcontextprotocol`</mark> 项目维护，而不是一个 Anthropic 私有传输协议。 1 

最重要的结论是： **2026-07-28 版 Streamable HTTP 与很多人熟悉的 2025 版已经是两套明显不同的传输模型。** 2025 版是“一个 HTTP endpoint + POST + 可选独立 GET/SSE + <mark>`Mcp-Session-Id`</mark> + 可恢复 SSE”；2026-07-28 版则把核心模型改成 **stateless、per-request、single-POST** ：每个 JSON-RPC request/notification 独立 POST，request 的响应要么是单个 JSON，要么是“仅属于该 request”的 SSE 流；协议层 session、独立 GET 流、 <mark>`Last-Event-ID`</mark> 恢复和事件 ID 都被移除。 2 

这次改造的真正工程目标不是“更好的 token streaming”，而是 **让 MCP 请求重新成为普通、可路由、可观测、可水平扩展的 HTTP 请求** 。2025 模型要求网关知道 session、sticky routing 或共享 session store，并常常必须解析 JSON 才知道调用的是哪个 method/tool；2026 模型把协议版本、method 和关键名称镜像为 <mark>`MCP-ProtocolVersion` 、</mark> <mark>`Mcp-Method` 、</mark> <mark>`Mcp-Name`</mark> 等 HTTP headers，使 L7 gateway、WAF、rate limiter 和负载均衡器可以不深度解析 JSON body 就做路由和策略判断。 3 

官方 TypeScript SDK v2 已把这个设计实现为 **“one HTTP exchange = one transport instance = 通常一个新 server instance”** ： <mark>`createMcpHandler()`</mark> 是现代入口，内部使用 <mark>`PerRequestHTTPServerTransport` 。</mark> 默认 <mark>`responseMode: "auto"` ：</mark> 如果 handler 直接完成，则返回普通 JSON；如果在最终 result 前产生 progress/logging 等相关消息，则动态升级为 SSE，最后把 terminal JSON-RPC response 放入 SSE 后关闭。SDK 默认 request body 上限是 4 MiB、SSE keepalive 是 15 秒 <mark>、</mark> <mark>`subscriptions/listen`</mark> 默认最多 1024 条并发订阅。 4 

一个尤其值得注意的实现细节是 **backpressure** 。当前 <mark>`perRequestTransport.ts`</mark> 的 SSE 写路径直接调用 Web Streams <mark>`controller.enqueue()` ，</mark> 源码中没有检查 <mark>`desiredSize` ，</mark> 也没有等待 writable drain。 HTTP/2 和 HTTP/3 本身仍有 transport-level flow control，但 SDK 这一层没有显式把慢消费者的压力反馈到 MCP producer。因此，当应用生成事件的速度持续高于网络消费速度时， **JavaScript stream queue / runtime** 5 **buffering 可能增长** ；这是从源码做出的工程推断，而不是官方公布的性能结论。 

当前协议还做了一个看似“倒退”、实际上非常关键的选择： **不再提供 transport-level resumability** 。2026-07-28 changelog 明确移除了 SSE event IDs <mark>、</mark> <mark>`Last-Event-ID`</mark> 和 replay；流断裂时，in-flight result 可能丢失，客户端必须用新的 request ID 重新发起操作。因此，对有副作用的 MCP tool，生产系统应在业务层设计 idempotency key / operation ID，而不能把“HTTP 重试”误认为安全。后半句是基于规范语义的工程建议。 6 

认证也不是 Streamable HTTP 自己重新发明的协议。MCP HTTP authorization 建立在 OAuth 2.1、Bearer Token、RFC 9728 Protected Resource Metadata、RFC 8707 Resource Indicators、RFC 9207 issuer validation 等机制上；access token 要随每个 HTTP request 发送，不能放 query string，server 必须验证 token 的 intended resource/audience，并明确禁止把 MCP client 的 token 原样透传给上游 API。 7 

**一句话评价** ：2026 Streamable HTTP 的核心创新并不是新的 wire-level streaming primitive，而是把 MCP 从“有状态的长连接 RPC over HTTP/SSE”重新塑造成“ **HTTP-native、每请求自描述、可网关路由、必要时局部 SSE streaming 的 RPC binding** ”。这使它在企业 HTTP 基础设施中的部署特性明显优于长期 WebSocket/session 模型，但代价是失去 transport-level resume、真正的单连接 full-duplex，以及需要应用层承担状态外置、幂等和部分慢消费者治理。 8 

## **架构、演进与核心设计** 

### **从 Anthropic MCP 到现代 Streamable HTTP** 

Anthropic 在 2024 年 11 月 25 日宣布并开源 MCP，当时的目标是给 AI 应用与数据源、tools 建立一个通用开放标准。Anthropic 后来在 2025 年 5 月开始让 Claude 的远程 Integrations 使用 remote MCP servers；到 2025 年 12 月 9 日，MCP 被捐赠给 Linux Foundation 的 AAIF，以保持 vendor-neutral、community-driven 的治理模式。 9 

2025 年 3 月 26 日的 Streamable HTTP 首次替代 2024-11-05 的 HTTP+SSE transport。当时的设计仍然是 

session-oriented：POST 用于 client→server 消息，GET 可以建立独立 SSE channel，server 可以利用 session、 SSE event ID 和 <mark>`Last-Event-ID`</mark> 实现恢复。2025-11-25 版本继续维持这一总体模型。 10 

2025 年底 MCP Transport Working Group 明确指出这种架构在 enterprise scale 上的问题：sticky routing、共享 session storage、gateway 深度 JSON 解析以及“session 到底属于 transport 还是应用”的边界变得越来越复杂。随后 SEP-2243 提出把 method/name 等路由字段放进 HTTP headers，最终在 2026-07-28 版本形成新的 stateless transport。 11 

<!-- Start of picture text -->
MCP HTTP transport 演进<br>2024-11-25 2025-03-26 2025-11-25 2025-12-09 2025-12-19 2026-02-04 2026-07-28 2026-08<br>Anthropic Streamable HTTP 2025 版 Streamable Anthropic 将 MCP Transport WG 提出 SEP-2243 推进 HTTP 新 Streamable HTTP TS SDK 出现若干<br>发布并开源 MCP 替代 HTTP + SSE HTTP 延续 session 捐赠给 AAIF / Linux stateless future header 标准化 Streamable HTTP<br>模型 Foundation open issues<br>single POST /<br>初始 HTTP + SSE POST + GET/SSE per-request /<br>transport stateless<br>Session 与<br>resumability header routing /<br>MRTR<br>移除<br>GET、session、Last-Event-ID<br><!-- End of picture text -->

这些节点来自 Anthropic、MCP 官方规范、Transport WG roadmap 和 SEP-2243； **目前没有官方公布下一个 Streamable HTTP transport revision 的确定发布日期** 。 12 

### **现代架构** 

2026 架构可以抽象为： 

<!-- Start of picture text -->
Fresh McpServer instance<br>listen POST<br>subscriptions/listen<br>MCP Client POST /mcp HTTP Gateway / LB / WAF Mcp-Method / Mcp-Namerouting Auth + Origin / Hostvalidation Header / Body validation createMcpHandler External Event Bus<br>JSON or SSE PerRequestHTTPServerTransport JSON result Tool / Resource / Prompthandler<br>progress / related events<br><!-- End of picture text -->

每个 request 都应携带足够协议元数据，因此可以落到 round-robin 后面的任意合适实例；协议不再要求 <mark>`McpSession-Id`</mark> 来把请求粘到原来的 process。需要跨请求的业务状态仍然可以存在，但应显式存在数据库、 cache、state handle 或 tool 参数中，而不是隐藏在 transport session 内。官方 release note 特别强调，“去掉协议 session”并不等同于“所有应用必须无状态”。 13 

#### 这使基础设施职责分层更加清楚： 

|层|主要职责|典型实现|
|---|---|---|
|HTTP edge|TLS、routing、rate limit、WAF、header<br>policy|Envoy、NGINX、cloud LB|
|MCP HTTP<br>binding|Content-Type、协议版本、header/body<br>mirror、HTTP status|`createMcpHandler()`|
|Per-request<br>transport|JSON / SSE response shaping、取消、<br>keepalive|`PerRequestHTTPServerTransport`|
|MCP protocol|JSON-RPC、capabilities、tools/<br>resources/prompts|`McpServer` /<br>`Server`|
|Application|tool逻辑、业务状态、幂等、DB<br>transaction|用户代码|
|Long-lived<br>events|`subscriptions/listen` fan-out|`ServerEventBus` / Redis等|

官方 TypeScript v2 文档明确指出 <mark>`createMcpHandler`</mark> 的 factory 对每个 HTTP request 创建 fresh instance；默认 event bus 是 process-local，多进程部署若希望所有 <mark>`subscriptions/listen`</mark> 客户端都接收到事件，需要提供外部 pub/sub-backed <mark>`ServerEventBus` 。</mark> 14 

### **为什么把 method/name 放到 headers** 

SEP-2243 的动机非常明确：如果 tool name 只在 JSON body 中，负载均衡器、WAF、rate limiter、API gateway 和 observability middleware 都必须先 parse body，甚至重新序列化或 buffer 请求 <mark>。</mark> <mark>`Mcp-Method`</mark> 和 <mark>`McpName`</mark> 把 routing key 提升到 HTTP metadata 层。 15 

例如 gateway 可以执行： 

```
Mcp-Method = tools/call
Mcp-Name   = database-query
              │
              ├──> DB-tool service pool
              │
Mcp-Name   = browser-render
              └──> browser sandbox pool
```

这不意味着 header 取代 JSON body。规范明确要求 **body 仍是 source of truth** ，server 必须验证 mirror header 与 body 是否一致；否则攻击者可能制造“WAF 看见 A、应用执行 B”的 parser differential / routing confusion。header/body mismatch 在当前规范中应以 HTTP 400 和 JSON-RPC <mark>`-32020 HeaderMismatch`</mark> 处理。 16 

## **线协议、数据流与控制流** 

### **Request 和 response 的基本交换** 

现代 Streamable HTTP 的最小单位是 **一个 HTTP POST exchange** 。客户端对每个 JSON-RPC request 或 notification 发送一个独立 POST；POST 的 <mark>`Accept`</mark> 必须声明能够处理 JSON 与 SSE。notification 成功接收后返回空的 <mark>`202 Accepted` ；</mark> 有 <mark>`id`</mark> 的 request 最终返回普通 JSON 或 SSE。 17 

一个现代 `tools/call` 在 wire 上概念上类似： 

```
POST/mcpHTTP/1.1
Host:mcp.example.com
Content-Type:application/json
Accept:application/json, text/event-stream
MCP-Protocol-Version:2026-07-28
Mcp-Method:tools/call
Mcp-Name:search
Authorization:Bearer <access-token>
{
"jsonrpc":"2.0",
"id":42,
"method":"tools/call",
"params":{
"name":"search",
"arguments":{
"query":"streamable http"
},
"_meta":{
"io.modelcontextprotocol/protocolVersion":"2026-07-28"
}
```

```
}
```

```
}
```

这里最重要的语义不是具体大小写——HTTP field names 本身大小写不敏感——而是协议版本和路由 metadata 必须与 JSON envelope 一致；所有 POST 都需要现代协议版本 header，request 还需要 <mark>`Mcp-Method` ，</mark> 而 <mark>`tools/call` 、</mark> <mark>`resources/read` 、</mark> <mark>`prompts/get`</mark> 等要求对应 <mark>`Mcp-Name` 。</mark> 18 

TypeScript client 当前实现会从 message body 派生这些 headers；源码中可以看到类似： 

```
headers.set('mcp-method',message.method);
```

这正是 body→HTTP metadata mirroring 的实现位置之一；文件为 <mark>`packages/client/src/client/ streamableHttp.ts` 。</mark> 19 

### **Header 体系** 

|Header|当前用途|现代版状态|
|---|---|---|
|`Content-Type: application/json`|request body media type|必需|
|`Accept: application/json, text/event-`<br>`stream`|客户端接受普通JSON或流式结<br>果|必需|
|`MCP-Protocol-Version`|当前request的MCP revision|必需|
|`Mcp-Method`|JSON-RPC method的HTTP<br>mirror|request必需|
|`Mcp-Name`|tool/resource/prompt名称的<br>route hint|特定方法必需|
|`Mcp-Param-*`|schema明确允许的参数mirror|条件性|
|`Authorization: Bearer …`|OAuth access token|受保护endpoint<br>必需|
|`Mcp-Session-Id`|2025 transport session|**2026已移除**|
|`Last-Event-ID`|2025 SSE resume|**2026已移除**|

当前规范还提供 <mark>`x-mcp-header`</mark> schema extension：显式标记后，参数可镜像为 <mark>`Mcp-Param-{Name}` 。</mark> 由于 HTTP header 对任意 Unicode/control characters 并不安全，规范定义了 value conversion，包括在必要情况下使用 <mark>`=?base64?...?=`</mark> 形式。未知 MCP custom headers 应能穿过中间代理。 20 

这项设计的安全要求非常重要： 

<!-- Start of picture text -->
POST /mcp<br>解析 MCP headers 解析 JSON body<br>Header 与 Body 一致?<br>否是<br>HTTP 400<br>Protocol routing /<br>JSON-RPC -32020<br>HeaderMismatch dispatch<br><!-- End of picture text -->

也就是说， <mark>`Mcp-Name: harmless-tool`</mark> 不能与 body 里的 <mark>`tools/call -> privileged-tool`</mark> 共存而让网关与应用产生不同判断。 21 

### **JSON 模式与 SSE 模式** 

普通快速请求可以直接： 

<!-- Start of picture text -->
POST /mcp<br>      │<br>      ├─ handler executes<br>      │<br>      └──────── 200 application/json ────────><br><!-- End of picture text -->

如果中间需要 progress/logging 或其他与本 request 关联的输出： 

<!-- Start of picture text -->
MCP Client HTTP Handler PerRequestTransport Tool Handler<br>POST tools/call<br>create per-request transport<br>dispatch JSON-RPC request<br>related progress/log message<br>HTTP 200 text/event-stream<br>event: message / data: progress...<br>terminal JSON-RPC result<br>event: message / data: result...<br>EOF<br>MCP Client HTTP Handler PerRequestTransport Tool Handler<br><!-- End of picture text -->

<mark>`responseMode: "auto"`</mark> 正是这一行为：没有 mid-call message 时返回单一 JSON；第一次出现相关中间消息时才 lazy-upgrade 为 SSE。 <mark>`"sse"`</mark> 强制始终流式， <mark>`"json"`</mark> 则禁止流式并丢弃 terminal result 之前的相关消息。 22 

当前 TypeScript 实现的 SSE framing 非常直接。源码路径： 

```
packages/server/src/server/perRequestTransport.ts
```

其中 <mark>`writeMessageFrame()`</mark> 的核心是： 

```
this.writeFrame(`event: message\ndata: ${JSON.stringify(message)}\n\n`);
```

随后 <mark>`writeFrame()` ：</mark> 

```
this._sse.controller.enqueue(this._sse.encoder.encode(frame));
```

这是标准 SSE 文本 framing，而不是 MCP 自己的 binary frame。每个 message 的 MCP/SSE 固定 framing 开销约为 **23 bytes + JSON bytes** ，不含 HTTP headers、HTTP/2/3 DATA frame 或 TLS/QUIC overhead。 23 

WHO/WHATWG 的 SSE format 也是以空行终止 event；不过一个关键差别是，浏览器传统 <mark>`EventSource`</mark> API 是面向 GET 建连的，而现代 MCP 的 request-scoped SSE 是 **POST response body** 。因此 MCP browser client 通 

常应通过 <mark>`fetch()`</mark> + streaming body/SSE parser 读取，而不能简单把 POST endpoint 丢给 <mark>`new EventSource()` 。</mark> 24 

### **“Chunking”究竟发生在哪一层** 

Streamable HTTP **没有定义“一个 JSON-RPC event 必须对应一个 TCP chunk、HTTP/2 DATA frame 或 QUIC packet”** 。应用层只定义 SSE event boundary；底层 runtime、TLS、proxy 和 HTTP implementation 可以拆分或合并 byte chunks。SSE parser 必须按照文本 framing 重组，而不是把一次 socket/read 调用当作一个 MCP message。 25 

因此下面两种网络传输在 MCP 语义上完全等价： 

应用 `: event: message\ndata: {...}\n\n Wire A: [ event: message\n ][ data: {...}\n\n ] Wire B: [ eve ][ nt: message\ndata: { ][ ... }\n ][ \n ]` 

HTTP/2 会把 body 映射到 DATA frames，并具有 stream/connection flow control；HTTP/3 则把一个 requestresponse exchange 映射到 QUIC stream，提供 per-stream flow control，并消除了 HTTP/2/TCP 中“一个 TCP packet loss 阻塞同一连接全部 streams”的 transport-level head-of-line 问题。 26 

### **Backpressure** 

这里当前官方 TypeScript 实现存在一个值得重点关注的工程点。 <mark>`PerRequestHTTPServerTransport.writeFrame()`</mark> 调用： 

```
controller.enqueue(bytes)
```

但源码中找不到对 <mark>`ReadableStreamDefaultController.desiredSize`</mark> 的检查，也没有可等待的 <mark>`writer.write()`</mark> / drain path。也就是说，从 SDK transport 这一层看，没有显式的 producer throttling。 27 

这并不等于“完全没有 backpressure”：HTTP/2 有 flow-control window，HTTP/3/QUIC 也有 stream-level flow control。问题是这些网络信号是否、以及以多快速度向上反馈至 JavaScript producer，取决于 runtime 的 Web Streams→HTTP adapter；SDK 自己没有显式等待该反馈。因此对于高频 progress/log stream，应该专门做 slow-reader memory test，而不是假设 <mark>`enqueue()`</mark> 自动限制应用生成速率。 28 

### **Keepalive、取消和断线** 

SDK 在 SSE mode 默认每 **15,000 ms** 发送 comment frame keepalive <mark>；</mark> <mark>`writeCommentFrame()`</mark> 生成 SSE comment，而不是 MCP JSON-RPC message。当前源码还给 SSE response 设置 

`Cache-Control: no-cache, no-transform` 与 `X-Accel-Buffering: no` ，后者旨在避免 NGINX 类代理把流攒起来再整体发送。 29 

当前协议把关闭 request-scoped SSE stream 视为 cancellation mechanism；2026 HTTP transport 不再依赖旧式 transport session 内的 <mark>`notifications/cancelled` 。</mark> SDK 若 runtime 为原始 HTTP request 提供 abort signal，也会在 client disconnect 时关闭这一 exchange。 30 

更关键的是，2026 规范 **明确移除了 resumability** 。如果 SSE 在最终 JSON-RPC response 之前断开： 

<!-- Start of picture text -->
Client Server<br>POST request id=41<br>progress event<br>network failure<br>无 Last-Event-ID replay<br>POST same logical operation, new JSON-RPC id=42<br>new result<br>Client Server<br><!-- End of picture text -->

协议要求客户端重新发起 request，而不是 <mark>`Last-Event-ID`</mark> resume；因此 server 对非幂等 tool 最好额外接受业务级 operation/idempotency identifier。后者不是 MCP normative requirement，而是由 reissue 语义直接推导出的生产建议。 6 

与此相反，TypeScript SDK 里的 <mark>`StreamableHTTPClientTransport`</mark> 仍能看到 <mark>`resumeStream(lastEventId)` 、</mark> retry scheduler <mark>、</mark> <mark>`Mcp-Session-Id`</mark> 等代码。这些是 **2025-era compatibility path** ，不是 2026 transport 的恢复机制；旧客户端默认 retry 参数包括 1 秒初始延迟、30 秒最大延迟、1.5 growth factor 和有限重试。分析源码时必须把“multi-era SDK code”与“current normative protocol”分开，否则很容易误判 2026 Streamable HTTP 仍支持 resume。 31 

### **MRTR：为什么不再需要传统 server-initiated request** 

旧版 MCP 可以借 session-wide stream 让 server 主动向 client 发起 elicitation、sampling、roots 等 request。 2026 revision 将这类交互重构为 **Multi-Round-Trip Requests（MRTR）** ：server 返回 

`InputRequiredResult` ，其中描述所需 input；client 获得数据后重新执行原始 operation，并携带 <mark>`inputResponses` /</mark> <mark>`requestState` 。</mark> 32 

<!-- Start of picture text -->
Client MCP Server User / Host<br>tools/call(request)<br>InputRequiredResult + requestState<br>collect / approve requested input<br>input<br>retry original request + inputResponses + requestState<br>final result<br>Client MCP Server User / Host<br><!-- End of picture text -->

这是当前 transport 去 session 化的一个关键条件：server 无需保持一条长期双向 RPC channel 等待 client response，也减少了把 request routing 固定到某个 backend process 的必要性。 33 

## **SDK、模块与源码剖析** 

### **TypeScript v2 的主要模块** 

官方 TypeScript SDK v2 与 2026-07-28 spec 同步，代码拆成 client、server、Node/Express/Fastify/Hono 等 package；v1 仍处于兼容维护窗口，但现代实现应优先分析 v2。 34 

#### 最值得阅读的文件如下： 

|文件|关键符号|工程作用|
|---|---|---|
|`packages/server/src/`<br>`server/`|`createMcpHandler()` 、<br>`isLegacyRequest()`|HTTP entry、era<br>classification、<br>d/l|
|`createMcpHandler.ts`||moernegacy<br>routing|

|文件|关键符号|工程作用|
|---|---|---|
|`packages/server/src/`<br>`server/`<br>`perRequestTransport.ts`|`PerRequestHTTPServerTransport`|2026单请求<br>transport核心|
|`packages/server/src/`<br>`server/requestBody.ts`|`readRequestBody()`|request body<br>size / parsing<br>guard|
|`packages/server/src/`<br>`server/`<br>`serverEventBus.ts`|event bus实现|`subscriptions/`<br>`listen` fan-out|
|`packages/server/src/`<br>`server/`|`WebStandardStreamableHTTPServerTransport`|2025/session-<br>oriented<br>compatibility|
|`streamableHttp.ts`||transport|
|`packages/client/src/`<br>`client/`<br>`streamableHttp.ts`|`StreamableHTTPClientTransport`|HTTP client、<br>headers、legacy<br>compatibility/<br>resume|
|Node adapter package|`toNodeHandler()`|Web Standard<br>Request/Response<br>↔Node HTTP|
|middleware modules|bearer/origin/host auth validators|HTTP security<br>boundary|

这些路径和公开 API 均可从 TypeScript SDK v2 API docs 和 GitHub source 追踪；尤其要注意 <mark>`streamableHttp.ts`</mark> 是 multi-era/legacy machinery，而 <mark>`perRequestTransport.ts`</mark> 才是最清晰的 2026 per-request implementation。 35 

### **<mark>`createMcpHandler.ts`</mark>** 

<mark>`createMcpHandler()`</mark> 定义于： 

```
packages/server/src/server/createMcpHandler.ts:674
```

返回的 <mark>`McpHttpHandler`</mark> 是 Web-standard： 

```
{
fetch,
close,
notify,
```

```
bus
}
```

Node/Express 等再通过 <mark>`toNodeHandler()`</mark> 做 adapter。factory 每个 HTTP request 调用一次，得到 fresh <mark>`McpServer`</mark> 或低层 <mark>`Server` ；</mark> context 提供 <mark>`era: "modern" | "legacy"` 、</mark> <mark>`authInfo`</mark> 和原始 <mark>`requestInfo` 。</mark> 36 

其重要 option： 

|Option|默认|意义|
|---|---|---|
|`responseMode`|`auto`|JSON或lazy SSE|
|`legacy`|`stateless`|兼容2025-era请求|
|`maxRequestBodySize`|4 MiB|handler自己读取body时的上限|
|`maxSubscriptions`|1024|同handler的listen streams上限|
|`keepAliveMs`|15000|SSE comment heartbeat|
|`bus`|in-process|可换成跨process pub/sub|
|`onerror`|—|out-of-band error reporting|

这些默认值均来自当前 SDK v2 API reference。 36 

一个面向现代 SDK 的 TypeScript server 可以按如下结构组织；这是按当前 API 改写的可实现模式，而不是逐字复制官方示例： 

```
import{McpServer,createMcpHandler}from"@modelcontextprotocol/server";
import{toNodeHandler}from"@modelcontextprotocol/node";
import*aszfrom"zod/v4";
consthandler=createMcpHandler(
()=>{
constserver=newMcpServer({
name:"catalog-service",
version:"1.0.0",
});
server.registerTool(
"search",
{
description:"Search catalog",
inputSchema:z.object({
query:z.string(),
}),
```

`}, async ({ query }) => ({ content: [ { type: "text", text: `Result for: ${query}` }, ], }), ); return server; }, { responseMode: "auto", legacy: "stateless", maxRequestBodySize: 4 * 1024 * 1024, }, ); //` 在 `node:http / Express/Fastify` 中由对应 `adapter` 挂载： `// const nodeHandler = toNodeHandler(handler);` 

<mark>`registerTool` 、</mark> <mark>`createMcpHandler` 、</mark> fresh-per-request factory 和 Node adapter 都是当前官方 SDK API。 37 

如果 endpoint 只希望接受 2026 modern traffic，可以配置： 

```
consthandler=createMcpHandler(factory,{
legacy:"reject",
});
```

默认的 <mark>`legacy: "stateless"`</mark> 则会对 2025-era 请求用同一 factory 创建一次性的 stateless legacy server； GET/DELETE session 操作不会因此重新获得 sessionful semantics。 36 

### **<mark>`perRequestTransport.ts`</mark>** 

当前实现的核心 class 位于： 

```
packages/server/src/server/perRequestTransport.ts:122
```

关键方法为： 

```
start()             : line 156
handleMessage()     : line 173
send()              : line 241
```

```
writeCommentFrame() : line 333
close()             : line 344
```

官方 API 对它的描述非常准确： **“整个 lifetime 就是一个 HTTP exchange 的真正 Transport”** ； <mark>`handleMessage()`</mark> 第二次调用会报错，因为该 transport 严格 single-use。 38 

源码的实际控制路径可以简化为： 

```
flowchart TD
    I[handleMessage] --> D[Dispatch to Server]
    D --> O{send(message)}
    O -->|notification input| A[202 Accepted]
    O -->|terminal result, no prior stream| J[200 application/json]
    O -->|related message first| U[upgradeToSse]
    U --> Q[enqueue SSE frame]
    Q --> O
    O -->|terminal result after SSE| F[enqueue final frame]
    F --> X[close stream + transport]
```

如果 response 尚未 committed，validation ladder 的某些 JSON-RPC errors 可以映射成相应 HTTP status；一旦 SSE <mark>`200`</mark> 已经发出，后续错误就只能作为 SSE 中的 JSON-RPC error message 发送，因为 HTTP status 已经无法改变。源码特别处理了这一 committed/uncommitted distinction。 39 

<mark>`upgradeToSse()`</mark> 创建 <mark>`ReadableStream<Uint8Array>` ；</mark> consumer cancel 会调用 transport <mark>`close()` ，</mark> keepalive timer 随 stream 生命周期创建和销毁。当前 response headers 中包括： 

```
Content-Type: text/event-stream
Cache-Control: no-cache, no-transform
Connection: keep-alive
X-Accel-Buffering: no
```

23 这解释了 SDK 对 reverse proxy buffering 的明确考虑。 

一个值得代码审查团队关注的点仍是： 

```
this._sse.controller.enqueue(this._sse.encoder.encode(frame));
```

没有 <mark>`desiredSize`</mark> gate。对于每秒几十或几百个小 progress event 一般未必构成问题，但高频、大 payload、慢 reader 场景必须压测，因为源码并未提供显式 bounded application queue。这个结论是源码分析推论。 40 

### **<mark>`requestBody.ts`</mark>** 

当前 SDK 在 HTTP entry 层做 body-boundary 防护。 <mark>`readRequestBody()`</mark> 会首先利用 <mark>`Content-Length`</mark> 尽可能提前拒绝过大的请求，即使没有可信长度，也会在实际读取字节超过 limit 后终止；默认上限是 **4 MiB** 。 41 

这很重要，因为“streamable HTTP”并不意味着 inbound request body 无限流式处理 JSON-RPC：现有实现仍需得到并解析 JSON message。4 MiB 是 SDK 默认值，而不是 HTTP 或 MCP 理论最大值。 36 

### **<mark>`streamableHttp.ts` ：</mark> 为什么源码容易误导** 

另一个文件： 

```
packages/server/src/server/streamableHttp.ts
```

包含 <mark>`WebStandardStreamableHTTPServerTransport` 、</mark> session ID <mark>、</mark> <mark>`EventStore` 、</mark> GET/DELETE、 <mark>`Last-Event-ID`</mark> 和 SSE replay 等 machinery。这是 SDK 为 2025-era / migration compatibility 保留的实现，不应把这里所有行为都解释成 2026 normative semantics。 42 

它的 legacy SSE writer 同样形成： 

```
event: message
id: <optional event id>
data: <JSON>
```

而事件 ID/replay 正是 2026 current transport 明确移除的东西。 43 

### **Client API** 

当前 TypeScript client 的基本结构仍很简单： 

```
import{
Client,
StreamableHTTPClientTransport,
}from"@modelcontextprotocol/client";
```

```
constclient=newClient(
```

```
{name:"my-client",version:"1.0.0"},
{versionNegotiation:{mode:"auto"}},
);
```

```
consttransport=newStreamableHTTPClientTransport(
newURL("https://mcp.example.com/mcp"),
```

```
);
```

```
awaitclient.connect(transport);
constresult=awaitclient.callTool({
name:"search",
arguments:{query:"MCP"},
});
```

官方 client 文档使用 <mark>`Client`</mark> + <mark>`StreamableHTTPClientTransport` ；</mark> 对双时代部署，显式 <mark>`versionNegotiation: { mode: "auto" }`</mark> 会尝试较新的协议并在需要时退回 2025-era，而 pin 模式可以要求 2026-07-28，不接受 fallback。 44 

因此迁移期应 **明确配置 negotiation policy** ，而不要凭 SDK class 名称猜它正在使用哪个时代的 wire semantics。 45 

### **Python** 

官方 MCP Python SDK 同样支持 Streamable HTTP；官方仓库给出的运行方式包括： 

```
uvrunmcprunserver.py--transportstreamable-http
```

客户端则可以面向一个 HTTP MCP URL 建立连接。Python repo 中还存在： 

```
src/mcp/server/streamable_http.py
```

等具体传输实现。与 TypeScript 一样，在阅读 Python 源码时也必须区分当前协议和兼容 2025-era 的 session/ resume 代码。 46 

### **实现一个兼容 server 的伪代码** 

从 wire semantics 角度，一个最小 modern server 大致是： 

```
function handlePOST(req):
    require Content-Type == application/json
    require acceptable Origin / Host
    authenticate Bearer token if endpoint protected
```

```
    body = read_body(max = configured_limit)
    msg  = parse_json(body)
```

```
    require req.MCP-Protocol-Version == msg._meta.protocolVersion
    require req.Mcp-Method == msg.method
    if method has route-name:
```

```
        require req.Mcp-Name == corresponding body field
```

```
    if msg is notification:
        dispatch(msg)
        return HTTP 202 with empty body
    transport = new PerRequestTransport()
    start handler(msg)
```

```
    if handler returns terminal result before any related message:
        return HTTP 200 application/json(result)
    else:
        return HTTP 200 text/event-stream:
            for each related event:
                emit "event: message\ndata: <json>\n\n"
            emit terminal result
            close stream
```

这一结构直接对应 current spec 与 TypeScript v2 <mark>`createMcpHandler` /</mark> <mark>`PerRequestHTTPServerTransport` 。</mark> 47 

## **性能、基准与扩展部署** 

### **已公布性能数据** 

在本次检索的 **当前 MCP specification、2026-07-28 release note、TypeScript SDK docs/GitHub 和 Python SDK** 中，我没有找到由 MCP/Anthropic 官方发布的、可复现的 Streamable HTTP 标准 benchmark，例如固定硬件上的 P50/P95 latency、requests/sec、SSE events/sec 或 memory-per-stream。官方材料目前更关注协议架构、扩展性和 API，而不是宣称某个吞吐数字。 48 

因此，给出诸如“Streamable HTTP 能跑 100k RPS”或“额外延迟低于 1 ms”的固定数字都没有官方依据。其性能高度依赖 Node/Bun/Deno runtime、HTTP/1.1 vs H2/H3、TLS termination、proxy buffering、JSON payload、 49 auth verifier、tool handler、数据库和 event rate。 

### **可以从协议确定的固定成本** 

现代协议在热连接上，一个普通 RPC 不要求额外 transport handshake： 

```
POST request  ───────────>
              application work
<──────────── HTTP response
```

也就是说， **SSE upgrade 仍然是同一个 POST response** ，不是再开一次独立 stream handshake。这与 2025-era 需要维护 session/独立 GET SSE channel 的模型明显不同。 50 

应用级 SSE framing 固定增加约： 

```
"event: message\n"   = 15 bytes
"data: "             =  6 bytes
"\n\n"               =  2 bytes
                       --------
                         23 bytes/event
```

再加 JSON payload。本数字由 SDK 实际 framing 字符串直接计算得出，不含 HTTP/TLS/QUIC overhead。 23 

15 秒 keepalive 的 framing 是很小的固定开销，因此低事件速率下网络成本通常不会由 heartbeat 主导；但大量常驻 subscriptions 时，需要乘以并发 stream 数量。默认 1024-subscription cap 也说明 SDK 维护者明确把长驻流视为需要资源边界的对象。 36 

### **建议基准设计** 

应该至少分别测 **JSON fast path、request-scoped SSE、subscriptions/listen、slow reader、现代 stateless scale-out** 。推荐覆盖以下实验空间；这里的数字是 **测试范围** ，不是官方性能承诺： 

|维度|建议sweep|
|---|---|
|JSON payload|512 B、4 KiB、64 KiB、1 MiB、接近4 MiB|
|并发requests|1、10、100、1k、5k+|
|SSE event rate|1、10、100、1k events/s/stream|
|SSE stream数|1、100、1k，以及配置上限附近|
|RTT|localhost、1 ms、20 ms、80 ms、150 ms|
|packet loss|0、0.1%、1%、2%|
|HTTP|H1.1、H2、H3（基础设施支持时）|
|auth|none、local JWT verify、remote introspection|
|response mode|`json` 、<br>`auto` 、<br>`sse`|

测量公式可以拆解为： 

```
T_total
```

- `≈ T_connection` 

- `+ T_HTTP/gateway` 

- `+ T_auth` 

- `+ T_body_parse` 

- `+ T_MCP_validation` 

- `+ T_handler` 

- `+ T_serialize` 

- `+ T_network_response` 

对 warm H2/H3 connection <mark>，</mark> <mark>`T_connection`</mark> 可以摊薄；对冷连接则要分别统计 TCP/TLS 或 QUIC/TLS establishment，这不是 MCP 本身的成本。HTTP/2 与 HTTP/3 的连接和 multiplexing 行为由各自 RFC 定义。 26 

SSE 应测两个 latency： 

`TTFE = POST` 开始 `-> first SSE event TTFR = POST` 开始 `-> terminal JSON-RPC result` 

仅看 terminal latency 会掩盖 streaming 对用户体验的价值。 

### **Slow-reader / backpressure benchmark** 

这是我认为当前实现 **最值得专门测试的一项** ： 

```
Producer: 1 MB/s of SSE events
         |
         v
PerRequestTransport
 controller.enqueue(...)
         |
         v
Client reads only 10 KB/s
```

同时记录： 

```
process RSS
JS heap used
ReadableStream queued bytes
GC pause
event latency
connection termination behavior
```

由于当前源码没有 <mark>`desiredSize`</mark> gate，测试假设应该是：如果 runtime adapter 未能充分限制 producer， queue memory 可能随 producer-consumer gap 增长。只有实际 benchmark 才能确定具体 runtime 的行为。 40 

### **水平扩展** 

2026 设计最大的性能优势很可能不在单节点 microbenchmark，而在 **系统级扩展性** ： 

<!-- Start of picture text -->
Clients MCP instance A Shared application state<br>Clients Stateless LB MCP instance B<br>Clients MCP instance C<br>Redis / PubSub Event Bus<br><!-- End of picture text -->

普通 POST 不需要 protocol session affinity，因此可进行 round-robin / least-request routing。跨请求业务状态放 DB/cache/state handle <mark>；</mark> <mark>`subscriptions/listen`</mark> 等跨节点通知则应通过外部 event bus 发布。默认 <mark>`InMemoryServerEventBus`</mark> 只覆盖当前 process。 51 

相比 2025 sessionful deployment： 

|维度|2025 sessionful|2026 per-request|
|---|---|---|
|Sticky routing|常常需要|普通请求不需要|
|Session store|可能需要共享|协议层不需要|
|Backend failover|session迁移复杂|新request可去任意实例|
|Gateway body parsing|往往需要method/tool信息|headers可直接路由|
|Auto-scaling|受session drain约束|更接近普通HTTP|
|SSE stream|可是session-wide|request-scoped / subscription|
|Application state|常混在transport state|应显式外置|

这正是 Transport WG 从 2025 架构转向 2026 架构的核心原因。 

### **Proxy / ingress 配置** 

SSE endpoint 必须避免 reverse proxy 长时间 buffering；SDK 自身在 modern SSE response 中发送 <mark>`X-AccelBuffering: no`</mark> 和 <mark>`Cache-Control: no-cache, no-transform` ，</mark> 但生产环境仍应检查 ingress 

timeout、idle timeout、maximum response duration、connection draining 和 load-balancer buffering 策略。 23 

对于 subscription streams，还需要配置优雅 shutdown：先停止接收新 subscription，向 LB 标记 instance draining，再关闭现有 streams，避免 deployment rollout 产生大规模同步 reconnect。 

## **安全、认证与协议兼容性** 

### **Origin、Host 与 DNS rebinding** 

当前 Streamable HTTP spec 要求 server 验证 <mark>`Origin` ；</mark> 无效 Origin 应返回 <mark>`403` ，</mark> 而本地 server 应优先绑定 <mark>`127.0.0.1`</mark> 而不是所有 interfaces，以缓解 DNS rebinding。 17 

这里存在一个很重要的 SDK integration trap <mark>：</mark> <mark>`createMcpHandler()`</mark> 本身 **有意不替你完成所有 Host/Origin validation** ；官方文档要求在 bare fetch runtime 前加相应 middleware。Express helper 则会针对 localhost 默认执行 Host/Origin 防护。 53 

因此生产架构应类似： 

```
Internet
   |
 TLS
   v
[Host allowlist]
   |
[Origin policy]
   |
[OAuth Bearer validation]
   |
[Rate limit / body limit]
   |
[createMcpHandler]
```

而不是把 <mark>`createMcpHandler.fetch`</mark> 直接暴露到公网后假设 MCP SDK 自动承担完整 HTTP perimeter security。 54 

### **OAuth / Bearer authentication** 

MCP authorization 对 HTTP transport 是 optional feature；一旦启用，规范把 MCP server 定位为 OAuth resource server。当前要求包括 Protected Resource Metadata discovery、Authorization Server discovery、 Resource Indicators，以及 Bearer token 使用。 55 

客户端调用受保护 endpoint： 

```
Authorization: Bearer <access-token>
```

必须在 **每个相关 HTTP request** 上带 token，不能用： 

```
/mcp?access_token=...
```

server 必须验证 token 确实是为自己这个 resource 签发，包括 intended audience/resource。无效或过期 token 应返回 <mark>`401` ；</mark> scope 不足通常使用 <mark>`403`</mark> + <mark>`WWW-Authenticate: Bearer error="insufficient_scope"...` 。</mark> 55 

当前认证 discovery 涉及： 

- RFC 9728 Protected Resource Metadata； 

- RFC 8414 authorization server metadata； 

- 

- RFC 8707 resource indicator； 

- 

- RFC 9207 authorization-response issuer identification； 

- • OAuth 2.1 / PKCE。 7 

2026 authorization hardening 特别加强了 <mark>`iss`</mark> validation，以降低 OAuth mix-up attack 风险。 56 

### **Token passthrough 是明确禁止的** 

如果 MCP server 又调用第三方 API： 

`MCP client | Token A v MCP server | |` 不能原样转发 `Token A v Third-party API` 

正确模式是 MCP server 作为另一个 OAuth client，获取 **Token B** 给 upstream resource 使用。官方 security considerations 明确禁止把 MCP client→server 的 token 原样作为 downstream/upstream credential。 57 

### **Header/body mismatch 是安全边界** 

由于网关可能只看： 

```
Mcp-Method
Mcp-Name
Mcp-Param-*
```

而 application 看 body，因此它们必须 cryptographically/semantically 一致到足以避免策略绕过。当前 spec 要求 server cross-check，失配返回 <mark>`400 / -32020` 。</mark> 21 

实际部署还应确保代理 **不删除这些 MCP headers** ，也不要让未受信任的外部 proxy 自行重写 <mark>`Mcp-Method` /</mark> <mark>`Mcp-Name`</mark> 后绕过最终 server cross-check。 

### **DoS 与资源上限** 

默认 4 MiB body limit 是防止巨大 JSON request 占用 parsing/memory 的第一层 <mark>；</mark> <mark>`maxSubscriptions: 1024`</mark> 则为长驻 streams 提供并发边界。公网服务还应在 edge 上分别限制 request rate、并发 SSE streams、 36 tool-specific concurrency 和 token verification 成本。 

SSE keepalive 会让 idle streams 长期保持活跃，因此 subscription endpoints 特别需要 per-principal quota，而不仅是全局 connection limit。 

### **与 HTTP/2、HTTP/3 的关系** 

#### **HTTP/2 和 HTTP/3 不是 Streamable HTTP 的竞争协议，而是 Streamable HTTP 可以运行其上的 HTTP transport versions。** 

HTTP/2 提供 binary framing、header compression、多个 concurrent exchanges 和 flow control，但仍受底层 TCP packet loss 导致跨 stream head-of-line blocking 的影响。 58 

HTTP/3 把相同 HTTP semantics 映射到 QUIC，每个 request-response 使用独立 QUIC stream，具有 per59 stream flow control；一个 stream 的 packet loss 不会像 H2/TCP 那样直接停止其他独立 streams 的进展。 

因此，现代 Streamable HTTP 的“每个 JSON-RPC request 一个 POST”模型与 H2/H3 multiplexing 很自然地组合： 

```
One H2/H3 connection
```

```
├─ HTTP stream A -> MCP tools/call #1
├─ HTTP stream B -> MCP tools/call #2
├─ HTTP stream C -> MCP resources/read
└─ HTTP stream D -> long-lived subscriptions/listen
```

这一点在连接复用上比“每个调用创建新 TCP connection”高效得多。 26 

### **与 SSE、WebSocket、WebTransport 的比较** 

|特性|MCP<br>Streamable<br>HTTP 2026|传统SSE|WebSocket|WebTransport|
|---|---|---|---|---|
|基础协议|HTTP|HTTP|WS framing over<br>TCP/HTTP<br>handshake|HTTP/3/QUIC<br>binding|
|Client→Server|独立POST|通常另发HTTP|同连接双向|双向streams/<br>datagrams|
|Server→Client|JSON或<br>request-<br>scoped SSE|长驻单向event<br>stream|同连接双向|多stream +<br>datagram|
|Full duplex|非传统单连接<br>full-duplex|否|是|是|
|Unreliable<br>datagram|否|否|否|是|
|HTTP gateway<br>友好度|很高|很高|中等|基础设施成熟度较低|
|普通HTTP auth|原生|原生|handshake后自行<br>维护|可基于<br>WebTransport<br>origin/auth|
|Header-based<br>L7 routing|原生设计目标|可做|handshake后粒度<br>较粗|需专门infra|
|Current MCP<br>resume|**无**|EventSource可有<br>`Last-Event-ID`|应用自定义|应用自定义|
|Browser<br>primitive|`fetch`<br>streaming|`EventSource`|`WebSocket`|`WebTransport`|
|Proxy<br>compatibility|强|强|普遍但需upgrade<br>支持|尚依赖H3/<br>WebTransport stack|
|MCP official<br>transport|是|仅framing /历史<br>transport|否|否|

WebSocket RFC 6455 的目标就是提供一个持久双向 message-oriented channel，因此在极低延迟、频繁双向事件方面比 request/response HTTP 更直接，但它也天然把更多状态附着于连接；传统 HTTP gateway 的 perrequest caching、method routing、retry、authorization policy 和 autoscaling 通常更容易套在 Streamable HTTP 上。 60 

WebTransport 则更接近“现代 QUIC-native full duplex”：提供 bidirectional/unidirectional streams 与 datagrams。不过截至 2026 年 7 月，IETF 的 WebTransport-over-HTTP/3 仍以 <mark>`draft-ietf-webtranshttp3-16`</mark> 形式推进，W3C WebTransport API 与之协同发展；MCP 当前并没有把它作为标准 transport。 61 

SSE 在 MCP 2026 中更准确的定位是 **一种 HTTP response representation** ，而不是整个 transport 

architecture <mark>。</mark> <mark>`text/event-stream`</mark> 负责增量 server→client 数据；client→server、routing、auth、version negotiation 都仍是普通 HTTP POST。 62 

### **Anthropic 产品兼容性** 

Anthropic 当前 MCP Connector 要求 remote MCP server 可公开通过 HTTP 访问，并支持 Streamable HTTP 和 SSE transport；该 connector 文档当前仍声明它只支持 MCP feature set 中的 tool calls。 63 

Claude Code 配置则把： 

```
{
"type":"streamable-http",
"url":"https://example.com/mcp"
}
```

视为 HTTP transport， <mark>`streamable-http`</mark> 也可作为 <mark>`http`</mark> 的 alias；Anthropic 文档明确指出名称来自 MCP 64 specification。 

## **迁移、部署模式与工程建议** 

### **从旧 HTTP+SSE / 2025 Streamable HTTP 迁移** 

迁移最容易出错的是认为只要“升级 SDK package version”就完成了。真正变化的是 transport state model。 

|旧模型|现代模型|
|---|---|
|session initialization后保存<br>`Mcp-Session-Id`|不依赖protocol session|
|GET建立独立server event stream|无独立transport GET stream|
|DELETE销毁transport session|无protocol session可DELETE|
|`Last-Event-ID` 恢复|无replay|
|server-initiated RPC|MRTR|
|sticky backend常见|普通POST可stateless LB|
|transport隐式保存状态|application state显式传递/外置|
|gateway解析JSON做routing|`Mcp-Method` /<br>`Mcp-Name`|

2026 current spec 的 backward-compatibility section 明确列出这些旧能力，并说明它们不是现代 transport 的一部分。 65 

#### 推荐采用“双腿迁移”： 

<!-- Start of picture text -->
Incoming MCP request<br>Protocol era?<br>2026-07-28 2025-era<br>Modern Legacy compatibility<br>createMcpHandler handler<br>Shared server factory /<br>business logic<br><!-- End of picture text -->

TypeScript v2 的 <mark>`createMcpHandler()`</mark> 已内置默认 stateless legacy fallback；如需要保留一个真正 sessionful 的 2025 deployment，官方建议在 user-land 用 <mark>`isLegacyRequest()`</mark> 分流到旧 handler，同时令现代 handler 使用 <mark>`legacy: "reject"` 。</mark> 36 

客户端则推荐显式使用 auto negotiation： 

```
constclient=newClient(
```

   - `{ name: "client", version: "1.0.0" },` 

   - `{ versionNegotiation: { mode: "auto" } },` 

- `);` 

官方 troubleshooting 文档显示 auto 会尝试现代 negotiation，并在 server 不提供现代协议时回落至 2025 initialize；如果必须杜绝 legacy，则使用 pin/strict 策略。 66 

### **移除 transport session 后如何保存状态** 

错误迁移： 

`let currentUser; let activeTransaction; //` 假设下一个 `MCP request` 一定落在同一个 `process` 

现代 deployment 下这在水平扩展时不安全，因为下一个 request 可以落到任意实例。 

#### 更合理的模式： 

```
tools/start-job
 -> result { operationId: "op_123" }
tools/continue-job
 arguments {
   operationId: "op_123",
   ...
 }
backend:
 operationId -> DB / Redis / durable object / workflow engine
```

官方 release note 明确建议需要 state 时使用显式 state handle，而不是把 state 隐藏在 protocol session 中。 33 

### **对有副作用 tools 的重试策略** 

由于 2026 broken SSE 无法 resume，客户端可能重新执行逻辑上的同一 operation。因此对： 

```
transfer_money
send_email
create_order
delete_resource
deploy_service
```

之类有副作用的 tool，建议在业务 schema 中提供： 

```
{
"operationId":"uuid...",
```

```
"..."
}
```

server 将 <mark>`(principal, operationId)`</mark> 作为 dedup key，使网络失败后的 retry 返回原结果或已知状态，而不是重复执行。此处是基于当前“broken stream → new request”规范推导的应用层设计建议。 6 

### **Long-lived events** 

普通 progress 应尽量保持 request-scoped；真正长期 change notification 使用 <mark>`subscriptions/listen` 。</mark> 在单进程测试环境，默认 in-memory bus 足够；多 replica 生产系统应使用 Redis Streams/PubSub、NATS、 Kafka 或其他实现自己的 <mark>`ServerEventBus` ，</mark> 否则不同 replica 的 subscribers 只能看见本地事件。SDK 明确把 external bus 作为多进程扩展点。 14 

### **Kubernetes / serverless 模式** 

现代模型非常适合： 

```
Cloud LB
  -> stateless MCP pods
```

```
      -> DB/cache
```

```
      -> shared pub/sub
```

pod 可以按 request concurrency 自动扩缩，普通 request 不需 session affinity；deployment draining 主要需要照顾尚未结束的 request-scoped SSE 与 subscriptions。这个优势正是当前 stateless transport 的设计目标。 67 

对 serverless/fetch-native runtime <mark>，</mark> <mark>`createMcpHandler`</mark> 的 Web-standard <mark>`fetch`</mark> API 很自然；但务必额外配置 Origin/Host validation 和 authorization，因为 handler 本身不会自动从 <mark>`Authorization`</mark> header 构造已验证 <mark>`authInfo` 。</mark> 36 

### **推荐生产配置** 

一个比较稳妥的生产 topology 是： 

<!-- Start of picture text -->
Internet / Claude / MCP<br>Clients<br>Edge / API Gateway<br>OAuth JWT Verification<br>Rate limits + Body limits<br>Load Balancer<br>MCP Pod A MCP Pod B MCP Pod C<br>Durable State Shared Event Bus<br><!-- End of picture text -->

Gateway 至少应能够基于 <mark>`Mcp-Method` 、</mark> <mark>`Mcp-Name` 、</mark> principal/scope、body size 和 connection count 实施 policy，同时 backend 必须重新验证 header/body 一致性，不应把 gateway routing decision 当成最终 protocol validation。 68 

## **已知限制、开放问题、Roadmap 与主要来源** 

### **当前结构性限制** 

**没有 transport-level resume。** 这是 2026 的刻意设计，而不是遗漏；SSE 中断后 inflight request 需要重新发起。对长耗时、有副作用 operation 来说，这把 exactly-once / deduplication 问题推向 application layer。 6 

**不是一个真正的 persistent full-duplex channel。** 请求仍是独立 HTTP exchanges；即使 response 使用 SSE，它也主要服务于该 request 的 incremental output。需要多轮 client interaction 的协议功能已转向 MRTR，而不是维持 WebSocket 风格的长期双向 session。 32 

**每 request fresh server/transport 有对象创建成本。** 这换来了隔离和 stateless routing，但对于极端纯计算、极低 latency server <mark>，</mark> <mark>`McpServer + Protocol + Transport`</mark> 每 request 构建可能不是最低开销路径。官方 GitHub 已有人提出更轻量的 stateless dispatch 模式作为优化方向；这属于 implementation optimization discussion，而非规范缺陷。 69 

**SDK transport 没有显式 SSE producer backpressure。** 当前源码使用 <mark>`controller.enqueue()` ，</mark> 没有 <mark>`desiredSize`</mark> 检查；在大规模慢消费者条件下，需要通过 benchmark 验证 queue memory behavior。 40 

**应用状态没有消失，只是责任转移了。** DB transaction、OAuth upstream token、workflow state、longrunning task 等仍然可能高度 stateful；现代规范只消除了 transport session 的强制耦合。 32 

### **当前开放 issue** 

截至 2026 年 9 月，本次研究发现 TypeScript SDK 至少有一个值得现代 request-scoped SSE 用户关注的开放问题： **#2739** **<mark>`StreamableHTTPClientTransport leaves POST requests pending when their SSE response ends or errors`</mark>** <mark>。</mark> issue 描述称，当 POST 的 SSE response EOF 或出错但还没交付 terminal JSON-RPC result 时，transport 没有把这个生命周期失败及时关联回原 request；结果 request 可能一直等到 protocol timeout。该 issue 截至检索时为 Open。 70 

这正好暴露了 request-scoped streaming 的一个重要实现要求：HTTP body EOF 不等于业务 request 成功结束， client 必须确认对应 request ID 的 terminal JSON-RPC response 已到达，否则应该及时 reject，而不是把 EOF 当正常 completion。 70 

另一个开放 issue **#2730** 报告，在 Node StreamableHTTP transport 中，notification 配合 inbound <mark>`Connection: close`</mark> 时可能错误获得裸 <mark>`400` ，</mark> 而不是预期 <mark>`202` ；</mark> 报告同时在 v1 和 v2 Node transport 上复现，并指出 Claude Code 的某些请求会触发这一情况。 71 

不过 #2730 的 repro 使用 <mark>`Mcp-Session-Id`</mark> 等 2025-era/multi-era transport machinery，因此 **不能据此断言现代** **<mark>`createMcpHandler`</mark> +** **<mark>`PerRequestHTTPServerTransport`</mark> 路径一定存在同一个 bug** 。它更适合作为迁移期 Node adapter/reverse-proxy interoperability 的警告。 72 

### **Roadmap 判断** 

从官方路线来看，方向已经很清晰： 

<!-- Start of picture text -->
SDK hardening<br>OAuth/auth hardening<br>2025 Stateful StreamableHTTP Enterprise scaling pain SEP-2243 header routing 2026 Stateless per-requesttransport Current work MRTR<br>Subscriptions/event bus<br>Observability / OTel<br>metadata<br><!-- End of picture text -->

2026 changelog 还增加了 OpenTelemetry trace context 和统一 MCP request headers，说明该 roadmap 的重点明显偏向 **企业 HTTP infrastructure、routing、observability、authorization 与 stateless scale-out** ，而不是重新建立一个 transport-level persistent session。 73 

当前 authorization 文档还指出，未来 revision 预计可能把 OAuth authorization response 中 <mark>`iss`</mark> 从 SHOULD 强化为 MUST；不过这属于 auth roadmap，不等于已经宣布下一版 Streamable HTTP 的发布日期或完整 transport feature list。 55 

### **最终工程判断** 

从分布式系统角度，2026 Streamable HTTP 可以理解为一种很务实的“退一步进两步”： 

#### `2025:` 

```
persistent transport state
```

- `+ richer connection semantics` 

- `+ resumability` 

- `sticky routing` 

- `session coordination` 

- `gateway complexity` 

#### `2026:` 

```
ordinary independent HTTP exchanges
```

- `+ header-level routing` 

- `+ horizontal scale` 

- `+ standard OAuth / WAF / LB integration` 

- `+ selective SSE streaming` 

- `transport resume` 

- `persistent duplex RPC` 

- `implicit server state` 

这种选择特别适合 MCP 的真实 deployment topology：大量 clients 调用相对粗粒度的 tools/resources，而企业已经拥有成熟的 HTTP ingress、OAuth、WAF、rate limiting、load balancing 和 observability 系统。SEP-2243 和 Transport WG 的文档基本直接说明了这一设计取舍。 74 

如果从源码角度挑出三个最值得持续观察的技术点，我会是： **per-request object creation overhead、slowconsumer backpressure、request-scoped SSE lifecycle/error propagation** 。前两者分别已有轻量 stateless dispatch 的讨论和源码层 backpressure 缺口，第三个已经直接体现为 #2739 open issue。 75 

### **主要一手资料** 

|一手资料|研究用途|
|---|---|
|Anthropic —_Introducing the Model Context Protocol_<br>76|MCP起源、开放标准定位|
|Anthropic —_Donating MCP to the Agentic AI Foundation_<br>77|当前治理与AAIF/LF关系|
|Anthropic Claude MCP Connector docs<br>63|Anthropic产品对Streamable HTTP的支持|
|Anthropic Claude Code MCP docs<br>64|`http` /<br>`streamable-http`配置|
|MCP 2026-07-28 Streamable HTTP specification<br>78|当前normative wire semantics|
|MCP 2026-07-28 changelog<br>6|session/resume移除、OTel等变化|
|MCP 2026-07-28 release post<br>33|stateless/MRTR/header routing设计动机|

|一手资料|研究用途|
|---|---|
|SEP-2243 HTTP Standardization<br>15|`Mcp-Method`/<br>`Mcp-Name` 的架构依据|
|MCP Transport WG future roadmap<br>79|2025 session model的扩展问题|
|TypeScript SDK v2 repository/docs<br>80|官方实现|
|`createMcpHandler.ts` API/source<br>81|modern HTTP entry|
|`perRequestTransport.ts` API/source<br>82|2026 transport核心源码|
|Python MCP SDK / Streamable HTTP implementation<br>83|Python实现|
|MCP Authorization specification<br>55|OAuth / Bearer / RFC 9728 / RFC 9207|
|MCP Authorization Security Considerations<br>84|token audience、PKCE、token passthrough|
|RFC 9113 — HTTP/2<br>58|multiplexing、flow control|
|RFC 9114 — HTTP/3<br>59|QUIC、per-stream flow control|
|RFC 6455 — WebSocket<br>85|WebSocket对照|
|WHATWG HTML — Server-Sent Events<br>86|SSE framing|
|IETF WebTransport over HTTP/3 draft<br>87|WebTransport对照|
|TypeScript SDK issue #2739<br>70|request-scoped SSE EOF/error lifecycle|
|TypeScript SDK issue #2730<br>71|Node/legacy Streamable HTTP<br>interoperability|

**综合判断：** 对新建远程 MCP 服务，优先采用 2026-07-28 的 <mark>`createMcpHandler`</mark> / per-request model，把 transport session state 清空，把业务状态显式外置；用 <mark>`Mcp-Method` /</mark> <mark>`Mcp-Name`</mark> 做 edge routing，但在 backend 强制 cross-check；对有副作用 tool 加应用级 idempotency；对 long-lived SSE 专门做 slow-reader/ backpressure 和 deployment-drain 测试；迁移期间才保留 2025 sessionful transport，并明确把旧的 <mark>`McpSession-Id` 、</mark> GET stream、EventStore <mark>、</mark> <mark>`Last-Event-ID`</mark> 代码视为 compatibility layer，而不是未来架构。这个方向与 2026 规范、SDK v2 结构和 Transport WG 路线是一致的。 88 

1 9 12 76 https://www.anthropic.com/news/model-context-protocol https://www.anthropic.com/news/model-context-protocol 

2 16 17 18 20 21 30 47 50 62 65 78 https://modelcontextprotocol.io/specification/draft/basic/ transports/streamable-http 

https://modelcontextprotocol.io/specification/draft/basic/transports/streamable-http 

3 15 68 74 https://modelcontextprotocol.io/seps/2243-http-standardization https://modelcontextprotocol.io/seps/2243-http-standardization 

4 14 22 29 35 36 53 54 81 https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/ server/server/createMcpHandler.html 

https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/server/server/createMcpHandler.html 

5 23 25 27 39 40 https://github.com/modelcontextprotocol/typescript-sdk/blob/ 7f7a94c22017e121a960e071bb50ec75e34450bd/packages/server/src/server/perRequestTransport.ts https://github.com/modelcontextprotocol/typescript-sdk/blob/7f7a94c22017e121a960e071bb50ec75e34450bd/packages/server/ src/server/perRequestTransport.ts 

6 73 

https://modelcontextprotocol.io/specification/2026-07-28/changelog 

https://modelcontextprotocol.io/specification/2026-07-28/changelog 

7 55 

https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization 

https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization 

8 13 32 33 48 51 56 67 88 https://blog.modelcontextprotocol.io/posts/2026-07-28/ https://blog.modelcontextprotocol.io/posts/2026-07-28/ 

10 https://modelcontextprotocol.io/specification/2025-03-26/basic/transports https://modelcontextprotocol.io/specification/2025-03-26/basic/transports 

11 52 79 https://blog.modelcontextprotocol.io/posts/2025-12-19-mcp-transport-future/ 

https://blog.modelcontextprotocol.io/posts/2025-12-19-mcp-transport-future/ 

> 19 https://github.com/modelcontextprotocol/typescript-sdk/blob/ 

7f7a94c22017e121a960e071bb50ec75e34450bd/packages/client/src/client/streamableHttp.ts 

https://github.com/modelcontextprotocol/typescript-sdk/blob/7f7a94c22017e121a960e071bb50ec75e34450bd/packages/client/ src/client/streamableHttp.ts 

24 86 https://html.spec.whatwg.org/dev/ 

https://html.spec.whatwg.org/dev/ 

26 28 49 58 https://www.rfc-editor.org/info/rfc9113/ 

https://www.rfc-editor.org/info/rfc9113/ 

> 31 https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/client/client/ streamableHttp.html 

https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/client/client/streamableHttp.html 

34 80 https://github.com/modelcontextprotocol/typescript-sdk 

https://github.com/modelcontextprotocol/typescript-sdk 

https://ts.sdk.modelcontextprotocol.io/v2/servers/tools.html 

https://ts.sdk.modelcontextprotocol.io/v2/servers/tools.html 

38 82 https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/server/server/ perRequestTransport.html 

https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/server/server/perRequestTransport.html 

> 41 https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/server/server/ requestBody.html 

https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/server/server/requestBody.html 

> 42 https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/server/server/ streamableHttp.html 

https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/server/server/streamableHttp.html 

> 43 https://github.com/modelcontextprotocol/typescript-sdk/blob/ 7f7a94c22017e121a960e071bb50ec75e34450bd/packages/server/src/server/streamableHttp.ts https://github.com/modelcontextprotocol/typescript-sdk/blob/7f7a94c22017e121a960e071bb50ec75e34450bd/packages/server/ src/server/streamableHttp.ts 

> 44 https://ts.sdk.modelcontextprotocol.io/v2/clients/connect.html 

https://ts.sdk.modelcontextprotocol.io/v2/clients/connect.html 

45 66 https://ts.sdk.modelcontextprotocol.io/v2/troubleshooting.html 

https://ts.sdk.modelcontextprotocol.io/v2/troubleshooting.html 

46 83 https://github.com/modelcontextprotocol/python-sdk 

https://github.com/modelcontextprotocol/python-sdk 

57 84 https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/securityconsiderations 

https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations 

> 59 https://www.rfc-editor.org/info/rfc9114/ 

https://www.rfc-editor.org/info/rfc9114/ 

60 85 https://www.rfc-editor.org/info/rfc6455/ https://www.rfc-editor.org/info/rfc6455/ 

61 87 https://datatracker.ietf.org/doc/draft-ietf-webtrans-http3/ 

https://datatracker.ietf.org/doc/draft-ietf-webtrans-http3/ 

> 63 https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector 

https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector 

> 64 https://docs.anthropic.com/en/docs/claude-code/mcp 

https://docs.anthropic.com/en/docs/claude-code/mcp 

69 75 https://github.com/modelcontextprotocol/typescript-sdk/issues/2090 https://github.com/modelcontextprotocol/typescript-sdk/issues/2090 

> 70 https://github.com/modelcontextprotocol/typescript-sdk/issues/2739 

https://github.com/modelcontextprotocol/typescript-sdk/issues/2739 

71 72 https://github.com/modelcontextprotocol/typescript-sdk/issues/2730 

https://github.com/modelcontextprotocol/typescript-sdk/issues/2730 

> 77 https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agenticai-foundation 

https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation 

