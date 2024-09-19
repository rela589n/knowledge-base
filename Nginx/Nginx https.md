> Make sure you have disabled cache when testing request from your browser

Use following config to enable https:

```
listen 443 ssl http2;  

ssl_certificate         /opt/ssl/certificate.crt;  
ssl_certificate_key     /opt/ssl/privateKey.key;
```

#### HTTPS header (*very important*)

Symfony framework uses `HTTPS` header to define the request scheme.

In order to make nginx pass this param, add this config:

```conf
fastcgi_param  HTTPS     $https if_not_empty;
```
