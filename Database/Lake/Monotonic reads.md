There may be the case when the same **request is first sent to the fresh replica**, then **to the stale replica**. Things will look like going backward in time (applied update is flipped back and forth). To prevent this, we need **monotonic reads**.

**Monotonic read** - stronger guarantee than [[Eventual Consistency]], though it is weaker than strong consistency. For any particular user, the requests are **sent to some particular replica**.
