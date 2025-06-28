Model aggregate and inner entities.
Make sure that inner entities are partitioned by the parent id.
Insert few thousand aggregates, and few million inner entities.
Analyse performance of inner queries, and compare it to ordinary approach with just two tables.
That's actually interesting story about Composition. It would be cool if it worked better because only one particular predetermined table is needed to be scanned, not the whole table.