---
aliases:
  - Cross-Site Scripting
---
**XSS** for example when backend accepts **payload as is** and then it's **printed** on the web page **without escaping**. 

It allows execution of any **arbitrary script** on behalf of user.

To protect from it, make sure to **sanitize html** and output with **escaping**.
