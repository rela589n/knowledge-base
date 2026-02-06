---
aliases:
  - vespa-deploy
---
**Deploy** - apply application configuration to Vespa.

See [text-search tutorial](https://docs.vespa.ai/en/learn/tutorials/text-search.html#deploy-the-application-package)

## From Inside Container

```bash
docker compose exec -it vespa bash
```

### Prepare (validate config)

```bash
vespa-deploy prepare /app
```

### Activate (apply config)

```bash
vespa-deploy activate
```

## Via REST API

```bash
zip -r - . | curl --header "Content-Type: application/zip" \
  --data-binary @- \
  http://localhost:19071/application/v2/tenant/default/prepareandactivate
```

## Verify the Deployment

```bash
curl http://localhost:8080/state/v1/health
```

Port 8080 only becomes available after successful deployment.
