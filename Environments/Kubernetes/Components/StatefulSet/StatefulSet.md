**StatefulSet** is similar to [[Deployment]], but it's meant to manage **stateful [[POD]]s**.

It manages the **access** to the **persistent storage** (when which [[POD]]s can read and write). 

![[StatefulSet.png]]

It's tedious to configure DB in [[Kubernetes|K8s]], and that's why often DB is externalized.