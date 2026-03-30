```yaml
security:
  providers:
    third_party_users:
      memory:
        users:
          your_third_party:
            password: '%env(APP_THIRD_PARTY_USER_PASSWORD)%'
            roles: [ 'ROLE_THIRD_PARTY_USER' ]
  firewalls:
    third_party:
      pattern: ^/api/v1.0/third-party
      stateless: true
      provider: your_third_party
      host: "%api_host%"
      http_basic: ~

  access_control:
    - { host: "%api_host%", path: ^/api/v1.0/third-party/endpoint, roles: ROLE_THIRD_PARTY_USER }
```

Then, on login, do:
```
Authorization: Basic base_64_encoded{login:password}
```

In `APP_THIRD_PARTY_USER_PASSWORD` there must be hashed with 

```shell
bin/console security:hash-password
```

