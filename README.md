This repository provides a test environment to be able to use Jupyter lab and PostgreSQL via docker-compose file.  

## Structure  

<pre>
|__ code
|   |- psql.py
|   |- schema.py
|   |- server_setting.py
|   |- upload.py
|__ sql
|   |- create-tables.sql
|   |- values.sql
|- docker-compose.yml
|- Dockerfile
|- environment.yml
|- README.md

</pre>
## run docker compose file  
- it will create jupyter lab and postgres images and containers  
```bash
docker compose up
```

User can stop and start a container at any time
```bash
docker stop 823e5551c4ae #container id
docker start 823e5551c4ae
```
## Access Jupyterlab  
Open a browser and type <code>localhost:8888</code>  
TOKEN=easy  


