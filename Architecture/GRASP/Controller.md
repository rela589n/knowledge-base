**Controller** stands **in-between** of UI and [[Use Case|Application Layer]],
*orchestrating* information flow 
		*from* UI 
		*into* business logic 
	(and vice versa),
***separating*** the two.

Changes in UI don't bother business code, 
and changes to the business code don't bother UI
([[Protected Variations]])
