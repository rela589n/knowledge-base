---
aliases:
  - extra_hosts
---
Basically, what it does is that it adds entries to `/etc/hosts` file.

For example:

```yaml
	extra_hosts:
		- "host.docker.internal:host-gateway"
```

This will add `host.docker.internal` domain with host gateway ip into hosts file.

Just like this (172.17.0.1):

```hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::  ip6-localnet
ff00::  ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.1      host.docker.internal
172.26.0.5      507714518d75
```



