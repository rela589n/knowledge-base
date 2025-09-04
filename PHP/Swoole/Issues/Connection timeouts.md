Database server could close connection if you didn't make any requests for the past period of time. Or the connection could close when [[Redis]] crashes (and recovers later on), - the connection would be broken.

![[Pasted image 20241109202808.png]]