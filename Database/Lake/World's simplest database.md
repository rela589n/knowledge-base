World's simplest key-value database:

```bash
db_set () {
	echo "$1,$2" >> database
}

db_get () {
	grep "^$1," database | sed -e "s/^$1,//" | tail -n 1
}
```

Many databases use [[Log (sequence)]] which is append-only data file. Concept is similar to what `db_set` does.

![[Log (sequence)#^a46879]]

The `db_get`  has  `O(n)` cost of lookup, meaning if database will grow twice, lookup time will  double too.
