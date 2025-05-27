---
aliases:
  - Regex negative lookbehind
---

Everything that does not end with `Test` or `ApiPoint`:
```
^(?!.*(Test|ApiPoint)$).*
```

Much easier way to do this is **lookbehind**:

```
(?<!Test|ApiPoint)$
```
