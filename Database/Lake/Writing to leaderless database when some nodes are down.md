The client sends **Quorum Write** to all replicas. Say, if 2/3 databases accepted the write, it is considered successful.

The client sends **Quorum Read** to all replicas as well. The results may differ (some values are up-to-date, others are stale or absent). **Version numbers** are used to **determine latest values**.

See:
- [[Leaderless Read-repair and anti-entropy]];
- [[Quorums for reading and writing]];
- [[Sloppy quorums and Hinted Handoff]];

