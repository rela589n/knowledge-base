This will install `sudo`, and add user to `sudoers` with NOPASSWD:

```shell
apt-get install -y sudo && \
echo "$USER_NAME ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER_NAME \
```
