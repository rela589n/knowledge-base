**Shared-nothing architecture** (**horizontal scaling**, **scaling-out**) - each node has **it's own resources**, which are not shared. Any **coordination** between nodes is implemented **on the code level** using network. It is possible to **distribute data** across multiple regions, thus **reduce latency** for users. ^b18052

Shared-nothing architecture brings **additional complexity to applications**, which the database can no longer hide from us. ^05e41e

Shared-nothing systems **communicate** only **via the network,** no direct access to disk or memory is allowed. Only network calls. ^6b450e

**Shared-nothing** is a **simplest way** to build systems, because:
- relatively **cheap**;
- requires **no special hardware**;
- **reliability** may be achieved **via redundancy**.

