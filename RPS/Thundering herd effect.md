Thundering herd effect, or why **max queue size is important**.

Suppose you have 3 servers that operate at their 100% capacity of 100 req/s:
- 100 req/s
- 100 req/s
- 100 req/s

Hence, it's 300 requests that are processed each second with the input rate of 300 req/s.

- 1s - 300
- 2s - 300
- 3s - 300

Up to this point it all works fine, but it's the last point system can operate. If we increase rate just by 1 req/second, - the system will stop operating after some time.

| Second | Input | Processed | Queued |
| ------ | ----- | --------- | ------ |
| 1      | 301   | 300       | 1      |
| 2      | 302   | 300       | 2      |
| 3      | 303   | 300       | 3      |

After some time, 300 seconds (5 minutes) to be more precise,  queue would be filled with 300 pending requests:

| Second | Input | Processed | Queued |
| ------ | ----- | --------- | ------ |
| 300    | 600   | 300       | 300    |
| 301    | 601   | 300       | 301    |

Basically at this point, if a user sends the request, it'll have [[Latency]] of two seconds, meaning that it won't be get into processing until first 600 requests from the [[Head of Line Blocking|head of line]] are processed.

Do you know how much time would it take for this number to come to 10 seconds? Let's see.

Current two second delay is caused by the fact that processing speed is 300 req/s and there are 600 incoming requests in the queue. Thus, `latency=queued/speed`. As you might've guessed, in order to get the latency of 10 seconds with the same speed of 300req/s we will solve this simple equation `10=q/300`. Hence,  `q = 10 * 300 = 3000;` in the queue must be 3000 pending requests.

In this simple example, since there already are 300 requests, it would take another 2700 requests to reach the latency of 10 seconds. With each request being added each second, it will take the same number of 2700 seconds (45 minutes) to reach this point.

As you can see, ultimately it has taken only 50 minutes of just one single additional [[Request per second|RPS]] for the system to become quite unusable.

Now, let's get back to the original system state when it consumes 300 [[Request per second|RPS]] load:
- 100 req/s
- 100 req/s
- 100 req/s

Consider something goes wrong with the third server (system fault, or temporary power outage). The rest two servers will face a **thundering herd** of 100 requests per second:

| Second | Input | Processed | Queue |
| ------ | ----- | --------- | ----- |
| 1      | 300   | 200       | 100   |
| 2      | 400   | 200       | 200   |
| 3      | 500   | 200       | 300   |

Obviously in this scenario queue grows tremendously fast - with an increasing speed of 100 [[Request per second|RPS]] per second.

How much time will it take to reach 10 seconds latency?  `latency=queued/speed`, where speed = 200 [[Request per second|RPS]], thus queue size would be 2000 requests that will come into sight in just 20 seconds!

The most frightening thing here is that even if the third server gets back at this very point, - it won't help. They all together won't be able to cope with this herd of 2000 queued requests in a reasonable time. System is already down after just a few seconds!

The only way to rescue this kind of situation when queue is already bloated with incoming requests no-one already waits the response for is to clear the queue altogether and start processing from the scratch.

Obviously, if auto-scaling is enabled, it's fundamentally not possible to get the system operating on full capacity in the first place (unless it's a ddos-attack which you did not anticipate the protection for).

But if you don't, there's also a way to prevent system from the crash. 

The solution comes down to merely limiting the incoming queue size. If the system is not able to process more than 300 [[Request per second|RPS]], it makes no sense to allow load higher than that (inferred from the evidence above). 

Let's consider metrics on per-server basis. One node is able to handle load of 100 [[Request per second|RPS]]. This implies latency of 1 second if we limit incoming queue by 100 requests.

Here's some flexibility, though. The same 100 [[Request per second|RPS]] could be expressed in various ways:
- 100 req / 1 second
- 200 req / 2 seconds
- 500 req / 5 seconds

There's no need to limit the incoming queue by the exact number of requests server could process in one second. For instance, we could set queue limit to 200 meaning that it's ok for our system to have latency of 2 seconds during the increased load period.

Le'ts consider that we stick with max queue size of 100 items. This would mean that if server gets extra 101-st request to process, - this request will be rejected.

Therefore, during the load spike we'll get the following situation:

| Second | Input | Processed | Queued | Rejected |
| ------ | ----- | --------- | ------ | -------- |
| 1      | 300   | 300       | 0      | 0        |
| 2      | 301   | 300       | 0      | 1        |
| 3      | 337   | 300       | 0      | 37       |

Not ideal for that 301-st user whose request will not be  processed, but it's far better for the system, since the complete crash because of thundering herd effect will not happen.

In case if third server suddenly crashes, only 2/3 of requests will be processed, - which is still quite a bad situation:

| Second | Input | Processed | Queued | Rejected |
| ------ | ----- | --------- | ------ | -------- |
| 1      | 300   | 200       | 0      | 100      |
| 2      | 301   | 200       | 0      | 101      |
| 3      | 337   | 200       | 0      | 137      |

If it was a temporary power outage on the third server, presumably it'll get back very soon (let's say up to a minute). Then, having the same input rate of 300 [[Request per second|RPS]], all these requests will be processed.

To conclude, there's no point to try queue up more than you are able to handle. Just reject it. Lest should you overload yourself and eventually suffer a complete crash. Even after the recovery won't you be able to handle the incoming queue.
