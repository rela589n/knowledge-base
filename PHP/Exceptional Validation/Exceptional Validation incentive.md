First of all, thank you for writing this beautiful "Architecture of Complex Web Applications" book. It's awesome, and it's the book, that makes you think.

I would like to emphasize on chapter `6-validation.md`, where you say about Value objects and validation.

On the projects I worked on, we have used the approach you have mentioned here:

> The idea of removing the Laravel validation code seems intriguing. We can eliminate the **$this->validate()** call and simply catch the **InvalidArgumentException** in a global error handler.

These were Symfony projects, but about the idea...

Actually, I think that every value-object should be responsible for it's own validation rules. 

For example:

```php
#[ORM\Embeddable]
final readonly class Email
{
    private function __construct(
        #[ORM\Column(nullable: false)]
        private string $email,
    ) {
    }

    public static function fromString(string $email, ValidatorInterface $validator): self
    {
        // Value-object must convey the basic validation rules in order to enforce invariants provided by the business.
        // In addition, this approach makes invariants easily unit-tested.
        // Ad-hoc infrastructure-related validation logic (like email uniqueness)
        // should be implemented in each particular domain service outside the value-object.

        $violationList = $validator->validate($email, [
            new Assert\NotBlank(),
            new Assert\Email(),
        ]);

        if (0 !== $violationList->count()) {
            throw new EmailValidationFailedException($email, $violationList);
        }

        return new self($email);
    }

    public function getEmail(): string
    {
        return $this->email;
    }
}
```

So we have the validation logic right in place. Not only does `Email` class validate for the correct email, it also validates that value is not empty (could check string length, etc), tuning value object to be more precise about validation errors.

> However, as mentioned, HTTP request data are not always equivalent to the data passed to the Application Layer.
> 
> When a user changes their password, the application requests the old password, the new password, and the new password to be repeated. The Web layer validation should check the new password fields for a match...

Regarding this, I do not agree. HTTP layer should not implement any validations on its own. It should be dumb stupid - just pass the data and return response. When password is being reset, we'd need both new password and it's confirmation in Service, since these are the business rules that require us to. It's much more obvious to kept all business rules right in the service, than anywhere else.

Now, every value-object implements business validation rules for the particular value. When it comes to violations being mapped to the respective input data, it's where things are interesting.

In it's simplest form here's what it looks like:

```php
#[ExceptionalValidation]
final readonly class RegisterUserCommand
{
    #[ApiDoc\Property(example: 'email@test.com')]
    #[Capture(exception: EmailValidationFailedException::class, formatter: ViolationListExceptionFormatter::class)]
    #[Capture(exception: EmailAlreadyTakenException::class)]
    private string $email;

    #[ApiDoc\Property(example: 'p@$$w0rd')]
    #[Capture(exception: PasswordValidationFailedException::class, formatter: ViolationListExceptionFormatter::class)]
    private string $password;

    // @@
```

In this example, `EmailValidationFailedException` is captured and ascribed to `$email` property, and `PasswordValidationFailedException` to `$password` property.

To answer the question where actual analysis of these attributes take place, I'd say that it's the best if done as a command bus middleware (`ExceptionalValidationMiddleware`) - that is the way we have done it. Another option, which I should point out, but which I don't think is the optimal one is through some global listener that will take the exception and check if it matches with any of the command properties.

In any case, this approach simplifies a lot of things, as it allows us to keep business rules where they belong away from externals, sorting out the core problems that are revealed by validation group problems (different validation on nested objects in different scenarios), since in that case attributes provide only metadata about what and whither exceptions should be caught (happening when the validation has already been performed), not about what validation rules should be done, as in case of attributes validation.
