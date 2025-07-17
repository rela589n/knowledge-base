See [[State Management.canvas|State Management]]

State is managed by Ghost objects. It uses [[Lazy Loading]] technique, and therefore state is populated step by step.

When some property is updated, this change is recorded in internal `$changes` array, that is used later on during flush.

It's not strictly necessary to have property initialized to make an update. If new value is written, it just won't just be compared with the existing value, and sql statement will be issued.

#### Collection

Collection replacements are not allowed. Since relationship is defined reactively, when it's needed to be cleared, it must be cleared explicitly.