Every element of the layer depends either on the elements of this same layer or on the layers beneath.

Upward communication - only indirect.

Each layer represents some aspect of a system:
- UI (presentation);
- App (application) - thin, coordinates tasks to domain layer;
- Domain (model) - business rules ([[Heart of software]]), business state is retrieved via infrastructure layer;
- Infrastructure (utilities) - low-level code to support higher levels.

It is crucial for Domain to be isolated from other layers so that volatile business logic may be implemented with minimal effort.
