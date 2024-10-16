When you need to process a bunch of data and run some post task after all.

Step1 - process records:
- record1
- record2
- recordN

Step2 - after all records have been processed run:
- event

The idea is very simple. You usually have state database for each of the records. Thus, there're `orchestrator` and `record` entities. When the record is processed, we could update `orchestrator` state to include this update.

Primarily, we dispatch into the queue for processing all the items:
- record1
- record2
- ...
- event

Every one of them.

The key point here is that we won't process the event until all of the records have successfully completed.

The way to accomplish this is by means of commutative hash function. `orchestrator` entity will have `processingHash` field. This field will be updated every time record is processed. 

The way to update it is following: `newHash = (oldHash * recordId) mod M`. In fact, since multiplication is commutative, it doesn't really matter in which order the records are processed.

Hence, this update happens to orchestrator entity each time record is processed.

Regarding the `event` processing, - it is gonna be in the same queue as the rest of participants of the processing. In the process, which records and event are produced, we compute the final expected hash of all the processed records. 

Therefore, if `event` is taken out of the queue, while some records have not completed their processing yet, we'll have hash mismatch (and put the `event` back into the queue). Once all the records have been processed successfully, the hash will match, and the `event` will get processed.

