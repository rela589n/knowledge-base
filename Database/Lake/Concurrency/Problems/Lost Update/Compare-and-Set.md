Updates add **where conditions** *that* ***check* old state**.
Update happens only if old state's the same.
If no rows were updated, the operation should be retried.

Useful when **DB doesn't support [[Transaction|Transactions]]**.

It might not be safe, ***depending on* the internals *of* DB**. 
If it compares where conditions on an old snapshot, but runs the update on already updated data, this will raise an issue.
