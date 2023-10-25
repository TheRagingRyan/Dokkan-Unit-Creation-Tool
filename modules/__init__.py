import subprocess
import os
import ast
from pathlib import Path

### Check for modules on run time
def module_check() -> bool:
    modules_to_check = ['dearpygui', 'pyautogui', 'easygui', 'bs4', 'requests', 'PIL', 'pypresence', 'icecream', 'urllib3']
    modules_to_install = ['dearpygui', 'pyautogui', 'easygui', 'beautifulsoup4', 'requests', 'Pillow', 'pypresence', 'icecream', 'urllib3==1.26.7']
    
    for i in range(len(modules_to_check)):
        try:
            __import__(modules_to_check[i])
        except Exception as e:
            print(e)
            subprocess.check_call(['pip', 'install', modules_to_install[i]])
    return True

module_check()
#########################################################################################################################################################  
from . functions import Config_AIO
from . classes import Leader_Skill_Info
from . configs import Config_Read

Config_Path = str(Path.home()) + '/Unit Creation Tool' + '/config.ini'


### Necessary for program to run properly. 
### Asks for decrypted database location, as well as grab categories from the Dokkan.wiki and save them to the config.
if not os.path.exists(Config_Path):
    Config_AIO()
    
config = Config_Read()



### Read the config to grab said categories for use in the program
cat_list = config.get('GLB_Categories', 'categories_list')
cat_list = ast.literal_eval(cat_list)
Leader_Skill_Info.cat_list = sorted(cat_list)



### Delete log file if it exists (only meant for Leader Skill really, cause that is the most convoluted section of the whole program)
if os.path.exists('error_log.txt'):
    os.remove('error_log.txt')
    