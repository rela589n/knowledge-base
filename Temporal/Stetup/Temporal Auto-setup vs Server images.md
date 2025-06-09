In [[Temporal]], [[Temporal Auto-setup|Auto-setup]] image is used mostly for local development, as it creates database (runs migrations), creates default namespace.

For production usage, use [[Temporal Server setup|Server setup]]. To migrate database, you'd likely need `temporal-sql-tool`, and to create namespace `admin-tools`.
