Vespa is a distributed system.

Even a single-node runs multiple internal services:
- Config server (manages configuration, port 19071)
- Container (handles queries, port 8080)
- Content (stores data)
### Docker Compose Config

Specify `VESPA_CONFIGSERVERS` to a host name of the container. You shouldn't use `localhost` since on inner nodes it resolves to locahost.

Without explicit hostname → random ID (e.g. `03b8a5340ee8`) → config server unreachable.

---
