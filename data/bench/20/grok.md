Streamable HTTP 是 MCP（Model Context Protocol）的远程传输，现行规范是协议版本 **2026-07-28**。Anthropic 是这份规范的主要推动方，Claude 和 Claude Code 都按这套线协议连远程 MCP server。官方定义在 Streamable HTTP。

这一版把传输做成了**无会话、单端点、每次请求自包含**的 HTTP。服务端不再持有连接级状态，反向要数据也不再从流里主动发 JSON-RPC request。

## 三代线协议

| 代际 | 形态 | 状态 |
|---|---|---|
| 2024-11-05 HTTP+SSE | 两个端点：GET 开长连接 SSE，POST 发请求。第一条 SSE 是 `endpoint` 事件，告诉客户端往哪 POST | 自 2025-03-26 起废弃，新实现不应再采用 |
| 2025-03-26 至 2025-11-25 Streamable HTTP | 单端点 `/mcp`，但有 `Mcp-Session-Id`、GET 推送流、DELETE 结束会话、`Last-Event-ID` 断点续传，流上还能下发服务端 request | 已被 2026-07-28 拿掉 |
| **2026-07-28** | 只剩 POST。每个 JSON-RPC 消息一次 HTTP 请求。响应要么一个 JSON，要么一条只属于这次请求的 SSE | 当前实现目标 |

改掉的四件事对应四个 SEP 决定：没有独立 GET 流、没有协议级 session、响应流上禁止独立的服务端 request、没有 `Last-Event-ID` 重放（SEP-2575、SEP-2567）。断流就丢这次在途请求，客户端必须用**新的 JSON-RPC id** 重发。

## 端点契约

一个 MCP endpoint，惯例是 `POST /mcp`。GET 和 DELETE 回 **405**。每个客户端消息都是一次新的 POST，body 只能是**一条** JSON-RPC request 或 notification，不能是 response，也不能 batch。

必带头：

| Header | 规则 |
|---|---|
| `Accept` | 必须同时列出 `application/json` 和 `text/event-stream`。服务端二选一，客户端两种都要能吃 |
| `Content-Type` | `application/json` |
| [illegible] | [illegible] |
| `MCP-Protocol-Version` | 例如 `2026-07-28`，必须和 body 里 `_meta["io.modelcontextprotocol/protocolVersion"]` 逐字相同 |
| `Mcp-Method` | 镜像 body 的 `method` |
| `Mcp-Name` | `tools/call`、`resources/read`、`prompts/get` 必填，镜像 `params.name` 或 `params.uri` |

头和 body 不一致，或者缺头，返回 **400**，JSON-RPC `-32020` **HeaderMismatch**。版本服务端不支持，同样 **400**，带 `UnsupportedProtocolVersionError`，并列出支持的版本。未知方法是 **404** + `-32601`。

`Mcp-Method` / `Mcp-Name` 的工程目的是让网关、限流和计费**不用解析 JSON body** 就能路由。非 ASCII 或含控制字符的名字用哨兵编码：`=?base64?<base64>?=`。工具参数还可以用注解 `x-mcp-header` 镜像成 `Mcp-Param-{name}`，只允许 string / integer / boolean。

一次 `tools/call`：

```http
POST /mcp HTTP/1.1
Content-Type: application/json
Accept: application/json, text/event-stream
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: get_weather

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": { "location": "Seattle, WA" },
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientInfo": { "name": "ExampleClient", "version": "1.0.0" },
      "io.modelcontextprotocol/clientCapabilities": {}
    }
  }
}
```

没有 `initialize`。版本、能力和身份都挂在**每一次**请求的 `_meta` 上。客户端应带 `clientInfo`，服务端应在每条 result 的 `_meta` 里回 `serverInfo`。想提前选版本，打 `server/discover`（服务端必须实现）。

## 响应怎么分叉

```text
      [illegible]                          [illegible]

                     POST JSON-RPC
                                             ►
  [illegible]         [notification]

                 202 Accepted, empty body
    ◄
                        [短请求]

                   200 application/json
    ◄
                    [有进度或长订阅]

                  200 text/event-stream
    ◄
                 notifications/progress
    ◄
                JSON-RPC result 然后关流
    ◄

      [illegible]                          [illegible]
```

- Notification：接受则 **202**、无 body；拒绝则 4xx，body 可以是一条没有 `id` 的 JSON-RPC error。
- 普通 request：**200** + `Content-Type: application/json`，一个对象。
- 需要中途通知或长连接：**200** + `Content-Type: text/event-stream`。

SSE 上只允许和**这次请求有关**的 notification（`notifications/progress`、`notifications/message`），最后一条应当是对应 `id` 的 JSON-RPC response，并结束流。服务端**不得**在这条流上发独立的 JSON-RPC request。流不可恢复，不要写 SSE `id:`，也不要认 `Last-Event-ID`。

长流（尤其是 `subscriptions/listen`）要防代理缓冲：响应加 `X-Accel-Buffering: no`，并周期性写 SSE 注释心跳 `:\r\n`。反向代理侧对应 `proxy_buffering off`，并把 `proxy_read_timeout` 拉长。

取消信号变了。Streamable HTTP **没有** `notifications/cancelled`（那只留在 stdio）。客户端取消就是关掉这次 POST 的响应流。Python SDK 里，每个在途 POST 挂在自己的 cancel scope 上，收到取消就 abort，不再发一条 notification。

## 服务端反过来要数据：MRTR

旧模型里，服务端可以在 SSE 上主动发 `sampling/createMessage`、`elicitation/create`、`roots/list`。无会话之后没有一条能把客户端的回答送回“那个 session”的通道，所以改成 **Multi Round-Trip Requests**（SEP-2322）。

服务端不发 request，而是把这次调用的 result 标成未完成：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resultType": "input_required",
    "requestState": "AEAD-protected blob",
    "inputRequests": {
      "github_user": {
        "method": "elicitation/create",
        "params": { "mode": "form", "message": "GitHub username", "requestedSchema": {} }
      }
    }
  }
}
```

规则：

- 每条 result 必须有 `resultType`：`"complete"` 或 `"input_required"`。老服务器省略这个字段时，客户端必须当成 `"complete"`。
- `inputRequests` 和 `requestState` 至少有一个。`requestState` 对客户端是不透明字符串，必须原样回传，不能解析、不能改。
- 只能要客户端在 capabilities 里声明过的方法。
- 客户端用**新的 JSON-RPC id** 重发**同一条**原始请求，带上 `inputResponses`（key 对齐）和原样的 `requestState`。
- 服务端用 `requestState` 把重试接回上次的中间状态。因为传输层已经无状态，这个 blob 通常要自己做签名或 AEAD，不能靠内存 session。

## 变更通知：`subscriptions/listen`

列表变化和资源更新不再走 GET，也不再走 `resources/subscribe`。客户端另发一条 POST：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "subscriptions/listen",
  "params": {
    "notifications": {
      "toolsListChanged": true,
      "resourceSubscriptions": ["file:///project/config.json"]
    }
  }
}
```

服务端用 SSE 把这条 POST 挂住。第一条必须是 `notifications/subscriptions/acknowledged`，并在 `_meta["io.modelcontextprotocol/subscriptionId"]` 里给出订阅 id；在此之前不能推任何通知。之后每条通知都带同一个 subscriptionId。服务端不得推客户端没点名的类型。正常结束时用原 `id` 回一条 `resultType: "complete"`；传输突然断开则没有这条 result，客户端自行重订（没有续传）。

进度和日志**不**走这条流，只走触发它们的那次 `tools/call` 的响应流。日志级别也不再是 `logging/setLevel`，而是这次请求 `_meta` 里的 `io.modelcontextprotocol/logLevel`；请求没带这个字段，服务端就不能发 `notifications/message`。`ping` 也删了。

## 无 session 之后状态放哪

`Mcp-Session-Id` 必须忽略，不能签发、不能回显。`tools/list` 一类列目录接口不再按连接而变。跨调用状态只能是服务端自己签发的 handle，当作普通工具参数传回来（SEP-2567）。`requestState` 只覆盖**同一次逻辑调用的重试**，不是用户会话。

所以水平扩展时：任意实例都能接任意 POST，不需要会话亲和，也不需要为传输层做 Redis event store。实例内存里只该有“这一条 HTTP 请求还没写完”的状态。

## 安全

规范强制三条：

1. 校验 `Origin`。有 Origin 且不合法必须 **403**，防 DNS rebinding。body 可以是一条无 `id` 的 JSON-RPC error。
2. 本地进程只绑 `127.0.0.1`，不要 `0.0.0.0`。
3. 远程连接做认证。MCP 这边是 OAuth 2.1 resource server：校验 Bearer，并按 RFC 8707 核对 `aud` 是否就是这个 MCP 资源 URL。动态客户端注册（RFC 7591）已让位给 Client ID Metadata Documents。

Python SDK 还会把超过 4 MiB 的 body 直接 **413**，这是实现限制，不是协议字段。

## SDK 里怎么落地

官方 SDK 从 2026-07-27/28 起切到 v2，同一进程同时说新旧两代，由**客户端第一包**决定走哪条。

**Python**（python-sdk v2）：`FastMCP` 改名为 `MCPServer`，装饰器 API 不动。一个 `Client(url)` 取代以前的 transport + `ClientSession + initialize()`。`serve_dual_era_loop` 看第一包是现代 `_meta` 还是旧 handshake。Streamable HTTP 客户端把每个在途 POST 放进 `_in_flight_posts`，取消只 abort 对应 scope。2026 版本下 `listChanged` 只看有没有实现 `subscriptions/listen`，旧的 `resources/subscribe` handler 在现代线路上不会被派发。

**TypeScript**：单体包 `@modelcontextprotocol/sdk@1.x` 仍停在 handshake 时代。v2 拆成 `@modelcontextprotocol/server`、`client`、`core`，外加 `@modelcontextprotocol/express` / `node` / `hono` / `fastify`。现代 server 是：每个 POST new 一个无 session 的 transport，`handleRequest` 后在 `res.close` 上拆掉。不要再配 `sessionIdGenerator`，不要再挂 GET。

**Go SDK** 更硬：`StreamableHTTPOptions.Stateless = true` 才接受 `2026-07-28`。非 stateless handler 会直接拒这个版本，因为无会话模式下服务端无法把客户端响应送回某个 session。

服务端处理顺序可以收成这样：

1. 方法不是 POST → 405。
2. 校验 Origin → 否则 403。
3. 鉴权（Bearer / `aud`）。
4. 解析单条 JSON-RPC；同时读 `MCP-Protocol-Version`、`Mcp-Method`、`Mcp-Name`，和 body / `_meta` 对账 → 否则 400 / `-32020`。
5. 版本不在支持列表 → 400 + `UnsupportedProtocolVersionError`。
6. 是 notification → 202 空 body。
7. 是 request：短结果直接 `application/json`；需要进度或 listen 则切 SSE，先写相关 notification，最后写 result 并结束。
8. result 若是 `input_required`，把续跑所需状态封进 `requestState`，不要留在进程内存里等下一次连接。

## 客户端探测旧服务器

Claude 到现在仍同时接受 Streamable HTTP 和旧 HTTP+SSE，没有公布关停日期。探测顺序是规范写死的：

1. 先按 2026-07-28 POST（带 Accept 和三个 MCP 头）。
2. 成功就锁定现代传输。
3. 若 **400** 且 body 是认得的现代 JSON-RPC error（HeaderMismatch、UnsupportedProtocolVersion），说明对方是现代服务器，按它广告的版本改请求重试，不要退回 SSE。
4. 若 400/404/405 且 body 空或不是现代错误，再 GET，等 SSE 里的 `endpoint` 事件，退回 2024-11-05 HTTP+SSE。
5. 对 2025 年那代：若对方回了 `Mcp-Session-Id`、要求 GET 流，客户端要另走那一版；纯 2026 服务器则忽略这些头。

只实现 2026 的服务器见到旧流量：GET/DELETE → 405；`Mcp-Session-Id` 和 `Last-Event-ID` 丢掉，不回显。
