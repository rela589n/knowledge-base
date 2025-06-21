---
aliases:
  - KernelBrowser
  - Symfony Test Login
---

```php
private function login(string $id): void  
{  
    /** @var TokenStorageInterface $tokenStorage */  
    $tokenStorage = self::getContainer()->get('security.token_storage');  
  
    $tokenStorage->setToken(new TestBrowserToken(user: new InMemoryUser($id, null)));  
}
```