#TLDW

When there are **multiple replicas with no leader**, [[Version numbers|algorithm]] changes following way.

The [[Version numbers|version number]] is maintained **per each replica** **per each key**. Each replica **increments it's own version** number. Also, it **keeps versions of other replicas**.

**Version vector** - collection of **versions from all replicas**.