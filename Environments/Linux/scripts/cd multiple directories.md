```shell
cd() {
    another=`echo $@ | cut -c5-`

    if [[ $@ == "..2/"* ]]; then
        command cd ../../"$another"
    elif [[ $@ == "..3/"* ]]; then
        command cd ../../../"$another"
    elif [[ $@ == "..4/"* ]]; then
        command cd ../../../../"$another"
    else
        command cd "$@"
    fi
}
```

