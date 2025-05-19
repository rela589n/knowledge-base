---
aliases:
  - Log Navigator
---
Use following shortcuts:
`g` - go to start (`:goto 0`)
`G` - go to end (`:goto 100%`)

also, you can avoid including whole file into lnav, by using `tail`:

```shell
tail -f var/log/test.log | lnav
```

To find by any text, use `/` and start typing text.

## Filters

Command:
`:filter-in temporal` - filters by match

`:filter-out INFO` - filter by negative match (skip these)

Use `Tab` to switch into filters viewing mode.

`Shift+P` - pretty-print (JSON, XML)
## Theme

Use `:config /ui/theme` (and Tab) to configure.
