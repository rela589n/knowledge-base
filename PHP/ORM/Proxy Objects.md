[[State Management]] is accomplished via Object Proxies.

There are two types of proxies:
- Ghost Proxies
- Link Proxies

Ghosts [[State Management|Manage the State]], perform [[Lazy Loading]], and spy on the interactions with the entity to track the changes. They manage mapped properties, keep track of the unique fields ([[Lazy Loading|Loading]] of unique field could result in [[Proxy Merge|Proxy Merge]]), and make sure that each update is appropriated to the [[Reactive Collection|Reactive Collections]].

Links could come as a result of a [[Proxy Merge]]. Before they came to be Links they were ordinary Ghost Objects. Yet, once collision had been detected, [[Proxy Merge]] happened and they were updated to forward all interactions to the target Ghost object. They are indifferentiable from the real Ghost but by object id.

> When comparing entities, make sure to compare their identifiers, not object identities. Never use `$e1 === $e2`.

Actually everything that ORM can do is done primarily with Ghost objects. That's why on the very first `add()` the existing object is reset as lazy (if that was possible?) so that we can use Ghost functionality with it.

<s>After calling `sync()`, new entities are made persistent and they are discarded in favor of Proxies. Beware that doing any modifications to these entities after first `sync()` call won't be tracked.</s>

After adding new entity into the Collection, the very added object is actually discarded. Instead, Collection will retain another Ghost object that has all needed ORM features. This object is returned from `add()` method.

Consider the case when the Whole [[Aggregate]] is created at once.

Let's say that Post and Post.comments is created at once. When Post is being added to the collection, [[Entity Ghost kick-in]] happens. At this point, related collections are [[Autowire Feature|Autowired]], and existing items are moved there (with another [[Entity Ghost kick-in|Kick-in]]).

Thus, afterwards all these objects will be replaced with their mirror Ghosts.
