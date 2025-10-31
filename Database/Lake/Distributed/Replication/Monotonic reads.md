There may be the case when the same **request is first sent to the fresh [[Replica]]**, then **to the stale [[Replica]]**. Things will look like going backward in time (applied update is flipped back and forth). To prevent this, we need **monotonic reads**.

**Monotonic read** - stronger guarantee than [[Convergence]], though it is weaker than strong consistency. For any particular user, the requests are **sent to some particular replica**.
