---
aliases:
  - services.xml overview
---
**services.xml** - defines how Vespa deploys and runs your application.
	While the schema defines what data looks like,
		services.xml defines where it lives and how it's processed.

### The Two Core Components

```xml
<services>
    <container>   <!-- Stateless layer (handles requests) -->
    <content>     <!-- Stateful layer (stores data) -->
</services>
```

Think of it like a restaurant:
- **Container** = the waiters (take orders, serve food, stateless)
- **Content** = the kitchen (prepares and stores food, stateful)

---

### The Container: Request Handling

```xml
<container id="text_search" version="1.0">
    <search />
    <document-processing />
    <document-api />
</container>
```

This defines a stateless cluster that handles all incoming requests.

| Element                  | What It Enables                     |
| ------------------------ | ----------------------------------- |
| `<search />`             | Query endpoints (/search/)          |
| `<document-api />`       | Feed endpoints (/document/v1/...)   |
| `<document-processing />` | Transform documents before indexing |

Stateless means:
- No data stored here
- Can scale horizontally (add more containers)
- Any container can handle any request
- Containers forward work to content nodes

> [!tip] Insight
> The `id="text_search"` is important —
> 	it's referenced later by `<document-processing cluster="text_search">`.
> 	This tells content nodes: "use this container cluster for doc processing."

---

### The Content: Data Storage

```xml
<content id="msmarco" version="1.0">
    <min-redundancy>1</min-redundancy>
    <documents>
        <document type="msmarco" mode="index" />
        <document-processing cluster="text_search" />
    </documents>
    <nodes>
        <node distribution-key="0" hostalias="node1" />
    </nodes>
</content>
```

This defines a stateful cluster that stores and indexes your documents.

#### Redundancy

```xml
<min-redundancy>1</min-redundancy>
```

- How many copies of each document to keep
- 1 = single copy (no redundancy, fine for development)
- Production typically uses 2 or 3 for fault tolerance

#### Documents

```xml
<documents>
    <document type="msmarco" mode="index" />
    <document-processing cluster="text_search" />
</documents>
```

`type="msmarco"`
- Links to your schema file (msmarco.sd)
- One content cluster can hold multiple document types

`mode="index"`
- Full indexing mode (searchable, rankable)
- Alternative: `mode="streaming"` for personal data / high cardinality

`cluster="text_search"`
- Route document processing through the container cluster
- Enables document processors (transformations, enrichment)

#### Nodes

```xml
<nodes>
    <node distribution-key="0" hostalias="node1" />
</nodes>
```

Physical topology — where data lives.

| Attribute              | Meaning                                |
| ---------------------- | -------------------------------------- |
| `distribution-key="0"` | Unique ID for data distribution        |
| `hostalias="node1"`    | References a host defined in hosts.xml |

Single node = all data on one machine (development setup).

---

### Request Flow Visualization

```
Client Request
      │
      ▼
┌─────────────────────────────────────────┐
│  CONTAINER CLUSTER (text_search)        │
│  ┌─────────────────────────────────┐    │
│  │  <search />                     │ ◄── GET /search/?yql=...
│  │  <document-api />               │ ◄── POST /document/v1/...
│  │  <document-processing />        │ ◄── Transform before indexing
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
      │
      │ (forward to content)
      ▼
┌─────────────────────────────────────────┐
│  CONTENT CLUSTER (msmarco)              │
│  ┌─────────────────────────────────┐    │
│  │  node1 (distribution-key=0)     │    │
│  │    └── msmarco documents        │    │
│  │        └── inverted index       │    │
│  │        └── attribute store      │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

---

### Scaling: Development → Production

**Development** (single node)
```xml
<nodes>
    <node distribution-key="0" hostalias="node1" />
</nodes>
```

Single node, no redundancy — simple and fast.

**Production** (scaled)
```xml
<min-redundancy>2</min-redundancy>
<nodes>
    <node distribution-key="0" hostalias="node1" />
    <node distribution-key="1" hostalias="node2" />
    <node distribution-key="2" hostalias="node3" />
</nodes>
```

- Data distributed across nodes (sharding)
- Each document replicated to 2 nodes (redundancy)
- Vespa handles distribution automatically

> [!tip] Insight
> `distribution-key` determines data placement.
> Vespa hashes document IDs and assigns them to nodes based on these keys.
> If you add/remove nodes, Vespa redistributes data automatically —
> 	but only if you keep existing distribution-keys stable.

---

### Connection to Your Schema

The relationship between files:

```
services.xml                          schemas/msmarco.sd
─────────────────                     ──────────────────
<document type="msmarco" ...>   ───►  schema msmarco {
                                          document msmarco { ... }
                                      }
```

The `type` attribute must match the schema name exactly.

---

### Summary: What Each Part Controls

| Component          | Responsibility                                | Scales By                     |
| ------------------ | --------------------------------------------- | ----------------------------- |
| `<container>`      | HTTP endpoints, query parsing, doc processing | Adding containers (stateless) |
| `<content>`        | Storage, indexing, search execution           | Adding nodes (sharding)       |
| `<min-redundancy>` | Fault tolerance                               | Copies per document           |
| `<nodes>`          | Physical topology                             | Adding machines               |

## See Also

- [[Vespa Application]]
- [[Vespa Architecture]]
- [[Container Cluster]]
- [[Content Cluster]]
