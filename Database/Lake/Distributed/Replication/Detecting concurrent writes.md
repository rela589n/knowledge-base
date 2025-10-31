When two clients concurrently modify the same piece of data, nodes may **receive updates in different order**.
- **Node1** may receive update ***from* client A**, 
  and **not** receive ***from* B** (due to network issue);
- **Node2** may receive first update ***from* A**, ***then from* B**;
- Node3 may receive first update ***from* B**, ***then from* A**.

[[LWW (last write wins)]] may be used for discarding concurrent writes, but **it implies data loss**. 

To handle concurrent writes sensibly, **explicit tracking of [[Capturing the happens-before relationship|dependent and concurrent]] operations** is necessary.
