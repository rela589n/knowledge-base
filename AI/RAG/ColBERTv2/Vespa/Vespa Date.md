https://docs.vespa.ai/en/writing/indexing.html#date-indexing

```sd
schema docs {

    document docs {
        field date_string type string {
            indexing: summary
        }
    }

    field date type long {
        indexing: input date_string | to_epoch_second | attribute | summary
    }

    field last_modified type long {
        indexing: now | attribute | summary
    }
}
```
