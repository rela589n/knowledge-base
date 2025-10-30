Commonly, web servers provide the configuration for:
- number of workers;
- [[Max queue size]].

Proper configuration of queue size would allow us to withstand an increase of load ([[Load spike]]) for a short period of time.

In order to calculate it, we'd need to know:
- normal server [[Request per second|RPS]] capacity;
- desired [[Service level objectives|Service level objective]];

Server [[Request per second|RPS]] could be obtained from two parameters :
- number of workers;
- [[Server-side response time]] (for some [[Percentiles|percentile]]).

`RPS = n_workers / serv_res_time`

Let's consider the example.

Given that:
- [[Server-side response time]] ([[Third quartile|p75]]): 0.5 seconds  
- number of workers: 16

Objective - calculate max queue size to:
- have worst admissible [[Client-side response time]]: 3 seconds.

In this example, max queue size would be the number of requests `n_workers` (16 workers) can handle within `client_res_time` 3 seconds.

Server [[Third quartile|p75]] [[Request per second|RPS]] would be `RPS = n_workers / serv_res_time`
Hence, the speed of 16 workers is: `16 / 0.5 = 32rps`

In order to have [[Client-side response time]] within 3 seconds limit, it should be multiplied by 32rps (`q_size = client_res_time * RPS`) as this: `q_size = 3 * 32 = 96`

Therefore, if we have [[Third quartile|p75]] [[Server-side response time]] as 0.5 seconds and [[Max queue size]] as 96, the max [[Third quartile|p75]] [[Client-side response time]] would be at most 3 seconds.

It doesn't necessarily mean that users will never wait for longer than 3 seconds. There could be one request (belonging to these top [[First quartile|p25]] requests not included) lasting for 10 seconds just because it alone takes some time to process. Some other requests (up to 20 of them if we consider [[Third quartile|p75]] scenario) would need to wait for this one to complete if there are no other workers available (due to [[Head of Line Blocking]]). Yet, in [[Third quartile|p75]] perspective, given configuration should provide [[Client-side response time]] as 3 seconds during the high load period.

What will happen if system operates on 32 RPS (100% capacity) and then load increases to 33 RPS (103%)? After 96 seconds queue will become full and each second a signle unlucky request will be dropped. 

The overall [[Client-side response time]] for p75 of requests will increase to ~3 seconds instead of ~0.5. Yet, there are still [[First quartile|p25]] that could experience response time of more than 3 seconds. How far the [[Client-side response time]] for these requests above [[Third quartile|p75]] would deviate from 3 seconds will initially actually depend on how desired [[Percentiles|percentile]] of initial  [[Server-side response time]] deviates from [[Third quartile|p75]] used in these calculations.

Once again, these calculations are for [[Third quartile|p75]], meaning that 3 seconds response is not the typical one, since [[Typical Response Time]] is [[Median percentile]], - and this is going to be less than 3 seconds. 

To understand the typical response time in this configuration, the same formula cold be used `client_res_time = q_size / RPS`.

If we consider the same `q_size=96` and have measurements of [[Server-side response time]] `RPS` for [[Median percentile|p50]], say `64` (for the response time of `0.25s`, since `16/0.25=64`), then  `client_res_time = 96 / 64 = 1.5s`.

Therefore, for the given system under given configuration of `q_size=96` typical request performance under peak load would be `1.5 seconds`, while [[Third quartile|p75]] performance would be `3 seconds`.
Under given circumstances the system is likely to withstand the load w/o being too sluggish to the end users.

> The optimal approach for calculating the [[Max queue size]] is to check the [[Server-side response time]] [[Percentiles]] distribution chart of the system, and then take the decision about [[Client-side response time]] boundaries.
