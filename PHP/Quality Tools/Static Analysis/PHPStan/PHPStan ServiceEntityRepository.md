[[PHPStan]]

```neon
stubFiles:  
    - vendor-bin/linters/stub/ServiceEntityRepository.stub
```

`ServiceEntityRepository.stub`:

```stub
<?php  
namespace Doctrine\Bundle\DoctrineBundle\Repository;  
  
use \Doctrine\ORM\EntityRepository;  
  
/**  
 * @template TEntityClass of object  
 * @template-extends EntityRepository<TEntityClass>  
 */  
class ServiceEntityRepository extends EntityRepository {  
}
```

