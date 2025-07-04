---
aliases: []
---
Every aggregate entity  must have:
- it's own namespace;
- a namespaces for related entities (direct)
- a namespace for related infrastructural / ui things (like gateway, repository, presenters, fixtures, http exceptions etc) - these should likely have a separate namespace (Support);
- the namespace for features/scenarios/actions;

[[Important things at the top, not important things - at the bottom]]

See [[DDD Layered Architecture]]

See also [[DDD Concepts]], yet do not take into account their [[Folder by type packaging|Tier-based packaging]].