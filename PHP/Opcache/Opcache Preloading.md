It's possible to preload specific scripts on startup.

You might've seen something like this:

```php
// Help opcache.preload discover always-needed symbols
class_exists(ApcuAdapter::class);
class_exists(ArrayAdapter::class);
```

You should see [Preloading For Symfony](https://symfony.com/blog/php-preloading-and-symfony)
