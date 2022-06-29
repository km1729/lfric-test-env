This document contains UML of Python code for daily updating lfric reports to grafana database.   

# orm_update.py  
```mermaid
flowchart LR
%%{init: {'theme': 'neutral' } }%%  
    subgraph 1[setting]
        11[set file_directory] --> 12[define a model]
        12 --> 13[define a model_run]
    end

    subgraph 2[model_configuration]
        model_config{check if the model<br/> exist in db}
        model_config -->|yes| db_id[get<br/>model_cofing_id]  
        model_config -->|no| db_add[update <br/> the new model]
        db_add --> db_id
    end    

    subgraph 3[model_run]
        model_run{check if the model_run<br/> exist in db}
        model_run --> |yes|db_id2[get<br/>model_run_id]  
        model_run --> |no| db_add2[update <br/>the model_run <br/>with<b> model_cofing_id</b>]
        db_add2 --> db_id2
    end

    subgraph 4[model_profile]
        41[define a model_profile]
        42[update the model_profile <br/> with the <b>model_run_id</b>]
        41--->42  
    end
    1 --> 2-->3-->4

    style db_id fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5    
    style db_id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5

```
# file relations  
```mermaid
flowchart LR
    a[psql.py]
    b[setting.py]
    c[orm_schema.py]
    d[orm_upload.py]
    b --> a
    a --- c
    a --- d
    c --- d
```
**setting.py**: Database connection configuration.  
**psql.py**: Create database connection and session.  
**orm_schema.py**: Declare a mapping to interact with the database tables, columns and constraints and so on.  
**orm_upload.py**: Define a model and test results from report(s). Then update the data to the databae.  


# References  
- [sqlalchemy official](https://docs.sqlalchemy.org/en/14/index.html)  
