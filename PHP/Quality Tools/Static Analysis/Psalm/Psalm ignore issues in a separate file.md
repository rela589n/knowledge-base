Your main `psalm.xml`:

```diff
  <?xml version="1.0" encoding="UTF-8"?>
  <psalm
+       xmlns:xi="http://www.w3.org/2001/XInclude"
@@  
+         <xi:include  
+                 href="./psalm-vendor-issues.xml"  
+                 xpointer="xpointer(/*[local-name()='psalm']/*[local-name()='issueHandlers']/*)"  
+         />  
      </issueHandlers>  
  </psalm>
```

You additional `psalm-vendor-issues.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<psalm
        xmlns="https://getpsalm.org/schema/config"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="https://getpsalm.org/schema/config vendor-bin/psalm/vendor/vimeo/psalm/config.xsd"
>
    <issueHandlers>
		<!-- Your issue handlers -->
    </issueHandlers>
</psalm>
```

> Note that we're using psalm in `vendor-bin`.
> Adjust the directory to your proper installation path.

