---
aliases:
  - kubernetes-cli
---
**kubectl** is a CLI for [[Cluster]].

![[kubectl commands.png]]
![[kubectl commands - 2.png]]

###### `kubectl get nodes`:

```shell
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   19m   v1.33.1
```

###### `kubectl create deployment ngninx-dep --image nginx`:

```shell
deployment.apps/ngninx-dep created
```

###### `kubectl get deployments`:

```shell
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
ngninx-dep   1/1     1            1           8m24s
```

###### `kubectl get pods`

```shell
NAME                          READY   STATUS    RESTARTS   AGE
ngninx-dep-75fd6f9d87-w8k7j   1/1     Running   0          9m36s
```

###### `kubectl edit deployments ngninx-dep `

> Use `KUBE_EDITOR="nano"` prefix

Change image, replicas count.

###### `kubectl get replicasets`

Updated the config, everything else is updated automatically.

```shell
NAME                    DESIRED   CURRENT   READY   AGE
ngninx-dep-75fd6f9d87   0         0         0       20m
ngninx-dep-79497d4798   2         2         2       86s
```

###### `kubectl logs ngninx-dep-79497d4798-d8bxq`

It shows the logs of the container.

```shell
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
```

###### `kubectl describe pod ngninx-dep-79497d4798-d8bxq`

It shows information about the [[POD]] itself, including the events:

```shell
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  7m12s  default-scheduler  Successfully assigned default/ngninx-dep-79497d4798-d8bxq to minikube
  Normal  Pulling    7m11s  kubelet            Pulling image "nginx:1.28"
  Normal  Pulled     7m4s   kubelet            Successfully pulled image "nginx:1.28" in 7.101s (7.101s including waiting). Image size: 192480094 bytes.
  Normal  Created    7m4s   kubelet            Created container: nginx
  Normal  Started    7m4s   kubelet            Started container nginx
```

###### `kubectl exec ngninx-dep-79497d4798-d8bxq -it -- bash`

You'll get into the [[Container]] of that [[POD]].

###### `kubectl delete deployment ngninx-dep`

```shell
deployment.apps "ngninx-dep" deleted from default namespace
```

Deployment deleted, all the replicasets and [[POD]]s were deleted.

###### `kubectl apply -f nginx-deployment.yaml`

This command applies the configuration from the file, adjusting the [[Cluster]] to a desired state.

