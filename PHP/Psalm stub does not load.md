When psalm stub is registered for class used in inheritance, it's necessary to register it with [`preloadClasses` option](https://psalm.dev/docs/running_psalm/configuration/#stubs):

```diff
<stubs>  
-    <file name="vendor-bin/linters/stub/ServiceEntityRepository.stub"/>  
+    <file name="vendor-bin/linters/stub/ServiceEntityRepository.stub" preloadClasses="true"/>  
</stubs>
```