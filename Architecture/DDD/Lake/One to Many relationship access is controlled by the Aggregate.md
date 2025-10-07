---
aliases:
  - How to control one to many relationship to prevent unauthorized access
---
For example:
`/questionnaires/{questionnaireId}/questions/{questionId}`

You'd want to make sure that Question of `questionId` belongs to Questionnaire, and if it doesn't - thrown an exception (probably 404).

If that's the case, then Questionnaire should be [[Aggregate Root]], and Question - subsidiary entity. Use [[Association Traversal]] to find one.
