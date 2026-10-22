# MCP Streamable HTTP 的具体工程实现：以 2026-07-28 规范为基线

**工程结论先行。**截至 2026-09-13，最新稳定规范应以 **MCP 2026-07-28** 为版本主键，正式发布日期为 2026 年 7 月 28 日。发布主体是 Model Context Protocol 项目；Anthropic 同期公告说明，相关支持正在向 Claude 产品滚动推出。[1][2]

**新服务推荐无会话。**具体做法是：提供一个 `/mcp` 入口，每条 JSON-RPC 请求独立使用 POST，响应按需选择 JSON 或请求范围内的 SSE。现代路径不再执行 `initialize`，不再使用 `Mcp-Session-Id`，也不再通过 `Last-Event-ID` 恢复断流。业务连续性应由显式业务句柄、受保护的 `requestState` 和外部持久化存储承担。[3]

**兼容必须按版本分流。**现有服务若依赖旧客户端、会话内状态或 SSE 事件重放，应保留独立的兼容路径。不能因为 SDK 中仍有 `EventStore`、GET 和 DELETE 接口，就把这些机制放进 2026-07-28 的现代协议流程。[4]

**阅读路线如下。**先明确版本和 SDK 的对应关系，再还原 HTTP、JSON-RPC 与 SSE 时序。随后分别给出服务端、客户端和生产环境的实现方案，最后说明迁移步骤、测试门槛与架构取舍。

| 协议时代 | 入口与响应 | 状态与恢复 | 推荐使用条件 |
|---|---|---|---|
| 2026-07-28 | POST `/mcp`；JSON 或请求级 SSE | 无协议会话；断流后新请求 | 新建服务、任意副本处理 |
| 2025-era Streamable HTTP | 同一路径 POST、GET、DELETE | 可选会话与事件重放 | 保留旧客户端能力 |
| 2024-11-05 HTTP+SSE | GET `/sse`、POST `/messages` | 连接关联的旧流程 | 迁移期兼容 |

三代传输的边界来自当前规范的兼容性章节；路径名称是常见约定，真正需要固定的是协议行为。[3]

本节参考文献：
[1] MCP 稳定发布 <https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28> 摘录：“Repository navigation This release marks the stable release of the 2026-07-28 revision of the Model Context Protocol. The specification is available on the official Model Context Protocol website. For a detailed overview of changes, see 2026-07-28 changelog.”
[2] Anthropic 产品公告 <https://claude.com/blog/bringing-mcp-2026-07-28-to-claude> 摘录：“Bringing MCP 2026-07-28 to Claude The fifth spec release of the Model Context Protocol, MCP 2026-07-28, is live today. The latest spec moves MCP to a stateless core, while hardening authorization and graduating official extensions. Support is being rolled out across Claude products. What's new in MCP MCP recently surpassed 400M monthly SDK downloads…”
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport from protocol version 2024-11-05. Revision 2026-07-28 changed the behavior of Streamable HTTP. Clients must ensure they handle backwards compatibility correctly. Changes included: - Removal of the GET stream endpoint. - Removal of protocol-level…”
[4] TypeScript 版本迁移 <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> 摘录：“(Typings published before 2.0.0-alpha.4 predate this exclusion: there the typed maps still carry the tasks/ entries and the CreateTaskResult the isCallToolResult guard if you are pinned to one of those alphas. 2.0.0-alpha.4 and later include the exclusion.) Where task interop is genuinely required, use the explicit-schema custom-method form on both…”

## 一、先确定“最新发布”具体指什么

本节参考文献：
[1] MCP 稳定发布 <https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28> 摘录：“Repository navigation This release mark…”
[2] Anthropic 产品公告 <https://claude.com/blog/bringing-mcp-2026-07-28-to-claude> 摘录：“Bringing MCP 2026-07-28 to Claude The f…”
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in proto…”
[4] TypeScript 版本迁移 <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> 摘录：“title Supporting protocol revision 2026…”

### 规范版本、Anthropic 产品与 SDK 是三个层次

**准确对象是规范。**Streamable HTTP 是 MCP 的远程传输方式，不是 Claude 模型版本，也不是 Anthropic Messages API 的流式接口。MCP 官方发布公告将 2026-07-28 定义为从双向、有状态协议转向无状态请求—响应核心的重要修订。[5]

| 对象 | 版本或日期 | 发布内容 | 工程用途 |
|---|---|---|---|
| MCP 稳定规范 | 2026-07-28 | 协议与传输规则 | 线协议主键 |
| MCP 正式公告 | 2026-07-28 | 无状态、MRTR、请求头、授权 | 理解设计变化 |
| Anthropic 产品公告 | 2026-07-28 | Claude 产品支持滚动推出 | 判断宿主接入范围 |
| TypeScript v2 发布线 | 仓库标注 2026-07-27 | 实现 2026-07-28 规范 | 选择实现依赖 |

规范日期与 SDK 发布日期不必相同。TypeScript 仓库明确把 v2 标为稳定发布线，并将其映射到 2026-07-28 规范。[6]

**主体需要分清。**MCP 本身由 Anthropic 于 2024 年引入，但本次稳定规范由 MCP 项目发布。正式公告署名 David Soria Parra 和 Den Delimarsky，两人均为 Lead Maintainer。Anthropic 的公告则说明 Claude 产品如何采用这次规范变化。[5][7]

**版本判定有条件。**若将“最新”进一步限定为 Anthropic 独立传输发行号、Anthropic 客户端末次补丁号，或 TypeScript client 的独立末次 tag，应以截止日前对应产品的专属 tag 和发布时间决定。本文采用 MCP 规范版本和官方稳定实现基线，不把历史问题中的客户端版本改称截止日最新版。

本节参考文献：
[5] MCP 发布公告 <https://blog.modelcontextprotocol.io/posts/2026-07-28/> 摘录：“The 2026-07-28 Model Context Protocol specification is out, bringing a stateless protocol core, Multi Round-Trip Requests, header-based routing, cacheable list results, authorization hardening, a formal extensions framework, and updated Tier 1 SDKs. July 28, 2026 · 12 min · David Soria Parra (Lead Maintainer), Den Delimarsky (Lead Maintainer) Since our last November release MCP continued to grow at an astonishing r…”
[6] TypeScript 官方仓库 <https://github.com/modelcontextprotocol/typescript-sdk> 摘录：“This is the main branch: v2 of the SDK (@modelcontextprotocol/server , @modelcontextprotocol/client ), the stable release line, implementing the 2026-07-28 MCP spec. Start with the v2 documentation; coming from v1, see the migration guide. v1.x (@modelcontextprotocol/sdk ) lives on the v1.x branch and continues to receive bug fixes and security updates for at least six months after the v2 release (2026-07-27). Its…”
[7] MCP 的起源 <https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html> 摘录：“MCP (Model Context Protocol) Security Cheat Sheet¶ Introduction¶ The Model Context Protocol (MCP), introduced by Anthropic in November 2024, standardizes how AI applications (LLM clients) connect to external tools, data sources, and services. Think of it as a universal interface layer, a USB-C port for AI , replacing fragmented, custom integrations with a single protocol. However, MCP introduces a fundamentally new…”

### 可以落地的 SDK 基线

**服务端已有明确锚点。**Python 官方稳定基线是 `mcp==2.0.0`，TypeScript 服务端基线是 `@modelcontextprotocol/server@2.0.0`。前者的发布说明明确支持 2026-07-28，并能从同一服务器服务更早修订。[8][9]

| 实现对象 | 本文采用的基线 | 主要入口 | 版本含义 |
|---|---|---|---|
| Python 官方 SDK | `mcp==2.0.0` | `MCPServer`、`Client` | 双协议时代实现 |
| TypeScript 服务端 | `server@2.0.0` | `createMcpHandler` | 现代 HTTP 入口 |
| TypeScript 客户端 | v2 同组配套基线 | `Client`、HTTP transport | 协商现代或旧协议 |
| Anthropic Agent SDK | `0.2.52`，2026-03-03 问题环境 | 内嵌 MCP 客户端 | 历史互操作案例 |

TypeScript 发布说明指出核心包采用同组版本发布规则，`2.0.0` 可作为配套实现锚点。独立客户端的截止日末次发布身份，仍按前述 tag 条件判定。[9][10]

**Python 名称容易混淆。**官方 Python SDK v2 使用 `mcp.server.mcpserver.MCPServer`。旧版官方 SDK 的 `mcp.server.fastmcp.FastMCP`，以及独立项目的 `from fastmcp import FastMCP`，属于不同 API 和发布体系。Anthropic 远程示例同时展示了官方 TypeScript SDK 与独立 FastMCP，不能据此混装构造参数。[11][12]

该示例的具体组合是：Express 的 `/mcp` POST 每次创建 `StreamableHTTPServerTransport`，设置 `sessionIdGenerator: undefined`，再执行 `server.connect(transport)` 和 `handleRequest`；默认端口为 `process.env.PORT ?? 3000`，response close 时关闭 transport。

本节参考文献：
[8] Python v2.0.0 <https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0> 摘录：“Repository navigation MCP Python SDK v2 Stable Release This is v2.0.0, the stable v2 release of the MCP Python SDK. It supports the 2026-07-28 revision of the Model Context Protocol and serves every earlier revision from the same server. pip install mcp now installs 2.x. pip install mcp cli uv add…”
[9] TypeScript server v2.0.0 <https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/@modelcontextprotocol/server@2.0.0> 摘录：“charset=utf-8 , including malformed parameter sections likeapplication/json; ) continue to work. SDK clients always send the correct header and are unaffected.The new isJsonContentType(header) helper is exported for transport and framework-adapter authors — custom entries composing the exported bui…”
[10] Agent SDK 历史环境 <https://github.com/anthropics/claude-agent-sdk-typescript/issues/202> 摘录：“Repository navigation HTTP MCP transport does not send Accept: application/json, text/event-stream header, causing 406 on Streamable HTTP servers 202 @anthropic-ai/claude-agent-sdk : 0.2.52 (latest)@modelcontextprotocol/sdk : 1.27.1 (latest)- Node: 22+, Bun 1.3+ When using the Claude Agent SDK with…”
[11] Python v2 迁移 <https://github.com/modelcontextprotocol/python-sdk/blob/e8e64842/docs/migration.md> 摘录：“This guide covers the breaking changes introduced in v2 of the MCP Python SDK and how to update your code. Version 2 of the MCP Python SDK introduces several breaking changes to improve the API, align with the MCP specification, and provide better type safety. The deprecated streamablehttp_client f…”
[12] Anthropic HTTP 示例 <https://github.com/anthropics/claude-plugins-official/blob/main/plugins/mcp-server-dev/skills/build-mcp-server/references/remote-http-scaffold.md> 摘录：“Minimal working servers in both recommended frameworks. Start here, then add tools. npm install @modelcontextprotocol/sdk zod express npm install -D typescript @types/express @types/node tsx src/server.ts import { McpServer } from @modelcontextprotocol/sdk/server/mcp.js ; import { StreamableHTTPSer…”

### 最值得注意的最终规范修正

**最终格式不同于早期草案。**TypeScript `server@2.0.0` 发布说明记录了一个关键修正：`server/discover` 的服务端身份不再放在结果体的 `serverInfo` 字段，而是移到结果 `_meta` 的 `io.modelcontextprotocol/serverInfo`。请求中的 `clientInfo` 也从必填降为 SHOULD。[9]

**这个差异会影响协商。**如果客户端仍要求发现结果必须包含体内 `serverInfo`，就可能把合规现代服务器误判为旧服务器。随后发出 `initialize`，反而导致 modern-only 服务连接失败。这里不是网络不通，而是发现结果的解析模型落后于最终规范。

**身份元数据不等于认证。**`clientInfo` 和 `serverInfo` 用于声明名称与版本。TypeScript 发布说明明确将服务端身份视为自报、未经身份验证的展示信息。授权必须依赖可信 HTTP 认证上下文，不能信任 `_meta` 中自称的客户端名称。[9]

**本节判断。**应先锁定“规范修订＋SDK tag＋目标宿主版本”，再讨论功能支持。仅写“支持 Streamable HTTP”，不足以确定握手、会话、恢复和授权行为。

本节参考文献：
[9] TypeScript server v2.0.0 <https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/@modelcontextprotocol/server@2.0.0> 摘录：“Repository navigation @modelcontextprotocol/server@2.0.0 Minor Changes Thanks @felixweinberger! - Export theProtocol base class andmergeCapabilities from the@modelcontextprotocol/client and@modelcontextprotocol/server package roots, restoring the v1 import for consumers that subclassProtocol the MCP Apps SDK). The client and server packages each bundle their own compiled copy of the class, so import it from one package consistently within a process.The codemod now rewrites andmergeCapabilities imports fromshared/protocol.js to the client or server package root, like the module's other symbols, instead of dropping them with an action-required marker. Thanks @felixweinberger! - Move the schema source modules (spec schemas, OAuth schemas, protocol constants) into@modelcontextprotocol/core and resolve them from there as a regular runtime depend…”

## 二、现代 Streamable HTTP 的完整协议流程

本节参考文献：
[9] TypeScript server v2.0.0 <https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/@modelcontextprotocol/server@2.0.0> 摘录：“- Add configurable SSE keep-alive commen…”

### 单一端点不等于只有一种响应

**每条消息独立 POST。**现代服务器暴露一个 MCP endpoint，通常是 `/mcp`。客户端每条 JSON-RPC request 或 notification 都单独发送，POST body 必须是一个消息对象。现代客户端不能向服务器 POST 独立 JSON-RPC response。[3]

| 方法与路径 | 请求方向 | 用途 | 响应方向与形式 |
|---|---|---|---|
| POST `/mcp` | 客户端到服务端 | 普通 RPC | 服务端返回 JSON 或 SSE |
| POST `/mcp` | 客户端到服务端 | `subscriptions/listen` | 服务端保持 SSE 响应 |
| POST `/mcp` | 客户端到服务端 | 被接受的 notification | 202，无响应体 |
| GET `/mcp` | 旧客户端可能发起 | 现代路径不建独立流 | 现代实现返回 405 |
| DELETE `/mcp` | 旧客户端可能发起 | 现代路径不终止会话 | 现代实现返回 405 |
| OPTIONS `/mcp` | 浏览器到边缘层 | CORS 预检 | 边缘层返回预检结果 |

规范对 modern-only 服务收到 GET、DELETE 的建议是返回 `405 Method Not Allowed`。OPTIONS 是浏览器 HTTP 接入机制，不是 MCP RPC。[3]

**SSE 没有被整体删除。**删除的是旧传输中的独立 GET 通道、协议会话和事件续传。SSE，即 Server-Sent Events，仍可作为 POST 的响应体格式。它不需要 WebSocket，也不是 HTTP `101 Switching Protocols` 升级。

**两种媒体类型都要支持。**客户端 POST 使用 `Content-Type: application/json`，并同时声明 `Accept: application/json, text/event-stream`。服务端可以返回任一种表示形式，客户端应依据实际响应的 `Content-Type` 分派解析器。[3]

本节参考文献：
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport from protocol version 2024-11-05. Revision 2026-07-28 changed the behavior of Streamable HTTP. Clients must ensure they handle backwards compatibility correctly. Changes included: - Removal of the GET stream endpoint. - Removal of protocol-level sessions. - The server exposes a single HTTP endpoint (the MCP endpoint) that accepts POST. - The client sends every JSON-RPC request or notification as its own HTTP POST. - The server answers each request with either a single JSON object or a Server-Sent Events (SSE) stream scoped to that request, carrying request-related notifications followed by the final response. - Server-to-client interactions (sampling, elicitation, roots) are embedded in results as input requests per Multi Round-Trip Requests (MRTR) (SEP-2322). - Long-lived change notifications (such as list changes and resource updates) are delivered on the response stream of a subscriptions/listen Security & Endpoint When implementing Streamable HTTP transport:- Servers MUST validate the header on all incoming connections to prevent DNS rebinding attacks.- If the header is present and invalid, servers MUST respond with HTTP 403 Forbidden. The HTTP response body MAY comprise a JSON-RPC error response that has noid - When running locally, servers SHOULD bind only to localhost (127.0.0.1) rather than all netw…”

### 请求头与请求体共同构成校验入口

**镜像头用于网关。**`Mcp-Method` 把 JSON-RPC `method` 暴露给网关；`Mcp-Name` 在调用工具、读取资源和获取提示词时暴露目标名称或 URI。这样负载均衡、限流和审计组件不必为路由深度解析 JSON body。[3]

| 请求字段 | 典型值 | 对应内容 | 校验重点 |
|---|---|---|---|
| `Content-Type` | `application/json` | POST body 格式 | 按媒体类型解析 |
| `Accept` | JSON 与 SSE 两项 | 客户端消费能力 | 两种响应均可处理 |
| `MCP-Protocol-Version` | `2026-07-28` | `_meta` 中协议版本 | 头体一致 |
| `Mcp-Method` | `tools/call` | `method` | 值大小写敏感 |
| `Mcp-Name` | `search_items` | `params.name` 或 `uri` | 按适用方法要求 |
| `Authorization` | Bearer token | HTTP 认证上下文 | 每次请求独立验证 |

**头体一致性是安全边界。**网关若按头中的“只读查询”放行，后端却按 body 执行“写入操作”，两层策略就会分裂。服务器必须比对这些字段，而不是把头和 body 当成两套可以任选的事实源。缺失、格式错误或不一致时，现代规范使用 HTTP 400 和 `HeaderMismatch`，错误码为 `-32020`。[3]

**头名称不区分大小写。**`mcp-method` 与 `Mcp-Method` 等价，但方法值 `tools/call` 与 `TOOLS/CALL` 不等价。TypeScript `2.0.0` 还专门修正了头值两侧 HTTP 可选空白的处理，避免不同 Fetch runtime 暴露方式造成互操作差异。[9]

下面是一条教学用现代请求。应用名称、请求 ID 和查询值仅用于展示字段位置。

```http
POST /mcp HTTP/1.1
Host: mcp.example.com
Authorization: Bearer <access-token>
Content-Type: application/json
Accept: application/json, text/event-stream
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: search_items

{
  "jsonrpc": "2.0",
  "id": 42,
  "method": "tools/call",
  "params": {
    "name": "search_items",
    "arguments": {
      "query": "otters",
      "limit": 10
    },
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientCapabilities": {},
      "io.modelcontextprotocol/clientInfo": {
        "name": "engineering-client",
        "version": "0.1.0"
      },
      "progressToken": "search-42"
    }
  }
}
```

**业务调用不要求先握手。**现代客户端可以直接发送上述请求，也可以先调用 `server/discover`。后者用于获取支持版本、能力和服务端身份，不创建协议会话。随后每个请求仍需携带自身版本和能力，不能依赖发现调用留下的连接内状态。[13]

本节参考文献：
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport from protocol version 2024-11-05. Revision 2026-07-28 changed the behavior of Streamable HTTP. Clients must ensure they handle backwards compatibility correctly. Changes included: - Removal of the GET stream endpoint. - Removal of protocol-level sessions. - The server exposes a single HTTP endpoint (the MCP endpoint) that accepts POST. - The client sends every JSON-RPC request or notification as its own HTTP POST. - The server answers each request with either a single JSON object or a Server-Sent Events (SSE) stream scoped to that request, carrying request-related notifications followed by the final response. - Server-to-client interactions (sampling, elicitation, roots) are embedded in results as input requests per Multi Round-Trip Requests (MRTR) (…”
[9] TypeScript server v2.0.0 <https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/@modelcontextprotocol/server@2.0.0> 摘录：“Repository navigation @modelcontextprotocol/server@2.0.0 Minor Changes Thanks @felixweinberger! - Export theProtocol base class andmergeCapabilities from the@modelcontextprotocol/client and@modelcontextprotocol/server package roots, restoring the v1 import for consumers that subclassProtocol the MCP Apps SDK). The client and server packages each bundle their own compiled copy of the class, so import it from one package consistently within a process.The codemod now rewrites andmergeCapabilities imports fromshared/protocol.js to the client or server package root, like the module's other symbols, instead of dropping them with an action-required marker. Thanks @felixweinberger! - Move the schema source modules (spec schemas, OAuth schemas, protocol constants) into@modelcontextprotocol/core and resolve them from there as a regular runtime dependency instead o…”
[13] 发现与按请求协商 <https://modelcontextprotocol.io/specification/2026-07-28/changelog> 摘录：“Major changes Remove protocol-level sessions and the Mcp-Session-Id header from the Streamable HTTP transport. List endpoints (tools/list ,resources/list ,prompts/list ) no longer vary per-connection. Servers that need cross-call state use explicit, server-minted handles passed as ordinary tool arguments (SEP-2567). Make MCP stateless: remove the /notifications/initialized Every request now carries its protocol version and client capabilities in_meta (io.modelcontextprotocol/protocolVersion ,io.modelcontextprotocol/clientCapabilities Clients SHOULD identify themselves on each request (io.modelcontextprotocol/clientInfo ), and servers SHOULD identify themselves in each result’s_meta (io.modelcontextprotocol/serverInfo Version mismatches returnUnsupportedProtocolVersionError server/discover : servers MUST implement this RPC to advertise their supported pro…”

### JSON 与 SSE 的结果如何返回

**快速调用直接返回 JSON。**若工具不需要进度通知，服务端可以一次性返回结果。结果属于请求 `id=42`，不会再经另一条 GET 通道交付。

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "id": 42,
  "result": {
    "resultType": "complete",
    "content": [
      { "type": "text", "text": "[]" }
    ],
    "structuredContent": {
      "items": []
    }
  }
}
```

**需要进度时使用请求级 SSE。**服务器可在最终响应之前发送相关的 `notifications/progress` 或 `notifications/message`。这些通知必须属于原始请求，不能在该流中夹入另一个独立的服务器 RPC。[3]

```http
HTTP/1.1 200 OK
Content-Type: text/event-stream
Cache-Control: no-cache
X-Accel-Buffering: no

event: message
data: {"jsonrpc":"2.0","method":"notifications/progress","params":{"progressToken":"search-42","progress":1,"total":1}}

event: message
data: {"jsonrpc":"2.0","id":42,"result":{"resultType":"complete","content":[{"type":"text","text":"[]"}],"structuredContent":{"items":[]}}}

```

**事件 ID 不参与现代恢复。**上述流故意没有 SSE `id:` 字段，也没有 `Last-Event-ID`。现代协议已经移除事件重投和断点续传；普通请求的最终 JSON-RPC response 应结束对应流。[13]

**通知确认不代表后台任务完成。**HTTP 202 只表示服务器接受了一个 notification。现代核心没有需要客户端通过 HTTP 发送的内置 notification；`notifications/cancelled` 留在 stdio 取消路径。因此不能把旧 `notifications/initialized` 塞进现代流程，也不能用 202 冒充 `tools/call` 的成功结果。[3]

本节参考文献：
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport from protocol version 2024-11-05. Revision 2026-07-28 changed the behavior of Streamable HTTP. Clients must ensure they handle backwards compatibility correctly. Changes included: - Removal of the GET stream endpoint. - Removal of protocol-level sessions. - The server exposes a single HTTP endpoint (the MCP endpoint) that accepts POST. - The client sends every JSON-RPC request or notification as its own HTTP POST. - The server answers each request with either a single JSON object or a Server-Sent Events (SSE) stream scoped to that request, carrying request-related notifications followed by the final response. - Server-to-client interactions (sampling, elicitation, roots) are embedded in results as input requests per Multi Round-Trip Requests (MRTR) (SEP-2322). - Long-lived ch…”
[13] 发现与按请求协商 <https://modelcontextprotocol.io/specification/2026-07-28/changelog> 摘录：“Major changes Remove protocol-level sessions and the Mcp-Session-Id header from the Streamable HTTP transport. List endpoints (tools/list ,resources/list ,prompts/list ) no longer vary per-connection. Servers that need cross-call state use explicit, server-minted handles passed as ordinary tool arguments (SEP-2567). Make MCP stateless: remove the /notifications/initialized Every request now carries its protocol version and client capabilities in_meta (io.modelcontextprotocol/protocolVersion ,io.modelcontextprotocol/clientCapabilities Clients SHOULD identify themselves on each request (io.modelcontextprotocol/clientInfo ), and servers SHOULD identify themselves in each result’s_meta (io.modelcontextprotocol/serverInfo Version mismatches returnUnsupportedProtocolVersionError server/discover : servers MUST implement this RPC to advertise their supported protocol versions, capabiliti…”

### MRTR：需要用户输入时，不再反向调用客户端

**多轮交互改为结果驱动。**MRTR 是 Multi Round-Trip Requests，即多轮往返请求。服务器处理工具、资源或提示词时，如需客户端补充输入，就返回 `resultType: "input_required"`。客户端完成输入后，重新发起原调用，而不是 POST 一条独立 JSON-RPC response。[5]

```text
客户端                              任意兼容服务端副本
  │ POST tools/call，id=A                    │
  ├────────────────────────────────────────►│
  │ input_required                          │
  │ inputRequests + 可选 requestState       │
  ◄─────────────────────────────────────────┤
  │                                         │
  │ 本地收集用户输入或履行已声明能力         │
  │                                         │
  │ POST 原调用，id=B                        │
  │ inputResponses + 原样 requestState       │
  ├────────────────────────────────────────►│
  │ complete，或下一轮 input_required       │
  ◄─────────────────────────────────────────┤
```

**请求 ID 必须更新。**再次进入时使用新 JSON-RPC ID，`requestState` 则逐字节原样回传。原方法和业务参数保持对应关系，新增 `inputResponses` 承载答案。TypeScript 客户端支持自动履行，默认最多 10 轮，并可关闭自动履行。[4]

**能力声明决定可请求内容。**服务器只能索取客户端已经声明支持的能力。若调用方未声明某种 elicitation 能力，服务器不能要求它执行相应输入交互。缺失能力错误使用 `MissingRequiredClientCapabilityError`，错误码为 `-32021`。[9]

**MRTR 减少连接绑定。**等待用户确认可能远长于实际计算。把等待状态封装为受保护的 payload 后，服务器可以释放本次 HTTP 请求。下一轮到达另一副本也能继续，前提是状态验证、授权和相关业务存储跨副本一致。

**新系统应减少旧能力依赖。**正式公告将 Roots、Sampling 和 Logging 标为弃用，保留至少 12 个月窗口。MRTR 为双时代工具提供交互迁移路径，但新工具不宜因此继续扩大这些旧能力的依赖。[5]

本节参考文献：
[5] MCP 发布公告 <https://blog.modelcontextprotocol.io/posts/2026-07-28/> 摘录：“The 2026-07-28 Model Context Protocol specification is out, bringing a stateless protocol core, Multi Round-Trip Requests, header-based routing, cacheable list results, authorization hardening, a formal extensions framework, and updated Tier 1 SDKs. July 28, 2026 · 12 min · David Soria Parra (Lead Maintainer), Den Delimarsky (Lead Maintainer) Since our last November release MCP continued to grow at an astonishing rate. Across our Tier 1 SDKs, we’re seeing close to half-a-billion downloads a month, with both TypeScript and Python SDKs crossing the 1 billion total downloads threshold. In just a few months, the protocol continued to grow as the data a…”
[4] TypeScript 版本迁移 <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> 摘录：“(Typings published before 2.0.0-alpha.4 predate this exclusion: there the typed maps still carry the tasks/ entries and the CreateTaskResult the isCallToolResult guard if you are pinned to one of those alphas. 2.0.0-alpha.4 and later include the exclusion.) Where task interop is genuinely required, use the explicit-schema custom-method form on both sides: request({ method: 'tasks/get', params }, resultSchema) setRequestHandler('tasks/get', { params, result }, handler) to serve, with the schemas of the revision you are talking to (GetTaskResultSchema is the 2025-11-25 shape). 2026-era connection only tasks/get and tasks/cancel , the two names the Ta…”
[9] TypeScript server v2.0.0 <https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/@modelcontextprotocol/server@2.0.0> 摘录：“Repository navigation @modelcontextprotocol/server@2.0.0 Minor Changes Thanks @felixweinberger! - Export theProtocol base class andmergeCapabilities from the@modelcontextprotocol/client and@modelcontextprotocol/server package roots, restoring the v1 import for consumers that subclassProtocol the MCP Apps SDK). The client and server packages each bundle their own compiled copy of the class, so import it from one package consistently within a process.The codemod now rewrites andmergeCapabilities imports fromshared/protocol.js to the client or server package root, like the module's other symbols, instead of dropping them with an action-required marker.”

### 长期通知通过 subscriptions/listen

**长期变化单独订阅。**工具目录变化、提示词目录变化和资源更新，使用 `subscriptions/listen` 的 POST 响应流。客户端选择通知类型，服务器先确认，再推送匹配事件，并使用订阅标识关联通知。[13]

**两类流不能混用。**工具执行进度留在该工具的请求流，目录变化留在 listen 流。这样一个工具请求取消时，只关闭自己的响应，不会把整个客户端的变化订阅一并终止。

**订阅恢复依赖重新读取。**现代 listen 流不提供事件重放。连接中断后，客户端应重新 listen，并获取相关资源或列表的当前状态。它适合“变化提示＋重新读取”，不应直接承担不能丢失的业务事件日志。[14]

本节参考文献：
[13] 发现与按请求协商 <https://modelcontextprotocol.io/specification/2026-07-28/changelog> 摘录：“Major changes Remove protocol-level sessions and the Mcp-Session-Id header from the Streamable HTTP transport. List endpoints (tools/list ,resources/list ,prompts/list ) no longer vary per-connection. Servers that need cross-call state use expli…”
[14] Python 订阅部署说明 <https://py.sdk.modelcontextprotocol.io/run/deploy/> 摘录：“Deploy & scale Your server works. Now it needs a real hostname, and more than one worker behind it. Almost none of that is MCP's business. You bring the ASGI server, the process manager, the load balancer. What this page has is the short list of…”

### 错误与取消必须区分处理阶段

**HTTP 状态表达入口问题。**请求尚未进入响应流时，可用 HTTP 状态拒绝格式、版本、认证或方法错误。若 SSE 已经发送 HTTP 200，之后不能改写状态，只能在流内发送对应 JSON-RPC error。[9]

| 情况 | HTTP 状态 | 消息语义 | 客户端处理 |
|---|---|---|---|
| 版本头与 `_meta` 不一致 | 400 | `-32020` | 修正请求 |
| 不支持协议版本 | 400 | 支持版本列表 | 选择共同版本 |
| 缺少所需客户端能力 | 400 | `-32021` | 调整能力或调用 |
| 未实现 RPC 方法 | 404 | `-32601` | 判断方法支持 |
| 现代 GET、DELETE | 405 | 方法不允许 | 不建立旧通道 |
| Accept 不满足 | 406 | 表示形式不接受 | 修复请求头 |
| POST 非 JSON 媒体类型 | 415 | 媒体类型不支持 | 修复 Content-Type |

这些规则分别由传输规范、官方测试和 TypeScript 发布说明支持。错误媒体类型在现代入口按 415 处理；旧传输测试中的历史状态应留在对应版本用例内。[3][15][9]

**断流就是取消信号。**现代 SSE response stream 关闭后，服务器必须将其视为该请求取消，并尽快停止工作，不再发送后续消息。客户端不应再额外 POST `notifications/cancelled`。[3]

**取消不是事务回滚。**若数据库提交或外部写入已经完成，关闭 HTTP 流不会自动撤销副作用。工程上必须把“停止继续计算”“查询已提交结果”和“撤销业务操作”分成不同机制。

**本节判断。**现代协议的核心不是“把消息改成 POST”，而是让一个 POST 拥有完整上下文、独立响应和独立取消边界。可靠业务状态必须位于这个边界之外。

本节参考文献：
[9] TypeScript server v2.0.0 <https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/@modelcontextprotocol/server@2.0.0> 摘录：“handshake against it — a hard connect failure against a modern-only server such as go-sdk v1.7.0-pre.3), and the server rejected conforming clients that omitclientInfo - The 2026 wire schemas are the final revision exactly: no body onDiscoverResult , envelopeclientInfo optional (a present-but-malformed value still fails validation). - Servers stamp _meta 'io.modelcontextprotocol/serverInfo' on every 2026-era respon…”
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“PT9iYXNlNjQ/bGl0ZXJhbD89? Scenario: Parameter value provided Client Behavior: Client MUST include the header Server Behavior: Server MUST validate header matches body Scenario: Parameter value is null Client Behavior: Client MUST omit the header Server Behavior: Server MUST NOT expect the header Scenario: Parameter not in arguments Client Behavior: Client MUST omit the header Server Behavior: Server MUST NOT expect…”
[15] 官方传输测试 <https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/shared/test_streamable_http.py> 摘录：“description= Tool that sends notification1, closes stream, sends notification2, notification3 , input_schema={ type : object , properties : {}}, name= tool_with_standalone_stream_close , description= Tool that closes standalone GET stream mid-operation , input_schema={ type : object , properties : {}}, async def _handle_call_tool(ctx: ServerRequestContext ServerState , params: CallToolRequestParams) - CallToolResul…”

## 三、服务端如何具体实现

本节参考文献：
[9] TypeScript server v2.0.0 <https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/@modelcontextprotocol/server@2.0.0> 摘录：“Repository navigation @modelcontextprot…”
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in proto…”
[15] 官方传输测试 <https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/shared/test_streamable_http.py> 摘录：“Repository navigation Expand file tree…”

### 推荐的落地结构

**入口优先使用官方 SDK。**JSON-RPC 分派、协议时代判断、媒体类型选择和 SSE 编码应尽量交给官方实现。应用负责可信身份、工具授权、持久化状态、幂等性和资源预算。

| 实施阶段 | 具体决策 | 验收结果 |
|---|---|---|
| 依赖锁定 | 固定规范与 SDK tag | 构建可复现 |
| HTTP 入口 | 一个 `/mcp` 路由 | 现代请求不建会话 |
| 传输处理 | SDK 分派 JSON 或 SSE | 媒体类型和错误正确 |
| 业务状态 | 显式句柄与外部存储 | 请求可换副本 |
| 安全与资源 | 认证、授权、有界队列 | 越权与过载被拒绝 |
| 兼容发布 | 旧新路径隔离 | 可观察、可回滚 |

**推荐拆成三层。**第一层是 HTTP 安全和接入控制；第二层是 MCP handler；第三层是业务服务。工具处理函数依赖第三层，而不是直接依赖某个 transport 或 TCP 连接。这样同一业务逻辑可以同时服务现代和旧协议。

**请求校验只做一次。**如果框架已经解析 body，应确认 SDK 接口如何接收解析结果。若 SDK 需要原始 Request，则不要在前置中间件中无界读取并消耗流。日志记录也不能为了打印 body 再复制一份大型请求。

本节参考文献：
[9] TypeScript server v2.0.0 <https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/@modelcontextprotocol/server@2.0.0> 摘录：“The JSON-RPC error body is unchanged, every other error code (including a handler relaying a downstream peer's-32020 ) keeps the origin-keyed in-band behavior, and the mapping only applies while the response is uncommitted: an exchange that already streamed — or one hosted withr…”
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“- The body of the HTTP POST MUST be a single JSON-RPC request or notification. The client MUST NOT send JSON-RPC responses. - If the body is a JSON-RPC notification: - If the server accepts it, the server MUST return HTTP status code 202 Accepted with no body. - If the server ca…”
[15] 官方传输测试 <https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/shared/test_streamable_http.py> 摘录：“await request_body.send({ type : http.request , body : json.dumps(body).encode(), more_body : False}) with anyio.fail_after(5): await transport.handle_request(scope, incoming.receive, send) return next(message status for message in sent if message type == http.response.start ) @…”

### Python：最小服务与 ASGI 挂载

**最小服务可以很短。**下面采用官方 Python v2 的类名和运行参数。它适合先验证现代 JSON 响应路径，工具返回值由 SDK 转换成协议结果。[11]

```python
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("tool-hub")

@mcp.tool()
def add(a: int, b: int) -> dict[str, int]:
    """返回两个整数的和。"""
    return {"result": a + b}

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8000,
        stateless_http=True,
        json_response=True,
    )
```

**配置位置发生了变化。**v2 将 `json_response`、`stateless_http`、host、port、路径和传输安全参数，从旧构造器移到 `run()` 或 `streamable_http_app()` 等入口。旧版示例里的 `FastMCP(..., stateless_http=True)` 不能只改类名就当成 v2 配置。[11]

**两个参数不是同一轴。**`json_response=True` 选择单次 JSON 响应；需要进度流时使用 SSE 对应模式。`stateless_http=True` 主要影响旧协议兼容路径是否保留 transport session。现代 2026-07-28 本身就是无协议会话，不能靠这个开关“升级”旧消息格式。[16]

**挂载必须保留生命周期。**已有 FastAPI 或 Starlette 服务可使用 `streamable_http_app()`。宿主应用需要执行 SDK 对应 lifespan，确保运行时资源初始化与退出清理完整。Anyscale 的部署示例也显式把 MCP app 的 lifespan 交给宿主应用。[14][17]

下面是挂载结构伪代码；`mount_with_lifespan` 和安全封装函数属于应用层。

```python
mcp_app = mcp.streamable_http_app(
    stateless_http=True,
    json_response=False,
    transport_security=security_settings,
)

app = mount_with_lifespan(
    child=mcp_app,
    mount_path="/",
    child_lifespan=mcp_app.lifespan,
)

app = apply_http_security(
    app,
    host_allowlist=public_hosts,
    origin_allowlist=browser_origins,
    bearer_verifier=token_verifier,
)
```

**挂载路径要算清楚。**若 MCP app 内部已经使用 `/mcp`，宿主再挂到 `/api`，最终 URL 就是 `/api/mcp`。再次挂到 `/mcp` 可能得到重复路径。入口、OAuth resource URI、客户端 URL 和网关路由必须采用同一公开地址。

本节参考文献：
[11] Python v2 迁移 <https://github.com/modelcontextprotocol/python-sdk/blob/e8e64842/docs/migration.md> 摘录：“This guide covers the breaking changes introduced in v2 of the MCP Python SDK and how to update your code. Version 2 of the MCP Python SDK introduces several breaking changes to improve the API, align with the MCP specification, and provide better type safety. The deprecated streamablehttp_client function has been removed. Use streamable_http_client Before (v1): from mcp.client.streamable_http import streamablehttp_client async with streamablehttp_client( headers={ Authorization : Bearer token }, sse_read_timeout=300, auth=my_auth, ) as (read_stream, write_stream, get_session_…”
[16] Python 双时代入口 <https://github.com/modelcontextprotocol/python-sdk/issues/2893> 摘录：“You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert A single HTTP entry that branches: legacy traffic goes to the existing manager untouched; modern traffic goes to a new sessionless path. This is where the sessionless wire mode and the inbound header validation live. What's in it Single entry point that branches legacy → existing StreamableHTTPSessionManager (untouched, including stateless_htt…”
[14] Python 订阅部署说明 <https://py.sdk.modelcontextprotocol.io/run/deploy/> 摘录：“Deploy & scale Your server works. Now it needs a real hostname, and more than one worker behind it. Almost none of that is MCP's business. You bring the ASGI server, the process manager, the load balancer. What this page has is the short list of things that are MCP's business: one setting that gates every deployment, and the two places where more than one worker changes what the SDK does. Before anything else: the Host allowlist streamable_http_app() cannot know which hostname it will be served behind, so it assumes the safest answer: localhost. With no transport_security= , t…”
[17] ASGI 挂载示例 <https://docs.anyscale.com/mcp/scalable-remote-mcp-deployment> 摘录：“Deploy scalable MCP servers with Ray Serve Deploy scalable MCP servers with Ray Serve Transform local Model Context Protocol (MCP) servers into production services on Anyscale using Ray Serve. This guide covers transport protocols, statelessness, ingress configuration, autoscaling, resource allocation, observability, high availability, authentication, and validation. Why use Ray Serve and Anyscale services for MCP deployment Ray Serve provides the following advantages when you deploy MCP: - Automatic scaling: Adjusts replicas based on traffic to meet demand. - Load balancing:…”

### TypeScript：使用 factory 构建每请求 handler

**现代入口是 createMcpHandler。**官方 v2 提供 `createMcpHandler(factory)`，按请求创建处理实例。Web Standard runtime 可直接使用 handler；Node.js 框架通过 `toNodeHandler` 适配。[4]

下面是接口级伪代码。公开入口名称来自 SDK；认证、业务依赖和工具注册函数是应用注入点。

```typescript
const handler = createMcpHandler(
  () => {
    const server = buildServer({
      name: "tool-hub",
      services: sharedBusinessServices,
      requestStateVerifier,
      subscriptionBus: sharedSubscriptionBus,
    });

    registerTools(server);
    return server;
  },
  {
    legacy: "reject",
    keepAliveMs: 15_000,
  }
);

// Web Standard 主机
async function fetch(request: Request): Promise<Response> {
  const early = await validateHostOriginAndCors(request);
  if (early) return early;

  const principal = await authenticate(request);
  return runWithPrincipal(principal, () => handler(request));
}

// Node.js 主机：由适配器承接同一个 handler
const nodeHandler = toNodeHandler(fetch);
```

**兼容策略要显式设置。**默认 `legacy: "stateless"` 可让同一 factory 服务旧时代的无状态流量。现代专用入口可使用 `legacy: "reject"`。已有旧有状态服务则应在前面分流，不要让现代 factory 无意接管旧 session。[4]

**共享的是业务依赖。**数据库连接池、HTTP 连接池和只读工具目录可以在进程级复用。认证上下文、取消信号、进度通道和本次调用状态必须按请求隔离。工厂模式不意味着每次请求都重新建立数据库连接。

**Anthropic 示例提供了起点。**其 Express scaffold 对每个 POST 新建 `sessionIdGenerator: undefined` 的 transport，并在 response close 时关闭 transport。这适合 API 包装型服务。现代 v2 实现应进一步使用 factory 管理请求隔离，不把示例中的外层对象布局直接当成并发保证。[12]

本节参考文献：
[4] TypeScript 版本迁移 <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> 摘录：“(Typings published before 2.0.0-alpha.4 predate this exclusion: there the typed maps still carry the tasks/ entries and the CreateTaskResult the isCallToolResult guard if you are pinned to one of those alphas. 2.0.0-alpha.4 and later include the exclusion.) Where task interop is genuinely required, use the explicit-schema custom-method form on both sides: request({ method: 'tasks/get', params }, resultSchema) setRequestHandler('tasks/get', { params, result }, handler) to serve, with the schemas of the revision you are talking to (GetTaskResultSchema is the 2025-11-25 shape). 2026-era connection only tasks/get and tasks/cancel , the two names the Tasks extension keeps, are served and sent this way; tasks/result and tasks/list refused there. With no handler registered, inbound tasks/ requests get -32601 The experimental tasks interception layer is removed entirely — see upgrade-to-v2.md › Experimental tasks interception removed. Axis 2025-era (2024-10-07 … 2025-11-25) 2026-07-28 Server HTTP entry Streamab…”
[12] Anthropic HTTP 示例 <https://github.com/anthropics/claude-plugins-official/blob/main/plugins/mcp-server-dev/skills/build-mcp-server/references/remote-http-scaffold.md> 摘录：“Minimal working servers in both recommended frameworks. Start here, then add tools. npm install @modelcontextprotocol/sdk zod express npm install -D typescript @types/express @types/node tsx src/server.ts import { McpServer } from @modelcontextprotocol/sdk/server/mcp.js ; import { StreamableHTTPServerTransport } from @modelcontextprotocol/sdk/server/streamableHttp.js ; import express from express ; import { z } from zod ; const server = new McpServer( { name: my-service , version: 0.1.0 }, { instructions: Prefer search_items before calling get_item directly — IDs aren't guessable. }, // Pattern A: one tool per action server.registerTool( search_items , description: Search items by keyword. Returns up to limit matches ranked by relevance. , inputSchema: { query: z.string().describe( Search keywords ), limit: z.number().int().min(1).max(50).default(10), annotations: { readOnlyHint: true }, async ({ query, limit }, extra) = { // extra.signal is an AbortSignal — check it in long loops for cancellation const…”

### 路由、分派和流生命周期

**处理链应先拒绝再执行。**推荐顺序是：接入限制、Host/Origin、CORS、认证、协议校验、工具授权、资源准入，最后执行业务。工具副作用不能发生在头体一致性和权限验证之前。

```text
handle(request):
    处理独立 health 路由
    校验路径、Host、Origin，处理允许的 CORS preflight
    从可信认证层取得 principal

    若为已启用的 legacy 流量:
        交给隔离的 legacy handler

    要求现代 RPC 使用 POST
    在解析前实施 body/header 大小限制
    校验 Content-Type 与 Accept
    解析单条 JSON-RPC 消息
    校验协议 envelope 及所有适用镜像头
    校验 method、tool、resource 与 principal 权限

    取得本工具的并发准入许可
    创建独立 cancellation scope 与事件通道
    交给 SDK 分派并序列化结果

    finally:
        取消未完成子任务
        解绑订阅、清理临时资源
        归还并发许可
```

**SSE 写出必须有背压。**生产者生成事件快于网络消费时，不能无限追加内存数组。每个流应有有界队列，并等待可写状态；连接关闭时，阻塞在队列和下游 I/O 上的任务也应被取消。

```text
serve_request_stream(context, writer):
    启动受 context.cancel 控制的工具任务

    try:
        while 收到当前请求的事件:
            若已取消，立即停止
            等待 writer 可写
            写入完整 SSE frame
        写入最终 JSON-RPC response
    finally:
        停止心跳
        取消剩余生产任务
        关闭当前请求事件队列
        释放当前请求资源
```

**关闭清理必须幂等。**客户端取消、代理断连、工具异常和进程排空都可能触发同一清理路径。资源释放函数应允许重复调用，避免一次取消又引起第二次异常，掩盖原始失败。

**最终响应要保留空间。**进度信息可以限频或合并，但最终结果和协议错误不能被当成普通进度静默丢弃。队列满时，应暂停生产者，或按明确策略终止请求。不要继续写入已经断开的流。

本节参考文献：
[4] TypeScript 版本迁移 <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> 摘录：“Axis: Client cancellation (Streamable HTTP) 2025-era (2024-10-07 … 2025-11-25): POST notifications/cancelled 2026-07-28: close the request's SSE response stream Axis: ctx.mcpReq.log() level filter 2025-era (2024-10-07 … 2025-11-25): session-scoped logging/setLevel 2026-07-28: per-request _meta.logLevel envelope key (absent = opt-out) Axis: 400 JSON-RPC error body 2025-era (2024-10-07 … 2025-11-25): SdkHttpError 2026-07-28: ProtocolError (in-band) Axis: Era-mismatched spec method (outbound) 2025-era (2024-10-07 … 2025-11-25): n/a 2026-07-28: SdkError(MethodNotSupportedByProtocolVersion)”
[12] Anthropic HTTP 示例 <https://github.com/anthropics/claude-plugins-official/blob/main/plugins/mcp-server-dev/skills/build-mcp-server/references/remote-http-scaffold.md> 摘录：“Claude Code claude mcp add --transport http name url (add --scope user for global, --header Authorization: Bearer ... for auth) Claude Desktop / Claude.ai Settings → Connectors → Add custom connector. Not claude_desktop_config.json — remote servers configured there are ignored. Connector directory Anthropic maintains a submission guide for listing in the public connector directory. Fastest path: Cloudflare Workers — two commands from zero to a live https:// URL on the free tier. Uses a Workers-native scaffold (not Express). → deploy-cloudflare-workers.md This Express scaffold runs on any Node host — Render, Railway, Fly.io, a VPS. Containerize it (node:20-slim , copy, npm ci , node dist/server.js FastMCP is the same story with a Python base image. responds toinitialize with server capabilities - returns your…”

### 将协议状态、业务状态和多轮状态分开

**现代服务仍可有业务状态。**官方建议让创建工具返回显式句柄，例如 `basket_id` 或 `browser_id`。后续工具将句柄作为普通参数传回，服务端据此查找业务对象。[18]

| 状态类型 | 推荐保存位置 | 生命周期 | 跨副本要求 |
|---|---|---|---|
| 当前请求上下文 | 请求内存 | 一个 POST | 不跨请求复用 |
| 业务句柄与结果 | 外部持久化存储 | 业务 TTL | 任意副本可读取 |
| MRTR `requestState` | 受保护 payload 或状态引用 | 多轮交互 TTL | 共享验证配置 |
| 旧协议 session | 兼容层 manager | 会话关闭或过期 | 亲和路由或专门共享设计 |

**句柄不是通行证。**应以可信 token 派生的 principal 绑定状态，例如使用 `<user_id>:<handle>` 查找。每次调用都重新检查 owner、租户、对象状态和权限。不能因为调用方知道一个随机 ID，就允许访问对象。[19]

**requestState 也不可信。**它由客户端携带往返，服务器必须验证完整性、principal、原始方法、参数和过期时间。TypeScript 提供的 `createRequestStateCodec` 使用 HMAC-SHA256 签名，但不加密；敏感数据不应因“已签名”就直接放入可读 payload。[4]

**业务连续性优先使用耐久对象。**对导出、审批或长任务，可让创建工具提交一个持久化任务并返回 `job_id`，后续通过查询工具读取状态。这里的工具名和对象结构属于应用协议，不自动等同于 MCP Tasks 扩展。Python `v2.0.0` 的发布说明明确将 Tasks 扩展列为该版本之外的能力。[8]

本节参考文献：
[18] 显式状态句柄 <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/> 摘录：“The release candidate for MCP 2026-07-28 is now available. It is the largest revision of the protocol since launch and delivers on the 2026 roadmap: - a stateless core that scales on ordinary HTTP infrastructure - extensions including server-rendered UIs through MCP Apps and long-runni…”
[19] 状态句柄安全 <https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices> 摘录：“Introduction Purpose and Scope This document provides security considerations for the Model Context Protocol (MCP), complementing the MCP Authorization specification. This document identifies security risks, attack vectors, and best practices specific to MCP implementations. The primar…”
[4] TypeScript 版本迁移 <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> 摘录：“(Typings published before 2.0.0-alpha.4 predate this exclusion: there the typed maps still carry the tasks/ entries and the CreateTaskResult the isCallToolResult guard if you are pinned to one of those alphas. 2.0.0-alpha.4 and later include the exclusion.) Where task interop is genuin…”
[8] Python v2.0.0 <https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0> 摘录：“Repository navigation MCP Python SDK v2 Stable Release This is v2.0.0, the stable v2 release of the MCP Python SDK. It supports the 2026-07-28 revision of the Model Context Protocol and serves every earlier revision from the same server. pip install mcp now installs 2.x. pip install mc…”

### 并发、队列和资源限制

**无会话不等于无上限。**现代路径取消了 session 容量，但仍有活跃请求、SSE 流、订阅、下游连接和业务任务。应对这些资源分别限额，不能仅设置进程内存上限后等待过载。

| 控制项 | 数值或表达 | 本文使用方式 |
|---|---|---|
| Python v2 HTTP body | 4 MiB | 官方稳定入口大小基线 |
| SSE 心跳 | 15,000 毫秒 | TypeScript 配置基线 |
| `requestState` TTL | 600 秒 | Python 部署文档参考 |
| 共享状态密钥 | 至少 32 bytes | 所有副本一致 |
| legacy 空闲时间 | 1,800 秒 | 兼容层实施参考值 |
| legacy 会话上限 | 10,000 个 | 兼容层实施参考值 |
| 事件队列 | 字节预算与条数双限制 | 应用定义 |
| 工具并发 | 按下游与资源预算决定 | 应用定义 |

4 MiB 请求体限制及 HTTP 413 来自 Python `v2.0.0` 发布说明。会话空闲与容量值来自 session manager 文档，在这里作为兼容层配置参考，而不反推为 `v2.0.0` 的全部默认行为。[8][20][14]

**准入必须按工具隔离。**查询数据库、调用 SaaS API 和执行 GPU 推理，受不同资源限制。推荐设置全局准入、租户配额和工具级并发池。Anyscale 也建议将阻塞模型调用卸载到线程或进程，保持事件循环可响应。[17]

**队列容量可以直接计算。**设单流队列字节预算为 \(B_q\)，最大事件大小为 \(E_{\max}\)，则最多容纳的完整事件数受下式限制。实现仍应同时限制条数，防止大量小对象产生额外开销。

$$Q_{\max}\leq\left\lfloor B_q/E_{\max}\right\rfloor$$

**会话数不能代替请求数。**若错误地允许 10,000 个活跃请求各缓存 4 MiB body，仅 body 就是 `10,000×4=40,000 MiB`，约 `39.1 GiB`，还未计入解析对象和响应缓冲。这是由两个上限构成的极端预算计算，不是 SDK 的内存测量。

**本节判断。**新服务采用每请求 handler、外部业务状态和有界流队列。只有明确依赖旧协议功能时，才增加 session manager 与事件重放兼容层。

本节参考文献：
[8] Python v2.0.0 <https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0> 摘录：“Repository navigation MCP Python SDK v2 Stable Release This is v2.0.0, the stable v2 release of the MCP Python SDK. It supports the 2026-07-28 revision of the Model Context Protocol and serves every earlier revision from the same server. pip install mcp now installs 2.x. pip install mcp cli uv add mcp cli Documentation Rewrite The documentation has the full tutorial and API…”
[20] session manager 参数 <https://py.sdk.modelcontextprotocol.io/api/mcp/server/streamable_http_manager/> 摘录：“395 class StreamableHTTPSessionManager: Manages StreamableHTTP sessions with optional resumability via event store. This class abstracts away the complexity of session management, event storage, and request handling for StreamableHTTP transports. Session tracking for clients Resumability via an optional event store Connection management and lifecycle Request handling and tr…”
[14] Python 订阅部署说明 <https://py.sdk.modelcontextprotocol.io/run/deploy/> 摘录：“Deploy & scale Your server works. Now it needs a real hostname, and more than one worker behind it. Almost none of that is MCP's business. You bring the ASGI server, the process manager, the load balancer. What this page has is the short list of things that are MCP's business: one setting that gates every deployment, and the two places where more than one worker changes wha…”
[17] ASGI 挂载示例 <https://docs.anyscale.com/mcp/scalable-remote-mcp-deployment> 摘录：“Deploy scalable MCP servers with Ray Serve Deploy scalable MCP servers with Ray Serve Transform local Model Context Protocol (MCP) servers into production services on Anyscale using Ray Serve. This guide covers transport protocols, statelessness, ingress configuration, autoscaling, resource allocation, observability, high availability, authentication, and validation. Why us…”

## 四、客户端接入、重试和互操作

本节参考文献：
[8] Python v2.0.0 <https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0> 摘录：“Repository navigation MCP Python SDK v2…”
[20] session manager 参数 <https://py.sdk.modelcontextprotocol.io/api/mcp/server/streamable_http_manager/> 摘录：“395 class StreamableHTTPSessionManager:…”
[14] Python 订阅部署说明 <https://py.sdk.modelcontextprotocol.io/run/deploy/> 摘录：“Deploy & scale Your server works. Now i…”
[17] ASGI 挂载示例 <https://docs.anyscale.com/mcp/scalable-remote-mcp-deployment> 摘录：“Deploy scalable MCP servers with Ray Se…”

### 现代客户端的调用顺序

**现代连接不需要 initialize。**客户端先选择固定版本或自动发现策略，再配置认证和能力处理器。之后可以发现工具并调用，SDK 应为每条请求构造独立元数据。[4]

| TypeScript 协商模式 | 发现行为 | 遇到旧服务器 | 推荐场景 |
|---|---|---|---|
| `legacy`，默认 | 不探测现代能力 | 直接旧握手 | 保持既有行为 |
| `auto` | 调用 `server/discover` | 回到旧握手 | 混合服务器 |
| 固定 `2026-07-28` | 仅允许现代协议 | 明确失败 | 已完成现代验收 |

TypeScript v2 的默认协商仍是 legacy，因此“换成 v2 包”不自动等于“本次连接采用现代协议”。[4]

**Python 优先使用高层 Client。**官方客户端教程要求 Python MCP SDK `2.0.0` 或以上。v2 的高层 `Client(target)` 将 transport、session 和初始化处理统一起来，可以直接面向 URL 使用。[21][8]

下面保留官方高层接口的调用形态，作为接入骨架。

```python
async def use_server():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        result = await client.call_tool(
            "add",
            {"a": 1, "b": 2},
        )
        print(result.structured_content)
        # 本文服务端工具的结果为 {"result": 3}
```

**低层返回值也有变化。**v1 的 `streamable_http_client` 返回读流、写流和 session ID 回调三项；v2 返回读流和写流两项。自建 HTTP client 时，headers、认证与超时配置也应按迁移文档移动，不能沿用旧参数位置。[11]

本节参考文献：
[4] TypeScript 版本迁移 <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> 摘录：“(Typings published before 2.0.0-alpha.4 predate this exclusion: there the typed maps still carry the tasks/ entries and the CreateTaskResult the isCallToolResult guard if you are pinned to one of those alphas. 2.0.0-alpha.4 and later include the exclusion.) Where task interop is genuinely required, use the explicit-schema custom-meth…”
[21] 官方客户端教程 <https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client> 摘录：“- TypeScript You can find the complete code for this tutorial here.Add That The client will: System Requirements Before starting, ensure your system meets these requirements:- Mac or Windows computer - Latest Python version installed - Latest version of installed - You must use the Python MCP SDK 2.0.0 or higher Setting Up Your Envir…”
[8] Python v2.0.0 <https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0> 摘录：“Repository navigation MCP Python SDK v2 Stable Release This is v2.0.0, the stable v2 release of the MCP Python SDK. It supports the 2026-07-28 revision of the Model Context Protocol and serves every earlier revision from the same server. pip install mcp now installs 2.x. pip install mcp cli uv add mcp cli Documentation Rewrite The do…”
[11] Python v2 迁移 <https://github.com/modelcontextprotocol/python-sdk/blob/e8e64842/docs/migration.md> 摘录：“This guide covers the breaking changes introduced in v2 of the MCP Python SDK and how to update your code. Version 2 of the MCP Python SDK introduces several breaking changes to improve the API, align with the MCP specification, and provide better type safety. The deprecated streamablehttp_client function has been removed. Use stream…”

### 自建客户端需要实现的状态机

**状态机要围绕一次逻辑调用。**JSON-RPC ID 标识某次协议请求，业务操作 ID 标识一次逻辑操作。网络重试与 MRTR 会产生多个协议请求，但应保留同一个业务操作身份，以防重复执行副作用。

```text
invoke(method, original_params):
    选择已支持的协议版本
    创建本次逻辑操作的 operation_id
    continuation := 空

    循环:
        为本次 POST 分配新的 JSON-RPC id
        构造版本、能力与身份 _meta
        合并 inputResponses 和原样 requestState
        从 body 生成标准头及适用 Mcp-Param-* 头
        发送 POST，绑定本请求取消信号

        先分类 HTTP 状态
        再按 Content-Type 读取 JSON 或 SSE
        校验最终响应 id 与结果类型

        若 complete:
            返回业务结果

        若 input_required:
            检查能力和轮数预算
            调用已注册输入处理器
            保存原样 requestState
            继续原调用

        若断流:
            按幂等或任务查询策略处理
            不使用 Last-Event-ID
```

**能力要逐请求传入。**发现阶段知道客户端支持 elicitation，不代表后续任意请求都可从服务器内存中取用这一信息。服务器按当前请求声明判断是否允许嵌入输入请求。这也是同一客户端能够并行使用不同调用上下文的基础。

**MRTR 需要独立预算。**TypeScript 默认最多 10 轮自动履行，达到上限会产生明确 SDK 错误。应用还应给用户交互设置总时限，防止等估计不超过 600 秒（按默认 requestState TTL 600 秒）。的流程长期占用调用方逻辑状态。[4]

本节参考文献：
[4] TypeScript 版本迁移 <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> 摘录：“(Typings published before 2.0.0-alpha.4 predate this exclusion: there the typed maps still carry the tasks/ entries and the CreateTaskResult the isCallToolResult guard if you are pinned to one of those alphas. 2.0.0-alpha.4 and later include the exclusion.) Where task interop is genuinely required, use the explicit-schema custom-method form on both sides: request({ method: 'tasks/get', params }, resultSchema) setRequestHandler('tasks/get', { params, result }, handler) to serve, with the schemas of the revision you are talking to (GetTaskResultSchema is the 2025-11-25 shape). 2026-era connection only tasks/get and tasks/cancel , the two names the Tasks extension keeps, are served and sent this way; tasks/result and tasks/list refused there. With no handler registered, inbound tasks/ requests get -32601 The experimental tasks interception layer is removed entirely — see upgrade-to-v2.md › Experimental tasks interception removed. Axis 2025-era (2024-10-07 … 2025-11-25) 2026-07-28 Server HTTP entry StreamableHTTPServerTransport createMcpHandler (legacy: 'stateless' also serves 2025) Server stdio entry server.connect(new StdioServerTransport()) serveStdio(factory) (also serves 2025 unless legacy: 'reject' ) Client connect initialize handshake server/discover probe (versionNegotiation ) Client identity getClientCapabilities() / getClientVersion() (initialize-scoped)…”

### SSE 消费不能按网络 chunk 分割

**一个 chunk 不是一个事件。**代理和 TCP 都可能拆分或合并数据。客户端必须使用增量 UTF-8 解码和 SSE framing，处理空行分隔、多条 `data:` 行，以及以冒号开始的注释。

**解析后再分派 JSON-RPC。**进度通知交给回调；最终 response 必须匹配该 POST 的请求 ID。若普通工具流在最终响应之前结束，应归类为断流，不应把已经收到的进度当成成功结果。

**心跳不是业务事件。**规范鼓励长驻 listen 流使用 `:` 注释保活，客户端必须忽略。若解析器把心跳当成空 JSON，安静期就会出现误报。[3]

**浏览器应使用 POST 流读取。**现代路径需要请求 body、Bearer 认证和多个 MCP 头。原生 `EventSource` 的 GET 接口不对应这个调用模型，应使用支持 POST 响应流的 Fetch 或 SDK 实现。

**取消只影响当前调用。**TypeScript v2 支持每请求 `requestSignal`。现代连接上 abort 该 signal 会关闭对应 POST/SSE，作为协议取消信号。不要为取消一个工具而关闭整个共享客户端和所有订阅。[22]

本节参考文献：
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport from protocol version 2024-11-05. Revision 2026-07-28 changed the behavior of Streamable HTTP. Clients must ensure they handle backwards compatibility correctly. Changes included: - Removal of the GET stream endpoint. - Removal of protocol-level sessions. - The server exposes a single H…”
[22] 每请求取消接口 <https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/client/client/streamableHttp.html> 摘录：“MCP TypeScript SDK (V2) / @modelcontextprotocol/client / client/streamableHttp client/streamableHttp StreamableHTTPClientTransport Defined in: packages/client/src/client/streamableHttp.ts:343 Client transport for Streamable HTTP: this implements the MCP Streamable HTTP transport specification. It will connect to a server using HTTP POST for sending messages and HTTP GET with Server-Sent Eve…”

### 网络重试、认证重试和业务恢复分开

**重试首先看副作用。**只读查询可以重新发起；创建工单、提交审批和外部写入，应先检查操作记录或使用业务幂等键。新的 JSON-RPC ID 本身不提供幂等保证。

| 失败类别 | 推荐动作 | 是否自动重试 | 版本降级 |
|---|---|---|---|
| HTTP 401 | 刷新或重新授权 | SDK 刷新后一次 | 不降级 |
| HTTP 403 | 判断权限或 scope | 按授权流程决定 | 不降级 |
| HTTP 406、415 | 修复请求表示 | 修复后再发 | 不降级 |
| HTTP 429、503 | 遵循限流与预算 | 仅安全调用 | 不降级 |
| 网络错误、5xx | 退避并检查幂等 | 有限重试 | 不作版本证据 |
| 现代 SSE 断流 | 新 ID 重发或查询任务 | 按业务语义决定 | 不续传事件 |
| legacy session 404 | 丢弃旧会话并重建 | 安全调用可重放 | 保持对应旧版本 |

**认证重试有明确边界。**TypeScript 的 `authProvider.token()` 在每个请求前获取 token。收到 401 后，如果提供 `onUnauthorized()`，刷新并重试一次；第二次仍为 401 则返回认证错误，不应无限循环。[22]

**退避参数必须标明所属路径。**TypeScript legacy transport 的默认值是：初始 1,000 毫秒、上限 30,000 毫秒、增长因子 1.5、最多两次重连。不能把这些默认值写成现代协议的统一网络恢复规则。[22]

**现代应用可以显式借用参数。**若希望采用同一组起点，可在应用重试层配置 1 秒基数、1.5 倍增长、30 秒上限和最多两次，并加入随机抖动。这是应用建议，不是协议默认；只对幂等调用或有幂等保护的操作启用。

$$d_k\sim U\left(0,\min\left(30,\;1\times1.5^{k-1}\right)\right)\ \text{秒}$$

**重试总时长可计算。**按前两次退避上界计算，等待最多为 `1＋1.5＝2.5 秒`。若每次尝试的全程上限是 \(T\)，三次尝试的逻辑调用预算上界是 \(3T+2.5\) 秒。认证刷新与用户输入耗时应另行纳入统一总预算。

**服务端成功可能先于客户端失败。**例如数据库已经提交，但最终 SSE frame 在代理处丢失。正确恢复方式是以同一业务操作键查询结果，或者幂等重发。盲目重跑可能产生第二份工单，而事件续传也不能替代业务去重。

本节参考文献：
[22] 每请求取消接口 <https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/client/client/streamableHttp.html> 摘录：“MCP TypeScript SDK (V2) / @modelcontextprotocol/client / client/streamableHttp client/streamableHttp StreamableHTTPClientTransport Defined in: packages/client/src/client/streamableHttp.ts:343 Client transport for Streamable HTTP: this implements the MCP Streamable HTTP transport specification. It will connect to a server using HTTP POST for sending messages and HTTP GET with Server-Sent Events for receiving messages. Constructors new StreamableHTTPClientTransport( ):StreamableHTTPClientTransport Defined in: packages/client/src/client/streamableHttp.ts:376 StreamableHTTPClientTransportOptions hasPerRequestStream hasPerRequestStream:true Defined in: packages/client/src/client/streamableHttp.ts:374 Streamable HTTP opens one POST (and SSE response stream) per outbound request and honors TransportSendOptions.requestSignal On a 2026-era connection the protocol layer aborts that per-request stream as the spec cancellation signal instead of POSTing notifications/cancelled Implementation of Defined in: packages/client/src/client/streamableHttp.ts:364 Callback for when the connection is closed for any reason. This should be invoked when close() is called as well. Implementation of Defined in: packages/client/src/client/streamableHttp.ts:365 Callback for when an error occurs. Note that errors are not necessarily fatal; they are used for reporting any kind of exceptional condition out of band. Implementation of Defined in: packages/client/src/client/streamableHttp.ts:366 Callback for when a message (request or response) is received over the connection. Includes the request and authInfo if the transp…”

### Claude 与官方客户端的互操作边界

**产品名称不能代替协议证据。**官方 SDK、Claude Code、Desktop、Claude.ai 和 API connector 各有版本和宿主限制。产品支持 HTTP transport，不代表它已经采用 2026-07-28 的全部核心消息格式。

| 客户端 | 版本或时间 | 已记录行为 | 工程处理 |
|---|---|---|---|
| Claude Code | 2.1.71，Linux | POST 成功，GET 405 被报告为失败 | 检查传输配置与旧探测 |
| Claude Code | 2.1.233，2026-08-17 | 维护者 GET 重测为 0 次 406 | 按环境保存回归样例 |
| Claude Desktop | 1.20186.9，2026-07-20 案例 | Code tab 连接器发现存在差异 | 分开测试 UI 与 CLI |
| Claude.ai | 2026 年 8 月报告 | 支持 HTTP 与旧 HTTP+SSE | 保留双时代接入 |
| Claude API connector | `mcp-client-2025-11-20` beta | 公开 HTTP 或 SSE 服务 | 按 connector 能力设计 |
| Managed Agents | 2026-08-05 更新 | HTTP 优先，SSE 自动 fallback | 区分早期 beta 行为 |

这些条目分别来自版本化问题记录、维护者回复和兼容性报告。[23][24][25][26][27]

**两份 Accept 记录不矛盾。**Claude Code 的报告者在重连 GET 上观察到缺少 Accept；维护者在 `2.1.233` 的严格服务器上重测，初始、重开和重连 GET 都带正确头。工程判断应落实到具体版本、代理和请求阶段，而不是断言所有 Claude HTTP 连接都有同一回归。

**Agent SDK 也有历史反例。**`@anthropic-ai/claude-agent-sdk 0.2.52` 的问题记录中，四个独立服务器都因缺少双值 Accept 返回 406。手动补头后请求成功。这个案例说明应检查实际发出的 wire headers，而不是仅检查服务端是否接受 curl。[10]

**接入入口应采用官方形式。**Claude Code 使用 `claude mcp add --transport http <name> <url>`。Desktop 与 Claude.ai 的远程服务通过 Connectors UI 添加，而不是按本地 stdio 条目写入 `claude_desktop_config.json`。[12]

**宿主限制要进入工具设计。**2026 年 8 月兼容性报告给出的 Claude.ai、Desktop 工具结果上限约为 150,000 字符，工具超时为 5 分钟，并列出资源订阅和 Sampling 等能力边界。大结果应分页或返回资源引用，长任务应返回可查询句柄。[26]

**本节判断。**客户端实现的关键不是“自动重连”，而是区分认证恢复、协议协商、输入续轮和业务重试。四者混在一起，最容易造成错误降级和重复副作用。

本节参考文献：
[23] Code 2.1.71 <https://github.com/anthropics/claude-code/issues/32708> 摘录：“for GET, per the MCP 2025-03-26 spec. Claude Code CLI handles this correctly — it POSTs theinitialize request and proceeds.What doesn't work: claude_desktop_config.json has no support forurl -based MCP servers at all. Adding url : without acommand field causes the Desktop app to sil…”
[24] Code 2.1.233 <https://github.com/anthropics/claude-code/issues/73444> 摘录：“github-actions commentedon Aug 24, 2026 Closing for now — we still need reproduction steps to investigate. Please open a new issue if this is still relevant. github-actions commentedon Oct 14, 2026 This issue has been automatically locked since it was closed and has not had any acti…”
[25] Desktop 发现案例 <https://github.com/anthropics/claude-code/issues/79491> 摘录：“Repository navigation Desktop app (Code tab): failed claude.ai connector fetch cached indefinitely — connector silently missing from all sessions until manually toggled 79491 - Claude Code: 2.1.215 - Claude desktop app: 1.20186.9 (macOS, Darwin 25.5.0) - Session type: Code tab in th…”
[26] Claude 兼容性报告 <https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/> 摘录：“Streamable HTTP with sessions 2025-03-26 through 2025-11-25 POST , optional GET , optional DELETE on /mcp initialize and notifications/initialized Optional MCP-Session-Id Stateless Streamable HTTP 2026-07-28 POST /mcp Optional server/discover , then self-contained requests No protoc…”
[27] Managed Agents 更新 <https://github.com/anthropics/anthropic-sdk-python/issues/1383> 摘录：“You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert {{ message }} Repository navigation Managed A…”
[10] Agent SDK 历史环境 <https://github.com/anthropics/claude-agent-sdk-typescript/issues/202> 摘录：“Repository navigation HTTP MCP transport does not send Accept: application/json, text/event-stream header, causing 406 on Streamable HTTP servers 202 @anthropic-ai/claude-agent-sdk : 0.2.52 (latest)@modelcontextprotocol/sdk : 1.27.1 (latest)- Node: 22+, Bun 1.3+ When using the Claud…”
[12] Anthropic HTTP 示例 <https://github.com/anthropics/claude-plugins-official/blob/main/plugins/mcp-server-dev/skills/build-mcp-server/references/remote-http-scaffold.md> 摘录：“Minimal working servers in both recommended frameworks. Start here, then add tools. npm install @modelcontextprotocol/sdk zod express npm install -D typescript @types/express @types/node tsx src/server.ts import { McpServer } from @modelcontextprotocol/sdk/server/mcp.js ; import { S…”

## 五、生产环境：安全、代理与水平扩展

本节参考文献：
[23] Code 2.1.71 <https://github.com/anthropics/claude-code/issues/32708> 摘录：“Repository navigation streamable-http M…”
[24] Code 2.1.233 <https://github.com/anthropics/claude-code/issues/73444> 摘录：“Repository navigation MCP HTTP client s…”
[25] Desktop 发现案例 <https://github.com/anthropics/claude-code/issues/79491> 摘录：“Repository navigation Desktop app (Code…”
[26] Claude 兼容性报告 <https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/> 摘录：“Migrate Your Claude Connector from SSE…”
[27] Managed Agents 更新 <https://github.com/anthropics/anthropic-sdk-python/issues/1383> 摘录：“我们跑生产环境遇到过类似的噩梦： 结果就是——我们的Agent需要同时维护4种…”
[10] Agent SDK 历史环境 <https://github.com/anthropics/claude-agent-sdk-typescript/issues/202> 摘录：“Repository navigation HTTP MCP transpor…”
[12] Anthropic HTTP 示例 <https://github.com/anthropics/claude-plugins-official/blob/main/plugins/mcp-server-dev/skills/build-mcp-server/references/remote-http-scaffold.md> 摘录：“Minimal working servers in both recomme…”

### 认证采用资源服务器模型

**远程服务应使用 TLS 与 OAuth。**受保护的 HTTP MCP 服务按 OAuth 2.1 resource server 模型实现。通过 Protected Resource Metadata 发现授权服务器，access token 必须明确签发给当前 MCP 资源。[19][28]

典型未认证响应与元数据如下；域名和 scope 名为部署示例。

```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer resource_metadata="https://mcp.example.com/.well-known/oauth-protected-resource"
```

```json
{
  "resource": "https://mcp.example.com/mcp",
  "authorization_servers": [
    "https://identity.example.com"
  ],
  "scopes_supported": [
    "tools:read"
  ]
}
```

**每次请求重新建立身份。**客户端获取 token 时通过 `resource` 指示目标 MCP 资源。服务端每个请求验证签发者、有效期、受众和权限范围，再生成可信 principal。不能在一次发现或初始化成功后，把后续 HTTP 请求视为已经认证。

**audience 要故障关闭。**Python OAuth 一致性改动明确记录：配置资源服务器 URL 后，已验证但缺少目标 resource 的 token，应返回 `401 invalid_token`。部署时应检查验证器或认证配置是否真正执行了受众约束，而不是只验证 JWT 签名。[29]

**入站 token 不能直接透传。**MCP 服务调用第三方 API 时，应使用单独的下游凭据或明确的授权交换。接受一个并非签发给自己的 token，再原样转发给下游，是官方安全文档禁止的 token passthrough 反模式。[19]

**工具授权仍需单独执行。**合法 token 只证明调用方获得了某些资源权限。具体工具、业务对象、租户和写入动作仍需校验。`readOnlyHint` 等工具注解不能替代服务端授权，也不能保证外部系统真正无副作用。

本节参考文献：
[19] 状态句柄安全 <https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices> 摘录：“Introduction Purpose and Scope This document provides security considerations for the Model Context Protocol (MCP), complementing the MCP Authorization specification. This document identifies security risks, attack vectors, and best practices specific to MCP implementations. The primary audience for this document includes developers implementing MCP authorization flows, MCP server operators, and security professionals evaluating MCP-based systems. This document should be read alongside…”
[28] 资源服务器部署说明 <https://agentcat.com/guides/configuring-mcp-installations-production/> 摘录：“This guide covers those, verified against the current spec revision — 2026-07-28 — and the SDKs that implement it, and skips the infrastructure you can get from any platform's docs. The throughline: a local stdio server and a production HTTP server are not the same program with a flag flipped. They have different transports, different auth, and a different threat model. Treating production as the dev server, but hosted is where the real bugs come from. The config you start from is the w…”
[29] Python audience 门禁 <https://github.com/modelcontextprotocol/python-sdk/pull/2999> 摘录：“2 issues found across 29 files Prompt for AI agents (unresolved issues) Check if these issues are valid — if so, understand the root cause of each and fix them. If appropriate, use sub-agents to investigate and fix each issue separately. file name= src/mcp/shared/auth_utils.py violation number= 1 location= src/mcp/shared/auth_utils.py:32 P2: Audience canonicalization can throw ValueError on malformed resource ports, breaking auth flow with a server error. /violation violation number= 2…”

### OAuth 发现和注册也属于攻击面

**授权服务身份必须绑定。**2026-07-28 加强了 RFC 9207 `iss` 校验和凭据的 issuer 隔离，并将 DCR 转向 CIMD。旧 DCR 在兼容窗口内继续工作，但新授权体系不宜只依赖开放动态注册。[5]

**SDK 功能需要显式接通。**TypeScript 迁移文档指出，部分授权硬化以 SDK opt-in 形式提供，不因协议版本自动启用。应接通 issuer stamp、discovery state、scope step-up 和相应持久化。OAuth 回调的 `state` 也需要调用方自行验证。[4][22]

**发现 URL 必须防 SSRF。**MCP client 可能根据远程元数据继续访问授权服务器或 CIMD URL。生产环境应要求 HTTPS，限制私网、loopback 和链路本地目标，并逐跳校验重定向。安全文档特别列出云元数据地址和本地服务作为风险目标。[19]

**URL 规范化会影响认证。**Prefect FastMCP 的 PR #4659 记录过一个具体问题：对外公布的是 `https://example.com/token`，内部却因尾斜杠生成 `https://example.com//token`。严格的 `private_key_jwt` audience 校验因此拒绝正常客户端。[30]

**两种 audience 不要混淆。**access token 的 audience 指向 MCP 资源；`private_key_jwt` 客户端断言的 audience 指向 token endpoint。前述回归测试直接断言“内部期望端点＝对外公布端点”，而不是用 fixture 预先注入一个正确 URL。

本节参考文献：
[5] MCP 发布公告 <https://blog.modelcontextprotocol.io/posts/2026-07-28/> 摘录：“The 2026-07-28 Model Context Protocol specification is out, bringing a stateless protocol core, Multi Round-Trip Requests, header-based routing, cacheable list results, authorization hardening, a formal extensions fr…”
[4] TypeScript 版本迁移 <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> 摘录：“(Typings published before 2.0.0-alpha.4 predate this exclusion: there the typed maps still carry the tasks/ entries and the CreateTaskResult the isCallToolResult guard if you are pinned to one of those alphas. 2.0.0-…”
[22] 每请求取消接口 <https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/client/client/streamableHttp.html> 摘录：“MCP TypeScript SDK (V2) / @modelcontextprotocol/client / client/streamableHttp client/streamableHttp StreamableHTTPClientTransport Defined in: packages/client/src/client/streamableHttp.ts:343 Client transport for Str…”
[19] 状态句柄安全 <https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices> 摘录：“Introduction Purpose and Scope This document provides security considerations for the Model Context Protocol (MCP), complementing the MCP Authorization specification. This document identifies security risks, attack v…”
[30] token endpoint 回归案例 <https://github.com/PrefectHQ/fastmcp/pull/4659> 摘录：“Repository navigation Bind CIMD assertion audience to the advertised token endpoint - 4659 Conversation A bare-authority base_url renders with a trailing slash, so the expected aud was while the metadata advertised @…”

### Host、Origin 与 CORS 各司其职

**Origin 校验是协议要求。**存在但不合法的 Origin 必须返回 403。无 Origin 的非浏览器客户端，不应仅因缺少该头而被拒绝。Host 校验还用于阻止攻击者把受控域名重新解析到本地服务。[3][7]

**CORS 不替代身份验证。**CORS 主要控制浏览器是否允许脚本读取响应，不阻止非浏览器直接请求。允许来源应列出具体域名；带凭据时不能使用 `Access-Control-Allow-Origin: *`。预检应允许应用实际使用的 Authorization、Content-Type 和 MCP headers。

**响应头也要可读取。**浏览器 OAuth 客户端可能需要读取 `WWW-Authenticate`。旧会话兼容客户端还可能需要读取 `Mcp-Session-Id`。应按接入路径配置 expose headers，而不是无差别暴露所有内部头。

**Python 部署要配置公开域名。**官方部署文档说明，默认 DNS rebinding 防护只接受本地 Host。真实域名部署应显式设置 `allowed_hosts`、`allowed_origins`；非法 Host 可在进入 MCP 前返回 HTTP 421，非法 Origin 返回 403。[14]

**代理头只能信任受控入口。**TLS 在 ingress 或负载均衡终止时，ASGI server 应正确识别转发协议。Uvicorn 可配置 `--proxy-headers` 和明确的 `--forwarded-allow-ips`。只有不存在绕过代理的入口时，才适合扩大转发头信任范围。[14]

本节参考文献：
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport from protocol version 2024-11-05. Revision 2026-07-28 changed the behavior of Streamable HTTP. Clients must ensure they handle backwards compatibility correctly. Changes included: - Removal of the GET stream endpoint. - Removal of protocol-le…”
[7] MCP 的起源 <https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html> 摘录：“MCP (Model Context Protocol) Security Cheat Sheet¶ Introduction¶ The Model Context Protocol (MCP), introduced by Anthropic in November 2024, standardizes how AI applications (LLM clients) connect to external tools, data sources, and services. Think of it as a universal interface layer, a USB-C port for AI , replacing fragmented, custom integratio…”
[14] Python 订阅部署说明 <https://py.sdk.modelcontextprotocol.io/run/deploy/> 摘录：“Deploy & scale Your server works. Now it needs a real hostname, and more than one worker behind it. Almost none of that is MCP's business. You bring the ASGI server, the process manager, the load balancer. What this page has is the short list of things that are MCP's business: one setting that gates every deployment, and the two places where more…”

### 反向代理配置与超时关系

**先保证不缓冲响应。**SSE 事件需要及时 flush。服务端按规范设置 `X-Accel-Buffering: no`，nginx 对 MCP 路径关闭响应缓冲和缓存。不要把响应头误写成只有发给上游的请求头。[3]

下面是 nginx 配置骨架。证书路径、域名与代理超时属于部署配置。

```nginx
upstream mcp_backend {
    server 127.0.0.1:8000;
    keepalive 32;
}

server {
    listen 443 ssl;
    server_name mcp.example.com;

    ssl_certificate     /etc/letsencrypt/live/mcp.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/mcp.example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;

    location = /mcp {
        proxy_pass http://mcp_backend;
        proxy_http_version 1.1;
        proxy_set_header Connection "";

        proxy_set_header Host $host;
        proxy_set_header Authorization $http_authorization;
        proxy_set_header Accept $http_accept;
        proxy_set_header MCP-Protocol-Version $http_mcp_protocol_version;
        proxy_set_header Mcp-Method $http_mcp_method;
        proxy_set_header Mcp-Name $http_mcp_name;

        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_buffering off;
        proxy_cache off;
        client_max_body_size 4m;

        proxy_read_timeout 3600s;

        # 本方案关闭代理对上游调用的透明重试。
        # 由了解工具幂等性的客户端或应用层决定重试。
        proxy_next_upstream off;
    }
}
```

**示例值不是统一 SLO。**`keepalive 32` 来自代理配置示例，`proxy_read_timeout 3600s` 来自 SSE 部署示例。TLS 1.2 以上与证书链验证属于安全配置建议。[31][32][33]

**其他 MCP 头仍应透传。**上述显式头有助于检查配置，但 `Mcp-Param-*` 等扩展头也必须保留。不能在网关采用固定白名单后，只放行表中三个标准 MCP 头。

**心跳与总期限必须分开。**idle timeout 关注相邻数据间隔；工具 deadline 关注整个执行时长。SSE 心跳可以维持连接，但不能让一个超出业务期限的工具无限执行。

设心跳周期为 \(H\)，链路中最小 idle timeout 为 \(I_{\min}\)，网络与调度裕量为 \(J\)，应满足：

$$H+J<I_{\min}$$

**保活流量可以估算。**按 15 秒一次心跳计算，每条安静流每小时发送 `3,600÷15＝240` 次心跳。若采用 `:\r\n\r\n` 的 5 字节注释帧，纯 SSE payload 为 `240×5＝1,200 字节/流·小时`；实际还包括网络封装。

**连接池不减少活跃流数量。**nginx 的 `keepalive 32` 是空闲上游连接缓存，不是 32 条 HTTP/1.1 连接可以同时承载任意数量长期 SSE。使用 HTTP/2 时，也应区分 TCP 连接数与并发 HTTP stream 数。

**平台必须支持真实流式。**现代无协议会话有利于 serverless，但 `subscriptions/listen` 仍是长期响应。若网关缓冲输出、函数限制响应时长，或适配器不传播 disconnect，协议无状态本身不能消除这些运行时约束。

本节参考文献：
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport from protocol version 2024-11-05. Revision 2026-07-28 changed the behavior of Streamable HTTP. Clients must ensure they handle backwards compatibility correctly. Changes included: - Removal of the GET stream endpoint. - Removal of protocol-level sessions. - The server exposes a single HTTP endpoint (the MCP endpoint) that accepts POST. - The client sends every JSON-RPC request or notification as its own HTTP POST. - The server answers each request with either a single JSON object or a Server-Sent Events (SSE) stream scoped to that request, carrying request-related notifications followed by the final response. - Server-to-clien…”
[31] 代理连接池示例 <https://fast.io/resources/mcp-server-proxy/> 摘录：“keepalive 32; listen 443 ssl; server_name mcp.example.com; ssl_certificate /etc/letsencrypt/live/mcp.example.com/fullchain.pem; ssl_certificate_key /etc/letsencrypt/live/mcp.example.com/privkey.pem; location /mcp { proxy_http_version 1.1; proxy_set_header Connection ; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Forwarded-Proto $scheme; proxy_buffering off; proxy_cache off; chunked_transfer_encoding off; proxy_read_timeout 86400s; proxy_send_timeout 86400s; location /sse { proxy_http_version 1.1; proxy_set_header Connection ; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_buffering off; proxy_cache…”
[32] SSE 超时示例 <https://sudoall.com/mcp-streamable-http-sse/> 摘录：“stdio works beautifully for local tools, but the moment you want to share an MCP server across a network – serving multiple clients, deploying to a container, integrating with a third-party host over the internet – you need HTTP transport. The MCP specification defines Streamable HTTP as the canonical remote transport: HTTP POST for client-to-server requests, Server-Sent Events (SSE) for server-to-client streaming. This lesson covers the protocol mechanics, the implementation pattern, and the hard-won lessons about making streaming work reliably in production. The Streamable HTTP Protocol The Streamable HTTP transport uses a single HTTP endpoint (typically /mcp ) and the following request flow: - Client to server: HTTP POST with C…”
[33] TLS 安全清单 <https://github.com/slowmist/MCP-Security-Checklist/blob/main/README_CN.md> 摘录：“本安全检查清单由 @SlowMist_Team 编写并维护。 慢雾科技作为全球领先的区块链生态威胁情报公司，旨在帮助区块链生态与 AI 生态相融合的过程中拥有更加深度的安全防护能力及保护用户拥有更高的隐私性。 感谢 FENZ.AI 倾力相助 FENZ.AI 以未来科技重塑 AI 安全审计。 从 MCP 攻击检测到 AI 忠诚度评估，Fenz 正在构建AI时代的基础设施—— 超级智能，始于超强安全 。 - MCP Server( MCP 插件)安全 - MCP 客户端/MCP HOST 安全 - MCP 在不同 LLM 上的适配和调用安全 - 多 MCP 场景安全 - 加密货币相关 MCP 的特有安全点 - MCP 安全自查工具 随着大模型的迅猛发展，各种新的AI工具也在不断涌现，当下代表性的 MCP（Model Context Protocol）标准实现的工具正逐渐成为连接大语言模型（LLM）与外部工具、数据源之间的关键桥梁。 自 2024 年底发布以来，MCP 已被广泛应用于 Claude Desktop、Cursor 等主流 AI 应用中，MCP Server 的各种商店也在不断出现，展现出强大的生态扩展能力。 然而，MCP 的快速普及也带来了新的安全挑战。 当前 MCP 架构中，系统由 Host（本地运行的 AI 应用环境）、Client（负责与Server通信与工具调用的组件） 以及 Server（MCP 插件所对应的服务端） 三部分构成。 用户通过 Host 与 AI 交互，Client 将用户请求解析并转发至 MCP Server，执行工具调用或资源访问。 在多实例、多组件协同运行的场景下，该架构暴露出一系列安全风险，尤其在涉及加密货币交易或…”

### 多实例部署：哪些状态真正需要共享

**现代请求可任意落副本。**官方 Python 部署矩阵明确：2026-07-28 不设置 `Mcp-Session-Id`，任意 worker 可处理请求。旧有状态连接则通常把 session 放在单 worker 内存，跨 worker 可能收到 404。[14]

| 部署方案 | 路由策略 | 共享组件 | 故障语义 |
|---|---|---|---|
| 现代无协议会话 | round-robin | 业务存储、状态密钥、可选订阅 bus | 在途流取消，业务按句柄恢复 |
| legacy 本地会话 | sticky session | 可选持久事件存储 | worker 丢失需重建会话 |
| legacy 分布式兼容层 | owner 路由或协调层 | 会话索引、EventStore、消息协调 | 取决于状态和执行协调设计 |

**EventStore 不等于完整会话迁移。**它保存并重放 SSE 消息，不会把正在运行的协程、TCP 连接或 transport 对象自动迁到另一机器。将一个 `Map` 换成 Redis，不会自动得到无缝故障转移。官方 TypeScript 扩展文档也把共享事件存储与 affinity、pub/sub 等方案分开讨论。[34]

**多轮状态密钥必须共享。**Python 文档给出四 worker 的具体失败形态：各进程默认生成不同密钥，第二轮请求落到另一 worker 时，`requestState` 无法解封，返回 `-32602`。所有副本应共享至少 32 bytes 的密钥，并使用一致 server name 或显式 audience。[14]

**轮换要保留过渡能力。**如果状态有效期采用 600 秒，旧验证密钥至少应覆盖仍被允许使用的状态窗口。签发用新 key，验证接受当前允许的 key 集合。这里的密钥保留应服从状态过期与吊销策略，而不是无限保留历史 key。

**订阅需要跨进程总线。**Python 的 `SubscriptionBus` 只有 `publish`、`subscribe` 两个方法，可基于 Redis 或 NATS 实现。TypeScript 默认事件总线同样位于进程内，多节点应注入共享 bus。[14][34]

**总线不自动提供重放。**跨副本 pub/sub 解决“事件能否到达持有连接的副本”。现代客户端断流后的恢复，仍应重新订阅并 fetch 当前状态。需要可靠、可审计事件历史的业务，应使用应用事件日志或任务系统。

本节参考文献：
[14] Python 订阅部署说明 <https://py.sdk.modelcontextprotocol.io/run/deploy/> 摘录：“Deploy & scale Your server works. Now it needs a real hostname, and more than one worker behind it. Almost none of that is MCP's business. You bring the ASGI server, the process manager, the load balancer. What this page has is the short list of things that are MCP's business: one setting that gates every deployment, and the two places where more than one worker changes what the SDK does. Before anything else: the Host allowlist streamable_http_app() cannot know which hostname it will be served behind, so it assumes the safest ans…”
[34] 会话与扩展设计 <https://ts.sdk.modelcontextprotocol.io/v2/serving/sessions-state-scaling.html> 摘录：“Sessions, state, and scaling createMcpHandler builds a fresh server instance from your factory for every HTTP request and holds nothing between requests, so a v2 server is stateless and scales horizontally by default — Serve over HTTP is the whole setup. Read on if you run a sessionful 2025-era deployment, need a dropped stream to resume, or push change notifications across nodes. Pin a client to a session A session pins a client to one long-lived transport instance; sessions belong to the hand-wired 2025-era transport — the 2026-…”

### 日志、指标、健康检查和退出

**HTTP 200 不代表调用成功。**流内 JSON-RPC error 仍可能携带在 HTTP 200 上。监控应分别统计 HTTP 状态、协议错误和工具业务失败，否则流式服务的成功率会被高估。

以下是本方案建议的指标名，不是 MCP 强制命名。

| 建议指标 | 类型 | 主要用途 |
|---|---|---|
| `mcp_requests_total` | counter | 按版本、方法、HTTP 状态计数 |
| `mcp_rpc_errors_total` | counter | 统计流内和 JSON 协议错误 |
| `mcp_request_duration_seconds` | histogram | 全程延迟与分位数 |
| `mcp_active_streams` | gauge | 请求流与订阅流占用 |
| `mcp_event_queue_bytes` | gauge | 识别慢客户端积压 |
| `mcp_stream_disconnects_total` | counter | 区分主动取消与异常断流 |
| `mcp_request_state_failures_total` | counter | 篡改、过期、跨副本配置问题 |
| `mcp_legacy_requests_total` | counter | 判断兼容路径使用量 |
| `mcp_idempotency_hits_total` | counter | 观察重试与重复操作 |

**追踪应串起逻辑操作。**2026-07-28 为 `_meta` 记录了 `traceparent`、`tracestate` 和 `baggage`。MRTR 各轮、网络重试和后台任务可通过逻辑操作 ID 关联，同时保留每次 POST 的独立请求 ID。[13]

**敏感字段不要成为标签。**principal、对象句柄和请求 ID 适合受控日志或 trace 属性，不宜直接放入高基数指标。Authorization、refresh token、完整 `requestState` 和敏感工具参数应脱敏。网关可见的 `Mcp-Param-*` 也不能包含密码、API key 或个人敏感信息。[35]

**健康检查与 MCP 路由分开。**Python SDK 不是应用服务器，不提供 workers、TLS、生产超时和完整健康体系。自定义 `/health` 可作为 liveness，但官方文档提醒该路由不会自动继承 MCP 认证，因此只能暴露最少健康信息。[14]

**退出时先排空再关闭。**建议先撤下 readiness，停止接收新调用，再等待在途请求达到排空期限。到期取消剩余请求并关闭订阅，最后释放连接池。AWS 的参考架构使用 ALB 健康检查、ECS 替换和连接排空，说明这些职责应交给应用服务器与编排层协同完成。[36]

**本节判断。**无协议会话简化的是请求路由，不是授权、持久化或长连接运维。生产可扩展性来自明确划分这几类状态，而不是统一设置一个“stateless”开关。

本节参考文献：
[13] 发现与按请求协商 <https://modelcontextprotocol.io/specification/2026-07-28/changelog> 摘录：“Major changes Remove protocol-level sessions and the Mcp-Session-Id header from the Streamable HTTP transport. List endpoints (tools/list ,resources/list ,prompts/list ) no longer vary per-connection. Servers that need cross-call state use explicit, server-minted handles passed as ordinary tool arguments (SEP-2567). Make…”
[35] 头字段信息泄露风险 <https://modelcontextprotocol.io/seps/2243-http-standardization> 摘录：“FinalStandards Track This SEP has reached Final status and is preserved as a historical record of the design as accepted. Changes made to the protocol after finalization are not reflected here. Refer to the current specification and its changelog for authoritative requirements. This SEP proposes exposing critical routing…”
[14] Python 订阅部署说明 <https://py.sdk.modelcontextprotocol.io/run/deploy/> 摘录：“Deploy & scale Your server works. Now it needs a real hostname, and more than one worker behind it. Almost none of that is MCP's business. You bring the ASGI server, the process manager, the load balancer. What this page has is the short list of things that are MCP's business: one setting that gates every deployment, and…”
[36] AWS 部署参考 <https://docs.aws.amazon.com/solutions/deploying-model-context-protocol-servers-on-aws/> 摘录：“Let's make it happen Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs. This Guidance demonstrates how to securely run Model Context Protocol (MCP) servers on the AWS Cloud using containerized architecture. It helps organizations implement…”

## 六、从旧 HTTP/SSE 迁移到现代实现

本节参考文献：
[13] 发现与按请求协商 <https://modelcontextprotocol.io/specification/2026-07-28/changelog> 摘录：“header from the Streamable HTTP transpo…”
[35] 头字段信息泄露风险 <https://modelcontextprotocol.io/seps/2243-http-standardization> 摘录：“This SEP proposes exposing critical rou…”
[14] Python 订阅部署说明 <https://py.sdk.modelcontextprotocol.io/run/deploy/> 摘录：“streamable_http_app() cannot know which…”
[36] AWS 部署参考 <https://docs.aws.amazon.com/solutions/deploying-model-context-protocol-servers-on-aws/> 摘录：“CloudFront provides HTTPS encryption in…”

### 迁移不是简单改 URL

**第一轮变化发生在 2025 年。**2025-03-26 引入 Streamable HTTP，取代 2024-11-05 的双端点 HTTP+SSE。2026-07-28 则继续移除握手、协议会话、独立 GET 和事件恢复。两次迁移改变的层次不同。[3]

旧 HTTP+SSE 的典型顺序是：

```text
GET /sse
  → 打开 SSE
  → 收到 endpoint event，得到消息提交地址

POST /messages?sessionId=...
  → 提交 JSON-RPC
  → 响应与通知从原 SSE 返回
```

2025-era Streamable HTTP 的有状态顺序则是：

```text
POST /mcp initialize
  → 初始化结果，可能包含 Mcp-Session-Id

POST /mcp notifications/initialized
  → 202，无 body

GET /mcp，携带 session ID
  → 独立 SSE back-channel

POST /mcp tools/call
  → JSON 或请求级 SSE

GET /mcp，携带 Last-Event-ID
  → 按可用 EventStore 重放

DELETE /mcp，携带 session ID
  → 终止旧会话
```

官方 v1.x 兼容示例同时实现了这两条历史路径。[37]

**旧无状态不等于现代协议。**2025-era 服务即使把 `sessionIdGenerator` 设为 `undefined`，仍可能使用 initialize 和旧结果格式。现代服务则使用每请求 `_meta`、MRTR 和新订阅语义。迁移测试需要检查消息内容，不只检查有没有 session header。

本节参考文献：
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport from protocol version 2024-11-05. Revision 2026-07-28 changed the behavior of Streamable HTTP. Clients must ensure they handle backwards compatibility correctly. Changes included: - Removal of the GET stream endpoint. - Removal of protocol-level sessions. - The server exposes a single HTT…”
[37] 旧新传输兼容示例 <https://github.com/modelcontextprotocol/typescript-sdk/blob/v1.x/src/examples/server/sseAndStreamableHttpCompatibleServer.ts> 摘录：“Repository navigation Expand file tree Copy pathsseAndStreamableHttpCompatibleServer.ts More file actions 293 lines (268 loc) · 11.1 KB Copy pathsseAndStreamableHttpCompatibleServer.ts File metadata and controls 293 lines (268 loc) · 11.1 KB import { Request, Response } from 'express'; import { randomUUID } from 'node:crypto'; import { McpServer } from '../../server/mcp.js'; import { Streamab…”

### 双时代分流与降级规则

**已有有状态服务宜保留原路。**TypeScript 提供 `isLegacyRequest`，可将没有现代 envelope 声明的流量送到旧 handler，再把现代流量交给 `legacy: "reject"` 的新入口。格式错误的现代声明仍由现代路径拒绝，不能借此滑入旧处理器。[4]

| 现有实现 | 推荐迁移方式 | 保留内容 | 主要改动 |
|---|---|---|---|
| TypeScript v1 无状态 HTTP | 映射到 v2 factory | 业务工具逻辑 | 包入口与 handler |
| TypeScript v1 有状态 HTTP | 前置双时代分流 | session manager、EventStore | 新增现代路径 |
| Python v1 | 升级 v2 双时代服务器 | 旧客户端服务能力 | 类名、参数、客户端 API |
| 2024 HTTP+SSE | 新增 `/mcp` 并行服务 | `/sse`、`/messages` | 客户端入口与传输 |

**降级先看响应体。**现代服务器也可能返回 400、404。若 body 是可识别的现代 JSON-RPC error，应修正请求、选择支持版本或处理方法错误。不能看到 4xx 就统一切回 SSE。[3]

**旧 HTTP+SSE 探测有明确条件。**客户端先 POST 到用户提供的 URL。只有收到 400、404 或 405，且 body 不属于可识别现代错误，才进一步 GET 并等待首个 `endpoint` event。认证失败、5xx 和网络超时都不能充当协议时代证据。

**网关也要防错误降级。**旧协议未必提供现代头体校验保证。如果网关按 `Mcp-Param-Tenant` 做租户策略，就必须确认请求使用要求校验的版本。不能把未校验的旧客户端镜像头当成可信授权依据。[3]

本节参考文献：
[4] TypeScript 版本迁移 <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> 摘录：“(Typings published before 2.0.0-alpha.4 predate this exclusion: there the typed maps still carry the tasks/ entries and the CreateTaskResult the isCallToolResult guard if you are pinned to one of those alphas. 2.0.0-alpha.4 and later include the exclusion.) Where task interop is genuinely required, use the explicit-schema custom-method form on both sides: request({ method: 'tasks/get', params }, result…”
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“Streamable HTTP was introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport from protocol version 2024-11-05. Revision 2026-07-28 changed the behavior of Streamable HTTP. Clients must ensure they handle backwards compatibility correctly. Changes included: - Removal of the GET stream endpoint. - Removal of protocol-level sessions. - The server exposes a single HTTP endpoint…”

### 可执行的迁移步骤

**建议采用渐进切换。**以下是工程运行步骤，兼容路由由官方 SDK 支持；观察与回滚窗口参考迁移运行手册。[38]

1. 盘点 `/sse`、`/messages` 和现有 `/mcp` 的调用方、版本及流量。
2. 保留旧路径，新增现代 handler，并用发布开关控制入口。
3. 将隐式会话业务状态改为显式句柄，补齐 owner、TTL 和幂等记录。
4. 先迁移受控客户端，固定已通过测试的 SDK 与宿主版本。
5. 按协议时代观察 400、405、406、认证错误、断流和重复操作。
6. 对旧路由至少观察两周，或采用一个业务计费周期的窗口。
7. 旧流量归零、在途会话排空且目标客户端通过后，再下线旧路径。

**配置变更要同步完成。**Claude Code 使用 `--transport http` 与 `/mcp`；旧配置回退时仍使用对应 SSE 类型和地址。Python 更新三元组返回值及运行参数，TypeScript 更新 server/client 包入口。Desktop 的远程连接使用 Connectors UI。[38][11]

本节参考文献：
[38] 迁移运行手册 <https://startdebugging.net/2026/07/migrate-an-mcp-server-from-sse-to-streamable-http/> 摘录：“, you are running the 2024-11-05 HTTP+SSE transport, which the Model Context Protocol deprecated in the 2025-03-26 revision and replaced with Streamable HTTP. For a single-process server the migration is a half-day job: your tool, resource…”
[11] Python v2 迁移 <https://github.com/modelcontextprotocol/python-sdk/blob/e8e64842/docs/migration.md> 摘录：“This guide covers the breaking changes introduced in v2 of the MCP Python SDK and how to update your code. Version 2 of the MCP Python SDK introduces several breaking changes to improve the API, align with the MCP specification, and provid…”

### 会话、在途任务与回滚

**能否迁移取决于耐久锚点。**已经有持久化业务句柄、任务 ID 或可验证 continuation 的状态，可以由现代请求继续引用。只存在于旧 transport 内存的对象，则应采用排空、重新发起或应用自定义转换，不能仅把 session ID 换个字段名。

| 既有状态 | 推荐处理 | 切换后的身份 | 风险控制 |
|---|---|---|---|
| 持久化业务对象 | 保留对象并返回句柄 | principal＋handle | 重新授权 |
| 持久化后台任务 | 保留任务和结果 | principal＋job ID | 防重复提交 |
| 仅内存的空闲 session | 排空或重新建立 | 新请求上下文 | 清理旧资源 |
| 正在执行的直接调用 | 等待完成或明确中断 | 新请求或业务操作键 | 避免重复副作用 |

**回滚需要保留业务格式兼容。**旧端点保留期间，可恢复客户端旧 URL 和类型，或切回上一版本镜像。若数据库 schema、句柄格式或任务记录已被新版本单向改写，仅回滚 HTTP 路由不够，因此业务存储应在兼容窗口内支持前后版本读取。

**在途请求不要强行“搬家”。**SSE 连接与处理协程属于运行中的执行上下文。更稳妥的切换是停止给旧路径分配新工作，让其完成或到期取消。可靠长任务应先移到独立任务系统，再切换传输。

**回滚范围需要事先验证。**应验证旧地址仍可握手、旧结果格式仍能解析，以及新版本写入的业务记录可由旧版本读取。运行手册给出的回滚动作是恢复旧 URL/type，或重新部署标记的上一版本；这不是协议定义的在线会话转换机制。[38]

**本节判断。**最安全的迁移单位是“协议入口＋客户端版本＋业务状态格式”，不是单个 URL。先解除业务对 transport session 的依赖，后续版本升级才会显著变轻。

本节参考文献：
[38] 迁移运行手册 <https://startdebugging.net/2026/07/migrate-an-mcp-server-from-sse-to-streamable-http/> 摘录：“Migrate an MCP Server from SSE to Streamable HTTP (2026 Checklist) The legacy HTTP+SSE transport used two endpoints and a sticky connection. Streamable HTTP uses one. Here is the step-by-step migration for the TypeScript and Python SDKs, the client configs you have to repoint, and the proxy buffering gotcha that makes the new endpoint look broken. If your MCP server still answers on GET /sse and takes messages on POST /messages? sessionId=... , you are running the 2024-11-05 HTTP+SSE transport, which the Model Context Protocol deprecated in the 2025-03-26 revision and replaced with Streamable HTTP. For a single-process server the migration is a half-day job: your tool, resource, and prompt handlers do not change at all. What changes is the endpoint shape (two endpoints collapse into one…”

## 七、如何验证正确性、性能和生产可用性

本节参考文献：
[38] 迁移运行手册 <https://startdebugging.net/2026/07/migrate-an-mcp-server-from-sse-to-streamable-http/> 摘录：“Migrate an MCP Server from SSE to Strea…”

### 官方示例能证明哪些行为

**先用官方样例建立对照。**Python 的 `simple-streamablehttp`、TypeScript 的 stateful/stateless 示例和 Anthropic Express scaffold，可以作为基础接入与旧路径对照。Inspector 适合交互调试和 CI smoke test。[39][6][12]

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:8000/mcp \
  --transport http --method tools/list
```

**样例必须标注协议时代。**带 GET、DELETE、`InMemoryEventStore` 的示例主要用于旧兼容语义。现代验收应明确使用 2026-07-28，检查无 initialize、无 session ID、头体一致性和断流取消。

**交互测试比单元测试更接近接入。**Python interaction suite 在测试内声明服务器，由真实高层 Client 驱动，并按 transport 与规范版本矩阵运行。其 MRTR、并行隔离、版本协商和状态校验场景，适合转化为项目回归资产。[40]

**测试通过不等于完整合规。**同一 PR 明确区分规范要求、已记录差异和延期条目。其汇总表列出 54 个已记录差异；部分历史审查涉及自定义头、低层能力门禁和 audience 行为。因此应检查测试断言是否要求合规，而不是只固定现状。

**上游场景也应按日期理解。**2026-07-01 的实现记录已经报告 header validation、custom header validation 和 server-stateless 场景通过；server-sessionless 的上游场景当时依赖 conformance suite 更新。项目验收应直接执行目标语义，不把某个历史状态标签替代为当前发布保证。[16]

本节参考文献：
[39] Python 示例 <https://github.com/modelcontextprotocol/python-sdk/tree/main/examples/servers/simple-streamablehttp> 摘录：“A simple MCP server example demonstrating the StreamableHttp transport, which enables HTTP-based communication with MCP servers using streaming. - Uses the StreamableH…”
[6] TypeScript 官方仓库 <https://github.com/modelcontextprotocol/typescript-sdk> 摘录：“This is the main branch: v2 of the SDK (@modelcontextprotocol/server , @modelcontextprotocol/client ), the stable release line, implementing the 2026-07-28 MCP spec. S…”
[12] Anthropic HTTP 示例 <https://github.com/anthropics/claude-plugins-official/blob/main/plugins/mcp-server-dev/skills/build-mcp-server/references/remote-http-scaffold.md> 摘录：“Minimal working servers in both recommended frameworks. Start here, then add tools. npm install @modelcontextprotocol/sdk zod express npm install -D typescript @types/…”
[40] 官方 interaction suite <https://github.com/modelcontextprotocol/python-sdk/pull/3018> 摘录：“from the 2025-11-25 baseline to the 2026-07-28 spec revision: ~109 new test functions across 40 test files, manifest groundwork (requirement id renames, era added_in l…”
[16] Python 双时代入口 <https://github.com/modelcontextprotocol/python-sdk/issues/2893> 摘录：“You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts…”

### 协议与网关测试矩阵

**通过标准是执行前拒绝。**格式、镜像头、认证或大小校验失败后，工具 handler 不得产生副作用。测试不仅检查状态码，也应检查 handler 调用次数和下游写入记录。

| 测试输入 | 预期结果 | 必须断言的行为 |
|---|---|---|
| 缺少或错配标准头 | 400、`-32020` | 工具未执行 |
| 不支持协议版本 | 400、版本错误 | 返回支持版本 |
| 未声明所需输入能力 | 400 或已提交流内错误 | 不越过能力门禁 |
| 未知 RPC 方法 | 404、`-32601` | 不误入 legacy |
| 现代 GET、DELETE | 405 | 不创建会话 |
| Accept 缺少任一必需类型 | 406 | 不开始工具执行 |
| 非 JSON Content-Type | 415 | 按媒体类型判断 |
| 无效 JSON 或消息数组 | 拒绝请求 | 不按批量消息执行 |
| 被接受的 notification | 202、空 body | 不伪装工具结果 |
| body 为 4 MiB＋1 字节 | 413 | 解析前后均无副作用 |

4 MiB 等于 4,194,304 字节，因此大小边界用例是 4,194,305 字节。现代媒体类型与错误门槛来自规范、稳定发布说明和传输测试。[3][8][9]

**媒体类型要测解析边界。**`application/json; charset=utf-8` 应按 JSON 处理，不能采用字符串完全相等判断。反过来，`text/plain; a=application/json` 不能因包含 JSON 字样就放行。TypeScript 发布说明正是针对这类问题进行了修正。

**header 上限由链路最小值决定。**协议不统一规定 header 总大小。SEP 举出的基础设施范围从部分服务器的 4–8 KB，到某些边缘平台的 128 KB。客户端必须处理 413 和 431；部署应记录实际网关上限。[35]

$$H_{\text{effective}}=\min(H_{\text{edge}},H_{\text{ingress}},H_{\text{server}})$$

**自定义头要测完整转换。**`x-mcp-header` 只允许静态可达的 string、integer、boolean 参数，不能标记 number、数组或任意动态路径。非 ASCII、控制字符、首尾空白和哨兵冲突值需要规范编码；服务器解码后再与 body 比对。[3]

**大头不能靠静默省略解决。**若网关依赖某个已声明参数头，客户端省略它会破坏路由和校验。应减少不必要的注解、缩短路由参数或调整明确的基础设施预算，而不是跳过必需字段。

本节参考文献：
[3] Streamable HTTP 规范 <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> 摘录：“SGVsbG8sIOS4lueVjA==? Original Value: padded Reason: Leading/trailing spaces Encoded Header Value: Mcp-Param-Text: =? IHBhZGRlZCA=? Original Value: line1\nline2 Reason: Contains newline Encoded Header Value: Mcp-Param-Text: =? bGluZTEKbGluZTI=? Original Value: =? = Reason: Matches sentin…”
[8] Python v2.0.0 <https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0> 摘录：“Repository navigation MCP Python SDK v2 Stable Release This is v2.0.0, the stable v2 release of the MCP Python SDK. It supports the 2026-07-28 revision of the Model Context Protocol and serves every earlier revision from the same server. pip install mcp now installs 2.x. pip install mcp…”
[9] TypeScript server v2.0.0 <https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/@modelcontextprotocol/server@2.0.0> 摘录：“handshake against it — a hard connect failure against a modern-only server such as go-sdk v1.7.0-pre.3), and the server rejected conforming clients that omitclientInfo - The 2026 wire schemas are the final revision exactly: no body onDiscoverResult , envelopeclientInfo optional (a presen…”
[35] 头字段信息泄露风险 <https://modelcontextprotocol.io/seps/2243-http-standardization> 摘录：“FinalStandards Track This SEP has reached Final status and is preserved as a historical record of the design as accepted. Changes made to the protocol after finalization are not reflected here. Refer to the current specification and its changelog for authoritative requirements. This SEP…”

### 安全和身份测试矩阵

**安全测试必须穿过真实网络边界。**Python 进程内传输 fixture 关闭了 DNS rebinding 模拟，不能覆盖真实 Host、Origin 和代理行为。应使用实际监听端口、反向代理和浏览器预检夹具。[15]

| 场景 | 预期结果 | 通过标准 |
|---|---|---|
| 无 token 访问受保护 RPC | 401 与认证 challenge | 不进入业务处理 |
| token audience 错误或缺失 | 401 `invalid_token` | 不向下游透传 |
| 合法用户访问他人 handle | 拒绝访问 | owner 绑定有效 |
| `requestState` 篡改或过期 | 状态验证失败 | 不恢复处理上下文 |
| 非法 Origin | 403 | 工具未执行 |
| 非法 Host | 部署策略拒绝；Python 可为 421 | 不绕过本地防护 |
| 凭据式浏览器跨域 | 仅允许具体来源 | 无通配凭据授权 |
| OAuth 发现指向私网 | 阻止访问 | 不产生内部请求 |
| 回调 `iss`、state 或 URI 错配 | 授权流程失败 | 不兑换错误授权码 |
| 头体目标或租户不一致 | 400、`-32020` | 不发生跨租户执行 |

**错误消息要保持不透明。**内部异常应在服务端记录详细堆栈，客户端获得稳定、受控的错误。Python 一致性改动将未处理异常映射为 `-32603` 与不透明内部错误消息，避免直接泄露后端细节。[29]

**作用域不足不等于网络错误。**如果服务器要求 step-up，应走明确的再授权流程。普通 403 不应触发无限刷新，也不能降级到一个安全门槛更低的传输入口。

本节参考文献：
[15] 官方传输测试 <https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/shared/test_streamable_http.py> 摘录：“Repository navigation Expand file tree Copy pathtest_streamable_http.py More file actions 2361 lines (1992 loc) · 96.8 KB Copy pathtest_streamable_http.py File metadata and controls 2361 lines (1992 loc) · 96.8 KB Tests for the StreamableHTTP server and client transport. Contains tests for both server and client sides of the StreamableHTTP transport, driven entirely in pro…”
[29] Python audience 门禁 <https://github.com/modelcontextprotocol/python-sdk/pull/2999> 摘录：“2 issues found across 29 files Prompt for AI agents (unresolved issues) Check if these issues are valid — if so, understand the root cause of each and fix them. If appropriate, use sub-agents to investigate and fix each issue separately. file name= src/mcp/shared/auth_utils.py violation number= 1 location= src/mcp/shared/auth_utils.py:32 P2: Audience canonicalization can t…”

### 断流、并发与跨副本行为测试

**恢复测试要覆盖提交边界。**只测“断线后能再次连接”不够。真正危险的是业务已经提交、客户端却没有收到最终结果。验收应直接检查副作用只发生一次。

| 场景 | 预期行为 | 验收重点 |
|---|---|---|
| 工具 SSE 中途断开 | 当前请求取消 | 后端停止继续发消息 |
| 一次调用取消，另一次仍运行 | 相互隔离 | 不关闭整个客户端 |
| 提交后、结果前断流 | 查询或幂等重试 | 外部操作不重复 |
| MRTR 第二轮换 worker | 验证并继续 | 共享密钥与 audience 一致 |
| 并行 MRTR 调用 | 各自匹配状态 | 不串输入和结果 |
| MRTR 超出 10 轮配置 | 明确终止 | 不形成无限循环 |
| listen 断开后重建 | 重新订阅与 fetch | 不假设事件重放 |
| 多副本发布资源变化 | 订阅副本收到通知 | 共享 bus 生效 |
| legacy session 失效 | 重建旧握手 | 不持续携带失效 ID |
| 进程滚动退出 | 排空或明确取消 | 无孤儿请求与许可泄漏 |

**代理测试要观察事件到达时间。**上游写出时间、代理出口时间和客户端收到时间应可关联。若所有进度直到最终结果才一次到达，即使最后结果正确，也属于流式部署失败。

**慢客户端要有稳定内存。**主动降低读取速度，观察队列是否触及设定上限。达到上限后必须触发背压、合并允许合并的进度，或按策略终止连接。不能让工具数量不变而内存持续增长。

**缓存测试关系到数据隔离。**列表和读取结果的 `ttlMs`、`cacheScope` 应与真实内容匹配。用户私有内容必须按身份分区，不得因结果声明 public 而跨用户复用。工具目录还应采用稳定排序，减少无意义缓存变化。[13]

**重启后要重新发现。**Claude Code `2.0.75` 的历史问题记录曾报告服务器重启后工具丢失，并被归为重复问题。它适合作为“服务器重启、工具重新发现和宿主恢复”的回归场景，而不是协议层必然行为。[41]

本节参考文献：
[13] 发现与按请求协商 <https://modelcontextprotocol.io/specification/2026-07-28/changelog> 摘录：“Major changes Remove protocol-level sessions and the Mcp-Session-Id header from the Streamable HTTP transport. List endpoints (tools/list ,resources/list ,prompts/list ) no longer vary per-connection. Servers that need cross-call state use explicit, server-minted handles passed as ordinary tool arguments (SEP-2567). Make MCP stateless: remove the /notifications/initialized Every request now carries its protocol version and client capabilit…”
[41] 服务器重启案例 <https://github.com/anthropics/claude-code/issues/15094> 摘录：“Repository navigation Bug MCP server restart with HTTP streaming terminates Claude Code session 15094 Closed as duplicate Closed as duplicate duplicateThis issue or pull request already existsThis issue or pull request already exists Bug Description In the latest version of Claude Code, I have noticed a significant pattern. If a Claude Code session is attached to an MCP server that is running HTTP streaming, and that HTTP MCP server restar…”

### 性能数字如何用于判断

**现有比较支持方向判断。**JSJSON 指南对旧 SSE 与 2025-era Streamable HTTP 自述进行了同硬件比较。以下保持其约值，并按端点重新计算变化幅度。[42]

| 指标 | 旧 SSE 报告值 | Streamable HTTP 报告值 | 按约值计算 |
|---|---|---|---|
| 初始化握手延迟 | 约 120 毫秒 | 约 45 毫秒 | 减少约 62.5% |
| 消息往返 P95 | 约 80 毫秒 | 约 35 毫秒 | 减少约 56.25% |
| 单实例并发连接 | 约 500 条 | 约 5,000 条 | 约 10 倍 |
| 1,000 连接内存 | 约 180 MB | 约 25 MB | 减少约 86.1% |

**冷启动属于另一项指标。**同一指南给出 Streamable HTTP serverless 冷启动小于 50 毫秒的报告值。它描述该指南中的部署情形，不等于任意 Python、Node 或边缘运行时的启动上限。

**不能归因为 SSE 本身更慢。**旧 SSE 也可以使用异步实现，不要求每连接独占线程。减少常驻空闲连接、握手与协议会话管理，才是可能降低资源占用的机制。工具本身的执行时长和输出大小仍可能主导端到端延迟。

**容量应按活跃请求建模。**设普通 JSON 请求速率为 \(\lambda_j\)、平均时长为 \(W_j\)，流式请求速率为 \(\lambda_s\)、平均占用时间为 \(W_s\)，长期订阅数为 \(N_l\)，则稳定条件下：

$$C_{\text{active}}\approx\lambda_jW_j+\lambda_sW_s+N_l$$

**这个公式解释了部署差异。**JSON 短调用完成后释放请求资源；请求级 SSE 持续占用到工具完成；listen 流在安静时也占用连接与运行时资源。因此不能用同一个“每秒请求数”概括三种负载。

**内存预算要包含队列。**设基础进程内存为 \(M_0\)，每活跃流的固定状态为 \(M_s\)，每流队列预算为 \(B_q\)，共享缓存预算为 \(M_c\)，则规划上界可写为：

$$M_{\text{budget}}\geq M_0+C_{\text{active}}(M_s+B_q)+M_c$$

**事件积压可预测失控方向。**若事件生产速率为 \(r_p\)，消费速率为 \(r_c\)，在生产快于消费时，积压约按下式增长。持续正增长必须通过背压或终止策略打断。

$$\Delta Q(t)\approx\max(0,r_p-r_c)\times t$$

**带宽主要由业务输出决定。**设平均事件大小为 \(E\)，发送速率为 \(r\)，同时活跃流为 \(C\)，则纯业务 payload 带宽近似为 \(CrE\)。大量工具结果或高频进度，比心跳更容易成为出口带宽瓶颈。

**压测结果应绑定工作负载。**容量报告至少记录硬件、CPU/内存限制、运行时、SDK tag、工具耗时、输出大小、JSON/SSE 比例、订阅数量、样本量和重复次数。结果同时给出吞吐、P50/P95、活跃流、队列字节、RSS、事件循环延迟与取消清理耗时。

**验收门槛应围绕不变量。**在目标负载持续运行时，队列不越界，内存不单调增长，取消不留下任务，错误率不超过业务 SLO。超过准入预算时返回受控过载结果，优于继续接受并最终耗尽进程资源。

本节参考文献：
[42] 第三方性能比较 <https://www.jsjson.com/blog/blog-mcp-streamable-http-guide> 摘录：“2025 年 3 月，MCP（Model Context Protocol）规范发布了 2025-03-26 版本，其中一个最重要的变更是引入了 Streamable HTTP 传输层，正式取代了此前基于 SSE（Server-Sent Events）的 HTTP 传输方案。 这一变更彻底改变了 MCP Server 的部署架构——从需要维护长连接的有状态服务，演进为可水平扩展的无状态 HTTP 服务。 如果你正在构建或维护 MCP Server，理解 Streamable HTTP 不是可选项，而是必修课。 🔌 一、为什么 MCP 要从 SSE 迁移到 Streamable HTTP 1.1 旧版 SSE 传输的核心痛点 在 2024-11-05 版本的 MCP 规范中，HTTP 传输层基于两个独立的端点： POST /messages — 客户端向服务端发送 JSON-RPC 请求GET /sse — 客户端通过 SSE 长连接接收服务端的响应和通知 这种设计存在三个致命问题： 连接管理复杂 SSE 是长连接，需要心跳保活、断线重连 运维成本高，反向代理配置困难 无法水平扩展 Session 绑定在特定服务端实例的 SSE 连接上 部署在多实例/Serverless 环境时请求路由失败 浏览器兼容性差 EventSource API 不支持自定义 Headers 无法传递 Authorization 等认证头 ⚠️ 警告： SSE 传输在生产环境中最常遇到的问题是——Nginx/Cloudflare 等反向代理默认会缓冲 SSE 响应，导致客户端收不到实时消息。 proxy_buffering off 和X-Accel-Buffering: no 1.2 Streamable HTTP 的设计哲学 Streamable HTTP 的核心思想是：用标准 HTTP POST 完成所有通信，响应可以是普通 JSON 也可以是 SSE 流。 客户端 → 服务端：始终使用 POST /mcp 端点发送 JSON-RPC 消息 服务端 → 客户端：响应 Content-Type 可以是 application/json （单条响应）或 text/event-stream （流式响应），由服务端按需决定 这种设计带来了几个关键优势： - ✅ 无状态可扩展 — 每个请求都是独立的 HTTP 请求，天然支持负载均衡 - ✅ 标准 HTTP 认证 — 直接使用 Authorization 头，兼容 OAuth 2.1 - ✅ Serverless 友好 — 无需维持长连接，完美适配 Cloudflare Workers / AWS Lambda - ✅ 浏览器原生支持 — 使用 API，无需EventSource 特性 stdio SSE (旧版 HTTP) Streamable HTTP --- --- --- --- 连接方式 标准输入/输出 SSE 长连接 + POST 标准 HTTP POST 服务端状态 有状态 有状态 无状态（可选有状态） 水平扩展 ❌ 不支持 ❌ 困难 ✅ 原生支持 Serverless 部署 ❌ 不支持 ❌ 困难 ✅ 完美支持 浏览器直连 ❌ 不支持 ⚠️ 受限 ✅ 完整支持 认证方式 进程权限 URL 参数/自定义 标准 HTTP Headers 适用场景 本地 CLI 工具 内部服务 生产级 API 服务 ⚡ 关键结论： 如果你的 MCP Se…”

### 最终工程选型

**不同工作负载采用不同响应。**现代协议支持 JSON、请求级 SSE 和长期订阅，并不要求所有工具都开长连接。应按交互需求选择最简单的资源模型。

| 需求 | 推荐方案 | 主要收益 | 必须补齐 |
|---|---|---|---|
| 快速查询、普通 API 包装 | 现代 POST＋JSON | 简化连接管理 | 授权、限流、结果上限 |
| 工具执行需要进度 | 现代 POST＋请求级 SSE | 独立进度与取消 | 背压、断连传播 |
| 工具或资源变化通知 | `subscriptions/listen` | 显式长期订阅 | 共享 bus、重订阅后读取 |
| 结果必须耐久可查询 | 应用任务与显式句柄 | 不依赖在途流 | 幂等、持久化、owner |
| 旧客户端或旧反向通道 | 隔离 legacy handler | 保持兼容能力 | session 生命周期、回滚 |

**可靠性应上移一层。**若业务硬性要求断线后继续取得结果，优先将结果变成可查询业务对象。若还必须保留旧 SSE 重放，则在兼容层使用持久 EventStore，并明确其历史窗口和会话恢复条件。两者解决的问题不同。

**证据口径集中说明。**本文规范时间截止于 2026-09-13，SDK 以所列稳定 tag 作为实现基线；滚动文档中的运行参数仅作为标明的配置参考。客户端案例按具体版本和环境解释，第三方性能项保留其约值及比较对象；公式计算、配置建议和伪代码均不作为已执行的容量或合规测试结果。

**最终判断明确。**新建远程 MCP 服务，采用官方 v2 SDK、每请求无协议会话入口和外部业务状态。对旧系统保留受控兼容层。上线成败主要取决于头体校验、按请求授权、取消传播、幂等恢复和跨副本状态一致性，而不是是否成功返回过一次 SSE。

本节参考文献：
[42] 第三方性能比较 <https://www.jsjson.com/blog/blog-mcp-streamable-http-guide> 摘录：“，否则服务端不知道客户端支持什么格式 - ❌ 坑 2：在无状态模式下使用通知 — 无状态模式不支持服务端主动推送， server.notification() 调用会静默失败 - ❌ 坑 3：Nginx 缓冲 SSE — 如前所述，必须配置 proxy_buffering off - ❌ 坑 4：Session ID 传递错误 — Mcp-Session-Id 是小写 HTTP 头，不是 query 参数 - ❌ 坑 5：忽略 DELETE 端点 — 客户端断开时需要调用 清理服务端资源，否则会导致内存泄漏 ⚠️ 警告： 如果你使用的是 @modelcontextprotocol/sdk 的早期版本（ 1.12.0），可能还没有 Streamable HTTP 支持。 你的 MCP Server 需要部署在哪里？ ├─ 本地 CLI 工具 / IDE 插件 │ └─ 使用 stdio 传输 ✅ ├─ 内部服务 / 开发环境 │ └─ Streamable HTTP（无状态模式）✅ ├─ 对外 API 服务 / 生产环境 │ ├─ 需要服务端通知/进度？ │ │ ├─ 是 → Streamable HTTP（有状态 + Redis）✅ │ │ └─ 否 → Streamable HTTP（无状态）✅ │ └─ 需要 Serverless 部署？ │ └─ Streamable HTTP（无状态 + Cloudflare Workers）✅ └─ 浏览器端 MCP Client └─ Streamable HTTP（fetch API）✅ - 新项目直接使用 Streamable HTTP — 不要再使用 SSE 传输，它已被标记为 deprecated - 优先选择无状态模式 — 除非你明确需要服务端推送通知 - 正确配置反向…”

## 参考文献

[1] <https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28> MCP 稳定发布
[2] <https://claude.com/blog/bringing-mcp-2026-07-28-to-claude> Anthropic 产品公告
[3] <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http> Streamable HTTP 规范; 协议版本对照; 发送消息规则; 现代与旧方法边界; 媒体类型协商; 标准请求头; 服务端校验规则; SSE 响应约束; notification 的适用范围; 传输规范; 取消条款; SSE 保活规则; 传输安全条款; SSE 代理要求; 传输演进; 现代错误识别; 镜像头的版…
[4] <https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md> TypeScript 版本迁移; TypeScript MRTR 实现; TypeScript HTTP 入口; 默认兼容行为; requestState 验证机制; 现代客户端流程; 版本协商选项; 自动履行与轮数上限; TypeScript 授权迁移; 双时代路由
[5] <https://blog.modelcontextprotocol.io/posts/2026-07-28/> MCP 发布公告; MCP 发布说明; MRTR 发布说明; 能力弃用政策; 授权硬化说明
[6] <https://github.com/modelcontextprotocol/typescript-sdk> TypeScript 官方仓库; TypeScript 示例仓库
[7] <https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html> MCP 的起源; OWASP 接入要求
[8] <https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0> Python v2.0.0; Python v2.0.0 能力范围; Python body 限制; Python 高层客户端; Python 大小限制
[9] <https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/@modelcontextprotocol/server@2.0.0> TypeScript server v2.0.0; TypeScript 同组发布规则; 最终身份格式修正; 身份字段的信任边界; 请求头空白处理; 能力错误映射; 已提交流的错误语义; 媒体类型修正; TypeScript 媒体类型检查
[10] <https://github.com/anthropics/claude-agent-sdk-typescript/issues/202> Agent SDK 历史环境; Agent SDK Accept 案例
[11] <https://github.com/modelcontextprotocol/python-sdk/blob/e8e64842/docs/migration.md> Python v2 迁移; Python v2 API 迁移; 运行参数迁移; Python transport 迁移; Python API 变更
[12] <https://github.com/anthropics/claude-plugins-official/blob/main/plugins/mcp-server-dev/skills/build-mcp-server/references/remote-http-scaffold.md> Anthropic HTTP 示例; Anthropic Express scaffold; Anthropic 接入说明; Anthropic Inspector 用法
[13] <https://modelcontextprotocol.io/specification/2026-07-28/changelog> 发现与按请求协商; 取消事件续传的变更; 订阅机制变更; 追踪上下文变更; 缓存与排序要求
[14] <https://py.sdk.modelcontextprotocol.io/run/deploy/> Python 订阅部署说明; Python 部署边界; 多副本状态配置; Python Host 与 Origin; 反向代理配置; Python 扩展矩阵; 跨 worker requestState; Python SubscriptionBus; SDK 部署职责
[15] <https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/shared/test_streamable_http.py> 官方传输测试; 官方传输测试边界
[16] <https://github.com/modelcontextprotocol/python-sdk/issues/2893> Python 双时代入口; Python 实现进展
[17] <https://docs.anyscale.com/mcp/scalable-remote-mcp-deployment> ASGI 挂载示例; 运行时并发建议
[18] <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/> 显式状态句柄
[19] <https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices> 状态句柄安全; MCP 安全要求; token passthrough 风险; OAuth 发现 SSRF
[20] <https://py.sdk.modelcontextprotocol.io/api/mcp/server/streamable_http_manager/> session manager 参数
[21] <https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client> 官方客户端教程
[22] <https://ts.sdk.modelcontextprotocol.io/v2/api/%40modelcontextprotocol/client/client/streamableHttp.html> 每请求取消接口; 客户端认证契约; legacy 重连参数; 客户端 state 职责
[23] <https://github.com/anthropics/claude-code/issues/32708> Code 2.1.71
[24] <https://github.com/anthropics/claude-code/issues/73444> Code 2.1.233
[25] <https://github.com/anthropics/claude-code/issues/79491> Desktop 发现案例
[26] <https://sunpeak.ai/blogs/claude-connector-sse-to-streamable-http/> Claude 兼容性报告; Claude 宿主约束
[27] <https://github.com/anthropics/anthropic-sdk-python/issues/1383> Managed Agents 更新
[28] <https://agentcat.com/guides/configuring-mcp-installations-production/> 资源服务器部署说明
[29] <https://github.com/modelcontextprotocol/python-sdk/pull/2999> Python audience 门禁; Python 错误处理
[30] <https://github.com/PrefectHQ/fastmcp/pull/4659> token endpoint 回归案例
[31] <https://fast.io/resources/mcp-server-proxy/> 代理连接池示例
[32] <https://sudoall.com/mcp-streamable-http-sse/> SSE 超时示例
[33] <https://github.com/slowmist/MCP-Security-Checklist/blob/main/README_CN.md> TLS 安全清单
[34] <https://ts.sdk.modelcontextprotocol.io/v2/serving/sessions-state-scaling.html> 会话与扩展设计; TypeScript 共享事件总线
[35] <https://modelcontextprotocol.io/seps/2243-http-standardization> 头字段信息泄露风险; header 大小边界
[36] <https://docs.aws.amazon.com/solutions/deploying-model-context-protocol-servers-on-aws/> AWS 部署参考
[37] <https://github.com/modelcontextprotocol/typescript-sdk/blob/v1.x/src/examples/server/sseAndStreamableHttpCompatibleServer.ts> 旧新传输兼容示例
[38] <https://startdebugging.net/2026/07/migrate-an-mcp-server-from-sse-to-streamable-http/> 迁移运行手册; 客户端迁移配置; 回滚操作
[39] <https://github.com/modelcontextprotocol/python-sdk/tree/main/examples/servers/simple-streamablehttp> Python 示例
[40] <https://github.com/modelcontextprotocol/python-sdk/pull/3018> 官方 interaction suite
[41] <https://github.com/anthropics/claude-code/issues/15094> 服务器重启案例
[42] <https://www.jsjson.com/blog/blog-mcp-streamable-http-guide> 第三方性能比较
