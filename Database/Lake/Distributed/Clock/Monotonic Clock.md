**Monotonic Clock** - meant to **always move forward**, but clock value on one machine doesn't make any sense for other.

These are suitable for **duration measurements**, but **not for absolute measurement** of time. ^4b7ce2

**Slewing the clock** - **NTP server** can't make monotonic clock to move back or forth, but it **may adjust its speed**.

