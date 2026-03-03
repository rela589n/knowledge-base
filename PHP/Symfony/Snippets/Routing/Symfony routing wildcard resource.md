---
aliases:
  - Symfony route wildcard resource
---
```yaml
api_frontend_auth:
    resource: '../../../**/{*FrontendApiPoint.php}'
    type: attribute
    prefix: /api/example-project/auth
    host: '%api_host%'
    schemes: '%api_scheme%'
```

