If  `tls` is configured, then in any case client must provide `['credentials' => ChannelCredentials::createSsl()]`  configuration. 

Thus, Server [[TLS certificate]] is always validated. You can trust the server certificate by providing it to the credentials object: `ChannelCredentials::createSsl($serverCert)`.

This is must have. The rest is configured per [[client_auth_type config]].
