> As an example, the Laravel's middleware implement CoR pattern.

**Chain of Responsibility** (aka **Chain of Command**) is a pattern, which allows to pass the request through the chain of handlers, where each separate handler can decide what to do with this request (process or pass to the next handler).

Example:
- `RejectRedeliveredMessageMiddleware` (sf middleware)
- custom middlewares for message bus
- event listeners with stop propagations

