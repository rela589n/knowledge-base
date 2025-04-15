`JWT_PASSPHRASE` env variable must be set before generating jwt keys, otherwise generated token will be empty.

To fix the problem, set this variable and run:
```shell
bin/console lexik:jwt:generate-keypair --overwrite
```
