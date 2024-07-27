There are **deliberate nodes-liars**, see **[[Byzantine faults]]** for details. Usually web-apps do **not implement** such protectoin since usually all nodes are controlled by a single organization.

Also, there are **weak forms of lying**:
- network **packets may be corrupted** by driver/OS/hardware bugs. Simple **checksums in app protocols** may be used;
- **clients may send malicious requests**, therefore input validation, range limiting, sanitizing, sanity checks, output escaping is necessary;
- NTP clients detect servers-outliers and exclude them from synchronization.
