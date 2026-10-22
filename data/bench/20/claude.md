# Anthropic/MCP Streamable HTTP 工程实现深度报告（截至 2026-10-16）

截至 2026 年 10 月，Streamable HTTP 的“最新版本”是 MCP 规范 **2026-07-28**  修订版（2026-07-28 正式发布）。它把 [stacktr +2](https://stacktr.ee/blog/mcp-2026-spec-changes) Streamable HTTP 从“可选会话 + 双向 SSE + 可恢复流”的有状态传输，改成了“每个请求都是一个自描述的 POST”的无状态传输：`Mcp-Session-Id`、`initialize` 握手、GET 流、DELETE 和 `Last-Event-ID` 断点续传全部删除，新增 `Mcp-Method`/`Mcp-Name` 路由头。工程上的结论是：**新服务器应按 [github +3](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx) 2026-07-28 的无状态模型来写（TS 用 `createMcpHandler`，Python 用 v2 的 `MCPServer.streamable_http_app()`），同时在过渡期内对 2025 年代的客户端做兼容。**

## TL;DR

- **最新状态（2026-07-28 规范，标记为“最新”）** ：MCP 在协议层变为无状态。Streamable HTTP 只剩单一端点上的 POST。服务端到客户端的请求改由 Multi Round-Trip Requests（MRTR）承载，变更通知改用 `subscriptions/listen` 长流，中途断流即视为取消，SSE 不再可恢复。按官方发布博客的说法，“All four Tier 1 SDKs speak 2026-07-28 as of today”（TypeScript、Python、Go、C#），Rust SDK 处于 beta。旧的 HTTP+SSE 传输被正式归类为 Deprecated，博客称其有“a year-long offramp”，弃用政策规定“a twelve-month minimum window”。
- **SDK 落地** ：TypeScript v2（2026-07-27 发布，已拆分为 `@modelcontextprotocol/server`/`client` 等包）以 `createMcpHandler(factory)` 为 HTTP 入口，默认 `legacy: 'stateless'`，同一端点同时服务两个协议时代。v1.x（`@modelcontextprotocol/sdk` 1.32.1）只实现到 2025-11-25，仍可用 `StreamableHTTPServerTransport`。Python v2 把 FastMCP 改名为 `MCPServer`，`streamable_http_app()` 按 `MCP-Protocol-Version` 头自动分流两个时代，`stateless_http` 只对旧时代的连接生效。
- **Anthropic 自身使用** ：Claude.ai 自定义连接器和 Messages API 的 MCP connector（beta 头 `mcp-client-2025-11-20`，另有新的 `mcp-client-2026-09-15`）都支持 Streamable HTTP 和遗留 SSE，SSE 正在弃用中。Claude Code 用 `claude mcp add --transport http` 接入远程服务器，并在 2026 年 10 月的 2.1.292 到 2.1.299 版本中，陆续把 stdio、claude.ai 连接器等场景默认改为协商 2026-07-28。部署上建议：新服务按无状态设计，关闭代理缓冲，用显式句柄（handle）或 `requestState` 替代会话状态，旧的 SSE 端点只保留到有明确下线日期为止。

---

## 一、最新状态与修订演进

### 1.1 版本时间线

| 修订 | 日期 | Streamable HTTP 相关变化 |
| --- | --- | --- |
| 2024-11-05 | 2024-11 | 原始 HTTP+SSE 双端点传输：`GET /sse` 负责下行，另有一个 POST 端点，首个事件为 `endpoint` [bex](https://bex.co/blog/2026/09/12/mcp-breaks-forward-pinning-infrastructure-server)[sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) |
| **2025-03-26** | 2025-03 | 由 PR #206 引入 Streamable HTTP，取代 HTTP+SSE。该 PR 由 jspahrsummers 于 2025-03-17 提交，2025-03-24 合并。同期引入了 JSON-RPC batching [github +2](https://github.com/modelcontextprotocol/python-sdk/issues/2278) |
| **2025-06-18** | 2025-06 | 移除 JSON-RPC batching（PR #416）。后续 HTTP 请求必须带 `MCP-Protocol-Version` 头（PR #548）。MCP 服务器被归类为 OAuth Resource Server，并要求实现 RFC 8707 Resource Indicators [modelcontextprotocol](https://modelcontextprotocol.info/specification/2025-06-18/changelog/) |
| **2025-11-25** | 2025-11 | 明确规定 Origin 无效时返回 403（PR #1439）。新增 SSE“轮询”能力：服务器可随时断开连接（SEP-1699），恢复一律走 GET，事件 ID 应编码流标识（Issue #1847） [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/changelog) |
| **2026-07-28（最新）** | 2026-07-28 发布；RC 于 2026-05-21 锁定 [stacktr](https://stacktr.ee/blog/mcp-2026-spec-changes)[modelcontextprotocol](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) | 协议无状态化：删除会话、握手、GET 流、DELETE、`Last-Event-ID`。新增 `Mcp-Method`/`Mcp-Name`/`Mcp-Param-*`、`server/discover`、`subscriptions/listen`、MRTR。HTTP+SSE 被正式归类为 Deprecated（SEP-2596） [github](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx) [bex](https://bex.co/blog/2026/09/12/mcp-breaks-forward-pinning-infrastructure-server)[sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) |

2025 年 12 月 19 日，官方博客 “Exploring the Future of MCP Transports” 先公布了无状态化路线，表示 MCP 只保留 stdio 和 Streamable HTTP 两种官方传输。 [modelcontextprotocol](https://blog.modelcontextprotocol.io/posts/2025-12-19-mcp-transport-future/)2026-07-28 的 RC 公告称这一版本“completing the plan we laid out in The Future of MCP Transports”。 [modelcontextprotocol](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)

### 1.2 2026-07-28 changelog 中与传输直接相关的条目

- 从 Streamable HTTP 中移除协议级会话和 `Mcp-Session-Id`。需要跨调用状态的服务器改用“server-minted handles passed as ordinary tool arguments”（SEP-2567）。 [github +2](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx)
- 移除 `initialize`/`notifications/initialized` 握手。每个请求都在 `_meta` 中携带 `io.modelcontextprotocol/protocolVersion` 和 `io.modelcontextprotocol/clientCapabilities`（SEP-2575）。 [github +2](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx)
- 新增必须实现的 `server/discover`，用于预先做版本选择或探测兼容性。 [github +2](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx)
- 用 `subscriptions/listen` 取代 HTTP GET 端点和 `resources/subscribe`，它是一条长期存在的 POST 响应流。 [github +2](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx)
- 移除 SSE 可恢复性和重投递：“A broken response stream loses the in-flight request; clients MUST re-issue it as a new request with a new request ID”（SEP-2575）。 [github](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx)[sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/)
- 要求 `Mcp-Method`、`Mcp-Name` 请求头，并通过 `x-mcp-header` 支持把工具参数映射成自定义头（SEP-2243）。 [github +2](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx)
- 错误码重新编号：`HeaderMismatch` 为 −32020，`MissingRequiredClientCapability` 为 −32021，`UnsupportedProtocolVersion` 为 −32022。 [github](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx)
- 弃用政策：Deprecated 特性的最短窗口为 12 个月（David Soria Parra 和 Den Delimarsky 撰写的发布博客原文为“A formal deprecation policy with a twelve-month minimum window”，HTTP+SSE 则有“a year-long offramp”）。Roots、Sampling、Logging 以及 HTTP+SSE 均被列为 Deprecated。

官方发布博客由 David Soria Parra 和 Den Delimarsky 撰写，原话是：“MCP is transforming from a bidirectional stateful protocol into a request/response stateless protocol”，并且“Any request can now land on any server instance behind a plain round-robin load balancer without needing shared storage.” [modelcontextprotocol +2](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

---

## 二、协议设计：两代 Streamable HTTP 对照

### 2.1 2025 时代（2025-03-26 至 2025-11-25）

- **单一 MCP 端点** ，同时支持 POST 和 GET，例如 `https://example.com/mcp`。 [modelcontextprotocol +2](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- **POST** ：每条 JSON-RPC 消息都是一个新的 POST，`Accept` 头必须同时列出 `application/json` 和 `text/event-stream`。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
    - 如果请求体是 notification 或 response：服务器接受时返回 **202 Accepted** （无 body），不接受时返回 4xx（如 400），可附带一个不含 `id` 的 JSON-RPC 错误。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
    - 如果请求体是 request：服务器返回 `application/json`（单个对象）或 `text/event-stream`（SSE），客户端必须同时支持这两种。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)[medium](https://medium.com/@higress_ai/comparison-of-data-before-and-after-using-streamable-http-b094db8b414e)
    - 在 SSE 上，服务器可以先发送与该请求相关的 request 和 notification，最后发送 response，之后应当关闭流。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
    - 2025-11-25 起，服务器应先发送一个“带事件 ID、data 为空”的事件，用来 prime 客户端的重连。之后服务器可以主动断开连接（但流本身不结束），断开前应发送 `retry` 字段，客户端必须遵守该值。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
    - 断连不等于取消。要取消请求，客户端应显式发送 `CancelledNotification`。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- **GET** ：客户端可以用 GET 打开服务端主动推送的 SSE 流，`Accept` 需包含 `text/event-stream`。服务器要么返回 SSE，要么返回 **405** 。这条流上除非是在恢复流，否则不能发送 response。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- **多连接** ：客户端可以同时连着多条 SSE。服务器的每条消息只能在一条流上发送，不得广播。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- **可恢复性** ：SSE 事件的 `id` 必须在会话内（或在该客户端的所有流中）全局唯一，并应编码其所属的流。客户端用 GET 加 `Last-Event-ID` 恢复，服务器只能重放原来那条流上的消息。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- **会话** ：服务器可以在返回 `InitializeResult` 的响应里通过 `MCP-Session-Id` 下发会话 ID。会话 ID 应具备密码学安全性，且只能包含可见 ASCII 字符（0x21 到 0x7E）。客户端此后每个请求都必须带上它。服务器对缺少会话 ID 的请求应返回 400，会话过期后返回 **404** ，客户端收到 404 后必须重新发送 `InitializeRequest`。客户端可以用 **DELETE**  显式结束会话，服务器可以对 DELETE 返回 405。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- **版本头** ：2025-06-18 起必须携带 `MCP-Protocol-Version`。缺失时，服务器应按 2025-03-26 处理。版本无效时返回 [dev](https://dev.to/forgecode/mcp-2025-06-18-spec-update-security-structured-output-elicitation-1pin)[imasters](https://imasters.com/inteligencia-artificial/mcp-2025-06-18-what-breaks-in-agents-and-integrations-when-upgrading-versions) 400。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- **安全** ：必须校验 `Origin`，无效时返回 403。本地运行时应只绑定 127.0.0.1。应对所有连接做认证。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)

### 2.2 2026-07-28（最新）

- 端点只要求支持 POST。客户端发送的每个 [sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) request 或 notification 都是一个独立的 POST，请求体必须是单个 request 或 notification，不得发送 response。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- 服务器可以返回单个 JSON，也可以返回一条**只属于该请求** 的 SSE 流。流上只能有与该请求相关的 notification（如 `notifications/progress`），最后是 response。流上**不得** 出现服务器发起的独立 request。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- 服务端到客户端的交互（sampling、elicitation、roots）改用 MRTR：服务器返回 `InputRequiredResult`（`resultType: "input_required"`），客户端带着 `inputResponses` 重新发送原请求，此时使用新的请求 id。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- 长期的变更通知通过 `subscriptions/listen` 的响应流下发。服务器建议定期发送 SSE 注释行 `:\r\n` 作为保活。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- 发起 SSE 时，服务器应带上 `X-Accel-Buffering: no` 响应头，避免 nginx 等反向代理缓冲。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- **取消** ：关闭 SSE 响应流必须被视为取消该请求。在 [sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) Streamable HTTP 上不再需要发送 `notifications/cancelled`。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- **对旧流量的处理** ：对 GET 或 DELETE 返回 405。忽略 `Mcp-Session-Id`，既不生成也不回显。忽略 `Last-Event-ID`。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- **与 HTTP+SSE 的兼容探测** ：客户端先发 POST。如果收到 400、404 或 405，并且响应体**不是** 可识别的现代 JSON-RPC 错误，再尝试 GET，看是否会收到 `endpoint` 事件。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)

### 2.3 关键请求头与状态码速查表

| 项 | 适用修订 | 规则 |
| --- | --- | --- |
| `Accept: application/json, text/event-stream` | 全部 | POST 必须同时列出两种类型。2025 时代的 GET 只需 `text/event-stream` |
| `MCP-Protocol-Version` | 2025-06-18 起为 MUST | 2026 起必须与 `_meta` 中的 `io.modelcontextprotocol/protocolVersion` 一致，否则返回 400 + `HeaderMismatch`（−32020）。不支持的版本返回 400 + `UnsupportedProtocolVersionError` [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) |
| `MCP-Session-Id` | 仅 2025 时代 | 在 initialize 的响应中下发。缺失返回 400，过期返回 404。2026 服务器忽略此头 |
| `Last-Event-ID` | 仅 2025 时代 | 通过 GET 恢复流。2026 服务器忽略此头 |
| `Mcp-Method` / `Mcp-Name` | 2026-07-28 | 所有请求都必须带 `Mcp-Method`。`tools/call`、`resources/read`、`prompts/get` 还必须带 `Mcp-Name`。非 ASCII 值使用 `=?base64?…?=` 编码 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) |
| `Mcp-Param-{Name}` | 2026-07-28 | 由工具 schema 中的 `x-mcp-header` 声明，客户端必须支持。头与 body 不一致时返回 400 + −32020 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) |
| `X-Accel-Buffering: no` | 2026-07-28 起写入规范（SHOULD） | 服务器开启 SSE 时设置 |
| 202 Accepted | 全部 | 服务器接受 notification 或 response 时返回，无 body |
| 400 Bad Request | 全部 | 请求非法、版本不支持、头不匹配，或 2025 时代缺少会话 ID |
| 403 Forbidden | 全部 | `Origin` 无效 |
| 404 Not Found | 2025：会话过期；2026：方法不存在（附 −32601） | 2026 时代靠 JSON-RPC body 区分这个 404 与“旧 HTTP+SSE 服务器没有这个端点”的 404 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) |
| 405 Method Not Allowed | 全部 | 2025 时代表示不提供 GET 流或不允许 DELETE。2026 时代对所有 GET 和 DELETE 返回 405 |
| 421 / 403（Python SDK 实现） | SDK 行为 | Host 不在白名单返回 421，Origin 不在白名单返回 403 [modelcontextprotocol](https://py.sdk.modelcontextprotocol.io/run/deploy/) |
| 413（Python SDK v2） | SDK 行为 | 请求体超过 4 MiB [github](https://github.com/modelcontextprotocol/python-sdk/releases) |

---

## 三、官方 SDK 的具体实现

### 3.1 TypeScript SDK

**版本格局（截至 2026-10）**

- **v2** （2026-07-27 发布，当前稳定线）拆分为 `@modelcontextprotocol/server`、`@modelcontextprotocol/client`、`core`，外加 `node`、`express`、`hono`、`fastify` 适配器，以及 `server-legacy`（遗留 SSE）和 `codemod`。最新版本为 [modelcontextprotocol](https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28) v2.2.0（2026-09-28）。 [github +2](https://github.com/modelcontextprotocol/typescript-sdk)
- **v1.x** （`@modelcontextprotocol/sdk`）是维护线，最新为 **1.32.1（2026-10-05）** ，只实现到 2025-11-25，不会支持 2026-07-28。v2 发布后，v1.x 至少还会获得 6 个月的修复。1.30.0 [npmjs](https://www.npmjs.com/package/@modelcontextprotocol/sdk)[releasealert](https://releasealert.dev/npmjs/@modelcontextprotocol/sdk) 修复了 Streamable HTTP 服务端 SSE keep-alive 注释帧的发送问题（#2538、#2547）。 [newreleases](https://newreleases.io/project/npm/@modelcontextprotocol/sdk/release/1.30.0)

**v1 的 `StreamableHTTPServerTransport`（2025 时代，仍被大量生产代码使用）**

- 主要选项：`sessionIdGenerator`（传 `undefined` 即无状态）、`onsessioninitialized`、`onsessionclosed`、`enableJsonResponse`（默认 false，即优先使用 SSE）、`eventStore`（提供后开启可恢复性）、`retryInterval`（下发给客户端的 SSE `retry` 值）、`allowedHosts`/`allowedOrigins`/`enableDnsRebindingProtection`。 [glama +4](https://glama.ai/mcp/servers/@Jeffwalters9597/MCP/blob/0506addf35f422650658c5e665ea184e3115a184/src/server/streamableHttp.ts)
- 后三个 DNS rebinding 选项有社区 PR 称其已被标记 deprecated，推荐改用 `createMcpExpressApp`/`hostHeaderValidation()` 中间件。**这一点我没有在 [github](https://github.com/hktari/toshl-mcp-server/pull/49) SDK 源码中直接核实。**  CVE-2026-61568（`@zereight/mcp-gitlab`）就是因为既没有设置这些选项，也没有加中间件，导致本地 Streamable HTTP 端点可以被 DNS rebinding 攻击。 [gitlab](https://advisories.gitlab.com/npm/@zereight/mcp-gitlab/CVE-2026-61568/)
- `EventStore` 接口：`storeEvent(streamId, message): Promise<EventId>`、`replayEventsAfter(lastEventId, { send }): Promise<StreamId>`，以及可选的 `getStreamIdForEventId`。对未知事件 ID，SDK 返回 400 “Invalid event ID format”。 [github +2](https://github.com/modelcontextprotocol/servers/pull/5006)
- **内部多路复用机制** （依据早期 v1 源码快照和 v2 代码分析）：
    - `_streamMapping`（流 ID 到 SSE 响应或控制器） [deepwiki](https://deepwiki.com/modelcontextprotocol/typescript-sdk/3.5-streamable-http-server-transport)[jsdelivr](https://cdn.jsdelivr.net/npm/modelcontextprotocol-gemini@0.0.2/dist/esm/server/streamableHttp.d.ts)
    - `_requestToStreamMapping`（JSON-RPC 请求 ID 到流 ID） [deepwiki](https://deepwiki.com/modelcontextprotocol/typescript-sdk/3.5-streamable-http-server-transport)
    - `_requestResponseMap`（JSON 模式下暂存 response） [deepwiki](https://deepwiki.com/modelcontextprotocol/typescript-sdk/3.5-streamable-http-server-transport)
    - `_standaloneSseStreamId`（GET 独立流。社区普遍称其值为 `'_GET_stream'`，我未在源码中直接看到这个字面量）
    - `send()` 先用 `relatedRequestId` 查 `_requestToStreamMapping` 找到流。没有关联请求 ID 的消息写入独立流。一个 POST 中的所有请求都收到 response 后，关闭该 SSE 并清理映射。
    - 恢复时，`replayEventsAfter` 返回 streamId，再把新的 `res` 重新挂到 `_streamMapping` 上。 [github](https://github.com/modelcontextprotocol/typescript-sdk/issues/451)
    - 当前 v1.x 的 Node 版 transport 是对 `WebStandardStreamableHTTPServerTransport` 的包装。 [github](https://github.com/backstage/backstage/issues/35791)
- **客户端 `StreamableHTTPClientTransport`** ：选项包括 `authProvider`（OAuth）、`requestInit`、`sessionId`、`reconnectionOptions`。重连默认值为 `initialReconnectionDelay: 1000`、`maxReconnectionDelay: 30000`、`reconnectionDelayGrowFactor: 1.5`、`maxRetries: 2`。Issue #2098 指出，重试 2 次就放弃会让 GET-SSE 失效，导致 response 送不到客户端，这是一个已知坑。客户端会自动管理 [github](https://github.com/modelcontextprotocol/typescript-sdk/issues/2098)[deepwiki](https://deepwiki.com/moinfra/mcp-client-sdk/3.2.1-streamablehttp-transport) `mcp-session-id` 和 `mcp-protocol-version` 头，它们的优先级高于用户自定义头。 [modelcontextprotocol](https://ts.sdk.modelcontextprotocol.io/v2/api/@modelcontextprotocol/client/client/streamableHttp.html)

v1 有状态示例（2025 时代，Express，用会话 ID 到 transport 的 Map 管理会话）：

ts

```
import express from 'express'; import { randomUUID } from 'node:crypto'; import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'; import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js'; import { isInitializeRequest } from '@modelcontextprotocol/sdk/types.js'; const app = express(); app.use(express.json()); const transports: Record<string, StreamableHTTPServerTransport> = {}; app.post('/mcp', async (req, res) => { const sid = req.headers['mcp-session-id'] as string | undefined; let transport = sid ? transports[sid] : undefined; if (!transport && isInitializeRequest(req.body)) { transport = new StreamableHTTPServerTransport({ sessionIdGenerator: () => randomUUID(), onsessioninitialized: (id) => { transports[id] = transport!; }, // eventStore: new MyRedisEventStore(), // 开启 Last-Event-ID 恢复 }); transport.onclose = () => { if (transport!.sessionId) delete transports[transport!.sessionId]; }; const server = new McpServer({ name: 'demo', version: '1.0.0' }); await server.connect(transport); } if (!transport) return res.status(400).json({ jsonrpc: '2.0', error: { code: -32000, message: 'Bad Request: No valid session ID provided' }, id: null }); await transport.handleRequest(req, res, req.body); }); // GET（SSE 推送 / 恢复）与 DELETE（结束会话）同样按 mcp-session-id 查 transport 后调用 handleRequest
```

v1 的无状态写法：每个请求新建一个 `McpServer` 和一个 `new StreamableHTTPServerTransport({ sessionIdGenerator: undefined, enableJsonResponse: true })`，请求结束后关闭。v2 [milos-mitrovic](https://milos-mitrovic.online/blog/serve-mcp-over-streamable-http-instead-of-stdio) 迁移指南明确说这种写法“maps directly onto the default entry”。 [modelcontextprotocol](https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28)[startdebugging](https://startdebugging.net/2026/07/migrate-an-mcp-server-from-sse-to-streamable-http/)

**v2 的 `createMcpHandler`（2026 时代，推荐写法）**

ts

```
import express from 'express'; import { createMcpHandler, McpServer } from '@modelcontextprotocol/server'; import { toNodeHandler } from '@modelcontextprotocol/node'; import * as z from 'zod/v4'; const handler = createMcpHandler(() => { // 每个请求调用一次工厂 const server = new McpServer({ name: 'notes', version: '1.0.0' }); server.registerTool('add', { inputSchema: z.object({ a: z.number(), b: z.number() }) }, async ({ a, b }) => ({ content: [{ type: 'text', text: String(a + b) }] })); return server; }, { legacy: 'stateless' }); // 'reject' = 只服务 2026-07-28 const app = express(); app.use(express.json()); app.all('/mcp', (req, res) => void toNodeHandler(handler)(req, res, req.body)); app.listen(3000, '127.0.0.1'); // Workers/Deno/Bun 等 Web 标准运行时：export default handler;（handler.fetch(Request) => Response）
```

- `createMcpHandler` 返回 `{ fetch, close, notify, bus }`。默认 `legacy: 'stateless'`：对 2025 时代的客户端按无状态方式处理，没有 `initialize` 会话，也没有服务器到客户端请求的回传通道。 [modelcontextprotocol](https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28)[modelcontextprotocol](https://ts.sdk.modelcontextprotocol.io/v2/serving/http.html)
- 如果确实要保留 2025 时代的**有状态** 会话，需要并行跑两个 handler：用 `isLegacyRequest(request)` 把旧请求分流给原有的 v1 有状态 handler，新请求交给 `legacy: 'reject'` 的现代 handler。AAIF 和 Cloudflare 的迁移指南都推荐这种双通道做法。 [modelcontextprotocol +2](https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28)
- 跨请求状态的替代方案：MRTR 的 `requestState`（由服务器签发的不透明令牌），或者由工具签发、模型回传的显式句柄。
- 客户端版本协商：`new Client(info, { versionNegotiation: { mode: 'auto' } })` 会先发 `server/discover` 探测，失败后回退到 2025 握手。默认 `'legacy'` 与 v1 逐字节一致。`{ pin: '2026-07-28' }` 只用现代协议。HTTP 上探测到 401、403 或 5xx 不会被当作“旧版本”的证据，而是直接报错。 [modelcontextprotocol](https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28)

### 3.2 Python SDK（`mcp`）

- **v2（稳定版，同时服务两个协议时代）** ：`FastMCP` 改名为 `MCPServer`（`mcp.server.mcpserver`）。传输参数从构造函数移到 `run()` 或 `streamable_http_app()`。`streamablehttp_client` 被移除，客户端改用 `streamable_http_client` 或高层的 `Client(url)`。HTTP 栈从 httpx 加 httpx-sse 换成 `httpx2`。请求体默认上限 4 MiB，超过返回 413（`max_request_body_size`）。OpenTelemetry 默认开启。会话管理器、`EventStore`、stateless 模式均“unchanged”。2.x 中 Streamable HTTP 空闲会话默认会过期，并限制并发会话数（#3395）。 [pydantic +3](https://pydantic.dev/articles/mcp-python-sdk-v2-beta)
- **两个时代的分流** ：同一个 `streamable_http_app()` 按 `MCP-Protocol-Version` 头路由。现代请求在读取 `stateless_http` 之前就已经返回，所以官方文档说：“stateless_http is a knob for the legacy leg only”。对旧时代的客户端：默认是会话加 `Mcp-Session-Id`，会话存在单个 worker 的内存里，必须做粘性路由，否则会收到 404 “Session not found”；如果设置 `stateless_http=True`，则没有会话，但也失去服务器到客户端的回传通道和可恢复性。 [modelcontextprotocol](https://py.sdk.modelcontextprotocol.io/run/legacy-clients/)[modelcontextprotocol](https://py.sdk.modelcontextprotocol.io/run/deploy/)
- **安全默认值** ：不传 `transport_security=` 时，默认开启 DNS rebinding 防护，只接受 localhost 的 Host。部署到真实域名后必须设置 `TransportSecuritySettings(allowed_hosts=[...], allowed_origins=[...])`，否则所有请求都会返回 421。 [modelcontextprotocol](https://py.sdk.modelcontextprotocol.io/run/deploy/)
- **多 worker 的坑** ：MRTR 的 `request_state` 默认用每个进程启动时 `os.urandom(32)` 生成的密钥加密。多 worker 部署时必须给所有实例配置同一个 `RequestStateSecurity(keys=[...])`，**并且** 服务器名称（audience）也要一致，否则跨 worker 的重试会收到 −32602 “Invalid or expired requestState”。变更通知要跨副本传递，需要自己基于 Redis、NATS 等实现 `SubscriptionBus`（只有 `publish` 和 `subscribe` 两个方法）。SDK 不提供 `workers=` 参数，多进程交给 uvicorn、gunicorn 等。 [modelcontextprotocol](https://py.sdk.modelcontextprotocol.io/run/deploy/)

python

```
# server.py — Python SDK v2 from mcp.server import MCPServer from mcp.server.transport_security import TransportSecuritySettings mcp = MCPServer("units") @mcp.tool() def c_to_f(c: float) -> float: """Celsius to Fahrenheit""" return c * 9 / 5 + 32 app = mcp.streamable_http_app( transport_security=TransportSecuritySettings( allowed_hosts=["mcp.example.com", "mcp.example.com:*"], allowed_origins=["https://app.example.com"], ), stateless_http=True, # 仅影响 2025 时代客户端；2026 请求天然无状态 json_response=True, ) # uvicorn server:app --workers 4 --proxy-headers --forwarded-allow-ips='<proxy>' # client.py import anyio from mcp import Client async def main(): async with Client("https://mcp.example.com/mcp") as client: # 默认 mode='auto' print(await client.call_tool("c_to_f", {"c": 21})) anyio.run(main)
```

v1（`mcp.server.fastmcp`）的低层写法是 `StreamableHTTPSessionManager(app=server, event_store=..., json_response=..., stateless=True)`，挂载到 Starlette 的 `Mount("/mcp", app=handle)` 上，并在 lifespan 中 `async with session_manager.run()`。已知问题有两个。一是挂载子应用时 Starlette 不会运行子应用的 lifespan（Issue #673），必须在外层的 lifespan 里手动进入每个 `session_manager.run()`。二是 v1 无状态模式下客户端断开会导致崩溃（Issue #3142），修复只进入了 2.0，v1.x 还在等回移。 [github +3](https://github.com/modelcontextprotocol/python-sdk/issues/673)

### 3.3 其他官方 SDK

- **C#** ：v2.0 实现了 2026-07-28，HTTP 传输**默认无状态** 。`SessionMode` [modelcontextprotocol](https://csharp.sdk.modelcontextprotocol.io/v2/api/ModelContextProtocol.AspNetCore.HttpServerTransportOptions.html)[microsoft](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/) 可选 `Stateless`、`Stateful`（拒绝 2026-07-28）或 `StatefulForInitializeClients`（混合）。有状态模式下 `IdleTimeout` 默认 2 小时，`MaxIdleSessionCount` 默认 10,000。v1 时代有 `EventStreamStore`（`ISseEventStreamStore`）支持可恢复性。 [modelcontextprotocol +2](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/)
- **Go** ：v1.7.0-pre.1 起支持 2026-07-28，但必须设置 `StreamableHTTPOptions.Stateless = true` 才会接受新协议。 [modelcontextprotocol](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/)
- **Rust（rmcp）** ：对新规范的支持处于 beta。注意它构建的 [modelcontextprotocol](https://blog.modelcontextprotocol.io/posts/2026-07-28/) stdio 服务器收到 `initialize` 之前的未知请求会直接退出，TS v2 客户端因此会用一个“兄弟进程”去探测。 [modelcontextprotocol](https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28)
- **Kotlin** ：`StreamableHttpClientTransport` 支持 SSE 指数退避重连和 `Last-Event-ID` 恢复。服务端的 `StreamableHttpServerTransport` 和 `EventStore` 通过 PR #449 加入（2025-12 时仍为 WIP）。 [github](https://github.com/modelcontextprotocol/kotlin-sdk/pull/449)[modelcontextprotocol](https://kotlin.sdk.modelcontextprotocol.io/kotlin-sdk-client/io.modelcontextprotocol.kotlin.sdk.client/-streamable-http-client-transport/index.html)
- 关于 Java、Swift、Ruby、PHP SDK 对 2026-07-28 的支持，本次没有找到权威信息，**需自行核实** 。

---

## 四、Anthropic 自身的工程使用

- **Claude.ai / Desktop / Cowork 自定义连接器** ：官方文档要求远程服务器使用 Streamable HTTP，原文为 “Claude also supports the legacy HTTP+SSE transport, which is being deprecated in favor of Streamable HTTP”。连接从 [sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) Anthropic 云端发起，服务器必须能从公网访问。认证方面遵循 2025-03-26、2025-06-18、2025-11-25 三版授权规范，支持 DCR 等注册方式。所有付费计划和免费计划都可以使用，但免费用户只能添加 [sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) 1 个自定义连接器。 [claude](https://claude.com/docs/connectors/building)[claude](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- **Messages API 的 MCP connector** ：beta 头为 `mcp-client-2025-11-20`，旧的 `mcp-client-2025-04-04` 已弃用。通过 [sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) `mcp_servers` 数组（`type: "url"`，URL 必须是 https，`name`，可选 `authorization_token`）加 `tools` 中的 `mcp_toolset`（`default_config`、`configs`、`defer_loading`）配置。只支持工具调用，支持 Streamable HTTP 和 SSE，不支持本地 stdio。OAuth [sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) 流程需要调用方自己完成并刷新 token。新的 `mcp-client-2026-09-15` beta 头会在响应开头返回 `mcp_tool_listing` 块，并允许把工具列表“钉住”（pin），避免服务器在会话中途改变工具集。 [claude](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
- **Claude Code** ：`claude mcp add --transport http <name> <url>` 是推荐的远程接入方式。在 `.mcp.json` 中 `"type": "streamable-http"` 是 `http` 的别名。`--transport sse` 已被标记为弃用。支持 OAuth 2.0（通过 `/mcp` 交互认证）、`headersHelper`、`authServerMetadataUrl`。**2026-07-28 [mcpbundles](https://www.mcpbundles.com/blog/claude-code-mcp-tools)[claude](https://code.claude.com/docs/en/mcp) 的支持情况（最新）** ，据官方 changelog：
    - 2.1.274：让 Bedrock、Vertex、Foundry 安装也默认对直连 HTTP 服务器协商 2026-07-28。这意味着其他安装方式在此之前已经是这个默认值。 [gradually](https://www.gradually.ai/en/changelogs/claude-code/)
    - 2.1.292（2026-10-06）：stdio 服务器默认协商 2026-07-28。 [claude](https://code.claude.com/docs/en/changelog)
    - 2.1.295（2026-10-08）：claude.ai 连接器默认协商 2026-07-28。 [claude](https://code.claude.com/docs/en/changelog)
    - 2.1.299（2026-10-14）：云端会话和 Remote Control 连接器默认协商 2026-07-28。 [claude](https://code.claude.com/docs/en/changelog)
    - 可以用 `MCP_PROTOCOL_NEGOTIATION=legacy` 退回旧协议。 [claude](https://code.claude.com/docs/en/changelog)
- **口径不一致之处** ：Anthropic 于 2026-07-28 发布的博客说 “Support is being rolled out across Claude products”。但截至本报告，Claude.ai [claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) 连接器的开发文档只列出了 2025 年的三版授权规范，并没有承诺支持 2026-07-28 的核心传输格式。MCP [sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) connector 的 beta 头命名仍是 2025 年的。**因此对 [sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) Claude 产品线来说，同时支持 2025 时代的 Streamable HTTP 仍然是必要的。**
- **云厂商** ：
    - Cloudflare 在 2026-08-06 的博客中介绍了 Agents SDK 对新规范的支持；其产品管理高级总监 Brendan Irvine-Broque 在 MCP 官方发布博客中说：“Cloudflare’s Agents SDK supports the spec from day zero… customers like Sentry and Linear can adopt it on day zero”。它在 `agents/mcp/server` 中提供 `createMcpHandler`，旧的有状态通道使用 `createLegacyMcpHandler`/`McpAgent`（基于 Durable Objects，可用 `DurableObjectEventStore` 应对 Cloudflare 边缘约 5 分钟的空闲流看门狗）。同一个 `/mcp` 端点同时接受新协议请求和 2025 时代的无状态请求。 [cloudflare +2](https://blog.cloudflare.com/mcp-v2/)
    - AWS Agentic AI 副总裁 Swami Sivasubramanian 在 MCP 官方 2026-07-28 发布博客中说：“With the new MCP specification and its stateless protocol core available in Amazon Bedrock AgentCore… Tasks, one of the first official MCP extensions and contributed by AWS”。
    - 在同一篇博客中，Google Cloud 工程院士 Anna Berenberg 表示“At Google Cloud, we are excited to leverage these powerful new capabilities across our ecosystem”，Microsoft Foundry 工程副总裁 Tina Schuchman 表示“MCP is foundational to Microsoft Foundry, enabling us to scale from dozens of integrations to thousands”。

---

## 五、部署与扩展模式

### 5.1 无状态与有状态模式对比

| 维度 | 无状态（2026-07-28 原生，或 2025 时代的 stateless 模式） | 有状态（2025 时代会话） |
| --- | --- | --- |
| 会话标识 | 无，每个请求自带 `_meta` | `Mcp-Session-Id`，存在单个进程的内存里或外部存储中 |
| 负载均衡 | 普通轮询，任意实例都能处理 | 需要按头做粘性路由（AWS ALB 和 GCLB 原生不支持基于头的亲和性，通常要在前面加一层 nginx、Envoy 或 HAProxy），或使用共享会话存储 [bex](https://bex.co/blog/2026/07/09/mcp-stateless-spec-freeze-load-balancers) |
| 服务器到客户端请求 | 2026 时代用 MRTR。2025 时代的无状态模式下没有这个能力 | 走 SSE 回传通道，支持 sampling、elicitation、roots |
| 断线恢复 | 2026 时代没有，客户端用新 ID 重新发请求 | 可以用 `EventStore` 加 `Last-Event-ID`，多实例部署需要共享的事件存储（如 Redis） |
| 取消 | 关闭响应流即取消 | 发送 `notifications/cancelled` |
| 跨调用状态 | 显式句柄或 `requestState`（多实例需共享密钥和 audience） | 隐式的会话内存 |
| Serverless（Lambda、Workers） | 天然适配 | 需要 Durable Objects、DynamoDB 等外部状态 |
| 适合场景 | 绝大多数工具型服务器 | 必须服务需要回传通道的旧客户端的场景 |

### 5.2 反向代理与负载均衡

- **关闭缓冲** ：nginx 设置 `proxy_buffering off; proxy_cache off;`，必要时也关掉 `gzip`（压缩会按块缓冲），服务器端发送 `X-Accel-Buffering: no`（2026 规范已写入）。否则 SSE 会被攒到连接关闭时才一次性送达。 [modelcontextprotocol +2](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- **空闲超时** ：nginx 官方指令参考写明“Default: proxy_read_timeout 60s”，且该超时只计两次连续读操作之间的间隔；AWS ELB 文档写明“By default, ELB sets the idle timeout value for your load balancer to 60 seconds”（可设 1 到 4000 秒）。Cloudflare 官方“Connection limits”文档（2026-07-23 更新）给出的 Proxy Read Timeout 为 125 秒（超时返回 524，仅 Enterprise 区域可调），Proxy Idle Timeout 为 900 秒；但其 Error 524 页面写的是“the default 120 seconds Proxy Read Timeout”，两份官方文档不一致，常见的“约 100 秒”说法已过时。处理办法是调大中间每一跳的**空闲** 超时，同时让服务器定期发送 `:` 注释行作为心跳。在 [xoflux](https://xoflux.com/blog/streaming-llm-sse-load-balancer) 2025-11-25 的规范下，也可以借助 SEP-1699 的“服务器主动断开 + `retry` + GET 恢复”轮询模式，避开负载均衡的超时。 [github](https://github.com/modelcontextprotocol/typescript-sdk/pull/1726)[modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/changelog)
- **TLS 终止** ：Python 应用部署在代理之后时，要设置 `--proxy-headers --forwarded-allow-ips`。否则 `/mcp` 到 `/mcp/` 的重定向会被降级成 http，客户端会拒绝跟随。 [modelcontextprotocol](https://py.sdk.modelcontextprotocol.io/run/deploy/)
- **网关路由与可观测性** ：2026 时代可以直接按 `Mcp-Method`、`Mcp-Name` 做路由、限流和工具级指标统计。但规范要求中间件按头做策略之前，先确认 [modelcontextprotocol](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) `MCP-Protocol-Version` 是要求头与 body 一致校验的版本，否则不应信任这些头。Python [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) SDK v2 默认输出 OTel span（如 `mcp.method.name`、`mcp.protocol.version`），2026 [pydantic](https://pydantic.dev/articles/mcp-python-sdk-v2-beta) 规范还定义了 `_meta` 中的 `traceparent`/`tracestate` 传播方式。 [github](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx)
- **与 stdio 的对比** ：stdio 用于本地单用户场景，没有网络暴露面，客户端应优先支持。Streamable [modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) HTTP 用于远程多租户场景，必须配 TLS 和认证。 [aws](https://builder.aws.com/content/35A0IphCeLvYzly9Sw40G1dVNzc/mcp-transport-mechanisms-stdio-vs-streamable-http)[niteagent](https://niteagent.com/blog/mcp-transport-deep-dive-stdio-vs-streamable-http/)

### 5.3 从 HTTP+SSE 迁移的要点

1. 把 `GET /sse` 加 `POST /messages?sessionId=` 两个端点合并为单一的 `/mcp`，会话标识从 query 参数改为请求头。新代码直接按 2026 的无状态模型写，不要把 `MCP-Session-Id` 的设计带进现代路径。 [startdebugging](https://startdebugging.net/2026/07/migrate-an-mcp-server-from-sse-to-streamable-http/)[sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/)
2. 客户端配置从 `"type": "sse"` 改为 `"type": "http"`，URL 通常以 `/mcp` 结尾。很多服务器在同一个 URL 上同时提供两种传输。 [mcpbundles](https://www.mcpbundles.com/blog/claude-code-mcp-tools)[startdebugging](https://startdebugging.net/2026/07/migrate-an-mcp-server-from-sse-to-streamable-http/)
3. 服务器端：TS 用 `createMcpHandler`（旧的 SSE 移到 `@modelcontextprotocol/server-legacy`），Python 用 v2 的 `streamable_http_app()`，Cloudflare 用 `createMcpHandler` 加一条临时的旧通道。
4. 过渡期内保留旧端点，统计流量，并定好下线日期。发布博客写明 [sunpeak](https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/) HTTP+SSE 有“a year-long offramp”。
5. 对代理层，在**新路径** 上同样关闭缓冲并调大超时。 [startdebugging](https://startdebugging.net/2026/07/migrate-an-mcp-server-from-sse-to-streamable-http/)

---

## 六、设计动机、批评与展望

- **为什么要替换 HTTP+SSE** （PR #206 和 Discussion #102）：旧方案中服务器消息只能通过 SSE 下发；需要长期占用一个连接；服务器必须记住哪条 SSE 对应哪个会话，扩容依赖粘性会话；不能断线恢复；不适合 serverless。Streamable [fka](https://blog.fka.dev/blog/2025-06-06-why-mcp-deprecated-sse-and-go-with-streamable-http/) HTTP 的思路是“plain HTTP + optional SSE”：最简单的服务器只做普通的请求和响应，需要流式时再升级到 SSE。维护者当时讨论过以 WebSocket 为主，但没有采用。该 [github +2](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206) PR 致谢了 Shopify、Pydantic、Cloudflare、LangChain、Vercel 等方面的贡献者。 [github](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206)
- **2025 时代暴露的问题** ：
    - 有状态会话导致必须做粘性路由或使用共享存储，ALB 和 GCLB 还要额外加一层代理。 [bex](https://bex.co/blog/2026/07/09/mcp-stateless-spec-freeze-load-balancers)
    - 可恢复性实现复杂（事件 ID 必须编码流标识，重放不能跨流），社区实现的 bug 很多，例如 [github](https://github.com/modelcontextprotocol/servers/issues/4087)[modelcontextprotocol](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) TS 客户端只重试 2 次（#2098），Python v1 无状态模式崩溃（#3142）。 [github](https://github.com/modelcontextprotocol/python-sdk/issues/3142)[github](https://github.com/modelcontextprotocol/typescript-sdk/issues/2098)
    - JSON-RPC batching 引入一个版本后就被删除了。 [github](https://github.com/ryanjoachim/mcp-batchit/issues/3)
    - DNS rebinding 一类的本地暴露风险，已出现 CVE。 [github](https://github.com/clawfetch/clawfetch-mcp/issues/2)[gitlab](https://advisories.gitlab.com/npm/@zereight/mcp-gitlab/CVE-2026-61568/)
- **2026-07-28 的取舍** ：用 MRTR 和显式句柄换来水平扩展能力和网关可见性，代价是失去“服务器主动发请求”和断流恢复，正在执行的请求一旦断流就丢失，只能重发。对需要长时间运行的任务，官方的答案是 Tasks 扩展（`io.modelcontextprotocol/tasks`，用 `tasks/get` 轮询）。批评意见主要集中在迁移成本上：五次修订几乎每次都有破坏性变更。Python [github](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/changelog.mdx) [bex](https://bex.co/blog/2026/09/12/mcp-breaks-forward-pinning-infrastructure-server) 社区也有人指出，2025 时代的客户端在相当长时间内仍会是“大多数”，所以服务器必须支持两个时代。 [modelcontextprotocol](https://py.sdk.modelcontextprotocol.io/whats-new/)
- **后续方向（属于预期，不是既成事实）** ：AAIF 文章提到，下一步可能做资源 eTag、更多 TTL 提示，以及可插拔传输（WebSocket、gRPC）。2025-12 [aaif](https://aaif.io/blog/stateless-the-future-of-mcp-transports) 的路线图还提出了 `/.well-known/mcp.json` Server Cards 的设想。HTTP+SSE [modelcontextprotocol](https://blog.modelcontextprotocol.io/posts/2025-12-19-mcp-transport-future/) 已具备在未来修订中被删除的条件。 [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)

## 建议

1. **新建远程 MCP 服务** ：TS 直接用 v2 的 `createMcpHandler`（`legacy: 'stateless'`），Python 用 v2 的 `MCPServer`。不要依赖会话内存，跨调用状态用句柄或 `requestState`，多实例部署时共享密钥和 audience。
2. **面向 Claude 产品线** ：同时保证 2025 时代 Streamable HTTP 的兼容性。Claude.ai 连接器文档和 API connector 目前仍以 2025 规范为准，Claude Code 虽然已默认协商 2026-07-28，但可以通过环境变量退回旧协议。用 MCP Inspector（默认走 Legacy）和 Claude Code 分别验证两个时代。 [computingforgeeks](https://computingforgeeks.com/migrate-mcp-server-stateless/)
3. **需要回传通道的旧客户端** ：采用双通道部署（`isLegacyRequest` 分流到原有的有状态 handler 加粘性路由），并设定下线日期。
4. **基础设施** ：关闭代理缓冲，调大空闲超时，加心跳。配置 Host/Origin 白名单（Python 默认值在生产环境会直接返回 421）。在网关上按 `Mcp-Method`/`Mcp-Name` 做路由和限流，但要先校验协议版本。

## 注意事项与不确定性

- TS v1 的 `allowedHosts`/`allowedOrigins`/`enableDnsRebindingProtection` 是否已标记 deprecated，以及独立流 ID 的字面量 `'_GET_stream'`，都没有在 v1.x HEAD 源码中直接核实。
- Claude Code 的 2.1.274 和 2.1.281 两个版本的日期没有拿到。changelog 只写了“negotiate protocol version 2026-07-28”，没有逐项说明 `server/discover` 等细节。
- Python v1 的“最后一个 v1 版本”存在说法冲突：第三方文章称 `mcp==1.30.0`，GitHub Issue #3142 中写的是 v1.28.1 为当时最新稳定版。**以 [computingforgeeks](https://computingforgeeks.com/migrate-mcp-server-stateless/)[github](https://github.com/modelcontextprotocol/python-sdk/issues/3142) PyPI 为准。**
- Cloudflare 的 Proxy Read Timeout 在其官方文档中存在 125 秒与 120 秒两种写法；其他托管平台的空闲超时数值仍来自二手博客。
- Java、Swift、Ruby、PHP SDK 对 2026-07-28 的支持情况，本次没有找到权威信息。