Worker Factory stores an array repository of Workers.

Every worker is unique per [[Task Queue]] name (used as a key in the array).

Factory has a Server. Its run() method dispatches messages to the server, yet it dispatches the request back to the factory, so it's factory's business after all.

Worker Factory processes the Request either by sending to the Router (if no task queue header), or dispatching it to the worker based on [[Task Queue]] (header).

Normally, header should be present, since `WorkflowOptions` has it by default, and `ActivityOptions` inherits it from `WorkflowOptions`.

Every Worker has Router.  Whenever Worker processes Request, it delegates it's processing to the Router.

Router matches request by name. Collection of routes is indexed by name. Route name is short class name. Thus, only one route is executed.

> How does temporal worker receive messages?
