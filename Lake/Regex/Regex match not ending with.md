---
aliases:
  - Regex negative lookbehind
---

Everything that does not end with `Test` or `ApiPoint` using [[Regex negative lookahead|Lookahed]]:
```
^(?!.*(Test|ApiPoint)$).*
```

Much easier way to do this is **lookbehind**:

```
(?<!Test|ApiPoint)$
```
