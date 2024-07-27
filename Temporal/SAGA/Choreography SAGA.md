Event-driven approach.

For example, vacation file signature:
- sign file
- acknowledge signature
- acknowledge to crm
- signature successful

SignFile triggers FileSignedEvent
FileSignedEvent is listened by AcknowledgeSignature
AcknowledgeSignature triggers SignatureAcknowledgedEvent
SignatureAcknowledgedEvent is listened by AcknowledgeToCrm
AcknowledgeToCrm triggers AcknowledgedToCrmEvent
AcknowledgedToCrmEvent is listened by SignatureSuccessful

Is very complex to debug
In case of bugs, system could end up in undefined state
Easily scales (each step could be executed in the queue)
One service being down, doesn't lay down the entire system
