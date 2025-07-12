---
aliases:
  - Published SDK
---
**Open Host Service** - [[Model Context Strategies|Relationship]], in which host [[Bounded Context]] **exposes public SDK** that other [[Bounded Context|Bounded Contexts]] can use to integrate.

When [[Bounded Context]] is needed to be integrated again and again, it brings much **overhead of writing [[Translation Layer]] for every Customer**. Open **SDK simplifies the integration**.

It exposes as set of [[Service|Services]] each client can use.

When new changes are released on the host, there's no need for rewriting all the clients, because we can just update SDK.

Example of [[Open Host Service]]:
- Stripe SDK
- SOAP integrations (WSDL)
- GRPC
