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

- **Redundancy** — how many [[Replica|Replicas]] of each document
- **Distribution key** — identifies [[Bucket-to-Node Distribution]]
- **Document type** — references a [[Schema]]

## Multiple Clusters

`services.xml` supports multiple content clusters:

```xml
<services version="1.0">
  <content id="music" version="1.0">
    <documents>
      <document type="song" mode="index"/>
    </documents>
    <nodes>
      <node hostalias="node1" distribution-key="0"/>
    </nodes>
  </content>

  <content id="videos" version="1.0">
    <documents>
      <document type="video" mode="index"/>
    </documents>
    <nodes>
      <node hostalias="node2" distribution-key="0"/>
    </nodes>
  </content>
</services>
```

**Use cases:**
- **Data isolation** — different document types, different scaling needs
- **Independent [[Content Cluster Scaling|Scaling]]** — scale each cluster separately
- **Different redundancy** — critical data gets more replicas

**Constraint:** `distribution-key` must be unique *within* each cluster
	but can repeat across clusters

## Scaling

See [[Content Cluster Scaling]]
