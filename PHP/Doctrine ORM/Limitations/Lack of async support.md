[[Entity manager leaks]]

There's no way to use connection pool. 
Ideally, this should be isolated so logical connection is the same, while physical connection is different.
