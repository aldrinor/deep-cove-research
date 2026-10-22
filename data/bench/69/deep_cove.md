# A2A and MCP: Different Boundaries, Complementary Roles in AI-Agent Systems

**The central difference is responsibility:** Google’s Agent2Agent protocol, or A2A, standardizes how independent agents delegate work and collaborate; the Model Context Protocol, or MCP, standardizes how an AI application accesses tools, resources, prompts, and external context. A2A’s distinctive contribution is an integrated model for discovering an agent, submitting work, tracking its lifecycle, requesting intervention, and collecting results without exposing the agent’s internal implementation. Google explicitly introduced A2A as complementary to MCP, not as its replacement. [1]

**The practical architecture often uses both:** An agent receives a delegated task through A2A, uses MCP-connected tools internally, and returns A2A artifacts. There is functional overlap—MCP can wrap another agent as a tool—but an ordinary tool call and a resumable collaboration are different contracts. The comparison below uses a **13 September 2026** snapshot, including MCP’s substantial move toward stateless requests in its 2026-07-28 revision. [2]

| Decision dimension | MCP | A2A | Practical judgment |
|---|---|---|---|
| Primary boundary | Application to tools and context | Agent to independent agent | Select by the relationship being standardized |
| Discovery | Server capabilities and primitive catalogs | Agent Cards and declared skills | Function discovery differs from collaborator discovery |
| Interaction | Structured calls and results | Messages or tracked Tasks | Use task semantics when work has a lifecycle |
| State | Stateless core; explicit handles; optional Tasks | Core stateful Tasks and contexts | Separate transport state from work state |
| Context ownership | Host selects context and tool inputs | Remote agent retains internal context | Exchange only information needed for the task |
| Asynchronous work | Streaming, progress, optional Tasks | Polling, streaming, webhook updates | Check declared and implemented capabilities |
| Human intervention | Elicitation and multi-round-trip requests | Input-required and auth-required states | Both support intervention through different models |
| Security and deployment | Local stdio or remote HTTP; optional authorization framework | Network services; advertised security schemes; encrypted production bindings | Trust and policy remain deployment responsibilities |
| Combined-stack role | Tool and data access within participants | Delegation between participants | Direct layering needs no protocol translator |

**The report follows the engineering decisions:** First establish the release and governance context, then explain each protocol’s operating model. The subsequent sections compare discovery, control, state, ownership, and security; demonstrate composition and bridge behavior; and judge A2A’s innovations against the specific integration problems it addresses.

Section references:
[1] Google’s launch announcement <https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/> Excerpt: "A2A is an open protocol that complements Anthropic's Model Context Protocol (MCP), which provides helpful tools and context to agents. Drawing on Google's internal expertise in scaling agentic systems, we designed the A2A protocol to address the challenges we identified in deploying large-scale, multi-agent systems for our customers. A2A empowers developers to build agents capable of connecting with any other agent built using the protocol and offers users the flexibility to combine agents from various providers. Critically, businesses benefit from a standardized method fo…"
[2] MCP specification <https://modelcontextprotocol.io/specification/2026-07-28> Excerpt: "- Stateless, self-contained requests - Per-request capability negotiation Servers offer any of the following features to clients:- Resources: Context and data, for the user or the AI model to use - Prompts: Templated messages and workflows for users - Tools: Functions for the AI model to execute - Elicitation: Server-initiated requests for additional information from users Additional Utilities - Configuration - Progress tracking - Cancellation - Error reporting Beyond the core protocol, MCP defines optional extensions that add modular, specialized, or experimental function…"

## Release context and the September 2026 baseline

### Origins, versions, and terminology

**A2A began as Google’s initiative:** Google published A2A in April 2025, with AuthZed’s historical account dating the public introduction to **9 April 2025**. Google’s announcement described an open protocol supported by more than 50 technology partners and positioned it around collaboration across enterprise applications and frameworks. The Linux Foundation announced the project’s transfer into its governance on **23 June 2025**. [3][4]

**MCP preceded A2A’s public launch:** Anthropic created MCP to replace repeated custom integrations between AI applications and external systems. Its release history identifies **2024-11-05 as the initial specification revision**; the public introduction occurred on **25 November 2024**. Those are different dates: a protocol revision identifier should not be mistaken for the announcement date. Anthropic credits David Soria Parra and Justin Spahr-Summers as MCP’s creators. [5][6][7]

| Attribute | MCP | A2A |
|---|---|---|
| Canonical name | Model Context Protocol | Agent2Agent Protocol |
| Original developer | Anthropic | Google |
| Initial public introduction | 25 November 2024 | 9 April 2025, reported by AuthZed |
| Initial revision context | Revision 2024-11-05 | Google’s April 2025 protocol draft |
| September 2026 release baseline | Stable revision 2026-07-28 | Specification release v1.0.1 |
| Baseline release date | 28 July 2026 | 26 May 2026 on the release listing |
| Governance | LF Projects; maintainer-led | Linux Foundation; Technical Steering Committee |
| Native operating boundary | Tools, resources, prompts, context | Independent agent collaboration |

**The release baselines are specific:** A2A reached v1.0.0 on **12 March 2026**; its GitHub release listing identifies **v1.0.1, dated 26 May 2026**, as the subsequent release. MCP’s release history identifies **2026-07-28** as its stable revision. These are the release baselines for this snapshot, rather than assumptions that every running server already implements them. [8][9][5]

**Three version labels need separating:** An A2A specification release such as `v1.0.1`, an advertised wire protocol version such as `1.0`, and an individual agent’s application version are distinct. A2A negotiates the major/minor protocol version; an Agent Card separately describes the deployed agent’s own version. Likewise, an MCP SDK’s `2.0` version is not the protocol’s revision identifier, which remains date-based. [10][11]

**A2A’s documentation has a labeling inconsistency:** The specification document at the v1.0.1 path still displays “Latest Released Version 1.0.0.” For compatibility decisions, the tagged release, its schema, and its release notes are more useful than that banner. This distinction matters because v1.0.1 includes binding-level fixes, rather than merely editorial changes. [12][9]

Section references:
[3] A2A launch history <https://authzed.com/learn/agent-to-agent-communication-guide-google-a2a-protocol> Excerpt: "Google introduced A2A on April 9, 2025, as an open protocol for agents to discover one another and coo…"
[4] Linux Foundation project announcement <https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents> Excerpt: "DENVER – Open Source Summit North America – June 23, 2025 – The Linux Foundation, the nonprofit organi…"
[5] MCP release history <https://github.com/modelcontextprotocol/modelcontextprotocol/releases> Excerpt: "This release marks the final 2024-11-05 revision of the Model Context Protocol, including all backward…"
[6] Public launch chronology <https://en.wikipedia.org/wiki/Model_Context_Protocol> Excerpt: "MCP was announced by Anthropic ( Anthropic ) in November 2024 as an open standard ( Open standard ) (…"
[7] Anthropic’s introduction <https://www.anthropic.com/news/model-context-protocol> Excerpt: "MCP was created at Anthropic by David Soria Parra and Justin Spahr-Summers. We’re committed to buildin…"
[8] A2A release history <https://github.com/a2aproject/A2A/releases> Excerpt: "1.0.0 (2026-03-12) ⚠ BREAKING CHANGES - spec: Combine TaskPushNotificationConfig andPushNotificationCo…"
[9] A2A v1.0.1 release <https://github.com/a2aproject/A2A/releases/tag/v1.0.1> Excerpt: "(2026-05-26) prefer application/a2a+json in HTTP binding ( recent transcoding-related error changes (…"
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "The specific version of the A2A protocol in use is identified using the Major.Minor elements (e.g. ) o…"
[11] MCP C SDK revision explanation <https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/> Excerpt: "Our versioning strategy declared when we released v1.0 remains the same with v2.0. We’ve been testing…"
[12] Versioned specification document <https://github.com/a2aproject/A2A/blob/v1.0.1/docs/specification.md> Excerpt: "note Latest Released Version 1.0.0 Previous Versions See Release Notes for changes made between versio…"

### Governance and implementation status

**Neither is simply a vendor API:** A2A is a Linux Foundation project with an eight-seat Technical Steering Committee representing Google, Microsoft, Cisco, AWS, Salesforce, ServiceNow, SAP, and IBM. MCP is a Series of LF Projects, LLC project governed through contributors, maintainers, Core Maintainers, and Lead Maintainers; its governance document identifies David Soria Parra and Den Delimarsky as Lead Maintainers with final decision authority. [13][14]

**Their ecosystems are operationally substantial:** A2A has SDKs, framework integrations, official demonstrations, compatibility testing, nightly interoperability testing, and named deployment integrations. MCP has official SDKs and support in clients including Claude, ChatGPT, Visual Studio Code, and Cursor. These implementation inventories establish practical availability; the later implementation section distinguishes them from revision-specific conformance results. [15][16]

**The historical framing has changed:** “Google’s recently released A2A” accurately describes its April 2025 introduction, but by September 2026 the relevant object is a foundation-governed protocol in the 1.0 family. The useful comparison is therefore between evolving interoperability contracts, not a timeless Google-versus-Anthropic product contest.

Section references:
[13] A2A governance <https://github.com/a2aproject/A2A/blob/main/GOVERNANCE.md> Excerpt: "The Agent2Agent project is governed by the Technical Steering Committee. The Committee has eight seats, each held by the f…"
[14] MCP governance <https://modelcontextprotocol.io/community/governance> Excerpt: "Lead Maintainers hold final authority and can veto any decision by Core Maintainers or Maintainers — the role commonly kno…"
[15] A2A SDKs and tooling <https://github.com/a2aproject/a2a-samples/> Excerpt: "Welcome to the official code samples and demonstrations for the Agent2Agent (A2A) Protocol. We are thrilled to have you he…"
[16] MCP-supported applications <https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro> Excerpt: "AI assistants like Claude and ChatGPT, development tools like Visual Studio Code, Cursor, MCPJam, and many others all supp…"

## MCP: how an AI application obtains tools and context

### The host, client, and server boundary

**MCP separates application responsibility from connectivity:** A host is the AI application managing the user interaction and model workflow. A client is a connector inside that host. A server exposes context and capabilities through MCP. A host can use multiple clients to reach different servers without requiring each server to understand the host’s full application architecture. [2]

| Role | Responsibility | Typical example |
|---|---|---|
| Host | Manages the user, model workflow, selection, and consent | Coding assistant or enterprise chatbot |
| Client | Exchanges MCP messages with a server | Connector within the assistant |
| Server | Exposes tools, resources, prompts, and supported features | Repository, database, or calendar service |

**The model is not the connector:** An LLM may select a tool from descriptions presented to it, but application code performs the actual protocol exchange. The host obtains capability descriptions through its client, supplies relevant descriptions or retrieved context to the model, and directs the client to invoke a selected capability. The server executes the operation and returns a result that the host can use in the next model turn. [17]

**Discovery answers a capability question:** Once an endpoint is known, MCP lets the application learn what that server offers. Supported primitive families are exposed through operations such as `tools/list`, `resources/list`, and `prompts/list`. The 2026 implementation model also includes `server/discover` for server-level discovery, while protocol version and client capability information accompany self-contained requests. [17][18]

**Endpoint discovery remains a separate concern:** Knowing which MCP server to contact can come from configuration, installation, or a registry. Learning that server’s available functions is a protocol operation. This is analogous to distinguishing a service directory from an API’s method catalog: the two can be connected, but they solve different problems.

Section references:
[2] MCP specification <https://modelcontextprotocol.io/specification/2026-07-28> Excerpt: "Servers offer any of the following features to clients:- Resources: Context and data, for the user or the AI model to use - Prompts: Templated messages and workflows for users - Tools: Functions for the AI model to execute - Elicitation: Server-initiated request…"
[17] MCP interaction model <https://arxiv.org/html/2607.23884v1> Excerpt: "The results indicate that MCP can support inter-agent coordination in constrained LLM-based systems through a comparatively lightweight implementation model with lower coordination complexity, fewer protocol primitives, and reduced orchestration overhead, althou…"
[18] Official Python SDK’s current wire model <https://github.com/modelcontextprotocol/python-sdk/releases> Excerpt: "At 2026-07-28 the server can no longer call the client, so tools return the question instead. A Resolve(fn) parameter is filled by your function invisibly to the model and can put a question to the user; one tool body serves both eras. Extension APIs, OpenTeleme…"

### Tools, resources, and prompts

**MCP exposes three principal primitives:** Tools perform actions, resources supply readable information, and prompts provide reusable interaction templates. Their conventional control labels describe how a host presents them—not whether developers can bypass permissions or give a model unrestricted execution authority. [2][19]

| Primitive | Conventional control | What it provides | Concrete example |
|---|---|---|---|
| Tools | Model-controlled | Executable functions with structured inputs | Query inventory or create a ticket |
| Resources | Application-controlled | Readable data and context | File contents or a database record |
| Prompts | User-controlled | Reusable messages and workflows | A selected review or analysis template |

**Tools standardize executable capabilities:** A tool description tells the application and model what a function does and what arguments it accepts. The host can then issue a structured call instead of inventing a different connector for every model provider. A database query, file operation, or business API can all sit behind this interface; the server’s internal implementation remains its own concern. [17]

**Resources standardize readable context:** A resource might contain a document, repository file, database record, or API-derived information. The host decides which material is relevant and how to place it into the model’s working context. MCP therefore supplies a path to context; it does not require every available resource to be loaded into every prompt. [2]

**Prompts standardize reusable interaction structure:** A prompt can package a templated message or workflow that the user selects through the host. This is different from a remote agent’s private system prompt. Publishing an MCP prompt is an intentional capability; it does not imply that every server or agent must reveal its internal instructions. [2]

**The host retains orchestration authority:** In the common MCP pattern, the application determines which capabilities are available, what the model sees, and whether a proposed invocation is allowed. Even when the function behind a tool contains sophisticated planning or another LLM, the external contract can remain “call this named capability with these arguments.”

Section references:
[2] MCP specification <https://modelcontextprotocol.io/specification/2026-07-28> Excerpt: "Servers offer any of the following features to clients:- Resources: Context and data, for the user or the AI model to use - Prompts: Templated messages and workflows for users - Tools: Functions for the AI model to execute - Elicitation: Server-initiated requests for additional information fro…"
[19] Primitive control boundaries <https://arxiv.org/html/2505.02279v1> Excerpt: "Aspect: Message Format MCP (Model Context Protocol): JSON-RPC 2.0 with Prompts, Tools, Resources ACP (Agent Communication Protocol): Structured multipart messages with MIME-typed parts A2A (Agent-to-Agent Protocol): Task + Artifact messaging over JSON ANP (Agent Network Protocol): JSON-LD with…"
[17] MCP interaction model <https://arxiv.org/html/2607.23884v1> Excerpt: "The Model Context Protocol (MCP) is a JSON-RPC client–server interface for secure context ingestion and structured tool invocation which streamlines the integration of LLMs with external data sources and tools. To this end, it supports flexible plug-and-play tools, safe infrastructure integrat…"

### JSON-RPC, lifecycle, and transports

**MCP uses structured RPC messages:** Its message format is JSON-RPC 2.0. Requests identify an operation and carry a request ID; successful responses or errors correlate with that ID. Notifications communicate information without the same request/result exchange. This supplies a common envelope for capability discovery, invocation, progress, and other supported interactions. [20]

**The lifecycle is revision-dependent:** Earlier MCP revisions used an initialization phase for version and capability negotiation, an operating phase, and transport shutdown. The 2026-07-28 core changes that arrangement: requests are self-contained, the required `initialize`/`initialized` handshake is removed from the new request path, and protocol metadata travels with each request. [20][21]

| Protocol era | Setup and negotiation | Continuity model | Deployment consequence |
|---|---|---|---|
| 2025 session model | Initialization handshake | Connection-scoped capabilities and sessions | Session-aware routing may be needed |
| 2026-07-28 core | Self-contained request metadata | Stateless protocol request path | Any suitable instance can handle a request |
| Compatibility operation | SDK fallback for older peers | Legacy behavior where required | One deployment can serve multiple revision eras |

**Stateless requests simplify horizontal scaling:** Under a session-bound design, a request may depend on state established with a particular server instance. The new core avoids that protocol-level dependency. A load balancer can route a request to another suitable instance without first reconstructing an MCP session. Microsoft’s C# SDK explanation explicitly connects this change to ordinary HTTP routing, middleware, and multi-instance deployment. [11]

**MCP retains local and remote transports:** With `stdio`, a client launches a server subprocess and exchanges newline-delimited messages over standard input and output. With Streamable HTTP, messages are posted to a single endpoint and responses arrive as JSON or a request-scoped Server-Sent Events stream. Custom transports can preserve the protocol’s message and metadata semantics. [21]

**Streaming does not imply a persistent session:** Server-Sent Events, or SSE, is an HTTP mechanism for sending a sequence of events to a client. MCP can stream a particular response while keeping the wider protocol request model stateless. A connection can therefore remain open for one operation without becoming a hidden application session.

**Interactive tools survive the stateless transition:** Multi Round-Trip Requests let a server return an `input_required` result containing requests for additional information and opaque continuation state. The client obtains the information and reissues the operation with the responses and continuation state. This preserves interactive behavior without requiring the server to call back through a long-lived session. [11]

**The wire surface also aids infrastructure:** The 2026 HTTP design uses headers such as `Mcp-Method` and `Mcp-Name` so gateways and routers can recognize the operation without parsing the JSON body. The body remains authoritative, and a disagreement between it and the mirrored headers is an error. This is a deployment improvement, not a change from tool access into peer-agent collaboration. [11]

Section references:
[20] MCP JSON-RPC foundation <https://modelcontextprotocol.io/specification/2025-03-26/basic> Excerpt: "Responses are sent in reply to requests, containing the result or error of the operation.- Responses MUST include the same ID as the request they correspond to. - Responses are further sub-categorized as either successful results or MUST be set. A response MUST NOT set both. - Results MAY follow any JSON object structure, while errors MUST include an error code and message at minimum. - Error codes MUST be integers. Notifications Notif…"
[21] 2026 transport model <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports> Excerpt: "Custom transports that run over a reliable bidirectional byte stream (e.g., Unix domain sockets or TCP) SHOULD reuse the stdio framing rather than defining a new one: the stdio binding is just newline-delimited JSON-RPC over a byte stream, and only its process-lifecycle rules are specific to standard streams.Backward Compatibility Earlier protocol revisions established a connection-scoped session with aninitialize handshake and allowed…"
[11] MCP C SDK revision explanation <https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/> Excerpt: "It makes the protocol stateless by default, standardizes the HTTP surface so ordinary HTTP infrastructure can route MCP traffic, and introduces Multi Round-Trip Requests so interactive tools no longer require a long-lived session. That shift plays directly to .NET’s strengths. MCP over HTTP is a web workload after all, and ASP.NET Core has always focused on the exact concerns this MCP specification revision cares about: routing, middle…"

### Authorization and state boundaries

**Stateless protocol does not mean stateless tools:** A server can create an explicit handle—such as `basket_id` or `browser_id`—and require it on subsequent calls. The underlying basket or browser remains stateful; continuity is simply visible in the application arguments rather than hidden in transport metadata. [22]

**Long-running work is an optional extension:** MCP’s 2026 model includes a Tasks extension for asynchronous execution, polling, durable handles, and mid-flight input. Both peers must explicitly support that extension. Consequently, “MCP has no tasks” is outdated, while “every MCP tool invocation has A2A-equivalent task semantics” is also incorrect. [2]

**Authorization depends on the deployment:** MCP makes its authorization framework optional at protocol level. For HTTP implementations using it, the server acts as an OAuth 2.1 resource server and the client acts for the resource owner. Stdio implementations generally obtain credentials from the environment rather than following the HTTP authorization flow. [23]

**Consent remains a host responsibility:** MCP’s security guidance treats tools as potentially arbitrary code execution and requires explicit user consent for tool invocation and disclosure of user data. The protocol cannot itself enforce an application’s user interface, permissions, or data protection policy. “Model-controlled tool” therefore means the model can propose or select the operation, not that it should execute outside host control. [2]

**MCP’s architectural takeaway is capability access:** Choose it when the main requirement is a reusable, discoverable interface to functions and context, while keeping orchestration, consent, and application state explicit.

Section references:
[22] MCP explicit state handles <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/> Excerpt: "The explicit-handle pattern simply makes the state visible to the model rather than hidden away. Server-to-client requests, restructured A stateless protocol still needs a way for servers to ask the client for something mid-…"
[2] MCP specification <https://modelcontextprotocol.io/specification/2026-07-28> Excerpt: "Notable extensions include:- Tasks: Asynchronous execution of long-running operations, with polling, mid-flight input, and durable handles - Skills over MCP: Rich, structured instructions for agent workflows, discovered and…"
[23] MCP authorization specification <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization> Excerpt: "A protected MCP server acts as an OAuth 2.1 resource server, capable of accepting and responding to protected resource requests using access tokens. An MCP client acts as an OAuth 2.1 client, making protected resource reques…"

## A2A: how delegated work becomes discoverable and trackable

### Agent Cards describe a collaborator

**A2A begins with an independent participant:** An A2A client initiates requests; an A2A server exposes a remote agent or agentic system. “Peer collaboration” describes the participants’ independent responsibilities, not a requirement for a decentralized network transport. The wire interaction still has client and server roles, and a participating agent may act in either role across different interactions. [24]

**The Agent Card is its entry contract:** It is a JSON manifest describing the agent’s identity, skills, capabilities, supported interfaces, input/output modes, and security requirements. A client can use it to decide whether the agent is a suitable collaborator and how to communicate with it. The card describes the external service, not its private chain of reasoning or internal tool inventory. [25]

**Discovery uses known locations or directories:** A client can retrieve a card from `/.well-known/agent-card.json`, receive it through direct configuration, or obtain it from a registry. A2A standardizes the discoverable metadata and its use; it does not supply a mandatory global directory of every agent. [10]

**Selection involves more than a skill name:** A client should consider the declared skill, supported media types, protocol version, transport binding, and required extensions. It should also inspect whether the agent advertises streaming or push notifications. For example, an agent that describes document analysis but accepts only text is not automatically suitable for an image-bearing request. [10]

**Skills are descriptive rather than ordinary functions:** An Agent Card can describe a broad capability such as research, diagnosis, or shipment planning. That is not necessarily an exact function signature equivalent to an MCP tool’s argument schema. The client may communicate a goal and negotiate details through messages rather than call a skill ID as though it were a predefined procedure. [25]

Section references:
[24] A2A roles and concepts <https://a2a-protocol.org/latest/specification/> Excerpt: "- A2A Client: An application or agent that initiates requests to an A2A Server on behalf of a user or another system. - A2A Server (Remote Agent): An agent or agentic system that exposes an A2A-compliant endpoint, processing tasks and providing responses."
[25] A2A Agent Card model <https://github.com/a2aproject/A2A/blob/v1.0.0/specification/a2a.proto> Excerpt: "// metadata including the agent's identity, capabilities, skills, supported // communication methods, and security requirements. // Next ID: 20 message AgentCard { // A human readable name for the agent. // Example: Recipe Agent string name = 1 (google.a…"
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "Error Name: VersionNotSupportedError Description: The A2A protocol version specified in the request (via A2A-Version service parameter) is not supported by the agent. Functionality: Send message JSON-RPC Method: SendMessage gRPC Method: SendMessage REST…"

### Tasks, messages, parts, and artifacts

**A2A distinguishes communication from work:** A Message is a communication turn. A Task is the tracked work unit that may result from that communication. Parts carry content inside Messages and Artifacts; Artifacts represent outputs of the work. Keeping these concepts separate makes delayed execution and multi-turn clarification easier to express consistently. [24]

| Object | Role | Typical contents | Important distinction |
|---|---|---|---|
| Agent Card | Describes the remote participant | Identity, skills, interfaces, security | Capability declaration, not an execution result |
| Message | Carries a communication turn | Role, identifiers, Parts | Can initiate or continue work |
| Task | Tracks a work unit | ID, status, history, artifacts | Has an observable lifecycle |
| Part | Carries one content unit | Text, data, bytes, or file reference | Used in both messages and outputs |
| Artifact | Represents a task output | Document, image, structured data | Deliverable rather than progress narration |
| Context identifier | Groups related interactions | Opaque `contextId` | Reference to continuity, not shared memory |

**A message can produce either response form:** `SendMessage` may return a direct Message for a simple interaction or a Task for work that needs tracking. A quick informational reply need not create a task lifecycle. Conversely, a request that requires planning, external operations, or further input can return an addressable Task. [24]

**Task identity outlives a request:** The server creates the task ID, which the client can subsequently use to retrieve or interact with that work. This is different from the JSON-RPC request ID, which correlates a particular request and response. A message ID, task ID, and context ID likewise serve different purposes rather than being interchangeable correlation strings. [10]

**Artifacts give results an explicit home:** A report, extracted invoice data, modified image, or booking result can be returned as an Artifact composed of Parts. Status messages can explain progress, while artifact updates carry the developing output. This avoids forcing the client to infer which conversational sentence is the authoritative deliverable. [10]

**Multimodal content is part of the model:** Parts can represent text, structured data, file URLs, or inline bytes, with media information where appropriate. This lets a task combine, for example, a textual request and an image reference, then produce structured findings and a resulting document. Acceptance still depends on the agent’s advertised modes and implemented capability. [25]

**Retention is an implementation responsibility:** Artifacts and task history can make results retrievable after a connection ends, but the deployment must supply the storage and retention behavior. An in-memory task store does not become restart-safe merely because its objects use a standardized schema. A2A defines the externally visible model; storage infrastructure determines its operational durability.

Section references:
[24] A2A roles and concepts <https://a2a-protocol.org/latest/specification/> Excerpt: "The core interaction model defined by A2A is for clients to send messages to initiate a task that produces one or more artifacts. Messages play several key roles: - Task Initiation: Clients send Messages to agents to initiate new tasks. - Clarification Messages: Agents may send Messages back to the client to request clarification prior to initiating a task. - Status Messages: Agents attach Messag…"
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "- Artifact: An output (e.g., a document, image, structured data) generated by the agent as a result of a task, composed of - Streaming: Real-time, incremental updates for tasks (status changes, artifact chunks) delivered via protocol-specific streaming mechanisms. - Push Notifications: Asynchronous task updates delivered via server-initiated HTTP POST requests to a client-provided webhook URL, fo…"
[25] A2A Agent Card model <https://github.com/a2aproject/A2A/blob/v1.0.0/specification/a2a.proto> Excerpt: "// The media_type (MIME type) of the part content (e.g., text/plain , application/json , image/png ). // This field is available for all part types. string media_type = 7; // Defines the sender of a message in A2A protocol communication. // The role is unspecified. ROLE_UNSPECIFIED = 0; // The message is from the client to the server. ROLE_USER = 1; // The message is from the server to the client."

### Execution modes and update paths

**Blocking and asynchronous execution are distinct choices:** In the 1.0 schema, `return_immediately` controls response timing. When false or unset, the operation waits until the Task reaches a terminal or interrupted state. When true, it returns after task creation while processing may continue. A direct Message response does not use that task-waiting behavior. [25]

**The lifecycle remains independent of the connection:** Once a Task exists, the client can observe it through retrieval, a stream, or webhook updates. This is useful when execution lasts minutes, hours, or days, or when a mobile application or serverless caller cannot hold a connection open throughout the work. [26]

| Interaction mode | Mechanism | Best fit | Client responsibility |
|---|---|---|---|
| Blocking interaction | `SendMessage`, waiting enabled | Work expected to finish within the request | Handle completion or interruption |
| Non-blocking submission | `SendMessage`, immediate return | Background execution | Retain and monitor the task ID |
| Polling | `GetTask` | Infrequent updates or restrictive networks | Choose polling intervals and retrieve results |
| Streaming | `SendStreamingMessage` or `SubscribeToTask` | Interactive progress and artifact updates | Maintain or re-establish the stream |
| Push notifications | Server POST to a registered webhook | Disconnected or long-running workflows | Authenticate, acknowledge, and deduplicate |

**Polling retrieves authoritative current state:** `GetTask` returns the task’s current status, artifacts, and optionally history. This can be used after initial submission, following a webhook, or after a stream has ended. It gives clients a way to recover the state of work without depending on continuous receipt of every progress event. [10]

**Streaming exposes incremental progress:** A task stream begins with a Task and can continue with status and artifact update events. In the web bindings, SSE carries those updates; gRPC uses server-streaming RPCs. A direct Message-only stream is a simpler pattern: one Message followed by closure, rather than an implied task lifecycle. [10]

**Push decouples execution from connection lifetime:** The server posts an update to a client-provided webhook, and the client can retrieve the complete Task afterward. This is particularly useful when an operation completes long after its initiating request. Streaming and push are advertised capabilities, so a client should not assume every A2A deployment offers both. [26]

Section references:
[25] A2A Agent Card model <https://github.com/a2aproject/A2A/blob/v1.0.0/specification/a2a.proto> Excerpt: "// If true , the operation returns immediately after creating the task, // even if processing is still in progress. // If false (default), the operation MUST wait until the task reaches a // terminal ( COMPLETED , FAILED , CANCELED , REJECTED ) or interrupted // ( INPUT_REQUIRED , AUTH_REQUIRED ) state before returning. bool ret…"
[26] A2A streaming and asynchronous guide <https://github.com/a2aproject/A2A/blob/main/docs/topics/streaming-and-async.md> Excerpt: "For very long-running tasks (for example, lasting minutes, hours, or even days) or when clients are unable to or prefer not to maintain persistent connections (like mobile clients or serverless functions), A2A supports asynchronous updates using push notifications. This allows the A2A Server to actively notify a client-provided…"
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "This is typically used for polling the status of a task initiated with Send Message, or for fetching the final state of a task after being notified via a push notification or after a stream has ended. {{ proto_to_table( GetTaskRequest ) }} See History Length Semantics for details about historyLength : Current state and artifacts…"

### Pauses, continuation, and context

**Interruption is not failure:** A2A distinguishes processing states, paused states, and terminal outcomes. An agent can request clarification or additional authorization without pretending the work has completed or failed. The following are the eight named operational states commonly used in the lifecycle. [25]

| State group | States | Meaning | Expected client action |
|---|---|---|---|
| Processing | Submitted; working | Accepted or actively processing | Monitor or await results |
| Interrupted | Input-required; auth-required | Further input or authorization is needed | Resolve the request through an appropriate channel |
| Terminal | Completed; failed; canceled; rejected | This task has reached its final outcome | Collect results or handle the outcome |

**Input-required preserves the work reference:** The client can send a follow-up Message associated with the same task and context. A request for travel booking, for example, can pause while the agent asks for missing route details. A later answer continues that work rather than requiring an unrelated request with an application-invented correlation convention. [10]

**Auth-required signals a dependency, not permission:** A task may need an additional credential or human approval before continuing. The state transition itself does not authorize the requested action. A2A’s specification leaves the meaning, scope, validity, and revocation of the resulting credential or decision to the implementation, issuer, or extension, and generally directs credential exchange out of band. [10]

**Context identifiers organize continuity without merging memory:** A `contextId` can group related Tasks and Messages. It does not transfer a shared LLM transcript or grant access to another agent’s private state. Clients should treat server-generated identifiers as opaque and respect the server’s context policy. A completed task does not accept further messages; new follow-up work can instead be represented by a new task within the relevant context. [10]

**A2A’s architectural takeaway is managed delegation:** It gives independently implemented participants a common way to identify, observe, interrupt, continue, and complete work.

Section references:
[25] A2A Agent Card model <https://github.com/a2aproject/A2A/blob/v1.0.0/specification/a2a.proto> Excerpt: "ROLE_AGENT = 2; // Message is one unit of communication between client and server. // associated with a context and/or a task. For server messages, context_id must // be provided, and task_id only if a task was created. For client messages, both // fields are optional, with the caveat that if both are provided, they have to // match (the context_id has to be the one that is set on the task). // task_id is provided, the server will infe…"
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "The meaning and scope of any resulting authorization decision or credential MUST be defined by the agent's implementation, by the credential issuer, or by an A2A extension. If an implementation requires authorization for specific operations, it is responsible for defining how the authorized operation is identified and how that authorization is checked before the operation is performed. A credential or authorization decision obtained wh…"

## The differences that determine protocol choice

### The important distinction is the external contract

**An agent is not defined by transport:** Both protocols can use HTTP and structured messages, and both have client/server roles. An MCP tool can invoke an LLM, while an A2A participant can include deterministic software. The difference is the responsibility exposed to the caller: a named capability invocation versus a collaborator accepting work under a task-oriented interaction model. [27][17]

| Technical axis | MCP | A2A |
|---|---|---|
| Primary relationship | Host or agent to capability server | Client to independent remote agent |
| Abstraction level | Tool, resource, and prompt access | Goal delegation and collaboration |
| Discovery object | Capability metadata and primitive listings | Agent Card with skills and interfaces |
| Control flow | Named operation with structured arguments | Message yielding a Message or Task |
| Core state model | Stateless requests in 2026-07-28 | Stateful Tasks over independent requests |
| Task tracking | Opt-in Tasks extension | Core task IDs, states, retrieval, and artifacts |
| Context ownership | Host manages its model context and disclosed inputs | Remote agent manages its own internal execution context |

**A tool contract constrains the interaction shape:** If a caller asks `get_inventory(sku)`, it expects that capability’s result. Whether the server internally uses SQL, another API, or an LLM need not matter. If the caller instead asks a supplier agent to resolve a shortage, the supplier may evaluate alternatives, request approval, contact other systems, and return a negotiated outcome. A2A makes that longer relationship explicit.

**Autonomy can still exist behind MCP:** AWS demonstrates this with an Employee Info Agent wrapped as an MCP server tool and invoked by an HR agent. That is a legitimate inter-agent implementation. Its existence disproves the absolute statement that MCP cannot connect agents; it does not make the wrapper’s external contract identical to A2A’s task lifecycle. [28]

**The selection rule is conditional:** A tool wrapper can be sufficient when another agent’s behavior is well-defined and fits an invocation/result boundary. A2A becomes more compelling when clients need common semantics for clarification, interruption, status, cancellation, independent execution, and artifacts across implementations. This is a choice about the collaboration contract, not a judgment about whether one backend is “truly intelligent.”

Section references:
[27] Official A2A–MCP comparison <https://a2a-protocol.org/latest/topics/a2a-and-mcp/> Excerpt: "The Agent2Agent (A2A) Protocol and the Model Context Protocol (MCP) address these distinct but highly complementary needs. Horizontal and Vertical Layers¶ One way to picture the two protocols is by the direction they connect in. MCP is vertical. It deepens a single agent. You can build an agentic system under one roof —…"
[17] MCP interaction model <https://arxiv.org/html/2607.23884v1> Excerpt: "For this study, we therefore focus on evaluating MCP under its official specification and intended usage model, in order to ensure both a clearer and a fairer comparison with A2A’s protocol-level support for inter-agent communication, while considering infrastructure-mediated coordination as a direction for future work.…"
[28] AWS’s MCP-based HR example <https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/> Excerpt: "Multiple protocols have emerged that enable this capability, including the Model Context Protocol (MCP), open sourced by Anthropic in 2024, and the Agent2Agent protocol (A2A), introduced by Google this year. We believe that both MCP and A2A have a lot to offer. Demonstrating our commitment to these open standards, AWS i…"

### Discovery and negotiation expose different information

**MCP discovery favors invocation precision:** A tool catalog provides names, descriptions, and input schemas suitable for selecting a concrete function. That helps a host construct a valid call and govern its available operations. The scope of discovery is generally the server’s offered capabilities after the server endpoint has been selected.

**A2A discovery favors collaborator selection:** An Agent Card combines a description of what the participant does with information about its endpoint, transport, protocol version, modalities, optional features, and authentication requirements. That supports decisions about who should receive a goal and whether the intended interaction can be supported. [10]

**Negotiation is more than semantic similarity:** Two agents may both advertise “document analysis” while disagreeing about input formats, required extensions, or acceptable output modes. A2A provides declarations and compatibility checks for those protocol-level requirements. It does not guarantee that two implementations interpret every business concept identically or deliver equally good analysis.

**Extensions make compatibility explicit:** A2A agents can declare extensions and clients can opt into them through the binding’s service parameters. An unsupported required extension produces an error; a breaking extension version uses a new URI rather than silently falling back. This is useful for domain-specific additions without pretending the core protocol defines every domain’s semantics. [10]

**Declarations become testable obligations:** The A2A Technology Compatibility Kit, or TCK, uses Agent Card declarations to select tests. Advertising streaming or push makes the corresponding checks applicable; omitting those capabilities allows those optional-feature checks to be skipped. This links discovery metadata to observable behavior rather than treating the card solely as a description for an LLM. [29]

Section references:
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "Extensions allow agents to declare additional capabilities such as protocol enhancements or vendor-specific features, maintain compatibility with clients that don't support specific extensions, enable innovation through experimental or domain-specific features without modifying the core protocol, and facilitate standardization by providing a pathway for community-developed features to b…"
[29] A2A capability validation <https://github.com/a2aproject/a2a-tck/blob/main/docs/SDK_VALIDATION_GUIDE.md> Excerpt: "This guide helps SDK developers understand how to use the A2A Technology Compatibility Kit (TCK) to validate their implementations and achieve A2A specification compatibility. ./run_tck.py --sut-url --category mandatory Result: If this fails, your SDK is NOT A2A compliant. Fix all mandatory failures before proceeding. ./run_tck.py --sut-url --category capabilities Result: If this fails,…"

### State, ownership, and recovery are separate axes

**Statefulness is not one binary property:** Transport sessions, application state, task execution state, and model context are different things. MCP’s current core removes required protocol sessions while allowing explicit application handles and an optional Tasks extension. A2A maintains stateful Tasks without requiring the client to keep one connection open throughout their execution.

**Neither protocol automatically shares all context:** An MCP host supplies selected inputs and decides how retrieved information enters its model workflow. An A2A client sends selected Messages and Parts, while the remote agent retains its private prompts, memory, and tools. The difference is not “MCP exposes everything, A2A exposes nothing”; it is which external interaction the protocol standardizes. [2][24]

**Opaque tools are not unique to A2A:** An MCP server need not disclose its SQL queries, proprietary algorithms, or internal prompts either. A2A’s stronger distinction is that opacity surrounds an independently managed collaborator with its own task responsibility. The caller can monitor publicly observable work without receiving the implementation needed to perform that work itself.

**References can reduce unnecessary copying:** A2A permits file references and structured identifiers, so a deployment can exchange a reference to retained material instead of repeating a large payload in every handoff. Oracle’s research/writer example illustrates this pattern using a database-backed `memory_id`. The optimization comes from payload-by-reference and governed storage, not an intrinsic guarantee that A2A messages consume fewer tokens than MCP results. [30]

**Task recovery differs from event replay:** A2A allows retrieval of current task state after disconnection, but its specification warns that clients may miss streamed status Messages and that those Messages must not carry critical information as the sole reliable delivery mechanism. Task history is also not guaranteed to retain every transient message. Durable results and recoverable workflow state therefore need an intentional storage policy. [10]

Section references:
[2] MCP specification <https://modelcontextprotocol.io/specification/2026-07-28> Excerpt: "The Model Context Protocol enables powerful capabilities through arbitrary data access and code execution paths. With this power comes important security and trust considerations that all implementors must c…"
[24] A2A roles and concepts <https://a2a-protocol.org/latest/specification/> Excerpt: "Applications that use this media type: AI agent platforms, agentic workflow systems, multi-agent collaboration tools, and enterprise automation systems that implement the A2A protocol for agent-to-agent comm…"
[30] Oracle’s shared-state example <https://blogs.oracle.com/developers/the-agent-communication-matrix-when-mcp-a2a-and-plain-rest-each-win> Excerpt: "Three reference patterns cover most production needs. MCP-Centric Tool Access (one orchestrator, multiple tools), A2A Mesh with Oracle Memory (peer agents coordinating via task envelopes), and Queue-Backed B…"
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "The core interaction model defined by A2A is for clients to send messages to initiate a task that produces one or more artifacts. Messages play several key roles: - Task Initiation: Clients send Messages to…"

### Security, transport, and deployment consequences

**The surrounding infrastructure remains consequential:** Both protocols reuse established web mechanisms rather than creating a complete identity and trust system. Their deployment patterns differ, but neither protocol’s name proves that an endpoint, tool description, or agent output deserves trust.

| Technical axis | MCP | A2A |
|---|---|---|
| Streaming and async | Streamed replies, progress, optional Tasks | Task polling, streams, and optional webhooks |
| Security and identity | Optional OAuth-based HTTP authorization; host consent | Advertised schemes; request authentication and authorization |
| Standard transport surface | Stdio and Streamable HTTP | JSON-RPC, gRPC, HTTP+JSON/REST |
| Deployment topology | Local subprocess or remote service | Network-exposed agent service |
| Ecosystem | Broad client and SDK support | Multiple SDKs, frameworks, cloud integrations, TCK/ITK |
| Governance | LF Projects; Lead and Core Maintainers | Linux Foundation; eight-seat TSC |
| Interoperability boundary | Application-to-capability contract | Inter-agent collaboration contract |

**A2A advertises enterprise authentication requirements:** Its schema supports API keys, HTTP authentication, OAuth 2.0, OpenID Connect, and mutual TLS. Production HTTP bindings require HTTPS, while gRPC uses TLS. Credentials are acquired outside the A2A conversation and carried in appropriate headers or metadata. [25][10]

**Authorization has requirements but no universal policy engine:** A2A requires authorization checks and caller-scoped access to Tasks and related resources. The server defines the actual permission model—user, role, workspace, tenant, or domain-specific policy. It is therefore more accurate to say that A2A specifies enforcement responsibilities while leaving the authorization model implementation-specific than to say it simply has no authorization. [10]

**Authentication does not constrain delegated intent:** A valid OAuth token can still be too broad for a subtask. An agent delegated to summarize vacation balances should not automatically inherit permission to export unrelated payroll records. AuthZed’s analysis makes this concrete: perimeter authentication needs finer task- and data-level enforcement when agents recursively delegate work. [3]

**Local MCP changes the trust surface:** A stdio server is a subprocess, often operating with credentials or filesystem permissions supplied by the host environment. Remote MCP instead introduces network endpoint, token, and server trust questions. Consequently, “MCP is local and A2A is remote” is misleading: MCP supports remote services, and A2A participants can also run inside one organization or cluster.

**Signed cards establish integrity, not competence:** A2A supports optional JSON Web Signatures over canonicalized Agent Cards. A valid signature helps establish who signed the declaration and whether it was altered. It does not prove the declared skill works correctly, that the signer should receive sensitive data, or that an artifact is safe. The client still needs a trust anchor and policy for accepting the signer. [10]

**Untrusted descriptions are a shared risk:** A2A’s official samples warn that Agent Card names, descriptions, skills, Messages, Artifacts, and task statuses can carry prompt-injection content. MCP similarly treats tool descriptions and annotations as untrusted unless obtained from a trusted server. Discovery metadata should inform routing, not silently acquire authority over the host’s instructions or permissions. [15][2]

**Provider binding matters beyond readable names:** In *Security Threat Modeling for Emerging AI-Agent Protocols*, a deliberately constructed two-server MCP experiment produced 52 wrong-provider executions in 100 trials when cloned tool metadata was resolved by randomized tie-breaking. The result concerns the tested resolver and configuration, not an unavoidable failure of every MCP client. Its practical lesson is to bind a selected capability to an approved provider instead of relying only on a persuasive name or description. [31]

Section references:
[25] A2A Agent Card model <https://github.com/a2aproject/A2A/blob/v1.0.0/specification/a2a.proto> Excerpt: "// OAuth 2.0 authentication. OAuth2SecurityScheme oauth2_security_scheme = 3; // OpenID Connect authentication. OpenIdConnectSecurityScheme open_id_connect_security_scheme = 4; // Mutual TLS authentication. MutualTlsSecurityScheme mtls_security_scheme = 5; // Defin…"
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "- Agent Card: A JSON metadata document published by an A2A Server, describing its identity, capabilities, skills, service endpoint, and authentication requirements. - Message: A communication turn between a client and a remote agent, having a ( user or agent ) and…"
[3] A2A launch history <https://authzed.com/learn/agent-to-agent-communication-guide-google-a2a-protocol> Excerpt: "The agent instantly spins up a sub-agent to query the internal payroll database, passing along the employee's broad OAuth token to authenticate the request. From the database's perspective, the sub-agent is the employee. It has read access to everything the employe…"
[15] A2A SDKs and tooling <https://github.com/a2aproject/a2a-samples/> Excerpt: "All data received from an external agent—including but not limited to its AgentCard, messages, artifacts, and task statuses—should be handled as untrusted input. For example, a malicious agent could provide an AgentCard containing crafted data in its fields (e.g.,…"
[2] MCP specification <https://modelcontextprotocol.io/specification/2026-07-28> Excerpt: "- In particular, descriptions of tool behavior such as annotations should be considered untrusted, unless obtained from a trusted server. - Hosts must obtain explicit user consent before invoking any tool - Users should understand what each tool does before authori…"
[31] Security study and experiment <https://arxiv.org/html/2602.11327v2> Excerpt: "Metadata cloned \Rightarrow tie regime Random tie-break 100 52 0.520 Note: Exp: Experiment, N: Number of trials, VR: Violation Rate. MCP v1.25.0 (the latest version at the time of writing) is used in this experiment to ensure that the measured behavior is not a leg…"

### Richer semantics impose a complexity trade-off

**A2A’s additional structure has engineering cost:** *A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems* implemented the same fixed software-engineering collaboration with both protocols. The authors counted a smaller MCP implementation and a larger A2A implementation with more coordination abstractions and stages. [17]

| Study metric | MCP implementation | A2A implementation |
|---|---|---|
| Source lines of code | 1,255 | 1,898 |
| Coordination primitives | 4 | 10 |
| Coordination stages per interaction | 2 | 6 |
| Validation prompts | 30 | 30 |

**The measured increase was implementation-specific:** A2A used **51.2% more source lines**, calculated as `(1,898 − 1,255) ÷ 1,255 × 100`. The study counted Python and Java source using `cloc`, excluding blank lines, comments, and configuration files. Its 30 prompts comprised 10 straightforward and 20 more complex cases; the measurements characterize code and coordination structure, not a general latency or quality ranking. [17]

**Current MCP changes narrow simplistic contrasts:** The study supports the argument that A2A supplies explicit lifecycle abstractions while a tool-wrapper implementation can be lighter. Its broader statements about MCP lacking native multi-turn or task mechanisms must be read against the protocol era and implementation it evaluated, because the 2026 revision adds MRTR and an opt-in Tasks extension.

**The comparison’s takeaway is conditional selection:** Prefer the smallest contract that preserves the required behavior; richer coordination semantics are valuable when they replace application-specific lifecycle machinery, not merely because they exist.

Section references:
[17] MCP interaction model <https://arxiv.org/html/2607.23884v1> Excerpt: "The MCP-based and A2A-based implementations were validated using 30 prompts, of which 10 were straightforward and 20 were of higher complexity. The validation prompts are available in . Listing 1 contains one of the validation prompts, which requests the generation of a library model. Listing 2 presents the solution produced by the solution agent in response to the prompt in Listing 1, which was successfully validated both syntactically and semantically. 5.1 Analysis of Implementation and Coordination Complexity Table 1 presents a comparison between the MCP-based and A2A-based implementations in terms of implementation and coordination complexity. The A2A-based implementation cont…"

## How A2A and MCP connect in real workflows

### Direct layering requires no wire translation

**Composition is simpler than conversion:** An A2A server can use an MCP client internally without translating A2A into MCP. The agent receives a goal, decides how to execute it, calls its tools, and constructs a result. Each protocol terminates at the boundary it was designed to standardize. [27]

**A specialist can retain implementation freedom:** A purchasing, research, or verification agent can change its internal tool servers while preserving its A2A service contract. Conversely, a tool server can serve different MCP hosts without becoming an A2A participant. Neither protocol requires the other: A2A agents can call ordinary APIs, and MCP hosts can operate without any inter-agent delegation.

**The KYC pattern makes this concrete:** Tyk’s know-your-customer example places A2A between an orchestrator and a KYC agent, while MCP connects that specialist to credit-check and identity-verification services. The orchestrator receives the specialist’s completed Task and artifacts rather than managing its internal sequence of tool calls. [32]

1. The orchestrator selects the KYC agent using its declared capability and interaction requirements.
2. It sends the verification request through A2A.
3. The KYC agent calls the credit-check service through MCP.
4. It calls the identity-verification service through MCP and synthesizes the findings.
5. It returns the A2A task outcome and artifacts to the orchestrator.

**Responsibility stays on the correct side:** The orchestrator is responsible for choosing and authorizing the delegation. The specialist is responsible for its verification workflow and permitted tool use. This separation can reduce coupling, but it also makes the specialist’s output contract and access policy important: a successful task status is not, by itself, a regulatory conclusion.

Section references:
[27] Official A2A–MCP comparison <https://a2a-protocol.org/latest/topics/a2a-and-mcp/> Excerpt: "The Agent2Agent Protocol lets different agents collaborate to reach a common goal. This protocol offers the following capabilities: - Standardizes how independent, often opaque, AI agents communicate and collaborate as peers. - Gives agents an application-level protocol. With it, agents discover each other and negotiate interactions. They also manage shared task…"
[32] Layered KYC example <https://tyk.io/learning-center/agent-protocols-a-complete-guide-to-mcp-a2a-and-acp/> Excerpt: "Where MCP connects an application to a tool, A2A connects a team of specialist agents, potentially across organizations or frameworks. A2A reached v1.0 in 2026 and is governed under the Linux Foundation. The v1.0 spec is explicitly layered: - Canonical data model: AgentCard, AgentSkill, Task, Message, Part, Artifact (defined in Protobuf, also published as JSON S…"

### The official travel sample uses both layers

**The travel example demonstrates heterogeneous composition:** The A2A project’s `a2a_mcp` sample combines **three ADK task agents** with a **LangGraph planner**. The specialists handle air tickets, hotels, and car rental; each uses an MCP helper tool to query a domain-specific SQLite database. Results return to the planning workflow through A2A. [33]

| Participant | Framework | A2A responsibility | Internal MCP use |
|---|---|---|---|
| Planner | LangGraph | Decomposes and coordinates the trip request | Retrieves collaborator information |
| Air Tickets agent | ADK | Handles flight-related delegated work | Queries flight data |
| Hotels agent | ADK | Handles accommodation work | Queries hotel data |
| Car Rental agent | ADK | Handles rental-car work | Queries rental-car data |

**MCP also supplies discovery storage:** In this sample, an MCP server acts as a queryable repository of Agent Cards exposed as resources. A client lists or retrieves suitable cards, constructs an A2A client from them, and then communicates directly with the selected agents. The sample explicitly states that MCP is not involved in that direct runtime interaction after discovery. [33]

**This is co-use, not semantic conversion:** MCP transports the card as a resource; the card tells the caller how to begin an A2A interaction. There is no requirement to reinterpret every A2A Task as an MCP tool result. This is an important counterexample to the assumption that any system using both protocols must contain a complex bridge.

**Replanning illustrates the division of labor:** The sample allows the overall workflow to reconsider its plan after a budget mismatch or booking failure. Tool servers supply domain data, specialists perform their delegated roles, and the planner decides how to revise the larger arrangement. A2A standardizes communication among those participants; it does not prescribe the planning algorithm.

Section references:
[33] Official A2A/MCP travel sample <https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/a2a_mcp/README.md> Excerpt: "This enables dynamic agent interaction, particularly for planning and orchestration agents that utilize the A2A protocol. The Agent-to-Agent (A2A) protocol standardizes runtime communication between agents. - Agent Card: A JSON schema describing an agent's identity, capabilities (actions/functions), and interaction endpoints. - Message Formats & Interaction Flows: Such as for direct agent-to-agent interaction. MCP defines a standard way for applications (including AI models) to discover, access, and utilize contextual information, referred to as tools , resources , etc. The central idea is to use an MCP server as a centralized, queryable repository for A2A Agent Cards. - Each A2A Agent Card (JSON) is stored (e.g., as a JSON file). - The MCP server exposes these Agent Card…"

### Human intervention and framework independence

**The purchasing codelab demonstrates different behaviors:** Google’s purchasing concierge uses ADK to communicate with a CrewAI burger seller and a LangGraph pizza seller. The pizza agent accepts an order directly, while the burger agent asks for confirmation. The concierge relays the confirmation interaction and then continues the workflow. [34]

**The important result is preserved autonomy:** The sellers do not have to share the concierge’s framework or internal code. Nor must they behave identically. The common boundary lets the caller interact with each seller’s exposed behavior while keeping implementation-specific decisions on the seller’s side.

**The demonstration also has a revision context:** The codelab’s code advertises protocol version `0.2.6` and uses the earlier `/.well-known/agent.json` card path. Its demonstrated framework interoperability and confirmation flow remain informative, while its exact wire examples should not be substituted for the 1.0 schema and current card path. [34]

**An MCP-enabled agent can be exposed directly:** Google Cloud’s conversion guide starts with an ADK agent using `firecrawl-mcp` for web scraping. It adds an AgentSkill, AgentCard, and an A2A-facing task manager so an orchestrator can discover the specialist and delegate work through A2A. Its internal MCP tool remains part of the agent’s implementation. [35]

**AWS demonstrates the same architectural separation:** Its Strands A2A example connects an HR agent to an Employee Info agent, with the latter using an MCP tool to obtain employee data. This shows that the layering pattern is not specific to Google’s framework or cloud: the outside contract is agent collaboration, and the inside contract is tool access. [36]

Section references:
[34] Google purchasing-concierge codelab <https://codelabs.developers.google.com/intro-a2a-purchasing-concierge> Excerpt: "The pizza seller agent directly accepts our purchasing agent request, whereas the burger agent needs our confirmation before proceeding with our request and after we confirm the agent can rely the confirmation to the burger agent"
[35] Google Cloud’s ADK conversion example <https://cloud.google.com/blog/products/ai-machine-learning/unlock-ai-agent-collaboration-convert-adk-agents-for-a2a/> Excerpt: "This guide details the conversion of a standalone ADK/MCP agent into an A2A-compatible component and demonstrates how to build an orchestrator to manage such agents. The complete source code for all examples, along with official…"
[36] AWS Strands A2A example <https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-4-inter-agent-communication-on-a2a/> Excerpt: "For this example, let’s start with a basic architecture where a REST API exposes access to an HR agent which connects to an Employee Info agent: Architecture of the inter-agent system containing two agents (HR & Employee Info),…"

### When an adapter is actually necessary

**A bridge is needed when interfaces differ:** If an MCP-only consumer must invoke an A2A-only service as though it were a tool, something must translate between the contracts. Likewise, a gateway exposing agent discovery through MCP must decide how Agent Cards become MCP resources or tool descriptions. Direct internal MCP use by an A2A participant is a different case and needs no such translation.

**The mapping is semantic, not merely syntactic:** Converting JSON fields does not decide how a paused Task appears to an MCP client, whether a tool call should wait or return a handle, or how an artifact can be retrieved later. Those choices determine what behavior survives the boundary.

| A2A concept | Possible MCP projection | Decision the adapter must make |
|---|---|---|
| Agent skill | Namespaced tool description | Define a usable input and output contract |
| Message submission | Tool invocation | Preserve goal, identifiers, and caller context |
| Running Task | Task handle or deferred result | Select waiting, polling, and expiry behavior |
| Input-required state | Elicitation or continuation request | Preserve correlation and intervention semantics |
| Artifact | Tool content or resource reference | Preserve types, access, and retrieval |
| Security requirement | Incoming and outgoing credential flows | Bind caller authority to permitted delegation |

**Agent Cards do not generate complete tool schemas:** Because skills can be descriptive, an adapter may need a domain-specific argument contract or a generic message-based tool interface. Projecting a skill into a tool is therefore an architectural choice. A broad “research this issue” skill cannot automatically become a precise typed function merely by copying its name and description.

**A concrete bridge shows both feasibility and loss:** The `aarushitandon0/a2a-mcp-bridge` project targets MCP 2026-07-28 and A2A 1.0, discovers Agent Cards, projects skills as namespaced MCP tools, and translates calls, polling, and updates. It uses sealed opaque task handles while the remote A2A agent retains execution state. [37]

**Its documented boundaries are consequential:** That implementation requires an A2A JSON-RPC binding, provides only summarized artifact previews without follow-up detail retrieval, and does not implement RFC 8693 identity propagation through an agent chain. It also deliberately avoids answering A2A auth-required requests by forwarding credentials through model context. These choices demonstrate why a working adapter should not be assumed to preserve every native protocol behavior. [37]

**Proposed integration is a different evidence category:** IBM’s `mcp-context-forge` Issue #298 describes a gateway that would discover cards, convert skills into tools, manage A2A Tasks, map artifacts, and bridge authentication. As an issue with goals and acceptance criteria, it describes a proposed adapter boundary rather than a completed interoperability result. [38]

**Layering is established; translation needs its own contract:** Official documentation recommends co-use and describes selected tool-like skills being exposed through MCP. The integration pattern is complementary architecture; a bridge additionally needs an explicit agreement about lifecycle, artifacts, identity, and authorization. *From Glue-Code to Protocols* identifies precisely these cross-protocol semantic, security, privacy, and debugging concerns. [27][39]

**The integration takeaway is preservation of meaning:** Compose the protocols at their native boundaries when possible, and use a bridge only when the consumer needs another interface and the required semantics are deliberately preserved.

Section references:
[37] Community bridge implementation <https://github.com/aarushitandon0/a2a-mcp-bridge> Excerpt: "A bridge server that exposes Agent2Agent (A2A) remote agents as tools to Model Context Protocol (MCP) clients. It is built natively against the MCP 2026-07-28 specification revision and targets A2A 1.0. See SPEC-NOTES.md for the protocol research. A2A and MCP solve adjacent but different problems. A2A lets independent agents delegate work to one another over a…"
[38] IBM gateway proposal <https://github.com/IBM/mcp-context-forge/issues/298> Excerpt: "Goal: Enable the MCP Gateway to discover, register, and interact with A2A (Agent2Agent) servers by automatically converting A2A skills into MCP tools, providing seamless interoperability between MCP and A2A protocols Why now: The A2A protocol provides a standard for AI agent collaboration. By supporting A2A servers, the MCP Gateway becomes a bridge between MCP…"
[27] Official A2A–MCP comparison <https://a2a-protocol.org/latest/topics/a2a-and-mcp/> Excerpt: "The Agent2Agent (A2A) Protocol and the Model Context Protocol (MCP) address these distinct but highly complementary needs. Horizontal and Vertical Layers¶ One way to picture the two protocols is by the direction they connect in. MCP is vertical. It deepens a single agent. You can build an agentic system under one roof — one or more agents in a single applicatio…"
[39] Critical integration analysis <https://arxiv.org/abs/2505.03864> Excerpt: "We identify key challenges increased by the integration, including novel security vulnerabilities, privacy complexities, debugging difficulties across protocols, and the need for robust semantic negotiation mechanisms. In summary, A2A+MCP offers a vital architectural foundation, but fully realizing its potential requires substantial advancements to manage the c…"

## What is innovative about A2A?

### Its contribution is an integrated collaboration boundary

**A2A’s innovation is the coordinated package:** Agent Cards, opaque execution, native Tasks, interruption states, multimodal Parts, Artifacts, and update mechanisms reinforce one another. The resulting contract lets a caller discover a remote capability, delegate work, observe its progress, resolve an interruption, and retrieve outputs without adopting the remote agent’s framework. [24]

| A2A mechanism | What it changes | Comparison with MCP |
|---|---|---|
| Agent Cards | Combines collaborator identity and interaction requirements | MCP catalogs describe callable or readable primitives |
| Opaque collaboration | Preserves independent execution responsibility | MCP also hides implementation, but exposes capability invocations |
| Core Tasks | Makes work state addressable and observable | MCP Tasks are an opt-in extension |
| Asynchronous coordination | Separates work lifetime from connection lifetime | MCP also streams and supports asynchronous extensions |
| Intervention states | Makes clarification and authorization dependencies explicit | MCP supports elicitation and MRTR through another model |
| Webhook updates | Supports disconnected task observers | MCP’s broader push composition remains roadmap work |
| Multimodal Parts | Carries mixed content within one interaction model | MCP also handles structured content and optional UI capabilities |
| Artifacts | Separates deliverables from conversational updates | MCP returns tool content and resource-oriented results |
| Enterprise security declarations | Makes connection requirements discoverable | MCP supplies its own HTTP authorization model |
| Vendor-neutral bindings and governance | Reduces dependence on one runtime or framework | Both protocols pursue cross-vendor interoperability |

**The value lies between features:** A capability description alone does not solve delayed work. A task ID alone does not tell a caller how to authenticate. A webhook alone does not explain whether a task is complete or waiting for input. A2A’s contribution is to put those pieces around the same externally observable unit of work.

**This is not an intelligence upgrade:** A2A does not improve a model’s reasoning merely by connecting it to another agent. It improves the infrastructure through which responsibilities are delegated and outcomes are observed. Additional participants can still misunderstand goals, produce poor results, or pass work among themselves without progress; communication compatibility does not establish collaborative competence.

Section references:
[24] A2A roles and concepts <https://a2a-protocol.org/latest/specification/> Excerpt: "- A2A Server (Remote Agent): An agent or agentic system that exposes an A2A-compliant endpoint, processing tasks and providing responses. - Agent Card: A JSON metadata document published by an A2A Server, describing its identity, capabilities, skills, service endpoint, and authentication requirements. - Message: A communication turn between a client and a remote agent, having a ( user or agent ) and containing one or moreParts - Task: The fundamental unit of work managed by A2A, identified by a unique ID."

### Describable capabilities without shared internals

**Agent Cards make opaque services usable:** A remote agent can reveal enough about its purpose, input/output modes, endpoint, and security requirements for a caller to select it while keeping internal prompts, memory, tools, and implementation private. That is particularly useful across teams or organizations that cannot adopt one common runtime or disclose proprietary workflows. [24]

**Opacity changes the integration relationship:** The caller integrates with an outcome-oriented participant rather than reconstructing its workflow from individual tools. A KYC specialist, for example, can own its combination of verification services and policies. The orchestrator asks for permitted verification work and receives the agreed output, rather than needing the specialist’s complete tool configuration.

**Opacity also creates an evaluation obligation:** Because internal execution is hidden, clients need clear output contracts, observable task states, and an appropriate basis for trusting results. The practical benefit changes if the business process requires inspecting every intermediate decision or using a shared execution environment. A2A supports an opaque boundary; it does not require every application to prefer one.

Section references:
[24] A2A roles and concepts <https://a2a-protocol.org/latest/specification/> Excerpt: "- A2A Server (Remote Agent): An agent or agentic system that exposes an A2A-compliant endpoint, processing tasks and providing responses. - Agent Card: A JSON metadata document published by an A2A Server, describing its identity, capabilities, sk…"

### Native work continuity and human intervention

**Tasks standardize unfinished work:** In a heterogeneous system, “the server is not done” should not require every caller to understand a different custom status endpoint and continuation token. A2A gives that situation a common model: the Task remains addressable, its state is observable, and the client can retrieve or subscribe to updates. [10]

**Interruption becomes part of normal execution:** Input-required and auth-required distinguish a paused workflow from an operational failure. A remote agent can ask for a document, clarification, or additional authorization while retaining the task’s identity. This is useful for human-in-the-loop business processes where completion depends on decisions outside the model.

**MCP’s evolution changes the novelty comparison:** MCP now supports MRTR and optional Tasks, so these capabilities are not exclusive in every form. A2A’s distinction is that tracked inter-agent work sits in its core collaboration model. MCP retains a leaner capability-access core and adds specialized behaviors through explicitly supported extensions. [2]

**Push is a coordination option, not a new invention:** Webhooks and SSE predate A2A. Their significance here is that they carry standardized task status and artifact updates tied to the same lifecycle. The innovation claim is strongest at the integration level, not at the level of inventing server callbacks or streamed HTTP events.

Section references:
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "- A2A Server (Remote Agent): An agent or agentic system that exposes an A2A-compliant endpoint, processing tasks and providing response…"
[2] MCP specification <https://modelcontextprotocol.io/specification/2026-07-28> Excerpt: "Beyond the core protocol, MCP defines optional extensions that add modular, specialized, or experimental functionality. Extensions are…"

### Multimodal deliverables and enterprise compatibility

**Artifacts make outputs more than conversation:** A task can return a document, image, structured data, or a combination of Parts. An incremental artifact update can represent a developing deliverable while a status Message explains what is happening. This is more useful to downstream software than treating every output as an untyped paragraph in a chat transcript. [24]

**Multimodality is not an exclusive dividing line:** MCP’s ecosystem also supports structured results, resources, and interactive interfaces through MCP Apps, including forms, charts, and video players. A2A’s distinctive packaging is heterogeneous content inside agent Messages and task Artifacts. “A2A supports media, MCP supports only text” would misdescribe the alternatives. [2]

**Enterprise compatibility favors existing standards:** A2A separates its canonical model from abstract operations and concrete bindings. Its Protocol Buffer schema supplies a common definition, while JSON-RPC, gRPC, and HTTP+JSON/REST expose that model through different infrastructure choices. This allows common agent semantics without requiring every organization to adopt the same wire stack. [10]

**Neutrality reduces one kind of lock-in:** An agent built with LangChain, LangGraph, CrewAI, Semantic Kernel, ADK, Strands, or a custom runtime can participate if its external implementation is compatible. A2A does not replace those frameworks or automatically make every framework-generated agent interoperable. The boundary is standardized; each participant still has to implement it correctly.

**Historical priority needs a narrower claim:** Agent communication long predates A2A: the comparative literature discusses KQML from 1994 and FIPA-ACL from 2002. Calling an A2A feature historically unprecedented would require a dated, feature-by-feature comparison with earlier agent protocols and contemporaneous MCP revisions. The supported judgment is that A2A integrates a useful web-oriented collaboration boundary, not that it invented agent delegation, asynchronous work, or capability descriptions. [17]

**The innovation takeaway is coherent coordination:** A2A’s strongest contribution is a shared external model for heterogeneous agents to discover, delegate, pause, monitor, and deliver work while remaining independently implemented.

Section references:
[24] A2A roles and concepts <https://a2a-protocol.org/latest/specification/> Excerpt: "- Artifact: An output (e.g., a document, image, structured data) generated by the agent as a result of a t…"
[2] MCP specification <https://modelcontextprotocol.io/specification/2026-07-28> Excerpt: "- MCP Apps: Interactive UI elements (charts, forms, video players) rendered inline within conversations Se…"
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "While the A2A protocol provides three standard bindings (JSON-RPC, gRPC, and HTTP+JSON/REST), implementers…"
[17] MCP interaction model <https://arxiv.org/html/2607.23884v1> Excerpt: "We evaluate an MCP-based and an A2A-based multi-agent implementation of the same software engineering task…"

## The specific problems A2A is designed to address

### From fragmented integrations to shared contracts

**The officially stated problem is fragmentation:** Google’s launch announcement describes agents working across siloed data systems and applications, with different vendors and frameworks obstructing collaboration. AWS similarly describes custom integration code for each agent pairing as a source of development and maintenance overhead. A2A targets those communication and coordination boundaries. [1][36]

| Problem | A2A mechanism | Practical effect |
|---|---|---|
| Vendor and framework fragmentation | Shared data model, operations, bindings | Reduces interface-specific integration work |
| Finding a suitable remote capability | Agent Cards and registry hooks | Makes endpoint and skill descriptions machine-readable |
| Incompatible interaction requirements | Modes, versions, interfaces, extensions | Makes compatibility checks explicit |
| Stateful or delayed execution | Task IDs, states, retrieval | Keeps unfinished work addressable |
| Clarification and human approval | Input-required and auth-required states | Represents intervention without declaring failure |
| Cross-organization collaboration | Opaque remote-agent boundary | Preserves separate implementations and responsibilities |
| Identity and access requirements | Security declarations and scoped enforcement | Connects collaboration to existing security infrastructure |
| Mixed inputs and outputs | Parts and Artifacts | Supports media and structured deliverables |
| Agent-versus-tool confusion | Task-oriented boundary alongside MCP | Separates delegation from capability invocation |

**Standardization moves rather than abolishes work:** A common protocol can replace custom decisions about request envelopes, state names, result formats, and update mechanisms. It does not remove business-specific agreements about what a task means, what constitutes acceptable evidence, or which actions a collaborator may perform. Integration becomes more reusable at the communication layer while domain semantics remain important.

**Capability negotiation reduces avoidable mismatches:** A caller can reject an unsuitable interface or unsupported required extension before relying on it. That is more dependable than discovering halfway through a workflow that the remote service cannot accept the input modality or provide the expected update path. The conclusion changes when declared capabilities are inaccurate, which is why compatibility testing matters.

**Expected benefits should remain labeled:** Google and the Linux Foundation associate A2A with higher autonomy, improved productivity, reduced long-term integration cost, and less vendor lock-in. These are intended or project-claimed consequences of standardization, not measured causal savings established by the protocol specification. [1][40]

Section references:
[1] Google’s launch announcement <https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/> Excerpt: "Arize AI is proud to partner with Google as a launch partner for the A2A interoperability protocol, advancing seamless, secure interaction across AI agents as part of Arize's co…"
[36] AWS Strands A2A example <https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-4-inter-agent-communication-on-a2a/> Excerpt: "Without a standardized protocol, each agent pairing required custom integration code, leading to excessive development overhead and maintenance complexity. This created siloed A…"
[40] Linux Foundation’s milestone account <https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year> Excerpt: "SAN FRANCISCO – April 9, 2026 – The A2A (Agent-to-Agent) Protocol project, hosted by the Linux Foundation, today announced major adoption milestones at its one-year mark, with m…"

### Concrete use cases reveal the boundary

**The auto-repair example separates jobs clearly:** A Shop Manager delegates to a Mechanic through A2A; the Mechanic uses MCP for a diagnostic scanner, repair-manual database, and platform lift. When it needs a part, it communicates with a Parts Supplier agent through A2A. Diagnosis tools expose discrete operations, while the supplier interaction involves a separate participant’s capability and decision-making. [27]

**Hiring illustrates multi-system responsibility:** Google’s launch example has a hiring manager’s agent work with specialist agents to source candidates, arrange further interviews, and facilitate background checks. A2A supplies the communication model across those participants. It does not decide whether a background check is lawful, whether candidate data may be shared, or how hiring judgments should be governed. [1]

| Named use case | Inter-agent responsibility | Tool or data responsibility | Evidence type |
|---|---|---|---|
| Hiring and background checks | Coordinate sourcing, interviews, checks | Access permitted recruiting records | Official illustrative workflow |
| Financial advisor | Coordinate retrieval, analysis, recommendation, execution | Obtain market and account data | Official reference architecture |
| Research assistant | Coordinate planning, research, evaluation, composition | Retrieve sources and documents | Official reference architecture |
| Supply-chain optimization | Coordinate warehouse, shipment, and supplier agents | Query inventory and logistics systems | Official reference architecture |
| Inventory management | Resolve stock needs across participants | Read and update authorized inventory data | Architectural example |

**These examples share a responsibility pattern:** The financial-advisor, research-assistant, and supply-chain architectures divide broad work among specialized participants, while databases, APIs, and files remain capabilities used to execute those responsibilities. Google Cloud explicitly assigns A2A to inter-agent communication and MCP to agent-to-tool interaction in its reference architecture. [41]

**Cross-organization work makes the distinction sharper:** A sales agent can use MCP to inspect internal inventory and A2A to ask a logistics vendor’s supply-chain agent for help. The vendor can keep its routing logic and internal tools private while exposing a permitted collaboration contract. Separate authentication, error handling, and auditing remain necessary across the two boundaries. [3]

**The problem-solving takeaway is bounded interoperability:** A2A standardizes how independently controlled participants communicate about work; it does not, by itself, supply shared business meaning, universal discovery, delegated trust, or transactional correctness.

Section references:
[27] Official A2A–MCP comparison <https://a2a-protocol.org/latest/topics/a2a-and-mcp/> Excerpt: "It uses A2A to talk to a Parts Supplier agent and order the part. For example, the Mechanic agent might ask, Do you have part 12345 in stock for a Toyota Camry 2018? Order pro…"
[1] Google’s launch announcement <https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/> Excerpt: "SAP is committed to collaborating with Google Cloud and the broader ecosystem to shape the future of agent interoperability through the A2A protocol—a pivotal step toward enab…"
[41] Google Cloud multi-agent architecture <https://cloud.google.com/architecture/multiagent-ai-system>
[3] A2A launch history <https://authzed.com/learn/agent-to-agent-communication-guide-google-a2a-protocol> Excerpt: "A sales representative agent uses MCP to check internal inventory databases, and then uses A2A to message a distinct supply chain agent owned by your logistics vendor. The rea…"

## Implementation evidence and deployment judgment

### What named implementations establish

**A2A has moved beyond announcement-stage artifacts:** The Linux Foundation reported more than **150 supporting organizations on 9 April 2026**, alongside cloud integrations and production use across supply chain, financial services, insurance, and IT operations. The official repository inventory lists SDK targets for **Python, Go, JavaScript, Java, .NET, and Rust**. These are dated project-reported adoption milestones and concrete implementation artifacts. [40][15]

**Platform support is broader than one framework:** The Linux Foundation identifies Google Cloud, Microsoft Foundry and Copilot Studio, and Amazon Bedrock AgentCore integrations. AWS also reports A2A support in Strands and production use of Strands by teams including Amazon Q Developer, AWS Glue, and VPC Reachability Analyzer. The latter is evidence of framework production use, not proof that every named product uses every A2A feature in production. [40][36]

| Implementation | Protocol surface | Concrete evidence | What it demonstrates |
|---|---|---|---|
| Strands Agents | MCP and A2A | AWS’s HR/Employee Info example | Layered tool use and agent communication |
| WildFly A2A Jakarta | A2A 1.0 and 0.3; three bindings | 10 September 2026 release | Deployable enterprise integration |
| Archie Archivist | A2A 0.3 over JSON-RPC | Elastic newsroom tutorial | Named discovery and search implementation |
| MCP C# SDK v2 | MCP 2026-07-28; optional Tasks | Maintainer release explanation | Stateless requests and extension-based workflows |
| MCP Python SDK v2.0.0 | MCP 2026-07-28 and earlier revisions | Official release notes | Multi-revision support with feature-specific boundaries |

**WildFly provides a concrete stateful deployment example:** Its A2A Jakarta `1.0.0.Final` release supports the 1.0 specification over JSON-RPC, gRPC, and HTTP+JSON/REST, with a compatibility layer for 0.3 clients. Its enterprise example runs an agent across **two WildFly nodes**, using JPA-backed task and push-notification stores plus a Kafka-backed replicated queue manager. That shows how task state and live events can be retained across a load-balanced deployment. [42]

**Optional capabilities vary in real examples:** Elastic’s Archie Archivist advertises protocol version `0.3.0` and JSON-RPC, but its card sets streaming, push notifications, and state-transition history to false. It demonstrates an A2A discovery and search boundary without demonstrating every feature discussed in the specification. [43]

**MCP also has broad implementation support:** Its SDK documentation lists TypeScript, Python, C#, Go, Rust, and Ruby as Tier 1, Java as Tier 2, and Swift, PHP, and Kotlin as Tier 3. Client support includes major assistants and development environments. However, extension support remains implementation-specific: the Python SDK v2.0.0 release explicitly excludes the redesigned Tasks extension, while the C# SDK documents it as an opt-in package. [44][18][11]

Section references:
[40] Linux Foundation’s milestone account <https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year> Excerpt: "SAN FRANCISCO – April 9, 2026 – The A2A (Agent-to-Agent) Proto…"
[15] A2A SDKs and tooling <https://github.com/a2aproject/a2a-samples/> Excerpt: "Repository: a2a-python Category: SDK (Python) Description: Off…"
[36] AWS Strands A2A example <https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-4-inter-agent-communication-on-a2a/> Excerpt: "There are a number of areas we plan to work on so that A2A wor…"
[42] WildFly’s 10 September release <https://www.wildfly.org/news/2026/09/10/A2A-Jakarta-1-0-0-Final-is-released/> Excerpt: "A2A Jakarta supports version 1.0 of the A2A Protocol Specifica…"
[43] Elastic’s Archie Archivist implementation <https://www.elastic.co/search-labs/blog/a2a-protocol-mcp-llm-agent-newsroom-elasticsearch> Excerpt: "The card specifies the provider (Elastic) and the protocol ver…"
[44] MCP SDK inventory <https://modelcontextprotocol.io/docs/2026-07-28/sdk> Excerpt: "SDK: TypeScript Repository: modelcontextprotocol/typescript-sd…"
[18] Official Python SDK’s current wire model <https://github.com/modelcontextprotocol/python-sdk/releases> Excerpt: "Full Changelog: v2.0.0b2...v2.0.0rc1"
[11] MCP C SDK revision explanation <https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/> Excerpt: "There is exactly one place where v2 is not wire-compatible wit…"

### Compatibility tests measure particular surfaces

**A2A separates conformance from production quality:** Its TCK distinguishes mandatory protocol checks, declared-capability validation, quality checks, and optional features. Passing mandatory checks is not equivalent to demonstrating resilience, concurrency, secure deployment, or every optional capability. The project’s Integration Test Kit, or ITK, separately runs nightly interoperability tests between SDK peers and conformance tests across the standard bindings. [29][45]

**A dated Rust result illustrates test alignment:** The community `tomtom215/a2a-rust` implementation reports **88 passing and 4 failing out of 92 measured MUST requirements on 1 September 2026**, against a specified TCK revision. Its maintainer attributes the four failures to differences between the TCK’s v1.0.0 snapshot and later error mappings. This is an implementation- and suite-specific result, not an ecosystem-wide pass rate. [46]

**Release alignment can explain apparent defects:** The same report documents HTTP and gRPC error-mapping differences between v1.0.0 and v1.0.1, including the HTTP status associated with a non-cancelable Task. This makes a practical point: an SDK, its test suite, and its target specification need matching version assumptions. A red test can reveal an implementation defect or a stale expectation; the underlying request and expected semantics decide which.

Section references:
[29] A2A capability validation <https://github.com/a2aproject/a2a-tck/blob/main/docs/SDK_VALIDATION_GUIDE.md> Excerpt: "Concurrency test failed - only 2/5 parallel requests succeeded Issue: Poor concurre…"
[45] Nightly interoperability dashboard <https://a2aproject.github.io/a2a-itk/dashboard/> Excerpt: "Nightly results for the Agent2Agent (A2A) protocol SDKs, over the JSON-RPC, gRPC an…"
[46] Rust SDK’s dated TCK findings <https://github.com/tomtom215/a2a-rust/blob/main/docs/official-tck-findings.md> Excerpt: "the tally is 88 MUST passing and 4 failing, not 92 and 0. Nothing in this SDK chang…"

### MCP readiness is a revision-migration proxy

**The September probe measures four signals:** On **13 September 2026**, RoninForge reported probing **31,538 registered MCP servers**, with **11,929 reachable through its keyless initialization method**. It then checked four signals associated with the 2026-07-28 revision: server discovery, handshake-free requests, session independence, and routing-header enforcement. The results describe that reachable population and those tests. [47]

| Probe classification | Servers | Share of 11,929 reachable | Meaning |
|---|---:|---:|---|
| Passes all four signals | 31 | 0.3% | Meets the probe’s complete readiness test |
| Needs migration | 10,000 | 83.8% | Responds through older behavior; lacks new requirements |
| At risk | 1,898 | 15.9% | Uses a removed or deprecated surface |
| Total classified | 11,929 | 100.0% | Reachable runtime population |

**The denominator controls the interpretation:** The remaining **19,609 registered servers** were package-only, authentication-gated, or down and received no runtime classification. They should not be counted as failures. The probe also found **7,555 reachable servers, or 63.3%, accepting handshake-free calls**, showing that one central architectural change was more widely supported than the complete four-signal combination. [47]

**Migration readiness is not basic usefulness:** A server operating under an earlier MCP revision can still serve compatible clients. The four-signal result measures adoption of the newer request model, not whether the server performs its business function, handles data securely, or offers a particular extension. It is therefore a useful migration proxy rather than a complete maturity score.

**The two ecosystems cannot be ranked from these counts:** A2A supporting organizations, SDK test results, and named deployments measure different populations from MCP registry endpoints and runtime revision probes. Comparing “150 organizations” with “31 ready servers” would confuse adoption, implementation, and conformance units. Deployment choice should instead depend on the actual SDKs, endpoints, bindings, and features in the intended workflow.

A2A had more than 150 supporting organizations by 9 April 2026, while 31 of 11,929 reachable MCP servers (0.3%) passed all four 2026-07-28 readiness signals on 13 September 2026; 10,000 (83.8%) needed migration and 1,898 (15.9%) were at risk.

Section references:
[47] RoninForge’s dated readiness probe <https://roninforge.org/data/state-of-mcp/spec-readiness/> Excerpt: "On 2026-09-13 we probed every one of the 31,538 servers in the official registry against the Model Context Protocol's 2026-07-28 revision. Of the 11,929 reachable through a conformant keyless initialize, 31 pass all four required-conformance signals, against 29 in the 2026-09-09 census. That is 0.3% of the reachable population, so the honest reading is that migration has started, not that it has progressed. The counterweight is real either way: 63.3% already tolerate han…"

### Reliability and the final selection

**Webhooks require careful delivery language:** A2A describes push behavior in at-least-once terms, but the mandatory server guarantee is at least one delivery attempt per configured webhook. Retries can be implemented, duplicates can occur, and clients acknowledge receipt with HTTP 2xx. This is neither guaranteed eventual delivery under every failure nor exactly-once execution of the underlying business action. [10]

**Cancellation is not automatic rollback:** A client can request task cancellation, but success depends on the task’s stage and the server’s ability to stop it. An already executed payment, shipment, or external mutation may require separate compensating business logic. Likewise, retrying a submission after a timeout needs an intentional duplicate-handling policy; an addressable Task does not alone make every side effect idempotent. [10]

**Neither protocol replaces workflow infrastructure:** Durable queues, back-pressure, dead-letter handling, storage, tracing, and application authorization may still be needed. Oracle’s queue-backed document-processing example is a useful counterexample: where the model is simply a worker processing queued documents, adding an agent protocol does not necessarily improve the job. [30]

| Situation | Preferred boundary | Why |
|---|---|---|
| An application needs discoverable tools and context | MCP | Standardizes capability access |
| Independent agents need tracked delegation | A2A | Standardizes collaboration and work lifecycle |
| Specialists collaborate and use external tools | A2A plus MCP | Preserves both native boundaries |
| An MCP-only client must consume an A2A service | Explicit adapter | Translates the required semantics |
| A fixed background worker needs delivery and retries | Queue or ordinary service interface | Infrastructure reliability is the primary requirement |

**The remaining design questions are concrete:** Registry behavior, delegated identity, authorization narrowing, cross-protocol tracing, artifact access, and extension composition determine how well a particular deployment works. MCP’s August 2026 roadmap explicitly prioritizes agentic messaging composition, workload identity, delegation, and transport hardening; A2A’s published roadmap likewise identifies registry consolidation, expanded interoperability testing, and deployment practices. These are directions of work, not promises that every deployment already includes them. [48][40]

**How to read the evidence:** Protocol behavior above comes primarily from specifications and schemas; codelabs and samples establish demonstrated patterns; project announcements establish reported adoption; independent studies and probes establish narrower observations. Dates, revisions, and measurement populations remain attached to their figures. The 51.2% code increase is a calculation from the study’s reported source-line counts, not an ecosystem estimate, and its implementation comparison is not a universal performance ranking.

**The final architectural judgment is straightforward:** Use MCP to expose capabilities, A2A to delegate work across independently managed agents, and both when the system genuinely contains both relationships. A2A matters because it makes collaboration a recognizable, trackable protocol contract—not because it replaces tools, guarantees trust, or makes the participating agents inherently smarter.

Section references:
[10] A2A versioning and Agent Cards <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> Excerpt: "The server will attempt to cancel the task, but success is not guaranteed (e.g., the task might have already completed or failed, or cancellation might not be s…"
[30] Oracle’s shared-state example <https://blogs.oracle.com/developers/the-agent-communication-matrix-when-mcp-a2a-and-plain-rest-each-win> Excerpt: "Simple infrastructure still works well for many tasks. Message queues provide at-least-once delivery, dead-letter queues, and automatic back-pressure. Adding th…"
[48] MCP roadmap <https://modelcontextprotocol.io/development/roadmap> Excerpt: "Core Maintainers: Caitie McCaffrey, Clare Liguori, Peter Alexander Agentic workloads need messaging patterns beyond request and response: work that runs for min…"
[40] Linux Foundation’s milestone account <https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year> Excerpt: "Looking ahead, the A2A roadmap includes an interoperability specification, consolidation of efforts for registry and expanded testing and tooling, security and…"

## References

[1] <https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/> Google’s launch announcement; Google’s problem statement; Google’s expected benefits; Google’s Agentspace hiring example
[2] <https://modelcontextprotocol.io/specification/2026-07-28> MCP specification; MCP architectural roles; MCP features; MCP resources and context; MCP prompt definition; MCP extensions; MCP trust and safety principles; MC…
[3] <https://authzed.com/learn/agent-to-agent-communication-guide-google-a2a-protocol> A2A launch history; Delegated authorization analysis; Sales and logistics example
[4] <https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents> Linux Foundation project announcement
[5] <https://github.com/modelcontextprotocol/modelcontextprotocol/releases> MCP release history; MCP stable releases
[6] <https://en.wikipedia.org/wiki/Model_Context_Protocol> Public launch chronology
[7] <https://www.anthropic.com/news/model-context-protocol> Anthropic’s introduction
[8] <https://github.com/a2aproject/A2A/releases> A2A release history
[9] <https://github.com/a2aproject/A2A/releases/tag/v1.0.1> A2A v1.0.1 release; v1.0.1 changes
[10] <https://github.com/a2aproject/A2A/blob/main/docs/specification.md> A2A versioning and Agent Cards; A2A discovery mechanisms; A2A capability and interface declarations; A2A task and context semantics; A2A messages and artifacts…
[11] <https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/> MCP C# SDK revision explanation; MCP C# SDK scaling explanation; Microsoft’s MRTR explanation; MCP HTTP routing behavior; C# extension packaging
[12] <https://github.com/a2aproject/A2A/blob/v1.0.1/docs/specification.md> Versioned specification document
[13] <https://github.com/a2aproject/A2A/blob/main/GOVERNANCE.md> A2A governance
[14] <https://modelcontextprotocol.io/community/governance> MCP governance
[15] <https://github.com/a2aproject/a2a-samples/> A2A SDKs and tooling; A2A sample security warning; A2A SDK inventory
[16] <https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro> MCP-supported applications
[17] <https://arxiv.org/html/2607.23884v1> MCP interaction model; MCP primitive discovery; MCP tool model; Implementation-grounded comparison; Comparative implementation study; Study methods and counts;…
[18] <https://github.com/modelcontextprotocol/python-sdk/releases> Official Python SDK’s current wire model; Python SDK release
[19] <https://arxiv.org/html/2505.02279v1> Primitive control boundaries
[20] <https://modelcontextprotocol.io/specification/2025-03-26/basic> MCP JSON-RPC foundation; Earlier MCP lifecycle
[21] <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports> 2026 transport model; MCP transport specification
[22] <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/> MCP explicit state handles
[23] <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization> MCP authorization specification
[24] <https://a2a-protocol.org/latest/specification/> A2A roles and concepts; A2A core data model; A2A Send Message operation; A2A opaque execution; A2A design principles; A2A opaque-agent design; A2A artifact and…
[25] <https://github.com/a2aproject/A2A/blob/v1.0.0/specification/a2a.proto> A2A Agent Card model; Canonical AgentSkill description; Canonical Part representations; A2A execution-mode definition; A2A task states; A2A security schemes
[26] <https://github.com/a2aproject/A2A/blob/main/docs/topics/streaming-and-async.md> A2A streaming and asynchronous guide; A2A asynchronous notifications
[27] <https://a2a-protocol.org/latest/topics/a2a-and-mcp/> Official A2A–MCP comparison; Official layering guidance; Official bridge discussion; Official auto-repair scenario
[28] <https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/> AWS’s MCP-based HR example
[29] <https://github.com/a2aproject/a2a-tck/blob/main/docs/SDK_VALIDATION_GUIDE.md> A2A capability validation; A2A TCK guidance
[30] <https://blogs.oracle.com/developers/the-agent-communication-matrix-when-mcp-a2a-and-plain-rest-each-win> Oracle’s shared-state example; Queue-backed architectural example
[31] <https://arxiv.org/html/2602.11327v2> Security study and experiment
[32] <https://tyk.io/learning-center/agent-protocols-a-complete-guide-to-mcp-a2a-and-acp/> Layered KYC example
[33] <https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/a2a_mcp/README.md> Official A2A/MCP travel sample; Sample discovery-to-runtime flow
[34] <https://codelabs.developers.google.com/intro-a2a-purchasing-concierge> Google purchasing-concierge codelab; Codelab implementation details
[35] <https://cloud.google.com/blog/products/ai-machine-learning/unlock-ai-agent-collaboration-convert-adk-agents-for-a2a/> Google Cloud’s ADK conversion example
[36] <https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-4-inter-agent-communication-on-a2a/> AWS Strands A2A example; AWS’s interoperability rationale; AWS’s Strands account
[37] <https://github.com/aarushitandon0/a2a-mcp-bridge> Community bridge implementation; Bridge security and feature boundaries
[38] <https://github.com/IBM/mcp-context-forge/issues/298> IBM gateway proposal
[39] <https://arxiv.org/abs/2505.03864> Critical integration analysis
[40] <https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year> Linux Foundation’s milestone account; Linux Foundation’s one-year report; Platform integration report; A2A roadmap context
[41] <https://cloud.google.com/architecture/multiagent-ai-system> Google Cloud multi-agent architecture
[42] <https://www.wildfly.org/news/2026/09/10/A2A-Jakarta-1-0-0-Final-is-released/> WildFly’s 10 September release
[43] <https://www.elastic.co/search-labs/blog/a2a-protocol-mcp-llm-agent-newsroom-elasticsearch> Elastic’s Archie Archivist implementation
[44] <https://modelcontextprotocol.io/docs/2026-07-28/sdk> MCP SDK inventory
[45] <https://a2aproject.github.io/a2a-itk/dashboard/> Nightly interoperability dashboard
[46] <https://github.com/tomtom215/a2a-rust/blob/main/docs/official-tck-findings.md> Rust SDK’s dated TCK findings
[47] <https://roninforge.org/data/state-of-mcp/spec-readiness/> RoninForge’s dated readiness probe; Probe population and individual signals
[48] <https://modelcontextprotocol.io/development/roadmap> MCP roadmap
