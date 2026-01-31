
| Aspect         | Expiration               | Validation          |
| -------------- | ------------------------ | ------------------- |
| Server contact | None until cache expires | Every request       |
| Response       | Full content (200)       | Minimal check (304) |
| Data freshness | Can be stale             | Always verified     |

### [Expiration Model](Expiration%20Model.md)

"Trust the cache for X time, don't ask me"
- Cache serves stored responses without contacting server
- Headers: `Cache-Control`, `Expires`

### [Validation Model](Validation%20Model.md)

"Always ask me, but I'll tell you if nothing changed"
- Cache always validates with server
- Server can respond with 304 Not Modified (no body)
- Headers: `ETag`, `Last-Modified`

## Best Practice

Combine both models:
- Expiration for predictable static content
- Validation for dynamic content that may change unexpectedly
