**Read-repair** - when the **read** data has **stale values** for some replicas, **newer values are written** to these replicas.

**Anti-entropy process** - the background **process** constantly **checks for differences in the data** and **copies** missing **writes** from one replica to another.