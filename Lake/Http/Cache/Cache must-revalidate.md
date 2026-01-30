
**Core idea:**
- Once cache expires → **must revalidate** with origin server
- Cannot serve stale content, even if server is unreachable

```
Cache-Control: max-age=60, must-revalidate
```

## Problem It Solves

Default behavior without `must-revalidate`:

```
Cache expires → server unreachable
  ↓
Cache MAY serve stale content anyway
  (better stale than nothing)
```

With `must-revalidate`:

```
Cache expires → server unreachable
  ↓
Cache MUST return error (504 Gateway Timeout)
  (never serve stale)
```

## When to Use

Content where **staleness is unacceptable**:
- Financial data (prices, balances)
- Security-sensitive info
- Real-time inventory/availability

## When NOT to Use

Content where stale is better than error:
- News articles
- Static documentation
- Marketing pages

## Related Directives

| Directive | Meaning |
|-----------|---------|
| `must-revalidate` | After expiry, must validate or error |
| `proxy-revalidate` | Same, but only for shared caches (CDN) |
| `no-cache` | Always revalidate before serving |
| `no-store` | Don't cache at all |

## Comparison

```
max-age=60
  → Cache for 60s
  → After: may serve stale if server down

max-age=60, must-revalidate
  → Cache for 60s
  → After: must validate or return error

no-cache
  → Always validate before serving
  → (implies must-revalidate behavior)
```

## Symfony Example

```php
$response = new Response();
$response->setMaxAge(60);
$response->headers->addCacheControlDirective('must-revalidate');
```
