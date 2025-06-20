It's possible to use [docker image](https://hub.docker.com/r/temporalio/ui).

Here's how to do it:

```shell
docker run -p 8080:8080 --add-host host.docker.internal=host-gateway -e TEMPORAL_ADDRESS=host.docker.internal:7233 temporalio/ui:v2.38.3
```

Make sure that 7233 port is available for connection from docker container (it won't be, if it's forwarded as 127.0.0.1:7233)

Another option is to use host network:

```shell
docker run --network=host -e TEMPORAL_ADDRESS=127.0.0.1:7233 -e TEMPORAL_UI_PORT=8001 temporalio/ui:v2.38.3
```

Connecting to existing [[Docker]]-deployed [[Temporal Server]]:

```shell
docker run -p 8001:8080 --network=example-project_default -e TEMPORAL_ADDRESS=temporal:7233 temporalio/ui:v2.38.3
```

