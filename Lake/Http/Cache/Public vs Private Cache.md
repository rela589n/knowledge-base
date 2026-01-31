
**Core difference:**
- **Public** — can be stored by **shared caches** (CDNs, proxies)
- **Private** — only stored in **user's browser**

## Public Cache

```
Cache-Control: public, max-age=3600
```

Stored by:
- Browser
- CDN (CloudFront, Cloudflare)
- Reverse proxies (Varnish, Nginx)
- ISP caches

**Use for:**
- Static assets (CSS, JS, images)
- Content identical for all users
- Anonymous/public pages

## Private Cache

```
Cache-Control: private, max-age=3600
```

Stored by:
- <b>Browser <u>only</u></b>

**Use for:**
- User-specific data (profile, dashboard)
- Authenticated responses
- Personalized content

## Why It Matters

If you cache user-specific data as `public`:

```
User A requests /profile → CDN caches it
User B requests /profile → CDN serves User A's profile!
```

**Security risk** — sensitive data leaks to other users.

## Symfony Example

```php
$response = new Response();

$response->setPublic();   // Cache-Control: public
$response->setPrivate();  // Cache-Control: private (default)
```
