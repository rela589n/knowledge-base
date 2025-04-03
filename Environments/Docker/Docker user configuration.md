```diff
FROM ...

+ARG USER_NAME=app
+ARG USER_ID=1000
+ARG GROUP_ID=1000

...

+RUN groupadd --gid $GROUP_ID $USER_NAME
+RUN useradd --uid $USER_ID --gid $GROUP_ID --create-home $USER_NAME

+WORKDIR /app
+USER $USER_NAME

CMD [...]
```

In here  `--create-home` is necessary, since composer is storing cache in the home directory.

