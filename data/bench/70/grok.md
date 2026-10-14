Java web development moved from low-level request handling to a container that wires plain objects, then to a framework that removes most of that wiring. Each step attacked a specific kind of boilerplate the previous one left behind.

## Servlets: a Java process for HTTP

**What it was.** The Servlet API (late 1990s) put Java code inside a long-lived container (Tomcat and similar). One JVM handles many requests instead of CGI’s “new process per request.”

**Problem it solved.** CGI was slow to start, awkward to share state in, and not a real application model. Servlets gave a standard `HttpServletRequest` / `HttpServletResponse` lifecycle, sessions, filters, and deployment in a servlet container.

**What it left broken.**

- HTML built with `out.println` mixed view and logic.
- Every concern (parsing, validation, JDBC, transactions, security) was hand-written.
- Classes depended on the Servlet API, so unit tests needed a container or heavy mocks.
- Configuration and wiring lived in `web.xml` and constructors.

## JSP, then early MVC: separate the page, not the architecture

**JSP (1999)** inverted the servlet: HTML with embedded Java, compiled into a servlet. It fixed unreadable HTML generation and created scriptlet pages where business logic, SQL, and markup lived together.

**Apache Struts (~2000)** and similar action frameworks imposed MVC: a front controller, actions, form beans, and JSP views. That was the right shape, but configuration was large XML files, actions were still framework types, and data access, transactions, and testing stayed manual.

## J2EE / EJB: enterprise services, at a high cost

**Java EE** (J2EE from 1999) bundled servlets, JSP, JNDI, JTA, JMS, and especially **EJB** for distributed components, declarative transactions, and security.

**Problem it aimed to solve.** Real systems need transactions, remoting, persistence, and security without every team inventing them.

**What went wrong (especially EJB 2.x).**

- Many interfaces and deployment descriptors per component.
- Components had to run inside a full application server.
- The programming model was invasive: your code depended on EJB APIs and container services.
- Testing, startup, and vendor portability were slow. “Lightweight” was a reaction to this, not a slogan.

## Spring Framework: POJOs, a container you control

Rod Johnson’s critique of J2EE (2002) became the Spring Framework (1.0 in 2004). The goal was enterprise behavior **without** forcing business code to inherit framework types.

**Problems it targeted.**

- Tight coupling to container APIs and hard-to-test “new” graphs.
- Cross-cutting concerns (transactions, security, logging) copied into every method.
- Inconsistent, low-level use of JDBC, transactions, and messaging.
- Web MVC that was thinner and more testable than Struts-style actions.

**How the model changed.**

- **IoC / dependency injection.** Objects do not construct their collaborators. A container injects them. Classes stay plain Java (POJOs).
- **AOP.** Transactions, security checks, and similar cross-cutting behavior are applied outside the business method.
- **Portable service abstractions.** `JdbcTemplate`, transaction managers, and similar types hide boilerplate while letting you swap implementations.
- **Spring MVC.** `@Controller` methods take domain types and return views or bodies. DispatcherServlet is the front controller; you do not extend a framework action class for ordinary work.
- **Configuration moved from XML toward code.** Spring 2.5 added stereotype annotations. Spring 3 (2009) made `@Configuration` / `@Bean` and annotation MVC first-class. XML became optional.

Spring did not replace the servlet container. It ran on top of it. It also did not remove choice: you still picked versions, XML vs Java config, and server packaging. That flexibility became its own tax.

## Spring Boot: an opinionated distribution of Spring

**Spring Boot 1.0 (2014)** did not replace Spring’s programming model. It attacked **setup**: dependency lists, version alignment, XML or Java config for MVC and data sources, `web.xml`, and an external Tomcat install just to boot a service.

**What it added.**

- **Starters.** `spring-boot-starter-web`, `spring-boot-starter-data-jpa`, and others pull a coherent set of libraries.
- **Auto-configuration.** Classpath and properties decide beans. A web starter plus no custom server config means an embedded servlet container and a dispatcher servlet.
- **Executable packaging.** `java -jar app.jar` runs an embedded Tomcat, Jetty, or Undertow. External servers remain possible.
- **Externalized config.** `application.properties` / `application.yml`, profiles, and environment variables override defaults in a defined order.
- **Production hooks.** Actuator (health, metrics, info) and a uniform logging setup.

Later lines continued the same idea under new baselines: Spring 5 / Boot 2 added WebFlux (reactive, non-servlet); Spring 6 / Boot 3 moved `javax.*` to `jakarta.*`, required modern Java, and pushed observability and GraalVM native images. The servlet stack is still the default for typical MVC apps; WebFlux is a parallel stack for non-blocking I/O.

```text
CGI  →  Servlet  →  JSP / Struts  →  J2EE (EJB)
                         ↓
              Spring (IoC, AOP, MVC on servlets)
                         ↓
         Spring Boot (starters, auto-config, embedded server)
                         ↓
        Boot 2: WebFlux optional    Boot 3: Jakarta + Java 17+
```

## Core Spring functionality you actually use

| Area | What it does | Typical types |
|---|---|---|
| IoC container | Creates objects, injects dependencies, manages lifecycle and scope | `ApplicationContext`, `@Component`, `@Configuration`, `@Bean` |
| Stereotypes | Marks role; all are components, with different intent | `@Service`, `@Repository`, `@Controller`, `@RestController` |
| DI | Constructor injection is the default you should prefer | `@Autowired` (often optional on a single constructor), `@Qualifier`, `@Primary` |
| AOP / transactions | Wraps methods with transactional and other advice | `@Transactional`, `@EnableTransactionManagement` |
| Web MVC | Maps HTTP to methods, binds and validates input, writes responses | `@GetMapping`, `@RequestBody`, `@PathVariable`, `@Valid` |
| Data access | JDBC helpers or repository abstractions; exception translation | `JdbcTemplate`, Spring Data repositories, JPA |
| Config & profiles | Environment-specific beans and properties | `@Profile`, `@ConfigurationProperties`, `@Value` |
| Boot auto-config | Beans appear because a starter is on the classpath | `@SpringBootApplication` (`@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`) |
| Security | Filter chain in front of MVC: authn, authz, CSRF, method security | Spring Security filter chain, `@PreAuthorize` |
| Cross-cutting extras | Caching, scheduling, validation, messaging, events | `@Cacheable`, `@Scheduled`, `ApplicationEvent` |
| Testing | Context slices or full startup; MVC without a real socket | `@SpringBootTest`, `@WebMvcTest`, `MockMvc`, `@DataJpaTest` |

`@SpringBootApplication` is the composition root: component scan from that package downward, plus auto-configuration. A request then flows roughly:

`embedded container → filters (including Security) → DispatcherServlet → HandlerMapping → your @Controller → HttpMessageConverter / view → response`

Business services should not know HTTP. Repositories should not know controllers. Transactions usually sit on the service boundary.

## Essential knowledge for working in it

**Java, before Spring.**

- OOP, interfaces, generics, exceptions, collections.
- Annotations and reflection at a conceptual level (you rarely write reflection yourself; the container does).
- Classpath, packages, and build basics. Component scan only sees packages under the application class unless you tell it otherwise.
- Immutability and side effects: injected beans are usually singletons, so mutable fields are shared across requests.

**HTTP and the servlet model, even if you never write a servlet.**

- Methods, status codes, headers, query vs path vs body, cookies, sessions.
- Filters vs interceptors vs controller advice.
- Synchronous servlet request threads vs WebFlux event loops. Do not block the reactive thread.
- REST resource design is independent of Spring; Spring only maps it.

**The container mental model.**

- **Who creates the object?** If Spring creates it, Spring can inject into it. A `new` you wrote is invisible to the container.
- **Scope.** Singleton (default) vs prototype vs request/session. Injecting a shorter-lived bean into a singleton needs care.
- **Lifecycle.** Construction → dependency injection → `@PostConstruct` → use → `@PreDestroy`.
- **Proxying.** `@Transactional` and similar features wrap the bean in a proxy. Self-invocation (`this.method()`) skips the proxy, so the annotation does not run.
- **Configuration order.** Auto-config yields to your `@Bean` of the same type. Profiles and `@ConditionalOn*` decide what exists.

**Boot-specific habits.**

- Prefer starters over listing dozens of versions. The parent BOM manages versions.
- Treat `application.yml` as defaults; secrets and environment differences come from env vars or a config server, not committed passwords.
- Know the failure modes: missing bean (no scan / no starter), two beans of one type (need `@Qualifier` or `@Primary`), circular dependencies, and “it works in tests but the scan root is wrong.”
- Use Actuator health in any deployed service. Expose only what operations needs.

**Data and consistency.**

- SQL and transactions: isolation, propagation (`REQUIRED vs REQUIRES_NEW`), and rollback rules (runtime exceptions roll back by default).
- If you use JPA: persistence context, lazy loading, and the N+1 problem. `@Repository` plus Spring’s exception translation turns vendor SQL exceptions into `DataAccessException`.
- DTOs at the boundary. Do not bind HTTP bodies straight onto JPA entities unless the API is trivial and internal.

**Testing.**

- Unit-test services with plain JUnit and constructor injection; no Spring required.
- `@WebMvcTest` for controller contracts. `@DataJpaTest` for repositories. `@SpringBootTest` only when you need the real composition.
- Slice tests stay fast. Full-context tests catch wiring mistakes.

**What you can defer.**

- Writing your own `BeanFactoryPostProcessor` or deep AOP pointcuts.
- Replacing auto-config on day one. Learn the defaults, then override the one bean that is wrong.
- WebFlux, until you have a latency or streaming problem the servlet stack cannot meet.

## How to read a Spring Boot codebase

1. Start at `@SpringBootApplication` and the package layout.
2. Follow HTTP inward: controller → service → repository. Ignore framework classes until something fails.
3. Treat `@Transactional` service methods as the consistency boundary.
4. Check `application.yml` and profile-specific files before debugging “wrong database” or “missing feature.”
5. When a bean is missing or duplicated, reason about classpath (starters) and component scan before adding more annotations.

Servlets made HTTP a Java API. J2EE added enterprise services by eating the domain model. Spring put those services around ordinary objects. Spring Boot made a working Spring application the default rather than a project you assemble by hand. The skill that transfers across all of them is still the same: keep request handling, business rules, and persistence in separate layers, and let the container wire those layers instead of `new`
