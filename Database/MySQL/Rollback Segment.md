In [[MySQL]] when data is updated, the update happens in-place. 
Before update actually happens, row is written to the [[Rollback Segment]].

If some other transactions still need to reference previous [[MVCC]] version, they'll use one from Rollback Segment.
