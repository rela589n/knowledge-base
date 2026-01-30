Cache **always asks the server** if its copy is still valid
    but the server can respond with just "304 Not Modified"
        instead of regenerating the full response.

## Two Approaches

### 1. Last-Modified / If-Modified-Since

Based on **timestamp**:

- Server sends:    `Last-Modified: Thu, 30 Jan 2026 10:00:00 GMT`
- Client sends:    `If-Modified-Since: Thu, 30 Jan 2026 10:00:00 GMT`
- Server checks:   Has content changed since then?
	- No  → 304 Not Modified (empty body)
	- Yes → 200 OK (full content)

### 2. ETag / If-None-Match

Based on **content fingerprint**:

```
Server sends:    ETag: "abc123"
Client sends:    If-None-Match: "abc123"
Server checks:   Does current ETag match?
  Yes → 304 Not Modified (empty body)
  No  → 200 OK (full content + new ETag)
```

## Trade-offs

**Pros:**
- Always fresh data
- Saves bandwidth (304 has no body)
- Skips expensive work when content unchanged

**Cons:**
- Requires server roundtrip every time
- Server must compute Last-Modified or ETag

## When to Use

- Dynamic content that may change unexpectedly
- Content where freshness is critical
- When you can cheaply determine "has it changed?"

## Symfony Example

VERIFY IT!

```php
public function __invoke(Request $request): Response
{
    // Get last modification date (cheap query)
    $lastModified = $this->service->getLastModifiedAt();

    $response = new Response();
    $response->setLastModified($lastModified);
    $response->setPublic();

    // Check if client's cache is still valid
    if ($response->isNotModified($request)) {
        return $response;  // 304 - skip expensive work
    }

    // Only do expensive work if content changed
    $data = $this->service->getExpensiveData();

    return $response->setContent($data);
}
```

## ETag Example

VERIFY IT!

```php
$response = new Response();
$response->setEtag(md5($response->getContent()));
$response->setPublic();

if ($response->isNotModified($request)) {
    return $response;
}
```

---

See also: [HTTP Cache](HTTP%20Cache.md) | [Expiration Model](Expiration%20Model.md)
