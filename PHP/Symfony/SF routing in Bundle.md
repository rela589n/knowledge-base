`YourBundle/Resources/config/routes.yaml`:

```yaml
api_frontend_feature_name:
  resource: '../../Domain/**/{*FrontendApiPoint.php}'
  type: attribute
  prefix: /api/frontend/feature-name
  host: "%api_host%"
  schemes: "%api_scheme%"
```

Then, register it in the main `routes.yaml` file:

```yaml
your_feature_routes:
  resource: '@AppYourBundle/Resources/config/routes.yaml'
```

