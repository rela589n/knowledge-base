In distributed systems we **can't know anything for sure**, as we **don't have direct access** to other nodes. The only way **information** about particular node **can be received** - via **network messages or their absence**. Therefore [[Truth is defined by majority]].

## Knowledge about locks

One particular node may want to have a lock on something:
- **[[Leader lease|lease lock]]** in single-leader replication;
- lock for a particular **resource** (object, file, row);
- lock on a username (**unique constraint**).

Even though node thinks it is the owner of the lock, it may not be true anymore if [[Process Pauses|process was paused]]. Usually this leads to **two nodes performing modifications** as if they both hold the lock, leading to ***corrupted state***. ^12c90c

The **solution** lies down in **[[Fencing tokens]]**.




