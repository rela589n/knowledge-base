**Queuing in networks**:
- **on switch the links are queued**, as far as packets are 
passed one by one ([[Network congestion|net congestion]]). Some packets may be even dropped if queue fills up;
- when recepient is busy, **operating system queues packets** to process them when it'll have time;
- when using VMs, it is often that VM pauses while another VM uses CPU, in this case **VM monitor queues packets**.
- **TCP uses [[Network backpressure|backpressure]]** (queuing **on sender side**) to reduce the [[Network congestion|net congestion]].
