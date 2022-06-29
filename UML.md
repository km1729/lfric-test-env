This document contains UML of Python code for daily updating lfric reports to grafana database. 

# orm_update.py UML
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
        model_run --> |no| db_add2[update <br/>the model_run <br/>with model_cofing_id]
        db_add2 --> db_id2
    end

    subgraph 4[model_profile]
        41[define a model_profile]
        42[update the model_profile <br/> with the model_run_id]
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
**psql.py**: Create databse connection and session  
**orm_schema.py**: Define database tables and columns to be able interact with database  
**orm_upload.py**:   


# References
- [sqlalchemy official](https://docs.sqlalchemy.org/en/14/index.html)