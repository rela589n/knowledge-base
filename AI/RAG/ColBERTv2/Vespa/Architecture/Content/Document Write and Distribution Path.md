**Document Write Distribution Path** — the journey of a document from client request to durable storage across replicas.

## Overview

```
Client → Gateway → Distributor → Content Nodes (parallel) → ACKs → Response
```

## Step-by-Step

### 1. Client → Gateway

Client sends HTTP request:

```bash
curl -X POST \
  http://vespa-gateway:8080/document/v1/shop/product/docid/SKU-789 \
  -d '{"fields": {"title": "Wireless Keyboard", "price": 49.99}}'
```

Gateway (container node):
- Parses JSON
- Validates against [[Schema]]

### 2. Document ID → Bucket

Gateway computes bucket ([[Bucket Distribution]]):

```
"id:shop:product::SKU-789"
        ↓
   hash → 58-bit location
        ↓
   N least-significant bits
        ↓
   bucket ID: 0x8C
```

### 3. Find Distributor

Gateway queries cluster controller:
	"Who owns bucket 0x8C?"

Cluster state returns: distributor on node1

### 4. Distributor → Ideal State

Distributor calculates replica placement:

```
Ideal State Algorithm:
  input:  bucket ID + node list + redundancy
  output: [node0, node2]
```

### 5. Parallel Write

Distributor sends to both nodes simultaneously:

```
     Distributor
        /    \
       ↓      ↓
    node0   node2
```

Each content node's **proton** process:
1. Writes to transaction log (durability)
2. Indexes document
3. Stores in bucket replica
4. Sends ACK

### 6. Wait for ACKs

```
node0 ACK ✓
node2 ACK ✓
         ↓
ACK count == redundancy → success
```

**Key:** Write succeeds only when ALL `redundancy` copies confirm

### 7. Response

```
HTTP 200 OK
```

Document is now:
- Stored on 2 nodes
- Fully indexed
- Durable

## Failure Handling

**Write failure (node timeout):**
- Didn't reach redundancy count
- Client gets error
- Client should retry

**Node dies after write:**
1. Cluster controller detects failure
2. Distributor recalculates ideal state
3. Copies replica from surviving node
4. Redundancy restored automatically

## See Also

- [[Content Cluster]]
- [[Content Cluster Scaling]]
