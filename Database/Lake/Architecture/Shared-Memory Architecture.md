**Shared-Memory Architecture** - using multiple **joined components** (CPUs, RAM, disks) that are ***treated as* single machine**. 

#### Limited [[Availability|Fault Tolerance]]
We might replace hot-swappable components (memory modules, CPU, disks) w/o shutdown.

#### Limited [[Scalability]]
**Cost increase *isn't proportional to* the resource increase**. Scaling twice is increasing cost more than twice. Besides that, due to **bottlenecks**, 2x system won't handle 2x load.

