**MaxSim [[Similarity Score]]** - every **query token** *is scored against* every **document token** ([[O (N**2)]]).

For each query token `q` find the document token `d`
	that matches best (max [[Inner Product|Dot Product]])
Sum those best matches across all query tokens.

[[MaxSim Scoring.png]]
