# From Java Servlets to Spring Boot 4: How Java Web Development Evolved, What Spring Does, and What You Need to Know (October 2026)

Each step from CGI to Spring Boot fixed the biggest pain point of the step before it. Servlets fixed CGI’s process-per-request cost. JSP fixed HTML being written inside Java. Struts gave Model 2 applications a standard structure. Spring offered a lightweight alternative to EJB’s container-bound weight. Spring Boot removed Spring’s configuration and deployment overhead. As of October 2026, the current production line is **Spring Boot 4.1 (released June 10, 2026) on Spring Framework 7.0** , which keeps a **Java 17 baseline**  while giving first-class support to Java 25. Spring Boot 4.2 and Spring Framework 7.1 are in milestone and scheduled for November 2026.

## TL;DR

- **The lineage is a chain of fixes.**  CGI (one OS process per request) → Servlets (1997: one long-lived JVM object with many threads) → JSP (1999: HTML-first templates compiled into servlets) → Model 2/Struts (2000–2001: a front controller and MVC) → J2EE/EJB (1998–2003: transactions and distribution, at great cost in complexity) → Spring (1.0 in March 2004: POJOs, dependency injection, AOP, testability) → Spring Boot (1.0 in April 2014: auto-configuration, starters, embedded servers, fat JARs).
- **Spring’s core is still the IoC container plus proxies.**  Almost everything else is built on dependency injection and AOP proxies: declarative transactions, Spring MVC’s DispatcherServlet, data access with exception translation, Spring Security’s filter chain, and Boot’s conditional auto-configuration. Learn those two mechanisms and the rest of the framework stops looking like magic.
- **For new work in late 2026, use Spring Boot 4.1.x on Java 21 or 25.**  Learn core Java, HTTP/REST, SQL/JPA, Maven or Gradle, constructor injection, transaction boundaries, test slices with Testcontainers, and Actuator/Micrometer. Plan to move to Boot 4.2 after November 2026, because Spring’s own support data lists December 31, 2026 as the end of 4.0.x open-source support.

---

## Part 1 — Historical Evolution

### 1.1 Before servlets: CGI and its limits

In the mid-1990s, dynamic web content came mostly from the Common Gateway Interface (CGI). The web server started a **new operating-system process for each request** , usually running a Perl or C program. It passed request data through environment variables and stdin, and read the response from stdout. This caused three structural problems:

- **Performance.**  Process creation, interpreter startup and teardown happened on every hit, so throughput collapsed under load.
- **No shared state.**  Each process died after its response, so connection pools, caches and session data could not live in memory between requests.
- **Weak integration.**  Each request was isolated and had no standard model for sessions, security or lifecycle.

Java servlets are the Java counterpart to CGI, PHP and ASP. [zubiaga](http://taggedwiki.zubiaga.org/new_content/adeb90ddebfe5f167888774355537015)[freejavaguide](https://www.freejavaguide.com/java_servlet.html) They were designed specifically to keep the request handler alive between requests.

### 1.2 Java Servlets (1996–1997)

**History.**  Sun publicly announced the servlet API at the first JavaOne in May 1996. The Java Web Server (“Jeeves”) shipped as a product on June 5, 1997. The Servlet 1.0 specification, created by Pavni Diwanji at Sun, was finalized in June 1997. [encyclopedia](https://encyclopedia.pub/entry/36567) Later milestones:

- **Servlet 2.2**  (1999, part of J2EE 1.2): made web applications independent deployable units packaged as **WAR files** . [encyclopedia](https://encyclopedia.pub/entry/36567)
- **Servlet 2.3**  (2001): added **Filters** , the mechanism Spring Security still uses. [wikiwand](https://www.wikiwand.com/en/Jakarta_Servlet)
- **Servlet 3.0**  (December 2009, Java EE 6): added annotations, pluggability and async processing. [handwiki](https://handwiki.org/wiki/Java_servlet)

**How it works.**  A servlet is a Java object managed by a **servlet container** , also called a web container (Tomcat, Jetty and Undertow are examples). The container maps URLs to servlets, enforces access rights and owns the lifecycle: [zubiaga](http://taggedwiki.zubiaga.org/new_content/adeb90ddebfe5f167888774355537015)

1. `init()` runs once, when the servlet is loaded.
2. `service()` runs for every request on a container thread. `HttpServlet` dispatches it to `doGet()`, `doPost()` and the other HTTP methods.
3. `destroy()` runs once, at shutdown.

Usually there is **one servlet instance shared by many threads** , so any instance field is shared mutable state.

**What it fixed compared with CGI:**

- A long-lived JVM removed per-request process startup.
- Objects such as connection pools and caches could stay in memory.
- `HttpSession` gave built-in session tracking.
- Code was portable across containers.

**What it introduced:**

- HTML was assembled in Java with `out.println`.
- Request parsing and type conversion were verbose and manual.
- Developers had to reason about thread safety in shared servlet instances.
- Every servlet and mapping had to be declared in the `web.xml` deployment descriptor.

A minimal servlet from that era:

java

```
public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        resp.setContentType("text/html");
        PrintWriter out = resp.getWriter();
        out.println("<html><body><h1>Hello, " + req.getParameter("name") + "</h1></body></html>");
    }
}
```

xml

```
<!-- WEB-INF/web.xml --> <web-app> <servlet> <servlet-name>hello</servlet-name> <servlet-class>com.example.HelloServlet</servlet-class> </servlet> <servlet-mapping> <servlet-name>hello</servlet-name> <url-pattern>/hello</url-pattern> </servlet-mapping> </web-app>
```

The snippet also shows a security problem: it writes the request parameter straight into HTML without escaping it.

### 1.3 JavaServer Pages, JSTL and EL (1999–2003)

**JSP 1.0 shipped in June 1999.**  [depaul](https://condor.depaul.edu/mwright1/j2ee/lectures/class-01-004.html) It reversed the servlet model by putting **Java inside HTML**  instead of HTML inside Java. A JSP container translates each `.jsp` page into a servlet and compiles it, so JSP is an easier route to writing servlets rather than a separate runtime. [arxiv](https://arxiv.org/pdf/0801.2618) Later versions added:

- **Tag libraries**  (JSP 1.1). [javasprint](https://www.javasprint.com/java_training_tutorial_blog/java_jee_jsp_servlet_story_jsf_jstl_el_history.php)
- **JSTL** , the standard tag library. JSTL 1.0 required JSP 1.2. [javasprint](https://www.javasprint.com/java_training_tutorial_blog/java_jee_jsp_servlet_story_jsf_jstl_el_history.php)
- **JSP 2.0**  (November 2003): introduced the **Expression Language (EL)** , so pages could use `${user.name}` without scriptlets. [depaul](https://condor.depaul.edu/mwright1/j2ee/lectures/class-01-004.html)[arxiv](https://arxiv.org/pdf/0801.2618)

**What it fixed:**  designers could work in something close to HTML, and markup no longer had to be built from string concatenations.

**What it introduced:**  “spaghetti” pages, in which `<% ... %>` scriptlets mixed SQL calls, business rules and markup. Such pages were hard to test or reuse, and the presentation layer swallowed the logic. Today, putting Java code in JSP is widely regarded as bad practice. [Wikipedia](https://en.wikipedia.org/wiki/Jakarta_Servlet)

### 1.4 Model 1 vs Model 2 (MVC)

- **Model 1**  was page-centric. The browser requested a JSP, and that JSP handled the request, called JavaBeans and rendered the response. Navigation logic was spread across pages, which made applications hard to maintain and inflexible. [academia](https://www.academia.edu/33482501/Struts_2_Design_and_Programming_A_Tutorial)
- **Model 2**  applied MVC to the web. A servlet acts as the **controller** : it receives the request, invokes the **model**  (business logic and data), and forwards to a JSP **view**  that only renders. The term “Model 2” first appeared in the JSP 0.92 specification. [academia](https://www.academia.edu/33482501/Struts_2_Design_and_Programming_A_Tutorial)

Model 2 applications were quicker to build and easier to test, maintain and extend. [academia](https://www.academia.edu/33482501/Struts_2_Design_and_Programming_A_Tutorial) Writing the controller plumbing by hand in every project was repetitive, though, and that repetition created a market for frameworks.

### 1.5 Web frameworks on servlets: Struts and JSF

**Apache Struts**  was founded in **May 2000**  by Craig McClanahan, who was also lead developer of Tomcat 4.0. [apache](https://struts.apache.org/announce-2002.html) **Struts 1.0 was released on June 15, 2001.**  [grokipedia](https://grokipedia.com/page/Apache_Struts_1) It standardized Model 2:

- a single controller servlet, `ActionServlet`, implementing the **Front Controller**  pattern, which dispatched to developer-written `Action` classes;
- `ActionForm` beans that populated and validated form data;
- JSP tag libraries;
- one central `struts-config.xml` file that wired together models, views, controllers and forwards. [Wikipedia](https://en.wikipedia.org/wiki/Apache_Struts_1)

**What it fixed:**  consistent request routing, form handling, validation and internationalization.

**What it introduced:**

- Struts was **XML-heavy** .
- Actions inherited from framework base classes and were tied to the Servlet API, which made them **hard to unit-test** .
- Form beans duplicated domain objects.

Struts 2 was a different codebase, a rebrand of WebWork 2, and reached its first full release in February 2007. [Wikipedia](https://en.wikipedia.org/wiki/Apache_Struts_1)[dineshonjava](https://www.dineshonjava.com/struts-2-baby-step-to-learn/) **JavaServer Faces (JSF)**  became the component-based standard inside Java EE. It brought its own lifecycle complexity and its own XML.

### 1.6 Enterprise JavaBeans and J2EE (1998–2006)

**Timeline:**

- **EJB 1.0:**  March 1998. [infoworld](https://www.infoworld.com/article/2164596/the-state-of-java-middleware-part-2-enterprise-javabeans.html)[dokumen](https://dokumen.pub/pro-cdi-2-in-java-ee-8-an-in-depth-guide-to-context-and-dependency-injection-1nbsped-978-1-4842-4363-3.html)
- **EJB 2.0**  (JSR 19): final release on September 24, 2001. It added JMS integration, local interfaces, container-managed persistence for entity beans and EJB-QL. [jcp](https://jcp.org/en/jsr/detail?id=19)[jcp](https://www.jcp.org/en/jsr/summary?id=Enterprise+Java+Beans)
- **J2EE 1.2:**  December 1999. It bundled Servlets, JSP and EJB into one platform. [javasprint](https://www.javasprint.com/java_training_tutorial_blog/java_jee_jsp_servlet_story_jsf_jstl_el_history.php)

**What EJB promised:**  declarative **transactions** , **security** , **remoting/distribution** , pooling, and **persistence through entity beans** , all supplied by an application server.

**Why it became notoriously heavy.**  Oracle’s J2EE 1.4 tutorial describes the work for a remote bean: “you must code a remote interface and a home interface”, where the home interface defines life-cycle methods such as `create` and `remove`. [oracle](https://docs.oracle.com/javaee/1.4/tutorial/doc/EJBConcepts6.html) Entity beans also needed finder methods, a deployment descriptor and an EJB JAR assembled from the bean, its interfaces and its XML. [oracle](https://docs.oracle.com/javaee/1.4/tutorial/doc/EJBConcepts6.html)[oracle](https://docs.oracle.com/cd/B14099_19/web.1012/b15505/entity.htm) In practice this meant:

- several Java artifacts plus XML descriptors for a single business component;
- beans that implemented framework interfaces and depended on the container;
- code that was **almost impossible to unit-test outside a running application server** ;
- slow build, deploy and test cycles;
- entity beans that performed poorly and modeled domains badly.

The standard eventually acknowledged the problem. **EJB 3.0**  (JSR 220, final release on May 11, 2006, shipped as Java EE 5) stated that its purpose was “to improve the EJB architecture by reducing its complexity from the developer’s point of view.” [jcp](https://jcp.org/en/jsr/detail?id=220) It replaced most of the plumbing with annotations and POJOs, largely copying ideas that Spring and Hibernate had already proven.

**Hibernate as a reaction.**  The official Hibernate guide says: “The Hibernate project began in 2001, when Gavin King’s frustration with Entity Beans in EJB 2 boiled over.” King later joined the EJB 3 expert group and “convinced the group to deprecate Entity Beans in favor of a brand-new persistence API modelled after Hibernate.” [hibernate](https://docs.hibernate.org/orm/7.1/introduction/html_single/) That API became JPA. [javapro](https://javapro.io/2025/05/21/a-look-back-at-javas-30-year-journey-with-databases/)

### 1.7 Rod Johnson and the birth of Spring (2002–2004)

In late 2002, Rod Johnson published ***Expert One-on-One J2EE Design and Development*** . Sources differ on the month: the Spring blog says November 2002 and other references say October. [en-academic](https://en-academic.com/dic.nsf/enwiki/2665032)[spring](https://spring.io/blog/2006/11/09/spring-framework-the-origins-of-a-project-and-a-name/) Two features of the book matter for this history:

- **It challenged J2EE orthodoxy.**  It argued that most applications did not need distributed EJBs and demonstrated a high-quality seat-reservation application built **without EJB** . [medium](https://medium.com/@arowrayne/the-spring-revolutions-1-origins-4d4e2c57f8c9)[theblog](https://theblog.net/spring-framework/spring-framework-and-boot)
- **It shipped working code.**  In Johnson’s own words on the Spring blog (2006), the book “was accompanied by 30,000 lines of framework code”, in `com.interface21` packages.

Juergen Hoeller and Yann Caroff persuaded Johnson to turn that code into an open-source project, which **began in February 2003** . [theblog](https://theblog.net/spring-framework/spring-framework-and-boot) Caroff suggested the name “Spring” because it represented “a fresh start after the ‘winter’ of traditional J2EE.” [spring](https://spring.io/blog/2006/11/09/spring-framework-the-origins-of-a-project-and-a-name/) Spring 0.9 shipped in June 2003 under the Apache 2.0 license. [quickprogrammingtips](https://www.quickprogrammingtips.com/spring-boot/history-of-spring-framework-and-spring-boot.html) **Spring Framework 1.0 final was released on March 24, 2004.**  The 1.0 announcement listed: [spring](https://spring.io/blog/2004/03/24/spring-framework-1-0-final-released/)

- “the most sophisticated lightweight container available”;
- an AOP interception framework based on AOP Alliance;
- JDBC, Hibernate, JDO and iBATIS integration tied into Spring’s transaction management;
- JNDI support, remoting, scheduling and a web MVC framework.

The 2004 sequel, ***J2EE without EJB***  (Johnson and Hoeller), set out the lightweight-container architecture in full. [qconlondon](https://qconlondon.com/london-2008/qconlondon.com/london-2008/speaker/Rod%2BJohnson.html)

**The philosophy:**

- **POJOs:**  business objects do not extend framework classes.
- **Inversion of Control / Dependency Injection:**  the container builds and wires objects; objects do not look up their dependencies.
- **AOP for cross-cutting services:**  transactions, security and similar services are applied declaratively, without a heavyweight container.
- **Testability:**  objects can be created with `new` in a plain JUnit test.

**Naming the pattern.**  According to Johnson, the term “Dependency Injection” was coined by Martin Fowler, Johnson and the PicoContainer team in late 2003. [theserverside](https://www.theserverside.com/news/1364527/Introduction-to-the-Spring-Framework) Fowler’s essay “Inversion of Control Containers and the Dependency Injection pattern” (January 2004) made it widely known. The essay names constructor, setter and interface injection, contrasts DI with Service Locator, and concludes that “the choice between them is less important than the principle of separating configuration from use.” [hackernoon](https://hackernoon.com/you-dont-need-to-know-dependency-injection-2e9d2ba1978a)[researchr](https://researchr.org/publication/fowler2004inversion)

A minimal Spring 1.x/2.x XML configuration:

xml

```
<beans xmlns="http://www.springframework.org/schema/beans" ...> <bean id="orderRepository" class="com.example.JdbcOrderRepository"> <property name="dataSource" ref="dataSource"/> </bean> <bean id="orderService" class="com.example.OrderService"> <constructor-arg ref="orderRepository"/> </bean> </beans>
```

### 1.8 Spring’s own evolution (2006–2013)

| Version | Date | What changed |
| --- | --- | --- |
| Spring 2.0 | Oct 2006 | XML namespaces; AspectJ pointcut support |
| Spring 2.5 | Nov 2007 | Annotation-driven configuration (`@Autowired`, JSR-250 `@PostConstruct`/`@PreDestroy`), component scanning with `@Component`/`@Service`/`@Repository`/`@Controller`, annotated MVC controllers, and the **Spring TestContext Framework** |
| Spring 3.0 | Dec 2009 | Java 5+ baseline; Java-based `@Configuration`/`@Bean`; SpEL; REST support in Spring MVC |
| Spring 4.0 | Dec 2013 | Java 8 support; `@RestController`; WebSocket |

**What remained painful by about 2012:**

- **Config sprawl.**  Every project still had to declare DataSources, transaction managers, `DispatcherServlet` mappings, view resolvers, message converters and security filters, in XML, Java or both.
- **Dependency management (“JAR hell”).**  Developers had to choose versions of Spring, Hibernate, Jackson, logging bridges and servlet APIs that worked together.
- **Deployment friction.**  Applications were built as WARs, deployed into a separately installed and configured Tomcat or application server, and promoted between environments that differed.
- **Slow start.**  Hours of setup came before the first line of business logic.

### 1.9 Spring Boot (2014 → today)

**Origins.**  Spring Boot grew out of an October 2012 request (SPR-9888) to “improve containerless web application architectures.” [medium](https://medium.com/javarevisited/evolution-of-spring-boot-and-microservices-4d1109b5a4d3)[adtmag](https://adtmag.com/articles/2014/04/09/spring-boot-launch.aspx) **Spring Boot 1.0 went GA on April 1, 2014.**  Phil Webb’s announcement reported 1,720 commits by 54 contributors over the 18 months since the request and framed Boot as “an ultralight container, great for application or service deployment in the cloud.” [spring](https://spring.io/blog/2014/04/01/spring-boot-1-0-ga-released/)

**What Boot added and which problem each piece solved:**

| Boot feature | Problem it removed |
| --- | --- |
| **Auto-configuration**  (`@EnableAutoConfiguration`, `@Conditional*`) | Hand-wiring DataSources, MVC, Jackson, security and similar infrastructure |
| **Starters**  (`spring-boot-starter-web`, `-data-jpa`, …) plus a curated dependency BOM | JAR hell and version matching |
| **Embedded servers**  (Tomcat, Jetty, Undertow; Netty for WebFlux) | Installing and configuring an external server |
| **Executable fat JAR**  (`java -jar app.jar`) | WAR deployment and environment drift |
| **Externalized configuration**  (`application.properties`/`.yml`, profiles, environment variables) | Rebuilding the application for each environment |
| **Actuator**  (health, metrics, info, …) | Hand-built production monitoring |
| **“Opinionated defaults that get out of the way”** | Slow project start |

**How Boot enabled microservices.**  Each service became a small, self-contained, independently deployable JAR with built-in health checks and metrics. That shape fits PaaS platforms, containers and Kubernetes, and Spring Cloud added service discovery, config servers and gateways on top.

**Major milestones:**

- **Spring Boot 2.0 (March 1, 2018).**  First major revision, the result of “17 months work and over 6800 commits by 215 different individuals.” Built on Spring Framework 5.0, with: [spring](https://spring.io/blog/2018/03/01/spring-boot-2-0-goes-ga/)
    - a **Java 8 baseline** ;
    - **Spring WebFlux**  reactive support and embedded Netty;
    - a new Actuator architecture with **Micrometer**  metrics; [coderanch](https://coderanch.com/t/691399/frameworks/Spring-Boot-GA)
    - Kotlin support and HTTP/2;
    - HikariCP as the default connection pool. [versionlog](https://versionlog.com/spring-boot/2.0/)
- **Spring Boot 3.0 (November 24, 2022).**  [spring](https://spring.io/blog/2022/11/24/spring-boot-3-0-goes-ga/) Built on Spring Framework 6.0 (released November 16, 2022), with: [Wikipedia](https://en.wikipedia.org/wiki/Spring_Framework)
    - a **Java 17 baseline** ;
    - **Jakarta EE 9 baseline with EE 10 support** , which moved code from `javax.*` to `jakarta.*` (for example, `javax.servlet` became `jakarta.servlet`); [spring](https://spring.io/blog/2022/11/24/spring-boot-3-0-goes-ga/)[spring](https://spring.io/blog/2022/05/24/preparing-for-spring-boot-3-0/)
    - **GraalVM native image**  support through AOT processing, replacing the experimental Spring Native project; [spring](https://spring.io/blog/2022/11/24/spring-boot-3-0-goes-ga/)
    - observability through **Micrometer and Micrometer Tracing** ;
    - ProblemDetail (RFC 7807) error responses. [versionlog](https://versionlog.com/spring-boot/3.0/)
  Because Java EE and Jakarta EE APIs cannot be mixed in one project, this was the hardest upgrade in Boot’s history. [spring](https://spring.io/blog/2022/05/24/preparing-for-spring-boot-3-0/)
- **Spring Boot 3.2 (November 2023).**  With Java 21, setting `spring.threads.virtual.enabled=true` runs Tomcat and Jetty request handling, the `applicationTaskExecutor`, `@Async` methods and messaging listeners on **virtual threads** . [danvega](https://www.danvega.dev/blog/spring-boot-3-features) The release also added the new `RestClient` and `JdbcClient` and initial **CRaC**  (checkpoint/restore) support. Broadcom completed its acquisition of VMware, then Spring’s owner, the day before this release.
- **Spring Boot 3.5 (May 2025).**  The final 3.x line. Its last open-source patch, 3.5.16, shipped on June 25, 2026, after which support is commercial only. [herodevs](https://www.herodevs.com/blog-posts/spring-boot-versions-eol-dates-and-latest-releases-april-2026)
- **Spring Framework 7.0 (GA November 13, 2025) and Spring Boot 4.0 (GA November 20, 2025).**  [spring](https://spring.io/blog/2025/11/13/spring-framework-7-0-general-availability/)[spring](https://spring.io/blog/2025/11/20/spring-boot-4-0-0-available-now/)
    - **Baselines:**  keeps **Java 17 as the minimum**  while “embracing Java 25 (as the latest LTS)”; Jakarta EE 11 (Servlet 6.1, JPA 3.2, Bean Validation 3.1); Jackson 3.0; Kotlin 2.2; JUnit 6.0. [spring](https://spring.io/blog/2025/11/13/spring-framework-7-0-general-availability/)
    - **Framework features:**  null safety across the portfolio with **JSpecify** ; **API versioning** ; **HTTP Service Clients**  (`@HttpServiceClient`); programmatic bean registration; built-in resilience (`@Retryable`, `RetryTemplate`, `@ConcurrencyLimit`); `JmsClient`; `RestTestClient`. [infoq +2](https://www.infoq.com/articles/spring-team-spring-7-boot-4/)
    - **Boot changes:**  Boot 4.0 **fully modularized**  its own codebase into smaller, focused JARs, and enabled liveness and readiness probes by default. [spring](https://spring.io/blog/2025/11/20/spring-boot-4-0-0-available-now/)[spring](https://spring.io/blog/2025/09/18/spring-boot-4-0-0-M3-available-now/)
- **Spring Boot 4.1 (June 10, 2026) — current.**  Built on Spring Framework 7.0.x. It adds: [infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/)
    - **Spring gRPC auto-configuration** , with `@GrpcAdvice`; [infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/)
    - **SSRF mitigation**  through an `InetAddressFilter` for outbound HTTP clients; [infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/)
    - lazy JDBC connection fetching;
    - automatic Micrometer context propagation into `@Async` methods;
    - better OpenTelemetry support;
    - a Kotlin 2.3 baseline.
  It also removes APIs deprecated in 4.0 and deprecates DevTools LiveReload. The release slipped from its usual May slot, the first delay since the twice-yearly May/November cadence began in 2020. [infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/) Latest patches as of October 2026: **4.1.1 and 4.0.8, both released August 20, 2026.**  [versionlog](https://versionlog.com/spring-boot/)
- **What comes next (not yet released).**  **Spring Boot 4.2.0-M2**  shipped on September 25, 2026, with OpenTelemetry semantic conventions and SSL bundles for LDAP. [versionlog](https://versionlog.com/spring-boot/)[infoq](https://www.infoq.com/news/2026/09/spring-news-roundup-sep21-2026/) **Spring Framework 7.1**  is at milestone 2, scheduled for November 2026, and adds HTTP `QUERY` method support, a new multipart message converter and a Jackson 3.1 baseline. [infoq](https://www.infoq.com/news/2026/09/spring-news-roundup-sep21-2026/) Both are expected in November 2026; treat any feature list as provisional until GA.

**About the Java baseline.**  The Spring team and InfoQ both state that Boot 4.x keeps the **Java 17 minimum** . [spring](https://spring.io/blog/2025/11/13/spring-framework-7-0-general-availability/)[infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/) Some version-tracking sites claim Boot 4.1 requires Java 21. [versionlog](https://versionlog.com/spring-boot/4.1/) That claim conflicts with the primary sources and is wrong. Only specific integrations, such as jOOQ 3.20, need Java 21. [infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/) In practice, use **Java 21 or 25**  to get virtual threads and the newest JVM features.

### 1.10 Where Jakarta EE fits

Java EE, previously J2EE, was the **specification track** : Servlet, JSP, JPA, Bean Validation, CDI, EJB and others, implemented by application servers such as GlassFish, WildFly and WebLogic. Its move to Jakarta EE happened in four steps:

1. **2017.**  Oracle announced in August that it would move Java EE to an open foundation, and chose the **Eclipse Foundation**  in September. [eclipse](https://www.eclipse.org/ee4j/faq.php)[infoq](https://www.infoq.com/news/8331)
2. **February 26, 2018.**  The platform was renamed **Jakarta EE** , because Oracle kept the Java trademarks. [phoronix](https://www.phoronix.com/news/Java-EE-To-Jakarta-EE)[eclipse](https://blogs.eclipse.org/blog-tags/java-ee)
3. **December 8, 2020.**  **Jakarta EE 9**  changed the package namespace from `javax.*` to `jakarta.*` across all 41 specifications. [eclipse](https://blogs.eclipse.org/post/mike-milinkovich/jakarta-ee-9-delivers-big-bang)
4. **June 26, 2025.**  **Jakarta EE 11**  went GA, requiring Java 17+ and adding Jakarta Data. [siliconangle](https://siliconangle.com/2025/06/26/eclipse-foundation-announces-jakarta-ee-11-advance-cloud-native-java-productivity/)[globenewswire](https://www.globenewswire.com/news-release/2025/06/26/3105653/0/en/The-Eclipse-Foundation-s-Jakarta-EE-Working-Group-Announces-Jakarta-EE-11-Release.html)

**Spring is not a Jakarta EE implementation.**  It is an independent framework that **consumes selected Jakarta specifications** :

- Spring MVC runs on the **Servlet API** .
- Spring Data JPA builds on **JPA**  (usually Hibernate).
- Validation uses **Bean Validation**  (Hibernate Validator).

Spring replaces other parts of the platform with its own models: DI instead of CDI and EJB, `@Transactional` instead of EJB container transactions, and Spring Security instead of Jakarta Security. This is why Spring generations follow Jakarta levels: Boot 3 moved to EE 9/10 and Boot 4 moved to EE 11. [spring](https://spring.io/blog/2025/11/13/spring-framework-7-0-general-availability/)[spring](https://spring.io/blog/2022/11/24/spring-boot-3-0-goes-ga/)

---

## Part 2 — Generations at a Glance

| Generation (approx. date) | Problem it addressed | New problem it introduced |
| --- | --- | --- |
| **CGI**  (early–mid 1990s) | Dynamic content on static web servers | A process per request; no shared state; poor scalability |
| **Servlets**  (1997) | Process cost (long-lived, multithreaded JVM objects); sessions; portability | HTML in `println`; verbose request handling; thread-safety pitfalls; `web.xml` |
| **JSP / JSTL / EL**  (1999–2003) | HTML inside Java | Scriptlet “spaghetti”; logic in views; hard to test |
| **Model 2 / Struts / JSF**  (2000–2007) | No standard structure, routing, form binding or validation | XML-heavy config; inheritance-bound, servlet-coupled actions; hard to unit-test |
| **J2EE / EJB 1.x–2.x**  (1998–2006) | Transactions, security, distribution and persistence for enterprise systems | Home/remote interfaces, deployment descriptors, container lock-in, slow cycles, untestable code, poor entity beans |
| **Spring Framework**  (2003–2004 →) | EJB complexity: POJOs, DI, AOP, declarative transactions, testability | XML (later Java) config sprawl; dependency version conflicts; WAR deployment; slow project setup |
| **Spring Boot**  (2014 →) | Setup, dependency alignment, deployment, production readiness | “Magic” auto-configuration that is hard to debug if you don’t understand it; large framework surface; fast upgrade cadence (javax→jakarta, Jackson 3, modular starters) |

---

## Part 3 — Core Functionalities of the Spring Framework

### 3.1 The core container (IoC/DI)

- **IoC container.**  You describe *what*  objects (beans) exist and how they relate, through annotations, `@Bean` methods or XML. The container instantiates them, resolves their dependencies, applies post-processors and proxies, and manages their lifecycle.
- **`BeanFactory` vs `ApplicationContext`.**  `BeanFactory` is the basic DI engine. `ApplicationContext` extends it with event publishing, internationalization, resource loading, environment and profile abstraction, and automatic registration of `BeanPostProcessor`s. Applications nearly always use `ApplicationContext`, which Boot creates for you.
- **Bean lifecycle** , in order:
    1. instantiate;
    2. inject dependencies;
    3. run `*Aware` callbacks;
    4. run `BeanPostProcessor` before-initialization hooks;
    5. run `@PostConstruct` or `afterPropertiesSet`;
    6. run after-initialization hooks, **where AOP proxies are created** ;
    7. the bean is in use;
    8. run `@PreDestroy` or `destroy`.
- **Scopes:**
    - `singleton`: the default; one instance per container.
    - `prototype`: a new instance on each lookup; the container does not manage destruction.
    - Web scopes: `request`, `session`, `application` and `websocket`.
  Injecting a shorter-lived bean into a singleton requires a scoped proxy or an `ObjectProvider`.
- **Injection styles: constructor, setter and field.**  The Spring reference documentation says: “The Spring team generally advocates constructor injection, as it lets you implement application components as immutable objects and ensures that required dependencies are not null.” Use constructors for mandatory dependencies and setters for optional ones. Constructor injection also brings circular dependencies to light immediately rather than hiding them. Since Spring 4.3, a class with a single constructor needs no `@Autowired`.

### 3.2 Aspect-Oriented Programming (Spring AOP)

- **Purpose.**  AOP modularizes **cross-cutting concerns**  that would otherwise be scattered through business code: transactions, security checks, caching, logging, metrics, retries. The key terms are *aspect* , *join point*  (in Spring, always a method execution), *pointcut*  and *advice*  (`@Before`, `@AfterReturning`, `@Around`, and so on).
- **Proxies.**  Spring AOP is **proxy-based** : callers receive a wrapper around the target bean. It uses **JDK dynamic proxies**  (interface-based) or **CGLIB**  (subclass-based). Spring Boot defaults to class-based (CGLIB) proxies. `@Transactional`, `@Cacheable`, `@Async`, `@PreAuthorize` and the new `@Retryable` all work this way.
- **The self-invocation pitfall.**  In the reference documentation’s words, “self invocation via an explicit or implicit `this` reference will bypass the advice.” When one method on a bean calls another `@Transactional` method on the same bean, the call never passes through the proxy, so **no transaction starts** . The fixes, in order of preference:
    1. refactor the method into a separate bean;
    2. inject a self-reference;
    3. use AspectJ weaving.
  Also, proxies do not advise `private` methods, and with JDK proxies they do not advise `protected` methods either.

### 3.3 Spring MVC

- **`DispatcherServlet`**  is a single Front Controller servlet registered with the container, the same Model 2 pattern Struts used. For each request it:
    1. consults **HandlerMappings**  to find a handler method;
    2. calls it through a **HandlerAdapter** , resolving arguments such as `@PathVariable`, `@RequestParam`, `@RequestBody` and `@Valid`;
    3. turns the return value into either a view name, resolved by a **ViewResolver**  (Thymeleaf, JSP and others), or a response body written by **HttpMessageConverters** . Jackson 3 is the default JSON converter in Spring 7.
- **Annotations.**  `@Controller` returns views. `@RestController` is `@Controller` plus `@ResponseBody`. Routing uses `@RequestMapping` and its shortcuts: `@GetMapping`, `@PostMapping`, `@PutMapping`, `@PatchMapping` and `@DeleteMapping`.
- **Errors and validation.**
    - `@ExceptionHandler` methods, usually in a `@ControllerAdvice`/`@RestControllerAdvice` class, map exceptions to responses. `ProblemDetail` provides standard RFC error bodies.
    - **Bean Validation**  (`jakarta.validation`: `@NotNull`, `@Size`, …) is triggered by `@Valid` or `@Validated`.
- **Newer additions:**
    - **API versioning**  in Spring 7: path, header, query-parameter or media-type strategies. [infoq](https://www.infoq.com/articles/spring-team-spring-7-boot-4/)
    - **HTTP interface clients**  for declarative outbound calls.
    - `RestClient`, which is replacing `RestTemplate` for synchronous calls.

### 3.4 Data access and transactions

- **`JdbcTemplate`, and the fluent `JdbcClient` (6.1+),**  remove JDBC boilerplate: connection handling, statement cleanup and result-set iteration.
- **Exception translation.**  Vendor-specific `SQLException`s become Spring’s unchecked `DataAccessException` hierarchy, such as `DuplicateKeyException`. `@Repository` beans get this translation automatically.
- **Declarative transactions.**  `@Transactional` is implemented through AOP.
    - **Propagation**  defaults to `REQUIRED`. `REQUIRES_NEW`, `NESTED` and others are available.
    - **Isolation**  controls visibility between concurrent transactions.
    - `readOnly` provides optimization hints.
    - **Rollback rules:**  by default, only unchecked exceptions trigger rollback.
- **ORM integration.**  Spring integrates with **JPA/Hibernate**  (Hibernate 7 and JPA 3.2 in the Spring 7 generation), including transaction-bound `EntityManager`s.
- **Spring Data JPA.**  You declare an interface extending `JpaRepository<Order, Long>`, and Spring generates the implementation, including derived queries such as `findByCustomerEmail`, plus `@Query`, paging, projections and auditing. Spring Data AOT repositories improve startup time. [danvega](https://www.danvega.dev/blog/spring-boot-4-is-here)

### 3.5 Spring Security

- **How it plugs in.**  Spring Security is implemented as a **Servlet filter chain**  (`DelegatingFilterProxy` → `FilterChainProxy` → `SecurityFilterChain`) in front of the `DispatcherServlet`.
- **Authentication:**  form login, HTTP Basic, LDAP, OAuth2/OIDC login, SAML, and **resource servers that validate JWTs** . Spring Authorization Server lets you run your own OAuth2 authorization server.
- **Authorization:**  URL rules through `authorizeHttpRequests`, plus **method-level security**  with `@EnableMethodSecurity` and `@PreAuthorize("hasRole('ADMIN')")`. Method security is another AOP proxy, so the self-invocation pitfall applies.
- **Configuration and defaults.**  Modern configuration declares `SecurityFilterChain` beans using the lambda DSL, replacing the removed `WebSecurityConfigurerAdapter`. Defaults include CSRF protection, secure headers and password hashing through `DelegatingPasswordEncoder`.

### 3.6 Spring Boot specifics

- **`@SpringBootApplication`**  combines `@SpringBootConfiguration`, `@EnableAutoConfiguration` and `@ComponentScan`.
- **Auto-configuration.**  Auto-configurations are ordinary `@Configuration` classes listed in `META-INF/spring/...AutoConfiguration.imports`. They are guarded by conditions:
    - `@ConditionalOnClass`: is the library on the classpath?
    - `@ConditionalOnMissingBean`: did you define your own bean? If so, Boot backs off.
    - `@ConditionalOnProperty`, `@ConditionalOnWebApplication` and others.
  Boot 4 split these into per-technology modules.
- **Starters**  are dependency descriptors, such as `spring-boot-starter-web`, `-webflux`, `-data-jpa`, `-security`, `-actuator` and `-test`. Boot 4 added dedicated test starters per technology. [spring](https://spring.io/blog/2025/10/23/spring-boot-4-0-0-RC1-available-now/)
- **Embedded servers.**  Tomcat is the default. Jetty can be selected, and Netty is used for WebFlux. WAR deployment remains possible.
- **Actuator**  exposes `/actuator/health` (with liveness and readiness groups), `metrics`, `info`, `prometheus`, `loggers`, `env` and other endpoints. Secure them, because CVEs in 2026 targeted Actuator path handling. [spring](https://spring.io/blog/2026/03/19/spring-boot-4-0-4-available-now/)
- **Externalized configuration.**  Properties are read in a defined precedence order: command line, environment variables, profile-specific files, then `application.yml`. Profiles are selected with `spring.profiles.active`, and `@ConfigurationProperties` gives type-safe binding.
- **DevTools**  provides automatic restart during development. LiveReload is deprecated as of 4.1. [infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/)
- **Testing:**
    - `@SpringBootTest` runs a full context.
    - Slices load only part of the context: `@WebMvcTest` (MVC with `MockMvc`), `@DataJpaTest` (JPA with an embedded or test database) and `@JsonTest`.
    - `@MockitoBean` replaced the deprecated `@MockBean`.
    - `@ServiceConnection` gives first-class **Testcontainers**  support, along with Docker Compose support.

A minimal Spring Boot application, which replaces the servlet class, `web.xml`, external Tomcat and XML wiring shown earlier:

java

```
@SpringBootApplication public class DemoApplication { public static void main(String[] args) { SpringApplication.run(DemoApplication.class, args); } } @RestController class HelloController { @GetMapping("/hello") String hello(@RequestParam(defaultValue = "world") String name) { return "Hello, " + name; } }
```

Run it with `./mvnw spring-boot:run`, or build it and run `java -jar target/demo.jar`. Tomcat, Jackson, logging and a health endpoint (if Actuator is added) are configured automatically.

### 3.7 The wider ecosystem

- **Spring WebFlux:**  a reactive, non-blocking web stack on Project Reactor and Netty. Use it for streaming and high-concurrency I/O. Virtual threads now cover many cases that once needed reactive code.
- **Spring Cloud:**  config server, service discovery, Gateway, circuit breakers and load-balanced clients for microservices. Release train 2025.1 accompanies Boot 4. [infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/)
- **Spring Batch:**  chunk-oriented batch jobs with restartability (6.x in the Boot 4 generation).
- **Spring Integration:**  Enterprise Integration Patterns and messaging adapters. 7.1 added a CloudEvents module. [spring](https://spring.io/projects/release-highlights/)
- **Spring Modulith:**  structuring and verifying modular monoliths, with application-module tests (2.1 accompanied Boot 4.1). [spring](https://spring.io/projects/release-highlights/)[infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/)
- **Spring AI:**  model, vector-store and tool-calling abstractions for LLM applications. Spring AI 2.0 shipped alongside Boot 4.1 with a Boot 4/Jackson 3 baseline. [spring](https://spring.io/projects/release-highlights/)[infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/)
- **Spring gRPC:**  auto-configured from Boot 4.1. [infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/)
- **Spring testing:**  the TestContext framework (since 2.5), `MockMvc`, `WebTestClient` and `RestTestClient`.

### 3.8 Newest runtime-efficiency developments

- **Virtual threads (Java 21+).**  One property, `spring.threads.virtual.enabled=true`, since Boot 3.2. Watch out for pinning and for connection pools sized for the old thread model.
- **GraalVM native images**  through Spring AOT, since Boot 3.0. [spring](https://spring.io/blog/2022/11/24/spring-boot-3-0-goes-ga/) They start quickly and use little memory, but reflection and runtime proxies are restricted and builds are slower.
- **CRaC and Project Leyden/CDS.**  Checkpoint/restore and class-data sharing or AOT cache training runs reduce startup time on the JVM. Spring has aligned with Leyden since 6.x. [spring](https://spring.io/blog/2024/10/01/from-spring-framework-6-2-to-7-0/)
- **Spring Framework 7 features:**  JSpecify null safety, API versioning, HTTP service clients, resilience annotations and programmatic bean registration. These are **released, GA features** . The Framework 7.1 and Boot 4.2 items listed earlier are still in milestone.

---

## Part 4 — Essential Knowledge for Spring Developers

### 4.1 Java prerequisites

- **Core Java:**  OOP and interfaces, generics, collections, exceptions (checked vs unchecked matters for rollback rules), lambdas and streams, `Optional`, records, and `java.time`.
- **Annotations and reflection.**  Spring is driven by annotations, and proxies are built through reflection and bytecode generation. Understanding them explains most of Spring’s apparent magic.
- **Concurrency basics.**  Singleton beans are shared across threads, so keep them stateless. Learn virtual threads.
- **Baselines:**
    - Boot 3.x and 4.x require **Java 17+** . [herodevs](https://www.herodevs.com/blog-posts/spring-boot-versions-eol-dates-and-latest-releases-april-2026)[goregulus](https://goregulus.com/cra-basics/spring-boot-versions/)
    - **Java 21 or 25 is recommended**  for virtual threads and current JVM optimizations.
    - Boot 2.7 was the last line to support Java 8/11, and it is long out of open-source support. [danvega](https://www.danvega.dev/blog/spring-boot-3-features)

### 4.2 Build tools and project setup

- **Maven or Gradle**  (Boot 4 supports Gradle 9). [spring](https://spring.io/blog/2025/08/21/spring-boot-4-0-0-M2-available-now/) Understand transitive dependencies and how to inspect them with `mvn dependency:tree` or `gradle dependencies`.
- **The Boot parent POM / `spring-boot-dependencies` BOM**  pins compatible versions. Declare starters **without versions** , and override managed versions only deliberately.
- **Spring Initializr**  (start.spring.io, also built into IntelliJ and VS Code) generates a correct skeleton.

### 4.3 Web and data fundamentals

- **HTTP:**  methods and idempotency, status codes, headers, content negotiation, caching and CORS. **REST**  resource design and versioning. **JSON**  serialization with Jackson; note that Jackson 3 changes packages and defaults in Boot 4.
- **The Servlet API underneath.**  Filters, the request/response lifecycle, the thread-per-request model and sessions all still apply beneath Spring MVC and Spring Security.
- **SQL and JPA:**  joins, indexes and transactions; entity lifecycle and persistence context; lazy vs eager loading; schema migrations with Flyway or Liquibase.

### 4.4 Design principles and anti-patterns

- **SOLID and layering:**
    - controller: HTTP mapping and validation only;
    - service: business logic and transaction boundaries;
    - repository: persistence.
- **DTOs vs entities.**  Do not expose JPA entities through your API, because of lazy-loading exceptions, accidental over-posting and tight coupling.
- **Why DI improves testability:**  dependencies arrive through constructors, so a unit test can pass mocks without starting Spring.
- **Common anti-patterns:**
    - **Field injection**  with `@Autowired` everywhere: hidden dependencies, no `final`, harder tests.
    - **God services**  with a dozen dependencies.
    - **Misplaced transaction boundaries:**  `@Transactional` on controllers or on private methods, self-invocation, long transactions that hold connections during remote calls.
    - **N+1 queries.**  Fix them with fetch joins, `@EntityGraph` or batch fetching.
    - **Circular dependencies.**  Boot forbids them by default since 2.6; redesign instead of re-enabling them.
    - **Open-Session-in-View**  left on by default, which hides lazy-loading costs.

### 4.5 Configuration knowledge

- `application.properties`/`.yml`, **profiles**  (`dev`, `test`, `prod`) and property precedence.
- **`@ConfigurationProperties`**  records for type-safe, validated settings, preferred over scattered `@Value`.
- **Environment variables**  with relaxed binding: `SPRING_DATASOURCE_URL` binds to `spring.datasource.url`.
- **Secrets**  never belong in Git. Use environment or platform secrets, Vault (Spring Cloud Vault) or a cloud secret manager.

### 4.6 Testing

- **JUnit (6.x in the Spring 7 generation), Mockito and AssertJ.**  [spring](https://spring.io/blog/2025/11/13/spring-framework-7-0-general-availability/)
- **A test pyramid:**
    1. plain unit tests without Spring;
    2. **slices**  (`@WebMvcTest`, `@DataJpaTest`);
    3. a few **`@SpringBootTest`**  integration tests.
- **Testcontainers**  with `@ServiceConnection`, to test against real PostgreSQL, Kafka or Redis instead of H2.
- **Context caching:**  keep test configurations consistent so Spring can reuse application contexts and the suite stays fast.

### 4.7 Operations and production

- **Logging:**  SLF4J with Logback by default; structured JSON logging is available since Boot 3.4. [danvega](https://www.danvega.dev/blog/spring-boot-3-features)
- **Actuator**  health and readiness probes for Kubernetes; **Micrometer**  metrics, for example Prometheus.
- **Tracing:**  Micrometer Tracing/OpenTelemetry, with OTLP improvements in 4.1. [infoq](https://www.infoq.com/news/2026/06/spring-boot-4-1/)
- **Packaging:**  fat JARs, layered images through Cloud Native **Buildpacks**  (`spring-boot:build-image`), Dockerfiles, and GraalVM native images where startup time matters.
- **12-factor principles:**  configuration in the environment, stateless processes, logs as event streams, dev/prod parity.

### 4.8 Debugging auto-configuration

- Run with `--debug` or `debug=true` to print the **conditions evaluation report** , which shows which auto-configurations matched and why others backed off.
- Use the Actuator `conditions`, `beans`, `configprops` and `mappings` endpoints in non-production environments.
- Read the source of the relevant `*AutoConfiguration` class. Boot’s code is readable, and its `@Conditional` annotations document its behavior.
- Treat the **official reference docs**  (docs.spring.io), the **release notes and migration guides**  on the GitHub wikis, and the Spring blog as primary sources. Version-tracking sites, as shown above, sometimes publish wrong baselines.

### 4.9 Suggested learning path

1. **Core Java 17–21** , plus HTTP and SQL fundamentals.
2. **Raw Servlet basics.**  Write one servlet and one filter so you understand what Spring MVC and Spring Security sit on.
3. **Spring core:**  IoC/DI, bean lifecycle and scopes, `@Configuration`/`@Bean`, profiles.
4. **Spring Boot plus Spring MVC:**  a REST API with validation, error handling and `RestClient`.
5. **Data:**  JdbcClient, JPA/Hibernate, Spring Data, `@Transactional` semantics, Flyway.
6. **Testing:**  JUnit, Mockito, slices, Testcontainers.
7. **Spring Security:**  session login, then OAuth2 resource server with JWT.
8. **Production:**  Actuator, Micrometer and OpenTelemetry, Docker/Buildpacks, configuration and secrets.
9. **Specialize:**  WebFlux, Cloud, Batch, Modulith, Spring AI, native images.

**Newcomer pitfalls:**  copying pre-2022 tutorials that use `javax.*`, `WebSecurityConfigurerAdapter` or `RestTemplate`-only examples. Others: treating annotations as magic instead of proxies, ignoring transaction boundaries, exposing entities directly, and mixing incompatible library versions instead of letting the Boot BOM manage them.

**Certification and resources.**  The **Spring Certified Professional**  exam (code 2V0-72.22, now run by Broadcom) is still offered. Broadcom’s official exam datasheet describes it as “a 60-item exam, with a passing score of 300 using a scaled method”, with a 130-minute time limit; third-party prep sites put the price at $250. It covers configuration, bean lifecycle, AOP, JDBC and transactions, Spring Data, MVC/REST, security, testing and Boot. According to springcertified.com, the 2024 v2 exam covers Spring Framework 5.3 and Spring Boot 2.x, so check the current version on Broadcom’s education portal before you prepare. According to a Spring blog post of April 10, 2024, Spring Academy Pro, which includes the certification learning path, no longer requires a paid subscription for anyone registering a work, vocational or educational email address. Other good resources: spring.io guides, the reference docs, Baeldung, InfoQ’s Java/Spring news, and the Spring team’s own talks.

---

## Recommendations

- **Starting a new project in October 2026?**  Use **Spring Boot 4.1.x on Java 21 or 25** . Plan to move to **4.2 after its November 2026 GA** , because Spring’s own support data lists December 31, 2026 as the end of 4.0.x open-source support (4.1.x runs to July 31, 2027), and Spring’s support policy gives each minor line at least 13 months of free open-source patches.
- **Still on Boot 2.x or 3.x?**  Spring Boot 3.5’s open-source patches ended in June 2026. [herodevs](https://www.herodevs.com/blog-posts/spring-boot-versions-eol-dates-and-latest-releases-april-2026) Upgrade first to the latest 3.5, then to 4.x. Budget for these changes:
    - Jackson 3;
    - modular starters and auto-configuration packages;
    - JSpecify nullness;
    - Jakarta EE 11.
  If you are coming from 2.x, budget separately for the earlier `javax`→`jakarta` migration.
- **Invest in fundamentals before features.**  Most production Spring bugs come from four sources: proxy semantics (self-invocation, transaction boundaries), JPA fetching (N+1, lazy loading), thread-safety of singletons, and misread auto-configuration. None of these are framework defects.

## Caveats

- **Spring 4.2 and Framework 7.1 are not final.**  Their dates and features come from milestone release notes and InfoQ reporting and could change before GA.
- **Some historical dates vary by source.**  These include the month Johnson’s book was published (October vs November 2002) and the EJB 2.0 final date (the JCP gives September 24, 2001). [jcp](https://jcp.org/en/jsr/detail?id=19)
- **Support-window dates differ slightly across third-party trackers.**  Check them against spring.io’s support page.
- **Only the certification price comes from third-party prep sites.**  The exam format comes from Broadcom’s official datasheet.