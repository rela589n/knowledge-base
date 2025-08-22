```text
{#626
  +"metadata": []
  +"code": 14
  +"details": "failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:50051: Ssl handshake failed (TSI_PROTOCOL_FAILURE): SSL_ERROR_SSL: error:1000007d:SSL routines:OPENSSL_internal:CERTIFICATE_VERIFY_FAILED: self signed certificate"
}
```

This is when server has issued a self-signed certificate, that is not trusted by the client.
