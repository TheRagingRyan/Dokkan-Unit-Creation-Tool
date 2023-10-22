import os
import ast
from pathlib import Path
from . functions import Config_AIO
from . configs import Config_Read
from . classes import Leader_Skill_Info
Config_Path = str(Path.home()) + '/Unit Creation Tool' + '/config.ini'

if not os.path.exists(Config_Path):
    Config_AIO()


config = Config_Read()
cat_list = config.get('GLB_Categories', 'categories_list')
cat_list = ast.literal_eval(cat_list)
Leader_Skill_Info.cat_list = sorted(cat_list)
### Delete log file if it exists
if os.path.exists('error_log.txt'):
    os.remove('error_log.txt')
    