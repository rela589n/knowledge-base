See also: https://medium.com/the-sensiolabs-tech-blog/how-to-use-xdebug-in-docker-phpstorm-76d998ef2534

Make sure [[Docker Default Bridge Gateway|docker host-gateway]] is included in [[Docker extra hosts|extra_hosts]].

Then, verify you can connect to phpstorm:

```shell
telnet host.docker.internal 9003
# or
nc -zv host.docker.internal 9003
```

You should see:
```
Connection to host.docker.internal (172.17.0.1) 9003 port [tcp/*] succeeded!
```

Then, you could add environment configuration to container itself:

```yaml
environment:
	XDEBUG_CONFIG: 'client_host=host.docker.internal'
```

When debugging, PHP script connects to IDE by 9003 port so that it could start debug session. Then IDE must match path mapping with the local paths (e.g /app from docker with /home/your-project/path). 

It does not use mappings defined in PHP Interpreter options, because PHP Interpreter is used to run code from within the IDE, while debug connection happens from outside of IDE, so that it doesn't know that it's the same.

If we ran the same script from IDE (Run Configurations), it would have been IDE that triggered script, so it would have already knew that mappings could be taken from Interpreter options. Actually, it adds `"XDEBUG_CONFIG" => "idekey=18203"` environment when running script, so that it will be used when PHP script hits debug, so that PhpStorm would know the correct way to match it.

> Cannot find file '/app/bin/console' locally.
> To fix it set server name by environment variable PHP_IDE_CONFIG and restart debug session.

This issue is because PhpStorm could not match the path from debugger with it's project. To fix it, create server in PHP -> Servers:

![[Xdebug server.png]]

And add `PHP_IDE_CONFIG` environment to the docker:

```yaml
environment:
    PHP_IDE_CONFIG: "serverName=example-project-docker"
```

Therefore, when debug session will be started, PhpStorm will know that `PHP_IDE_CONFIG` contains correct server name, and it will use it to find out what path mapping are needed.

Finally, my `xdebug.ini` file looks like this:

```ini
[xdebug]
; use xdebug.mode=debug to debug from browser
; prepend XDEBUG_MODE=debug to console command to start debugging
xdebug.mode=develop
xdebug.client_host=host.docker.internal
xdebug.start_with_request=yes
xdebug.log=/app/var/log/xdebug.log
```

