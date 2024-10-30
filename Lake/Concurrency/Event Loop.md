---
aliases:
  - Scheduler
---
See https://dev.to/nodedoctors/an-animated-guide-to-nodejs-event-loop-3g62

An event loop is basically an algorithm for async processing in sync environments.

First off, there's always a **call stack**, that is used to handle function calls.

Before execution each next step, interpreter goes through the event loop to check **whether the stack is empty**:

1. If the stack is not empty, it executes each next operation from the stack. 
2. If a stack is already empty, it checks if there are any items present in the event queue. If so, it pushes the first item from this queue into the call stack and executes it. 

When the event queue is empty, the stack is empty, process continues further: new item is added to the stack, it may generate async job somewhere else, which may push callback into the event queue, which will be fetched later on.




