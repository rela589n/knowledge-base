---
aliases:
  - PHP Docker extension installer
  - install-php-extensions
---
The default `docker-php-ext-install` provided by PHP does not install apt/apk libraries that may be needed for extension (see [[PHP ext-pgsql extension docker installation|ext-pgsql installation]] for example).

Therefore, [`docker-php-extension-installer`](https://github.com/mlocati/docker-php-extension-installer) project was created that provides us with the main `install-php-extensions` command.
