Write a console command to start a workflow that will log Fibbonacci numbers up to given number, and wait for 1 second.

Create a separate console command to shift the limit for the running workflow.

Monitor logs to see that everything works.

Add one more command to inspect the current iteration of the workflow.

Find a solution to stuck workflow on the last iteration (93). If you just use update method, this won't help, since activity is failing over and over again before the workflow applies update event. 

You should apply [[Update]] and [[Reset]] from [[Temporal UI|UI]].;