---
aliases:
  - Published SDK
---
**Open Host Service** - [[Relationships Between Bounded Contexts|Relationship]], in which host [[Bounded Context]] **exposes public SDK** that can be used by other [[Bounded Context|Bounded Contexts]] to integrate.

When [[Bounded Context]] is needed to be integrated again and again, bringing much **overhead of writing [[Translation Layer]] for all the Customers**. Open **SDK simplifies the integration**.

It's represented as set of [[Service|Services]] each client can use.

When new changes are released on the host, there's no need for rewriting all the clients, because we can just update SDK.
