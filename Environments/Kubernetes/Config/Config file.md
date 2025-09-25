**Configuration file** stores the **options** which otherwise had to be manually written in [[kubectl]].

Best practice is keeping it **with the code**.

Config is made of these **parts**:
- **metadata**
- **specification**
- **status** (auto-generated, comes from [[etcd]])

[[Kubernetes|K8s]] checks that the status meets the spec. If not, it fixes that.