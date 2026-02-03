**Bucket-to-Node Distribution** — the algorithm that determines which nodes store each bucket.

## Core Concept

Each node has a `distribution-key` — its permanent identity for placement calculations.

```xml
<nodes>
  <node hostalias="node1" distribution-key="0"/>
  <node hostalias="node2" distribution-key="1"/>
  <node hostalias="node3" distribution-key="2"/>
</nodes>
```

## Ideal State Algorithm

Determines bucket placement without central coordination:

1. **Seed** random generator with bucket ID
2. **Generate** pseudo-random number for each node
   - `distribution-key="0"` → 1st random number
   - `distribution-key="1"` → 2nd random number
   - etc.
3. **Sort** nodes by random number (descending)
4. **Select** top N nodes (N = redundancy)

## Example

Bucket `0x8C`, redundancy=2:

```
distribution-key=0 → random: 0.34
distribution-key=1 → random: 0.91  ← highest
distribution-key=2 → random: 0.67  ← second
```

Result: bucket `0x8C` → **node1, node2**

## Why This Design

- **Deterministic** — any component computes placement independently
- **Minimal movement** — adding node N steals only ~1/N buckets from each existing node
- **No central registry** — algorithm replaces coordination

## Distribution-Key Rules

**Never change** a node's distribution-key
	it's permanent identity
	changing it breaks all bucket calculations
	causes data loss or unavailability

**Adding nodes:** use new keys (3, 4, 5...)

**Removing nodes:** delete `<node>` element, keep other keys unchanged

**Avoid large gaps** in key sequence
	wastes random number generations

## See Also

- [[Document Write Path]]
- [[Content Cluster Scaling]]
