Thundering herd effect, or why **max queue size is important**.

Suppose that you have 3 servers that operate at their 100% capacity of 100 req/s:
- 100 req/s
- 100 req/s
- 100 req/s

Hence, it's 300 requests that are processed every second with the input rate of 300 req/s.

- 1s - 300
- 2s - 300
- 3s - 300

Up to this point everyting works fine, but on the very edge. If we increase the input rate just by 1 req/second, - the system will crash after some time.

| Second | Input | Processed | Left |
| ------ | ----- | --------- | ---- |
| 1      | 301   | 300       | 1    |
| 2      | 302   | 300       | 2    |
| 3      | 303   | 300       | 3    |

Given that input rate is 301 req/s, while we able to process only 300 req/s, we'd have 1 request left for each second.

After some time, 300 seconds (5 minutes) to be more precise,  queue would be filled with 300 pending requests:

| Second | Input | Processed | Left |
| ------ | ----- | --------- | ---- |
| 300    | 600   | 300       | 300  |
| 301    | 601   | 300       | 301  |

Basically at this point, if a user sends the request, it'll have the [[Latency]] of two seconds, because it won't be taken for processing until that pending 600 requests from the [[Head of Line Blocking|head of the line]] are processed.

Do you know how much time would it take for this number to come to 10 seconds (completely unusable system)? Let's see.

Current two second delay is caused by the fact that our processing speed is 300 req/s and there are 600 incoming requests in the queue. 
Therefore, we can see that `latency=queued/speed`, and as you might've already guessed, in order to get the latency of 10 seconds with the same processing capacity of 300 req/s we just need to solve this simple equation `10=q/300`. Thereby,  `q = 10 * 300 = 3000;`, meaning that for 10 seconds latency the queue must have 3000 pending requests.

In this simple example, since there already are 300 requests, it would take another 2700 requests to reach that latency. With each request being added each second, it will take the same number of 2700 seconds (45 minutes) to take place.

From the outset, it has taken only 50 minutes of just one single additional [[Request per second|RPS]] for the system to become almost unusable. And you know that for 5 seconds latency, it would have taken twice as less - 25 minutes.

Now, let's get back to the original system state when it consumed 300 [[Request per second|requests per each second]]:

- 100 req/s
- 100 req/s
- 100 req/s

Consider that something goes wrong with the third server (system fault, or temporary power outage) so that it becomes unusable, or needs restart. Two other servers will face a **thundering herd** of 100 [[Request per second|RPS]] rushing out from the third server to these two:

| Second | Input | Processed | Left |
| ------ | ----- | --------- | ---- |
| 1      | 300   | 200       | 100  |
| 2      | 400   | 200       | 200  |
| 3      | 500   | 200       | 300  |

Well, that escalated quickly! In this case, queue grows tremendously fast - with an increasing speed of 100 [[Request per second|requests per second]].

What will it take to reach 10 seconds latency?  `latency=queued/speed`, where speed = 200 [[Request per second|RPS]], thus it takes 2000 requests, which would pile up in just 20 seconds!

The most frightening thing here is that even if the third server gets back at this very point, - it just won't help. These three tiny servers won't be able to cope with this massive herd of 2000 queued requests. System is already down in a matter of seconds!

> That's a good reason not to deploy anything when your system is operating at it's maximum.

There's only way to rescue this kind of a situation, and that is to clear the queue altogether and start processing from new requests. Most of the currently queued requests, being for a long time in the queue, are not awaited by anybody anyway, therefore it's better to drop them.

Obviously, if auto-scaling is enabled, it's not possible to get the system operating on full capacity in the first place (unless it's a ddos-attack which you did not anticipate the protection for).

But if you don't, there's also a way to prevent system from the crash.

The solution comes down to merely limiting the incoming queue size. If we know that the system is not able to process more than 300 [[Request per second|RPS]], it makes sense not to allow higher load than this (inferred from the evidence above).

Let's consider metrics on per-server basis. One node is able to handle 100 [[Request per second|RPS]] load. If we limit the incoming queue by 100 requests, we'll get the max latency of 1 second.

Yet, there's some flexibility, though. 

The same 100 [[Request per second|RPS]] could be expressed in various ways:
- 100 req / 1 second
- 200 req / 2 seconds
- 500 req / 5 seconds

There's no need to limit queue size by the exact number of requests server could process in one second. Instead, we could set limit to 200, meaning that it's ok for our system to have latency of 2 seconds during the peak load.

Le'ts say that we stick with max queue size as 100. It means that server will drop that 101-st request.

Therefore, during load spike we'll get the following situation:

| Second | Input | Processed | Left | Rejected |
| ------ | ----- | --------- | ---- | -------- |
| 1      | 300   | 300       | 0    | 0        |
| 2      | 301   | 300       | 0    | 1        |
| 3      | 337   | 300       | 0    | 37       |

Not ideal for that user of 301-st request, since it will not be  processed, but it's far better for the system, since it prevents it from the complete crash.

In case if third server suddenly crashes, only 2/3 of requests will be processed.

| Second | Input | Processed | Left | Rejected |
| ------ | ----- | --------- | ---- | -------- |
| 1      | 300   | 200       | 0    | 100      |
| 2      | 301   | 200       | 0    | 101      |
| 3      | 337   | 200       | 0    | 137      |

Though this is quite a bad situation, if it is only a temporary outage of the third server, hopefully it will be back soon, so that every processing will continue normally (at input rate = output rate = 300 [[Request per second|RPS]]).

It's worth mentioning that if your system operates at 67% of it's capacity, without proper configuration of the queue size, it's a dangerous state to be in. If only just one server crashes, or reboots, it will lay down the whole system just because of 1 extra [[Request per second|RPS]] that two servers could not keep up with.

To conclude, there's no point in trying to queue up more than you can handle. Just reject that what is above the limit, lest eventually you should overload yourself and suffer a complete crash. Even after recovery won't you be able to handle the incoming queue.
