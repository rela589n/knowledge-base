---
aliases:
  - vespa target
---
`vespa config set target <value>` — tells the Vespa CLI where to send commands
	like `vespa deploy`, `vespa feed`, `vespa query`.

## Values

- `local` — local Docker/development instance (`localhost:19071` config, `localhost:8080` queries)
- `cloud` — Vespa Cloud
- `<url>` — custom endpoint

## Example

```sh
vespa config set target local
```

Without this, the CLI doesn't know which Vespa instance to talk to.
