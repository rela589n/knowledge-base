Command Query Responsiblity Segregation - is a pattern that segregates (sets appart) write operations (Commands) from read operations (Queries) so that two could even be implemented on top of different storages.

CQRS is often used with [[Replication]] (when there's high read-write asymmetry) and sometimes [[Event Sourcing]].

https://martinfowler.com/bliki/CQRS.html