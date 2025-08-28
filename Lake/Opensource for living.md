---
aliases:
  - Opensource monetisation
---
The rule of thumb is that:

> Anything that attracts the audience over the internet can be turned into the income.

The main revenue is your **popularity**. You should utilize it.

There are open-source companies that **provide paid services**. People using their projects hire them to solve some particular problems they couldn't or aren't willing to solve themselves.

Another way is by [[Sponsorship platforms|sponsorship]]. Yet, this model doesn't always work in practice, because actual consumers usually just install your software and don't pay you any money for the product they use. Vue.js (authored by Evan You), having over a million users, has only a few hundreds sponsors. Yet, this is the main source of income for Vue.

I think one could promote sponsorship by requiring at least 1$ of monthly payment for documentation. So, everything is free, but to have the docs to read, you'll have to pay. Documentation should be licenced. Payment should be made as subscription, and not one-off payment, to prevent people from paying just again when they open docs.

Actually, docs could available for some time slot (somehow copying should be prevented). This should not prevent new people from viewing it, but those who already use the lib.

There are also partnerships. Like you can post some of the companies built on top of your project on your website (ads). Video teaching programs that generate income from teaching your framework could kick back some revenue back to you.

The main goal of open-source is not making the money out of it. The goal is to have the ability to keep working on it by the money passively coming to you by from it. You could start a business out of it, but this way you will have to run the business, not to do the actual programming.

For the companies using your software it is a good marketing to sponsor your project (even 10 dollars per month), since their logo will pop up at github, and people will see it and know that this company is sponsoring such a good project.

### Proprietary upgrade

There's option for opensource to make a well-used library, but provide **proprietary upgrade**. So, they don't have to pay for using, but they **have to pay for upgrade** toward the new versions. An access to private github repository can be granted for sponsorship.

Access can only be granted for the user, who's at least registered for some time (5 months), or who's verified. Access is granted by public key. Thence, if they need to use it, they'd need their private key.

### Dual Licence: licence check in the generated code

It's open-source (w/o modification), but its usage requires licence.

For example, when having ORM Proxies, one could place licence check there.

It requires a special algorithm for licence key generation. 
There must be 3 keys:
- licence key - issued to the user;
- distribution key - written in the source code (used to verify the licence);
- private key - used to issue licence keys (kept on the server).

Distribution key is updated with each release (including bug-fix).
During upgrade the users must get their new licence keys.

When old licence key is checked with the new distribution key, there must be an error triggered pointing to the website / github.

Subscription is implemented via native means of github. Your licence is active all the time you are sponsoring.

There's no impedance for the new devs to play around with your library. They'd be able to get free one-day licence key in one click. 

One-day licence keys are free of charge.
Anyone could go and get such key.

In README.md there must be a link to the website where they sign in with Github and get their key right away.

Licence key page must be protected by ReCaptcha.

Purchased licence keys could have or not have ttl, depending on price tier.

5$ / month - Licence key is granted for 5 months. At the end of this time, one have to manually get new licence key.
10$ / month - granted for 5 months, and there's 1 month grace period. Thus, after reaching 5 months, devs will face the error locally, but it won't be error on production.
15$ / month - 

Licence check could be in evaluated code that will not give any stack trace. Defer coroutine?