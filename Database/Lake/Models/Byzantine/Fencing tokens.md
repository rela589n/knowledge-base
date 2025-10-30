**Fencing tokens** are meant to solve lock issue in distributed systems:

![[Knowledge in distributed systems#^12c90c]]

When any particular resource is locked, the **lock manager issues fencing token**, which is sent along with the write to the resource. The **resource is responsible for checking the tokens** itself.

For instance, if resource has already processed token 32, and later on write with token 31 comes in, then it is rejected, since more recent token is most likely expired.

This is a good idea to **protect API from abusive clients** even though it is an internal API.
