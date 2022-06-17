import pathlib
from psql import db, session
from orm_schema import model_config, model_profile, model_run
import re

# dir for input files
file_input_path='file/'
p = pathlib.Path(file_input_path)
f_list = list(p.glob('**/*.txt'))

'''
model_config
10 /Jun/2022 
At this time, the timer is only use for the gunho c16_dt3600 model.
!!! new model required to have the following information some where in the txt file (title or the first line)
    model, resultion, thread, process and config
'''

model = session.query(model_config.id).filter(model_config.model == 'gungho').all()
gungho = model_config(model='gungho',resolution='c16_dt3600',\
    thread='1',process='6',config='canned')

# session.add(gunho)

if model is None:
    session.add(gungho)
    print(f'new model added')
    session.commit()

# get model_run variables from title 

for file in f_list: 
    '''
    model_run

    '''
    if len(file.stem) < 12 & file.stem.startswith('timer_'):
        revision = file.stem[6:]
        date = file.parts[1]

        cc_run = session.query(model_run.id).filter(model_run.revision == revision, model_run.datetime == date ).all()
        # print(cc_run)
        new_run = model_run(datetime = date, revision = revision, model_config_id = 1) #cc_run

        if cc_run == []:
            session.add(new_run)
            print(f'new run added')
            session.commit()


        '''
        model profile
        '''
        get_run_id = session.query(model_run.id).filter(model_run.revision == revision, model_run.datetime == date ).one()
        print(get_run_id[0])
        print(type(get_run_id[0]))
     
        with open (file, 'r') as f:
            next(f)
            for l in f:
                # replace the routine column values to '_' seperate text by removing space and comma 
                x = re.findall("[a-z_:][^|]+",l)
                routine = re.sub('[: ]+','_',x[0])
                # create list      
                replace_char = l.replace("||",",")
                list=''.join(replace_char.split(','))
                list = list.split()
                 # get min, mean, max, no_calls, time_perc and timer_per_call   
                min = list[-6]
                mean = list[-5]
                max = list[-4]
                no_calls = list[-3]
                time_perc = list[-2]
                time_per_call = list[-1]
                
                cc_model_profile = model_profile( \
                    routine = routine,
                    min_time = min,
                    mean_time = mean,
                    max_time = max,
                    no_calls = no_calls,
                    time_perc = time_perc,
                    time_per_call = time_per_call,
                    model_run_id = get_run_id[0]
                    )

                session.add(cc_model_profile)
                session.commit()

session.close()


