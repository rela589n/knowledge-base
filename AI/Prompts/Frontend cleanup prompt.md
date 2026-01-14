Make sure that every component has high cohesion. 
Use sharp naming.

Avoid stupid checks like Array.isArray() when type is already array. 
Never use casts (e.g. Number()) when it's already needed type. 
Do not ever check for type when it's guaranteed to be that type.
Make sure to use all appropriate type hints.

Never fail-safe! Fail-fast! If any of the preconditions aren't satisfied, throw. Be as robust as much as possible. Never leave empty catch blocks!

Don't add any useless checks that trow exception when there could not be an exception. Never code around checks that are already guaranteed by the object structure.

Make sure to extract conceptually common parts into a separate reusable elements.