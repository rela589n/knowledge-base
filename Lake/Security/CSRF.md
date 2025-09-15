---
aliases:
  - Cross-site Request Forgery
---
**CSRF** - attack, possible when backend uses **cookie authentication** (stateful) and no [[CORS]] configured (thought, it's possible to bypass).

Malicious actor creates a web-page that automatically sends a POST-request to your backend to do something. Since Person is authenticated, this request is valid.

To protect from it, form should includ **anti-CSRF token**.
