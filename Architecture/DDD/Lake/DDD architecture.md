---
aliases:
  - DDD namespaces structure
---
Every aggregate entity  must have:
- it's own namespace;
- a namespaces for related entities (direct)
- a namespace for related infrastructural / ui things (like gateway, repository, presenters, fixtures, http exceptions etc) - these should likely have a separate namespace (Support);
- the namespace for actions/scenarios;

See [[DDD Layered Architecture]]