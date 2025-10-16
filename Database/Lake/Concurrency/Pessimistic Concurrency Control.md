**Pessimistic [[Concurrency]] Control** is essentially what [[Two-Phase Locking (2PL)|2PL]] is. 

If **anything *could go* wrong**, 
	we'd **wait until situation is safe** again 
and only then continue execution. 

[[Actual Serial Execution]] is pessimistic to the extreme -
lock is held for the entire database.
