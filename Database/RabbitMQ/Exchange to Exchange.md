This is particularly feature of [[RabbitMQ]] .

One could define `auth_events` exchange and bind it to some other exchanges:
- `user_events` by `user.#` routing key
- `admin_events` by `admin.#` routing key

Then for `user_events` we could define this routing:
- `user_updates` by `user.registered`
- `user_updates` by `user.banned`
- `user_updates` by `user.deleted`

Hence, `user_updates` will have every update of the user, but this exchange won't include for example, `user.password_reset_request.created`, since it doesn't actually update the state of the user.

Then, `user_updates` could be easily bound to particular queues that are interested in any updates that happen to our users.
