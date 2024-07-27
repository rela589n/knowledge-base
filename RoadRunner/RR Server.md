[[RR Single entry point]]

The server is capable of nothing by itself w/o [[RR plugins]] .

```yaml
version: '3'  
server:  
    # RR uses a single server approach
    # This server could only handle incoming http requests
    # If something else (like queued processing) is needed, then server.command
    # should contain a php file that could handle both types of requests (depending on incoming RR_MODE env)
	command: "php server.php"
```

In order to handle at least some requests, plugins are required:

```yaml
http:
  address: 0.0.0.0:8080
```

This makes RR server available via HTTP. Note that `server.php` must be capable of HTTP requests processing. 

See https://github.com/rela589n/roadrunner-http as an implementation example.

