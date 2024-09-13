```yaml
services:  
    postgresql:  
        image: postgres:17rc1  
        healthcheck:  
            test: [ "CMD", "pg_isready", "-d", "project_db", "-U", "${DATABASE_USER:-postgres}" ]  
            timeout: 5s  
            retries: 5  
            start_period: 60s  
        environment:  
            PGDATA: "/var/lib/postgresql/data/pgdata"  
            POSTGRES_PASSWORD: "qwerty"  
            POSTGRES_DB: "project_db"  
            POSTGRES_USER: ${DATABASE_USER:-postgres}  
        volumes:  
            - "postgresdata:/var/lib/postgresql/data"  
        ports:  
            - "127.0.0.1:15432:5432"  
  
volumes:  
    postgresdata: ~
```

