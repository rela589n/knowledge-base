---
aliases:
---
**Schema Changes** - Vespa applies schema modifications live with zero downtime, but enforces rules to protect data.

https://docs.vespa.ai/en/basics/schemas.html#working-with-schemas
## Safe Changes - Applied Automatically

- Add new fields
- Add new schemas
- Change indexing settings (re-indexes in background)

## Breaking Changes - Blocked by Default

- Remove fields
- Change field types
- Rename fields

Vespa rejects these to prevent data loss.

### Forcing Breaking Changes

- Add `validation-overrides.xml` to acknowledge data loss
- Or create new schema + migrate data
- Or redeploy with fresh empty index
