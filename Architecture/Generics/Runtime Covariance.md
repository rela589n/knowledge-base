---
aliases:
  - Call-site variance
---
Having the parameter like this: `@param Collection<covariant Animal>`, we could pass in an [[Template Invariance|invariant]]  collection (`Collection<Dog>` or `Collection<Cat>`). If inside we would try to do any modification to the collection (like `add(T)` with incorrect type), it would result in compile-time error (because otherwise [[Template Invariance#^9212b1]] will get broken).
