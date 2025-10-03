---
aliases:
  - Published SDK
---
**Open Host Service** - **host [[Bounded Context|Context]]** *exposes* **public SDK** as an API that **other [[Bounded Context|Contexts]] can use** it to integrate.

Open **SDK *simplifies*** the **integration** 
*when* **[[Bounded Context|Context]]** must be **integrated again** and again
*eliminating* **overhead** of writing **[[Translation Layer]]** for **every Customer**. 

It exposes as set of [[Architecture/DDD/Lake/Patterns/Service/Service|Services]] that clients can use.

When new changes are released on the host, there's no need for rewriting all the clients, because we can just update SDK.

**Example** of [[Open Host Service]]:
- Stripe SDK
- SOAP integrations (WSDL)
- [[gRPC code generation]]
