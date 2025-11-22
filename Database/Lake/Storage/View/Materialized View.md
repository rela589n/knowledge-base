**Materialized View** - table-like object, which stores cached results of an underlying query.

When underlying data changes, view must be refreshed.
But refreshing it on every write, it will slow down write requests.
