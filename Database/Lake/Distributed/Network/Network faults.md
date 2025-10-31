We can't know what happened when we don't receive response. Usually sender **[[Network Timeouts|timeouts]]** are used to **give up on waiting** for the response, but host **may receive response** later **when it don't wait for it anymore**.

**Issues with network** (see [[Network faults in practice]]):
- **request** may be **lost** (network cable);
- **request** may be **delayed** (overloaded network or recepient);
- **remote host** may've **failed** (powered off);
- **remote host stopped responding** ([[Process Pauses]]);
- **response** may be **lost** (misconfigured switch);
- **response** may be **delayed** (overloaded network or local host).