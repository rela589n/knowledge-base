[[Microservices]] Incentive - @ changes **doesn't affect** each **other**.

- Team **Productivity**:
	- [[Continuous Integration|CI]] time;
	- teams disturbance;
- Lower **Error Cost**:
	- **Fault Isolation**:
		- one **feature** won't **break** the **whole system**;
		- **backup rollback** is per service
	- **Resources Isolation**:
		- feature won't **swallow** all the **RAM / CPU**;
- Easier **Deploymet**:
	- Isolated **Downtime** / No Downtime;
	- Isolated **Scope** of Deployment - roll out **frequently**;
- Independent **Stack**:
	- one in one **language**, another in another;
	- **Different Stack**.
- Independent **Upgrades**:
	- one service could be upgraded without the others;

Yet, it's:
- harder debug
- common things are duplicated
- more work for the upgrade
