
**Core idea:**
- Tells caches that the response depends on these request headers
- Cache stores **separate versions** for each combination

```
Vary: Accept-Encoding
```

## Problem It Solves

Without `Vary`:

```
Client A requests /page (Accept-Encoding: gzip)
  → Server returns gzip compressed
  → Cache stores it

Client B requests /page (no gzip support)
  → Cache serves gzip version
  → Client B can't decompress it!
```

With `Vary: Accept-Encoding`:

```
Cache stores two versions:
  /page + gzip    → compressed response
  /page + no-gzip → uncompressed response
```

## Common Uses

Specify `Vary` only on the <u>headers you use</u>.

| Vary Header       | Purpose                  |
| ----------------- | ------------------------ |
| `Accept-Encoding` | gzip vs uncompressed     |
| `Accept-Language` | English vs French vs ... |
| `Accept`          | JSON vs XML vs HTML      |

## Multiple Headers

```
Vary: Accept-Encoding, Accept-Language
```

Cache stores separate version for each **combination**:
- gzip + English
- gzip + French
- no-gzip + English
- no-gzip + French

## Caution

Beware of `Vary: Cookie` or `Vary: Authorization`, as it:
- **Kills shared caching**, since it creates version per user
- Use `Cache-Control: private` instead

## Symfony Example

```php
$response = new Response();
$response->setVary('Accept-Encoding');

// Multiple headers
$response->setVary(['Accept-Encoding', 'Accept-Language']);
```

---

See also: [HTTP Cache](./HTTP-Cache.md) | [Public vs Private Cache](./Public-vs-Private-Cache.md)
