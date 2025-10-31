The conflicts must be resolved in a **[[Convergence|Convergent]]** way:
- [[LWW (last write wins)]] (data loss);
- give each leader an ID, and let the **writes *of***  **higher-ID [[Replica|Replicas]] win**;
- **merge values** - maybe order and concat;
- ***record*** the **conflict** and *let* the **application code**  resolve it later (possibly by ***prompting*** the **user**). 
