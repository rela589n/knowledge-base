It's possible to intercept property access in child class:

```php
<?php

class User
{
    protected int $foo {
        set => $value + 1;
    }
}

class Child extends User
{
    protected(set) int $foo {
        get {
            if (isset($this->foo)) {
                return $this->foo;
            }

            var_dump('get');

            // this is different from a plain assignment
            // it sets to 124 (with parent hook)
            (fn () => $this->foo = 123)();
            // $this->initializeFoo(123); would do the same effect

            return $this->foo;
        }
        set {
            var_dump('set');

            parent::$foo::set($value);
        }
    }

    public function getFoo()
    {
        return $this->foo;
    }

    private function initializeFoo(): void
    {
        var_dump('initialize');

        $this->foo = 123;
    }
}

$user = new Child();

//$user->foo = 1;
//unset($user->foo);

var_dump($user->foo); // 124
```