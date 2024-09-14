Topic exchange allows more flexible routing of messages depending on the routing key wildcards.

For example, if out of all `auth_events` vacation service interested only in user events, we could define binding following way:
- `vacation_incoming_events` by `user.*`

It would match both `user.registered`, `user.deleted`, etc, but won't match for example `admin.logged_in`.

`*` stands for one word
`#` stands for zero to multiple words

