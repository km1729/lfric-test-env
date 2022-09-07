INSERT INTO model_config (model, resolution, thread, process, config) VALUES( 'model_a', 'c16_dt3600', '1', '6', 'breeze'); 
INSERT INTO model_config (model, resolution, thread, process, config) VALUES( 'model_b', 'c16_dt3600', '1', '6', 'breeze');

INSERT INTO model_run (datetime, revision, model_config_id) VALUES('2015-01-10 00:51:14', 25464,1);
INSERT INTO model_run (datetime, revision, model_config_id) VALUES('2015-02-10 00:51:14', 25485,1);
INSERT INTO model_run (datetime, revision, model_config_id) VALUES('2015-03-10 00:51:14', 26554,1);
INSERT INTO model_run (datetime, revision, model_config_id) VALUES('2015-01-10 00:51:14', 25464,2);
INSERT INTO model_run (datetime, revision, model_config_id) VALUES('2015-02-10 00:51:14', 25485,2);
INSERT INTO model_run (datetime, revision, model_config_id) VALUES('2015-03-10 00:51:14', 26554,2);

INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine1', 23.85, 24, 25, 1, 100, 23.9, 1);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine2', 3, 4, 5, 1, 13.5, 3.23, 1);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine3', 0.17, 0.17, 0.17, 0.72, 0.17, 1);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine1', 23.85, 24, 25, 1, 100, 23.9, 2);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine2', 3, 4, 5, 1, 13.5, 3.23, 2);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine3', 0.17, 0.17, 0.17, 0.72, 0.17, 2);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine1', 23.85, 24, 25, 1, 100, 23.9, 3);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine2', 3, 4, 5, 1, 13.5, 3.23, 3);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine3', 0.17, 0.17, 0.17, 0.72, 0.17, 3);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine1', 23.85, 24, 25, 1, 100, 23.9, 4);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine2', 3, 4, 5, 1, 13.5, 3.23, 4);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine3', 0.17, 0.17, 0.17, 0.72, 0.17, 4);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine1', 23.85, 24, 25, 1, 100, 23.9, 15);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine2', 3, 4, 5, 1, 13.5, 3.23, 5);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine3', 0.17, 0.17, 0.17, 0.72, 0.17, 5);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine1', 23.85, 24, 25, 1, 100, 23.9, 6);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine2', 3, 4, 5, 1, 13.5, 3.23, 6);
INSERT INTO model_profile (routine, min_time, mean_time, max_time, no_calls, time_perc, timer_per_call, model_run_id) VALUES('routine3', 0.17, 0.17, 0.17, 0.72, 0.17, 6);