Install packages from [packagist](https://packagist.org/)

Useful commands:

- `composer outdated` (check for outdated packages);
- `composer why-not` (check for version constraints not allowing us to upgrade);
- `composer recipes:update` - update symfony-packages automatically;

In order to upgrade symfony to a new version,
consider following approach:

## Dev-deps

Upgrade all dev packages to the latest versions,
so that CI would be able to run on new set of dev-packages.

## Small Packages

1. Upgrade all outdated third-party packages, except `symfony/*` (though, it would be nice to upgarde symfony to latest minor version).
2. Run & fix tests
3. Commit, deploy

## Main Upgrade

When it has all been successfully tested and works correctly, perform the main upgarde:

1. Upgarde symfony packages (remember, currently there should be not that much dependency issues, because of first phase).
2. Run & fix tests;
3. Upgrade rest of the packages to the newest version
4. Run & fix tests;
5. Commit, deploy