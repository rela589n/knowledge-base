[[SAGA pattern]]

Temporal server internally manages state of the workflows.
It could be the case that workflow started execution on one worker (that eventually crased), continued on another worker, and finished on the third one.

Each activity class is decorated to provide retry logic in case if requested service is temporarily down.

Temporal server internally manages queues so that activities could be executed in scalable manner.
