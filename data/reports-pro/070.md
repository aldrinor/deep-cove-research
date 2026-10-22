# From Java Servlets to Spring Boot: The Evolution of Java Web Development

**The evolution raised the abstraction.** Java web development moved from portable, container-managed Servlets to JSP templates and MVC separation; enterprise applications gained standardized services through EJB and J2EE/Java EE; Spring then simplified application construction through ordinary Java objects, dependency injection, and reusable infrastructure. Spring Boot addressed the next pressure: assembling, configuring, packaging, and operating those Spring applications consistently. These developments overlapped rather than forming a sequence of complete replacements. [1][2]

**Spring and Boot solve different problems.** Spring Framework supplies the application programming model: object management, AOP, transactions, data access, web frameworks, validation, integration, and testing. Spring Boot supplies opinionated defaults and application assembly around that model. A typical Boot application using Spring MVC still handles requests through a Servlet; WebFlux provides a separate reactive alternative. Developers therefore need both Java fundamentals and an understanding of HTTP, container behavior, configuration, persistence, transactions, testing, security, and production operation. [2]

**The report follows those pressures.** The chronological account explains what each iteration improved and what remained difficult. The functionality sections then separate Spring’s foundations from Boot’s conveniences, followed by the practical knowledge developers need and a parallel comparison of the three principal layers.

## Evolution scoreboard: problem pressure to abstraction

| Stage and period | Problem pressure | Solution introduced | Configuration and deployment | Remaining pressure |
|---|---|---|---|---|
| Servlets, 1996 onward | CGI portability and scaling | Container-managed Java requests | Servlet mappings; container runtime | Low-level application assembly |
| JSP and Model 1, 1999 onward | HTML embedded in Java | Server-side page templates | JSP pages in a web container | Processing and presentation coupling |
| MVC, Struts, and JSF, 2000–2004 | Web-code maintenance; UI construction | MVC flow or reusable components | Framework-specific web configuration | Integration with business infrastructure |
| EJB and J2EE/Java EE, 1999 onward | Repeated enterprise infrastructure | Standardized containers and services | Server-managed resources and deployment | Component ceremony; platform breadth |
| Spring Framework, 2002–2004 origins | J2EE complexity and difficult testing | POJOs, DI, AOP, service abstractions | Selectable modules; explicit configuration | Repeated setup and runtime assembly |
| Spring Boot, 2013–2014 origins | Spring setup and operational friction | Conditional defaults and packaged runtime | Starters; executable archives; properties | Understanding defaults and compatibility |

**Each row changes responsibility.** Servlets standardize how server-side Java participates in web requests. MVC structures the web application; enterprise containers standardize shared services; Spring makes application objects and infrastructure easier to compose; Boot standardizes the common choices surrounding that composition. The historical sequence and the distinctions between Model 1, Model 2, Struts, and JSF are described in Doug Meil’s 2023 account and Kurniawan and Xue’s 2004 comparison. [3][4]

## A chronological map of the major changes

### 1996–2004: web foundations and enterprise complexity

| Date or period | Development | Principal change |
|---|---|---|
| 1996 | Java Servlet API | Portable server-side Java web components |
| 1999 | JavaServer Pages | View templates extracted from Servlet code |
| December 1999 | J2EE 1.2 | Coordinated enterprise platform and interoperability |
| 2000 | Struts 1 | Framework organization around Model 2 MVC |
| September 2001 | J2EE 1.3 | Local EJB interfaces and connector support |
| 25 September 2001 | Servlet 2.3 and JSP 1.2 | Further standardized web capabilities |
| 2002–February 2003 | Spring origins and open sourcing | DI, simpler JDBC, portable service abstractions |
| November 2003 | J2EE 1.4 | Web services, deployment, and management integration |
| March–2004 | Spring 1.0 and Spring MVC 1.0 | Lightweight application infrastructure and MVC |
| 2004 | JSF 1.0 | Component-based, event-driven web interfaces |

**The dates represent different milestones.** Meil dates Servlets to 1996, JSP to 1999, Struts to 2000, and both JSF 1.0 and Spring MVC 1.0 to 2004. The JCP records the Servlet 2.3/JSP 1.2 final release on 25 September 2001, while Johns Hopkins’ platform summary supplies the J2EE version milestones. [3][5][6]

**Spring’s beginning has several dates.** Rod Johnson traced its origins to the framework code developed while writing *Expert One-on-One J2EE Design and Development* in 2002; it became open source in February 2003. Graudins and Zaitseva’s contemporary comparison dates Spring Framework 1.0 to March 2004. These are the origin, open-source, and version-1.0 milestones—not competing descriptions of one event. [7][8]

### 2006–2026: simpler programming, packaged applications, and new runtimes

| Date or generation | Development | Principal change |
|---|---|---|
| 11 May 2006 | Java EE 5 | Annotations, better defaults, simpler enterprise development |
| Spring 2.5 and 3.0 | Annotation configuration and JavaConfig | Less dependence on XML wiring |
| 10 December 2009 | Java EE 6 | Web Profile, extensibility, further simplification |
| June 2013 | Java EE 7 | WebSocket, JSON, batch, concurrency, simpler JMS |
| 2013–1 April 2014 | Boot prototype to Boot 1.0 GA | Opinionated, stand-alone Spring applications |
| September 2017 | Servlet 4.0 and Java EE 8 | Modern HTTP and web-platform capabilities |
| Spring Framework 5.0 | Spring WebFlux | Parallel non-blocking reactive web stack |
| Spring Framework 6.0 | Java 17 and Jakarta baseline | Modern JDK floor and `jakarta` enterprise APIs |
| 13 November 2025 | Spring Framework 7.0 GA | New generation underpinning Spring Boot 4.0 |
| June 2026 | Boot support transition | Final OSS 3.5 release; 4.x support paths |

**Both branches kept simplifying.** Java EE 5’s final release is recorded in the JCP catalog; Java EE 6 reached final release on 10 December 2009, and Java EE 8 on 18 September 2017. Servlet 4.0 reached final release on 5 September 2017. Spring’s own configuration evolved through annotations in 2.5 and Java-based bean definitions in 3.0. [9][10][11][12]

**Boot changed application assembly.** The Spring team’s 1 April 2014 announcement describes the progression from a polished SpringOne2GX 2013 prototype to Spring Boot 1.0.0 general availability. Later, Framework 5 introduced WebFlux, Framework 6 established the Java 17/Jakarta generation, and Framework 7.0 became generally available on 13 November 2025 as the foundation for Boot 4.0. [13][14][15][16]

**This is a branching history.** EJB was not a successor to JSP, nor did Spring Boot replace the Servlet API. Web presentation, business-component management, infrastructure composition, and deployment evolved together. Spring’s documentation explicitly describes Java EE/Jakarta EE and Spring as complementary: Spring integrates selected enterprise specifications without adopting the entire platform programming model. [2]

## Java Servlets: portable requests, low-level application code

### What Servlets improved over CGI

**Servlets made server-side Java portable.** Oracle’s Java EE tutorial identifies platform dependence and limited scalability as shortcomings of the CGI approaches that preceded Servlets. The Servlet API supplied a consistent way to generate dynamic, user-oriented content using Java components hosted by a container. The important improvement was a reusable execution contract rather than a complete application architecture. [1]

**The container handles web execution.** A Servlet container receives an HTTP request, selects the mapped Servlet, and supplies request and response objects. Application code reads parameters, headers, and other request information, invokes application behavior, and constructs a response. For HTTP Servlets, the familiar programming surface includes methods such as `doGet()` and `doPost()`, reached through the Servlet service mechanism. [17]

**Lifecycle is separate from requests.** The container initializes a Servlet through `init()`, invokes `service()` to handle requests, and calls `destroy()` when removing the Servlet during its managed lifecycle. Initialization is not repeated for every request, and destruction is not an end-of-request callback. Developers can therefore establish component-level resources during initialization and release them during normal teardown. [17]

**Shared instances require concurrency awareness.** A Servlet can serve concurrent requests, so request-specific information belongs in request-local data rather than casually assigned instance fields. A field holding “the current customer” can become shared mutable state across callers. The Servlet model removes much server-execution machinery from application code, but it does not remove Java’s concurrency and resource-ownership rules. [1]

### Why higher-level abstractions became attractive

**HTTP handling remained application plumbing.** A direct Servlet implementation still has to decide how URLs map to behavior, how input becomes application data, how failures become responses, and how business objects obtain their collaborators. Those decisions are possible with the API, but they are not the same thing as the API’s container contract. This is why a portable web foundation could coexist with substantial application boilerplate. [3]

**Generating HTML exposed the next problem.** When Java request handlers also construct page markup, presentation changes become entangled with Java control flow. A page designer’s concern—HTML structure—sits beside parameter parsing, branching, and business calls. JSP’s historical purpose was to extract view definition from Servlet code into a templating mechanism. [3]

**Deployment remained container-centered.** The application supplied web components, mappings, and resources to a Servlet container, often as a WAR, or web application archive. A full enterprise application server could additionally provide services such as EJB execution and coordinated resource management. A Servlet container and a full Java EE server therefore represented different levels of runtime responsibility, not interchangeable labels. [18]

**The lasting judgment is foundational.** Direct Servlets remain appropriate when low-level HTTP or container control is central, especially for narrowly scoped components. As application behavior grows, however, repeating routing, object assembly, presentation handling, and infrastructure integration makes a higher-level framework increasingly valuable.

## JSP, MVC, Struts, and JSF: separating web responsibilities

### JSP improved authoring, but Model 1 retained coupling

**JSP moved presentation into templates.** Introduced in 1999, JavaServer Pages let developers express dynamic page content without building the entire view inside a Servlet’s Java code. Oracle describes JSP as a simplified mechanism for rapidly creating server- and platform-independent dynamic web content. The JavaServer Pages Standard Tag Library, JSTL, supplied tags for recurring tasks such as iteration, conditionals, and internationalization. [3][19]

**Templates alone did not create architecture.** In the JSP-centered arrangement called Model 1, pages handled requests, performed processing, and generated presentation. That could be straightforward for limited processing requirements, but the same convenience encouraged business decisions and persistence work to accumulate inside presentation files. Changing a page could consequently require understanding much more than its appearance. [20]

**Maintenance was the decisive pressure.** Kurniawan and Xue’s 2004 study identified Model 1, Model 2, Struts, and JSF as four Java web-development models. It explicitly discouraged Model 1 for medium-sized and large applications because of maintenance difficulties. Their experimental comparison constructed three versions of an online store using Model 2, Struts, and JSF, illustrating that the architectural debate concerned complete application organization rather than merely template syntax. [4]

**Small applications provide the counterexample.** A short page with little processing does not necessarily benefit from a large framework structure. Model 1’s weakness becomes more consequential when processing, persistence, navigation, and presentation change independently. The transition toward MVC was therefore driven by separation of responsibilities, not by a claim that every JSP page was inherently problematic.

### Model 2 and Struts formalized request flow

**Model 2 separated three responsibilities.** Business objects or JavaBeans formed the model, JSP or HTML formed the view, and one or more Servlets acted as controllers. The controller interpreted the incoming request, coordinated application work, and selected the view. This made it possible to change presentation without embedding the same business processing in every page. [20]

**The request path became explicit.** In a typical Model 2 interaction, the Servlet reads request parameters, updates the model and saves it when necessary, then forwards the resulting model to a JSP. The view displays the result rather than deciding the entire operation. The benefit comes from assigning ownership of each decision; complete independence between the layers still requires disciplined design. [20]

**Struts turned a pattern into infrastructure.** Struts 1 appeared in 2000 and provided a framework around the Model 2 approach. Instead of every team inventing its own MVC conventions and request-flow machinery, a named, reusable framework supplied an organizing model. Spring’s web documentation credits Struts with simplifying the JSP/Servlet paradigm and attracting developers away from proprietary frameworks. [3][21]

**Web organization was only one layer.** A Struts application still needed a coherent way to construct services, manage persistence resources, apply transactions, and test business behavior. That remaining pressure is architectural: standardizing the web tier does not itself settle the composition of the business and infrastructure tiers. Spring could be introduced beneath an existing web framework rather than requiring an immediate rewrite of the interface. [21]

**Spring MVC continued the request-oriented branch.** Meil describes Spring MVC 1.0, introduced in 2004, as a reaction to Struts 1. The important transition was toward a web framework integrated with Spring’s broader object-management and infrastructure model. Struts also continued evolving: Struts 2 appeared in 2006, and its Spring integration demonstrates that the alternatives were not mutually exclusive technology stacks. [3][21]

### JSF pursued a component-oriented alternative

**JSF targeted interface construction.** JavaServer Faces 1.0 appeared in 2004 with a component-based, event-driven approach. Oracle describes its workflow as assembling reusable UI components, connecting them to application data, and wiring client-generated events to server-side handlers. Its primary abstraction was therefore closer to UI components and events than to manually coordinating each request and page handoff. [3][19]

| Approach | Main organizing unit | Request and presentation ownership | Principal benefit |
|---|---|---|---|
| JSP Model 1 | JSP page | Page handles processing and output | Simple small-page construction |
| Model 2 MVC | Controller, model, view | Servlet coordinates; JSP renders | Separation of web responsibilities |
| Struts | Framework-managed MVC flow | Model 2 conventions organize handling | Reusable web application structure |
| JSF | UI component and event | Component lifecycle coordinates interaction | Reusable server-side UI assembly |

**The approaches solve different problems.** The comparison follows the distinctions in the 2004 study and Oracle’s component model. Model 2 and Struts focus on structuring request processing; JSF focuses on constructing interactive server-side interfaces. Choosing between them involves the desired UI programming model as well as the underlying service architecture. [4][19]

**JSF also evolved internally.** Its 1.x generation used JSP as its templating mechanism, while 2.x adopted Facelets. Later integration considerations differed from the original promise of rapid component assembly: Spring’s 5.3 web documentation notes that recent JSF versions had become closely tied to CDI infrastructure, with some functionality requiring that environment, and described Spring’s JSF integration as primarily supporting migration. [3][21]

**There was no mandatory JSF-to-Spring transition.** Retaining or replacing Struts or JSF depends on the required UI model, service-container integration, runtime compatibility, and migration cost. Those conditions determine the practical tradeoff; chronological position alone does not establish a maintenance or performance winner.

**The transition’s lasting lesson.** Separating presentation from processing was necessary, but substantial applications also needed a consistent infrastructure model behind the web tier.

## EJB and Java EE: standardizing enterprise services

### Enterprise containers addressed a different problem

**Enterprise applications needed shared services.** Beyond rendering pages, applications needed persistence, transactions, messaging, security, naming, resource access, and managed deployment. J2EE—and later Java EE—coordinated specifications for these concerns. A full-platform server supplied containers and services so that each application did not have to implement its own enterprise runtime. [18]

**EJB standardized business-component execution.** Enterprise JavaBeans aimed to simplify distributed, object-oriented business applications by moving recurring execution concerns into a container. Its capabilities grew across versions: EJB 2.0 included JMS integration, improved entity persistence, portable finder queries, and server interoperability; EJB 2.1 added web-service support, message-driven-bean enhancements, and container-managed timers. [9]

**The early programming model added ceremony.** Graudins and Zaitseva’s 2006 comparison argued that EJB versions 1.0–2.1 were too complicated to fulfill their simplification goal. SpringSource’s migration guide illustrated the older remote-style model with three artifacts—remote interface, home interface, and implementation—plus an XML deployment descriptor, even for simple business behavior. The business operation could be small while the surrounding component contract remained substantial. [8][22]

**Container coupling affected feedback speed.** When business components depend heavily on server contracts, isolated tests and local execution become harder to arrange. The server’s integration is valuable when its services are needed, but requiring that environment for ordinary business logic increases the amount of infrastructure involved in development. Spring’s appeal emerged partly from separating application behavior from those deployment assumptions. [22]

### EJB 3 and Java EE simplified their own model

**EJB 3 directly targeted complexity.** Its specification’s stated purpose was to reduce developer-facing complexity. The changes described in the 2006 comparison included annotations usable alongside or instead of deployment descriptors, removal of required home/component interfaces, simpler bean types, interceptors, defaults, and simpler persistence. This was a substantive redesign of the enterprise programming model, not merely a change in terminology. [9][8]

**JPA separated persistence from EJB identity.** The Java Persistence API supplied a POJO persistence model for object-relational mapping. Although developed by the EJB 3.0 expert group, Oracle explicitly describes it as usable by web applications, application clients, and Java SE applications outside the enterprise platform. That separation made it possible for Spring to integrate a standard persistence API without requiring EJB components. [19]

**Java EE 5 emphasized easier development.** Released in May 2006, it combined annotations, better defaults, dependency injection into enterprise components, and technologies such as JPA. Java EE 6 continued that direction with profiles, more flexible deployment, no-interface EJBs, and component dependency injection. The platform was responding to many of the same developer pressures as Spring. [6]

**Profiles addressed excessive platform breadth.** The Java EE 6 proposal explicitly acknowledged that the platform had become broad enough to lose focus. Its Web Profile offered a subset aimed at typical web applications, while extensibility allowed other technologies to layer onto server implementations. Its pruning process also recognized that older technologies, including EJB container-managed persistence, had been superseded by alternatives such as JPA. [10]

| Platform generation | Development pressure | Response | Continuing design choice |
|---|---|---|---|
| J2EE 1.2–1.4 | Fragmented enterprise infrastructure | Standardized containers and services | Integration versus component ceremony |
| Java EE 5 | Difficult enterprise programming | Annotations, defaults, JPA, simpler components | Server services versus application autonomy |
| Java EE 6 | Broad platform; varied application needs | Web Profile, extensibility, simpler deployment | Full platform versus focused profile |
| Java EE 7 | Repeated infrastructure and new web needs | JSON, WebSocket, batch, concurrency, JMS improvements | Standard integration versus selected libraries |
| Java EE 8 | Modern web and managed-bean requirements | Updated web APIs and integration direction | Platform evolution versus application constraints |

**Later releases retained the infrastructure goal.** Java EE 7 added or strengthened WebSocket, JSON, batch processing, concurrency utilities, validation integration, and simplified JMS. Java EE 8’s specification proposal emphasized modern web standards, managed-bean integration, and cloud-oriented infrastructure; its proposed configuration and monitoring directions express design goals rather than measured operational outcomes. [6][11]

### Why Spring gained appeal without making Java EE irrelevant

**Spring offered a different composition model.** Instead of making ordinary application services special enterprise components, Spring could manage plain Java objects and attach infrastructure behavior around them. Developers could use local transactions or integrate server-provided JTA resources, select persistence technologies, and test business services outside a full application server. Spring could therefore supplement an enterprise application or replace parts of its component model. [22]

**The historical comparison was not one-sided.** Graudins and Zaitseva assessed 13 criteria on a 0.0–1.0 capability scale. Their assessment favored Spring in transaction facilities, service flexibility, testability, and price, but favored EJB 3.0 in persistence, configuration, security, and service integration. For example, they assigned testability scores of 1.0 to Spring and 0.8 to EJB, while service integration scored 0.7 and 0.9 respectively. [8]

**Deployment needs can reverse the preference.** Deep application-server integration, established operational tooling, or particular distributed-transaction requirements can make a server-managed model attractive. Spring’s own transaction documentation recommends EJB when propagation of transaction contexts across remote calls is required, while cautioning against unnecessarily spanning remote calls with transactions. A mature application may also gain less from migration than the migration costs. [23][22]

**The enterprise transition’s central judgment.** Spring’s advantage was a simpler, more portable application programming model—not the discovery of enterprise capabilities that Java EE lacked.

## Spring Framework: reusable infrastructure around ordinary Java objects

### IoC and dependency injection separate construction from behavior

**Spring manages the object graph.** Inversion of control, or IoC, is the broad idea of moving certain responsibilities from application objects to a framework. Dependency injection, DI, is Spring’s principal object-assembly mechanism: objects declare collaborators through constructor arguments, factory-method arguments, or properties, and the container supplies them. The object no longer needs to construct each collaborator or locate it through a registry. [24]

**Explicit dependencies improve replaceability.** Suppose a service needs a repository. If it constructs a particular database repository internally, its business behavior becomes coupled to that implementation and its setup. If it instead accepts a repository interface, production configuration can supply a persistent implementation while a unit test supplies a fake. The improvement comes from the object’s design; the container automates assembling that design. [25]

**Java configuration makes assembly visible.** The following illustrative excerpt assumes that another configuration supplies a `CustomerRepository` bean. The service itself contains ordinary Java behavior, while the configuration tells Spring how to construct it. `@Configuration` and `@Bean` are Spring Framework features. [26]

```java
interface CustomerRepository {
    String findName(long customerId);
}

class CustomerService {
    private final CustomerRepository customers;

    CustomerService(CustomerRepository customers) {
        this.customers = customers;
    }

    String customerName(long customerId) {
        return customers.findName(customerId);
    }
}

@Configuration(proxyBeanMethods = false)
class ServiceConfiguration {
    @Bean
    CustomerService customerService(CustomerRepository customers) {
        return new CustomerService(customers);
    }
}
```

**The container is not the business API.** Spring recommends that ordinary application code avoid repeated `getBean()` lookups. Injecting collaborators keeps dependencies apparent in constructors or methods and avoids turning the container into a service locator used throughout the codebase. Interfaces are useful design boundaries, but Spring does not require every managed class to implement a framework-specific interface. [12]

**ApplicationContext adds application services.** `BeanFactory` supplies the basic bean configuration and assembly contract. `ApplicationContext` extends it with facilities such as event publication, internationalized messages, AOP integration, and application-specific contexts. A `WebApplicationContext` connects that object-management model to a web environment. [24]

### Beans, scopes, and lifecycle define ownership

**A bean is a managed object.** A Spring bean is an object instantiated, assembled, and managed by Spring’s IoC container. Its bean definition is a construction recipe containing information such as its class, dependencies, scope, configuration values, and lifecycle callbacks. An ordinary object created by application code does not automatically acquire container management merely because its class contains annotations. [12]

**Scope determines sharing and lifetime.** Spring documents six standard scopes. Singleton and prototype are general container scopes; request, session, application, and WebSocket scopes require an appropriate web-aware context. These choices express different ownership rules rather than different kinds of business logic. [27]

| Scope | Instance boundary | Practical implication |
|---|---|---|
| `singleton` | One instance per definition per container | Shared service or infrastructure object |
| `prototype` | New instance per container request | Caller owns subsequent cleanup |
| `request` | One HTTP request | Request-specific state |
| `session` | One HTTP session | Session-associated state |
| `application` | One `ServletContext` | Shared web-application state |
| `websocket` | One WebSocket session | Connection-associated state |

**Singleton does not mean globally unique.** Spring’s default singleton scope is per bean definition and container, not one instance of a Java class across the entire JVM. Nor does it make mutable state thread-safe. Stateless services are natural singleton candidates because concurrent callers do not compete over conversational state stored in the service itself. [12]

**Lifecycle callbacks govern resource ownership.** Spring supports initialization and destruction through `@PostConstruct`, `@PreDestroy`, configured methods, and lifecycle interfaces. These hooks let an object prepare after its dependencies are supplied and release resources during normal shutdown. `Lifecycle` and `SmartLifecycle` additionally support coordinated start and stop behavior for components with more involved execution lifecycles. [28]

**Prototype scope has a cleanup boundary.** Spring initializes a prototype object but does not manage its complete subsequent lifecycle or invoke its configured destruction callback. Also, injecting a prototype directly into a singleton supplies the instance resolved during that injection; it does not create a fresh object for every later service call. A provider, scoped proxy, or another suitable lookup mechanism is needed when repeated acquisition is intentional. [27]

### AOP centralizes cross-cutting behavior

**AOP separates repeated infrastructure behavior.** Aspect-oriented programming addresses concerns that cut across many classes, such as transaction boundaries, auditing, or logging. A pointcut selects relevant method executions, and advice supplies behavior before, after, or around those executions. An aspect organizes that selection and behavior without requiring the same infrastructure code inside every business method. [29][30]

**Proxies implement the common mechanism.** Spring AOP typically exposes a proxy that intercepts a call and delegates to the underlying target. It supports JDK dynamic proxies for interfaces and CGLIB-generated subclasses for class-based proxying; configuration can influence which form is used. This allows a transaction interceptor, for example, to start a transaction, invoke a service, and then commit or roll back. [31]

**The call path determines interception.** If a method calls another method on the same object through `this`, the internal call does not pass through the external proxy. Consequently, advice attached to the internally called method does not get a new opportunity to run. An annotation can therefore be present in source code while its expected behavior is absent on a particular execution path. [31]

**Class design constrains class-based advice.** CGLIB cannot subclass a final class or override final or private methods to advise them. Spring AOP also focuses on method-execution interception rather than every possible bytecode join point. Where those boundaries matter, redesigning the service boundary or deliberately using AspectJ weaving may be appropriate; AspectJ’s bytecode weaving avoids the particular self-invocation limitation. [31]

### Data access removes plumbing, not database semantics

**Spring standardizes persistence integration.** The framework supplies JDBC support, DAO abstractions, ORM integration for JPA and Hibernate, and reactive relational access through R2DBC. Its purpose is to make infrastructure use consistent and reusable while leaving applications responsible for queries, mappings, and business meaning. Spring is not itself a relational database or an ORM provider. [32]

**JdbcTemplate handles repetitive resource work.** Direct JDBC requires opening connections, preparing statements, executing SQL, processing results, handling failures, and closing resources correctly. Spring’s JDBC facilities manage much of that repeated lifecycle while application code supplies the SQL, parameters, and result interpretation. This reduces boilerplate and makes participation in Spring-managed transactions more consistent. [25]

**Exception translation creates a shared vocabulary.** Spring DAO support can translate persistence-specific exceptions into a common data-access hierarchy. `@Repository` identifies repository components for discovery and configured exception-translation support. Application layers can consequently handle categories of persistence failure without depending everywhere on a particular provider’s exception types. [33]

**Connection ownership still matters.** A singleton `DataSource` is not the same thing as one database `Connection` shared by all requests. Gribanova-Podkina’s 2019 discussion illustrates the distinction: a single shared connection can centralize setup for a small application but becomes a contention queue as clients increase, whereas a connection pool lends available connections and accepts them back after use. Dependency injection organizes access to infrastructure; it does not make an unsuitable concurrency design scalable. [34]

### Transactions coordinate a unit of work

**Transactions are distinct from persistence access.** A repository describes how data is read or written; a transaction defines which operations belong to one coordinated unit of work. Spring provides consistent transaction abstractions across JDBC, JPA, Hibernate, and JTA, with both programmatic and declarative styles. The chosen transaction manager connects the application-level boundary to actual resources. [35]

**Declarative boundaries keep business code focused.** With appropriately configured `@Transactional` support, a service operation can execute inside a transaction without embedding begin, commit, and rollback calls in its business logic. Spring’s AOP infrastructure supplies that behavior around the call. The same application model can use local resource transactions or integrate JTA, depending on configuration and resource requirements. [23]

**Rollback follows rules, not annotation folklore.** Spring’s default convention rolls back on unchecked failures; checked exceptions require suitable rollback rules unless the defaults are changed. Developers must also understand propagation—whether an operation joins an existing transaction or establishes another boundary—and how exceptions cross the transactional interceptor. Catching and suppressing a failure changes what that interceptor observes. [23]

**Local atomicity is not distributed atomicity.** A database transaction does not automatically make a remote HTTP operation part of the same recoverable unit. Spring declarative transactions do not propagate transaction contexts across remote calls in the manner offered by some high-end application servers. This distinction is especially important when a service both changes local data and invokes another system. [23]

### Spring MVC builds on the Servlet foundation

**DispatcherServlet centralizes web processing.** Spring MVC uses the front-controller pattern: one central Servlet coordinates request processing, while configurable components perform mapping, invocation, exception resolution, conversion, and view rendering. Controllers express application-specific web behavior without each one reimplementing the shared dispatch algorithm. The underlying Servlet contract remains in place. [21]

**Controller methods become HTTP handlers.** `@Controller` and `@RestController` identify web components, while mappings such as `@RequestMapping` and `@GetMapping` associate methods with requests. Input binding, conversion, validation, and exception handling participate in the framework-managed request path. For response-body APIs, message converters can serialize returned application objects into formats such as JSON. [21][36]

**Views remain a separate concern.** For server-rendered applications, a controller can return a logical view name and a model. A `ViewResolver` maps that name to an actual view technology, allowing the web layer to use JSP, FreeMarker, or another supported renderer. Returning response data rather than a template changes the presentation path, not the need for sound application-layer separation. [21]

### WebFlux provides a different concurrency model

**WebFlux is a parallel web stack.** Added in Spring Framework 5.0, it is fully non-blocking, supports Reactive Streams back pressure, and can run on Netty or suitable Servlet containers. It does not directly depend on the Servlet programming model in the same way as MVC. Applications can also combine selected technologies, such as using the reactive `WebClient` from an MVC application. [14]

| Dimension | Spring MVC | Spring WebFlux |
|---|---|---|
| Foundation | Servlet API | Reactive Streams and non-blocking server APIs |
| Common programming style | Imperative controllers | Reactive controllers or functional endpoints |
| Runtime choices | Servlet containers | Netty or suitable Servlet containers |
| Natural persistence fit | JDBC/JPA and blocking libraries | Reactive access such as R2DBC |
| Web test tools | MockMvc | WebTestClient |
| Boot WAR deployment | Supported | Unsupported |

**Back pressure controls production rate.** In a reactive pipeline, the consumer can signal how quickly it is ready to receive data. That helps prevent an asynchronous producer from overwhelming downstream processing merely because it can emit quickly. The mechanism is about coordinating demand across asynchronous components, rather than simply marking a method as asynchronous. [25]

**Non-blocking benefits require compatible work.** If request handling calls blocking database or network code on a thread expected to process non-blocking events, it can undermine the intended execution model. MVC is often the simpler fit for an application centered on synchronous JDBC/JPA operations; WebFlux is attractive for genuinely asynchronous, streaming, or highly concurrent I/O workflows. The choice should follow the complete dependency path and team expertise, not an assumption that “reactive” means universally faster. [25]

### Validation, binding, and conversion are reusable infrastructure

**Validation is not only a controller concern.** Spring supplies a `Validator` contract usable independently of the web tier, with localization support. This allows validation rules to be shared where the same application behavior has multiple entry points, rather than relying on every caller to pass through one HTTP controller. [37]

**Binding and validation answer different questions.** Binding transfers input into an object; conversion turns values into the required types; validation determines whether the resulting values satisfy constraints. Spring provides `DataBinder`, `BeanWrapper`, general conversion, and formatting facilities for these responsibilities. A value can convert successfully yet still violate an application rule. [37]

**Standard constraints complement custom rules.** Bean Validation supplies an annotation-based metadata model, and Spring integrates that model with application and web infrastructure. Developers should distinguish structural constraints from business decisions: a correctly formatted customer identifier does not establish that the caller may access that customer. Validation and authorization protect different boundaries. [19]

### Integration and messaging extend beyond HTTP requests

**Spring also coordinates infrastructure interactions.** Framework integration facilities include REST clients, JMS, JMX management, email, task execution, scheduling, caching, and observability. These capabilities let services interact with external systems and background execution without each application inventing its own resource-handling conventions. [38]

**Messaging changes the interaction boundary.** JMS provides standardized asynchronous, loosely coupled communication; Spring adds facilities such as templates and listener infrastructure around that model. A message-driven operation is not simply an HTTP request on another transport: its completion, failure, and resource boundaries need to be designed around message processing. [19][38]

**Local events are not a broker.** `ApplicationContext` events support communication among components within an application context. More elaborate routing and transformation workflows belong to capabilities such as the separate Spring Integration project. Keeping these boundaries clear prevents an in-process notification mechanism from being mistaken for a distributed messaging system. [12]

**Historical integration lists need version context.** Older Spring releases supported RPC-style facilities such as HTTP Invoker and Hessian, along with dedicated EJB access. Spring Framework 6 removed several of those facilities; EJB lookup can instead use JNDI where appropriate. Understanding Spring’s evolution includes recognizing removals as well as additions. [15]

### Testing is part of the framework model

**Spring supports several verification boundaries.** Plain business objects can be tested without the container, while the TestContext Framework loads Spring configuration to verify wiring and infrastructure integration. Framework web tools include Servlet mocks, MockMvc, and WebTestClient. These tools address different questions, from isolated behavior to framework-managed request processing. [32]

**Integration tests need not deploy an application.** Spring’s `spring-test` support can verify component wiring, SQL, queries, and ORM mappings without deploying to an application server. It also caches application contexts so repeated tests can reuse expensive infrastructure setup. For tests configured with test-managed transactions, rollback support helps control changes to the database. [39]

### The Spring ecosystem has explicit project boundaries

**The framework is the foundation.** Spring Boot, Spring Security, Spring Data, Spring Cloud, and Spring Batch are separate projects with their own repositories and release cadences. Their frequent appearance together in applications does not make their capabilities interchangeable or automatically part of the core container. [2]

| Project | Primary responsibility | Relationship to Boot |
|---|---|---|
| Spring Security | Authentication and authorization | Boot configures common starting arrangements |
| Spring Data | Repository abstractions and store integration | Boot assembles supported data configurations |
| Spring Integration | Enterprise integration patterns | Boot simplifies infrastructure assembly |
| Spring AMQP | AMQP and RabbitMQ integration | Boot offers messaging starters and configuration |
| Spring Cloud | Distributed-system infrastructure | Used when corresponding application needs arise |
| Spring Batch | Structured batch processing | Boot integrates batch application startup |

**These distinctions prevent misplaced expectations.** For example, Spring Framework integrates JPA, Spring Data can create repository implementations, and Boot can configure the surrounding application from dependencies and properties. Those are three contributions to one data-access path—not three names for the same feature. Likewise, core JMS support and Spring AMQP’s RabbitMQ support are related messaging capabilities with different APIs. [40][22][41]

**The framework’s lasting judgment.** Spring reduces infrastructure duplication by composing ordinary objects with reusable services, but developers must still understand the runtime boundaries through which those services are applied.

## Spring Boot: assembling and running Spring applications

### Boot addressed the cost of starting every application

**Spring’s flexibility created repeated decisions.** A conventional Spring application had to select modules and compatible third-party libraries, construct configuration, initialize contexts, arrange web registration, choose packaging, and assemble production support. Spring had already simplified business programming, but teams could still repeat much of the same application setup. Boot’s central contribution was an opinionated, reusable starting arrangement. [42][43]

**The programming model remained Spring’s.** A controller, injected service, repository, and transactional proxy retain their respective Spring responsibilities inside a Boot application. Boot’s startup machinery creates and configures the application context and its surrounding runtime. Its convenience does not require a new business-component model, mandatory microservices, or a fixed number of application layers. [2]

### Auto-configuration applies conditional defaults

**Auto-configuration responds to application state.** Boot considers dependencies on the classpath and relevant application configuration when supplying infrastructure. Its documentation gives the example of HSQLDB: if the database library is present and the application has not defined database connection beans, Boot can configure an in-memory database. The behavior follows conditions, rather than interpreting arbitrary business intentions. [44]

**User configuration can replace defaults.** Defining a custom `DataSource` causes the default embedded-database configuration to back away. Other configurations provide their own conditions and customization points. The practical model is “sensible infrastructure unless the application supplies another arrangement,” with the exact conditions determining what happens. [44]

**Diagnosis requires understanding those conditions.** A changed dependency or an added bean can change which configuration applies. Boot’s `--debug` option produces a conditions report, and unwanted auto-configurations can be excluded through supported configuration mechanisms. Depending on internal bean methods of auto-configuration classes is different from using their supported customization or exclusion interfaces. [44]

**Bootstrap becomes a Java entry point.** A common application starts through `SpringApplication.run()` and enables component discovery and auto-configuration with `@SpringBootApplication`. The following excerpt shows only that startup responsibility; application components remain separate. Boot favors Java configuration, while retaining ways to import XML where needed. [45]

```java
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

**Annotations still have distinct owners.** `@RestController` and request-mapping annotations belong to Spring’s web programming model, not Boot’s application-assembly layer. Similarly, Java configuration and annotation-based dependency injection existed before Boot. The historical shift from XML to Java and annotation configuration should therefore not be confused with Boot’s later introduction. [42][12]

### Starters, dependency management, and build plugins do different jobs

**Boot coordinates dependency choices.** Starters supply useful sets of dependencies for a capability, while Boot’s curated dependency management supplies compatible versions. Maven or Gradle still resolves those dependencies and builds the application. Libraries are not discovered and downloaded as a substitute for a declared build. [42]

| Mechanism | Question it answers | Result |
|---|---|---|
| Starter | Which libraries support this capability? | Convenient transitive dependency set |
| Dependency-management BOM | Which versions belong together? | Coordinated managed versions |
| Build plugin | How is the application packaged and launched? | Executable archive and build integration |

**A BOM is not a feature dependency.** A bill of materials establishes version constraints; it does not by itself mean every managed library is included. A starter expresses dependency choices, and the packaging plugin creates the executable application artifact. Understanding these roles makes build problems easier to diagnose than treating “the Boot dependency” as one indivisible mechanism. [42]

**Overrides preserve choice but add responsibility.** Developers can override managed versions, but doing so changes the dependency combination selected by Boot. Upgrading Boot can update managed dependencies together, reducing repeated compatibility decisions. A local override should therefore be a deliberate choice supported by dependency inspection and tests, rather than an arbitrary attempt to make one compilation error disappear. [42]

### Embedded runtimes invert the traditional startup sequence

**The application can start its server.** In conventional Spring MVC deployment, a Servlet container starts the application and invokes its initialization hooks. In the embedded Boot model, Spring configuration bootstraps the application and embedded container, then registers relevant Servlets and filters. This reverses which component is the primary startup owner without removing the container itself. [21]

**Executable archives simplify delivery.** A Boot executable JAR contains application classes and the dependencies needed to run them, including the embedded web runtime for a web application. It can be launched with `java -jar`, while the host still supplies a compatible Java runtime and access to external services. Packaging reduces separate application-server setup; it does not package away databases, credentials, networking, or runtime compatibility. [42]

**Server choice remains configurable.** Boot’s documented servlet web starter uses Tomcat by default, while its reactive web starter uses Reactor Netty. Supported alternatives can be selected through dependency changes. Boot also supports traditional Servlet-based WAR deployment; WebFlux applications have a different deployment model and do not support WAR deployment. [46][47]

**Packaging shifts operational ownership.** With an embedded server version selected in the application build, runtime changes become part of the application’s dependency and release process. That makes the delivered artifact more explicit, but also makes reviewing server and library updates an application-team concern. “No separately installed server” should not be read as “no server operation.”

### External configuration and Actuator standardize common needs

**Configuration moves outside application code.** Boot supports properties files, YAML, environment variables, and command-line arguments so that the same application can run with different environment settings. Values can be accessed individually or bound into structured objects with `@ConfigurationProperties`. Spring profiles additionally control which configuration participates in a particular environment. [48][49]

**Actuator supplies management infrastructure.** It adds application monitoring and management facilities through HTTP or JMX, including health, metrics, and auditing support. Rather than each team constructing unrelated management endpoints, Boot provides an integrated model and extension points. Its signals still need to be interpreted according to what they actually measure. [50]

**Convenience is not loss of all control.** Oracle’s 2024 explanation emphasizes the tradeoff between configuration freedom and faster setup, but Boot’s own documentation shows extensive back-off and customization mechanisms. A large application does not become unsuitable for Boot merely because it is large. The stronger reason to use Framework without Boot is a concrete assembly or runtime requirement that conflicts with Boot’s conventions. [43][44]

**Boot’s central judgment is practical.** For applications that fit its supported combinations, Boot removes repeated infrastructure decisions while retaining Spring’s programming model; the responsibility moves from writing every configuration to understanding and intentionally customizing the resulting configuration.

## Modern Spring: compatibility and support through September 2026

### Java and Jakarta boundaries affect real applications

**Framework generations have compatibility contracts.** The Spring versions matrix distinguishes the JDK and enterprise API ranges for Framework 5.3, 6.2, and 7.x. Framework 6 introduced the Java 17 minimum and the Jakarta EE 9 baseline; Framework 7’s focus on Java 25 does not mean that Java 25 replaced Java 17 as its minimum. [51][16]

| Framework line | Documented JDK range | Enterprise API alignment | Namespace |
|---|---|---|---|
| 5.3 | JDK 8–21 | Java EE 7–8 | `javax` |
| 6.2 | JDK 17–25 | Jakarta EE 9–10 | `jakarta` |
| 7.x | JDK 17–25+ | EE 11 baseline; early EE 12 support | `jakarta` |

**Namespace migration is a system change.** Moving to the Jakarta generation affects enterprise API imports and compatible implementations. Spring 6 migration guidance pairs changes such as `javax.servlet` to `jakarta.servlet` with Servlet-container upgrades, and moves common injection and lifecycle annotations to their Jakarta packages. Updating application imports while leaving an incompatible server or persistence provider is not a complete migration. [15]

**API names require selective treatment.** The migration concerns affected enterprise APIs, not a blanket renaming of every Java package beginning with `javax`. For example, JDBC infrastructure uses Java SE’s `javax.sql.DataSource`. Developers need to understand which specification owns an API rather than applying a global text replacement. [42][15]

### Support is separate from runtime compatibility

**A running build can outlive support.** The Spring team announced Boot 3.5.16 on 25 June 2026 as the last open-source release of the 3.5 generation and directed users toward 4.0.x or 4.1.x for continued OSS support. Framework’s versions page likewise records the end of OSS support for 5.3 in August 2024 and 6.2 in June 2026, alongside commercial support options. [52][51]

**Published support windows guide maintenance.** Dan Vega’s 2026 support summary lists the following release and support horizons for the relevant Boot branches. The future dates are published support schedules, while the 3.5 OSS ending is also supported by the Spring team’s release announcement. [53]

| Boot branch | Initial release | Scheduled OSS support end | Listed enterprise support end |
|---|---|---|---|
| 3.5.x | May 2025 | June 2026 | June 2032 |
| 4.0.x | November 2025 | December 2026 | December 2027 |
| 4.1.x | June 2026 | July 2027 | July 2028 |

**The modern transition preserves the pattern.** Framework 7 and Boot 4 continue adapting application infrastructure to current JDK and Jakarta ecosystems rather than introducing a replacement for Spring’s core object model. For developers, version selection is therefore simultaneously a language, API, library, server, and maintenance decision.

## Essential knowledge for developers working with Spring

### Java, object design, annotations, and reflection

**Java fundamentals remain the first prerequisite.** Developers should be comfortable with classes, constructors, interfaces, generics, collections, exceptions, and resource management. Concurrency also matters because application services and infrastructure objects are frequently shared. Spring can assemble these objects, but it cannot make their Java behavior correct through configuration alone. [12]

**Object design determines injection quality.** Constructor dependencies expose what an object requires, while interfaces can define stable collaboration boundaries. This makes it easier to replace infrastructure in tests or change implementations through configuration. An interface is not mandatory for every class, but understanding interfaces, implementation types, and method visibility is important both for application design and proxy behavior. [24][31]

**Annotations are metadata, not executable promises.** `@Component`, `@Bean`, `@Profile`, request mappings, and `@Transactional` describe roles or intended behavior. A corresponding Spring processor, configuration, or interceptor must interpret that metadata in the relevant context. Developers should be able to explain which mechanism consumes an annotation and when, rather than treating the annotation itself as the implementation. [12]

**Reflection explains important runtime behavior.** Reflection allows Java code to inspect classes and members and access or invoke them dynamically. Spring’s testing documentation explicitly connects reflective access with non-public injection points and lifecycle callbacks, while its AOT documentation discusses runtime hints for reflection and proxies. This knowledge helps explain behavior that is not apparent from direct constructor and method calls in application source. [25]

**Reflection and proxies are different mechanisms.** Reflection concerns dynamic inspection and access; a proxy is an intervening object through which calls pass. Spring can also inspect bytecode metadata and perform build-time processing, so not every discovery operation should be described as reflective class loading. Java module access rules, retained parameter names, and generated proxies become especially relevant when diagnosing framework integration or native-image builds. [12][15]

**AOT changes some configuration timing.** Ahead-of-time processing can move discovery and bean-graph decisions from startup to build time. In that model, classpath and conditions affecting bean presence need to be settled for the generated arrangement; configuration values unrelated to bean selection are a separate concern. Teams using native images should understand this boundary rather than assuming every runtime profile change can reconstruct an arbitrary application graph. [25]

### HTTP, REST, and the selected web stack

**HTTP knowledge governs controller correctness.** A developer should understand request methods, paths, query parameters, headers, bodies, response status codes, cookies, and sessions. Spring maps those protocol elements into Java method arguments and return values, but the API still has an externally observable HTTP contract. A method returning the expected Java object is only part of correct endpoint behavior. [21]

**REST is more than JSON output.** Resource-oriented paths, appropriate method semantics, meaningful status codes, and consistent error representations require deliberate design. `@RestController` provides response-body handling; it does not establish those design decisions automatically. Developers should also know where conversion, validation, authentication, and exception mapping occur along the request path. [36]

**Stack selection changes the dependency contract.** For MVC, understand Servlet filters, `DispatcherServlet`, controller invocation, and the selected response path. For WebFlux, additionally understand reactive composition, cancellation, demand, and the consequences of blocking work. A reactive HTTP client can be useful inside an MVC application without forcing a migration of the server stack. [14]

### Configuration, profiles, scopes, and builds

**Configuration is part of program behavior.** Developers need to understand explicit bean definitions, component scanning, conditional configuration, and dependency resolution. When several beans match one dependency, qualifiers, primary candidates, or explicit wiring determine the intended collaborator. Package layout also matters because Boot’s repository and application discovery conventions are centered on its configuration packages. [12][40]

**Profile ordering can change deployment behavior.** Boot loads configuration from multiple property sources; profile-specific files override corresponding non-profile-specific files, and multiple profiles use a last-wins strategy for conflicting values. The active-profile setting itself follows property-source precedence, so a command-line setting can replace one in a configuration file. Developers should be able to explain the effective value, not merely identify one file containing it. [48][49]

**Structured configuration improves clarity.** `@ConfigurationProperties` binds related settings into a typed object rather than scattering individual string lookups throughout services. Profile groups can combine related environment concerns, such as production database and messaging configurations. These mechanisms help separate deployment choices from business code while keeping the configuration model understandable. [48][49]

**Externalized secrets still need protection.** Moving a password into a YAML file or environment variable does not encrypt it. Boot does not provide built-in property-value encryption; its documentation describes extension points and secure external configuration integrations such as Spring Cloud Vault. Configuration ownership, secret delivery, and diagnostic exposure must be considered together. [48]

**Build competence prevents runtime surprises.** Developers need Maven or Gradle dependency graphs, transitive dependencies, scopes, version management, and Boot’s packaging integration. A compile-time API and its runtime implementation must agree with the selected Java and Jakarta generation. Inspecting the actual resolved dependencies is often more informative than inspecting the version written beside one direct dependency. [42]

**Scope and startup choices deserve review.** The earlier lifecycle rules become practical questions: is this mutable object shared, who closes this resource, and does initialization trigger expensive infrastructure too early? Boot’s Servlet registration guidance specifically warns that filters, Servlets, and listeners are installed early and should avoid unintentionally forcing eager database or JPA initialization. [46]

### Persistence and transaction reasoning

**SQL knowledge remains essential.** JDBC users need to understand statements, parameters, result mapping, and connection ownership; JPA users additionally need entity mappings, persistence-context behavior, and the queries their provider executes. A repository abstraction can reduce repetitive code without eliminating database constraints, query costs, or concurrency behavior. [25]

**Transaction boundaries should match business operations.** A developer should be able to identify the entry call into the transactional proxy, the selected transaction manager, participating resources, propagation behavior, and rollback rules. `REQUIRED`, for example, expresses participation in an existing transaction or creation of one when needed; `REQUIRES_NEW` expresses a distinct transaction boundary. These choices affect correctness and resource use, not just annotation style. [35]

**Failure handling must preserve intended semantics.** If a service catches an exception and returns normally, the transaction interceptor sees a different outcome than if the failure escapes. Likewise, a call made internally rather than through the configured proxy may have different infrastructure behavior. Reviewing these paths is more valuable than simply checking that `@Transactional` appears somewhere on the class. [23][31]

### Tests should verify the boundary in question

**Unit tests verify ordinary behavior.** Constructor injection allows a service to be instantiated directly with test collaborators. Such tests should focus on business decisions and failure handling without requiring an application context. They deliberately do not prove that Spring discovers the bean, applies a proxy, or maps an HTTP request correctly. [25]

**Context tests verify actual assembly.** TestContext-based integration tests check whether the configured objects work together and whether infrastructure such as mappings or queries behaves as expected. Context caching reduces repeated startup work when tests share equivalent configuration. This makes a focused integration test a different instrument from both a plain unit test and a deployed end-to-end test. [39]

**Boot adds focused and full-context options.** Test slices such as `@WebMvcTest` and `@DataJpaTest` narrow the configured application to a particular concern, while `@SpringBootTest` creates a Boot-aware context. Slice filtering follows component-scanning rules, so explicitly declared configuration may require deliberate imports. A slice should be selected because it matches the behavior being tested. [54][55]

| `@SpringBootTest` mode | Web environment | Server started? | Appropriate focus |
|---|---|---|---|
| `MOCK` | Mock web environment | No | Framework-level web integration |
| `RANDOM_PORT` | Real server on an available port | Yes | HTTP and server interaction |
| `DEFINED_PORT` | Real server on configured/default port | Yes | Fixed-port integration needs |
| `NONE` | Non-web application context | No | Non-web Boot application behavior |

**A full context need not start HTTP.** `MOCK` is the default `@SpringBootTest` mode, whereas `RANDOM_PORT` and `DEFINED_PORT` start embedded servers. MockMvc can exercise MVC request handling without that server, but container-specific behavior—such as the container’s error-page dispatch—requires a test boundary that includes the real runtime. [56]

**Database cleanup follows execution boundaries.** TestContext rolls back tests configured with test-managed transactions by default. An HTTP call to a running server is not the same execution boundary as directly invoking a bean inside the test’s transaction. Developers should therefore design setup and cleanup around where the application work actually executes, rather than assuming one test annotation undoes every server-side effect. [39]

**Security belongs in the test contract.** A successful response for an authenticated user proves little about anonymous access or another user’s permissions. Spring Security provides dedicated test support, including distinct servlet and reactive paths. Tests should exercise the real configured rules at the appropriate boundary, not merely bypass them to reach the controller. [57][58]

### Security requires identity, permissions, and configuration ownership

**Authentication and authorization are different.** Authentication establishes the caller’s identity; authorization decides what that caller may do. In a hypothetical order system, recognizing a customer does not establish permission to read every customer’s orders. Secure application behavior requires rules that connect identity to resources and operations, not merely a login mechanism.

**The security model follows the stack.** Servlet applications use `SecurityFilterChain` and related authentication components such as `UserDetailsService`. Reactive applications use `SecurityWebFilterChain` and reactive counterparts. These facilities belong to Spring Security; Boot supplies conditional configuration around them when the relevant dependencies are present. [59]

**Custom beans change default ownership.** Defining a `SecurityFilterChain` replaces Boot’s default web security arrangement, leaving the application responsible for its access rules. Supplying authentication-related beans can separately replace the default user configuration. These are specific back-off decisions, so “we added custom security” should prompt a review of the resulting chains and rules, including management endpoints. [60]

**Dependencies can affect security behavior.** HeroDevs’ April 2026 analysis reported CVE-2026-40976 in Boot 4.0.0–4.0.5 under a specific combination: a Servlet application relying on the default security chain, Actuator auto-configuration present, and the health module absent. It reported the authorization-bypass fix in Boot 4.0.6. The practical lesson is to test endpoint protection against the delivered dependency arrangement and maintain patched versions. [61]

### Observability and deployment complete application competence

**Operational signals answer different questions.** A health endpoint, a readiness probe, and a latency metric are not interchangeable statements that “the system works.” Their usefulness depends on which condition they measure and which automated or human decision consumes the result. Actuator supplies infrastructure for these signals; developers must connect them to application responsibilities. [50]

| Signal | Question answered | Example decision |
|---|---|---|
| Component health | Does the selected check pass? | Investigate a failing dependency |
| Liveness | Does this process need restarting? | Restart an unrecoverable local process |
| Readiness | Should this replica receive traffic? | Remove or restore traffic |
| Metrics | What are volume and latency trends? | Diagnose capacity or degradation |
| Traces | Where did a request spend time? | Follow work across components |

**A green dependency can hide failed work.** DevDojo’s Boot 4.1 example explains that the automatic RabbitMQ health indicator reads the broker’s version property and reports success when the broker responds. It does not count consumers or queued messages. A reachable broker with zero consumers can therefore remain healthy while application work stalls; queue processing requires its own operational signal. [41]

**Probe design can amplify failures.** Liveness should describe the local process rather than automatically include shared databases, queues, or external APIs. Otherwise, a shared dependency outage can trigger restarts of otherwise functioning replicas. Readiness is the place to consider traffic eligibility, but including a shared dependency also means accepting that its failure may remove every replica from traffic. [41]

**Endpoint access has several gates.** Actuator distinguishes whether an endpoint is available, whether it is exposed over HTTP or JMX, and who is authorized to use it. Only health is exposed by default in the documented arrangement; adding Spring Security and custom chains changes the relevant protection rules. Sensitive diagnostic endpoints should have deliberate exposure and authorization policies rather than being published simply because they exist. [62]

**Observability needs meaningful dimensions.** Spring’s Micrometer Observation integration can connect instrumentation to metrics, traces, and logs. The Spring Observability Team illustrates an important distinction: a templated route such as `/user/{userId}` is a bounded metric dimension, whereas individual user-specific URLs create unbounded cardinality. Good instrumentation describes behavior without turning every unique request into a separate metric series. [63]

**Deployment knowledge includes packaging details.** Traditional Boot WAR deployment uses `SpringBootServletInitializer` and compatible container dependencies. The deployment guide specifically distinguishes Gradle’s `providedRuntime` from `compileOnly`, since missing test-classpath dependencies can break web integration tests. Executable JARs, external-container WARs, and native images consequently require different build and runtime assumptions. [47]

**Operational competence closes the loop.** Developers should be able to explain what starts the process, which server and JVM it uses, where configuration originates, what is exposed, what health means, and how updates are delivered. That knowledge turns a locally successful application into a maintainable production service.

### A practical learning sequence

| Order | Knowledge area | Be able to explain | Why it matters |
|---|---|---|---|
| 1 | Java and object design | Constructors, interfaces, exceptions, metadata | Predict ordinary object behavior |
| 2 | HTTP and web stack | Request mapping, responses, MVC versus WebFlux | Design correct external contracts |
| 3 | Container and configuration | DI, scopes, lifecycle, profiles, precedence | Predict runtime assembly |
| 4 | Build and persistence | Dependency graphs, JDBC/JPA, transactions | Preserve compatibility and data correctness |
| 5 | Testing and security | Test boundaries, identity, access rules | Verify behavior and protection |
| 6 | Production operation | Packaging, probes, metrics, traces, support | Diagnose and maintain deployed applications |

**The learning goal is prediction.** A competent Spring developer can explain why a particular bean exists, why a request reaches a method, why advice does or does not run, and why the deployed application reports a particular operational state.

## Servlets, Spring Framework, and Spring Boot compared

**The alternatives occupy nested layers.** The following comparison concerns what each layer contributes directly. A Servlet application can use additional libraries, a Spring application can use an embedded server without Boot, and a Boot application can retain custom Servlets. The distinction is which responsibilities the selected layer standardizes. [21][2]

| Dimension | Direct Servlet programming | Spring Framework without Boot | Spring Boot application |
|---|---|---|---|
| Abstraction level | HTTP and container API | Application objects and infrastructure | Opinionated Spring application assembly |
| Request handling | Servlet service methods | MVC dispatch or WebFlux | Configured Spring web stack |
| Configuration | Mappings and container setup | XML/Java configuration; context setup | Conditional defaults; external configuration |
| Dependency management | Chosen build/container policy | Selected modules and compatible libraries | Starters and curated managed versions |
| Deployment/runtime | Servlet container; commonly WAR | Stand-alone or container deployment | Executable JAR; Servlet WAR option |
| Testing | Java tests; chosen web fixtures | POJO tests, TestContext, web tools | Slices, Boot context, real-server modes |
| Operations | Application and container facilities | Framework hooks and selected integrations | Actuator and observability configuration |
| Developer productivity | Explicit low-level implementation | Reusable infrastructure and declarative services | Less repeated setup and packaging |
| Main tradeoff | Control versus application assembly | Flexibility versus configuration responsibility | Convention versus conditional complexity |

**Request handling shows the continuity.** In a typical Servlet-based Boot application, the path is still HTTP request → container and filters → `DispatcherServlet` → controller → application service. Boot changes how the infrastructure is assembled and started; Spring MVC changes how application handlers participate in that infrastructure. That relationship explains why Servlet knowledge remains useful after adopting both Spring and Boot. [21]

**Testing shows the rise in abstraction.** Direct Servlet behavior can be tested with suitable request and response fixtures or a running container. Spring adds explicit support for application-context wiring and framework-managed web behavior, and Boot adds application-aware configuration, focused slices, and server-starting modes. The progression improves the available verification tools without making one test scope sufficient for every concern. [21][56]

**Productivity comes from removed decisions.** Servlets remove server-extension inconsistency; Spring removes repeated object wiring and infrastructure implementation; Boot removes repeated choices about common dependency combinations, startup, packaging, and management. Those are observable reductions in assembly responsibility, not a universal throughput ranking. A workload’s runtime behavior still follows its database, network calls, algorithms, concurrency model, and configuration.

**The choice follows concrete constraints.** Direct Servlet APIs are appropriate for container-level components and specialized handling. Framework-only assembly is attractive when explicit infrastructure composition is itself a requirement. Boot is a strong default for a supported, repeatable Spring application runtime, while external-server policies, legacy integration, reactive deployment boundaries, or specialized transaction requirements can change the preferred arrangement. [47][23]

**Historical precision follows each source’s basis.** JCP entries for EJB 2.0 on 20 February 2002, Servlet 2.4 on 11 September 2007, EJB 3.0 on 14 November 2007, and Servlet 3.0 on 9 March 2011 describe maintenance stages. The 2006 capability scores are authors’ 0–1 assessments, made while EJB 3.0 was a proposed final draft; productivity comparisons here are qualitative. Compatibility and support describe the September 2026 snapshot, with future Boot support horizons attributed to Vega’s published table. [9][8][53]

**The enduring conclusion is cumulative.** Servlets supplied the web execution foundation; JSP and MVC improved separation; EJB and Java EE standardized enterprise services; Spring made those services easier to compose around testable Java objects; Boot made the resulting applications easier to assemble and operate. Learning Spring well means understanding both the abstractions it provides and the lower-level responsibilities those abstractions continue to organize.

## References

[1] <https://docs.oracle.com/javaee/5/tutorial/doc/bnafd.html> Servlet origins; Oracle’s Servlet introduction; Servlet concurrency and shared resources
[2] <https://docs.spring.io/spring-framework/reference/overview.html> Spring history; Framework overview; Spring’s relationship with enterprise standards; Spring project boundaries; Spring’s description of Boot; Spring’s modular…
[3] <https://cacm.acm.org/blogcacm/the-confounding-saga-of-java-web-application-development/> Java web chronology; Web framework timeline; Servlets’ low-level role; The Servlet-to-JSP transition; JSP’s historical role; Struts chronology; Framework chron…
[4] <https://link.springer.com/chapter/10.1007/978-3-540-24655-8_77> Web design-model comparison; The 2004 study; Design-model comparison
[5] <https://www.jcp.org/en/jsr/detail?id=53> Servlet 2.3 and JSP 1.2
[6] <https://jcs.ep.jhu.edu/legacy-ejava-javaee/coursedocs/content/html/javaeeintro-javaee-versions.html> J2EE version highlights; Java EE version highlights; Java EE 7 highlights
[7] <https://www.infoq.com/podcasts/johnson-spring-framework/> Johnson’s account
[8] <http://ecet.ecs.uni-ruse.bg/cst06/Docs/cp/SIII/IIIA.18.pdf> 2006 enterprise-framework comparison; Contemporary EJB assessment; EJB 3 simplification mechanisms; The 2006 scorecard; Historical assessment
[9] <https://www.jcp.org/en/jsr/tech?listBy=3&listByType=platform> JCP milestones; EJB specification descriptions; EJB 3’s stated purpose; JCP stage records
[10] <https://www.jcp.org/en/jsr/detail?id=316> Java EE 6; Java EE 6’s rationale
[11] <https://www.jcp.org/en/jsr/detail?id=366> Java EE 8; Java EE 8 scope
[12] <https://docs.spring.io/spring-framework/docs/5.3.x/reference/html/core.html> Spring configuration history; Container independence; Beans and definitions; Singleton semantics; Events and Spring Integration; Spring configuration milestone…
[13] <https://spring.io/blog/2014/04/01/this-week-in-spring-spring-boot-edition-april-1st-2014> Boot’s GA announcement
[14] <https://docs.spring.io/spring-framework/reference/web/webflux.html> WebFlux history; WebFlux architecture; MVC and WebFlux coexistence
[15] <https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-6.0-Release-Notes> Framework 6 migration; Framework 6 integration changes; Framework 6 migration notes; Jakarta migration scope; Parameter-name guidance
[16] <https://spring.io/blog/2025/11/13/spring-framework-7-0-general-availability> Framework 7.0 announcement; Framework 7’s focus
[17] <https://docs.oracle.com/cd/A97688_16/generic.903/a97679/tecbkgnd.htm> Servlet technical background; Container-managed lifecycle
[18] <https://blog.doubleslash.de/en/software-technologien/jee-vs-spring-similarities-differences-and-decision-criteria> Enterprise containers; Java EE architecture and services
[19] <https://www.oracle.com/java/technologies/javaee/javaeetechnologies.html> Oracle’s JSP and JSTL descriptions; Oracle’s JSF model; JSF components and events; Oracle’s JPA definition; Bean Validation’s model; JMS’s role
[20] <https://www.codemag.com/Article/1405001/Java-Servlets-and-JSP> Model 1’s responsibilities; Model 2’s structure; Model 2 request processing
[21] <https://docs.spring.io/spring-framework/docs/5.3.34/reference/html/web.html> Spring’s account of Struts; Spring’s layered integration model; Third-party web-framework integration; JSF integration boundaries; Spring MVC architecture; Ann…
[22] <https://static.spring.io/drupal/files/MigratingAppsToSpring.pdf> Traditional EJB artifacts; Spring’s migration rationale; Spring’s enterprise-service model; Incremental adoption and migration costs; Portfolio responsibilities
[23] <https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html> Remote transaction boundaries; Declarative transactions; Rollback and declarative semantics; Remote-call boundary; Declarative transaction behavior; Transactio…
[24] <https://docs.spring.io/spring-framework/reference/core/beans/introduction.html> Spring’s IoC definition; Container interfaces; DI contracts
[25] <https://docs.spring.io/spring-framework/docs/6.0.0/reference/pdf/spring-framework.pdf> DI and testable objects; JDBC responsibilities; Reactive Streams motivation; WebFlux’s motivation; Reflection and AOT facilities; Spring AOT restrictions; Spri…
[26] <https://docs.spring.io/spring-framework/reference/core/beans/java/basic-concepts.html> Java-based bean definitions
[27] <https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html> Bean scopes; Prototype lifecycle and injection
[28] <https://docs.spring.io/spring-framework/reference/core/beans/factory-nature.html> Lifecycle facilities
[29] <https://docs.spring.io/spring-framework/reference/core/aop.html> Spring AOP
[30] <https://docs.spring.io/spring-framework/reference/core/aop/introduction-defn.html> AOP concepts
[31] <https://docs.spring.io/spring-framework/reference/core/aop/proxying.html> Proxy mechanisms; Self-invocation behavior; Proxy restrictions and weaving; Proxy design constraints; Proxy call paths
[32] <https://docs.spring.io/spring-framework/reference/index.html> Data-access functionality; Spring testing facilities
[33] <https://docs.spring.io/spring-framework/reference/data-access/dao.html> DAO support and exception translation
[34] <https://doi.org/10.25136/2306-4196.2019.2.19589> Connection-management comparison
[35] <https://docs.spring.io/spring-framework/reference/data-access/transaction.html> Spring transaction management; Transaction abstraction
[36] <https://docs.spring.io/spring-boot/reference/web/servlet.html> Boot’s MVC reference; Controllers and response handling
[37] <https://docs.spring.io/spring-framework/reference/core/validation.html> Spring validation; Binding and conversion facilities
[38] <https://docs.spring.io/spring-framework/reference/integration.html> Spring integration facilities; Spring’s messaging support
[39] <https://docs.spring.io/spring-framework/reference/testing/integration.html> TestContext integration support; Integration-test goals; Test-managed transactions
[40] <https://docs.spring.io/spring-boot/how-to/data-access.html> Repository integration; Repository scanning
[41] <https://devdojo.academy/en/blog/spring-boot-actuator-production-endpoints-health/> AMQP application example; RabbitMQ health semantics; Liveness and readiness consequences
[42] <https://docs.spring.io/spring-boot/docs/asciidoctor/html/> Boot’s design goals; Web annotation ownership; Boot’s build and dependency model; Starters and managed dependencies; Curated dependency versions; Executable JA…
[43] <https://www.oracle.com/database/spring-boot/> Configuration-choice pressure; Oracle’s comparison
[44] <https://docs.spring.io/spring-boot/reference/using/auto-configuration.html> Boot auto-configuration; Auto-configuration back-off; Diagnosing and excluding configuration; Boot customization model
[45] <https://docs.spring.io/spring-boot/reference/using/configuration-classes.html> Boot configuration guidance
[46] <https://docs.spring.io/spring-boot/how-to/webserver.html> Embedded-server selection; Early web-component initialization
[47] <https://docs.spring.io/spring-boot/how-to/deployment/traditional-deployment.html> Traditional deployment boundaries; Traditional deployment mechanics; Deployment choices
[48] <https://docs.spring.io/spring-boot/reference/features/external-config.html> Externalized configuration; Configuration precedence; Property binding; Property encryption boundary
[49] <https://docs.spring.io/spring-boot/reference/features/profiles.html> Profiles; Profile activation; Profile groups
[50] <https://docs.spring.io/spring-boot/reference/actuator/index.html> Production-ready features; Actuator management model
[51] <https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-Versions> Spring compatibility matrix; Framework support ranges
[52] <https://spring.io/blog/2026/06/25/spring-boot-3-5-16-available-now> Boot 3.5.16 announcement
[53] <https://www.danvega.dev/blog/spring-boot-end-of-life> Vega’s support table; Support schedule
[54] <https://docs.spring.io/spring-boot/reference/testing/index.html> Boot testing support
[55] <https://docs.spring.io/spring-boot/how-to/testing.html> Slice-test boundaries
[56] <https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html> Boot web-test modes; Boot test modes
[57] <https://docs.spring.io/spring-security/reference/servlet/test/index.html> Servlet security testing
[58] <https://docs.spring.io/spring-security/reference/reactive/test/index.html> Reactive security testing
[59] <https://docs.spring.io/spring-boot/reference/web/spring-security.html> Boot’s security paths
[60] <https://docs.spring.io/spring-boot/how-to/security.html> Security customization and back-off
[61] <https://www.herodevs.com/blog-posts/cve-2026-40976-spring-boot-4-0-actuator-authorization-bypass> The reported Actuator dependency-state vulnerability
[62] <https://docs.spring.io/spring-boot/reference/actuator/endpoints.html> Actuator endpoint controls
[63] <https://spring.io/blog/2022/10/12/observability-with-spring-boot-3> Spring observability and cardinality
