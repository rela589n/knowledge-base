---
aliases:
  - Opensource monetisation
---
The rule of thumb is that:

> Anything that attracts the audience over the internet can be turned into the income.

The main revenue is your **popularity**. You should utilize it.

There are open-source companies that **provide paid services**. People using their projects hire them to solve some particular problems they couldn't or aren't willing to solve themselves.

Another way is by [[Sponsorship platforms|sponsorship]]. Yet, this model doesn't always work in practice, because actual consumers usually just install your software and don't pay you any money for the product they use. Vue.js (authored by Evan You), having over a million users, has only a few hundreds sponsors. Yet, this is the main source of income for Vue.

I think one could promote sponsorship by requiring at least 1$ of monthly <strike>payment for documentation</strike>. So, everything is free, but to have the docs to read, you'll have to pay. Documentation should be licenced. Payment should be made as subscription, and not one-off payment, to prevent people from paying just again when they open docs.

Actually, docs could available for some time slot (somehow copying should be prevented). This should not prevent new people from viewing it, but those who already use the lib.

There are also partnerships. Like you can post some of the companies built on top of your project on your website (ads). Video teaching programs that generate income from teaching your framework could kick back some revenue back to you.

The main goal of open-source is not making the money out of it. The goal is to have the ability to keep working on it by the money passively coming to you by from it. You could start a business out of it, but this way you will have to run the business, not to do the actual programming.

For the companies using your software it is a good marketing to sponsor your project (even 10 dollars per month), since their logo will pop up at github, and people will see it and know that this company is sponsoring such a good project.

### Proprietary upgrade

There's option for opensource to make a well-used library, but provide **proprietary upgrade**. So, they don't have to pay for using, but they **have to pay for upgrade** toward the new versions. An access to private github repository can be granted for sponsorship.

Access can only be granted for the user, who's at least registered for some time (5 months), or who's verified. Access is granted by public key. Thence, if they need to use it, they'd need their private key.

### Dual Licence: licence check in the generated code

It's open-source (w/o modification), but its usage requires licence.

For example, when having ORM Proxies, one could place a licence check there.

It requires a special algorithm for licence key generation. 
There must be 3 keys:
- licence key - issued to the user;
- distribution key - written in the source code (used to verify the licence);
- private key - used to issue licence keys (kept on the server).

Distribution key is updated with every release (except bug-fix).
During upgrade the users must get their new licence keys.

Licence key could be considered the part of repository, yet must not be published in public. Since it's used both for development and deployment, it could be committed. 

It is a sensitive information as any other key (not to be shared in public), but it's no more sensitive than a private codebase.

When old licence key is checked with the new distribution key, there must be an error triggered pointing to the website / github.

Licence key should have:
- a prefix that will identify the product. This way it will be easier to search over the internet and find the leaked keys;
- the id that will allow you to issue a patch that explicitly blocks that key;
- some information about the user (login, email) to know the person whose key was leaked.

Starting point for a hacker to check is to find where the licence key is used. If he can't find it out, he'll debug it.

In the library code, one could add "autoload.files" to load licence-checking file. This way, it won't be possible to patch the `composer.json` to skip it, but it will still be possible to patch the file to skip the licence.

The licence file could register an autoloader which is crucial to the application itself. It's not a standard psr-4 loading. It's custom. This loader will **use licence key** to load the file. One wouldn't be able to load all files in their application because each class would require a key variable from the autoloader to ensure it's the same as the signatureI:

```php
if ($v !== '1009877e') {
    throw new Exception();
}
```

Patching it manually would mean patching all the library files on every upgrade.

There should be variations about variable names and structure. There must be at least ten different ways of implementing this to prevent people from using auto replace with regex. 

This hash value will change every time the new version is released.

Thus, if one would like to do something like this, he'd need to develop a tool for cleaning up the class from these checks. That's the opposite of you developing the tool for adding these checks.

Besides that, you can patch a random method to add the licence check there.

It's problematic to check, since you still can make your class loader return the expected string (if written as literal). To solve this, the hash must be evaluated in place.

Another option could be creating an <strike>obfuscated class</strike> that is inherent to the usage of the library (like `EntityManager`), where licence check would happen. This way one trying to skip it will have to replace the complete class. Yet, this is not good for supporting this class, since it won't be easy to maintain. And also it's hard to obfuscate code w/o any extensions.

Licence check could fail with some probability. For example, 10%, which makes it more trouble to find the place.

If you fail right from the licence checker, it will be easy to track that. Exceptions leave stack trace, and even though it's evaluated, it's possible to find `evals` in the code.

When the library code is autoloaded, one could check for a file hash sum. If it's not in the list, stored by the licence file, it will cause the application to fail.

One could make the library work unexpectedly if the licence file is absent. Sick library. It will not fail explicitly. It will fail due to other reasons.

Licence check could be in evaluated code that will not give any stack trace.

Subscription is implemented via native means of github. Your licence is active all the time you are sponsoring.

There's no impedance for the new devs to play around with your library. They'd be able to get free one-day licence key in one click. 

One-day licence keys are free of charge.
Anyone could go and get such key.

In README.md there must be a link to the website where they sign in with Github and get their key right away.

Licence key page must be protected by ReCaptcha.

Purchased licence keys could have or not have ttl, depending on price tier.

5$ / month - Licence key is granted for 5 months. At the end of this time, one have to manually get new licence key.
10$ / month - granted for 5 months, and there's 1 month grace period. Thus, after reaching 5 months, devs will face the error locally, but it won't be error on production.
15$ / month - granted w/o any ttl. You will just need to have an active payment to upgrade.
