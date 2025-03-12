[[Eusphpei]]

Simple installation (for particular architecture):
```Dockerfile
COPY ./eusphpei /usr/lib/php/8.2/eusphpei
COPY ./eusphpei.ini /etc/php/8.2/mods-available/eusphpei.ini
RUN  ln -sf /etc/php/8.2/mods-available/eusphpei.ini  /etc/php/8.2/cli/conf.d/20-eusphpei.ini \
    && ln -sf /etc/php/8.2/mods-available/eusphpei.ini /etc/php/8.2/fpm/conf.d/20-eusphpei.ini \
```

Here, `eusphpei` folder contains bunch of `.so` files, and `eusphpei.ini` is just one-line file: `extension="/usr/lib/php/8.2/eusphpei/eusphpe.so"`

Installation for either amd64 or arm64:

```Dockerfile
COPY eusphpei/arm64/* /usr/lib/php/modules-arm64/
COPY eusphpei/amd64/* /usr/lib/php/modules-amd64/
COPY eusphpei/eusphpei.ini /etc/php/8.2/mods-available/eusphpei.ini

RUN ARCH=$(uname -m) \
    && mkdir -p /usr/lib/php/8.2/eusphpei \
    && if [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then \
        cp -r /usr/lib/php/modules-arm64/* /usr/lib/php/8.2/eusphpei; \
    else \
        cp -r /usr/lib/php/modules-amd64/* /usr/lib/php/8.2/eusphpei; \
    fi \
    && rm -rf /usr/lib/php/modules-arm64 /usr/lib/php/modules-amd64

RUN  ln -sf /etc/php/8.2/mods-available/eusphpei.ini  /etc/php/8.2/cli/conf.d/20-eusphpei.ini \
    && ln -sf /etc/php/8.2/mods-available/eusphpei.ini /etc/php/8.2/fpm/conf.d/20-eusphpei.ini
```

Finally, add this to docker-compose volumes:

```yaml
volumes:
  - "./docker-configs/dev/eusphpei/osplm.ini:/usr/lib/php/8.2/eusphpei/osplm.ini"
  # This volume isn't always bound correctly. Check if /data/certificates has correct certs
  - { type: bind, source: ./docker-configs/dev/configs/eusphpei/certificates/, target: /data/certificates/ }
```

Certificates folder must have `CACertificates.p7b` file. You could get it from https://iit.com.ua/download/productfiles/CACertificates.p7b.
