### Problem
It is a pity when a wall-size model diagram is unusable for implementation and developers make their own ad-hoc design.

### Solution
A **single model** has to be used both **for analysis and software design** and other processes. Lest, analysis model won't deal with tech complexities and become abandoned.

### Application
In order to use single model, the first things necessary is to design the model in a literal way of domain, and then adjust it to fulfill technical requirements.

Finally, [[Binding model to implementation|model is bound to implementation]] - when [[Code|code]] changes, the underlying [[Domain Model|model]] has to update and vice versa - changing the model changes the code.