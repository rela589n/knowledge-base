```sql
ALTER TABLE vacations 
    ADD CONSTRAINT vacations_non_overlapping_periods 
    EXCLUDE USING GIST (schedule_id WITH =, TSRANGE(period_start, period_end) WITH &&)
DEFERRABLE INITIALLY DEFERRED
```

See [[Doctrine Migrations & Exclude Constraint]]
