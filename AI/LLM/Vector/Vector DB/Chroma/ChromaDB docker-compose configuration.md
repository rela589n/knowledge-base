```yaml
services:
    chromadb:
        image: chromadb/chroma:1.4.1
        ports:
            - "127.0.0.1:8002:8000"
        environment:
            IS_PERSISTENT: "TRUE"
            ANONYMIZED_TELEMETRY: "FALSE"
        volumes:
            - chromadb_data:/chroma/chroma
        healthcheck:
            test: ["CMD", "curl", "-f", "http://localhost:8000/api/v2/heartbeat"]
            interval: 30s
            timeout: 10s
            retries: 3

volumes:
    chromadb_data: ~
```