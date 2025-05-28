[[Activity|Activities]] are guaranteed to have **at least one execution**. 

Thus, they should be **[[Idempotence|idempotent]]** ([[Activity ID]]), because they can be retried. If activity was successfully executed by [[Worker]], but [[Server|Temporal Service]] has failed just before confirmation, it'll be re-executed.

[[Activity|Activities]] should be **granular**, because if one has multiple parts that can fail independently, retrying the activity will cause retry for all of them.
