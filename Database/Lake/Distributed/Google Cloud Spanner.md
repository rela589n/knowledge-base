**Spanner** - distributed database with [[Snapshot Isolation]] transactions.

For snapshot isolation transactions, it uses [[Google TrueTime]] api. If two ranges `[A1, B1]`, `[A2, B2]` do not overlap, then either is greater than another, meaning happened before. Only if intervals overlap we don't know what happened before.

[[Google Cloud Spanner]] ensures that transaction **intervals do not overlap**. For each transaction it **deliberately waits for the length of [[Clock Confidence Interval|confidence interval]]**.

