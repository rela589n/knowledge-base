
**Core idea:**
- Can't easily invalidate cached content
- So **change the URL** when content changes
- Old URL stays cached (but unused)
- New URL fetches fresh content

## The Problem

```
GET /style.css
Cache-Control: max-age=31536000 (1 year)
```

You update CSS → users still get old cached version
    → no way to force browsers to fetch new file

## The Solution: Change URL

**Before update:**
```
/style.css → cached for 1 year
```

**After update:**
```
/style.css?v=2       # query string
/style.v2.css        # filename version
/style.a1b2c3d4.css  # content hash (best)
```

New URL = cache miss = fresh content

## Three Approaches

| Method | Example | Pros/Cons |
|--------|---------|-----------|
| Query string | `style.css?v=2` | Simple, but some CDNs ignore query strings |
| Version in filename | `style.v2.css` | Manual versioning |
| Content hash | `style.a1b2c3.css` | Auto-generated, changes only when content changes |

## Content Hash (Best Practice)

Build tools generate hash from file content:

```
style.css → style.8f3e2a1b.css
app.js    → app.c4d5e6f7.js
```

**Benefits:**
- Hash changes only if content changes
- Same content = same hash = cache hit
- Set `max-age=31536000, immutable`
- Perfect caching with instant invalidation

## Implementation

**Webpack:**
```js
output: {
  filename: '[name].[contenthash].js'
}
```

**Symfony Encore:**
```js
Encore.enableVersioning()
```

**HTML references:**
```html
<!-- Before build -->
<link href="{{ asset('style.css') }}">

<!-- After build (auto-generated) -->
<link href="/build/style.8f3e2a1b.css">
```

## Combined with Immutable

```
Cache-Control: public, max-age=31536000, immutable
```

- Long cache (1 year)
- No revalidation needed
- URL change = new file
