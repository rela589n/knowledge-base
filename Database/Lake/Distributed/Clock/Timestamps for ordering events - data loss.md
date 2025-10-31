In distributed databases ([[Multi-Leader Replication|Multi-Leader]] and [[Leaderless Replication|Leaderless]]) [[Happens-before relationship|Dependent]] operations may resolve conflicts by [[LWW (last write wins)]] strategy.

On some nodes it is possible that **former write will overwrite dependent latter**, meaning **data loss**. See [[LWW clock issues]].
