Defaults options for [[Activity]]:
- initial interval: _1 second_; ^0cd43f
- max interval is _100 times initial interval_ (e.g. 100s);
- backoff: 2;

You can call the same [[Activity]] with different [[Retry Policy|Retry Options]]

Also, it's possible to specify `#[MethodRetry]` options for particular [[Activity]] method.
