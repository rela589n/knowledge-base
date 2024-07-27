In distributed databases (specifically [[Multi-Leader Replication]] and [[Leaderless Replication]]) [[Happens-before relationship|dependent]] operations may resolve conflicts by [[LWW (last write wins)]] strategy.

On some nodes it is possible that **former write will overwrite dependent latter**, meaning **data loss**. See [[LWW clock issues]].

It is possible to make [[LWW (last write wins)]] more reliable by usage fo [[Logical clocks]], which are based on incremental counters.

