---
aliases:
  - Vespa middleware
  - API entrypoint
---
**Container Cluster** — the stateless middleware layer in [[Vespa Architecture|Vespa]].

## Role

- Sits between clients and content nodes
- Handles HTTP requests (queries, document writes)
- Processes data before indexing
- Transforms query results before returning

## Configuration

Defined in `services.xml`:

```xml
<container id="default" version="1.0">
  <search/>           <!-- enables query handling -->
  <document-api/>     <!-- enables document CRUD -->
  <nodes>
    <node hostalias="node1"/>
  </nodes>
</container>
```

## Extension Points

- **Searchers** — custom query processing logic
- **Document processors** — transform documents before indexing
- **Handlers** — custom HTTP endpoints
- **Components** — shared services (written in Java)

## Port

Listens on `:8080` by default.
