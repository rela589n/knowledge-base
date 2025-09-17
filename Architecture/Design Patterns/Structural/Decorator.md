**Decorator** allows to **add behavior** to the object **w/o modifying it**s source code.

We have one **interface** and multiple implementations.

One **implementation** "decorates" **(wraps) another** 
and **adds** some additional **behavior** (like logs) to the original class.

**Examples :**
- Profiler:
	- `TraceableEventDispatcher` (keeps track of the events)
	- `TraceableMessageBus` (keeps track of dispatched messages)
- [[Centrifugo]] - response logging
- logging/caching gateway responses

