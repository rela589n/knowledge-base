---
aliases:
  - Cluster Keeper
---
**Cluster Controller** — the component that monitors node health and publishes cluster state.

## Role

- Continuously polls all nodes for **health/connectivity**
- Maintains set of nodes it considers healthy
- Publishes versioned **cluster state** when set changes

## Cluster State

A versioned snapshot of which nodes are up/down:

```
State version: 42
  node0: UP
  node1: UP
  node2: DOWN
```

When a node fails or recovers:
1. Controller detects the change
2. Increments state version
3. Broadcasts new state to all nodes

## Why Versioning Matters

All nodes must agree on cluster state to compute identical bucket placements.

```
Same inputs → Same outputs

Inputs:
  - Bucket ID
  - Node list (from cluster state)
  - Redundancy setting

Output:
  - Which nodes own this bucket
```

If nodes disagreed on state → overlapping bucket ownership → data corruption

## Consistency Guarantee

Given the same cluster state version:
- All [[Distributor|distributors]] compute identical bucket ownership
- No overlapping ownership possible
- Writes always go to the correct replicas

## See Also

- [[Distributor]]
- [[Content Cluster]]
- [[Bucket-to-Node Distribution]]
