CREATE TABLE model_config (
    id serial PRIMARY KEY,
    model VARCHAR NOT NULL,
    resolution VARCHAR,
    thread VARCHAR,
    process VARCHAR,
    config VARCHAR
);

CREATE TABLE model_run (
    id serial PRIMARY KEY,
    datetime TIMESTAMP,
    revision INTEGER,
    model_config_id INTEGER REFERENCES model_config (id)
);

CREATE TABLE model_profile (
    id serial PRIMARY KEY,
    routine VARCHAR,
    min_time NUMERIC(10,2),
    mean_time NUMERIC(10,2),
    max_time NUMERIC(10,2),
    no_calls INTEGER,
    time_perc NUMERIC(10,2),
    time_per_call NUMERIC(10,2),
    model_run_id INTEGER REFERENCES model_run (id)
);

CREATE VIEW model_view as (
    SELECT mc.model,
        mc.resolution,
        mc.thread,
        mc.process,
        mc.config,
        mr.datetime,
        mr.revision,
        mp.routine,
        mp.min_time,
        mp.mean_time,
        mp.max_time,
        mp.no_calls,
        mp.time_perc,
        mp.time_per_call
    FROM model_run mr
        JOIN model_config mc ON mr.model_config_id = mc.id
        JOIN model_profile mp ON mp.model_run_id = mr.id
);