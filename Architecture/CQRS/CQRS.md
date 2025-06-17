---
aliases:
  - Command Query Responsiblity Segregation
---
Command Query Responsiblity Segregation - is a pattern that segregates (sets apart) write operations ([[Command|Commands]]) from read operations ([[Query|Queries]]) so that two can even be implemented with different storages.

CQRS is often used with [[Replication]] (when there's high read-write asymmetry) and sometimes [[Event Sourcing]].

https://martinfowler.com/bliki/CQRS.html