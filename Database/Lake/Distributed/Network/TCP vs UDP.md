UDP removes some of [[Network variability|delay entropy reasons]]:
- it doesn't use [[Network backpressure|flow control]].
- it doesn't [[TCP retransmission timeouts|retry lost packets]].

Actually UDP is acceptable when delayed packets are worthless (voice-, video-conferencing). Packet retries are done at human level if necessary ("The sound just cut out for a moment").