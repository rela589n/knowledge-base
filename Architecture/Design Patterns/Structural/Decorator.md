**Decorator**: ***add* behavior** to the object 
	***w/o modifying*  its** source code.

One **interface** ([[Dependency inversion principle|DIP]]) and multiple implementations.

One **implementation** "decorates" **(wraps) another** 
and **adds** some additional **behavior** (like logs) to the original class.

**Examples :**
- Profiler:
	- `TraceableEventDispatcher` (keeps track of the events)
	- `TraceableMessageBus` (keeps track of dispatched messages)
- [[Centrifugo]] - response logging
- logging/caching gateway responses
