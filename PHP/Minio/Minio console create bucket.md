```shell
# Download MinIO Client (mc)
sudo curl -O https://dl.min.io/client/mc/release/linux-amd64/mc
sudo chmod +x mc
sudo mv mc /usr/local/bin/

# Configure MinIO client
sudo mc alias set local http://minio:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD

# Create bucket (if not exists)
sudo mc mb local/bucket-name || true

# Check MinIO availability via healthcheck after bucket creation
curl -v http://minio:9000/minio/health/live || { echo "MinIO is unavailable"; exit 1; }
```
