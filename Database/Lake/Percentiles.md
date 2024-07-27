![[Latency]]

**Median measure** is more important than arithmetic average. For instance if we take into account response time, median 100ms would mean that 50% of all requests are completed within 100ms limit. Median is **50-th percentile**. There can also be **90-th percentile**, **95-th**, **99.9-th percentiles**.

**Service level objectives** (**SLO**) describe **expected performance** of the service.
**Service level agreements** (**SLA**) describe **expected availability** of the service.

**SLO** & **SLA** usually are **described in percentiles**.

![[Head of Line Blocking]]

#### Percentiles in practice

![[Tail Latency Amplification]]

Algorithms to evaluate percentiles are described here: forward decay [25], t-digest [26], or HdrHistogram [27].
