[[Activity]] [[Forward Compatibility]].

When activity code is older than a newly deployed worker code (this can be if workers are provisioned gradually - some have already been updated, others are going to be updated).

Change from `int $scalar` into `AppCommand` that encloses that scalar is possible after the full upgrade. Actually, upgrade will auto-correct the problem.

Therefore, no [[Forward Compatibility]]. 
Take a look at [[Activity Execution Failure#^8c045a]].
