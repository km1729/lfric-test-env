CREATE TABLE model_config2 (
    id serial PRIMARY KEY,
    model VARCHAR NOT NULL, -- lfric_atm
    config VARCHAR, -- thai_ben1
    resolution VARCHAR, -- C48_MG_dt-1800p0
    thread INTEGER, -- 1
    ncpus VARCHAR, -- mpi * thread
    compiler VARCHAR, -- gnu or intel
    optimizer VARCHAR -- full debug
);

CREATE TABLE model_run2 (
    id serial PRIMARY KEY,
    datetime TIMESTAMP,
    revision INTEGER,
    model_config_id INTEGER REFERENCES model_config2 (id)
);

CREATE TABLE model_profile2 (
    id serial PRIMARY KEY,
    routine VARCHAR,
    min_time NUMERIC(10,2),
    mean_time NUMERIC(10,2),
    max_time NUMERIC(10,2),
    no_calls INTEGER,
    time_perc NUMERIC(10,2),
    time_per_call NUMERIC(10,2),
    model_run_id INTEGER REFERENCES model_run2 (id)
);

CREATE VIEW model_view2 as (
    SELECT mc.model,
        mc.resolution,
        mc.thread,
        mc.ncpus,
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
    FROM model_run2 mr
        JOIN model_config2 mc ON mr.model_config_id = mc.id
        JOIN model_profile2 mp ON mp.model_run_id = mr.id
);