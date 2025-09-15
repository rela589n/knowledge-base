---
aliases:
  - Cross-Origin Resource Sharing
---
**CORS** - **headers** that are **added by the backend** that are **analysed by web browser** that checks if current domain is legitimate, and rejects if not. 

So, returning CORS Allow Origin example.com, will inform the browser to accept the response only if current domain is example.com.

This prevents from attacks such as copied web-site that is redirecting traffic to the upstream backend.
