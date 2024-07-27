There may be the case when the same **request is first sent to the fresh replica**, then **to the stale replica**. Things will look like going backward in time. To prevent this, we need **monotonic reads**.

**Monotonic read** - stronger guarantee than [[Eventual consistency]], though it is weaker than strong consistency. For any particular user, the requests are **sent to some particular replica**.
