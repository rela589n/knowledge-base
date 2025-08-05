```php
Deprecation::trigger(  
    'doctrine/orm',  
    'https://github.com/doctrine/orm/pull/1212121',  
    'In ORM 4.0, the AttributeDriver will use iterable source file path names. To opt into the new mode today, set the "useSourceFilePathNames" constructor parameter to true.',  
    self::class  
);
```

