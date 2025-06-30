---
aliases:
  - It is not possible to map entity with a composite primary key as part of the primary key of another entity
---
It is not possible to map entity 'App\EmployeePortal\Accounting\Account\Account' with a composite primary key as part of the primary key of another entity 'App\EmployeePortal\Accounting\Account\AccountTransaction#account'.

This is not possible:
```php
class AccountTransaction
{
    #[ORM\Id]
    #[ORM\Column(type: 'uuid')]
    private Uuid $id;

    #[ORM\Id]
    #[ORM\ManyToOne(targetEntity: Account::class)]
    #[ORM\JoinColumn(name: 'account_id', referencedColumnName: 'id')]
    #[ORM\JoinColumn(name: 'user_id', referencedColumnName: 'user_id')]
    private Account $account;

@@
```
