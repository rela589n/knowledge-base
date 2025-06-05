See [[WorkflowPrototype]] to understand the reasons.

If you need to rename the workflow, you should do it this way:
- copy current class, and name it as you want;
- mark old class deprecated;
- in the old class instantiate new workflow class;
- on any interaction with old workflow, delegate it to the new one.

If the workflow isn't long running, after all old workflows are completed, 