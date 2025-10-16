The client application may have the requirement of offline operation. Then every device will have it's own leader database. Once back online, databases are synchronized. The replication lag may be several hours or even days.

> As the rich history of broken calendar sync shows, multi-leader replication is a hard thing to get right.

[[CouchDB]] is designed to make multi-leader configuration easier.