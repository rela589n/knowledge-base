This code checks if any of the typed classes declares ExceptionalValidation attribute:
```php
$object = $parentRule->getEnclosingObject();

$classReflection = $this->reflector->reflectClass($object::class);

$propertyType = $classReflection->properties()[$parentRule->getName()]->type();

$visitor = new class extends DefaultTypeVisitor {
    #[Override]
    public function namedObject(Type $type, NamedClassId|AnonymousClassId $classId, array $typeArguments): bool
    {
        if ([] !== $classId->reflect()->getAttributes(ExceptionalValidation::class)) {
            return true;
        }

        return $this->check($typeArguments);
    }

    #[Override]
    public function intersection(Type $type, array $ofTypes): bool
    {
        return $this->check($ofTypes);
    }

    #[Override]
    public function union(Type $type, array $ofTypes): bool
    {
        return $this->check($ofTypes);
    }

    #[Override]
    protected function default(Type $type): false
    {
        return false;
    }

    /** @param Type[] $types */
    private function check(array $types): bool
    {
        foreach ($types as $type) {
            if ($type->accept($this)) {
                return true;
            }
        }

        return false;
    }
};

dd($propertyType->accept($visitor));
```