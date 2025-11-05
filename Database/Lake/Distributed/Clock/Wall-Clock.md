---
aliases:
  - Time-of-day Clock
---
**Wall-Clock** - represents calendar time, usually as the **number of seconds (or milliseconds) since epoch**.

*Suitable for* **absolute time *measurement***, yet ***not for* duration**. ^69c3a4

If machine's time is **ahead of NTP server**,
	time may be **forcefully reset to the past time**.

Time may **differ on different nodes** because of [[Clocks Synchronization Issues]].

This leads to [[Problems when Relying on Synchronized Clocks]].


