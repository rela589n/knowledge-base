[[Composer]] metapackage is an empty package (with no code), that may contain requirements and trigger their installation, and it itself has it's own version. 

Example of metapackage is `spiral/roadrunner`. It has no dependencies by itself, but rather serves just as marker to specify which version of roadrunner binary some particular library requires.

