`openssl_pkey_new` - new private key
`openssl_pkey_export` - export private key
`openssl_pkey_get_details` - details
`openssl_pkey_get_public` - public from private
`openssl_private_encrypt` - encrypt with private

```php
<?php

require "/app/vendor/autoload.php";

/** @var OpenSSLAsymmetricKey $privateKey */
$privateKey = openssl_pkey_new(array('private_key_bits' => 2048));

/** @var string $privateKeyPem */
openssl_pkey_export($privateKey, $privateKeyPem);

/** @var array{bits:int,key:string,rsa:array} $keyDetails */
$keyDetails = openssl_pkey_get_details($privateKey);

/** @var string $publicKeyPem */
$publicKeyPem = $keyDetails['key'];

/** @var OpenSSLAsymmetricKey $publicKey */
$publicKey = openssl_pkey_get_public($publicKeyPem);

openssl_private_encrypt('39ce6841-121d-7e2b-929f-72b78da514a8', $encrpted, $privateKey);

dd(openssl_error_string(), $encrpted, base64_encode($encrpted), strlen($encrpted));
```