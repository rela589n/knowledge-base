Allows to add the behavior to object w/o modifying it's source code.

We have one interface and multiple implementations.

One implementation "decorates" another in terms of adding some additional behavior (like logs) to the original class.

Examples:
- `TraceableEventDispatcher` (keeps track of the events)
- `TraceableMessageBus` (keeps track of dispatched messages)
- logging/caching gateway responses

