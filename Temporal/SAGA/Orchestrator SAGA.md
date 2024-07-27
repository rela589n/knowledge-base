When multiple steps are required to implement the business transaction, there's a single orchestrator that controls the whole flow.

For example, vacation file signature:
- sign file
- acknowledge signature
- acknowledge to crm
- signature successful

There would be SignVacationFileWorkflow that would call four activities:
- SignFileActivity
- AcknowledgeSignatureActivity
- AcknowledgeToCrmActivity
- SignatureSuccessfulActivity

In case of any failure (for example, AcknowledgeToCrmActivity fails unrecoverably), SAGA should execute compensation steps (e.g. compensate AcknowledgeSignatureActivity and SignFileActivity), - that would probably revert status and delete signed file.
