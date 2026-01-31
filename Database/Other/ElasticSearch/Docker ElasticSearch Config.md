TEST it!

```yaml
    elastic:
        image: elasticsearch:9.0.1
        ports:
            - "127.0.0.1:9200:9200"
            - "127.0.0.1:9300:9300"
        environment:
            # Increase JVM heap size to prevent out-of-memory errors
            ES_JAVA_OPTS: "-Xms512m -Xmx512m"
        volumes:
            - "elastic_data:/usr/share/elasticsearch/data"
```