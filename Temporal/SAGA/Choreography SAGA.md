**Event-driven** approach.

**Example:** vacation file signature:
- sign file
- acknowledge signature
- acknowledge to crm
- signature successful

**`SignFile`** triggers **`FileSignedEvent`**
	 is *listened by* **`AcknowledgeSignature`**
		*triggers* **`SignatureAcknowledgedEvent`**
			is *listened by* **`AcknowledgeToCrm`**
				*triggers* **`AcknowledgedToCrmEvent`**
					 is *listened by* **`SignatureSuccessful`**

It is very ***hard to* debug**
It is very ***hard to* handle errors**
	(each step could fail independently).

In case of bugs, system could end up in an undefined state (somewhere in between of the workflow).

Easily scales (each step could be executed in the queue)
One service being down, doesn't lay down the entire system
