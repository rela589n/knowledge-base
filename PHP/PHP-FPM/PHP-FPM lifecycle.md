Explanation: https://medium.com/@mgonzalezbaile/demystifying-nginx-and-php-fpm-for-php-developers-bba548dd38f9

Configuration: https://www.php.net/manual/en/install.fpm.configuration.php

PHP-fpm could only work along with [[Nginx]], since it could not handle incoming requests by itself.

![[Pasted image 20240914203127.png]]

See [[PHP-FPM strategies]].
See [[PHP-FPM configuration]].

PHP-FPM provides a status page, which could provide monitoring insights about active and idle fpm processes.
