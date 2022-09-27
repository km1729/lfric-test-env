from pathlib import Path
from psql import db, session
from schema import model_config, model_profile, model_run
from datetime import datetime
import re
import sys

# file path: Timer file
timerFileList = list(Path("/scratch/hc46/hc46_gitlab/cylc-run").rglob("timer.txt"))

# file path: model config infrom from the resource control 
rcFileLfric = Path('/scratch/hc46/hc46_gitlab/cylc-run/lfric_atm_nightly/suite_control.rc')
rcFileGungho = Path('/scratch/hc46/hc46_gitlab/cylc-run/gungho_nightly/suite_control.rc')

# file path: revision
revFilehGungho = Path('/scratch/hc46/hc46_gitlab/cylc-run/gungho_nightly/revision')
revFileLfric = Path('/scratch/hc46/hc46_gitlab/cylc-run/lfric_atm_nightly/revision')
                    
# re: weekly setup has been removed therefore it has to changed to performance to get data >> find another way
# it can be changed !!!! nightly bom
nightlySetup = r'(?:\'nightly\':\s\[)([\s\S\w]+)(?:\'performance\')'

# re: model configuration 
configuration = r'(?:run_gungho_|run_lfric_atm_)+([a-z0-9_.-]+[^_A-Z])'
modelReolustion = r'([A-Z]+[.\d_\w-]+)(?:_intel|_gnu|_cray)'
compiler = r'intel|gnu|cray'
optimizationLevel=r'fast-debug$|full-debug$'
mpi = r'(?:mpi_parts\":\b)(\d{1,3})'
thread = r'(?:threads\":\b)(\d{1,3})'

# get lfric & gungho config date from suite_control.rc file
with open(rcFileLfric, 'r') as f:
    lfricSuiteControl = f.read()
    lfricNightlySetupData = ''.join(re.findall(nightlySetup, lfricSuiteControl))
    
with open(rcFileGungho, 'r') as f:
    gunghoSuiteControl = f.read()
    gunghoNightlySetupData = ''.join(re.findall(nightlySetup, gunghoSuiteControl))
    
# get revision #
with open(revFileLfric, 'r') as f:
    lfricRevision = f.read()
    
with open(revFilehGungho, 'r') as f:
    gunghoRevision = f.read()

print(lfricRevision,gunghoRevision)

# get model information from TIMER file
# find timer files from the path
for file in timerFileList: #Pathtype
    #change Path to list to use the startwith()to find the model timer files 
    pathToList = list(str(file).split("/")) 

    # /work/1/ dirctory
    if pathToList[7] == '1':
        
        for fName in pathToList:
            if fName.startswith('run_lfric'):
                c_timestamp = file.stat().st_ctime
                # convert creation timestamp into DateTime object
                c_time = datetime.datetime.fromtimestamp(c_timestamp)
                print('Created on:', c_time)
                print(f"model: lfric_atm")
                modelConfiguration = ''.join(re.findall(configuration,fName))
                print(f"model config: {modelConfiguration}")
                print(f"resolution: {''.join(re.findall(modelReolustion,fName))}")
                print(f"compiler: {''.join(re.findall(compiler,fName))}")
                print(f"optimizer: {''.join(re.findall(optimizationLevel,fName))}")
                
                # the function(configDataFromRc) not working, in the desktop > works                
                modelConfigData = re.search('('+modelConfiguration+'\\b)(?:.*?)(env=\{(.*?)})',lfricNightlySetupData,  re.MULTILINE | re.DOTALL )
                if modelConfigData:
                    print(f"mpi: {''.join(re.findall(mpi,modelConfigData.group()))}")
                    print(f"thread: {''.join(re.findall(thread,modelConfigData.group()))}")
                else:
                    print(f" '{modelConfiguration}' has no configuration data")
                
                print()


            elif fName.startswith('run_gungho'):
                print(f"model: gungho")
                modelConfiguration = ''.join(re.findall(configuration,fName))
                print(f"model config: {modelConfiguration}")
                print(f"resolution: {''.join(re.findall(modelReolustion,fName))}")
                print(f"compiler: {''.join(re.findall(compiler,fName))}")
                print(f"optimizer: {''.join(re.findall(optimizationLevel,fName))}")
                
                # the function(configDataFromRc) not working, in the desktop > works                
                modelConfigData = re.search('('+modelConfiguration+'\\b)(?:.*?)(env=\{(.*?)})',gunghoNightlySetupData,  re.MULTILINE | re.DOTALL )
                if modelConfigData:
                    print(f"mpi: {''.join(re.findall(mpi,modelConfigData.group()))}")
                    print(f"thread: {''.join(re.findall(thread,modelConfigData.group()))}")
                else:
                    print(f" '{modelConfiguration}' has no configuration data")
                
                print()

            else:
                pass
            

model_name = sys.argv[2]
num_procs = sys.argv[3]
path = sys.argv[1] + '/src_' + model_name + '_intel_production/' + model_name
num_thread='1'
model_resolution='c16_dt3600'
configuration='canned'

file = open('/scratch/hc46/hc46_gitlab/artefacts/' + model_name  + '_intel_production/revision')
revision = file.readline().rstrip('\n')
file.close()
file = open('/scratch/hc46/hc46_gitlab/artefacts/' + model_name  + '_intel_production/date')
date2 = file.readline().rstrip('\n')
date = datetime.strptime(date2,'%Y%m%d%H%M%S')
file.close()
file = path + '/example/timer.txt'

if model_name == 'gungho':
    model_id = 1
elif model_name == 'lfric_atm':
    model_id = 2
else:
    raise Exception('Invalid model name: {0}'.format(model_name))

'''
model_config
10 /Jun/2022 
At this time, the timer is only use for the gunho c16_dt3600 model.
!!! new model required to have the following information some where in the txt file (title or the first line)
    model, resultion, thread, process and config
'''

isExist_model = session.query(model_config.id).filter(model_config.model == model_name, model_config.resolution == model_resolution, \
    model_config.thread == num_thread, model_config.process == num_procs, model_config.config == configuration).all()
new_model = model_config(model=model_name,resolution=model_resolution,\
    thread=num_thread, process=num_procs,config=configuration)

if isExist_model is None:
    session.add(new_model)
    print(f'new model {0} added'.format(model_name))
    session.commit()


'''
model_run
'''
print(file, revision, date)

isExist_run = session.query(model_run.id).filter(model_run.revision == revision, model_run.datetime == date ).all()

new_run = model_run(datetime = date, revision = revision, model_config_id = model_id)

if isExist_run == []:
    session.add(new_run)
    print(f'new run added')
    session.commit()

'''
model profile
'''
get_run_id = session.query(model_run.id).filter(model_run.revision == revision, model_run.datetime == date ).one()
print(get_run_id[0])
print(num_procs)
     
with open (file, 'r') as f:
    next(f)
    for l in f:
        # replace the routine column values to '_' seperate text by removing space and comma 
        x = re.findall("[a-z_:][^|]+",l)
        routine = re.sub('[: ]+','_',x[0])

        # get min, mean, max, no_calls, time_perc and timer_per_call       
        replace_char = l.replace("||",",")
        list=''.join(replace_char.split(','))
        list = list.split()
        min = list[-6]
        mean = list[-5]
        max = list[-4]
        no_calls = list[-3]
        time_perc = list[-2]
        time_per_call = list[-1]
                
        new_model_profile = model_profile( \
            routine = routine,
            min_time = min,
            mean_time = mean,
            max_time = max,
            no_calls = no_calls,
            time_perc = time_perc,
            time_per_call = time_per_call,
            model_run_id = get_run_id[0]
            )

        session.add(new_model_profile)
        session.commit()

session.close()
