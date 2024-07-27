More details at https://docs.google.com/document/d/1lIldIy_6iP2wKJVtxMsa7m2aUTTq1HHwxNo7wnMYt8Q/edit#heading=h.lrvj6uobtw26

Difference between authentication and authorization.
JWT issues (when user has been revoked from some permissions).
Making classes final.
SF autowire & autoconfigure

# PHP

## Generators, Testing

https://github.com/sebastianbergmann/phpunit/issues/4757

## What is array zipping, how you would do this?

https://www.php.net/manual/en/function.array-map.php

null as callback

## What is the difference between array_merge and []= and += for arrays

`+=` does not overwrite existing keys, adds non-present
`array_replace` always overwrite any existing keys
`array_merge`  overwrite only string keys, numeric will be indexed
`[]=` will append value by next numeric index

## What is the late static binding?

**Late static binding** - PHP saves class from last non-forwarding method call, so that it may be referenced. Forwarding calls are `self::`, `static::`, `parent::` and `forward_static_call()`.

# General industry knowledge

## What happens when we type url in browser and click enter? Lifecycle

## Ways to set up PHP to process requests (SAPI)


# Other questions

## What books have you read? What you heard about?


