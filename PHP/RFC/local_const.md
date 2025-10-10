
firm
invar
strong


```php
class RegisterUser {
    
    public function __invoke(string $email, string $password): User {
        firm u = new User();
        
        u->email = $email;
        u->password = $password;
        
        // a lot of code here
        
        // error here
        u = 123;
        
        
        return u;
    }
}


$registerUser = new RegisterUser();
$registerUser('admin@example.com', 'password');
```


### Proc:

1. More reliable code, because once we created a firm value, it can never be reassigned. Thus you have less scenarios, side effects or edge cases to reason about. 

```
firm somethingConst = 'some default value';

// A lot of code here...

var_dump(somethingConst); // still the same
```

2. Better code readability. 
If you will invite some Java programmer to review your code (I've tried), first thing he will tell you is that he is horrified by the amount of `$` signs all around.
Use of `firm` notation will eliminate `$` signs.

Consider for example:

```php
$token = $this->tokensRepository->findWithTrashedById($linkId);
$file = $this->filesRepository->findById($fileId);

$this->authorize('deleteOf', [$token, $file]);
$command->execute(Collection::wrap($token));

return redirect()->route('dashboard.links.index', $fileId);
```

```php
firm token = $this->tokensRepository->findWithTrashedById(linkId);
firm file = $this->filesRepository->findById(fileId);

$this->authorize('deleteOf', [token, file]);
command->execute(Collection::wrap(token));

return redirect()->route('dashboard.links.index', fileId);
```

 When you see `$variable`, you know that it could be changed; on other hand, `invariable` could by no means be changed.

### Cons:
Firm value doesn't mean for object that it's properties could not be changed. It just guarantees that reference will not get changed. 
For a beginners at first it could be confusing that we can change properties of `firm` object. PHP shold not restrict object properties from being changed.
If it is really needed, then a programmer should design his class to be immutable.



