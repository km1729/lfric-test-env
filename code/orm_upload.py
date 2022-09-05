import pathlib
from psql import db, session
from orm_schema import model_config, model_profile, model_run
import re

# dir for input files
file_input_path='./file'
p = pathlib.Path(file_input_path)
f_list = list(p.glob('**/*.txt'))

# model configuration
model_name = 'atm'
num_procss = '6'
num_thread='1'
model_resolution='c16_dt3600'
configuration='canned'

isExist_model = session.query(model_config).filter(\
            model_config.model == model_name, \
            model_config.resolution == model_resolution, \
            model_config.thread == num_thread, \
            model_config.process == num_procss, \
            model_config.config == configuration).all()

new_model = model_config(model=model_name, resolution=model_resolution,\
    thread=num_thread, process=num_procss, config=configuration)

if isExist_model==[]:
    session.add(new_model)
    print(f'new model {model_name} added')
    session.commit()

# for file in f_list: 
#     # Model_config
#     if len(file.stem) < 12 and file.stem.startswith('timer_'):         

        #Model_run
        # revision = file.stem[6:]
        # date = file.parts[1]

        # print(file, revision, date)

        # isExist_run = session.query(model_run.id).filter(model_run.revision == revision, model_run.datetime == date ).all()
        # print(isExist_run)

        # new_run = model_run(datetime = date, revision = revision, model_config_id = isExist_model)

        # if isExist_run == []:
        #     session.add(new_run)
        #     print(f'new run added')
        #     session.commit()


        # '''
        # model profile
        # '''
        # get_run_id = session.query(model_run.id).filter(model_run.revision == revision, model_run.datetime == date ).one()
        # print(get_run_id[0])
        # print(type(get_run_id[0]))
     
        # with open (file, 'r') as f:
        #     next(f)
        #     for l in f:
        #         # replace the routine column values to '_' seperate text by removing space and comma 
        #         x = re.findall("[a-z_:][^|]+",l)
        #         routine = re.sub('[: ]+','_',x[0])

        #         # get min, mean, max, no_calls, time_perc and timer_per_call       
        #         replace_char = l.replace("||",",")
        #         list=''.join(replace_char.split(','))
        #         list = list.split()
        #         min = list[-6]
        #         mean = list[-5]
        #         max = list[-4]
        #         no_calls = list[-3]
        #         time_perc = list[-2]
        #         time_per_call = list[-1]
                
        #         cc_model_profile = model_profile( \
        #             routine = routine,
        #             min_time = min,
        #             mean_time = mean,
        #             max_time = max,
        #             no_calls = no_calls,
        #             time_perc = time_perc,
        #             time_per_call = time_per_call,
        #             model_run_id = get_run_id[0]
        #             )

        #         session.add(cc_model_profile)
        #         session.commit()

# session.close()