```shell
kubectl logs -l app.kubernetes.io/component=backend -f
```

можна подивитись список подів з їх лейблами і фільтрувати по будь якому в принципі

```shell
kubectl get pods --show-labels
```
