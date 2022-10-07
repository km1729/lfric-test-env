from pathlib import Path
import re
import yaml

with open ('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

timerFileList = Path(data['timerFile'])
print(timerFileList)

for key, value in data:
    print(key, ' : ', value)


