[[State Management]] is accomplished via Object Proxies.

There are two types of proxies:
- Wrappers (Proxies)
- Ghosts

Wrappers are the objects that client code interacts with. They point to Ghosts. This distinction between the two is primarily needed due for [[Proxy Merge]].

Ghosts [[State Management|Manage the State]], perform [[Lazy Loading]], and generally spy on the interactions with the entity. They manage mapped properties, keep track of the unique fields ([[Lazy Loading|Loading]] of unique field could result in [[Proxy Merge|Proxy Merge]]), and make sure that each update is appropriated to the [[Reactive Collection|Reactive Collections]].

Actually, anything that ORM can do is primarily done with Ghost objects. That's why on the very first `add()` the existing object is being reset as lazy so that we can use Ghost functionality with it.
