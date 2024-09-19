Commonly, web servers provide the configuration for:
- number of workers;
- [[max queue size]].

Configuration of q size would allow us to withstand an increase of load ([[Load spike]]) for a short period of time.

In order to calculate it, we'd need:
- normal server [[Request per second|RPS]];
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

Server [[Request per second|RPS]] would be `RPS = n_workers / serv_res_time`
Hence, the speed of 16 workers is: `16 / 0.5 = 32rps`

In order to have [[Client-side response time]] within 3 seconds limit, it should be multiplied by 32rps: `q_size = 3 * 32 = 96`

Therefore, if we have [[Third quartile|p75]] [[Server-side response time]] as 0.5 seconds and [[Max queue size]] as 96, the max [[Third quartile|p75]] [[Client-side response time]] would be at most 3 seconds.

It doesn't necessarily mean that no users will ever wait for longer than 3 seconds. Due to [[Head of Line Blocking]], there could be one request lasting 10 seconds just because it takes some time to process. Some other request would need to wait for it to complete. Though, in [[Third quartile|p75]] perspective, given configuration provides [[Client-side response time]] as 3 seconds.

What will happen if system operates on 32 RPS (100% capacity) and then load increases to 33 RPS (103%)? After 96 seconds queue will become full and every second one unlucky request will be dropped. The overall [[Client-side response time]] in p75 of cases will increase to around 3 seconds instead of 0.5. Yet, there are still [[First quartile|p25]] that could experience response time of more than 3 seconds.

 The overall [[Client-side response time]] in p75 of cases will increase to around 3 seconds instead of 0.5. Yet, there are still [[First quartile|p25]] that could experience response time of more than 3 seconds.