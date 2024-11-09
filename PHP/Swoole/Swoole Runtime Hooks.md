Runtime hooks are killer feature of [[Swoole]].

Most of the common built-in I/O-blocking functions like `file_get_contents`,  `sleep` easily become non-blocking with [[Swoole extension]].

This includes:
- pdo_mysql
- pdo_pgsql
- redis
- curl



