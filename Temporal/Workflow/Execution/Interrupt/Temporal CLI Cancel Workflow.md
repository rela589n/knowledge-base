[Documentation](https://docs.temporal.io/cli/workflow#cancel)

Cancel one [[Workflow Execution|Workflow]]:
```shell
temporal workflow cancel --workflow-id=meaningful-business-id
```

Cancel multiple:

```shell
temporal workflow cancel \
  --query 'ExecutionStatus = "Running" AND WorkflowType="YourWorkflow"' \
  --reason "Testing"
```
