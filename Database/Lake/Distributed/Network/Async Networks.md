![[Shared-Nothing Architecture#^6b450e]]

**Asynchronous packet network** (Ethernet) does not provide any **guarantees** regarding **when message will arive** or whether **will it arrive** at all. In other words, [[Network Unbounded Delay|latency is unbounded]].

**Async nets** are good **for bursty traffic** (sending an email, requesting a web page, etc), but are **poor for continuous traffic** (videos). ^07b634

Networks are used for [[Network for failed nodes detection|failed nodes detection]], but not at all are they reliable. See [[Network faults]].
