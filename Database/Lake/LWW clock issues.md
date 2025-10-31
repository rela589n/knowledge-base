Problems with [[LWW (last write wins)]]:
- **Writes *may disappear*** because of **lagging clock** if fast clock node just wrote the value;
- it **can't distinguish** between truly **[[Concurrent operations|concurrent writes]] and [[Happens-before relationship|dependent]]** which happened **in quick succession**, additional [[Version vectors|mechanisms]] are required to prevent violations of causality;
- two writes may have the **exact same timestamp** and it's necessary to **resolve the conflit**. 
  A **random tiebreaker** value may be used, but it also implies **data loss**.
