The conflicts must be resolved in a **[[Eventual consistency#^01eced|convergent]]** way.

Ways to achieve convergent conflict resolution:
- give each write an ID (either random number or kty-value hash or uuid or timestamp), and let the **write with the higher ID-number win**. If timestamp is used, this is called [[LWW (last write wins)]]. Approach implies **data loss**;
- give each leader an ID, and let the **writes with the higher-ID replicas win**;
- **merge values** somehow - like order values, and concatenate;
- **record the conflict** and **write the application code** to resolve it later on (possibly by **prompting the user**). 
