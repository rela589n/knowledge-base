---
aliases:
  - Rector rules processing
---
## Processing the rules

### Preparation

1.  Get the list of the rector-reported issues:
   `composer ci:rector | awk '/^$/{f=0} /Applied rules:/{f=1} f' | grep -v "Applied rules:" | sort | uniq`
2. Temporarily add this list to `withSkip()`.
   For example:
```diff  
---  
Index: rector.php  
@@ -39,7 +55,15 @@  
         ReduceAlwaysFalseIfOrRector::class,  
-    ]);  
+    ])  
+    ->withSkip([ /// FIXME: process these rules, removing them by one:  
+        ExplicitAttributeNamedArgsRector::class,  
+        AddNameToNullArgumentRector::class,  
+        NewlineAfterStatementRector::class,  
+    ]);  
```
3. Verify that `composer ci:rector` reports none;

### Processing

Process the added rules, removing them by one: 

1. Remove one rule from the added `withSkip()` array;
2. Run `composer ci:rector-fix` (and `composer ci:ecs-fix`);
3. Review the code, changed by the rector.
4. Commit, specifying the processed rule class base name.
