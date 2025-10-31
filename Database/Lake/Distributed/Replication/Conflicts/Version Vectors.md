#TLDW

When there are **multiple [[Replica|Replicas]] with no leader**, [[Version Numbers]] algorithm changes following way.

The [[Version Numbers|Version Number]] is maintained **for each [[Replica]]** **for each key**. 

Each [[Replica]] **increments it's own version** number.  

Each [[Replica]] **keeps versions of other [[Replica|Replicas]]**.

**Version vector** - collection of **versions from all [[Replica|Replicas]]**.