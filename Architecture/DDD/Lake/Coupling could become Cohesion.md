[[Coupling]] between packages could become [[Cohesion]] if respective coupled objects are moved into their own sets of packages.

For example:
```
Http/{Register,Login}
Service/{Register,Login}
```

could be reorganized into:

```
Register/{Http,Service}
Login/{Http,Service}
```

So that eventually `Register` and `Login` are independent of one another.