**ConfigMap** stores external application configurations (like adjustable ENVs, enabled features, DB host, etc). 

> Don't put secrets there. Use [[Secret]] instead.

You connect ConfigMap to the [[POD]].
Inside of the [[POD]] these values are ENV-variables.
