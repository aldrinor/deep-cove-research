# From Java Servlets to Spring Boot: An Analytical History, the Core of the Spring Framework, and the Knowledge a Spring Developer Needs (status as of 23 September 2026) 

The path from the Java Servlet API to Spring Boot is a sequence of corrections. Each layer kept the one beneath it and hid a burden the earlier layer had left to the developer. Servlets replaced CGI's process-per-request model with a managed, multithreaded container. JSP and MVC frameworks such as Struts separated presentation from control. Spring replaced the invasive EJB 2.x component model with dependency-injected plain Java objects. Spring Boot replaced hand-assembled configuration, dependency version management and external container deployment with classpath-conditional auto-configuration, curated dependency sets and embedded servers. As of 23 September 2026, the current generation is Spring Framework 7.0 (GA 13 November 2025) and Spring Boot 4.1 (4.1.0 on 10 June 2026; 4.1.1 on 20 August 2026). Spring +2 Spring Boot 4.2.0-M1 shipped on 20 August 2026 and the 4.2 GA is expected in November 2026. Every Spring Boot 3.x line is now outside free open-source support. 

## TL;DR 

- The lineage is cumulative, not a series of replacements. Spring MVC still runs as a servlet ( `DispatcherServlet` ). Spring Boot is Spring Framework plus conventions. Spring Framework 7 targets Jakarta EE 11 (Servlet 6.1, JPA 3.2, Bean Validation 3.1). Understanding the Servlet API, dependency injection and proxies is still what separates developers who can debug Spring from those who can only configure it. 

- Each iteration solved a named problem and created a new one. Servlets fixed CGI's overhead but pushed HTML into Java code. JSP fixed authoring but invited "scriptlet spaghetti". Struts enforced MVC at the price of XML and coupling to the Servlet API. EJB 2.x offered declarative enterprise services but was invasive and hard to test. Spring's POJO/DI/AOP model fixed testability and invasiveness but moved the burden into configuration and dependency management. Spring Boot fixed that burden through conventions whose behaviour is implicit. 

- Current state (verified September 2026): Spring Framework 7.0.x and Spring Boot 4.x keep a Java 17 baseline while "embracing" Java 25. Boot 3.5 open-source support ended 30 June 2026, Boot 4.0's ends 31 December 2026, and Boot 4.1 is supported to 31 July 2027 (per Spring's generations feed as quoted secondhand). New work should target Boot 4.1 on Java 21 or 25. 

## 1. Introduction: The Recurring Tensions 

Three tensions recur at every stage of this history. 

1. Abstraction vs. control. Each layer hides machinery (sockets, threads, transactions, bean wiring) to raise productivity, and each makes behaviour harder to see when 

something fails. Spring Boot's auto-configuration is the extreme case: much of what an application does is decided by which JARs are on the classpath. 

2. Standardisation vs. innovation. The Java Community Process (JCP), and later the Eclipse Foundation's Jakarta EE process, produced portable specifications (Servlet, JSP, EJB, JPA, CDI). Open-source frameworks (Struts, Hibernate, Spring, Guice, Seam) innovated faster, and the standards later absorbed their ideas. Spring has mostly consumed the standards at the bottom of the stack (Servlet, JPA, Bean Validation) while competing with them in the component model. 

3. Configuration burden vs. flexibility. Deployment descriptors, `struts-config.xml` , Spring XML, Java `@Configuration` classes and Boot's `application.yml` are successive answers to one question: how much must the developer state explicitly, and how much can the framework infer? 

## 2. Chronological Timeline 

|Year|Technology / version|Governingspecor<br>release|Problem<br>addressed|Limitation that<br>motivatedthe<br>nextiteration|
|---|---|---|---|---|
|1996–<br>1998|Java ServletAPI<br>(announced JavaOne May<br>1996;Java Web Server<br>shipped5June1997;API<br>2.0Dec1997)<br>Wikipedia|SunMicrosystems<br>(pre-JCP)|CGI's process-per-<br>requestcost; no<br>portable in-<br>process server<br>extension model|HTML generated<br>inJavavia<br>`out.println`|
|1999|Servlet 2.1 (Jan), 2.2 (Dec);<br>JSP1.0 (Jun), 1.1 (Dec);<br>TomcatdonatedtoApache|Sunexpertgroups<br>(JamesDavidson,<br>servletlead)<br>Raibledesigns|Page-centric<br>authoring;<br>`web.xml` /WAR<br>model|Scriptlets mixed<br>logic into views<br>("Model1")|
|2000–<br>2001|Apache Struts 1 (donated<br>May 2000; 1.0June2001);<br>Servlet 2.3 (JSR53, final25<br>Sep 2001)<br>Wikipedia<br>jcp|Apache Jakarta<br>project /JCP|Enforced Model2<br>MVCvia a front<br>controller; filters|HeavyXML,<br>ServletAPI<br>coupling,<br>singletonActions,<br>hardto unit-test|
|1999–<br>2003|J2EE1.2–1.4 with EJB<br>1.x/2.x|JCP|Distributed<br>transactions,<br>security,<br>persistence,<br>remoting|Invasive APIs,<br>descriptors,<br>container-bound<br>testing|
|2002|ExpertOne-on-One J2EE<br>Designand Development<br>(Rod Johnson,Wrox,Oct<br>2002)<br>Wikipedia<br>ADTmag|Bookwith<br>"Interface21"<br>framework code|Critiqueof EJB-<br>centric<br>architecture|Codeneeded a<br>projectand<br>community|
|2003–<br>2004|Spring0.9 (Jun 2003) →<br>Spring1.0 (24Mar 2004);<br>Fowler'sDI article(Jan<br>2004)<br>researchr +2|spring.io;<br>martinfowler.com|POJOs,IoC/DI,<br>AOP,declarative<br>transactions<br>withoutEJB|Verbose XML<br>beandefinitions|
|2006|EJB3.0 +JPA1.0 (JSR220,<br>final11May 2006);<br>Spring2.0 (Oct 2006)<br>jcp<br>Spring|JCP/Spring|Standardsabsorb<br>POJOsand<br>annotations;XML<br>namespaces,<br>AspectJ|Still XML-centric|

|Year|Technology / version|Governingspecor<br>release|Problem<br>addressed|Limitation that<br>motivatedthe<br>nextiteration|
|---|---|---|---|---|
|2007|Spring2.5 (19Nov 2007)|Springrelease|Annotation-<br>drivenDI,<br>component<br>scanning,<br>annotated<br>controllers<br>Spring|Mixed<br>XML/annotation<br>configuration|
|2008|SpringSource acquires<br>G2One(Grails/Groovy), 11<br>Nov 2008<br>Spring<br>Wikipedia|Company<br>announcement|Convention over<br>configuration<br>enters the Spring<br>family|—|
|2009|Spring3.0 (16Dec2009);<br>Java EE6,CDI(JSR299)<br>and Servlet 3.0 (JSR315)<br>final10Dec2009;JSR330<br>final14Oct 2009<br>Spring +4|Spring/JCP|Java config,SpEL,<br>REST;<br>standardised DI|Manylibraries to<br>assemble and<br>versionbyhand|
|2011|Spring3.1 (13Dec2011)|Springrelease|Profiles,<br>Environment,<br>`@Enable*` ,<br>caching<br>Spring|Configuration still<br>hand-assembled|
|2012|SPR-9888 "containerless"<br>issue(Mike Youngstrom,<br>Oct 2012)<br>github<br>Medium|Spring JIRA/<br>GitHub#14521|Asksfora<br>`main()` -<br>bootstrapped<br>Spring<br>architecture|—|
|2013|Servlet 3.1 (JSR340, final<br>28May 2013);<br>Spring<br>4.0 (Dec2013)<br>jcp<br>Wikipedia|JCP/Spring|Non-blocking I/O;<br>Java8,<br>WebSocket,<br>`@Conditional`|—|
|2014|Spring Boot 1.0GA(1Apr<br>2014)<br>Spring<br>Spring|spring.io|Auto-<br>configuration,<br>starters,<br>embedded|Opaque"magic";<br>startupcost|

|Year|Technology / version|Governingspecor<br>release|Problem<br>addressed|Limitation that<br>motivatedthe<br>nextiteration|
|---|---|---|---|---|
||||containers,<br>Actuator||
|2017|Servlet 4.0 (JSR369, final5<br>Sep 2017);Spring5.0<br>(WebFlux,Kotlin);Java EE<br>toEclipse(Sep 2017)<br>ADTmag<br>jcp|JCP/Spring/<br>Oracle|HTTP/2; reactive<br>stack|Reactive<br>complexity|
|2018|"Jakarta EE" name(26Feb<br>2018);<br>Spring Boot 2.0 (1Mar<br>2018)<br>eclipse-foundation|Eclipse/ spring.io|Java8baseline,<br>WebFlux,<br>Micrometer<br>Spring|`javax`<br>namespace frozen|
|2020|Jakarta EE9 (8Dec2020):<br>`javax.*` →<br>`jakarta.*`<br>Eclipse Foundation<br>Jakarta EE|Eclipse Foundation|Frees the<br>namespace from<br>Oracle's<br>trademark|Ecosystem-wide<br>migration|
|2022–<br>2023|Jakarta EE10 (22Sep 2022);<br>Spring Framework6.0 (16<br>Nov 2022);<br>Spring Boot<br>3.0 (24Nov 2022);<br>Framework6.1 /Boot 3.2<br>(Nov 2023)<br>Jakarta EE<br>Wikipedia|Eclipse/ spring.io|Java17,Jakarta<br>namespace,<br>GraalVMnative,<br>observability;<br>virtualthreads<br>Spring|Migrationcost;<br>native constraints|
|2024–<br>2025|Jakarta Servlet 6.1 (28Mar<br>2024);Boot 3.5 (May 2025);<br>Jakarta EE11 (26Jun 2025);<br>Spring Framework7.0 (13<br>Nov 2025);<br>Spring Boot<br>4.0 (20Nov 2025)<br>Spring<br>Jakarta EE<br>Jakarta EE +2|jakarta.ee/<br>spring.io|Jakarta EE11,<br>JSpecify null<br>safety,<br>modularised Boot,<br>APIversioning|Upgrade effort<br>(Jackson 3,<br>Hibernate7)|
|2026|Spring Boot 4.1.0 (10Jun),<br>4.1.1 (20Aug);Boot 3.5<br>open-sourcesupportends<br>(30Jun)<br>Spring +2|spring.io|gRPC,SSRF<br>mitigation,<br>OpenTelemetry|Boot 4.2expected<br>Nov 2026|

Where the record is thin. Early Servlet dates are poorly documented. Wikipedia-derived sources say version 1.0 was "finalized in June 1997" (credited to Pavani Diwanji). O'Reilly's Java Servlet Programming covers "Version 2.0 of the Servlet API, which was introduced as part of the Java Web Server 1.1 in December 1997 and clarified by the release of the Java Servlet Development Kit 2.0 in April 1998". Encyclopedia MDPI The JSP specification's historical note gives the 1999 dates for Servlet 2.1/2.2 and JSP 1.0/1.1. Raibledesigns No Sun-authored document fixes a "Servlet 1.0" date, so treat pre-1999 dates as approximate. The Struts 1.0 date (June 2001) likewise comes from secondary sources. Java-samples EDUCBA 

## 3. The Stages: Problem → Solution → New Problem 

3.1 The Java Servlet API (1996–present) 

What a servlet is. A servlet is a Java class, typically extending `HttpServlet` , that a servlet container (Tomcat, Jetty, or an application server's web tier) loads, initialises once ( `init` ), calls for each request ( `service` → `doGet` / `doPost` ) and eventually destroys ( `destroy` ). The container owns the socket, parses HTTP, maps URLs to servlets and dispatches each request on a worker thread from its pool, passing `HttpServletRequest` , `HttpServletResponse` and `HttpSession` objects. uspto 

Problems solved. Compared with CGI, which started an operating-system process per request, servlets run in one long-lived JVM, one thread per request, so start-up cost is paid once and state (connection pools, caches) survives between requests. `HttpSession` gave a standard answer to HTTP's statelessness. Servlets were portable, unlike the vendor-specific NSAPI/ISAPI extensions of the time. uspto The Swiss Bay 

Governance. James Gosling's 1994/95 Java web server work led to the 1996 Java Web Server project (lead engineer Pavani Diwanji). James Duncan Davidson led the expert group for Servlet 2.1 (January 1999) and 2.2 (December 1999), Raibledesigns Javasprint and his reference implementation, internally "Tomcat", went to Apache in 1999. Tomitribe daily.dev JCP versions followed: 2.3 (JSR 53, 25 Sep 2001), filters and listeners; 2.4 (JSR 154, 24 Nov 2003); 2.5 (a JSR 154 maintenance release, 11 May 2006); 3.0 (JSR 315, 10 Dec 2009), annotations, pluggability, async; 3.1 (JSR 340, 28 May 2013), non-blocking I/O; 4.0 (JSR 369, 5 Sep 2017), HTTP/2 jcp +4 (Oracle's licence page says "August 2017"; the JCP date is used here). Oracle Under Eclipse, Jakarta Servlet 5.0 changed only the namespace, 6.0 removed deprecated APIs such as `SingleThreadModel` , and 6.1 (final 28 March 2024, Jakarta EE 11) removed SecurityManager references and added control of redirect status codes and bodies. Eclipse +3 

Problems created. Markup embedded in Java ( `out.println("<table>...")` ), with no separation of presentation from logic. Manual request parsing ( `getParameter` returns `String` ), conversion and validation. Thread-safety traps, because one servlet instance serves all threads. Poor testability outside a container. These still matter: 

`DispatcherServlet` is an `HttpServlet` , Spring Security is a servlet `Filter` chain, and the thread-per-request model is exactly what virtual threads now make cheaper. 

### 3.2 JSP, JavaBeans, JSTL and Model 1 vs. Model 2 (1999–early 2000s) 

JavaServer Pages inverted the servlet: HTML templates with embedded Java, compiled into servlets. JavaBeans ( `<jsp:useBean>` ) carried data. Custom tag libraries and later JSTL plus the Expression Language offered logic-free rendering. In "Model 1", each JSP handled its own request. In "Model 2" (MVC for the web), a servlet controller handles the request, calls the model and forwards to a JSP that only renders. Nothing enforced Model 2, so scriptlets ( `<% ... %>` ) let business logic and even SQL leak into views ("scriptlet spaghetti"). Frameworks arose to institutionalise Model 2. 

### 3.3 Apache Struts 1 and contemporaries (2000–2013) 

Craig McClanahan, who served on the Servlet 2.2/2.3 and JSP 1.1/1.2 expert groups and was architect of Tomcat's Catalina container, donated Struts to Apache in May 2000. Version 1.0 followed in June 2001. Dinesh on Java Wikipedia Matt Raible, quoted by InfoQ, called Struts 1.x "the 'Killer App' for J2EE" because "people were struggling with Servlets and JSPs and how to architect their web applications back in 2001." infoq 

Mechanics. A front controller, `ActionServlet` , received all `*.do` requests. It consulted `struts-config.xml` to map paths to `Action` classes, populated `ActionForm` beans from parameters, validated them, called `Action.execute(mapping, form, request, response)` and forwarded to a logical view (JSP, later Tiles). Grokipedia MVC became structurally enforced. 

Limitations. Heavy XML configuration. Tight coupling to the Servlet API and inheritance from framework base classes. Singleton Actions shared across threads, so instance state produced thread-safety bugs. Poor unit-testability (mocking the servlet environment or using StrutsTestCase). `ActionForm` classes duplicated the domain model. 

Contemporaries. WebWork, an interceptor-based and more POJO-like design, merged with Struts to become Struts 2 (announced December 2005). Wikipedia Tapestry pursued a component model, and JavaServer Faces, co-led by McClanahan, standardised a component/event model. Grokipedia The final Struts 1 release was 1.3.10 (December 2008), and Apache declared Struts 1 end-of-life in 2013. Wikipedia infoq 

### 3.4 J2EE and Enterprise JavaBeans 1.x/2.x (1998–2006) 

The vision and the solution. Developers would write business components (EJBs), and a heavyweight application server (BEA WebLogic, IBM WebSphere, JBoss) would supply distributed transactions (JTA), declarative security, persistence, remoting (RMI/IIOP), pooling and scalability. Components were located via JNDI and configured through XML deployment descriptors ( `ejb-jar.xml` plus vendor files). Session beans encapsulated operations, entity beans with container-managed persistence (CMP) represented data, and message-driven beans arrived in EJB 2.0. Each EJB 2.x component needed a bean class 

implementing `SessionBean` / `EntityBean` , a home interface and a remote and/or local interface. 

Problems created. Business logic was tied to EJB interfaces, lifecycle callbacks ( `ejbCreate` , `ejbActivate` ) and checked `RemoteException` s. Unit tests needed a deployed server. Development cycles were slow (package, deploy, restart). Remote-by-default design produced patterns such as Data Transfer Objects and Session Façades that existed mainly to work around the model. Entity-bean persistence was widely judged inferior to O/R mappers like Hibernate. Vendor-specific descriptors undermined portability. 

The critiques. Rod Johnson's Expert One-on-One J2EE Design and Development (Wrox, October 2002) argued from project experience that most applications did not need distributed EJBs. ADTmag Its roughly 30,000 lines of "Interface21 framework" code (package `com.interface21` ) showed the alternative: Wikipedia Svitla Systems factoryconfigured JavaBeans, a JDBC abstraction and a web MVC framework. J2EE Development without EJB (Wrox, 2004, with Juergen Hoeller) generalised this into lightweight containers, POJOs, AOP-based declarative services and testability. These books are the primary statement of Spring's design rationale. Later retrospective claims about why "EJB failed" are community narrative unless traceable to such texts. 

### 3.5 The Spring Framework (2003–present) 

Origins. Per the Apress/Springer text Spring Basics, Spring "has its origins in the companion code for Rod Johnson's book". Two Wrox-forum readers, Juergen Hoeller and Yann Caroff, "persuaded Rod to turn the code into an open source project", and because the "Interface21 framework" name did not suit a community, "they felt they needed a name that could better inspire a community." Springer Work began around February 2003. Version 0.9 was released under Apache 2.0 in June 2003, and Spring Framework 1.0 final was announced 24 March 2004 (spring.io, Thomas Risberg). Spring Quickprogramming... Hoeller has led the core framework since 2003. P2hp The company Interface21 (2004) later became SpringSource, then passed through VMware and Pivotal and is now part of Broadcom. (The story that "Spring" meant a fresh start after the J2EE "winter" appears only in secondary retellings. Treat it as folklore.) Quickprogramming... Theblog 

What 1.0 contained. The announcement lists "the most sophisticated lightweight container available today, with various flavors of setter and constructor injection", an "AOP interception framework based on the AOP Alliance interfaces", JNDI support, an application context "providing resource loading and message access abstractions", and "generic transaction management with pluggable strategies, supporting declarative and programmatic demarcation", Spring plus JDBC/ORM support and web MVC. 

### Core ideas as a response to EJB. 

|EJB2.x problem|Spring'sanswer|
|---|---|
|Componentsimplement<br>containerinterfaces;JNDI<br>lookups|POJOs plus IoC/DI: the containerbuilds objectsandsupplies<br>collaborators|
|Declarativeservices onlyinside<br>anEJB container|AOPproxiesapply transactionsandsecurity toanySpring bean|
|Transactions require JTA and|**`PlatformTransactionManager`** : thesame<br>`@Transactional`|
|anapp server|codeoverJDBC,JPAorJTA|
|JDBC boilerplate,checked|Templates (<br>`JdbcTemplate` ) manageresources; theunchecked|
|`SQLException`|**`DataAccessException`**hierarchy translates vendorerrors|
|Testingneedsa deployedserver|Plain objectsconstructedwithmocks;in-processintegration tests|
|Vendorlock-in|Consistentabstractions over persistence, messaging, remoting|

The DI terminology. Martin Fowler's "Inversion of Control Containers and the Dependency Injection pattern" (January 2004) noted "a rush of lightweight containers" whose wiring pattern went by "the very generic name of 'Inversion of Control'". He proposed "the more specific name of 'Dependency Injection'", renamed "type 1/2/3 IoC" as interface, setter and constructor injection, HackerNoon researchr and concluded that the choice between DI and Service Locator "is less important than the principle of separating configuration from use." Goodreads (The article is usually dated 23 January 2004, but Matt Raible blogged on 14 January 2004 that it had reached the spring-user list, so an earlier version probably circulated first. "January 2004" is the safe citation.) Raibledesigns The StoryGraph 

Spring MVC vs. Struts. Spring MVC keeps the front controller but makes every part a pluggable strategy: `DispatcherServlet` → `HandlerMapping` → `HandlerAdapter` → handler → `ViewResolver` . Controllers are ordinary injected beans, not framework base classes (after 2.5), and can be tested without a container. 

Milestones (spring.io announcements unless noted). 

- 2.0 (October 2006, per Spring's 2.5 reference docs): extensible XML namespaces ( `<tx:>` , `<aop:>` ), AspectJ pointcuts and `@AspectJ` , new bean scopes. Spring 2.5 (19 November 2007): "auto-detecting application components in the classpath", "a new annotation-based controller model for Spring MVC", `@Autowired` ("the one configuration annotation that rules them all", in Hoeller's words), JSR-250 

- `@PostConstruct` / `@PreDestroy` / `@Resource` , `@RequestMapping` , the TestContext 

- Framework. Spring Spring 

- 3.0 (16 December 2009): Java 5-based; SpEL; "comprehensive REST support" 

- ( `@PathVariable` , `RestTemplate` ); `@Configuration` / `@Bean` ; `@Inject` (JSR 330); Java EE 

- 6 compatibility. Spring Spring 

- 3.1 (13 December 2011): "the environment abstraction and the associated bean definition profiles", "@Enable* annotations", and "the cache abstraction with our declarative caching solution (@Cacheable etc)". Spring 

- 4.0 (GA 12 December 2013, per Adrian Colyer's spring.io post "Announcing Spring Framework 4.0 GA Release", which says "Spring Framework 4.0 offers 1st class Java 8 support"): Java 8, WebSocket/STOMP, `@Conditional` , the mechanism Boot builds on. 4.3 (June 2016) was the last Java 6+/Servlet 2.5+ generation. Wikipedia 

- 5.0 (GA 28 September 2017; Juergen Hoeller on spring.io: "Spring Framework 5.0 is finally generally available as 5.0.0.RELEASE... with support for JDK 9 and the Java EE 8 API level (e.g. Servlet 4.0)"): Reactor-based Spring WebFlux, Kotlin, Java 8 baseline. 

- 6.0 (16 November 2022): Java 17, Jakarta EE 9+ with a Jakarta EE 10 focus (Servlet 6.0, JPA 3.1), Wikipedia AOT engine for GraalVM, Micrometer Observation, `ProblemDetail` , HTTP interface clients. 

- 6.1 (November 2023): virtual threads, `RestClient` , `JdbcClient` . 6.2 (November 2024): last 6.x, under Boot 3.4/3.5. 

- 7.0 (13 November 2025): Hoeller called it "the beginning of a new framework generation with a focus on Java 25". Its baseline items are "Embracing Java 25 (as the latest LTS) while retaining a Java 17 baseline", "Jakarta EE 11 API level: Servlet 6.1, JPA 3.2, Bean Validation 3.1", Spring "Comprehensive null safety through JSpecify", Jackson 3.0 (2.x deprecated), Kotlin 2.2 and JUnit 6.0. New features are programmatic bean registration, spring resilience annotations ( `@Retryable` , `@ConcurrencyLimit` , from the former spring-retry project), `JmsClient` , API versioning, HTTP interface client configuration and `RestTestClient` . Spring The release notes deprecate `RestTemplate` in the documentation, with the formal `@Deprecated` annotation arriving 

- in 7.1, and deprecate the `<mvc:*>` XML namespace. GitHub Maintenance continues (for example 7.0.3 on 15 January 2026; Boot 4.1.0 ships 7.0.8, which caps SpEL evaluation at 10,000 operations by default). Spring +2 

3.6 The standards respond: EJB 3.0, JPA, CDI, JSR 330, Jakarta EE 

- EJB 3.0 and JPA 1.0 (JSR 220, final 11 May 2006) brought annotations, POJO-style beans without home interfaces, resource injection, and a standard ORM API shaped by Hibernate. Java Community Pro... jcp This is the clearest case of standards absorbing proven open-source ideas. 

- JSR 330 (final 14 Oct 2009) standardised `@Inject` , `@Named` , `@Qualifier` and `@Singleton` , led jointly by Guice's Bob Lee and Spring's Rod Johnson. jcp Spring 3.0 

- supported it at GA. Spring 

- JSR 299 CDI 1.0 (final 10 Dec 2009), originally "Web Beans" and influenced by Seam and Guice, gave Java EE a full contextual DI model. It shipped in Java EE 6 (JSR 316, 10 Dec 2009) with Servlet 3.0. Java Community Pro... 

- The move to Eclipse. Oracle announced its intention to open up Java EE in August 2017. Eclipse Foundation Executive Director Mike Milinkovich then wrote in "Java EE Moves to the Eclipse Foundation" that "Oracle announced today that they, along with IBM and Red Hat, will be moving Java EE to the Eclipse Foundation"; SiliconANGLE's coverage of that announcement is dated 12 September 2017. The Eclipse Foundation announced "Jakarta EE" on 26 February 2018 ("Almost 7,000 people voted in our community poll, and over 64% voted in favour of Jakarta EE"). eclipse-foundation 

- The namespace break. Jakarta EE 8 (10 September 2019) kept `javax.*` . Jakarta EE 9 (8 December 2020) completed "the transition from the use of the javax.* package namespace to jakarta.*". Jakarta EE Jakarta EE Jakarta EE 10 followed on 22 September 2022, and Jakarta EE 11 was announced as generally available on 26 June 2025 (the Eclipse process record gives 18 June 2025). Jakarta EE +2 

Relation to Spring. Spring and the platform converged on ideas (POJOs, annotations, DI) but diverged on deployment and governance. Spring treats Jakarta specifications as APIs it implements against, not a runtime the application must be deployed into. Spring's major versions are therefore paced by Jakarta baselines: Spring 6/Boot 3 forced the `jakarta.*` migration, and Spring 7/Boot 4 moved to Jakarta EE 11 Spring Spring (Tomcat 11, Hibernate ORM 7, Hibernate Validator 9, per Hoeller's October 2024 roadmap). Spring 

### 3.7 What persisted and motivated Spring Boot 

By about 2012, Spring had solved invasiveness and testability but left four burdens: 

1. Configuration assembly. Every application re-declared the same `DataSource` , `EntityManagerFactory` , transaction manager, `DispatcherServlet` , converters and 

security chain. 

2. Dependency version management. Mutually compatible versions of Spring modules, Hibernate, Jackson, logging bridges and transitive dependencies had to be found by hand. Spring 3.0.3 stopped shipping a dependencies download "due to legal implications with the multitude of licenses", which pushed users onto Maven/Ivy. Spring 

3. WAR packaging and external containers, a poor fit for the emerging PaaS and microservice model. 

4. Slow project bootstrapping, and no production-readiness features (health, metrics, externalised configuration) out of the box. 

Convention-over-configuration influences. Ruby on Rails popularised the principle, and Grails brought it to the JVM on top of Spring. InfoWorld (2008) noted that Grails, "like the popular Ruby on Rails Web framework, follows the philosophy of 'convention over configuration'". InfoWorld SpringSource acquired G2One on 11 November 2008, which Rod Johnson announced as "More Weapons for the War on Complexity". eWEEK Spring Dropwizard showed the self-contained embedded-Jetty service model. 

The originating issue. In SPR-9888 (October 2012; GitHub spring-framework #14521), Mike Youngstrom wrote: "Traditionally Spring web applications have been embedded in a servlet container. This was useful in the past when the majority of enterprise applications ran in and depended on the servlet container for deployment and configuration." He argued that "Spring's dependence on frameworks and containers outside of Spring's component model increases the learning curve", proposed embedding container services "within a Spring Container bootstrapped from a simple main() method", and named DropWizard as the main inspiration. DZone github Phil Webb and Dave Syer led the resulting work, shown at SpringOne2GX 2013, and Spring Boot 1.0 GA shipped on 1 April 2014. Spring Webb noted "18 months since the original request to 'improve containerless web application architectures', that gave birth to Spring Boot", with "1720 commits by 54 different contributors". He described Boot as "an ultralight container, great for application or service deployment in the cloud", since "Today's PaaS environments provide much of the management, scale out, and reliability features already". Spring Spring 

## 4. Core Functionalities of the Spring Framework 

### 4.1 The IoC container 

- **`BeanFactory`** vs. **`ApplicationContext`** . `BeanFactory` is the minimal container that 

- instantiates and wires beans from `BeanDefinition` s. `ApplicationContext` adds eager singleton creation, automatic post-processor registration, events, internationalisation, resource loading and the `Environment` . Applications almost always use the latter. 

- Bean definitions. Bean definitions come from XML, component scanning, `@Bean` methods, or (since 7.0) programmatic registration. The reference documentation notes these "are then converted internally into instances of BeanDefinition and used to load an entire Spring IoC container instance". Spring 

- Scopes. `singleton` (default), `prototype` , and the web scopes `request` , `session` , `application` and `websocket` . Injecting a shorter-lived bean into a singleton requires a 

- scoped proxy or `ObjectProvider` . 

- Lifecycle. Instantiation → injection → `Aware` callbacks → `BeanPostProcessor` beforeinitialisation → `@PostConstruct` / `InitializingBean#afterPropertiesSet` / custom init → after-initialisation (where AOP proxies are usually created) → use → `@PreDestroy` / `DisposableBean#destroy` . A **`BeanFactoryPostProcessor`** modifies definitions (for 

- example, placeholder resolution). A **`BeanPostProcessor`** modifies instances. Much of Spring's "magic" is post-processors. 

DI styles and the documented recommendation. Constructor, setter and field injection are all supported. The reference documentation states: "it is a good rule of thumb to use constructors for mandatory dependencies and setter methods or configuration methods for optional dependencies". It adds that the Spring team "generally advocates constructor injection, as it lets you implement application components as immutable objects and ensures that required dependencies are not 

null." Spring Medium Field injection hides dependencies and blocks plain-Java construction in tests. 

- Disambiguation. `@Qualifier` selects among candidates, `@Primary` sets a default, and `@Lazy` defers creation or injects a lazy proxy. 

Circular dependencies. With constructor injection, "the Spring IoC container detects this circular reference at runtime, and throws a BeanCurrentlyInCreationException". Setter injection can resolve cycles, "although it is not recommended". Spring Spring Boot has prohibited circular references by default since 2.6. 

### 4.2 Component scanning and stereotypes 

`@Component` is the generic stereotype. `@Service` , `@Repository` (which also enables persistence exception translation) and `@Controller` specialise it, Redis and `@RestController` = `@Controller` + `@ResponseBody` . Stereotypes work as meta-annotations, and this composability is what makes `@SpringBootApplication` possible. 

### 4.3 Aspect-oriented programming 

Proxy-based model. Spring AOP wraps beans in a proxy during post-processing. Interface-based beans can use a JDK dynamic proxy. Otherwise, and by default in Spring Boot, Spring uses a CGLIB subclass. AspectJ's pointcut language and `@Before` / `@After` / `@AfterReturning` / `@AfterThrowing` / `@Around` advice are supported, but weaving uses proxies unless full AspectJ weaving is configured. 

Declarative features. `@Transactional` , `@Cacheable` , `@Async` , 

`@Secured` / `@PreAuthorize` and 7.0's `@Retryable` / `@ConcurrencyLimit` are all proxyapplied advisors. 

Self-invocation limitation. A call to another method on the same object ( `this.other()` ) bypasses the proxy, so its annotation is silently ignored. CGLIB also cannot intercept `final` methods or classes. This is the most common source of " `@Transactional` doesn't work" defects. 

### 4.4 Data access and transactions 

JDBC. `JdbcTemplate` manages connections, statements and result sets and translates `SQLException` s. `NamedParameterJdbcTemplate` adds `:name` parameters. `JdbcClient` (6.1+) is a fluent façade over both. 

Transactions. `PlatformTransactionManager` (JDBC, JPA and JTA implementations, plus `ReactiveTransactionManager` ) decouples demarcation from technology. 

`@Transactional` exposes propagation ( `REQUIRED` default, `REQUIRES_NEW` , `NESTED` , `SUPPORTS` , `MANDATORY` , `NOT_SUPPORTED` , `NEVER` ), isolation, `readOnly` , timeouts and rollback rules. By default only unchecked exceptions and `Error` s roll back. 

ORM. JPA integration (Hibernate ORM 7 / JPA 3.2 in the 7.0 generation) via `LocalContainerEntityManagerFactoryBean` and transaction-bound shared `EntityManager` proxies. 

Spring Data generates repositories from interfaces, including derived queries parsed from method names ( `findByEmailAndActiveTrue` ), `@Query` , paging and auditing. 

### 4.5 Web: Spring MVC and Spring WebFlux 

- Spring MVC. `DispatcherServlet` → `HandlerMapping` ( `RequestMappingHandlerMapping` ) → `HandlerAdapter` → argument resolvers ( `@PathVariable` , `@RequestParam` , 

- `@RequestBody` ...) → controller → return-value handlers → **`HttpMessageConverter`** s 

- (Jackson for JSON; 7.0 adds centralised `HttpMessageConverters` configuration and Jackson 3) or a `ViewResolver` . Spring 

- Validation. Jakarta Validation (Bean Validation 3.1) via `@Valid` / `@Validated` . 

- Error handling. `@ExceptionHandler` , `@ControllerAdvice` / `@RestControllerAdvice` , and since 6.0 `ProblemDetail` / `ErrorResponse` for standard problem-details bodies. These were originally based on RFC 7807, which RFC 9457 superseded in July 2023. (Spring's precise RFC 9457 conformance statement was not re-verified.) 

- 7.0 additions. API versioning (header, path or media-type resolution, with deprecation support) and declarative `@HttpExchange` HTTP interface clients. Spring Spring WebFlux (since 5.0). Non-blocking, built on Project Reactor ( `Mono` / `Flux` ), running on Netty or Servlet 3.1+ non-blocking I/O, with annotated or functional endpoints and `WebClient` . 

- Blocking vs. reactive vs. virtual threads. The servlet stack binds one platform thread per request, which limits concurrency under blocking I/O. WebFlux decouples concurrency from threads at the cost of a different, harder-to-debug programming model. Since 6.1/Boot 3.2 on Java 21+, virtual threads let the blocking model scale for I/O-bound workloads. For typical CRUD/REST services this weakens the case for adopting WebFlux purely for throughput, though WebFlux keeps its edge for streaming and back-pressure. This is a considered judgement, not a benchmark result. 

### 4.6 Spring Security 

Spring Security is integrated as a servlet `Filter` ( `DelegatingFilterProxy` → 

`FilterChainProxy` → `SecurityFilterChain` s) or as a `WebFilter` chain on WebFlux. It covers 

authentication (form, Basic, OAuth2/OIDC login, SAML), authorisation (request matchers and proxy-based method security via `@PreAuthorize` ), CSRF protection, session 

management and OAuth2 Resource Server validation of JWTs or opaque tokens. The line shipping with Boot 4.1 is Spring Security 7.1. InfoQ GitHub 

### 4.7 Other core abstractions 

Caching: `@EnableCaching` , `@Cacheable` / `@CachePut` / `@CacheEvict` over pluggable providers. 

Scheduling and async: `@Scheduled` , `@Async` , `TaskExecutor` / `TaskScheduler` and virtual-thread executors. Boot 4.1 adds Micrometer context propagation for `@Async` . daily.dev 

Events: `ApplicationEventPublisher` , `@EventListener` , and 

`@TransactionalEventListener` (after commit or rollback). 

Resources, Environment and SpEL: the `Resource` abstraction ( `classpath:` , `file:` , URLs), `PropertySource` s, `@Profile` , `@Value` , and SpEL expressions in `@Value` , security annotations and cache keys. 

Testing: the TestContext Framework (context caching; since 7.0.3, unused cached contexts are lazily paused), Spring `@SpringJUnitConfig` , transactional test rollback, `MockMvc` , `WebTestClient` and `RestTestClient` (7.0). 

### 4.8 The wider portfolio (brief) 

Spring Data, Spring Security, Spring Cloud, Spring Batch, Spring Integration, Spring for Apache Kafka/AMQP, Spring Modulith, Spring gRPC (auto-configured from Boot 4.1), and Spring AI (2.0 ships alongside Boot 4.1 per InfoQ). InfoQ 

## 5. Spring Boot: Design and Mechanics 

### 5.1 Auto-configuration 

- `@SpringBootApplication` = `@SpringBootConfiguration` + `@EnableAutoConfiguration` + 

- `@ComponentScan` of the annotated class's package. 

- `@EnableAutoConfiguration` imports candidate configuration classes guarded by 

- conditions built on `@Conditional` : `@ConditionalOnClass` (a library is present), 

- `@ConditionalOnMissingBean` (so user beans win and Boot "backs off"), 

`@ConditionalOnProperty` , `@ConditionalOnWebApplication` . Webb put it this way in 2018: "We still auto-configure Spring, based on what is in your classpath. We still back-off if you define your own beans." InfoQ 

Registration. Through Boot 2.6, candidates were listed in `META-INF/spring.factories` under the `EnableAutoConfiguration` key. Boot 2.7 introduced <mark>`META-`</mark> 

<mark>`INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports`</mark> (one class per line) and `@AutoConfiguration` , while still honouring `spring.factories` . Boot 

3.0 removed `spring.factories` registration for auto-configurations; "Other entries in spring.factories under other keys are unaffected." Springcertified +2 Boot 4.0 removed public members from auto-configuration classes, because "Autoconfigurations never have been public API and now this is enforced through Java mechanisms." GitHub 

Diagnosis. `--debug` or the Actuator `conditions` endpoint prints the condition evaluation report, which is essential for demystifying Boot. 

### 5.2 Starters and the curated BOM 

Starters ( `spring-boot-starter-web` , `-data-jpa` , `-security` , `-actuator` ...) are dependency descriptors for coherent library sets. **`spring-boot-dependencies`** is a Maven BOM, inherited via `spring-boot-starter-parent` , imported, or applied as a Gradle platform, that pins tested versions of Spring projects and hundreds of third-party libraries. In InfoQ's words, it keeps 

"overlapping transitive dependencies consistent", infoq which ended most "dependency hell" for mainstream stacks. Boot 4.0 delivered "a complete modularization of the Spring Boot codebase" into "smaller and more focused jars", Spring which changes some artifact coordinates during upgrades. 

### 5.3 Embedded containers and executable JARs 

Boot embeds Tomcat (default), Jetty or Reactor Netty and starts the server from the Spring context, reversing the classic model in which the container hosted Spring. The Boot Maven/Gradle plugins build an executable "fat" JAR, run with `java -jar` , and WAR deployment remains available. The Spring Boot 4.0 Migration Guide (GitHub wiki) records that "Spring Boot 4 requires a Servlet 6.1 baseline, with which Undertow is not yet compatible. As a result, Undertow support is dropped" (tracked as spring-boot issue #46917), and the team later "decided not to reintroduce Undertow support". 

### 5.4 Externalised configuration 

Boot reads property sources in a defined precedence: command-line arguments, environment variables, `application.properties` / `.yml` , profile-specific <mark>`application{profile}.yml` ,</mark> and config trees for Kubernetes secrets. `@ConfigurationProperties` binds hierarchical properties to type-safe objects, including records. Relaxed binding maps `MY_APP_TIMEOUT` , `my-app.timeout` and `myApp.timeout` to the same property. Profiles switch sets of configuration and beans. Boot 4.1 binds `Optional` constructor parameters as `Optional.empty()` . GitHub 

### 5.5 Actuator and observability 

Actuator exposes `health` (with liveness/readiness groups), `info` , `metrics` , `prometheus` , `env` , `loggers` , `conditions` and other endpoints over HTTP or JMX. Since Boot 2.0, Micrometer "replaces the metrics APIs that were previously part of Spring Boot itself" (Webb). InfoQ Boot 3.0 added the Micrometer Observation API and Micrometer Tracing Spring with OTLP/OpenTelemetry export, and Boot 4.1 extended OpenTelemetry support further. Security caveat: Boot 4.0.4 (19 March 2026) fixed "CVE-2026-22731: Authentication Bypass under Actuator Health groups paths" and CVE-2026-22733 for Cloud Foundry endpoints. Spring Expose endpoints deliberately and keep up with patch releases. 

### 5.6 Testing model 

`@SpringBootTest` starts the full context, optionally on a random port. Test slices start only part of it: `@WebMvcTest` (MVC plus the named controllers, with `MockMvc` ), `@DataJpaTest` (JPA and repositories, transactional), `@JsonTest` , `@WebFluxTest` , `@RestClientTest` . `@MockitoBean` succeeded the deprecated `@MockBean` . Testcontainers support with `@ServiceConnection` (Boot 3.1+) wires containerised databases and brokers automatically. Boot 4.1 adds `@AutoConfigureWebServer` for sliced tests that need a server. Spring 

### 5.7 Developer tooling 

DevTools offers restart on classpath change through two classloaders, LiveReload and development defaults. Spring Initializr (start.spring.io) generates projects; InfoQ reported in 2018 that it had generated "over 8 million projects". InfoQ `spring-boot:build-image` / `bootBuildImage` produce OCI images via Cloud Native Buildpacks without a Dockerfile. 

5.8 Boot milestones and current support 

|Version|Date|Key points (source)|
|---|---|---|
|1.0|1Apr 2014<br>Spring|Containerless,auto-configuration, starters,Actuator (Webb, spring.io)<br>Spring|
|2.0|1Mar 2018|"A Java8baseline,and Java9 support.Reactivewebprogramming<br>support with Spring WebFlux";Micrometer; "17 months work andover<br>6800commitsby 215differentindividuals" (Webb)<br>Spring|
|2.7|May 2022|Last 2.x;<br>`AutoConfiguration.imports` ; open-sourcesupport<br>extendedtoNov 2023 (spring.io)<br>Spring<br>github|
|3.0|24Nov 2022|Framework6.0,Java17,Jakarta EE9/10, "Supportforgeneratingnative<br>images with GraalVM, supersedingthe experimental Spring Native<br>project",MicrometerTracing(Wilkinson)<br>Spring<br>Spring|
|3.2|Nov 2023|Virtualthreads (<br>`spring.threads.virtual.enabled` ),<br>`RestClient` ,<br>`JdbcClient`|
|3.3 / 3.4|May 2024 /Nov<br>2024|Incremental; 3.4 open-sourcesupportended31Dec2025 (aggregators)<br>DEV Community|
|3.5|May 2025|Last 3.x, onFramework6.2;InfoQ: "only 13 months of freereleases,but<br>adds 72 months ofpaidones"; open-sourcesupportended30Jun 2026<br>HeroDevs<br>infoq|
|4.0|20Nov 2025|Framework7; modularisation;JSpecify; "Firstclass supportforJava25<br>(whilst retaining Java17compatibility)";APIversioning;HTTPservice<br>clients;Gradle9<br>Spring +2|
|4.1|10Jun 2026<br>(4.1.1: 20Aug<br>2026)|Spring gRPC,Jacksonconfiguration, "HTTP ClientSSRF Mitigation<br>with InetAddressFilter",OpenTelemetry,Log4jrotation;Framework<br>7.0.8,Security 7.1.0,Data2026.0.0<br>Spring +2|
|4.2|4.2.0-M1 on 20<br>Aug2026;GA<br>expected Nov<br>2026|Milestoneon thespring.io releasesblog;GApending(InfoQ)|

Support windows (as of 23 September 2026). Spring's policy page promises open-source minor releases "a minimum of 12 months" of support, and gives the last minor of each major line an extra enterprise period. Spring The per-branch dates below come from Spring's generations feed ( `api.spring.io/projects/spring-boot/generations` ), read secondhand via a third-party GitHub issue and consistent with several independent trackers: GitHub 

|Branch|Open-sourcesupportends|Commercialsupportends|
|---|---|---|
|3.5.x|30Jun 2026 (ended)|30Jun 2032|
|4.0.x|31Dec2026|31Dec2027|
|4.1.x|31Jul2027|31Jul2028|

Conflicting sources. One aggregator (endoflife.ai on dev.to) dates Boot 4.0 to "November 30, 2025" and 4.1 to "June 30, 2026", DEV Community which contradicts the spring.io announcements (20 November 2025; 10 June 2026). Another (versionlog.com) credits Spring Framework 7.0 with features such as "Micrometer 2.0" that appear in no Spring primary source. Redis Both should be disregarded. Java baseline: Boot 4.x requires Java 17. Claims that it requires Java 21 are wrong; only specific integrations (for example jOOQ 3.20 in Boot 4.1) need Java 21. InfoQ GitHub 

## 6. Essential Knowledge for Spring and Spring Boot Developers 

6.1 Foundational knowledge 

1. Java language. Programming to interfaces; generics ( `JpaRepository<User, Long>` ); annotations and reflection (retention, meta-annotations, runtime inspection, which is how Spring discovers `@Component` and `@Transactional` ); lambdas and streams; `Optional` ; records (DTOs, `@ConfigurationProperties` , JPA 3.2 embeddables); and, for 

Boot 4 code, JSpecify `@Nullable` / `@NullMarked` . 

2. Classpath and class loading. Auto-configuration is classpath-conditional, so adding a JAR can change behaviour. Reading dependency trees ( `mvn dependency:tree` , <mark>`gradle dependencies` )</mark> and understanding classloader boundaries (DevTools restart, fat-JAR launcher) are basic diagnostic skills. 

3. Build tooling. Maven and Gradle; BOMs (why Boot-managed dependencies omit versions, and how to override one safely); the Boot plugins (repackaging, <mark>`buildimage`</mark> , AOT processing). 

4. HTTP, REST and Servlet foundations. Methods, status codes, headers, content negotiation, idempotency, CORS. Filters (Spring Security is a filter chain), `DispatcherServlet` as a servlet, the request lifecycle, and the thread-per-request 

model, on which `ThreadLocal` contexts (security, transactions) and virtual-thread behaviour depend. 

   5. SQL and JPA/Hibernate. The entity lifecycle (transient, managed, detached, removed); dirty checking; lazy loading and the N+1 problem (fetch joins, entity graphs, projections); transaction boundaries (why lazy loading outside a transaction fails, and why Boot's default open-in-view hides this and should usually be disabled for APIs). 

   6. Testing practice. JUnit 5 (JUnit 6 in the 7.0 generation), Mockito, AssertJ; unit tests of constructor-injected POJOs without Spring; slice tests; Testcontainers. 

   7. Core Spring concepts. The container, scopes, constructor injection, `@Configuration` / `@Bean` , profiles, `@ConfigurationProperties` , and how to override 

   auto-configuration. 

- 6.2 Advanced knowledge 

   1. Proxy pitfalls. Self-invocation bypassing `@Transactional` / `@Async` / `@Cacheable` . `final` classes and methods cannot be advised by CGLIB, which matters in Kotlin and 

   is why the `kotlin-spring` plugin exists. Non-public methods: historically only public methods were transactional; since 6.0 class-based proxies also cover protected and package-visible methods, but relying on this is fragile. Checked-exception rollback rules. `REQUIRES_NEW` suspending outer transactions. 

   2. Lifecycle and startup. Post-processor ordering; circular dependencies; the "too many beans / slow startup" problem (lazy initialisation, trimming starters, `/actuator/startup` , CDS and AOT caches under Project Leyden, native images). 

   3. Configuration and secrets. Property precedence; keeping secrets out of `application.yml` (environment variables, Kubernetes config trees, Vault or cloud 

   secret managers); validated `@ConfigurationProperties` . 

   4. Observability. Actuator exposure and security; Micrometer meters and Observations; tracing with Micrometer Tracing/OpenTelemetry; structured logging. 

   5. Security. The `SecurityFilterChain` model; authentication vs. authorisation; OAuth2/OIDC and JWT resource servers; CSRF/CORS; method security. Threat awareness matters: Boot 4.1's `InetAddressFilter` targets server-side request forgery, and the 2026 Actuator CVEs show operational endpoints are attack surface. Spring danvega.dev 

   6. Containerisation. Docker; Buildpacks; layered JARs; JVM memory in containers; Kubernetes probes. 

   7. Native compilation trade-offs. GraalVM native images (since Boot 3.0 via Spring AOT) start much faster and use less memory. The costs are long builds, closed-world constraints (reflection and proxies need hints), conditions frozen at build time, and lower peak throughput than a warmed JIT. JVM-side AOT and CDS narrow the gap for many services. 

   8. Concurrency models. Virtual threads for I/O-bound servlet applications on Java 21+, with their pitfalls (pinning on `synchronized` in older JDKs, `ThreadLocal` -heavy 

libraries, connection pools becoming the bottleneck), versus the cases that still justify WebFlux. 

   9. Migration literacy. The **`javax.*`** → **`jakarta.*`** migration remains a real concern for legacy Boot 2.x code, and OpenRewrite automates much of it. Boot 3 → 4 involves modular starters, Jackson 3 ( `tools.jackson` packages), Hibernate 7, JUnit 6, removal in 4.1 ofAPIs deprecated in 4.0, and `RestClient` replacing `RestTemplate` . GitHub +2 

- 6.3 Recommended learning resources 

      - Official: Spring reference documentation (docs.spring.io); GitHub release notes and migration guides; spring.io guides; Spring Academy. 

      - Books: Craig Walls, Spring in Action (Manning; match the edition to your Boot generation); Thomas Vitale, Cloud Native Spring in Action (Manning); Rod Johnson's 2002 and 2004 Wrox books, which explain why Spring is shaped as it is. 

      - Background and secondary: Fowler's 2004 DI article; the Jakarta specifications; InfoQ; Baeldung for established how-tos (check against the reference documentation). 

## 7. Concluding Synthesis 

### 7.1 What the trajectory shows about framework design 

   1. Successful layers subsume rather than replace. The surviving technologies (Servlet, JPA, Bean Validation) became substrates. The discarded ones (Struts 1 Actions, EJB 2.x entity beans) imposed component models through inheritance and containerbound lifecycles. Spring outlasted its rivals largely by being non-invasive. 

   2. Testability was decisive, and it was stated as a goal from the start. Johnson's critique of EJB and Struts centred on testing outside the container. Boot's test slices and Testcontainers support follow the same line. 

   3. Configuration burden moves; it is never eliminated. It went from descriptors to `struts-config.xml` , Spring XML, annotations, Java config and then classpath 

   conventions. Boot's conventions are the most productive stage but make behaviour implicit. The condition evaluation report and Actuator are the price of keeping it debuggable. 

   4. Standards and open source co-evolve. EJB 3.0/JPA absorbed Hibernate and Spring ideas, CDI and JSR 330 standardised DI, and Spring aligns its majors with Jakarta baselines. 

- 7.2 Current state and open trade-offs (as of 23 September 2026) 

      - Versions. Spring Framework 7.0.x and Spring Boot 4.1.x are current, and Boot 4.0.x has free support until 31 December 2026. Boot 4.2.0-M1 shipped on 20 August 2026, with the 4.2 GA expected in November 2026. Recommendation: start new projects on Boot 4.1 with Java 21 or 25. Teams on 3.5 should migrate directly to 4.1 rather than stopping at 4.0, whose open-source window closes in about three months. GitHub 

Blocking vs. reactive vs. virtual threads. For request/response services, default to Spring MVC with virtual threads. Reserve WebFlux for streaming and back-pressure workloads or Reactor-fluent teams. This is a judgement from programming-model costs, not a cited benchmark. 

Alternatives. Jakarta EE 11 runtimes (Open Liberty, Payara, WildFly) offer a standards-based model. Quarkus and Micronaut were designed around build-time DI and native compilation and keep start-up and memory advantages in some scenarios. Spring's counterweights are ecosystem breadth, documentation and support, and a narrowing performance gap through AOT. Choose an alternative when start-up and footprint dominate and the team can accept a smaller ecosystem. Otherwise Spring Boot remains the lower-risk default. 

## Caveats 

Verified from primary sources: all JCP JSR final-release dates; Jakarta EE 9/10/11 and Servlet 6.1; Spring 1.0, 2.5, 3.0, 3.1, 7.0; Spring Boot 1.0, 2.0, 3.0, 4.0, 4.1.0, 4.1.1; the SPR9888 text; the G2One acquisition. 

Secondary sources only: Servlet dates for 1996–1998; Struts 1.0; the Spring 6.0 date (via Wikipedia). Spring 4.0 (12 December 2013) and 5.0 (28 September 2017) are dated from spring.io posts. The final 3.5 patch is confirmed by Andy Wilkinson's spring.io post "Spring Boot 3.5.16 available now" (25 June 2026): "This is the last OSS release of the 3.5.x generation. To continue to receive OSS support, upgrade to 4.0.x or 4.1.x". Support windows come from Spring's generations API as quoted by a third party, so check the Spring Boot "Support" tab before making lifecycle decisions. Engineering recommendations are reasoned judgements, not benchmark results.
