The [[Implementing Snapshot Isolation|Snapshot Isolation]] incremental transaction ids are used. In distributed systems we barely can generate **sequential ids without coordination**. If transaction A reads value written by transaction B it must have greater txid, otherwise it would be a violation of [[Causality]].

There's [[Twitter Snowflake]] approximate algorithm for sequential ids generation based on time.
![[Twitter Snowflake#^e12cfc]]

Timestamps seem to be good option at first, though [[Clocks Synchronization Issues]] lead to **each node having it's own time**, even though it may differ only by 5ms.

Also there's [[Google Cloud Spanner]] database, which implements distributed transactions **in a reliable way** using timestamp [[Clock confidence interval|confidence intervals]].