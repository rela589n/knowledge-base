Check out access control:

```yaml
access_control:
    - { host: '%api_host%', route: api_project_oauth2_token, roles: PUBLIC_ACCESS }

    - { host: '%api_host%', route: api_project_file_read, roles: PUBLIC_ACCESS }
```