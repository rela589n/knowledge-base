**Byzantine fault** - one that is **because of traitor nodes** in the system. Deceiving node may deliberately send fake [[Fencing tokens]], therefore lying to the system.

**Byzantine fault-tolerant system** continues operating correctly even if some nodes are not obeying to the protocol or malfunctioning.

Utility of Byzantine fault protection:
- in systems, **where faults are too expensive** (aircrafts, rockets). CPU or memory may get corrupted by radiation, leading to unpredictable responses to other nodes;
- systems with multiple organizations where some **participants may attempt to defraud** each other (blockchain).

**Bug in software** may be considered as a Byzantine fault. If same software is deployed to all nodes, then **whole system may be compromised**.

To prevent software Byzantine bugs:
- different implementations on different nodes (too expensive);
- traditional protection mechanisms (ACL, firewalls, encryption, authorization).
