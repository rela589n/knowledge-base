[[State Management]] is accomplished via Object Proxies.

There are two types of proxies:
- Ghost Proxies
- Ref Proxies

Ghosts [[State Management|Manage the State]], perform [[Lazy Loading]], and spy on the interactions with the entity to track the changes. 

They manage mapped properties, keep track of the unique fields ([[Lazy Loading|Loading]] of unique field could result in [[Proxy Merge|Proxy Merge]]), and make sure that each update is reflected in the [[Reactive Collection|Reactive Collections]].

Refs come as a product of a [[Proxy Merge]]. Once Refs were ordinary Ghost Objects. Yet, after collision had been detected and [[Proxy Merge]] happened, they were updated to forward all interactions to the target Ghost object. They are indifferentiable from the real Ghost object but by using object id.

> When comparing entities, you should implement `equals()` to compare their model identifiers, not object identities. Never use `$e1 === $e2`.

Basically everything that ORM can do is one way or another done with Ghost objects.

<s>After calling `sync()`, new entities are made persistent and they are discarded in favor of Proxies. Beware that doing any modifications to these entities after first `sync()` call won't be tracked.</s>

<s>That's why on the very first `add()` the existing object is reset as lazy (if that was possible?) so that we can use Ghost functionality with it.</s>

<s>When adding a new entity into the Collection, the very added object is discarded. Instead, the Collection will retain another corresponding Ghost object that will handle all needed ORM features. This is the object is returned from `add()` method.</s>

That's why entity is hooked to make all interactions with the model come through Ghosts. 

See [[Ghost Proxy kick-in]]

