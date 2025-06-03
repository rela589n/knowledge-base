- Activity sends http request that takes long time.
- [[Activity Execution Timeouts|Activity Execution Timeout]] is elapsed.
- Compensation is executed (no-op due to [[Idempotence]] check).
- Http request succeeds.
- Workflow is already closed, compensation executed, but state polluted.

It's not that simple. Setting [[Activity cancellationType]]=wait will not help, since it works for cancellation only within [[Activity Execution Timeouts|Execution Timeout]] limits, while here the timeout is elapsed.

We have to guarantee that compensation won't be executed until [[Activity]] has surely completed.

One way is to guarantee this is by ensuring that http timeout is less than [[Start-To-Close]] timeout. This way, since it's http request that takes most of the work, it will fail until [[Activity]] times-out.

Yet in the long run if http request has timed-out, it's possible that compensation will execute with no result if the request hasn't completed yet. Say, this request creates something in the database, and the compensation deletes it. Running deletion before creation will not delete anything.

But if the delay is caused by high load on the upstream, it's likely that the compensation will also time-out `¯\_(ツ)_/¯`.

There's nothing better we can do about it, except to ensure that [[Start-To-Close]] timeout incorporates http timeout so that it'll fail just in case of unavailable upstream. Also, we can make sure that current [[Verify that Activity hasn't Timed-out yet|Activity hasn't Timed-out just yet]] after http request.

Another way to design the system is to make it more [[Activities Idempotence and Granularity|granular]]. Http request will fail independently of your database, and you won't have to think about two actions in one [[Activity]], and then about two clean-up actions in one [[Activity]] [[SAGA|compensation]] code.
