# **The Evolution of Enterprise Java: From Servlets to Cloud-Native Spring Boot 3** 

The architecture of enterprise Java applications has undergone a radical transformation over the past two decades. The initial abstraction of Java Servlets provided a robust, multi-threaded mechanism for handling HTTP requests and responses, effectively replacing the cumbersome and resource-intensive Common Gateway Interface (CGI) scripts of the early web. However, as enterprise business logic grew increasingly complex, raw Servlets proved insufficient for coordinating distributed transaction management, implementing role-based security, and mapping object-oriented models to relational databases. 

To address these systemic enterprise requirements, Sun Microsystems introduced the Java 2 Platform, Enterprise Edition (J2EE). J2EE promised a highly standardized, distributed architecture based on Enterprise JavaBeans (EJBs). While conceptually ambitious, J2EE imposed massive operational and developmental overhead. Developing a simple database call using the EJB 2.0 specification required a developer to create a remote interface, a home interface, a bean implementation, and complex XML deployment descriptors<sup>1</sup> . The architecture relied heavily on the Java Naming and Directory Interface (JNDI) for component lookups and handled system exceptions poorly, resulting in fragile, bloated codebases<sup>1</sup> . 

The industry subsequently entered what is retrospectively referred to as the "J2EE Winter"<sup>3</sup> . Applications developed under orthodox J2EE paradigms were unduly complex, slow to start, exceptionally difficult to test out-of-container, and consistently failed to deliver timely business value<sup>5</sup> . The pervasive assumption baked into J2EE—that enterprise components must be natively distributed across multiple physical tiers—was a severe architectural mismatch for the reality that most web applications were simply co-located and bound by singular relational databases<sup>5</sup> . 

## **The Genesis of the Spring Framework: Reclaiming Control with POJOs** 

The enterprise paradigm shifted significantly in October 2002 when Australian developer and architect Rod Johnson published the seminal architectural text, _Expert One-on-One J2EE Design and Development_<sup>4</sup> . With extensive experience as a C and C++ developer before moving to server-side Java in 1996, and operating as a consultant in the finance and insurance sectors, Johnson had experienced the friction of J2EE firsthand<sup>8</sup> . His central thesis challenged the conventional wisdom propagated by major vendors: he argued that the problem was not J2EE's underlying APIs, but rather the orthodox, bloated implementations that forced developers into EJB anti-patterns<sup>5</sup> . 

Accompanying the book was approximately 30,000 lines of framework code, initially placed under the package namespace com.interface21<sup>3</sup> . This code practically demonstrated that enterprise-grade features could be delivered without heavy EJB containers by relying strictly on Plain Old Java Objects (POJOs)<sup>1</sup> . In February 2003, Johnson, along with core developers 

Juergen Hoeller and Yann Caroff, open-sourced this framework under the Apache 2.0 license<sup>6</sup> . Caroff suggested the name "Spring," symbolizing a fresh, natural start following the harsh winter of traditional J2EE development<sup>3</sup> . By 2005, the framework had recorded over two million downloads, rapidly establishing itself as the de facto standard for enterprise Java<sup>9</sup> . The core philosophy of the early Spring Framework relied on two foundational architectural patterns: Inversion of Control (IoC) and Aspect-Oriented Programming (AOP). Instead of components actively looking up their dependencies via JNDI registries, the Spring framework acted as an IoC container, instantiating components—referred to as "beans"—and injecting their required dependencies at runtime<sup>1</sup> . This Dependency Injection (DI) eliminated tight coupling and enabled robust unit testing through dependency mocking<sup>1</sup> . Simultaneously, cross-cutting concerns—such as logging, transaction management, and security, which were previously decentralized and highly repetitive—were isolated into "aspects" and woven into the business logic dynamically<sup>1</sup> . 

## **Architecting the Web Layer: Spring MVC and the DispatcherServlet** 

As the core IoC container matured, the framework expanded to encompass the entire web request lifecycle through the Spring Web MVC module. Rather than forcing developers to map dozens of individual Servlets in a massive web.xml deployment descriptor, Spring MVC was designed entirely around the Front Controller pattern<sup>11</sup> . 

The DispatcherServlet serves as this central orchestrator. It intercepts all incoming HTTP requests and meticulously manages the entire request-processing lifecycle<sup>13</sup> . The architectural flow is highly decoupled, ensuring that business controllers never directly interact with raw Servlet APIs unless absolutely necessary. 

The lifecycle executes as follows: 

1. **Interception:** The DispatcherServlet receives the raw HTTP request from the embedded or external servlet container (such as Tomcat or Undertow)<sup>13</sup> . 

2. **Routing:** It delegates the request to a HandlerMapping strategy. The HandlerMapping inspects the URL, HTTP method, and headers to determine which specific Controller (or handler method) is configured to process the request<sup>17</sup> . 

3. **Execution:** Because handlers can take many forms, an appropriate HandlerAdapter is selected to invoke the controller. The controller executes the domain business logic and returns a model alongside a logical view name (in traditional server-rendered applications) or serializes the model directly into a JSON payload (in modern REST architectures utilizing @ResponseBody or @RestController)<sup>19</sup> . 

4. **Resolution:** If a logical view is returned, a ViewResolver maps the logical string to a physical view template (e.g., Thymeleaf, JSP) to render the final HTML response<sup>20</sup> . 

This architecture not only eliminated Servlet API lock-in from business controllers but also established a lifecycle where interceptors could be globally applied to pre-process or post-process requests, fundamentally altering how enterprise Java web layers were constructed. Configuration of this environment occurs within the DispatcherServlet's own WebApplicationContext, providing a robust boundary between web-specific beans and root-level application services<sup>21</sup> . 

## **The Mechanics of Aspect-Oriented Programming (AOP)** 

At the heart of Spring's capability to manage declarative services—such as transactions, method-level security, and caching—is its Aspect-Oriented Programming (AOP) framework. AOP allows developers to weave "cross-cutting concerns" into various program modules without modifying the core business logic, relying exclusively on the Proxy Pattern<sup>1</sup> . When a Spring bean is instantiated, the framework determines if any AOP advice (e.g., @Transactional, @Cacheable) applies to it. If so, Spring does not return the raw bean instance to the calling client; instead, it dynamically generates and returns a proxy object<sup>22</sup> . This proxy intercepts method calls, executes the necessary advice (before, after, or around the target method), and then delegates the call to the actual target object<sup>22</sup> . 

Spring utilizes two primary mechanisms for proxy generation, each with distinct operational constraints: 

**Feature JDK Dynamic Proxy CGLIB Dynamic Proxy** 

|**Prerequisite Architecture**|The target class must<br>implement at least one<br>interface<sup>10</sup>.|Can proxy target classes<br>that do not implement any<br>interfaces<sup>10</sup>.|
|---|---|---|
|**Implementation**<br>**Mechanism**|Utilizes native Java<br>Reflection<br>(java.lang.reflect.Proxy) to<br>dynamically generate a<br>class implementing the<br>target's interfaces<sup>10</sup>.|Utilizes bytecode<br>manipulation (via ASM) to<br>dynamically generate a<br>subclass of the target class<br>at runtime<sup>10</sup>.|
|**Framework Default Usage**|Historically the default if an<br>interface was present.|The default proxy<br>mechanism since Spring<br>Boot 2.x for all AOP proxies<br>(including @Transactional),<br>regardless of interface<br>presence<sup>22</sup>.|
|**Performance Overhead**|Generally higher<br>performance when proxying<br>interfaces directly<sup>10</sup>.|Introduces a ~15-25%<br>overhead due to<br>subclassing, though highly<br>optimized for heavy method<br>call volumes<sup>10</sup>.|
|**Technical Limitations**|Can only intercept and<br>apply advice to methods<br>defined on the implemented<br>interface<sup>10</sup>.|Cannot proxy final classes<br>or override final methods.<br>Target constructors may be<br>bypassed via Objenesis<sup>23</sup>.|

### **The Proxy Self-Invocation Limitation** 

A critical architectural limitation of proxy-based AOP is the "self-invocation" bypass. When an external client calls a proxied method, the proxy successfully intercepts the call and applies the advice<sup>22</sup> . However, if a method within the target object calls _another_ method within the same object using the implicit or explicit this reference, the call executes directly on the raw target instance, completely bypassing the proxy and its associated AOP advice<sup>22</sup> . Consequently, a public method calling an internal @Transactional, @CachePut, or @Async method will execute without a transaction, without updating the cache, or synchronously, respectively<sup>22</sup> . 

To circumvent this limitation, developers must force the internal call to route through the external proxy. The preferred architectural solution is to refactor the codebase, moving the advised method to a separate Spring service bean<sup>26</sup> . When refactoring is unfeasible, developers frequently rely on self-injection, injecting a @Lazy reference of the bean into itself to force the 

call back through the proxy container<sup>23</sup> . 

Alternatively, Spring provides a programmatic escape hatch via AopContext.currentProxy(). If proxy exposure is explicitly enabled via @EnableAspectJAutoProxy(exposeProxy = true), developers can cast the current proxy and execute the call: 

<mark>Java public void processOrder() { // Casting the current proxy allows the internal call to be intercepted ((OrderService) AopContext.currentProxy()).updateInventory();</mark> } 

However, the use of AopContext.currentProxy() is widely considered an anti-pattern. It tightly couples domain business logic to the Spring AOP framework infrastructure, making the class explicitly aware that it operates within an AOP context, which heavily degrades the decoupling benefits of Inversion of Control<sup>24</sup> . 

## **Orchestrating Declarative Transaction Management** 

One of the most profound simplifications Spring introduced was declarative transaction management, which largely rendered raw JDBC commits, rollbacks, and complex JTA (Java Transaction API) orchestration obsolete<sup>30</sup> . Spring abstracts transaction management through the @Transactional annotation, underpinned by a highly sophisticated, multi-layered architecture. 

The core mechanics of transaction orchestration involve several distinct components working in concert: 

1. **The AOP Interceptor (TransactionInterceptor):** When a @Transactional method is invoked, the proxy delegates to the TransactionInterceptor. This interceptor acts as the gatekeeper, utilizing AOP mechanics to read metadata and dictate transaction start, commit, or rollback events<sup>30</sup> . 

2. **The Orchestrator (TransactionAspectSupport):** This base class contains the core logic, specifically the invokeWithinTransaction() method. It evaluates the method's attributes (e.g., isolation levels, propagation rules, timeout limits) and interacts with the underlying transaction manager<sup>32</sup> . 

3. **The Contract (PlatformTransactionManager):** An interface that defines three essential methods: getTransaction(), commit(), and rollback(). Implementations such as DataSourceTransactionManager (for plain JDBC) or JpaTransactionManager (for Hibernate/JPA) implement the physical database coordination<sup>30</sup> . 

4. **The Context Registry (TransactionSynchronizationManager):** A static facade over Java ThreadLocal storage. It binds physical database connections and transaction state flags to the current thread. This ensures that multiple nested data access operations 

within the same logical transaction utilize the exact same physical database connection, without requiring developers to explicitly pass connection objects through method signatures<sup>32</sup> . 

### **Transaction Propagation Mechanics** 

Transaction propagation strictly dictates how a method execution behaves relative to existing transactional boundaries. The PlatformTransactionManager queries the thread-local TransactionSynchronizationManager context and acts according to the defined propagation attribute<sup>30</sup> : 

|**Propagation Level**|**Operational Behavior**|
|---|---|
|**REQUIRED (Default)**|If a transaction exists in the thread context,<br>the method joins it. If none exists, a new<br>transaction is created and bound to the<br>thread<sup>28</sup>.|
|**REQUIRES_NEW**|The interceptor suspends any existing<br>transaction and creates a completely new,<br>independent transaction with a new physical<br>database connection. Once complete, the<br>original transaction is resumed<sup>28</sup>.|
|**NESTED**|If a transaction exists, a database savepoint<br>is created. The nested transaction can roll<br>back to this savepoint upon failure without<br>aborting the outer transaction. If no<br>transaction exists, it behaves identically to<br>REQUIRED<sup>28</sup>.|
|**SUPPORTS**|The method executes within an existing<br>transaction if present. If absent, the method<br>executes non-transactionally, maintaining<br>atomicity without locking resources<sup>28</sup>.|
|**MANDATORY**|Mandates execution within an existing<br>transaction. If absent, the interceptor throws<br>a TransactionRequiredException<sup>28</sup>.|
|**NOT_SUPPORTED**|Always executes non-transactionally. If a<br>transaction exists, it is temporarily<br>suspended while the method executes<sup>28</sup>.|

|**NEVER**|Mandates execution outside of any|
|---|---|
||transaction. Throws an|
||IllegalTransactionStateException if an active|
||transaction is detected<sup>28</sup>.|

By combining proxy interception with thread-local resource binding and precise propagation logic, Spring allows developers to construct complex, multi-layered transactional architectures—ensuring strict ACID (Atomicity, Consistency, Isolation, Durability) properties—simply by annotating method signatures<sup>30</sup> . 

## **Bridging the Gap: The Spring Security Architecture** 

Security in enterprise applications historically required hardcoding logic within individual servlets or defining rigid authentication roles in application server deployment descriptors. Spring Security modernized this by implementing an elegant, ordered filter chain architecture that bridges standard Servlet lifecycle constraints with the power of the Spring IoC container<sup>34</sup> . Under standard Servlet specifications, filters defined in web.xml (or via Servlet 3.0 initializers) must be instantiated by the Servlet container (e.g., Tomcat, Jetty). Consequently, these standard servlet filters cannot inherently utilize Spring's Dependency Injection or bean lifecycle management capabilities<sup>34</sup> . 

Spring resolves this critical impedance mismatch using a specific class: the DelegatingFilterProxy. 

The DelegatingFilterProxy is registered with the underlying Servlet container as a standard web filter. However, it contains no security logic itself. Instead, its sole responsibility is to intercept incoming requests, query the Spring Application Context for a specific bean (usually named springSecurityFilterChain), and delegate the doFilter method to that Spring-managed bean<sup>34</sup> . The target bean is an instance of FilterChainProxy. The FilterChainProxy acts as an internal router and orchestration engine within the Spring ecosystem. It evaluates the incoming request's URI against defined security patterns and delegates the processing to one or more SecurityFilterChain instances<sup>37</sup> . Each SecurityFilterChain contains a sequence of actual Spring-managed security filters (e.g., UsernamePasswordAuthenticationFilter, BearerTokenAuthenticationFilter, AuthorizationFilter) configured for that specific URL pattern<sup>41</sup> . This architecture provides monumental advantages for enterprise security. It guarantees that the entire security mechanism can leverage dependency injection, allows for dynamic instantiation of filters, and enables the FilterChainProxy to act as a centralized firewall via HttpFirewall integration<sup>37</sup> . The proxy manages request rejection for malformed URLs, ensures URL normalization, and critically guarantees the consistent clearing of the SecurityContextHolder upon request completion, preventing data leakage between pooled threads<sup>40</sup> . 

## **The Spring Boot Revolution: Convention Over Configuration** 

While the original Spring Framework elegantly solved the architectural problems of J2EE, its massive success eventually led to a new form of complexity. By the late 2000s, enterprise 

Spring applications required excessive amounts of boilerplate configuration—initially sprawling XML files, and later, extensive Java @Configuration classes<sup>1</sup> . Developers spent days configuring database connection pools, transaction managers, JPA entity managers, and web servlets before writing a single line of business logic<sup>43</sup> . 

In 2014, Spring Boot was introduced to decisively solve this configuration fatigue. It structurally inverted the traditional Java web deployment model. Rather than packaging the application as a WAR file to be deployed into a standalone, externally managed Tomcat instance, Spring Boot embedded the web server directly into a standalone JAR file, initializing it programmatically on application startup<sup>1</sup> . The framework embraced "Convention over Configuration," relying on sophisticated auto-configuration mechanisms to wire up sensible default objects based purely on the presence of libraries on the application classpath<sup>1</sup> . 

### **The Mechanics of Auto-Configuration** 

Spring Boot's auto-configuration is not a black box of magic; it is a highly deterministic, ordered evaluation of conditionals. The startup process is initiated by SpringApplication.run(), which deduces the WebApplicationType (e.g., SERVLET, REACTIVE, or NONE), prepares the environment, and triggers SpringApplicationRunListeners<sup>45</sup> . 

The configuration injection itself is governed by the @SpringBootApplication annotation, a composite meta-annotation that includes @EnableAutoConfiguration<sup>43</sup> . The @EnableAutoConfiguration annotation imports a specialized class named AutoConfigurationImportSelector<sup>44</sup> . The exclusive job of this selector is to locate, filter, and load pre-written configuration classes provided by Spring Boot or third-party "starters"<sup>43</sup> . Crucially, Spring Boot does not arbitrarily scan the entire classpath—an operation that would be prohibitively slow and unpredictable<sup>43</sup> . Instead, it relies on static registry files embedded within the library JARs to identify candidate configurations. 

- **Prior to Spring Boot 2.7:** This registry was located in META-INF/spring.factories under the EnableAutoConfiguration key<sup>43</sup> . While functional, this file was a shared bucket used for many unrelated framework abstractions. 

- **Spring Boot 2.7 and 3.0+:** The architecture migrated to a dedicated file located at META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports<sup>43</sup> . This dedicated file substantially improved application load times by strictly separating auto-configuration entries into a flat list of class names<sup>43</sup> . 

Once the AutoConfigurationImportSelector compiles the list of candidate configuration classes, it acts as a DeferredImportSelector. This guarantees that all user-defined configurations and explicit component scans are evaluated _first_<sup>43</sup> . Subsequently, the auto-configuration classes are evaluated against conditional annotations. For example, @ConditionalOnClass evaluates if a required dependency like HikariCP is present, and @ConditionalOnMissingBean checks if the user has already explicitly defined a DataSource<sup>43</sup> . 

If a user provides their own bean, the conditional immediately fails, and Spring Boot elegantly "backs off." This deferred evaluation mechanism ensures custom user configurations always supersede the framework's opinionated defaults without requiring manual opt-out flags, providing a seamless "it just works" developer experience<sup>43</sup> . To optimize this process further, auto-configuration classes typically declare @AutoConfiguration(proxyBeanMethods = false), skipping CGLIB proxy creation to improve startup performance<sup>44</sup> . 

## **The Modern Frontier: Spring Boot 3, Cloud-Native, and** 

## **GraalVM** 

The release of Spring Boot 3 in November 2022 represented the most significant architectural baseline shift in the framework's modern history. Driven by the evolution of the wider Java ecosystem and the stringent performance demands of cloud-native computing—specifically Kubernetes deployments and Serverless architectures—Spring Boot 3 enforced rigid modernization requirements. 

### **The Jakarta EE Migration Impact** 

Spring Boot 3 mandated a baseline of Java 17, granting developers access to modern language features like records and sealed classes, and initiated a comprehensive migration from the traditional Java EE namespace to the new Jakarta EE 9+ standards<sup>49</sup> . In 2017, Oracle donated the governance of Java EE to the Eclipse Foundation. However, due to trademark restrictions on the "Java" name, the specification was rebranded as Jakarta EE, forcing a massive, mandatory namespace shift from javax.* to jakarta.*<sup>49</sup> . 

This was not merely a cosmetic update; it was an industry-wide breaking change. Every foundational enterprise API—including Servlet (javax.servlet to jakarta.servlet), JPA (javax.persistence to jakarta.persistence), and Bean Validation (javax.validation to jakarta.validation)—was fundamentally altered<sup>49</sup> . 

Developers migrating legacy Spring Boot 2.x applications to Spring Boot 3 faced complex transitive dependency conflicts if they utilized third-party libraries that had not yet updated their internal imports to the jakarta namespace<sup>49</sup> . Successful migration requires rigorous validation and dependency analysis, often utilizing automated refactoring tools like OpenRewrite or Eclipse Transformer to perform the widespread source code and bytecode transformations required to bridge the namespace gap<sup>53</sup> . 

### **AOT Processing and GraalVM Native Image Compilation** 

Historically, the Spring framework relied heavily on runtime reflection, dynamic AOP proxy generation, and aggressive classpath scanning. While this provided exceptional developer flexibility, it incurred significant penalties in application startup time (often 2–5 seconds) and 

baseline memory footprint (200–500MB)<sup>55</sup> . In modern cloud-native environments characterized by ephemeral containers and "scale-to-zero" serverless architectures, these performance metrics became a critical liability<sup>57</sup> . 

Spring Boot 3 resolved this by delivering first-class support for GraalVM Native Image generation<sup>59</sup> . GraalVM allows Java applications to be compiled ahead-of-time (AOT) into highly optimized, standalone, OS-specific binaries, stripping away the JVM entirely. This results in sub-100 millisecond startup times and memory footprints reduced by over 70%<sup>55</sup> . However, the GraalVM Native Image builder operates under a strict "Closed World" assumption: it must definitively know every execution path, every class loaded via reflection, and every dynamic proxy generated at _compile time_<sup>58</sup> . 

To bridge the gap between Spring’s inherently dynamic nature and GraalVM’s static requirements, Spring introduced a robust AOT processing pipeline. During the build phase, the spring-boot-maven-plugin executes the highly specific process-aot goal<sup>58</sup> . This goal triggers a dry-run initialization of the Spring Application Context. The framework evaluates all auto-configuration conditionals, processes all @Value and @ConfigurationProperties injections, and statically registers the outcomes<sup>58</sup> . 

Simultaneously, the AOT engine generates Java source code (hardcoded context initializers) and highly specific reachability metadata files (JSON files detailing required reflection endpoints, resource files, and proxies) that instruct the GraalVM compiler on how to safely compile the native executable<sup>58</sup> . This represents a profound architectural inversion for the framework: Spring shifts its heavy framework initialization logic from application runtime to application build time. **Concurrency Paradigms: WebFlux vs. Virtual Threads** 

As enterprise throughput demands scaled, the traditional synchronous, thread-per-request model (using standard Spring MVC deployed on Tomcat) struggled with I/O-bound workloads. OS threads blocked while waiting for database queries or remote API calls, rapidly exhausting system resources and degrading throughput<sup>65</sup> . 

To address this, Spring introduced Spring WebFlux (based on Project Reactor) in 2017<sup>66</sup> . WebFlux utilizes a non-blocking, event-loop execution model (similar to Node.js), drastically improving concurrency. However, reactive programming introduced a notoriously steep learning curve, viral API changes (forcing codebases to return Mono and Flux wrappers), and exceptionally complex debugging due to stack traces populated heavily by reactor internal asynchronous mechanics<sup>66</sup> . 

The introduction of Virtual Threads (Project Loom) in Java 21, fully supported natively in Spring Boot 3.2, offers a compelling, paradigm-shifting alternative<sup>67</sup> . Virtual Threads decouple virtual concurrency constructs from heavy, physical OS threads. When a virtual thread encounters a blocking I/O operation (like a JDBC query), the JVM seamlessly suspends it, moving its execution stack to the heap and freeing the underlying carrier OS thread to execute other incoming requests<sup>65</sup> . 

Engineers can now achieve massive concurrency using familiar, imperative Spring MVC and standard JPA code simply by enabling spring.threads.virtual.enabled=true in their application properties<sup>69</sup> . Recent benchmarking of high-throughput API endpoints (such as JWT verification 

and database querying utilizing tools like Bombardier) reveals nuanced performance characteristics between the two paradigms: 

|**Workload Condition**|**WebFlux (Project Reactor)**|**Virtual Threads (Java 21)**|
|---|---|---|
|**Standard Load (< 10,000**<br>**req/sec)**|Excellent performance,<br>highly efficient baseline<br>memory usage<sup>68</sup>.|Performance comparable to<br>WebFlux. Slightly higher<br>heap utilization due to the<br>mechanics of stack<br>offloading<sup>68</sup>.|
|**Extreme Burst Load**<br>**(60,000+ connections)**|Demonstrates severe<br>degradation at absolute<br>extremes if backpressure<br>isn't perfectly tuned; median<br>latency spikes significantly<br>(up to ~1.2s) with high GC<br>time<sup>67</sup>.|Retains exceptionally flat<br>median latency (~100ms)<br>on Netty. However,<br>Tomcat's thread pools can<br>struggle with extreme bursty<br>loads compared to Netty<sup>67</sup>.|
|**Developer Experience**|High cognitive load.<br>Debugging requires deep<br>expertise in reactive<br>streams and backpressure.<br>Ecosystem fragmentation<br>(e.g., using R2DBC instead<br>of JDBC)<sup>69</sup>.|Low cognitive load. Allows<br>standard imperative coding,<br>seamless integration with<br>traditional JPA/JDBC, and<br>utilizes standard JUnit<br>testing without<br>StepVerifier<sup>69</sup>.|

Industry consensus suggests that while WebFlux maintains an edge in niche, hyper-scale data streaming scenarios due to its native backpressure awareness, Virtual Threads combined with Spring MVC provide 80% of the scalability benefits at 20% of the architectural complexity for standard enterprise API services<sup>69</sup> . 

### **Cloud-Native Observability** 

Finally, Spring Boot 3 deeply enhances its cloud-native pedigree by integrating advanced distributed tracing directly via the Spring Boot Actuator module. Actuator now embeds Micrometer, a vendor-neutral metrics facade<sup>59</sup> . Beyond exposing basic Prometheus metrics, Micrometer has evolved to seamlessly support OpenTelemetry. This integration allows developers to automatically inject request-scoped spans and trace contexts across distributed microservices, feeding telemetry data directly into distributed tracing backends like Zipkin or Jaeger with minimal manual instrumentation<sup>59</sup> . 

The evolution of enterprise Java—from the cumbersome, bloated specifications of J2EE to the elegant, embedded, cloud-native binaries of Spring Boot 3—represents a masterclass in software engineering adaptation. Rod Johnson’s original vision of relying on lightweight POJOs, 

dependency injection, and aspect-oriented programming remains the unshakeable foundation of the framework. However, Spring has survived by continuously cannibalizing its own complexities. It replaced XML configuration with annotations, replaced manual dependency wiring with auto-configuration, replaced external application servers with embedded containers, and is now actively replacing heavy runtime reflection with Ahead-of-Time compilation. By aggressively embracing modern Java language features, standardizing on Jakarta EE, and seamlessly integrating Virtual Threads, the Spring ecosystem ensures it remains the dominant, highly performant force in the modern era of distributed enterprise software. 

#### **Works cited** 

1. How Spring Took Back Control from Enterprise Java: A Documentary, <u>https://medium.com/@jamilxt/how-spring-took-back-control-from-enterprise-java-a</u> 

   - -documentary-6bb61ec78eec 

2. Java Persistence with Hibernate - ISBN 1932394885.pdf, <u>https://theswissbay.ch/pdf/Gentoomen%20Library/Programming/Java/Java%20Pe rsistence%20with%20Hibernate%20-%20ISBN%201932394885.pdf</u> 

3. Spring Framework: The Origins of a Project and a Name, <u>https://spring.io/blog/2006/11/09/spring-framework-the-origins-of-a-project-and-a-n ame/</u> 

4. Spring Framework History: 2002 – Present (Updated 1st Oct 2017), <u>https://springtutorials.com/spring-framework-history/</u> 

5. Expert One-on-One J2EE Design and Development | Wiley, <u>https://www.wiley.com/en-us/Expert+One-on-One+J2EE+Design+and+Developme nt-p-9780764543852</u> 

6. Spring – Framework for Java applications - IONOS, <u>https://www.ionos.com/digitalguide/websites/web-development/spring-frameworka-backbone-extension-of-java/</u> 

7. Spring Framework in Java - why is it worth your attention, <u>https://svitla.com/blog/spring-framework-in-java-why-is-it-worth-your-attention/</u> 

8. Speakers -> Rod Johnson - QCon London, <u>https://qconlondon.com/london-2008/qconlondon.com/london-2008/speaker/Rod% 2BJohnson.html</u> 

9. Rod Johnson Chats about the Spring Framework Early Days ... - InfoQ, <u>https://www.infoq.com/podcasts/johnson-spring-framework/</u> 

10. In-depth Analysis of JDK and CGLIB Dynamic Proxies: Principles, <u>https://www.novada.com/blog-ordinary/in-depth-analysis-of-jdk-and-cglib-dynamicproxies/</u> 

11. Lesson 4: The Lifecycle of a Request - Baeldung Membership, <u>https://www.baeldung.com/members/courses/rest-with-spring-boot/lessons/lesson4-the-lifecycle-of-a-request</u> 

12. DispatcherServlet :: Spring Framework, 

   - <u>https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-servlet.html</u> 

13. Spring MVC Architecture DispatcherServlet Flow, 

<u>https://learncodewithdurgesh.com/tutorials/spring-boot-tutorials/spring-mvc-archite</u> 

   - <u>cture-dispatcherservlet-flow</u> 

14. DispatcherServlet and Handler Mappings - DeepWiki, <u>https://deepwiki.com/spring-projects/spring-framework/6.1-dispatcherservlet-and-h andler-mappings</u> 

15. The Heart of Spring Boot: Understanding the DispatcherServlet, <u>https://medium.com/@govindaekbote7/the-heart-of-spring-boot-understanding-the</u> -dispatcherservlet-07a35e847416 

16. Journey of a Request in Spring Boot: A Deep Dive into the Full, <u>https://dev.to/devcorner/journey-of-a-request-in-spring-boot-a-deep-dive-into-the-f ull-request-lifecycle-5d24</u> 

17. Spring - MVC Framework - GeeksforGeeks, 

<u>https://www.geeksforgeeks.org/springboot/spring-mvc-framework/</u> 

18. 2.2. Overview of Spring MVC Architecture - terasoluna.org, <u>https://terasolunaorg.github.io/guideline/5.2.0.RELEASE/en/Overview/SpringMVC Overview.html</u> 

19. Spring Boot Interview Questions and Answers - GoodSpace AI, <u>https://goodspace.ai/interview-questions/springboot</u> 

20. org.springframework.web.filter - spring-framework, <u>https://docs.spring.io/spring-framework/docs/5.0.2.RELEASE/kdoc-api/spring-fram ework/org.springframework.web.filter/</u> 

21. Spring MVC Request Life Cycle - Just For Change - WordPress.com, <u>https://justforchangesake.wordpress.com/2014/05/07/spring-mvc-request-life-cycl e/</u> 

22. Why @Transactional Sometimes Fails: A Deep Dive into Spring AOP, <u>https://dev.to/headf1rst/the-aop-secret-behind-transactional-you-cant-ignore-4l6d</u> 

23. Spring AOP Under the Hood: How proxies work - Egor Voronianskii, <u>https://vrnsky.ghost.io/spring-aop-under-the-hood-how-proxies-work/</u> 

24. Proxying Mechanisms :: Spring Framework, <u>https://docs.spring.io/spring-framework/reference/core/aop/proxying.html</u> 

25. Spring AOP Example Tutorial – Aspect, Advice, Pointcut, JoinPoint, <u>https://mangohost.net/blog/spring-aop-example-tutorial-aspect-advice-pointcut-join point-annotations/</u> 

26. Self reference in a Spring application. | by Anton Rozhanskii - Medium, <u>https://medium.com/@anton.roz/self-invocation-in-a-spring-application-4d05ecaa0 865</u> 

27. Spring AOP does not work with self-invocation such as @CachePut, <u>https://stackoverflow.com/questions/54265032/spring-aop-does-not-work-with-selfinvocation-such-as-cacheput</u> 

28. Understanding Spring @Transactional Annotation, <u>https://pravin.dev/posts/spring-transactional-annotation/</u> 

29. Spring AOP not working, when the method is called internally within, <u>https://stackoverflow.com/questions/30598118/spring-aop-not-working-when-the-m ethod-is-called-internally-within-a-bean</u> 

30. Understanding Spring Boot's @Transactional Annotation - Medium, <u>https://medium.com/@niketl16/understanding-spring-boots-transactional-annotatio</u> 

<u>n-why-how-and-what-s-inside-7bc9f32be395</u> 

31. Spring In Action PDF - Bookey, 

<u>https://cdn.bookey.app/files/pdf/book/en/spring-in-action.pdf</u> 

32. Spring Transaction Management: A Deep Dive into the Architecture, <u>https://medium.com/@meet2sudhakar/spring-transaction-management-a-deep-div e-into-the-architecture-762b14a81f47</u> 

33. Transaction Propagation Mechanics in Spring Boot - Medium, <u>https://medium.com/@AlexanderObregon/transaction-propagation-mechanics-in-s pring-boot-explained-e93ef2675faf</u> 

34. 7. The Security Filter Chain - Spring, 

   - <u>https://docs.spring.io/spring-security/site/docs/3.0.x/reference/security-filter-chain. html</u> 

35. DelegatingFilterProxy (Spring Framework 7.0.9 API), <u>https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframew ork/web/filter/DelegatingFilterProxy.html</u> 

36. Spring Security Architecture: Filters, Chains, and Authentication, <u>https://ashishsrivastav.com/blog/spring-security-architecture-filters-chains</u> 

37. Architecture :: Spring Security, 

<u>https://docs.spring.io/spring-security/reference/servlet/architecture.html</u> 

38. Spring Security Filter Chain and DelegatingFilterProxy: Deep Dive, <u>https://medium.com/@aymenfarhani28/spring-security-filter-chain-and-delegatingfi lterproxy-deep-dive-570cf5c6cf6b</u> 

39. Spring Security Complete Guide: Internal Architecture, JWT, and, <u>https://medium.com/@mariorodrguezgalicia/spring-security-complete-guide-intern al-architecture-jwt-and-exception-handling-part-i-3f4e38bbfdc0</u> 

40. Chapter 6. Supporting Infrastructure - Spring, 

   - <u>https://docs.spring.io/spring-security/site/docs/2.0.x/reference/html/supporting-infr astructure.html</u> 

41. FilterChainProxy (spring-security-docs 7.1.1 API), <u>https://docs.spring.io/spring-security/reference/api/java/org/springframework/secur ity/web/FilterChainProxy.html</u> 

42. Internal working of Spring Security | by Yasif khan - Medium, <u>https://medium.com/@yasiffkhan/internal-working-of-spring-security-fde70cb3aa7 e</u> 

43. Auto-configuration mechanism (AutoConfiguration.imports / spring, <u>https://dev.to/ankit_verma_e2fa7fb2aa95d/auto-configuration-mechanism-autocon figurationimports-springfactories-hhb</u> 

44. Beyond Senior Level: Understanding Spring Boot from the Inside, <u>https://medium.com/@persolenom/beyond-senior-level-understanding-spring-boot</u> -from-the-inside-and-building-custom-230a5358bc6d 

45. Spring Boot Under the Hood. Part 1: What Really Happens When, <u>https://dev.to/silver_dev/part-1-what-really-happens-when-you-call-springapplicatio nrun-5b1j</u> 

46. EnableAutoConfiguration (Spring Boot 4.0.9-SNAPSHOT API), <u>https://docs.spring.io/spring-boot//4.0-SNAPSHOT/api/java/org/springframework/b</u> 

<u>oot/autoconfigure/EnableAutoConfiguration.html</u> 

47. Auto-configure your common module in the “Spring-Boot-Way”, <u>https://medium.com/spring-boot/auto-configure-your-common-module-in-the-sprin g-boot-way-32acd3976a70</u> 

48. Why use spring.factories for Spring Boot auto-configuration instead, <u>https://stackoverflow.com/questions/32107610/why-use-spring-factories-for-spring</u> -boot-auto-configuration-instead-of-annotatio 

49. SPRING BOOT 3 MIGRATION GUIDE, 

<u>https://cpanel.colegioamericano.edu.ec/portfolio/afD82A5FE103/Spring_Boot_3_ Migration_Guide</u> 

50. Untangling Spring Dependencies in Legacy Environments, <u>https://www.openlogic.com/blog/managing-spring-dependencies-in-legacy-environ ments</u> 

51. Preparing for Spring Boot 3.0, <u>https://spring.io/blog/2022/05/24/preparing-for-spring-boot-3-0/</u> 

52. Keep honoring javax.validation.constraints.* annotations when, <u>https://stackoverflow.com/questions/74991593/keep-honoring-javax-validation-con straints-annotations-when-switching-to-jakar</u> 

53. Spring Boot 3.0 Migration Guide - GitHub, <u>https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Migration-Guid</u> 

<u>e</u> 

54. Best Practices To Deal With Javax to Jakarta Migration - DZone, <u>https://dzone.com/articles/best-practices-to-deal-with-javax-to-jakarta-migra</u> 

55. GraalVM Native Image: Why Reflection Still Breaks in 2026 and How, <u>https://www.javacodegeeks.com/2026/06/graalvm-native-image-why-reflection-still</u> 

   - -breaks-in-2026-and-how-to-fix-it.html 

56. GraalVM Native Image for Spring Boot: Complete Guide 2026, <u>https://pavanrangani.com/blog/graalvm-native-image-spring-boot-guide</u> 

57. Towards Native: Examples and Principles of Spring and Dubbo AOT, <u>https://www.alibabacloud.com/blog/600383</u> 

58. Towards Native: Spring & Dubbo AOT Technical Examples and, <u>https://dubbo.apache.org/en/blog/2023/06/28/towards-native-spring-dubbo-aot-tec hnical-examples-and-principles-explanation/</u> 

59. Part 1: What's New in Spring Boot 3.x — Native Images, Jakarta EE, <u>https://medium.com/@Ishan.tharusha.wijayabahu/part-1-whats-new-in-spring-boot</u> -3-x-native-images-jakarta-ee-and-cloud-native-evolution-799adfd67876 

60. Spring Boot 4 AOT Data Repositories: The Underrated Feature, <u>https://www.rabinarayanpatra.com/blogs/spring-boot-4-aot-data-repositories</u> 

61. Introducing GraalVM Native Images :: Spring Boot, <u>https://docs.spring.io/spring-boot/reference/packaging/native-image/introducing-gr aalvm-native-images.html</u> 

62. AOT Processing and the Native Build Pipeline — Spring Boot 4, <u>https://www.coddykit.com/courses/spring_boot/aot-processing-and-the-native-buil d-pipeline-9312614</u> 

63. Ahead-of-Time Processing :: Spring Boot, 

<u>https://docs.spring.io/spring-boot/maven-plugin/aot.html</u> 

64. [Feature] Provide GraalVM Native Image packaging for Seata Server, <u>https://github.com/apache/incubator-seata/issues/8161</u> 

65. spring-boot virtual threads vs webflux -  l-lin, <u>https://l-lin.github.io/programming-languages/java/spring/spring-boot-virtual-thread s-vs-webflux</u> 

66. SpringBoot virtual threads vs webflux: Performance comparison for, <u>https://medium.com/deno-the-complete-reference/springboot-virtual-threads-vs-we bflux-performance-comparison-for-jwt-verify-and-mysql-query-ff94cf251c2c</u> 

67. GitHub - chrisgleissner/loom-webflux-benchmarks: Benchmarks of, <u>https://github.com/chrisgleissner/loom-webflux-benchmarks</u> 

68. Virtual Threads vs WebFlux: who wins? - Blog by Vincenzo Racca, <u>https://www.vincenzoracca.com/en/blog/framework/spring/virtual-threads-vs-webfl ux/</u> 

69. WebFlux vs Virtual Threads vs Quarkus: k6 benchmark on a ... - Reddit, <u>https://www.reddit.com/r/java/comments/1s9ijyd/webflux_vs_virtual_threads_vs_q uarkus_k6/</u> 

70. Tracing :: Spring Boot, 

<u>https://docs.spring.io/spring-boot/reference/actuator/tracing.html</u> 

71. Distributed Tracing + Micrometer: How They Work Together - Medium, <u>https://medium.com/codetodeploy/distributed-tracing-micrometer-how-they-work-t ogether-f01f91f2093d</u> 

72. OpenTelemetry vs Micrometer: Here's How to Decide - Last9, <u>https://last9.io/blog/opentelemetry-vs-micrometer/</u>
