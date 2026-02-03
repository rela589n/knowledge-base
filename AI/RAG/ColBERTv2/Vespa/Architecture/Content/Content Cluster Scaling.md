**Content Cluster Scaling** — adjusting capacity by adding/removing nodes while the system stays online.

## Two Dimensions

**Vertical (data capacity)**
- Add nodes → data partitions spread across more machines
- Each node holds a smaller portion of the corpus
- Use when data outgrows current storage

**Horizontal (query throughput)**
- Add *groups* of nodes
- Each group holds a complete replica of all data
- Queries served by any group → more parallel capacity

## Flat Scaling (Adding Nodes)

Before (2 nodes):

```xml
<content id="docs" version="1.0">
  <redundancy>2</redundancy>
  <documents>
    <document type="doc" mode="index"/>
  </documents>
  <nodes>
    <node hostalias="node1" distribution-key="0"/>
    <node hostalias="node2" distribution-key="1"/>
  </nodes>
</content>
```

After (4 nodes):

```xml
<nodes>
  <node hostalias="node1" distribution-key="0"/>
  <node hostalias="node2" distribution-key="1"/>
  <node hostalias="node3" distribution-key="2"/>  <!-- new -->
  <node hostalias="node4" distribution-key="3"/>  <!-- new -->
</nodes>
```

## Grouped Distribution (Query Scaling)

Each group holds full corpus replica:

```xml
<content id="docs" version="1.0">
  <min-redundancy>2</min-redundancy>
  <documents>
    <document type="doc" mode="index"/>
  </documents>
  <group>
    <distribution partitions="1|*"/>
    <group name="group0" distribution-key="0">
      <node hostalias="node1" distribution-key="0"/>
      <node hostalias="node2" distribution-key="1"/>
    </group>
    <group name="group1" distribution-key="1">
      <node hostalias="node3" distribution-key="2"/>
      <node hostalias="node4" distribution-key="3"/>
    </group>
  </group>
</content>
```

**Note:** `<group>` and `<nodes>` are mutually exclusive
	use one or the other, not both

## Self-Managed Procedure

1. **Prepare new node**
   - Install Vespa
   - Set `VESPA_CONFIGSERVERS` env var
   - Start the node

2. **Update configuration**
   - Add node to `hosts.xml`
   - Add node element to `services.xml`
   - Ensure unique `distribution-key`

3. **Redeploy**
   ```bash
   vespa deploy
   ```

4. **Monitor redistribution**
   ```bash
   vespa status --cluster docs
   # or check metric:
   # idealstate.merge_bucket.pending = 0 → done
   ```

## Critical Warning

**Never change a node's `distribution-key`**
	it's the node's permanent identity for data placement
	changing it causes undefined behavior:
		best case — temporary data unavailability
		worst case — data loss or crashes

When removing nodes:
	keep existing distribution-keys unchanged
	just remove the `<node>` element

## See Also

- [[Content Cluster]]
