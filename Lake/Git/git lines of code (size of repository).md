Number of files:

```shell
git ls-files src/ | egrep ".php" | wc -l
```

Number of lines of code:

```shell
git ls-files src/ | egrep ".php" | xargs cat | less | wc -l
```
