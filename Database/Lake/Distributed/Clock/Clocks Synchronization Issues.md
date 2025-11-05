Wall clock issues:
- **Clocks are prone to [[Clock Drift|Drifting]]**;
- NTP server time may be far ahead/behind machine time, leading **apps to see time going back/forth** substantially, or even **machine can refuse to sync clock**;
- misconfigured **firewall** may **refuse access to NTP** server;
- NTP **works via network** [[Network Unbounded Delay|prone to delays]], inaccuracy may be up to seconds when network is loaded;
- **NTP** may be **misconfigured** saying time inaccurate by hours. Usuaally clients request multiple NTP servers;
- time is prone to the **[[Leap second]]**;
- in VMs clock is virtualized, which makes app **timekeeping inaccurate** (jump forward by tens milliseconds) when **another VM is running**;
- clocks are **not reliable at all on third-party devices** (smartphones), which we have no control over.
