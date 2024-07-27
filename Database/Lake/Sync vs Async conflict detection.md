The conflict is detected later on asynchronously, and it may be **too late to ask the user to resolve the conflict**.

If we would stick to sync conflict detection, we will **lose the independence of leaders**. This is the same as if we had a single leader replication.
