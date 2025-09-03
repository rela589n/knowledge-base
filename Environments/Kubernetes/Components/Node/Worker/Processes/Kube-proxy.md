**Kube-proxy** forwards the requests from [[Environments/Kubernetes/Components/Service/Service|Service]]s to [[POD]]s.

It prefers [[POD]] on the same [[Worker Node]] when forwarding.

For instance, my-app -> db:

![[Kube-proxy.png]]
