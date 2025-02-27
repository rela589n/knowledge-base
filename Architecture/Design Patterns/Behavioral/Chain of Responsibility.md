> As an example, the Laravel's middleware implement CoR pattern.

**Chain of Responsibility** (aka **Chain of Command**) is a pattern, which allows to pass the request through the **chain of handlers**, where each separate handler decides what to do with this request (either to process is or pass to the next handler).

Example:
- `RejectRedeliveredMessageMiddleware` (sf middleware)
- message bus middlewares
- sf event listeners with stop propagation
