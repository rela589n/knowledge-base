To handle requests nginx uses workers and connections.

**Worker** - process responsible for maintaining number of incoming connections and processing their requests. 

> It's good to set number of workers to **auto**, meaning there would be as much workers as CPUs

**Connection** - each particular client request.


