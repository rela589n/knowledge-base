1. configure rector rule for the target version
2. run rector
3. review the diff
4. run the tests to find what's obviously broken
5. upgade:
5.1. read upgrade instructions of the upgraded libraries;
5.2. make the list of what must be fixed in the repository;
5.2. perform the manual upgrade of what is still to be upgraded (e.g. configurations like server_version, changes of the entity,
etc.) according to upgrade instructions;
6. repeat 4 and 5 until **tests are green** AND **all upgrade instructions were fixed** or found to be inapplicable.
7. verify that no upgrade instructions are applicable to our repository any longer.

