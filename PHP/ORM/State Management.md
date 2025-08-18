See [[State Management.canvas|State Management Diagram]]

State is managed by Ghost objects. It uses [[Lazy Loading]] technique, so that state is populated step by step.

Change management happens only to mapped properties. Not mapped aren't tracked.

When some property is updated, this change is recorded in internal `$changes` array, that is used later on during sync.

It's not strictly necessary to have property initialized to make an update. When a new value is written, if property is not initialized, it will just be updated without comparison with the current value (sql statement is for sure to be issued).

#### Collection Properties

[[Spec Collection]] replacements are not allowed. Since relationships are defined reactively, when it's necessary to clear it, it must be cleared explicitly.

### Proxy objects

[[Proxy Objects]]