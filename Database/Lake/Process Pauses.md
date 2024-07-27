A check inside of code may not work as expected since **code may stop it's execution** at any point for undetermined period of time because of **process pause**:
- **[[Limiting the impact of garbage collection|garbage collector]]** may run (in worst cases it ran for minutes);
- VMs manager may **switch CPU to another VM**;
- Process manager may **switch to another program**;
- **VMs may be suspended** (saving machine RAM state to disk) and **resumed** (loading it back to RAM) at any time;
- if **app waits for disk IO**, it's process may get suspended;
- a simple memory access may lead to loading page from disk when **memory swapping to disk** is enabled;
- user closes laptop or operator sends `SIGSTOP` **pause signal** (or Ctrl+Z in the terminal).

Hence, the code **can't make any assumptions regarding timing**. Nodes in distributed systems **must be ready** to operate even with **process pauses**.

![[Real-time systems#^a36850]]
