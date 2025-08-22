If [[RoadRunner mTLS]]

**`require_and_verify_client_cert`** - [[mTLS]]:
- Server **requires** client certificate;
- Both Client and Server verify each other's [[TLS certificate|TLS certificates]];
- Client must use `ChannelCredentials` with `$pem_private_key` and `$pem_cert_chain` (real)

**`verify_client_cert_if_given`** - [[Transport Layer Security|TLS]] or [[mTLS]]:
- Server could accept a client **certificate**, but **doesn't require** it;
- If the client sends one, it **is verified** against a [[Certificate Authority|CA]];
- Both Client and Server verify each other's [[TLS certificate|TLS certificates]];
- Client could use `ChannelCredentials` with and w/o `$pem_private_key` and `$pem_cert_chain` (real)

**`require_any_client_cert`** - weak [[mTLS]]:
- Server **requires** a client **certificate**;
- It **isn't verified** against [[Certificate Authority|CA]];
- Only Client verifies [[TLS certificate]] of the Server;
- Client must use `ChannelCredentials` with `$pem_private_key` and `$pem_cert_chain` (self-signed).

**`request_client_cert`** - [[Transport Layer Security|TLS]] or weak [[mTLS]]:
- Server could accept a client certificate, but **doesn't require** it;
- If the client sends one, it **isn’t verified** against a [[Certificate Authority|CA]];
- Only Client verifies [[TLS certificate]] of the Server;
- Client could use `ChannelCredentials` with and w/o `$pem_private_key` and `$pem_cert_chain` (self-signed).

**`no_client_certs`** - [[Transport Layer Security|TLS]]:
- Server doesn't accept a client certificate;
- Only Client verifies [[TLS certificate]] of the Server;
- Client uses `ChannelCredentials` w/o `$pem_private_key` and `$pem_cert_chain`.

Config essentials for **require_and_verify_client_cert**

- Server must have:    
    - cert and key: its own server certificate and private key.
    - root_ca: the CA (or bundle) that issued client certificates (trust anchor for client certs).
    - client_auth_type: require_and_verify_client_cert.

- Client must have:    
    - Its own certificate and private key (the client identity).
    - Trust of the server’s certificate (either system roots or the issuing CA/self-signed cert).
    - In gRPC clients, that usually means:
        - Provide server trust as root CA.
        - Provide client key + client cert for authentication.

