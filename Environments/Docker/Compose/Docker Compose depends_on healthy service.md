```yaml
depends_on:
	postgresql: { condition: service_started }
	temporal: { condition: service_healthy }
```

