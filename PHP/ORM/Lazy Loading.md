**Lazy Loading** - loading only what [[Specification]] requests (plus primary id) instead of loading heavy object right away.

[[ORM Collection|Collection]] provides objects that include no more than what's requested. So, if filter was by `email`, then objects returned will have `id` and `email` fields only.

State is populated step by step.
When field is being accessed, that's when it's loaded. The approach to load should be [[Column Loading|Eager Lazy Loading]] approach.

For example, suppose we've selected user by `email`. Attempting to access `password`  will cause it to be loaded from the database.

Due to the possibility of existence of multiple Proxies for the same entity, [[Proxy Merge]] are necessary.
