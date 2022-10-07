

```bash
#run docker compose file - it will create jupyter lab and postgres containers
docker compose up
```

Stop and Start a container  
```bash

```

Open a browser and type localhost:8888
token: easy  

postgres timezone update

```sql

SHOW timezone;

ALTER DATABASE db_name SET timezone = 'Asia/Seoul';

service postgresql restart

```
