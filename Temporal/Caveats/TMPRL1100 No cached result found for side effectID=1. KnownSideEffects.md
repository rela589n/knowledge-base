It's the problem of [[Workflow Replay|Workflow side effects]] that `yield Workflow::sideEffect()` was added in the place where it wasn't expected. 

This is due to [[Workflow Replay]], as it expects some other action to be there, yet there's side effect.

[[Workflow Versioning]] for the rescue.

