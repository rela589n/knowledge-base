Every entity must have:
- it's own namespace;
- the class itself (direct);
- a namespaces for related entities (direct)
- a namespace for related infrastructural / ui things (like gateway, repository, presenters, fixtures, http exceptions etc) - these should likely have a separate namespace (Support);
- the namespace for actions/scenarios;
