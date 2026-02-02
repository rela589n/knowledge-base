**Content Cluster** — the stateful storage layer in [[Vespa Architecture|Vespa]].

## Role

- Stores documents
- Maintains indexes (text, vector, attribute)
- Executes distributed search
- Handles data replication

## Configuration

Defined in `services.xml`:

```xml
<content id="default" version="1.0">
  <redundancy>1</redundancy>
  <documents>
    <document type="book" mode="index"/>
  </documents>
  <nodes>
    <node hostalias="node1" distribution-key="0"/>
  </nodes>
</content>
```

## Key Concepts

- **Redundancy** — how many copies of each document
- **Distribution key** — identifies the node for data partitioning
- **Document type** — references a [[Schema]]

## Scaling

- Data is partitioned across nodes
- Nodes can be added/removed dynamically
- Rebalancing happens automatically
