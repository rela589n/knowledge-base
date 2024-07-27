Temporal server internally manages state of the workflows.
It could be the case that workflow started being executed on one worker that eventually crased, continued on another worker and finished on the third one.

Each activity is decorated with retry logic in case if requested service is temporarily down.

Temporal server internally manages queues as well so that activities could be executed in scalable manner.

