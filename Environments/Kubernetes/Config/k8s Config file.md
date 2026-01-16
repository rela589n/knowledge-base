**Configuration file** stores the **options** which would otherwise be manually written for [[kubectl]].

Best practice is keeping it **with the code**.

Config is made of these **parts**:
- **metadata**
- **specification**
- **status** (auto-generated, comes from [[etcd]])

[[Kubernetes|K8s]] checks if the status meets the spec.
If not, it fixes that, [[Scheduler|Scheduling]] what's needed.
