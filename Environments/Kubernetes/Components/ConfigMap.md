**ConfigMap** - External application configurations (like adjustable ENVs, enabled features, DB host, etc). Don't put secrets there.

You connect ConfigMap to the [[POD]].
Inside of the [[POD]] you can use them as ENV-variables.