---
aliases:
  - vespa feed command
---
`vespa feed` — feeds documents from a JSONL file into Vespa in bulk.

## Usage

```sh
vespa feed -t http://localhost:8080 dataset/documents.jsonl
```

- `-t` — target container endpoint
- File contains one JSON document operation per line

## JSONL Format

```json
{"put": "id:namespace:doctype::1", "fields": {"title": "Hello", "body": "World"}}
{"put": "id:namespace:doctype::2", "fields": {"title": "Foo", "body": "Bar"}}
```

Handles batching and retries automatically via the `/document/v1/` API.
