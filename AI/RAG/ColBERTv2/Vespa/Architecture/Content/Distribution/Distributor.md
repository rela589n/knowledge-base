**Distributor** — the component that routes document operations to correct content nodes.

## Role

- Receives all document operations (put, update, get, remove)
- Determines which bucket a document belongs to
- Routes requests to content nodes holding that bucket's replicas
- Tracks bucket state and triggers maintenance operations

## Bucket Database

Each distributor maintains metadata for its buckets:

| Field | Purpose |
|-------|---------|
| Replica locations | Which content nodes hold copies |
| Document count | Number of docs in bucket |
| Checksum | For consistency verification |

**Key:** One bucket maps to exactly one distributor
	but distributor handles many buckets

## No Central Directory

Bucket information is **not** stored centrally.

At startup, distributor:
1. Polls content nodes for bucket info
2. Rebuilds bucket database from responses
3. Uses ideal state algorithm to validate ownership

At cluster state change:
1. Receives new state from [[Cluster Controller (health)]]
2. Polls content nodes for bucket handover
3. Takes ownership of new bucket set

## Maintenance Operations

Distributor monitors bucket health and triggers:

| Condition | Action |
|-----------|--------|
| Too few replicas | Create new replica on another node |
| Replicas differ | Merge to restore consistency |
| Too many replicas | Delete superfluous copies |

## See Also

- [[Write Path]]
- [[Bucket-to-Node Distribution]]
- [[Cluster Controller (health)]]
