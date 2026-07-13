Useful commands:

- `composer outdated` (check for outdated packages);
- `composer why-not` (check for version constraints not allowing us to upgrade);
- `composer recipes:update` - update symfony-packages automatically;

In order to upgrade symfony to a new version, consider following 3-step the scenario:

## Step 1 - static analysis:

### Update

Update static analysis tools to their latest possible versions.

### Maximize level

Set `level: max` and fix the problems.
Install 

## Step 2 - upgarde dev-deps

Upgrade all dev packages to the latest versions, so that CI would be able to run on new set of dev-packages.

## Step 3 - cover with tests

Make sure to cover as much as possible with:
- smoke tests
- functional tests

## Step 4:

1. Upgrade all outdated third-party packages, except `symfony/*` (though, it would be nice to upgarde symfony to latest minor version).
2. Run & fix tests
3. Commit, deploy

## Step 5: perform the main upgarde (once it has all been successfully tested and works correctly):

1. Upgarde symfony packages (remember, currently there should be not that much dependency issues, because of first phase).
2. Run & fix tests;
3. Upgrade rest of the packages to the newest version
4. Run & fix tests;
5. Commit, deploy