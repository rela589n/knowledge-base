---
aliases:
  - Vespa config server
---
**Config Cluster** — the coordination layer in [[Vespa Architecture|Vespa]].

## Role

- Distributes configuration to all nodes
- Manages application deployment
- Tracks cluster state
- **Source of truth** for the application package

## Port

Listens on `:19071` by default.

## Key Operations

- [[Vespa Deploy|Deploy]] application packages
- Coordinate config changes across nodes
- Health and convergence checks

## In Docker Compose

Specify `VESPA_CONFIGSERVERS` to a host name of the container.
You shouldn't use `localhost` since on inner nodes it resolves to locahost.

```yaml
environment:
  - VESPA_CONFIGSERVERS=vespa
```

Without explicit hostname → random ID (e.g. `03b8a5340ee8`) → config server unreachable.

