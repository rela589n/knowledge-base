Testing tool that allows to make a bunch of http requests to your backend.

```shell
sudo apt-get install apache2-utils
```

Basic GET test:
```shell
ab -n 1000 -c 16 https://your-api-endpoint
```

Basic POST test:
```shell
ab -n 1000 -c 32 -p requestBody.json -T application/json https://your-api-endpoint
```
