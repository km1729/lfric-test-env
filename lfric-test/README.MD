postgres timezone update

```sql

SHOW timezone;

ALTER DATABASE db_name SET timezone = 'Asia/Seoul';

service postgresql restart

```