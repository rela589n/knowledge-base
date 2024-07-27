**Wall-clock** (**Time-of-day clock**) - represents time of some calendar, usually represented as the **number of seconds (or milliseconds) since epoch**.

These are suitable for **absolute time measurement** and **not for duration**. ^69c3a4

If time on machine is **ahead of NTP server**, time may be **forcefully reset to past time**.

Time may **differ on different nodes** because of [[Clocks Synchronization Issues]].
This leads to [[Problems when Relying on Synchronized Clocks]].


