Setting up new follower should be done without downtime.

1. Take consistent data **snapshot from leader**;
2. **Roll out** this snapshot to new follower node;
3. The follower connects to leader and **asks log of all changes** which happened from the time when snapshot was taken (starting pointer is *log sequence number* or *binlog coordinates*);
4. Once follower processed all leader changes, it is called **caught up**.
