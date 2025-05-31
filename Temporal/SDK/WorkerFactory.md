Worker Factory has an array repository of Workers.

Each [[Worker Entity|worker]] is unique per [[Task Queue]] name (used as a key in the array).

Factory has a Server. Its `run()` method dispatches messages to the server, though it dispatches the request back to the factory's `onRequest()` method, so it's factory's business after all.

Worker Factory processes the Request either by sending it to its own Router (if no task queue header), or dispatching it to the worker based on [[Task Queue]] (header).

It's own router has only one route - `GetWorkerInfo`, which specifies the [[Task Queue]] and [[Workflow Type|Workflow Types]] and [[Activity Type|Activity Types]] it can process. Thus this information can be used to properly route [[Task|Tasks]] to the correct [[Worker|Workers]].

Normally [[Task Queue]] header is present, as `WorkflowOptions` has it by default, and `ActivityOptions` inherits it from `WorkflowOptions`.

Every Worker has a Router.  Whenever Worker processes Request, it delegates it's processing to the Router.

Collection of routes is indexed by name. 
Router matches request by name (e.g. key). 
Route name is short class name. 
Only one route is executed on request.

> How does temporal worker receive messages? Likely it executes `GetWorkerInfo` before anything else, and then this worker is "remembered" with these options.
