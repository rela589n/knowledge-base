---
aliases:
  - RoadRunner entry point
---
[[RoadRunner]] defines single server that runs a php file for every and all types of incoming requests.

The server is capable of nothing by itself w/o [[RR plugins]].

```yaml
version: '3'  
server:  
    # RR uses a single entry point approach
    # This server could handle either incoming 
    # http requests or queued processing or anything
    # else (then server.command should contain a single
    # php file that could handle all types of incoming
    # requests depending on RR_MODE env
	command: "php server.php"
```

In order to handle at least some requests, plugins are required:

```yaml
http:
  address: 0.0.0.0:8080
```

This makes RR server available via HTTP. Note that `server.php` must be capable of HTTP requests processing. 

See https://github.com/rela589n/roadrunner-http as an implementation example.
