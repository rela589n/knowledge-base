**Deployment** is a blueprint for spawning **stateless [[POD]]s**. 
You can **replicate [[POD]]s**, scale up, and scale down.

> To replicate stateful [[POD]]s, you should use [[StatefulSet]].
>  You can't do it with Deployment.

You manage Deployment, and it does everything underneath.
See [[ReplicaSet]].

![[K8s Deployment.png]]