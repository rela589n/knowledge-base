Event-driven approach.

For example, vacation file signature:
- sign file
- acknowledge signature
- acknowledge to crm
- signature successful

`SignFile` triggers `FileSignedEvent`
`FileSignedEvent` is listened by `AcknowledgeSignature`
`AcknowledgeSignature` triggers `SignatureAcknowledgedEvent`
`SignatureAcknowledgedEvent` is listened by `AcknowledgeToCrm`
`AcknowledgeToCrm` triggers `AcknowledgedToCrmEvent`
`AcknowledgedToCrmEvent` is listened by `SignatureSuccessful`

This is very *complex to debug*.
This is very *complex to handle the errors* (as each step could fail independently).

In case of bugs, system could end up in an undefined state (somewhere in between of the workflow).

Easily scales (each step could be executed in the queue)
One service being down, doesn't lay down the entire system
