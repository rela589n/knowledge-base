A random part, used during encryption that ensures randomness of the encrypted value, so that encrypting the same value with the same key will result in different encrypted values. This prevents pattern-based attacks.

For both AES-CBC mode and AES-CFB mode, the initialization vector is the size of a block, which is 16 bytes = 128 bits.