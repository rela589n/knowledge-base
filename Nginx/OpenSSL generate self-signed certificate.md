```shell
openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout privateKey.key -out certificate.crt
```

Common name (CN) must be as `localhost`.

You can append this param to skip interactive questions:

```shell
-subj "/C=AU/ST=Some-State/O=Internet Widgits Pty Ltd/CN=localhost"
```