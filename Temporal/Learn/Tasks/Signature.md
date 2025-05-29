Create a workflow that will model digital signatures.

There are two steps required:
- sign the file
- confirm to third party

Signature can fail due to multiple causes:
- missing private key
- expired private key certificate (return date of expiration)
- incorrect credentials

Confirmation can fail:
- 500 ([[Permanent Failure]])
- timeout ([[Transient Failure|Temporary Failure]])
- response error ([[Permanent Failure]])
