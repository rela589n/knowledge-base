**StatefulSet** is similar to [[Deployment]], but it's meant to manage **stateful [[POD]]s**.

It manages the **access** to the **persistent storage** (defines when and which [[POD]]s can read and write). 

![[StatefulSet.png]]

Often DB is externalized since it's tedious to configure DB in [[Kubernetes|K8s]].
