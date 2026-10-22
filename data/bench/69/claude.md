# A2A vs. MCP: How Google's Agent2Agent Protocol Relates to the Model Context Protocol (Status as of October 2026)

A2A and MCP are complementary layers, not rivals.\[1\] MCP (Anthropic, November 2024) standardizes how one AI application or agent connects *down* to tools, data and context. A2A (Google, April 2025) standardizes how independent, opaque agents connect *across* to one another to delegate stateful, possibly long-running tasks.\[2\] Since August 2026 both have sat under the same neutral home, the Linux Foundation's Agentic AI Foundation (AAIF). The line between them is real but blurrier than Google's launch messaging suggested, because MCP has since added task, elicitation and UI features that cover some of A2A's ground.\[3\] For most teams the right architecture is "MCP inside each agent, A2A between agents."\[4\] A2A is only worth adopting when agents really are independently owned, built or operated.\[5\]

## TL;DR

- **Different layers, shared DNA:** MCP connects an LLM application to tools and resources (a "vertical" link). A2A connects autonomous agents as peers (a "horizontal" link) using Agent Cards for discovery and a stateful Task lifecycle. Both use JSON-RPC 2.0 over HTTP, and both now live under the Linux Foundation's Agentic AI Foundation.
- **A2A's real innovations:** it treats a remote agent as an opaque collaborator rather than a function. Its building blocks are:
  - standardized discovery through a well-known Agent Card;
  - first-class long-lived Tasks with interrupted states (input-required, auth-required);
  - SSE streaming and webhook push notifications for work lasting hours or days;
  - modality/UX negotiation through typed Parts;
  - as of v1.0 (March 12, 2026), signed Agent Cards, multi-tenancy and three equivalent bindings (JSON-RPC, gRPC, HTTP+JSON/REST).
- **Practical verdict:** default to MCP for tool integration, since it is far more widely adopted. Add A2A at organizational, vendor or framework boundaries where agents must hand off multi-turn, asynchronous work without exposing their internals. Treat A2A's security story (optional card signing, no protocol-level prompt-injection defense) as something you must harden yourself.

## Key Findings

1. **Timeline in brief.**
   - **MCP:** announced November 25, 2024 (spec revision 2024-11-05); later revisions 2025-03-26, 2025-06-18, 2025-11-25 and 2026-07-28; donated to the newly formed AAIF on December 9, 2025.\[6\]
   - **A2A:** announced April 9, 2025; v0.2 on May 20, 2025; donated to the Linux Foundation June 23, 2025; v0.3.0 on July 30, 2025; absorbed IBM's ACP in August 2025; v1.0 on March 12, 2026; joined AAIF as a hosted project in August 2026.\[7\]
2. **Google positioned A2A as complementary from day one.**\[8\] The launch post called A2A "an open protocol that complements Anthropic's Model Context Protocol (MCP), which provides helpful tools and context to agents." The v1.0 announcement repeats the point: "MCP inside agents, A2A between agents."
3. **The protocols have converged in mechanics but not in purpose.**
   - \[9\]MCP's 2025-11-25 spec added an experimental Tasks primitive whose states (working, input_required, completed, failed, cancelled) closely mirror A2A's.
   - Its 2026-07-28 spec moved Tasks into an official extension, made the protocol stateless, and added MCP Apps (sandboxed iframe UIs).
   - A2A, for its part, now describes itself as "stateless, layered" and web-aligned.
4. **Adoption is asymmetric.**\[10\] MCP is the de facto tool-integration standard. In its December 9, 2025 donation post, Anthropic wrote that "there are now more than 10,000 active public MCP servers, covering everything from developer tools to Fortune 500 deployments." A2A's own figures are partner counts, not deployments:
   - more than 50 partners at launch;
   - more than 100 at the Linux Foundation handoff;\[7\]
   - "over 150 organizations" by August 2026.\[11\]
   A2A has native support in Google Cloud, AWS Bedrock AgentCore Runtime and Microsoft Azure AI Foundry/Copilot Studio.\[12\]
5. **The skeptics had a point in 2025, and less of one in 2026.**\[13\] Critics argued A2A was unnecessary fragmentation, and by September 2025 some were publishing "what happened to A2A?" post-mortems.\[14\]\[15\] Since then, the v1.0 release, the ACP merger, hyperscaler runtimes and the AAIF move have made the "A2A is dead" claim hard to sustain.\[5\] A2A's useful scope is still narrower than the launch hype implied.\[4\]

## Details

### 1. What each protocol is, who made it, and how it is governed

**MCP (Model Context Protocol).**
- **Origin:**\[16\] Anthropic engineers David Soria Parra and Justin Spahr-Summers created it, and Anthropic open-sourced it on November 25, 2024. The launch shipped the spec, Python and TypeScript SDKs, local server support in Claude Desktop, and reference servers for Google Drive, Slack, GitHub, Git, Postgres and Puppeteer.\[17\]\[18\]\[19\]
- **Version naming:** the first spec revision is dated 2024-11-05. MCP versions are named by the date of the last backward-incompatible change, so this date precedes the public launch.\[6\]
- **Adoption:**\[20\] on March 26, 2025, OpenAI CEO Sam Altman wrote that "people love MCP and we are excited to add support across our products." On April 9, 2025, Google DeepMind CEO Demis Hassabis said Google would be "supporting it for our Gemini models and SDK."
- **Governance:**
  - On December 9, 2025, Anthropic donated MCP to the Agentic AI Foundation, "a directed fund under the Linux Foundation, co-founded by Anthropic, Block and OpenAI, with support from Google, Microsoft, AWS, Cloudflare and Bloomberg."\[21\]\[22\]\[23\]
  - The MCP blog stressed that "MCP's maintainer structure stays the same" and that the Linux Foundation "will not dictate the technical direction of MCP."
  - At the one-year anniversary the project reported 58 maintainers.
- **The MCP Registry:**\[20\] an open catalog and API of MCP servers. It launched in preview on September 8, 2025, backed by Anthropic, GitHub, PulseMCP and Microsoft. The official registry README records that on October 24, 2025 "the Registry API has entered an API freeze (v0.1)."

**A2A (Agent2Agent).**
- **Launch:**\[8\] Google announced A2A on April 9, 2025 at Google Cloud Next, "with support and contributions from more than 50 technology partners."\[24\]
  - Technology partners included Atlassian, Box, Cohere, Intuit, LangChain, MongoDB, PayPal, Salesforce, SAP, ServiceNow, UKG and Workday.
  - \[8\]Service providers included Accenture, BCG, Capgemini, Cognizant, Deloitte, HCLTech, Infosys, KPMG, McKinsey, PwC, TCS and Wipro.
  - Google said it was "working with partners to launch a production-ready version of the protocol later this year." In fact v1.0 did not arrive until March 2026.
- **Linux Foundation handoff:** on June 23, 2025 the Linux Foundation launched the Agent2Agent project.\[7\]
  - Founding participants were AWS, Cisco, Google, Microsoft, Salesforce, SAP and ServiceNow.
  - Google transferred the spec, SDKs and developer tooling, and more than 100 companies supported the protocol by then.
- **Steering committee:**\[3\] the A2A Technical Steering Committee has representatives from eight companies: AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP and ServiceNow.\[12\]
- **AAIF move:** in August 2026 A2A moved inside the Linux Foundation structure to become an AAIF project.\[2\]
  - \[11\]A2A's own blog says it was "accepted as a Growth Stage project."
  - On the date: Axios (Ina Fried) and Forbes (Janakiram MSV) both report an August 17, 2026 AAIF announcement. August 20 appears only in smaller blogs, and the A2A blog's own post is dated August 27.
- **What the AAIF move does not do:** it does not merge the protocols. A2A and MCP keep separate maintainers and steering structures.

### 2. A2A's core architecture

- **Actors.**
  - \[8\]A **client agent** "is responsible for formulating and communicating tasks."
  - A **remote agent** "is responsible for acting on those tasks."
  - The remote agent is an **A2A server** exposing an HTTP endpoint. A user or the user's agent sits upstream of the client.
- **Agent Card (discovery).**
  - \[25\]An Agent Card is a JSON metadata document describing an agent's identity, skills, endpoint(s), supported modalities, capabilities (streaming, push notifications) and authentication requirements.\[26\]
  - It was originally served at `/.well-known/agent.json`. v0.3.0 (July 30, 2025) renamed this to `/.well-known/agent-card.json` as a breaking change, and v1.0 registered the path as an IANA well-known URI.
  - Agents can also offer an authenticated "extended" card containing details not exposed publicly.\[27\]
  - In v1.0 the card lists `supportedInterfaces[]`, each with its own `protocolBinding` (JSONRPC, GRPC, HTTP+JSON) and `protocolVersion`. This lets one agent serve v0.3 and v1.0 clients at the same time.
- **Task (the unit of work).** A Task is "the stateful unit of work being processed by the A2A Server," with a unique ID and a lifecycle. v1.0 defines nine `TaskState` values:\[27\]\[28\]
  - `TASK_STATE_UNSPECIFIED`;
  - `SUBMITTED` and `WORKING`;
  - two *interrupted* states, `INPUT_REQUIRED` and `AUTH_REQUIRED`;\[29\]\[30\]
  - four *terminal* states, `COMPLETED`, `FAILED`, `CANCELED` and `REJECTED`.\[29\]\[30\]

  Terminal tasks cannot restart; follow-up work must start a new task within the same `contextId`.\[29\]\[30\] v1.0 switched enum values from kebab-case (`input-required`) to SCREAMING_SNAKE_CASE for ProtoJSON compliance.\[31\]\[32\]
- **Messages and Parts.**
  - \[33\]A Message is one conversational turn with a role (user/agent) and one or more Parts.\[26\]
  - Parts carry text, files (by URL or bytes) or structured JSON data, each typed with a media type.
  - v1.0 dropped the `kind` discriminator in favor of identifying the part type by which JSON member is present (e.g., `{"text": ...}`).
- **Artifacts.** These are the outputs of a task (documents, images, structured data), streamed or returned on completion.
- **Transports and asynchrony.**
  - \[34\]A2A started as JSON-RPC 2.0 over HTTP(S) with Server-Sent Events (SSE) for streaming.
  - gRPC support arrived in v0.3. v1.0 formally specifies three equivalent bindings (JSON-RPC 2.0, gRPC, HTTP+JSON/REST) and makes `a2a.proto` the single normative definition of the data model.
  - Clients can receive results "using polling, streaming, or webhooks." Push notifications are server-initiated HTTP POSTs to a client-supplied webhook, intended for long-running or disconnected scenarios.
- **Security.**
  - \[35\]Production traffic must use HTTPS/TLS.
  - Identity is not carried in the payload. Instead, the Agent Card declares security schemes modeled on OpenAPI's (API key, HTTP auth, OAuth 2.0, OpenID Connect).
  - v0.3 added mutual TLS (mTLS) and card signatures.
  - v1.0 added Agent Card signature verification using JWS (RFC 7515) and JSON canonicalization (RFC 8785). It also removed the OAuth implicit flow in favor of Authorization Code + PKCE.
- **Opacity.** The docs say agents "don't share internal memory, tools, or direct resource access with each other."\[2\] Agents collaborate "even when they don't share memory, tools and context."
- **Extensions.**\[36\] A2A supports versioned extensions, negotiated through an `A2A-Extensions` header, plus custom protocol bindings. Google and PayPal used this to build the Agent Payments Protocol (AP2) for agentic commerce.

### 3. MCP's core architecture

- **Participants.**
  - A **host** is the AI application, e.g., Claude Desktop, ChatGPT, VS Code or a custom agent.\[21\]
  - The host creates one **client** per connection.\[17\]
  - Each client talks to an MCP **server**, a program exposing a system's capabilities.\[21\]
- **Server primitives.**
  - **Tools** are model-invoked functions described by JSON Schema; since 2026-07-28 they support full JSON Schema 2020-12.
  - **Resources** are application-controlled data addressed by URI.
  - **Prompts** are user-selected templates.
- **Client primitives.**
  - **Sampling:** the server asks the host's LLM to generate text.
  - **Roots:** filesystem/URI boundaries.
  - **Elicitation:** the server asks the user for structured input; added in 2025-06-18, with URL-mode elicitation added in 2025-11-25.\[37\]\[38\]
  - The 2026-07-28 spec deprecates roots, sampling and logging (annotation-only, with at least 12 months before possible removal). The recommended replacements are, respectively, tool parameters, direct LLM provider APIs, and stderr/OpenTelemetry.
- **Transports.**
  - stdio for local servers.
  - The original HTTP+SSE transport, replaced by **Streamable HTTP** in 2025-03-26.
  - In 2026-07-28 the `initialize` handshake and the `Mcp-Session-Id` header were removed. Each request is now self-contained, carrying `Mcp-Method`/`Mcp-Name` headers, and a server can run "behind a plain round-robin load balancer."
- **Capability negotiation.** Before 2026-07-28 this happened during `initialize`. Now client capabilities travel in `_meta` on each request, and a new `server/discover` method returns server capabilities.
- **Authorization.**
  - OAuth 2.1 arrived in 2025-03-26.\[39\]
  - 2025-06-18 classified MCP servers as OAuth Resource Servers (RFC 9728 protected-resource metadata), required Resource Indicators (RFC 8707), and removed JSON-RPC batching.\[6\]\[40\]
  - 2025-11-25 made Client ID Metadata Documents the default registration path and added machine-to-machine client credentials and enterprise Cross App Access.
  - 2026-07-28 requires validating the `iss` parameter (RFC 9207), among six authorization-hardening proposals.
- **Long-running work.**
  - \[9\]2025-11-25 introduced experimental Tasks, which let any request become "call-now, fetch-later."\[38\]
  - 2026-07-28 moved Tasks to an official extension (`tasks/get`, `tasks/update`, `tasks/cancel`; `tasks/list` removed). Anyone who built on the experimental API must migrate.

### 4. Side-by-side comparison

| Dimension | MCP (Model Context Protocol) | A2A (Agent2Agent) |
|---|---|---|
| Core purpose | Connect an LLM app/agent to tools, data, prompts ("vertical") | Let independent agents discover each other and collaborate as peers ("horizontal") |
| Creator / launch | Anthropic; announced Nov 25, 2024 (spec 2024-11-05) | Google; announced Apr 9, 2025 at Cloud Next |
| Governance (Oct 2026) | AAIF (Linux Foundation directed fund), donated Dec 9, 2025; maintainer structure unchanged | Linux Foundation project since Jun 23, 2025; AAIF project since Aug 2026; 8-company TSC |
| Current version | 2026-07-28 (stateless core, extensions, MCP Apps) | v1.0.0 (Mar 12, 2026); v0.3 still supported via dual-version Agent Cards |
| Participants | Host → client → server (tool provider) | Client agent ↔ remote agent (opaque A2A server) |
| Message format | JSON-RPC 2.0 | JSON-RPC 2.0, plus gRPC (Protocol Buffers) and HTTP+JSON/REST bindings; `a2a.proto` normative |
| Transport | stdio; Streamable HTTP (HTTP+SSE deprecated) | HTTPS required in production; SSE streaming; webhooks; gRPC over TLS |
| Discovery | Client configuration; official MCP Registry (preview since Sep 2025); `server/discover` | Agent Card at `/.well-known/agent-card.json` (was `agent.json` pre-v0.3); signed cards in v1.0 |
| Unit of interaction | Tool call / resource read / prompt | Task with 9-state lifecycle, Messages, Parts, Artifacts, `contextId` |
| State model | Protocol now stateless; apps pass explicit handles; Tasks as extension | Stateful Tasks are core; protocol also designed to be web-stateless |
| Streaming / async | Streamable HTTP; Tasks extension; multi round-trip `InputRequiredResult` | SSE streaming, polling, push-notification webhooks; built for hours/days |
| Human-in-the-loop | Elicitation (form and URL modes) | `INPUT_REQUIRED` / `AUTH_REQUIRED` interrupted states |
| Auth | OAuth 2.1; servers as resource servers; RFC 8707/9728/9207; CIMD | OpenAPI-style schemes (API key, HTTP, OAuth2, OIDC), mTLS; JWS-signed cards; no identity in payload |
| UI | MCP Apps: server-rendered HTML in sandboxed iframes | UX negotiation via typed Parts (forms, iframes, audio/video) |
| Mental model | "USB-C port for AI": agent *uses* capabilities | Agents as *colleagues*: agent *partners* on tasks |
| Typical use | Query a DB, call an API, read files, run a workflow tool | Delegate to a vendor's or another team's agent; cross-org supply chain, HR, IT, commerce |

### 5. Connections, overlap and the skeptics

**The official framing.** The A2A docs call MCP "vertical" ("it deepens a single agent") and A2A "horizontal" ("it connects agents across that boundary"). They summarize the split as: "A2A is about agents *partnering* on tasks; MCP is more about agents *using* capabilities."\[2\]

The canonical example is an auto repair shop:
- The customer talks to a Shop Manager agent through A2A.\[2\]
- The Mechanic agent calls diagnostic-scanner and repair-manual tools through MCP.\[2\]
- The Mechanic orders parts from a supplier's agent through A2A.\[2\]

The docs also concede the overlap.\[2\]\[41\] An A2A server "can expose some skills as MCP-compatible resources" when they are "well-defined and can be called in a tool-like, stateless way."\[2\] Bridge patterns that wrap a remote A2A agent as a local MCP tool are common in practice.

**Shared foundations.**
- Both protocols use JSON-RPC 2.0 over HTTP and SSE.
- Both lean on OAuth.
- Both now have extension mechanisms.
- Both sit in AAIF next to sibling projects such as goose and AGENTS.md.

**The skeptical case.** In April 2025, a widely shared fka.dev essay argued A2A "represents an unnecessary addition" because "while the MCP protocol itself is stateless, MCP servers can be fully stateful." It also said discovery and other A2A concepts "could be standardized as MCP extensions."\[14\] A follow-up in September 2025, "What happened to Google's A2A?", claimed A2A "seems to have quietly faded into the background while... MCP has become the de facto standard." It attributed this to MCP's "developer-first" and bottom-up adoption versus A2A's "enterprise-first approach." Credal similarly argued that "A2A's implementation burden ended up outweighing its benefits."\[42\]

These are opinion pieces from MCP-ecosystem vendors and bloggers, not neutral measurements. They captured a real 2025 adoption gap, but they predate v1.0, the AWS AgentCore integration and the AAIF move.

**Has the gap narrowed?** Yes, and in both directions:
- \[43\]MCP's experimental Tasks (2025-11-25) explicitly targets "multi-agent systems" running "for minutes or hours."
- Elicitation gives MCP human-in-the-loop prompts.
- MCP Apps gives it iframe UIs, an idea A2A floated at launch.

What MCP still lacks:
- a standard for discovering *agents* (as opposed to servers) with opaque internals;
- a peer-to-peer conversational model in which either side can be an autonomous reasoner;
- signed, self-describing identity documents for cross-organization trust.

My reading is that the protocols are converging on shared *plumbing* (stateless HTTP, OAuth, task handles, extensions) while staying different in *semantics*. MCP models a capability that a host's LLM invokes. A2A models a counterpart that accepts, negotiates, pauses, rejects and reports on work.

**Anthropic's stance.**\[44\]\[45\] No direct public statement by Anthropic or MCP's core maintainers (David Soria Parra, Justin Spahr-Summers, Den Delimarsky) about A2A could be found. Anthropic was not among A2A's launch partners. The "complementary" framing comes from Google and the A2A project. On the Google side, Demis Hassabis said on launch day that "MCP is a good protocol and it's rapidly becoming an open standard for the AI agentic era." The AAIF's August 2026 announcement repeats the division of labor but quotes only AAIF and Google Cloud officials. Treat claims that "both camps agree" as inferred from AAIF co-membership rather than from Anthropic's own words.

### 6. What is genuinely innovative about A2A

Prior multi-agent work fell into three camps:
- frameworks such as LangGraph, CrewAI and AutoGen, which orchestrate agents *inside one process or codebase*;
- function-calling APIs, which reduce every collaborator to a typed function;
- MCP, which standardizes tool access.

A2A's distinctive contributions are:

1. **The opaque agent as a first-class peer.** The launch principle was enabling "true multi-agent scenarios without limiting an agent to a 'tool.'" Vendors can collaborate without revealing prompts, memory, tools or proprietary logic. This is what makes cross-vendor and cross-company delegation commercially workable.
2. **Standardized, signed discovery.**\[3\] A well-known Agent Card does for agents roughly what `robots.txt` or OpenID discovery documents did for the web. v1.0 adds cryptographic verification of "agent identity and metadata" before interaction.
3. **The Task as a long-lived, stateful contract.**\[8\] Interrupted states (`INPUT_REQUIRED`, `AUTH_REQUIRED`) and `REJECTED` let a remote agent say "I need more from you" or "I won't do this." Function calls cannot express this. Google designed A2A for "deep research that may take hours and or even days when humans are in the loop."
4. **Multiple delivery modes for asynchrony.** Results can arrive through SSE streams, polling or webhooks, so a client can disconnect and be called back later.
5. **Modality and UX negotiation.**\[8\] Typed Parts let agents negotiate "the user's UI capabilities–e.g., iframes, video, web forms," and the protocol was designed to support "audio and video streaming."
6. **Enterprise-grade by reuse.**\[35\] Rather than inventing new security, A2A uses HTTP, TLS, OpenAPI-style schemes, mTLS and OAuth. Remote agents are "standard HTTP-based enterprise applications," which slot into existing gateways, identity systems and observability.
7. **Post-launch additions:**
   - \[3\]gRPC (v0.3) and a third REST binding with formal equivalence (v1.0);
   - per-interface version negotiation so v0.3 and v1.0 can coexist;
   - multi-tenancy ("a single endpoint to securely host many agents");
   - a formal extensions and custom-binding governance process;
   - tooling such as A2A Inspector, a Technology Compatibility Kit (TCK) and an A2A CLI (October 2026).

### 7. Problems A2A is designed to solve

- **Agent silos and the N×N integration problem.** "Before A2A, handing off work between agents built on different frameworks required writing custom integration code from scratch for every new pairing."\[11\]
- **Cross-vendor composition.** Enterprises run agents from Salesforce, ServiceNow, SAP, Atlassian, Microsoft and in-house teams. A2A lets these agents work "across their entire enterprise application estates."
- **Secure, auditable cross-organization communication.** It uses standard transport security, declared auth schemes, signed cards and no identity in the payload.
- **Limits of agents-as-tools.**\[46\] The A2A docs say "wrapping an agent as a simple tool is limiting: it can't capture the agent's full capabilities." Tools cannot ask clarifying questions, run for an hour, or decline.
- **Asynchronous, long-running work** with status updates and webhooks.
- **Human-in-the-loop checkpoints** via interrupted task states.
- **Capability discovery** without hard-coded integrations.
- **Ecosystem fragmentation among agent protocols.**\[47\]\[48\] IBM's Agent Communication Protocol (ACP) merged into A2A in August 2025. "The ACP team will be winding down active development," and IBM's Kate Blair joined the A2A TSC. Blair first posted the announcement on the BeeAI GitHub on August 25, 2025. LF AI & Data republished it on August 29, 2025, co-bylined with Google's Todd Segal.

### 8. Adoption, examples and open problems

**Launch vs. now.**

| Aspect | April 2025 launch | October 2026 |
|---|---|---|
| Spec | Draft at github.com/google/A2A; JSON-RPC + SSE | v1.0.0 (Mar 2026) under a2aproject; 3 bindings; proto-normative |
| Discovery | `/.well-known/agent.json`, unsigned | `/.well-known/agent-card.json` (IANA-registered), optional JWS signing |
| Governance | Google-led | Linux Foundation → AAIF project; 8-company TSC |
| Supporters | 50+ partners | "over 150 organizations" (A2A project, Aug 2026) |
| SDKs | Python, JS samples | Official Python, Go, Java, JavaScript, .NET, Rust (a2aproject org) |
| Hyperscalers | Google only | Google Cloud, AWS Bedrock AgentCore Runtime, Microsoft Azure AI Foundry/Copilot Studio |

**Google.**
- On July 31, 2025 Google shipped native A2A in its Agent Development Kit (ADK).
- It added A2A deployment to Agent Engine and integration with Agentspace (now part of Gemini Enterprise).
- The launch demo was candidate sourcing: a hiring manager's agent in Agentspace delegates to sourcing, scheduling and background-check agents.
- Google Cloud documentation lists an `lf.a2a.v1` package in its CX Agent Studio reference.

**Microsoft.** On May 7, 2025 Microsoft announced A2A support in Azure AI Foundry and Copilot Studio, so Copilot Studio agents can "securely invoke external agents, including those built with other platforms or hosted outside Microsoft."\[49\]\[50\] Microsoft also contributes through Semantic Kernel.

**AWS.**
- In November 2025 Amazon Bedrock AgentCore Runtime added A2A support.\[51\]
- The demo was an incident-response system in which a Google ADK host agent coordinates a Strands monitoring agent and an OpenAI Agents SDK operations agent.\[51\]\[52\]
- AWS's FAQ says A2A is "currently available in AgentCore Runtime, with broader A2A support across other AgentCore services coming soon."\[53\]

**Frameworks and SaaS.** A2A cites support from LangGraph, CrewAI, Pydantic AI, AG2 and IBM BeeAI. It says ServiceNow, Salesforce, Atlassian and SAP use A2A to connect workflows across products. Google Cloud's July 2025 post cited Adobe (making distributed agents interoperable) and Twilio (latency-aware agent selection). PayPal and Google are extending A2A into payments via AP2.

**Open problems.**
- **Security.**
  - \[54\]Researchers have documented Agent Card spoofing, Agent Card "context poisoning" (prompt injection hidden in card descriptions), task replay and cross-agent prompt injection.\[55\]\[56\]\[57\]\[58\] Sources include the Cloud Security Alliance's MAESTRO threat model (April 2025), arXiv 2504.16902, Palo Alto Networks, and a 2026 arXiv analysis ("A2ABreak").
  - That analysis notes the Agent Card is "the sole trust anchor" and that "signing is optional."
  - The spec leaves authorization semantics, retries, deduplication and prompt-injection defense to implementers.\[27\]\[29\]\[59\]
  - The opacity principle that protects vendor IP also stops a client from inspecting what a remote agent actually did.\[59\]
- **Maturity and churn.**
  - \[60\]v1.0 introduced breaking changes (enum casing, removed `kind`, removed implicit OAuth).
  - Earlier guides using `agent.json`, `tasks/send` or kebab-case states are out of date.
  - SDK v1.0 support has lagged the spec. The Java SDK shipped 1.0.0.Final on June 10, 2026, and the a2a-js v1.0.0 release (July 22, 2026) declared "@a2a-js/sdk is now generally available."
- **Adoption measurement.** Public A2A numbers are mostly supporter counts and vendor announcements. Independent data on production traffic is scarce, so "runs in production across supply chains, financial services, and mobile platforms" is the project's own claim.
- **Adjacent standards.**
  - \[61\]ACP is merged.\[62\]
  - Cisco-originated AGNTCY joined the Linux Foundation in July 2025 as complementary infrastructure (directory, identity, observability) that is interoperable with A2A, not a competitor.
  - Others, such as ANP and NLIP, remain niche.

## Recommendations

1. **Start with MCP** for any agent that needs tools or data. It has the broader ecosystem, registry and client support. Target the 2026-07-28 stateless spec for new remote servers.
2. **Add A2A at real boundaries**, meaning cases where the other side is independently owned, versioned or vendor-supplied, may run long, may need to ask questions, or may refuse. If the "agent" is really a deterministic function inside your own codebase, expose it as an MCP tool or use your framework's native sub-agent primitives. The A2A docs themselves say A2A is "not a sub-agent or tool-call protocol."
3. **Build on A2A v1.0** with an SDK that supports v0.3 compatibility mode.\[3\] Publish dual-version Agent Cards during migration.
4. **Harden A2A yourself:**
   - require signed Agent Cards and an allow-list of trusted issuers;
   - treat every card field and message as untrusted LLM input;\[63\]
   - use mTLS or OAuth with scoped, delegated tokens;
   - correlate A2A task IDs with downstream MCP tool calls in audit logs (W3C Trace Context is now standardized in MCP);
   - make clients idempotent against webhook loss.\[29\]
5. **Plan for convergence rather than a winner.** With both protocols under AAIF, expect bridges, shared gateways and possibly aligned auth and task semantics. Avoid hard-wiring business logic to either protocol's transport details.

## Caveats

- Several 2026 figures (150+ organizations, the AAIF join date, SDK GA dates) come from project announcements or secondary blogs.
  - On the AAIF date, Axios and Forbes both report an August 17, 2026 announcement. August 20 appears only in smaller blogs, and August 27 is the A2A blog's own post date.
  - The ACP merger's two dates (August 25 vs. 29, 2025) reflect Kate Blair's original GitHub post and LF AI & Data's republication.
- A2A's v0.2 release (May 20, 2025, announced at Google I/O) added stateless interactions and OpenAPI-style authentication schemes. GitHub's v0.2.0 release entry carries a later, retroactive date. The rename from `tasks/send` to `message/send` can be inferred by comparing the v0.1 and v0.2.0 specs but is not called out in a changelog.
- No direct Anthropic or MCP-maintainer commentary on A2A was found. Characterizations of their position are inferred.
- "A2A is dead" and "MCP won" pieces are opinion, mostly from MCP-ecosystem vendors. Vendor "hype vs. reality" retrospectives in 2026 argue the opposite. Neither side offers rigorous usage data.
- MCP's Tasks and A2A's interop features are still evolving. Code written against MCP's 2025-11-25 experimental Tasks API or A2A v0.x needs migration.

## 資料來源

1. [MCP and A2A: The Protocols Building the AI Agent Internet](https://medium.com/@aftab001x/mcp-and-a2a-the-protocols-building-the-ai-agent-internet-bc807181e68a)
2. [A2A and MCP - A2A Protocol](https://a2a-protocol.org/latest/topics/a2a-and-mcp/)
3. [A2A Protocol Ships v1.0: Production-Ready Standard for Agent-to-Agent Communication - A2A Protocol](https://a2a-protocol.org/latest/blog/2026/03/12/a2a-protocol-ships-v10-production-ready-standard-for-agent-to-agent-communication/)
4. [Google A2A Protocol in 2026: Adoption, Hype, and Reality - Rost Glukhov](https://www.glukhov.org/ai-systems/comparisons/a2a-protocol-2026-adoption/)
5. [Google A2A Protocol in 2026: Adoption, Hype, and Reality - DEV Community](https://dev.to/rosgluk/google-a2a-protocol-in-2026-adoption-hype-and-reality-51d6)
6. [Model Context Protocol Specification Version Timeline - Version-by-Version Changes and Adoption Milestones](https://hidekazu-konishi.com/entry/mcp_specification_version_timeline.html)
7. [55 Emerging Standards Adoption (A2A/MCP) Statistics](https://nevermined.ai/blog/emerging-standards-adoption-statistics)
8. [Announcing the Agent2Agent Protocol (A2A)- Google Developers Blog](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
9. [MCP 2025-11-25 is here: async Tasks, better OAuth, extensions, and a smoother agentic future — WorkOS](https://workos.com/blog/mcp-2025-11-25-spec-update)
10. [Top Gen AI Software Development Tools In 2026: LangChain, LlamaIndex, and More](https://geekvibesnation.com/top-gen-ai-software-development-tools-in-2026)
11. [A New Chapter for A2A: Joining the Agentic AI Foundation - A2A Protocol](https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/)
12. [AWS Marketplace: A2A Protocol Implementation on Bedrock AgentCore - Multi-Agent Systems](https://aws.amazon.com/marketplace/pp/prodview-3akts3vrfp3iq)
13. [What happened to Google's A2A? - fka.dev](https://blog.fka.dev/blog/2025-09-11-what-happened-to-googles-a2a/)
14. [Why Google's A2A Protocol Doesn't Make Sense When We Already Have MCP - fka.dev](https://blog.fka.dev/blog/2025-04-15-why-googles-a2a-protocol-doesnt-make-sense/)
15. [A2A Protocol: The Year the Agent Communication Standard Grew Up — aniketkarneai.com](https://aniketkarneai.com/blog/2026-07-06-a2a-protocol-ecosystem-2026)
16. [Who Created MCP Protocol? Origins and Impact](https://testml.org/blog/who-created-the-model-context-protocol-origins-and-impact/)
17. [Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol)
18. [Introducing the Model Context Protocol — Guide (Free)](https://www.beri.net/learning/anthropic-introducing-mcp)
19. [One Year of Model Context Protocol: From Experiment to Industry Standard](https://www.ajeetraina.com/one-year-of-model-context-protocol-from-experiment-to-industry-standard/)
20. [MCP Enterprise Adoption Guide 2026: Stats, Vendors, Security, guptadeepak.com](https://guptadeepak.com/the-complete-guide-to-model-context-protocol-mcp-enterprise-adoption-market-trends-and-implementation-strategies/)
21. [Before you connect another MCP server: an audit checklist for workplace teams - DEV Community](https://dev.to/ascotlan/before-you-connect-another-mcp-server-an-audit-checklist-for-workplace-teams-1mjb)
22. [What Is MCP in AI? How the Model Context Protocol Works, in Plain English](https://triseed.co/post/what-is-mcp-in-ai-how-the-model-context-protocol-works-in-plain-english)
23. [MCP joins the Agentic AI Foundation](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/)
24. [a2a protocol simply explained here](https://pocketflow.substack.com/p/a2a-protocol-simply-explained-here)
25. [Releases · a2aproject/A2A · GitHub](https://github.com/a2aproject/A2A/releases)
26. [Introduction to Agent To Agent (A2A) Protocol](https://medium.com/amex-gbt-technology/introduction-to-agent-to-agent-a2a-protocol-eb4941bff2d5)
27. [A2A Protocol Tutorial: v1.0 Agent Cards, Tasks and Bindings](https://www.matthewswong.com/en/blog/a2a-protocol-v1-agent-cards-guide/)
28. [Agent2Agent (A2A) Protocol Official Specification](https://a2a-protocol.org/v0.3.0/specification/)
29. [A2A's task lifecycle: what the async contract fixes, and what it leaves to you](https://vadim.blog/a2a-task-lifecycle-async-agent-contract/)
30. [Task Lifecycle](https://deepwiki.com/google/A2A/1.3-task-lifecycle)
31. [a2a-python/docs/migrations/v1\_0/README.md at main · a2aproject/a2a-python · GitHub](https://github.com/a2aproject/a2a-python/blob/main/docs/migrations/v1_0/README.md)
32. [Task state](https://emissar.ai/glossary/task-state)
33. [What's New in v1.0 - A2A Protocol](https://a2a-protocol.org/latest/whats-new-v1/)
34. [agent2agent linux foundation](https://www.infoq.com/news/2025/07/agent2agent-linux-foundation)
35. [Enterprise Features - A2A Protocol](https://a2a-protocol.org/latest/topics/enterprise-ready/)
36. [Where A2A Fits in the Open Agent Ecosystem - Agentic AI Foundation (AAIF)](https://aaif.io/blog/where-a2a-fits-in-the-open-agent-ecosystem)
37. [Key Changes - Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18/changelog)
38. [Specification](https://modelcontextprotocol.info/specification/)
39. [MCP Specification Changelog: Version History and Evolution](https://www.mcpserverspot.com/learn/fundamentals/mcp-specification-changelog)
40. [DEV Community](https://dev.to/forgecode/mcp-2025-06-18-spec-update-security-structured-output-elicitation-1pin)
41. [A2A + MCP: How Agent-to-Agent and Model Context Protocol Work Together](https://amux.io/guides/a2a-mcp-agent-protocols/)
42. [What happened to A2A Protocol? - Credal.ai](https://credal.ai/blog/what-happened-to-a2a-protocol)
43. [One Year of MCP: November 2025 Spec Release](https://daily.dev/posts/one-year-of-mcp-november-2025-spec-release-cyldqjdwh)
44. [A2A and MCP: Start of the AI Agent Protocol Wars? - Koyeb](https://www.koyeb.com/blog/google-a2a-anthropic-mcp-ai-agent-protocol-war)
45. [Google to embrace Anthropic’s standard for connecting AI models to data](https://techcrunch.com/2025/04/09/google-says-itll-embrace-anthropics-standard-for-connecting-ai-models-to-data/)
46. [What is A2A? - A2A Protocol](https://a2a-protocol.org/latest/topics/what-is-a2a/)
47. [ACP Joins Forces with A2A Under the Linux Foundation · i-am-bee · Discussion #5 · GitHub](https://github.com/orgs/i-am-bee/discussions/5)
48. [A2A vs. MCP vs. ACP: the protocol war that's costing your team months of rework - DEV Community](https://dev.to/alex_aslam/a2a-vs-mcp-vs-acp-the-protocol-war-thats-costing-your-team-months-of-rework-38ga)
49. [Microsoft Adopts A2A Protocol, Agentic AI Era Begins - Cloud Wars](https://cloudwars.com/ai/microsoft-adopts-a2a-protocol-agentic-ai-era-begins/)
50. [Empowering multi-agent apps with the open Agent2Agent (A2A) protocol](https://www.microsoft.com/en-us/microsoft-cloud/blog/2025/05/07/empowering-multi-agent-apps-with-the-open-agent2agent-a2a-protocol/)
51. [AWS adds Agent-to-Agent protocol support in Bedrock AgentCore Runtime - TechInformed](https://techinformed.com/aws-adds-agent-to-agent-protocol-support-in-bedrock-agentcore-runtime/)
52. [Introducing agent-to-agent protocol support in Amazon Bedrock AgentCore Runtime](https://aws-news.com/article/2025-11-11-introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime)
53. [aws.amazon.com](https://aws.amazon.com/bedrock/agentcore/faqs/)
54. [A2ABreak: Systematic Security Analysis of the A2A Protocol](https://arxiv.org/pdf/2609.10871)
55. [Building A Secure Agentic AI Application Leveraging Google’s A2A Protocol](https://arxiv.org/html/2504.16902v2)
56. [Safeguarding AI Agents: An In-Depth Look at A2A Protocol Risks and Mitigations](https://live.paloaltonetworks.com/t5/community-blogs/safeguarding-ai-agents-an-in-depth-look-at-a2a-protocol-risks/ba-p/1235996)
57. [From Prompt Injections to Protocol Exploits: Threats in LLM-Powered AI Agents Workflows](https://arxiv.org/pdf/2506.23260)
58. [Threat Modeling Google's A2A Protocol](https://cloudsecurityalliance.org/blog/2025/04/30/threat-modeling-google-s-a2a-protocol-with-the-maestro-framework)
59. [Google's A2A Protocol Has Zero Defenses Against Prompt Injection](https://grith.ai/blog/a2a-protocol-zero-defenses-prompt-injection)
60. [A2A Protocol Ships v1.0: Production-Ready Standard for ...](https://a2a-protocol.org/latest/announcing-1.0/)
61. [The Linux Foundation Expands Agentic AI Push With Third Major Project](https://www.linuxinsider.com/story/the-linux-foundation-expands-agentic-ai-push-with-third-major-project-177587.html)
62. [MCP Adoption Statistics 2026: Downloads, Servers and A2A](https://gravity.fast/data/mcp-adoption-statistics/)
63. [A2A Security & Risks Guide](https://tyk.io/learning-center/a2a-security-the-developers-complete-guide/)