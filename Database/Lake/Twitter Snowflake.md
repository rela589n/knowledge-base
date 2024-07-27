**Twitter Snowflake** - algo for **distributed** sequence numbers generation. It generates **approximately increasing unique IDs**. 

It's drawback is that when there are a lot small transactions, it **can't guarantee [[Happens-before relationship|causally dependent]] writes**. ^e12cfc