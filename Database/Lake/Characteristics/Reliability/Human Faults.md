**Human errors** - most of faults are **because of humans** as far as people are not reliable. 

To prevent human errors:
- we'd implement **UI** such that it is **easy to do the right thing** and it is hard (and discouraged) to do wrong one;
- set up **monitoring and mesurement**;
- unit, integration, manual **testing**;
- separate environment where errors doesn't become faults (for example **stage for client testing** to not test on prod);
- create ways to **quickly recover** from faults. For example, data audit, **way to rollback changes**. Other example: in case data computed incorrectly, anticipate tool to do full recomputation of data (which is less performant, but reliable). ^49be6e