If **DB doesn't provide a transactions**, we may detect lost read from our side using **compare-and-set** approach.

Update statement will add **where conditions to check old data state**, therefore update will not apply if old state was changed. Therefore, if no rows were updated, then operation flow should be retried.

It may not be safe, and **depends on internals of DB**. If DB compares where conditions on old snapshot, but runs the update on already updated data, this may be an issue.
