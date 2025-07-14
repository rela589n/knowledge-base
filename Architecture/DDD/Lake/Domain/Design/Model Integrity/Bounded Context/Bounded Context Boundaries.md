To determine **[[Bounded Context|Context]] Boundaries**, you first have to understand that one team is primarily interested in the **part of the system they'll have to change**, and secondarily in [[Context Integration Map|Integrations]].

Deep [[Context Integration Map|Integration]] between [[Bounded Context|Bounded Contexts]] is impractical.

With big [[Bounded Context]]:
- [[Continuous Integration]] will have some overhead;
- Features flow is easier;
- [[Translation Layer|Translation]] is harder.

With small [[Bounded Context]]:
- [[Continuous Integration]] is easier;
- Features flow is harder (integrated);
- [[Translation Layer|Translation]] is easier.


