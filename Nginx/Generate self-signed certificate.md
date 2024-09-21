```shell
openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout privateKey.key -out certificate.crt
```

Common name (CN) must be as `localhost`.
