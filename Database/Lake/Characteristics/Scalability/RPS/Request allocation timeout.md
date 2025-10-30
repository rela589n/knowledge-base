**Request allocation timeout** - option that allows us to specify the **hard limit** for the request [[Latency]] in the queue.

Basically, this is the time (in seconds) that request will have already waited for the worker until it gets dropped.

> It is much easier to configure, compared to [[Max queue size]], option, though it is much **less flexible** as well.

One could set some safe timeout of 8 seconds for http server.

Supported by [[RoadRunner]] ([request queues](https://docs.roadrunner.dev/docs/http/http#request-queues), [allocate_timeout](https://docs.roadrunner.dev/docs/error-codes/allocate-timeout))
