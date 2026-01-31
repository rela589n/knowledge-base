Cache uses stored responses <b><u>without contacting</u> the server</b>
    until the expiration time passes.

## Headers

```
Cache-Control: max-age=3600    # cache for 1 hour
Cache-Control: s-maxage=3600   # shared cache (CDN) duration
Expires: Thu, 30 Jan 2026 12:00:00 GMT
```

## How It Works

```
1. Server responds with: Cache-Control: max-age=3600
2. Cache stores response
3. Next request (within 1 hour):
   → Cache serves directly, no server contact
4. After 1 hour:
   → Cache considers response "stale"
   → Fetches fresh copy from server
```

## Trade-offs

**Pros:**
- Fastest possible response (no server roundtrip)
- Reduces server load significantly

**Cons:**
- Can serve stale data
- Server has no control until cache expires
- Hard to invalidate early

## When to Use

- Static assets (CSS, JS, images)
- Content with predictable update cycles
- Public content that tolerates some staleness

## Symfony Example

```php
$response = new Response();
$response->setPublic();
$response->setMaxAge(3600);        // browser cache
$response->setSharedMaxAge(3600);  // CDN cache

return $response;
```

---

See also: [HTTP Cache](HTTP%20Cache.md) | [Validation Model](Validation%20Model.md)
