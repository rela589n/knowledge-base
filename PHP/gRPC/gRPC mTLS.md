```php
/**  
 * Create SSL credentials.  
 *  
 * @param string|null $pem_root_certs  PEM encoding of the server root certificates  
 * @param string|null $pem_private_key PEM encoding of the client's private key  
 * @param string|null $pem_cert_chain  PEM encoding of the client's certificate chain  
 *  
 * @return ChannelCredentials The new SSL credentials object  
 * @throws \InvalidArgumentException  
 */  
public static function createSsl(  
    string $pem_root_certs = null,  
    string $pem_private_key = null,  
    string $pem_cert_chain = null  
) {}
```

`pem_root_certs` - [[Certificate Authority|CA]] root certificates (trusted). Used to validate Server's certificate.

`pem_private_key` - client's private key

`pem_cert_chain` - client's certificate
