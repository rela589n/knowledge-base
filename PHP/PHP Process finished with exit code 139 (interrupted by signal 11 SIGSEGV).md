There's somewhere infinite [[Recursion]]:

For example, when `$this->valueHolderf75ba` is `$this`:

```php
public function getThis() : static
{
    $this->initializerfd44b && ($this->initializerfd44b->__invoke($valueHolderf75ba, $this, 'getThis', array(), $this->initializerfd44b) || 1) && $this->valueHolderf75ba = $valueHolderf75ba;

    return $this->valueHolderf75ba->getThis();
}
```

It results in:

```
Process finished with exit code 139 (interrupted by signal 11:SIGSEGV)
```