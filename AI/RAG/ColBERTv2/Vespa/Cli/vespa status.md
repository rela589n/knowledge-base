---
aliases:
  - vespa health check
---
`vespa status` — checks if a Vespa component is up and responding.

## Variants

- `vespa status` — pings the **container** (`localhost:8080`)
- `vespa status deploy` — pings the **config server** (`localhost:19071`)

## Flags

- `--wait <seconds>` — keep retrying until ready or timeout
  Useful right after starting a Docker container
    since Vespa takes time to boot.

## Typical Startup Sequence

```sh
docker run ... vespa            # start container
vespa status deploy --wait 300  # wait for config server to be ready
vespa deploy app-package        # now safe to deploy
vespa status                    # wait for container to serve requests
```
