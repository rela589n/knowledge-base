---
aliases:
  - Overlap Policy
---
**[[Workflow Schedule]] Overlap Policy** controls the logic when the next [[Workflow Schedule Action|Action]] must be scheduled, but the previous one is still running. By default this policy will *Skip*.

- Skip - do not start new;
- BufferOne - allows at most one to be buffered and start right after the running one;
- BufferAll - unlimited buffer;
- CancelOther - cancel currently running, and start new one;
- TerminateOther - terminates currently other, and starts new;
- AllowAll - allow running any number of workflows simultaneously.



