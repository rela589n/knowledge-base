Create a separate `static-analysis` folder and add `composer.json` there:

```json
{
    "prefer-stable": true,
    "require": {
        "php": "^8.2"
    },
    "config": {
        "platform": {
            "php": "8.2.3"
        },
        "sort-packages": true,
        "allow-plugins": {
            "cweagans/composer-patches": true
        }
    },
    "extra": {
        "patches": {
            "amphp/amp": {
                "Cannot redeclare Amp\\delay() (previously declared in /app/vendor/amphp/amp/src/functions.php:64)": "patches/conditional_delay_function_declaration.patch",
                "Cannot redeclare Amp\\Internal\\formatStacktrace() (previously declared in /app/vendor/amphp/amp/src/Internal/functions.php:16)": "patches/conditional_formatStacktrace_function_declaration.patch"
            }
        }
    },
    "autoload": {
        "files": [
            "bootstrap.php"
        ]
    },
    "require-dev": {
        "cweagans/composer-patches": "^1.7",
        "psalm/plugin-phpunit": "^0.18.4",
        "psalm/plugin-symfony": "^5.1",
        "vimeo/psalm": "^5.21",
        "weirdan/doctrine-psalm-plugin": "^2.9"
    }
}
```

Bootstrap file `boostrap.php`:
```php
/** @var Composer\Autoload\ClassLoader $loader */
$loader = require dirname(__DIR__).'/vendor/autoload.php';

/**
 * Loader was registered with option $prepend=true, but we would like this option to be false,
 * because current composer.json dependencies should be preferred to main composer.json dependencies.
 */
$loader->unregister();
$loader->register(false);
```

`conditional_delay_function_declaration.patch`:

```patch
Subject: [PATCH] conditional delay function declaration
---
Index: static-analysis/vendor/amphp/amp/lib/functions.php
IDEA additional info:
Subsystem: com.intellij.openapi.diff.impl.patch.CharsetEP
<+>UTF-8
===================================================================
diff --git a/vendor/amphp/amp/lib/functions.php b/vendor/amphp/amp/lib/functions.php
--- a/vendor/amphp/amp/lib/functions.php	(revision 0bd9fd36d4e2de704ee39bb3741142966fd98fa2)
+++ b/vendor/amphp/amp/lib/functions.php	(date 1692946681408)
@@ -121,7 +121,7 @@
         Promise\rethrow(call($callback, ...$args));
     }
 
-    /**
+    if (!function_exists(delay::class)){/**
      * Sleeps for the specified number of milliseconds.
      *
      * @param int $milliseconds
@@ -132,7 +132,7 @@
     {
         return new Delayed($milliseconds);
     }
-
+}
     /**
      * Returns the current time relative to an arbitrary point in time.
      *
```

`conditional_formatStacktrace_function_declaration.patch`
```patch
Subject: [PATCH] conditional formatStacktrace function declaration
---
Index: static-analysis/vendor/amphp/amp/lib/Internal/functions.php
IDEA additional info:
Subsystem: com.intellij.openapi.diff.impl.patch.CharsetEP
<+>UTF-8
===================================================================
diff --git a/vendor/amphp/amp/lib/Internal/functions.php b/vendor/amphp/amp/lib/Internal/functions.php
--- a/vendor/amphp/amp/lib/Internal/functions.php	(revision 5691c5576b8733545cc9250a85a2c7e6708d95e7)
+++ b/vendor/amphp/amp/lib/Internal/functions.php	(date 1692947227288)
@@ -2,6 +2,7 @@
 
 namespace Amp\Internal;
 
+if (!function_exists(formatStacktrace::class)) {
 /**
  * Formats a stacktrace obtained via `debug_backtrace()`.
  *
@@ -29,7 +30,7 @@
         return $line . $e["function"] . "()";
     }, $trace, \array_keys($trace)));
 }
-
+}
 /**
  * Creates a `TypeError` with a standardized error message.
  *
```

Usage: `static-analysis/vendor/bin/psalm --no-diff`

Also, you could think about using https://github.com/bamarni/composer-bin-plugin for this same sake.

