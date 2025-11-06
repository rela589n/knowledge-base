See [[State Management.canvas|State Management Diagram]]

When you query the [[ORM Collection|Collection]], you use the [[Specification]] to describe the [[Query]].

When creating objects, it adheres to [[Lazy Loading]], populating only queried fields.

It is achieved by Proxy objects.
State is managed by these Ghost objects.

Change management happens only to mapped properties. Not mapped properties aren't tracked.

When some property is updated, this change is recorded in internal `$changes` array, used later during sync.

It isn't strictly necessary to have properties initialized to perform an update. When value is assigned, if property is not initialized, it is just updated without comparison with the current value.

If property is initialized, assigning value to it will determine whether update's necessary by comparing old value to the new value.

Custom comparators might be registered.

#### Collection Properties

[[Spec Collection|Collection]] replacements are not allowed.
Since relationships are reactive, clearing must be explicit.

Say we delete `Post` entity. All the comments must be deleted as well.

==**Where do we define onDelete, onUpdate?**==

### Proxy objects

[[Proxy Objects]]