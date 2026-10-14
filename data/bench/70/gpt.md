# **From Java Servlets to Spring Boot: The Evolution of Java Web Application Architecture** 

## **Executive summary** 

The evolution from Java Servlets to Spring Boot is best understood not as a sequence in which one technology simply replaced another, but as a progressive **relocation of infrastructure responsibility away from application code** . Servlets standardized the low-level server-side request/response contract; JSP moved HTML generation toward a view technology; Struts imposed a reusable MVC front-controller structure; JSF raised the abstraction further toward stateful UI components; Spring separated business objects from infrastructure through inversion of control, dependency injection, AOP, portable transaction management, and data-access abstractions; and Spring Boot finally standardized much of the _assembly and operational configuration_ of Spring applications through starters, dependency management, autoconfiguration, embedded servers, executable packaging, and production-oriented facilities such as Actuator. 1 

The historical inflection point was Spring's response to early-2000s enterprise Java complexity. Rod Johnson's 2002 _Expert One-on-One J2EE Design and Development_ included roughly 30,000 lines of framework code implementing ideas that would become Spring: an IoC container, dependency injection, early Spring MVC, <mark>`JdbcTemplate` ,</mark> and technology-independent data-access exceptions. The project became public in June 2003 and Spring Framework 1.0 was released on March 24, 2004. Spring's central proposition was that ordinary Java objects could obtain enterprise capabilities—particularly declarative transactions—without inheriting framework classes or requiring the full EJB/JTA/application-server programming model. 2 

Spring Boot's April 1, 2014 1.0 GA release attacked a different layer of complexity. By then Spring itself had made application code substantially more modular and testable, but developers still had to choose compatible library versions, configure an application context and web container, create deployment descriptors or server deployments, and repeatedly reproduce conventional infrastructure. Boot's answer was an opinionated integration layer: **starters specify coherent dependency sets; auto-configuration reacts to the classpath and existing beans; embedded servers enable stand-alone executable applications; external configuration separates environment from code; and Actuator exposes operational information.** Spring Boot explicitly describes its goal as making stand-alone, production-grade 3 Spring applications that can “just run,” with minimal Spring configuration. 

This history is therefore a movement through roughly five architectural levels: 

|Era|Primary abstraction<br>introduced|Main problem attacked|New trade-off|
|---|---|---|---|
|Servlet|Container-managed<br>HTTP endpoint|Portable server-side Java<br>request handling and<br>lifecycle|Application owns<br>dispatching, parameter<br>handling, and much HTTP<br>plumbing.<br>4|
|JSP|Server-side view<br>template compiled to<br>a servlet|Generating HTML without<br>constructing all markup in<br>servlet Java code|Scriptlets and page logic can<br>still couple presentation and<br>application logic.<br>5|
|Struts / JSF|MVC front controller /<br>component UI<br>framework|Repeated navigation,<br>dispatching, forms,<br>validation, UI state/event<br>infrastructure|Framework configuration<br>and lifecycle complexity<br>increase.<br>6|
|Spring<br>Framework|IoC/DI container plus<br>cross-cutting<br>enterprise services<br>around POJOs|Tight infrastructure coupling,<br>EJB/JTA complexity, difficult<br>testing, duplicated data-<br>access/transaction code|Developers must<br>understand container<br>semantics, proxies, bean<br>lifecycle, and configuration.<br>7|
|Spring Boot|Opinionated<br>application assembly<br>and runtime<br>conventions|Dependency/configuration/<br>deployment repetition and<br>operational boilerplate|More behavior is implicit;<br>developers must understand<br>what auto-configuration<br>actually selected.<br>8|

The key architectural lesson is that **Spring Boot does not make Servlets obsolete** . In a conventional Spring MVC application, HTTP requests still enter a Servlet container; Spring MVC's <mark>`DispatcherServlet`</mark> is itself the front-controller Servlet. Spring Boot automates construction and configuration of that stack. Understanding Servlet concepts—requests, responses, filters, sessions, container threading, and lifecycle— therefore remains valuable when debugging a Boot/Spring MVC application. 9 

No particular Java version was specified in the request, so this report deliberately does **not** assume one. Java requirements must be checked against the selected Spring/Spring Boot release line. As an important migration example, Spring Boot 3.0, released November 24, 2022, raised the baseline to Java 17 and moved from Java EE <mark>`javax.*`</mark> APIs to Jakarta EE <mark>`jakarta.*` ;</mark> applications migrating from older Servlet/Spring generations may therefore face a source and dependency migration independent of the architectural migration itself. 10 

## **Historical evolution and the problems each generation solved** 

The history begins with a deceptively small abstraction: provide a portable Java object that a web container can instantiate and invoke when an HTTP request arrives. Almost every subsequent framework discussed here retains that foundation while moving application developers farther away from its repetitive mechanics. 

### **Timeline** 

|Date|Technology /<br>version|Historical significance and problem addressed|
|---|---|---|
|**May**<br>**1996**|Java Servlet<br>announced|Sun announced development of the server-side counterpart to the<br>applet, establishing the basic idea of Java code managed by a web<br>server rather than a process-per-request model. The Servlet 1.0<br>specification was finalized in the 1997 period.<br>11|
|**June**<br>**1997**|Servlet 1.0<br>generation|Established the container-managed Servlet programming model.<br>The fundamental lifecycle remains recognizable today: construction,<br>`init` ,repeated<br>`service` calls, then<br>`destroy` .<br>12|
|**1999**|Servlet 2.2 / early<br>JSP generation|Servlet 2.2 became part of the J2EE-era web platform and<br>standardized independently deployable web applications; JSP<br>emerged as a presentation-oriented layer ultimately compiled into<br>Servlets.<br>13|
|**2001**|Servlet 2.3 / JSP 1.2;<br>Struts 1.0|Servlet/JSP matured while Apache Struts 1.0, released June 15, 2001,<br>provided a reusable MVC framework instead of requiring each<br>application to invent its own dispatch/navigation architecture.<br>14|
|**Nov.**<br>**24,**<br>**2003**|Servlet 2.4 / JSP 2.0|Servlet and JSP continued standardizing the web tier; JSP 2.0<br>advanced the templating/tag/EL-oriented presentation model rather<br>than treating JSP merely as Java embedded in HTML.<br>15|
|**2002–**<br>**June**<br>**2003**|Spring's origins /<br>public project|Rod Johnson's 2002 book shipped the framework ideas; community<br>collaborators including Juergen Hoeller helped turn them into an<br>open-source project publicly available in June 2003.<br>16|
|**Mar.**<br>**11,**<br>**2004**|JSF 1.0 final|JSF standardized a server-side UI-component model including state,<br>events, validation, and navigation, directly addressing the absence<br>of a standard high-level GUI framework on top of Servlet/JSP.<br>17|
|**Mar.**<br>**24,**<br>**2004**|Spring Framework<br>1.0 final|Delivered a lightweight IoC container, AOP, portable transaction<br>management, JDBC/ORM integration, MVC, and other services<br>around POJOs.<br>18|
|**2006–**<br>**2007**<br>**era**|Java/annotation-<br>oriented Spring<br>configuration<br>expands|Spring demonstrated<br>`@Configuration` /<br>`@Bean` Java<br>configuration as an alternative to XML; Spring 2.5-era annotation-<br>driven DI added mechanisms such as<br>`@Autowired` ,while<br>stereotypes such as<br>`@Component` ,<br>`@Service` ,<br>`@Repository` ,<br>and<br>`@Controller` eventually became normal Spring style.<br>19|
|**Dec.**<br>**10,**<br>**2009**|Servlet 3.0|The Servlet platform reduced deployment-descriptor dependence<br>and modernized container integration; this generation is important<br>to later programmatic/annotation-based Java web bootstrapping.<br>20|

|Date|Technology /<br>version|Historical significance and problem addressed|
|---|---|---|
|**May**<br>**28,**<br>**2013**|Servlet 3.1|Continued modernization of the Servlet foundation immediately<br>before Spring Boot's emergence.<br>21|
|**Apr. 1,**<br>**2014**|Spring Boot 1.0 GA|Added an opinionated, stand-alone application model around Spring<br>and dramatically reduced routine setup and deployment friction.<br>22|
|**Mar. 1,**<br>**2018**|Spring Boot 2.0 GA|First major Boot revision after the 1.x generation; built on Spring<br>Framework 5.0.<br>23|
|**Nov.**<br>**24,**<br>**2022**|Spring Boot 3.0 GA|Moved to Spring Framework 6, Java 17 baseline, Jakarta EE APIs,<br>improved Micrometer-based observability, and first-class GraalVM/<br>native-image support.<br>24|
|**Nov.**<br>**20,**<br>**2025**|Spring Boot 4.0 GA|Began the Boot 4 generation on Spring Framework 7; Boot's<br>architecture was further modularized and continued evolving its<br>observability/runtime integration.<br>25|
|**2026**|Spring Boot 4.x / 4.1<br>generation|Spring's project site lists Boot 4.1.1 as the current project generation<br>at the time of this research; the important architectural fact is<br>continuity rather than a change of fundamentals: Boot still<br>composes Spring around starters, conditional auto-configuration,<br>executable applications, and production tooling.<br>26|

### **Servlets: standardizing server-side Java** 

A Servlet is fundamentally a Java component whose lifecycle is managed by a Servlet container. The container constructs it, invokes initialization, sends requests through <mark>`service` ,</mark> and eventually calls <mark>`destroy` .</mark> That contract was transformative because application code no longer had to own the entire server process or low-level connection lifecycle. 4 

A traditional HTTP Servlet nevertheless exposes a comparatively low-level programming model: 

```
publicclassCustomerServletextendsHttpServlet{
privateCustomerDaocustomerDao;
```

```
@Override
publicvoidinit(){
customerDao=newCustomerDao(/* locate/configure dependencies */);
}
@Override
protectedvoiddoGet(
HttpServletRequestrequest,
```

```
HttpServletResponseresponse)throwsIOException{
```

```
Stringid=request.getParameter("id");
Customercustomer=customerDao.findById(Long.parseLong(id));
response.setContentType("text/html");
response.getWriter()
.println("<h1>"+customer.getName()+"</h1>");
}
}
```

The Servlet API itself does not require this poor separation of concerns, but it also does not supply an application architecture for preventing it. The endpoint can easily accumulate HTTP parsing, validation, service lookup, transaction handling, persistence calls, error conversion, navigation, and HTML rendering. This is the central distinction between an **API for request processing** and a **framework for application structure** . The later frameworks primarily attacked this accidental complexity rather than replacing the Servlet transport contract. 27 

Deployment also historically meant producing a web application archive and installing it into a separately managed Servlet/application server. That model gave operations teams a standardized container boundary but coupled development and deployment workflows to container configuration, shared server resources, deployment descriptors, JNDI resources, and application-server conventions. Spring's later portable abstractions and Boot's executable application model progressively weakened those couplings. 28 

### **JSP: moving presentation out of servlet code** 

JavaServer Pages addressed a straightforward weakness of writing HTML from Servlet methods: presentation is more maintainable when the document looks primarily like markup rather than a series of <mark>`println`</mark> calls. JSP is a server-side template technology that is ultimately translated/compiled into a Servlet; it supports template text, expression mechanisms, tags, and—historically—embedded Java. 5 

This allowed an early form of separation: 

```
HTTP request
    |
Servlet / controller logic
    |
request attributes / JavaBeans
    |
JSP view
    |
HTML response
```

But early JSP applications frequently moved rather than eliminated coupling: Java _scriptlets_ could put database access and business logic directly inside a view. JSP's later tag-library and expression-oriented evolution attempted to reduce this problem. The JSP 2.0 proposal itself noted that reusable custom actions 

were powerful but required Java implementation and could become cumbersome to compose, illustrating the pressure for progressively higher-level view abstractions. 29 

### **Struts: MVC as reusable infrastructure** 

Apache Struts 1.0 was released on June 15, 2001. Its important contribution was not that MVC had been invented, but that Java web teams no longer had to create their own MVC request dispatcher for each application. Struts supplied a front-controller-oriented framework and common services designed to encourage maintainable MVC web applications. 30 

Conceptually: 

```
Browser
  |
  v
ActionServlet
  |
  +--> action mapping/configuration
          |
          v
       Action
          |
          v
        Model
          |
          v
      JSP / View
```

Compared with raw Servlet/JSP code, this centralization made URL-to-handler mappings, form processing, validation, and navigation more systematic. In classic Struts 1 applications, however, this architecture became strongly associated with framework-specific <mark>`Action`</mark> types and substantial XML configuration such as <mark>`struts-config.xml` .</mark> In other words, Struts reduced _application-level dispatching boilerplate_ while introducing its own _framework coupling and configuration surface_. The framework reached end of life in its 1.x form, making it a significant legacy migration source rather than a contemporary target architecture. 31 

### **JSF: abstracting the UI rather than only the controller** 

JavaServer Faces attacked a different problem. Its specification proposal explicitly observed that Servlet and JSP were powerful underlying technologies but did not provide a standard API for managing a server-side GUI's component state, events, validation, and related interaction. Developers were repeatedly building specialized infrastructure to associate requests with UI components and event handlers. JSF therefore standardized a server-side component-oriented framework with state management, events, validation, navigation, internationalization, and accessibility concerns. 32 

That abstraction came with a correspondingly richer request lifecycle. A JSF request is not simply “map URL to controller method”; processing a stateful component tree involves lifecycle phases that can restore a view, apply request values, validate and update state, invoke application logic, and render the result. That is useful for server-rendered component applications, but it also means that debugging a JSF application often requires understanding the JSF lifecycle rather than only HTTP. 33 

Struts and JSF therefore represent two distinct attempts to tame Servlet/JSP complexity: 

- **Struts** concentrated on action-oriented MVC and navigation. 

• **JSF** concentrated on a higher-level component/event UI model. 

Neither was primarily designed to solve the deeper enterprise-layer problem of how arbitrary business services acquire database connections, transaction managers, messaging resources, or security collaborators without directly constructing or locating them. That is where Spring's contribution was 34 qualitatively different. 

### **Spring Framework: inversion of control over infrastructure** 

Rod Johnson describes Spring's roots in his experience with J2EE projects beginning around 1999. His 2002 book's accompanying framework already included the conceptual ancestors of <mark>`BeanFactory` /</mark> <mark>`ApplicationContext` ,</mark> dependency injection, Spring MVC, <mark>`JdbcTemplate` ,</mark> and a technologyindependent data-access exception hierarchy. Readers including Juergen Hoeller helped turn that code into an open-source project in 2003. The name “Spring” consciously suggested a fresh start after what Johnson characterized as the “winter” of traditional J2EE. 35 

The architectural change is easiest to see in object creation. 

#### **Traditional tightly coupled service:** 

```
publicclassOrderService{
privatefinalOrderDaodao=newJdbcOrderDao();
}
```

#### **Dependency-injected service:** 

```
@Service
publicclassOrderService{
privatefinalOrderRepositoryrepository;
publicOrderService(OrderRepositoryrepository){
this.repository=repository;
}
}
```

The second object describes what it needs but does not decide how the dependency is instantiated. Spring's container owns the object graph. This inversion enables implementations to be substituted, test doubles to be passed into ordinary Java unit tests, infrastructure to be decorated with interceptors, and application services to remain comparatively independent of initialization code. Spring's current container continues to distinguish the basic <mark>`BeanFactory`</mark> abstraction from the richer <mark>`ApplicationContext` ,</mark> which is the normal application-level container. 36 

Spring's 1.0 release emphasized another major departure from contemporary enterprise Java: a POJO could receive **declarative transactions** without becoming an EJB or manually calling a transaction API, and the same programming model could work with local resource transactions or JTA. Spring's transaction abstraction was specifically intended to avoid requiring an application server solely to obtain declarative transaction semantics. 37 

### **Spring Boot: convention and conditional configuration over Spring** 

Spring solved _application architecture_, but a nontrivial Spring application could still involve extensive XML, library/version selection, web-container setup, and deployment assembly. Boot 1.0's 2014 emergence therefore addressed an ecosystem-level problem: the pieces worked, but developers repeatedly wired the same combinations together. 38 

Boot's essential mechanism is conditional auto-configuration. It inspects the application's classpath, existing beans, properties, and other conditions and configures conventional infrastructure only when appropriate. For example, the official documentation explains that if an embedded database such as HSQLDB is present and the application has not supplied its own database-connection bean, Boot can configure one automatically. The developer opts into this model with <mark>`@EnableAutoConfiguration`</mark> or, normally, <mark>`@SpringBootApplication` .</mark> 39 

That changes the default project shape from “declare every framework object” to “declare application intent and override convention where necessary”: 

```
@SpringBootApplication
publicclassApplication{
publicstaticvoidmain(String[]args){
SpringApplication.run(Application.class,args);
}
}
```

The reduction in visible code is therefore not because the web server, MVC dispatcher, JSON conversion, connection pool, transaction manager, or security filters ceased to exist. Boot's important contribution is that much of their **conventional assembly becomes derived configuration instead of handwritten** 40 **configuration** . 

## **Architecture and technical comparison** 

The progression can be visualized as an increasing number of concerns being delegated to reusable infrastructure. 

<!-- Start of picture text -->
Spring Boot assembly<br>layer<br>Starters + Dependency Embedded Web Server<br>Management<br>Auto-configurationConditional HTTP Client<br>External Configuration Actuator / Observability<br>configures<br>Spring MVC application Servlet / JSP application<br>Servlet Container Servlet Container<br>Filters / Spring Security Application Servlet<br>DispatcherServlet Business Logic JSP View<br>HandlerMapping View or HTTP MessageConverter InfrastructureJDBC / Other<br>Transaction + AOPInfrastructure Controller<br>intercepts<br>Injected Service<br>Repository / DAO<br><!-- End of picture text -->

Spring MVC continues to rely on a Servlet container but installs <mark>`DispatcherServlet`</mark> as a **front controller** . The dispatcher performs a shared request-processing algorithm and delegates specialized tasks to configurable components such as handler mappings, handler adapters, view resolvers, and exception resolvers. Boot then configures the surrounding Spring MVC infrastructure and web server according to dependencies and conditions. 41 

### **Request lifecycle comparison** 

|Architecture|Simplified request lifecycle|Consequence|
|---|---|---|
||Container→filter chain→mapped Servlet|Explicit and transparent, but the Servlet<br>often becomes the place where|
|Direct Servlet|→<br>`service` /<br>`doGet` /<br>`doPost` →<br>response|parsing, routing-adjacent logic,<br>business invocation, and errors meet.<br>42|

|Architecture|Simplified request lifecycle|Consequence|
|---|---|---|
|Struts 1|Container→Struts controller Servlet→<br>action mapping→<br>`Action` →model→<br>forward/JSP|Centralized dispatch and navigation<br>reduce duplicated Servlet controllers<br>but introduce framework-specific<br>action/configuration concepts.<br>43|
|JSF|Container→Faces processing lifecycle→<br>restore/process component tree→<br>validation/model update/action→render|High-level server UI semantics, but<br>state and lifecycle become substantially<br>richer than plain HTTP dispatch.<br>44|
||Container→filters→|Central dispatch remains, but|
|Spring MVC|`DispatcherServlet` →handler<br>mapping/adapter→controller→service<br>→view/message converter|controllers can be thin POJOs with<br>injected services and rich binding/<br>validation/exception infrastructure.<br>45|
|Spring Boot<br>+ MVC|Same Spring MVC path, with Boot<br>constructing/configuring much of the<br>runtime|Operational and setup differences are<br>large; the fundamental MVC request<br>semantics are Spring MVC's rather than<br>a separate “Boot MVC.”<br>46|

### **Cross-cutting architecture comparison** 

|Concern|Servlet/JSP<br>alone|Struts / JSF|Spring Framework / MVC|Spring Boot|
|---|---|---|---|---|
|**Dependency**<br>**management**|Manual<br>construction,<br>factories,<br>JNDI, or<br>custom<br>infrastructure|Framework<br>objects<br>managed to<br>varying<br>degrees;<br>application<br>services<br>often need<br>additional<br>infrastructure|IoC container manages application<br>object graph through constructor/<br>setter/other injection.<br>47|Same Spring DI;<br>starters additionally<br>coordinate library<br>dependencies.<br>48|
|**Inversion of**<br>**control**|Container<br>controls<br>Servlet<br>lifecycle, but<br>usually not<br>arbitrary<br>domain/<br>service<br>objects|Framework<br>controls<br>actions/<br>components|Spring container controls general-<br>purpose application components|Same, with Boot also<br>controlling<br>conventional<br>_configuration_<br>_selection_.<br>39|

|Concern|Servlet/JSP<br>alone|Struts / JSF|Spring Framework / MVC|Spring Boot|
|---|---|---|---|---|
|**AOP**|Custom<br>filters/<br>proxies/<br>interceptors|Framework-<br>specific<br>interceptors/<br>hooks|Spring AOP creates runtime<br>proxies using JDK proxies or CGLIB<br>and applies advice at matching<br>join points.<br>49|Same Spring AOP;<br>Boot can configure<br>related infrastructure<br>when starters/<br>dependencies<br>require it.|
|**MVC**|Application<br>must<br>establish<br>conventions<br>itself|Struts<br>supplies<br>action MVC;<br>JSF supplies<br>component-<br>oriented<br>MVC/UI<br>framework|`DispatcherServlet` provides<br>front-controller MVC|Boot auto-configures<br>Spring MVC defaults<br>around the same<br>dispatcher.<br>41|
|**Transactions**|JDBC/JTA calls<br>or container-<br>specific<br>mechanisms|Commonly<br>delegated to<br>EJB/JTA or<br>integrated<br>libraries|Uniform<br>`PlatformTransactionManager`<br>model; declarative transactions<br>implemented using AOP proxies/<br>interceptors.<br>50|Boot detects data<br>technology and<br>commonly<br>configures the<br>relevant transaction<br>infrastructure.|
|**Data access**|Direct JDBC<br>plus manual<br>connection/<br>statement/<br>result/error<br>cleanup|Application-<br>specific DAO<br>layer|`JdbcTemplate` ,ORM/JPA<br>integration, uniform exception<br>hierarchy; Spring Data adds<br>repository abstraction.<br>51|Starters and auto-<br>configuration<br>assemble<br>datasource/JPA/<br>repository<br>infrastructure from<br>dependencies and<br>properties.|
|**Security**|Servlet-<br>container<br>security or<br>custom filters|Framework/<br>application-<br>specific<br>integrations|Spring Security supplies filter-<br>chain-based authentication and<br>authorization infrastructure|Security starter plus<br>Boot configuration;<br>application still<br>needs explicit<br>authorization policy.<br>52|
|**Configuration**|`web.xml` ,<br>server/JNDI<br>config, Java<br>code|Heavy use of<br>XML/config<br>files plus<br>annotations<br>in later<br>generations|Originally strongly XML-oriented;<br>later annotation scanning and Java<br>`@Configuration` /<br>`@Bean`|Java/annotations +<br>external properties +<br>conditional auto-<br>configuration;<br>explicit beans<br>override<br>conventions.<br>53|

|Concern|Servlet/JSP<br>alone|Struts / JSF|Spring Framework / MVC|Spring Boot|
|---|---|---|---|---|
|**Testing**|Often<br>requires<br>substantial<br>mocks or<br>deployment<br>when code<br>depends<br>directly on<br>Servlet/<br>container<br>APIs|Framework<br>test<br>harnesses<br>required for<br>tightly<br>coupled<br>components|POJO services can be unit-tested<br>independently;<br>`spring-test`<br>supports context/web integration<br>testing|`spring-boot-`<br>`starter-test` ,<br>`@SpringBootTest` ,<br>focused test slices,<br>MockMvc,<br>Testcontainers<br>integration.<br>54|
|**Deployment**|Usually WAR<br>→external<br>container|Usually WAR<br>→external<br>container|Can use traditional container<br>deployment|Stand-alone “just<br>run” model is a<br>primary design goal;<br>WAR-style<br>interoperability<br>remains relevant for<br>migration scenarios.<br>26|
|**Operations**|Usually<br>bespoke/<br>JMX/server<br>tooling|Mostly<br>container/<br>framework<br>tooling|Framework exposes infrastructure<br>but does not itself provide Boot's<br>operational surface|Actuator provides<br>built-in application<br>endpoints including<br>health and metrics-<br>related facilities.<br>55|

### **IoC and DI: the architectural boundary that mattered most** 

It is important to distinguish two kinds of inversion of control. A Servlet already experiences IoC: the Servlet does not call the container and ask for requests; the container calls the Servlet. Spring generalized that principle from HTTP endpoints to **the entire application object graph** . 56 

Constructor injection is generally the clearest expression: 

```
@Service
publicclassPaymentService{
privatefinalPaymentGatewaygateway;
privatefinalAuditRepositoryauditRepository;
publicPaymentService(
PaymentGatewaygateway,
AuditRepositoryauditRepository){
this.gateway=gateway;
```

```
this.auditRepository=auditRepository;
```

```
}
}
```

Dependencies are explicit in the type's constructor, and a unit test can create the service without starting Spring: 

```
PaymentServiceservice=
newPaymentService(fakeGateway,fakeAuditRepository);
```

This matters more architecturally than whether the bean definition was written in XML, Java, or discovered by annotations. **DI is the concept; XML, annotations, and Java configuration are merely different metadata mechanisms for constructing the graph.** Spring's current component model provides stereotypes including <mark>`@Component` ,</mark> <mark>`@Service` ,</mark> <mark>`@Repository` ,</mark> and <mark>`@Controller` ;</mark> current constructor injection also does not require <mark>`@Autowired`</mark> when a bean has a single constructor. 57 

### **AOP and declarative transactions** 

Spring AOP addresses cross-cutting behavior—transactions, security checks, caching, tracing, and similar concerns—that would otherwise become repetitive calls embedded throughout business methods. Spring's proxy-based AOP uses JDK dynamic proxies or CGLIB-class proxies. 49 

Declarative transaction management is a canonical example: 

```
@Transactional
publicvoidplaceOrder(Orderorder){
inventory.reserve(order);
orders.save(order);
payments.authorize(order);
}
```

Conceptually the call becomes: 

```
caller
   |
Spring proxy
   |-- begin transaction
   |
target method
   |
Spring proxy
   |-- commit / rollback
```

Spring's transaction abstraction deliberately hides whether the underlying mechanism is JDBC, JPA/ Hibernate, JTA, or another supported transaction resource, allowing transaction policy to remain more stable than the data-access implementation. 58 

This abstraction is powerful but not magical. Because common declarative transactions are proxy/ interceptor based, developers need to understand proxy boundaries. Transaction semantics also include propagation, isolation, read-only hints, timeout and rollback policy; Spring's default declarative rollback behavior ordinarily rolls back on unchecked <mark>`RuntimeException`</mark> and <mark>`Error` ,</mark> not every checked exception. Imperative transaction context is also thread-bound, so spawning work onto another thread does not automatically carry the transaction with it. 59 

### **Data access: from JDBC mechanics to repositories** 

Direct JDBC gives maximum SQL visibility but creates repetitive infrastructure work: connection/statement creation, resource cleanup, iteration over results, and exception translation. <mark>`JdbcTemplate`</mark> centralizes much of that lifecycle while allowing developers to retain explicit SQL. 60 

Spring ORM integration then allows JPA/Hibernate to participate naturally in the same Spring transaction infrastructure. Spring Data JPA goes another abstraction level higher: its stated purpose is to reduce persistence-layer boilerplate by allowing developers to define repository interfaces from which implementations and common query behavior can be generated. 61 

These layers should not be confused: 

```
Application
    |
Spring Data Repository          optional
    |
JPA API                         specification
    |
JPA provider (e.g. Hibernate)   implementation
    |
JDBC                            database API
    |
Database
```

A mature Spring developer should therefore understand the SQL and transaction behavior beneath the repository abstraction. Repository convenience does not eliminate query planning, indexes, lock contention, persistence-context behavior, N+1 queries, or connection-pool limits. 

### **Security: from container rules to an application security chain** 

For Servlet applications, Spring Security integrates primarily through the Servlet filter architecture. <mark>`FilterChainProxy`</mark> delegates to one or more <mark>`SecurityFilterChain`</mark> definitions and acts as the central entry point for Spring Security's Servlet support; the authentication model includes 

<mark>`SecurityContextHolder` ,</mark> <mark>`AuthenticationManager` ,</mark> providers, authorities, and related components. 52 

The resulting request path is approximately: 

```
HTTP request
   |
Servlet container
   |
DelegatingFilterProxy
   |
FilterChainProxy
   |
SecurityFilterChain
   |   authentication
   |   authorization
   |   CSRF / headers / other controls
   v
DispatcherServlet
   |
Controller
```

This is another example of evolution by layering rather than replacement: Spring Security builds on Servlet filters; Spring MVC builds on a Servlet; Spring Boot configures the environment in which all of them run. 62 

## **Spring's module model and the evolution of configuration** 

“Spring” is frequently used as though it were a single library. Architecturally, it is more useful to separate **Spring Framework** , portfolio projects such as **Spring Security** and **Spring Data** , and **Spring Boot** , which integrates and configures them. 

### **Core Spring responsibilities** 

|Area|Typical modules/<br>project|Responsibility|
|---|---|---|
||`spring-core` ,|Resource utilities, bean definitions, dependency injection,|
|**Core**|`spring-beans` ,|bean lifecycle, application context, events, component|
|**container**|`spring-context` ,|discovery, expression facilities.<br>`ApplicationContext` is|
||expression support|the richer superset used by normal applications.<br>36|
|**AOP**|Spring AOP / aspects<br>integration|Runtime proxy-based cross-cutting behavior, pointcuts and<br>advice; infrastructure underpinning features such as<br>declarative transactions.<br>63|

|Area|Typical modules/<br>project|Responsibility|
|---|---|---|
|**Transactions**|Spring transaction<br>infrastructure|Consistent programmatic and declarative transaction<br>model across local JDBC, JPA/Hibernate, JTA, and other<br>managers.<br>58|
|**JDBC**|`spring-jdbc`|`JdbcTemplate` ,resource management, SQL execution<br>support, and exception translation.<br>60|
|**ORM**|Spring ORM<br>integrations|Integrates ORM/JPA technologies with Spring resource and<br>transaction management.<br>64|
|**Web**<br>**foundation**|Spring Web|HTTP/web infrastructure and shared web facilities.|
|**Spring MVC**|`spring-webmvc`|Servlet-based front-controller MVC built around<br>`DispatcherServlet` .<br>45|
|**Testing**|`spring-test`|Application-context testing and web-test facilities that<br>allow integration testing without conventional application<br>deployment.<br>65|
|**Spring Data**|Separate Spring<br>portfolio project|Higher-level repository/data-access abstractions; Spring<br>Data JPA reduces JPA repository implementation<br>boilerplate.<br>66|
|**Spring**<br>**Security**|Separate Spring<br>portfolio project|Authentication, authorization and web-security<br>infrastructure, including Servlet<br>`SecurityFilterChain` .<br>52|
|**Spring Boot**|Separate Spring project|Opinionated dependency assembly, auto-configuration,<br>executable application model, externalized configuration,<br>testing integration and production tooling.<br>67|

That distinction is useful during troubleshooting. A failure in <mark>`@Transactional`</mark> semantics is usually a Spring Framework/AOP/transaction question; an unexpected generated query may be a Spring Data/JPA/ provider question; an authentication filter is a Spring Security concern; and an unexpected bean automatically appearing is often a Spring Boot auto-configuration question. 

### **Configuration evolved through several styles** 

The commonly presented story—“XML was replaced by annotations, which were replaced by Boot”—is too simplistic. These mechanisms solve different problems and can coexist. 

|Configuration<br>style|Example|Strength|Weakness|
|---|---|---|---|
|**Deployment**<br>**descriptor**|`web.xml`|Explicit<br>standardized<br>container<br>mappings|Verbose; describes web-<br>container wiring rather<br>than a general<br>application object<br>model.|
|**Spring XML**|`<bean id="..."`<br>`class="...">`|Centralized, explicit<br>wiring; application<br>classes need no<br>Spring annotations|Large applications can<br>produce substantial<br>XML; rename/<br>refactoring errors are<br>less naturally compiler-<br>visible. Spring's own<br>Java-config work<br>explicitly cited<br>refactoring/type<br>benefits.<br>68|
|**Annotation/**<br>**component**<br>**scan**|`@Service` ,<br>`@Repository` ,<br>`@Controller` ,injection<br>annotations|Wiring metadata<br>stays close to<br>component; greatly<br>reduces bean-<br>definition<br>repetition|Dependencies can<br>become implicit if<br>scanning boundaries<br>are poorly understood;<br>excessive annotation-<br>driven magic can<br>obscure architecture.<br>69|
|**Java**<br>**configuration**|`@Configuration` ,<br>`@Bean`|Explicit, type-safe<br>factory code; ideal<br>for third-party<br>objects and<br>conditional logic|Can become a large<br>hand-maintained<br>assembly layer if every<br>infrastructure bean is<br>manually declared.<br>68|
|**Boot auto-**<br>**configuration**|`@SpringBootApplication` +<br>classpath/properties|Eliminates<br>repeated<br>conventional<br>configuration;<br>backs off when<br>application<br>configuration<br>supplies<br>alternatives|Configuration is<br>partially implicit and<br>conditional, so<br>developers must learn<br>condition evaluation<br>and bean replacement.<br>39|

|Configuration<br>style|Example|Strength|Weakness|
|---|---|---|---|
||||Property precedence|
|**External**<br>**configuration**|`application.properties` /<br>YAML / environment<br>configuration|Separates runtime/<br>environment<br>choices from<br>compiled code|and profile/environment<br>differences can create<br>difficult-to-reproduce<br>behavior if|
||||uncontrolled.|

The most important distinction is: 

#### **Auto-configuration is not “no configuration.” It is configuration inferred from application intent and runtime conditions.** 

A database starter, driver, configuration properties, classpath and absence/presence of user-defined beans collectively become input to the configuration algorithm. Good Boot developers therefore know how to inspect and override that algorithm instead of treating it as unexplained magic. 39 

### **Why starters mattered** 

A starter is a curated dependency descriptor rather than a library containing all of the implementation itself. Boot's documentation describes starters as convenient dependency descriptors that provide a one-stop set of dependencies with managed transitive versions. <mark>`spring-boot-starter-data-jpa` ,</mark> for example, communicates architectural intent and lets Boot manage a coherent dependency set. 48 

This solves two previously independent problems: 

1. **dependency discovery** — “Which artifacts do I need for Spring MVC/JPA/security?” 

2. **dependency compatibility** — “Which versions of those artifacts were tested to work together?” 

That is one reason Boot's value is greater than simply bundling an embedded Tomcat server. 

### **From external container to executable application** 

Classic Java web delivery treated the application and server as separately assembled artifacts: 

```
application.war
      |
      v
preinstalled Tomcat / application server
      |
server XML / JNDI / shared libraries
```

Boot's stand-alone model reverses the ownership relationship conceptually: 

```
application
   |
   +-- Spring configuration
   +-- dependencies
   +-- embedded web server
   +-- configuration conventions
   |
executable application
```

This makes the runtime substantially more reproducible: the application build captures more of the webserver dependency choice rather than assuming an independently configured server installation. It does **not** eliminate environmental configuration—database endpoints, credentials, certificates, memory limits, proxies and observability backends still belong outside the binary—but it narrows the gap between what developers test and what production runs. Boot's official project description explicitly emphasizes standalone applications and production readiness. 26 

## **Essential Spring Boot knowledge for developers** 

Being productive with Spring Boot requires much more than remembering annotations. The core competency is being able to reason about what occurs **under** those annotations. 

### **Dependency injection and Spring Core** 

A developer should understand bean discovery, bean creation, constructor injection, bean scopes, lifecycle, <mark>`ApplicationContext` ,</mark> configuration classes and the difference between an ordinary Java object and a Spring-managed bean. <mark>`@Component` ,</mark> <mark>`@Service` ,</mark> <mark>`@Repository` ,</mark> and <mark>`@Controller`</mark> are specialized component stereotypes, and <mark>`@Repository`</mark> has additional significance for persistence exception translation. 69 

Prefer dependencies that are explicit in constructors. A class requiring twelve collaborators is not merely an injection inconvenience; it is often an architectural signal that the class has accumulated too many responsibilities. 

Developers should also recognize that not every object should be container-managed. Value objects, domain entities, request DTOs and short-lived algorithmic objects generally do not gain value merely by becoming Spring beans. 

### **Spring MVC** 

For the Servlet stack, developers should be able to trace: 

```
request
→ Servlet filters
→ DispatcherServlet
```

```
→ HandlerMapping / HandlerAdapter
```

- `→ controller` 

- `→ service` 

- `→ response body converter or view` 

- `→ response` 

The official MVC documentation identifies <mark>`DispatcherServlet`</mark> as Spring MVC's front controller and documents the delegation strategy used for mappings, exception handling and view resolution. 45 

Practical competency includes request mappings, path/query/header parameters, request-body deserialization, validation, HTTP status semantics, exception handling, content negotiation, filters versus MVC interceptors, synchronous request/thread implications, multipart handling, sessions and cookies. A developer who knows only <mark>`@RestController`</mark> and <mark>`@GetMapping`</mark> but cannot locate a failure in the filter/ dispatcher/controller chain does not yet understand the stack. 

### **Persistence, Spring Data and transactions** 

Spring Data JPA is extremely productive because repository implementations, pagination, query derivation and other routine data-layer mechanics can be generated from interfaces. Its own project documentation explicitly frames reduction of repository boilerplate as its purpose. 66 

But developers still need to understand: 

- where a transaction begins and ends; 

- entity state and persistence-context scope; 

- 

- lazy versus eager access; 

- 

- SQL actually generated by ORM operations; 

- 

- N+1 query patterns; 

- 

- indexes and query plans; 

- 

- connection-pool exhaustion; 

- 

- isolation and locking; 

- 

- rollback rules and transaction propagation. 

- 

Spring's <mark>`@Transactional`</mark> is AOP infrastructure rather than an imperative keyword in the Java language. Its implementation commonly involves an AOP proxy, <mark>`TransactionInterceptor` ,</mark> and a transaction manager. Default unchecked-exception rollback and thread-bound imperative transaction semantics are especially important production details. 70 

For SQL-heavy or performance-sensitive workloads, <mark>`JdbcTemplate`</mark> remains a legitimate Spring abstraction rather than a historical stepping stone that every project must abandon. It removes JDBC resource-management boilerplate without hiding SQL. 60 

### **Spring Security** 

A Spring MVC developer should be able to reason about the security filter chain before worrying about controller annotations. <mark>`FilterChainProxy`</mark> and <mark>`SecurityFilterChain`</mark> determine which security filters process a Servlet request, while the authentication architecture centers on the security context, authentication objects, authentication managers/providers and granted authorities. 52 

Essential knowledge includes the distinction between **authentication** and **authorization** , session versus bearer-token authentication, password hashing, CSRF, CORS, security headers, method-level authorization, OAuth2/OIDC concepts where relevant, and secure error behavior. 

A particularly dangerous Boot misconception is that adding a security starter means “security is solved.” The framework supplies mechanisms and secure defaults in several areas; the application must still define who is permitted to perform which business operations. 

### **Starters, Boot auto-configuration and overrides** 

A Boot developer should know how to answer: 

Why does this bean exist? 

That generally means tracing starter dependencies, auto-configuration conditions, user-provided beans and application properties. Boot auto-configuration is explicitly classpath- and condition-sensitive and is 39 intended to back away when application-defined configuration takes control. 

Blindly copying a configuration bean from an old Stack Overflow answer can therefore do more harm than good: manually declaring an object may disable a newer Boot auto-configuration branch that would otherwise configure more complete infrastructure. 

### **Actuator, monitoring and observability** 

Spring Boot Actuator exposes endpoints through which an application can be monitored and interacted with. Built-in endpoints include <mark>`health` ;</mark> endpoints can be selectively enabled/exposed over mechanisms including HTTP and JMX, and HTTP Actuator endpoints normally use the <mark>`/actuator`</mark> prefix. 55 

Production monitoring should normally cover at least: 

```
HTTP
  request rate
  latency distribution
  error rate
JVM
  heap / non-heap
  garbage collection
  threads
  CPU
Infrastructure
  connection pools
  queue depth
  downstream latency/errors
```

```
Application
```

```
  health/readiness
  domain-specific metrics
```

```
Tracing / logs
```

```
  request correlation
  distributed trace context
  structured diagnostic events
```

Boot 3 strengthened the observability model around Micrometer and Micrometer Tracing, and the Boot 4 generation continues that direction, including deeper OpenTelemetry interoperability. 71 

Actuator exposure itself is a security boundary. Operational endpoints should be exposed deliberately rather than indiscriminately because they can reveal health, configuration or runtime details. The Actuator documentation explicitly distinguishes endpoint availability and remote exposure. 55 

### **Testing strategy** 

Spring's greatest testing advantage comes from _architecture_, not from <mark>`@SpringBootTest` :</mark> when services receive collaborators through constructors and do not depend on container APIs, ordinary fast unit tests can instantiate them directly. 

Use progressively heavier tests only where the boundary requires them: 

|Test level|Typical mechanism|Best use|
|---|---|---|
|Plain unit test|JUnit + direct object construction/<br>mocks/fakes|Business rules, transformations, service<br>orchestration|
|MVC slice|`@WebMvcTest` ,MockMvc-<br>oriented support|Routing, validation, serialization,<br>controller/security behavior|
|Persistence slice|`@DataJpaTest` or equivalent<br>focused support|Mappings, repository queries,<br>persistence semantics|
|Spring integration|Spring Test / application context|Bean wiring, transaction/configuration<br>behavior|
|Boot integration|`@SpringBootTest`|Full application-context behavior and<br>major integration paths|
|Real infrastructure<br>integration|Testcontainers + Spring/Boot tests|Actual database/broker/network-driver<br>semantics|

Boot supplies dedicated testing modules and a starter commonly bringing JUnit Jupiter, AssertJ, Hamcrest and Spring testing support; its current testing model also provides focused slices such as MVC and data tests. Testcontainers can be used with ordinary JUnit or <mark>`@SpringBootTest` .</mark> 72 

A common performance mistake in test suites is to replace every unit or slice test with <mark>`@SpringBootTest` .</mark> The latter loads an application context and is appropriate when that integration is actually what the test intends to verify. Boot's documentation notes that even a default <mark>`@SpringBootTest`</mark> does not necessarily start a real network server; MVC can be tested through a mock environment and <mark>`MockMvc` .</mark> 73 

### **Packaging and deployment** 

Developers should understand both major deployment shapes: 

#### **Executable application** 

```
java -jar application.jar
        |
        +-- Spring Boot
        +-- embedded server
        +-- application
```

#### **Container-oriented migration/deployment** 

```
application.war
        |
external compatible servlet container
```

The first is the architectural norm associated with Boot's stand-alone model. The second can remain useful when organizational constraints or an incremental legacy migration require external-container deployment. 26 Boot's overall objective remains stand-alone production-grade applications with minimal configuration. 

Modern deployment also requires distinguishing **build artifact** , **container image** , and **runtime configuration** . Do not bake passwords, per-environment database URLs or private keys into a JAR merely because the JAR is executable. 

### **Performance: what developers should actually measure** 

Spring Boot itself is rarely the only meaningful performance variable. End-to-end latency may be dominated by database queries, remote calls, serialization, locks, connection-pool waiting, thread saturation, GC, cache behavior or logging. 

Useful investigations therefore proceed from metrics/traces/profiles toward a hypothesis rather than from folklore toward a configuration flag. 

Particularly common Spring/JPA problems include: 

|Pitfall|Why it hurts|
|---|---|
|N+1 ORM queries|One logical request unexpectedly issues many database round<br>trips.|
|Transactions wider than needed|Locks/resources are held while unrelated computation or<br>remote I/O runs.|
|undersized/oversized connection<br>pools|Requests either queue unnecessarily or overwhelm the<br>database.|
|Blocking external calls on request<br>threads|Throughput becomes dependent on downstream latency and<br>thread availability.|
|Unbounded caches/collections|Heap growth ultimately creates GC pressure or failure.|
|Excessive eager bean work|Startup and memory costs rise, especially for large contexts.|
|Excessive metrics label cardinality|Monitoring infrastructure can become expensive or unstable.|
|Logging request bodies<br>indiscriminately|CPU/I/O cost plus security/privacy leakage.|

The operational implication of Boot is not “performance is automatically handled”; rather, Actuator and the Micrometer-centered observability model make the application easier to measure and integrate with production monitoring. 74 

### **Common Spring pitfalls worth memorizing** 

Three subtle categories matter particularly often. 

**Proxy-bound behavior.** Spring AOP is proxy-based, so developers must understand whether a call actually passes through the proxy when relying on advice such as transactions. 63 

**Transaction assumptions.** Default rollback rules do not mean “every exception always rolls back,” and imperative transaction context does not automatically jump to a newly spawned thread. 70 

**Abstraction leakage.** Spring Data does not make SQL irrelevant, Spring MVC does not make HTTP irrelevant, Spring Security does not make Servlet filters irrelevant, and Boot does not make Spring configuration irrelevant. The abstractions work best when developers understand the layer beneath them. 75 

## **Migration from legacy Servlet/JSP applications to Spring Boot** 

A successful migration should treat legacy behavior as a system to be **characterized and decomposed** , not merely translate <mark>`doGet()`</mark> into <mark>`@GetMapping` .</mark> 

<!-- Start of picture text -->
Inventory legacyapplication<br>Characterization /regression tests<br>Target Boot linedependencies?with JDK andcompatible<br>No<br>Yes<br>Upgrade JDK / libraries /container APIs first application shellIntroduce Boot<br>Map infrastructure<br>Servlets -> Controllers SecurityFilterChainFilters / auth -> JDBC / DAOs -> SpringJDBC or Data JTA/manual tx -> Springtransaction boundaries JNDI/config -> externalconfiguration temporarily or migrateJSP strategy -> retainviews/API<br>Migrate one verticalbusiness slice<br>Run old/new behavior inregression suite No<br>Equivalent?<br>Yes<br>Migrate next slice<br>framework/containerRemove legacycoupling<br>health, security hardeningAdd Actuator, metrics,<br>Deploy, observe, tune<br><!-- End of picture text -->

### **Start with an inventory, not a rewrite** 

Before changing framework code, inventory: 

- every Servlet and URL mapping; 

- filters and their order; 

- 

- listeners; 

- 

- JSPs, tag libraries and include relationships; 

- Struts actions/configuration or JSF views/managed state; 

- 

- session attributes and assumptions about session affinity; 

- 

- authentication and authorization mechanisms; 

- 

- JNDI datasources, mail sessions or other server-bound resources; 

- JDBC/ORM libraries and explicit transaction code; 

- scheduled/background work; 

- upload/download behavior; 

- 

- exception mappings and error pages; 

- character encodings; 

- 

- properties scattered through files, JVM options and server configuration; 

- 

- external integrations and file-system assumptions. 

- 

This inventory is necessary because the visible Servlet code frequently represents only a fraction of the effective application behavior; filters, container resources, deployment descriptors and server configuration may participate in each request. 

### **Freeze behavior with characterization tests** 

Legacy migration is safer when existing HTTP behavior becomes executable specification before the implementation is changed. Capture status codes, redirects, headers, cookies, authentication rules, form validation, response bodies and key database side effects. 

Do not require every historical bug to become permanent. The important point is to distinguish **intentional fixes** from **accidental migration regressions** . 

Spring's integration-testing support is explicitly designed to allow application-context integration testing without traditional deployment, while Boot adds application and slice testing facilities. 76 

### **Choose an incremental boundary** 

Because Spring MVC's Servlet stack still runs through <mark>`DispatcherServlet` ,</mark> an incremental migration is often possible. Existing filter/Servlet concepts and Spring MVC can conceptually coexist while routes are moved toward controllers and injected services. 9 

A practical vertical slice is: 

- `one URL + validation + business service + database operation + authorization + response/view` 

Migrating one such slice validates the complete architecture much earlier than converting hundreds of DAOs or JSPs in isolation. 

### **Separate HTTP from business logic first** 

A legacy Servlet like: 

```
protectedvoiddoPost(...){
// parse HTTP
// validate
// query database
// calculate business result
// commit transaction
// choose JSP
}
```

should not become a Spring controller containing the same five concerns: 

```
@PostMapping(...)
publicStringsubmit(...){
// same monolithic logic, now with annotations
}
```

A better migration creates explicit layers: 

```
Controller
   |
Application/service boundary
   |
Domain/business logic
   |
Repository / integration adapters
```

The controller owns HTTP concerns; the service owns the use case and transaction boundary; repositories/ adapters own persistence and integration details. DI then makes the boundaries replaceable and testable. This is the architectural benefit that matters—not the number of annotations. 

### **Map old infrastructure to new infrastructure deliberately** 

|Legacy pattern|Typical Spring Boot destination|Migration concern|
|---|---|---|
|`HttpServlet`<br>controller|`@Controller` /<br>`@RestController`|Preserve URLs, method semantics,<br>encoding, status codes and redirects.<br>Spring MVC's dispatcher becomes the<br>application front controller.<br>45|
|`web.xml`|MVC mappings / Java<br>confiuration / Boot|Inventory filters/listeners/error behavior|
|mappings|ig<br>conventions|before deleting the descriptor.|
|Service locator / JNDI<br>lookup|Constructor-injected Spring<br>bean|Remove service-location code from<br>business classes.|
|JNDI datasource|Boot-configured datasource or<br>explicit bean|Validate pool properties, credentials and<br>transaction behavior.|
|Manual JDBC<br>boilerplate|`JdbcTemplate` ,JPA or Spring<br>Data|Do not automatically convert SQL that<br>benefits from remaining explicit.<br>`JdbcTemplate` exists specifically to<br>handle repetitive JDBC resource mechanics.<br>60|
|Manual<br>`commit` /<br>JTA calls|`@Transactional` around<br>service use cases|Re-evaluate propagation and rollback<br>semantics rather than mechanically<br>wrapping every DAO method.<br>77|

|Legacy pattern|Typical Spring Boot destination|Migration concern|
|---|---|---|
|Custom auth Servlet<br>filter / container<br>realm|Spring Security<br>`SecurityFilterChain`|Reproduce authentication_and authorization_<br>rules; verify ordering and endpoint<br>coverage.<br>78|
|Struts<br>`Action`|MVC controller + service|Move framework-specific action logic<br>toward plain service objects before deleting<br>Struts configuration.|
|JSF backing/<br>component logic|Depends on target UI strategy|Decide explicitly whether server-side<br>component UI remains a requirement or<br>whether the target becomes Spring MVC<br>views/REST endpoints.|
|JSP business<br>scriptlets|Service/controller/view-model<br>separation|Move logic out before attempting template<br>replacement.|
|Server-local config|External Boot configuration|Preserve environment separation while<br>reducing application-server coupling.|
|Server monitoring<br>scripts only|Actuator + platform monitoring|Add explicit health and metrics expectations<br>before cutover.<br>55|

### **Treat** **<mark>`javax`</mark> →** **<mark>`jakarta`</mark> as a migration project of its own** 

A particularly important boundary appears when an old application moves to the Spring Boot 3+ generation. Boot 3 migrated Java EE APIs to their Jakarta EE equivalents. A type such as: 

```
javax.servlet.Filter
```

becomes: 

```
jakarta.servlet.Filter
```

This is not merely a search-and-replace exercise because third-party libraries that implement or expose those APIs must also be compatible with the Jakarta generation. Spring's Boot 3 milestone guidance explicitly warned that applications needed to replace <mark>`javax`</mark> imports with Jakarta variants and that thirdparty compatibility mattered. 79 

This is why the request's unspecified Java version matters. A migration plan should first select a **target Spring Boot release line** , then derive from it the required Java baseline, Servlet/Jakarta generation, supported ORM/library versions and container compatibility. Boot 3.0, for example, required Java 17 and Jakarta APIs; choosing it implicitly makes those migration requirements part of the project. 80 

### **Handle JSP separately from the backend migration** 

Do not make “Servlet/JSP to Boot” synonymous with “rewrite every user interface at the same time.” Those are separable changes. 

A lower-risk sequence can be: 

```
legacy JSP + legacy backend
        ↓
legacy JSP + Spring services
        ↓
Spring MVC controller + existing/preserved view
        ↓
optional new template/UI/API architecture
```

The main goal is first to extract application logic out of JSPs, Servlet controllers and framework-specific actions. Once the service/use-case layer is independent, replacing the presentation technology is much less risky. 

### **Preserve URL, session and security semantics** 

Framework migrations frequently fail not because the business calculation changed but because edge semantics did: trailing slashes, encoded paths, form encoding, cookies, session timeouts, CSRF behavior, upload limits, exception status codes, redirect destinations or proxy headers. 

Security deserves explicit regression testing. Spring Security's Servlet implementation introduces its own filter-chain architecture; moving an old authentication filter into Spring Security changes the location where authentication context and authorization decisions are managed. 52 

### **Deployment migration is a separate axis** 

A team can modernize architecture before changing operations: 

```
Phase A:
Spring Boot application
        ↓
WAR in organization-managed container
```

```
Phase B:
same application
        ↓
stand-alone executable/containerized deployment
```

Where organizational constraints permit it, the second model captures more runtime dependencies in the application build and aligns directly with Boot's stand-alone design objective. 26 

The key is not to change source architecture, runtime platform, database, UI, authentication system and network topology simultaneously unless there is a compelling reason. Every independent migration dimension multiplies the regression space. 

### **Know when** **_not_ to translate one-for-one** 

A legacy application's architecture often represents constraints that no longer apply. Examples include a singleton “DAO manager” written because there was no DI container, manual transaction helpers created to hide JDBC commits, huge front-controller Servlets written before MVC frameworks, or server-specific JNDI locators used because application configuration could not travel with the artifact. 

Those classes should usually disappear rather than receive <mark>`@Component`</mark> annotations. 

Conversely, established SQL, domain algorithms and well-designed POJO services may need almost no conceptual rewrite. The best migration conserves proven domain behavior while replacing obsolete infrastructure boundaries. 

## **Developer checklist and architectural trade-offs** 

### **Concise developer checklist** 

|Area|A Spring Boot developer should be able to answer|
|---|---|
|**Servlet**<br>**foundation**|What are a Servlet container, request, response, filter, session, and thread-per-<br>request implications in the Spring MVC stack?<br>27|
|**DI**|Which component creates this object, what dependencies does it require, and can<br>it be unit-tested without Spring?|
|**Spring Core**|What is the<br>`ApplicationContext` ;how was this bean discovered/defined; what<br>is its scope/lifecycle?<br>36|
|**MVC**|Can you trace a request from filters through<br>`DispatcherServlet` to controller<br>and response conversion?<br>45|
|**Transactions**|Where is the transaction boundary, which manager is active, what causes rollback,<br>and does the call pass through the relevant proxy?<br>70|
|**Data**|What SQL actually executes, how many queries execute, and where are<br>connections/transactions held?|
|**Security**|Which<br>`SecurityFilterChain` handles the request, how is the principal<br>authenticated, and where is authorization enforced?<br>52|
|**Boot**|Which starter introduced a dependency, which auto-configuration created a bean,<br>and how would you override it?<br>81|
|**Configuration**|Which values vary by environment, where do secrets live, and which configuration<br>source wins?|

|Area|A Spring Boot developer should be able to answer|
|---|---|
|**Testing**|Which tests should be pure unit tests, slices, application-context tests or real-<br>infrastructure tests?<br>82|
|**Operations**|What health, latency, error, JVM, DB-pool and dependency metrics indicate trouble?<br>Are Actuator endpoints exposed safely?<br>55|
|**Packaging**|Is the target an executable application or WAR deployment, and what assumptions<br>belong to the deployment platform?<br>26|
|**Versioning**|What Java and Jakarta baselines does the chosen Boot generation require? Never<br>infer them from a different Spring release line.<br>24|

### **Pros and cons across the architectural generations** 

|Approach|Main advantages|Main disadvantages / risks|Best conceptual use<br>today|
|---|---|---|---|
|**Direct**<br>**Servlet API**|Small abstraction gap;<br>full control; standardized<br>lifecycle; excellent way to<br>understand web<br>foundations.<br>42|Repetitive routing/binding/<br>error/view code; easy to mix<br>infrastructure and business<br>concerns; manual wiring.|Infrastructure/<br>framework code, very<br>small specialized<br>handlers, and<br>foundational<br>knowledge.|
|**Servlet + JSP**|Simple server-rendered<br>model; JSP separates<br>much HTML from<br>controllers; standardized<br>web platform.<br>83|Scriptlets can collapse<br>separation; presentation and<br>server state can become<br>tightly intertwined; traditional<br>deployment/configuration<br>friction.|Primarily maintenance/<br>migration of<br>established<br>applications.|
|**Struts 1**|Established MVC<br>conventions and<br>centralized action<br>dispatch at a time when<br>applications otherwise<br>reinvented them.<br>30|Framework-specific actions/<br>configuration; older XML-<br>heavy model; Struts 1 is end-<br>of-life.<br>84|Legacy maintenance<br>and migration source.|
|**JSF**|Standardized<br>component state,<br>validation, events and<br>server-side UI lifecycle—<br>problems explicitly left<br>low-level by Servlet/JSP.<br>17|Rich lifecycle/state model is<br>harder to reason about than<br>request-oriented MVC and<br>may not match API-centric<br>systems.<br>33|Component-oriented<br>server-side Java UIs<br>where its model fits<br>requirements.|

|Approach|Main advantages|Main disadvantages / risks|Best conceptual use<br>today|
|---|---|---|---|
|**Spring**<br>**Framework**<br>**without**<br>**Boot**|Excellent IoC/DI, POJO<br>model, AOP, portable<br>transactions, MVC, JDBC/<br>ORM integration;<br>infrastructure can be<br>selected independently.<br>7|More assembly/<br>configuration/version-<br>management responsibility<br>rests on application team.|Framework/library<br>development, unusual<br>infrastructure<br>requirements, or cases<br>where Boot conventions<br>are intentionally not<br>desired.|
|**Spring Boot**|Fast conventional setup;<br>managed dependency<br>families; auto-<br>configuration; stand-<br>alone execution; mature<br>test and production<br>tooling.<br>85|Conditional behavior can<br>appear “magical”; large<br>dependency graphs are easy<br>to acquire; poor<br>understanding of JPA/<br>security/transactions remains<br>dangerous even when<br>configuration is easy.|Default choice for many<br>contemporary Spring<br>applications where<br>Spring's programming<br>model fits the problem.|

The larger conclusion is that every generation trades **explicit local code** for **shared framework convention** . Raw Servlets maximize explicitness but force the application to own repetitive infrastructure. Spring Boot minimizes routine assembly but demands framework literacy when defaults interact. Neither extreme eliminates complexity; the difference is whether that complexity is implemented repeatedly by individual applications or concentrated in reusable, standardized infrastructure. 

A useful mental model is therefore: 

#### `Servlet` 

- `= standard web execution model` 

#### `JSP / Struts / JSF` 

- `= higher-level web presentation/controller abstractions` 

#### `Spring Framework` 

- `= general application composition + enterprise infrastructure model` 

#### `Spring MVC` 

- `= Spring's Servlet-based web framework` 

```
Spring Data / Security
```

- `= specialized Spring portfolio projects` 

```
Spring Boot
```

- `= opinionated assembly, configuration and operational layer over Spring` 

That model prevents perhaps the most common conceptual error in learning Spring Boot: treating it as an alternative to Servlets. It is more accurately the distant descendant of a stack whose bottom layers— including HTTP, Servlet filters and the Servlet container for Spring MVC—are still operating underneath it. 86 

## **Further reading and primary sources** 

For the historical origin of Spring, the most valuable primary account is Rod Johnson's Spring blog essay **“Spring Framework: The Origins of a Project and a Name”** <u>, which directly discusses the 2002 book code,</u> the emergence of IoC/DI, <mark>`JdbcTemplate` ,</mark> MVC, the June 2003 public project, and the origin of the “Spring” name. 16 

For the first production Spring generation, read **<u>Spring Framework 1.0 Final Released</u>** <u>. The release</u> announcement is unusually useful historically because it shows what Spring considered differentiating in 2004: a lightweight container, AOP, portable declarative transaction management, DAO/JDBC abstractions, ORM integration and MVC. 18 

For the Servlet foundation, use the **<u>Jakarta Servlet specification</u>** together with the Servlet API documentation. The API's lifecycle description—initialization, request servicing and destruction—is fundamental to understanding what Spring MVC ultimately runs on. 87 

For JSP's role as a presentation technology, see the **<u>Jakarta Server Pages specification</u>** <u>. It is particularly</u> useful for understanding that JSP is translated into Servlet machinery rather than representing an unrelated runtime. 5 

For early MVC history, Apache's announcement of **Struts 1.0 on June 15, 2001** provides contemporary context for the framework's objective of providing a reusable MVC architecture. The Apache Struts project should primarily be read historically for Struts 1 because that generation has reached end of life. 88 

For JSF's original motivation, the JCP's **JSR 127 JavaServer Faces specification material** is especially revealing: it explicitly describes the problem of managing GUI state, form processing and componentspecific event dispatch directly over Servlet/JSP and explains why a standardized component framework was proposed. 17 

For modern Spring fundamentals, the most important official chapters are the **<u>Spring Framework IoC container reference</u>** <u>,</u> **<u>Spring MVC</u>** **<u><mark>`DispatcherServlet`</mark> documentation</u>** <u>,</u> **<u>Spring AOP reference</u>** <u>, and</u> **<u>Spring transaction reference</u>** <u>. Together they explain the mechanisms most frequently hidden by beginner-</u> level Spring Boot tutorials. 89 

For Spring Boot specifically, start with the **<u>Spring Boot project page</u>** and the **<u>auto-configuration documentation</u>** <u>. The latter is arguably the most important document for moving from “I can use Boot” to “I</u> 67 understand why Boot configured this application.” 

For persistence, the **<u>Spring JDBC reference</u>** and **<u>Spring Data JPA project documentation</u>** should be read together: the first demonstrates Spring's original philosophy of removing resource-management boilerplate while retaining SQL, while the second demonstrates the later repository-level abstraction. 51 

For security, read **<u>Spring Security's Servlet Architecture</u>** before relying exclusively on configuration snippets. Understanding <mark>`DelegatingFilterProxy` ,</mark> <mark>`FilterChainProxy`</mark> and <mark>`SecurityFilterChain`</mark> makes authentication and authorization failures far easier to diagnose. 52 

For production operation, use the **<u>Spring Boot Actuator endpoint reference</u>** and Boot's testing documentation. Actuator explains health/management endpoint exposure, while the testing reference distinguishes general Boot testing support, full application tests and focused test modules. 90 

Finally, anyone migrating a pre-Jakarta application into a modern Boot generation should read **<u>Spring Boot 3.0 Goes GA</u>** and **<u>Preparing for Spring Boot 3.0</u>** even when the ultimate target is newer than Boot 3. Those documents clearly mark the historical transition to Java 17 and <mark>`jakarta.*` ,</mark> which remains one of the most consequential fault lines between legacy <mark>`javax.servlet`</mark> applications and current Spring generations. 91 

1 4 27 42 56 https://jakarta.ee/specifications/servlet/6.0/apidocs/jakarta.servlet/jakarta/servlet/servlet https://jakarta.ee/specifications/servlet/6.0/apidocs/jakarta.servlet/jakarta/servlet/servlet 

2 16 35 https://spring.io/blog/2006/11/09/spring-framework-the-origins-of-a-project-and-a-name https://spring.io/blog/2006/11/09/spring-framework-the-origins-of-a-project-and-a-name 

3 26 67 85 https://spring.io/projects/spring-boot https://spring.io/projects/spring-boot 

5 83 https://jakarta.ee/specifications/pages/ https://jakarta.ee/specifications/pages/ 

6 30 43 88 https://struts.apache.org/announce-2002.html https://struts.apache.org/announce-2002.html 

7 18 37 https://spring.io/blog/2004/03/24/spring-framework-1-0-final-released https://spring.io/blog/2004/03/24/spring-framework-1-0-final-released 

https://docs.spring.io/spring-boot/reference/using/auto-configuration.html 

8 39 40 46 https://docs.spring.io/spring-boot/reference/using/auto-configuration.html 

9 41 45 86 https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-servlet.html 

https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-servlet.html 

10 24 71 80 91 https://spring.io/blog/2022/11/24/spring-boot-3-0-goes-ga https://spring.io/blog/2022/11/24/spring-boot-3-0-goes-ga 

> 11 https://www.eclipse.org/community/eclipse_newsletter/2020/february/3.php 

https://www.eclipse.org/community/eclipse_newsletter/2020/february/3.php 

> 12 https://encyclopedia.pub/entry/36567 https://encyclopedia.pub/entry/36567 

13 28 https://en.wikipedia.org/wiki/Jakarta_Servlet https://en.wikipedia.org/wiki/Jakarta_Servlet 

> 14 https://tomcat.apache.org/whichversion.html https://tomcat.apache.org/whichversion.html 

> 15 https://jcp.org/en/jsr/detail?id=154 

https://jcp.org/en/jsr/detail?id=154 

17 32 34 https://www.jcp.org/en/jsr/detail?id=127 

https://www.jcp.org/en/jsr/detail?id=127 

https://spring.io/blog/2006/11/28/a-java-configuration-option-for-spring 

19 53 68 https://spring.io/blog/2006/11/28/a-java-configuration-option-for-spring 

> 20 https://jcp.org/en/jsr/detail?id=315 https://jcp.org/en/jsr/detail?id=315 

> 21 https://jcp.org/en/jsr/detail?id=340 

https://jcp.org/en/jsr/detail?id=340 

22 38 https://spring.io/blog/2014/04/01/spring-boot-1-0-ga-released 

https://spring.io/blog/2014/04/01/spring-boot-1-0-ga-released 

> 23 https://spring.io/blog/2018/03/01/spring-boot-2-0-goes-ga 

https://spring.io/blog/2018/03/01/spring-boot-2-0-goes-ga 

https://spring.io/blog/2025/11/20/spring-boot-4-0-0-available-now 

https://spring.io/blog/2025/11/20/spring-boot-4-0-0-available-now 

> 29 https://www.jcp.org/en/jsr/detail?id=152 

https://www.jcp.org/en/jsr/detail?id=152 

31 84 https://struts.apache.org/struts1eol-announcement.html 

https://struts.apache.org/struts1eol-announcement.html 

33 44 

https://jakarta.ee/specifications/faces/3.0/jakarta-faces-3.0 

https://jakarta.ee/specifications/faces/3.0/jakarta-faces-3.0 

36 47 89 https://docs.spring.io/spring-framework/reference/core/beans/introduction.html 

https://docs.spring.io/spring-framework/reference/core/beans/introduction.html 

48 81 

https://docs.spring.io/spring-boot/reference/using/build-systems.html 

https://docs.spring.io/spring-boot/reference/using/build-systems.html 

49 63 https://docs.spring.io/spring-framework/reference/core/aop/introduction-defn.html 

https://docs.spring.io/spring-framework/reference/core/aop/introduction-defn.html 

50 59 https://docs.spring.io/spring-framework/reference/data-access/transaction/strategies.html https://docs.spring.io/spring-framework/reference/data-access/transaction/strategies.html 

51 60 https://docs.spring.io/spring-framework/reference/data-access/jdbc/core.html 

https://docs.spring.io/spring-framework/reference/data-access/jdbc/core.html 

52 62 78 https://docs.spring.io/spring-security/reference/servlet/architecture.html https://docs.spring.io/spring-security/reference/servlet/architecture.html 

54 72 82 https://docs.spring.io/spring-boot/reference/testing/index.html https://docs.spring.io/spring-boot/reference/testing/index.html 

55 74 90 https://docs.spring.io/spring-boot/reference/actuator/endpoints.html 

https://docs.spring.io/spring-boot/reference/actuator/endpoints.html 

57 69 https://docs.spring.io/spring-framework/reference/core/beans/classpath-scanning.html https://docs.spring.io/spring-framework/reference/core/beans/classpath-scanning.html 

58 61 64 https://docs.spring.io/spring-framework/reference/data-access/transaction.html https://docs.spring.io/spring-framework/reference/data-access/transaction.html 

65 76 https://docs.spring.io/spring-boot/reference/testing/spring-applications.html https://docs.spring.io/spring-boot/reference/testing/spring-applications.html 

66 75 https://spring.io/projects/spring-data-jpa 

https://spring.io/projects/spring-data-jpa 

> 70 https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/tx-declexplained.html 

https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/tx-decl-explained.html 

> 73 https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html 

https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html 

> 77 https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html 

> 79 https://spring.io/blog/2022/01/20/spring-boot-3-0-0-m1-is-now-available 

https://spring.io/blog/2022/01/20/spring-boot-3-0-0-m1-is-now-available 

87 https://jakarta.ee/specifications/servlet/6.1/jakarta-servlet-spec-6.1 

https://jakarta.ee/specifications/servlet/6.1/jakarta-servlet-spec-6.1 

