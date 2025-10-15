**Orchestrator [[SAGA pattern|SAGA]]** - ***controls*** the whole **workflow** of steps required to implement business transaction.

**Example:** vacation file signature:
- sign file
- acknowledge signature
- acknowledge to crm
- signature successful

There would be SignVacationFileWorkflow that would call four activities:
- SignFileActivity
- AcknowledgeSignatureActivity
- AcknowledgeToCrmActivity
- SignatureSuccessfulActivity

In case of **any failure** 
	(for example, AcknowledgeToCrmActivity fails unrecoverably), 
SAGA should *execute* **compensation steps** 
	(e.g. compensate AcknowledgeSignatureActivity and SignFileActivity)
		 it would delete the signed file and revert status.