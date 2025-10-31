Too **hight timeout** will cause **clients to wait** or see errors.
Too **low timeout** will cause high rate of **false faults**. 

It leads to:
- **lost data**;
- **actions** performed **more than once**;
- **increased network load** (to transfer responsibilities to other node);
- **complete system failure** if system operates on high load and **nodes declare each other** dead.

In the utopia world, where network could guarantee packet delivery within time `D`, and recepient could respond within time `R`, a reasonable timeout would be `T=2D+R` .

In fact, **network delivery time** is prone to **[[Network variability|variability]]** and **[[Network Unbounded Delay|unbounded delays]],** and recepient is prone to other current processess.

The **reasonable timeout** is selected **experimentally** - monitor different clients of network during some time period, **measure round-trip delays**.

Another option is to use **variable timeouts** based on metrics (response time, variability - _jitter_) being collected.



