**Scalability** - ability to cope with increased data and load growth. ^def-scalability

When **one node** ***can't handle*** data volume, r/w load,
it can be ***spread*** *across* **multiple nodes**.
#### Measurements

- for **Describing The Load** [[Load Parameters]] are used;
- for **Describing Performance** [[Percentiles]] are used.

#### Handling the Load

**[[Shared-Nothing Architecture]]** - multiple **machines distribute the load** among each other.

**Elastic systems** - which can **add resources** when **load is increased**. They are useful when load **increase is not predictable**, unlike manual scaling.

**Factors** to take into account when **designing the architecture**: 
- volume of **reads/writes**;
- **volume of data**;
- **response time** reqs.

For instance, application which has to handle 100k req/sec with req of 1kB will be designed differently than app which has to handle 3 req/min, but with request of 2GB, though data throughput is the same.
