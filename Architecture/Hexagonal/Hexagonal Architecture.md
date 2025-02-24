Architecture of **ports** and **adapters**.

The business logic is isolated from externals (it is the central part).

Core defines interfaces (**ports**) that must be implemented by external system **adapters** (like database, gateways) .

Adapters are implementation of ports and define how core application takes in input (like api endpoint, console command, background consumer etc) - primary adapters, and how the external systems are interacted with - secondary adapters.

![[Hexagonal Architecture.png]]