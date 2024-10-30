[[RoadRunner|RR]]  provides pool of [[RR Worker|workers]]. It keeps track of every worker, can allocate new ones, reset, generally manage.

[[RoadRunner|RR]] internally keeps the queue of incoming requests. It should be limited by some number to prevent [[Thundering herd effect]]

[[RR pool scaling|Can be scaled programmatically]]
