How long completed/failed workflow executions are persisted? Are they deleted afterwards? ([[Temporal Retention Period]])

How often is Workflow Task re-scheduled in case of [[Workflow Task Failure]]?

What happens if compensation takes longer, than specified activity timeout? Will it fail?

How to run workflow without waiting for it? Is it called scheduling? - Just use WorkflowClient::run() method instead of calling workflow object.

What happens if the workflow throws an exception?

How to use [[Activity Timeouts]] wisely?

Для чого використовувати WorkflowInterface, ActivityInterface? 

Як дебажити activity, і воркфлови, якщо вони запускаються воркером? Тобто, умовно я можу викликати якийсь `dd()`, щоб глянути щось? Тобто, лише `dc exec backend vendor/bin/var-dump-server`. Pprof (-d option)?

В семплах бачив postgresql і elasticsearch, - так розумію їх треба окремо розгортати? Є temporal cli, і для тесту можна використовувати built-in server.

Що всередині використовується як черга? Так само БД, чи можливо там якийсь брокер піднімається?

