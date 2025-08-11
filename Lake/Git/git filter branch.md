
Example of filter branch script that rewrites commit author:

```shell
FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch --env-filter '
CORRECT_NAME="Yevhen Sidelnyk"
CORRECT_EMAIL="zsidelnik@gmail.com"
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
' --tag-name-filter cat -- --all fd1fe2d..HEAD
```

> You can omit revisions, since the current approach will rewrite all but the first commit.

It could also be configured with message filter:

```
 --msg-filter '
sed -e 's/taskid\x2Eorg\x3Amassmediagroup\x2Fphotos\x2Dexchanger\x2Dsidelnyk/origin/'
'
```

