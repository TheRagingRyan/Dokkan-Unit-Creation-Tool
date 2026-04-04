import os
from pathlib import Path


### Delete log file if it exists (only meant for Leader Skill really, cause that is the most convoluted section of the whole program)
if os.path.exists('error_log.txt'):
    os.remove('error_log.txt')

#########################################################################################################################################################  
from . functions import Config_AIO
from . discord import Initialize_Discord_Presence
config_path = 'config/config.ini'


### Necessary for program to run properly. 
### Asks for decrypted database location, as well as grab categories from the Dokkan.wiki and save them to the config.
if not os.path.exists(config_path):
    Config_AIO()

RPC = Initialize_Discord_Presence()
    
# config = Config_Read()



### Read the config to grab said categories for use in the program
# cat_list = config.get('GLB_Categories', 'categories_list')
# cat_list = ast.literal_eval(cat_list)
# Leader_Skill_Info.cat_list = sorted(cat_list)





    