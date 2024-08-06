
See https://dev.to/nodedoctors/an-animated-guide-to-nodejs-event-loop-3g62

An event loop is basically an algorithm for async processing in sync environments.

First off, there's a call stack, which is used to handle function calls.

Interpreter before execution each next step goes through the event loop to check if the stack is empty. 

If it's not, it does execute each next operation from the stack. 

If a stack is empty already, it checks if there are any items present in the event queue. If so, it pushes next item from this queue into the call stack and executes it. 

When the event queue is empty, the stack is empty, process continues further: new item is added to the stack, it may generate async job somewhere else, which may push callback into the event queue, which will be fetched later on.




