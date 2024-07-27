**Real-time collaborative editing apps** allow multiple users to edit the same document (like Google Docs).

To guarantee that there will be no editing conflicts, the app must **obtain the lock on the document** before the user can edit it. If another user wants to edit, he would need to wait for previous user to commit the changes.

Usually **unit of change** is made very **small** (single keystroke), because this allows faster collaboration and avoid locking. Though, it **requires conflict resolution**.
