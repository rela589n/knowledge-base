---
aliases:
  - Vespa App
---
**Application** - a deployed unit of configuration that tells Vespa what data to accept and how to handle it.

One Vespa cluster runs one Application.

## Structure

```
my-app/
├── services.xml      # cluster configuration
└── schemas/
    └── book.sd       # document schema
```

## Purpose

- Specifies what services to run
- Defines document fields, types, indexing ([[Vespa Schema|Schemas]])

## Key Point

- Vespa won't serve port 8080 until an application is deployed
- Deploy via config server on port 19071

See also [[Vespa Deploy]]
