# from colorama import Fore as fore
# from colorama import Style as style
# from colorama import init as colorama_init
import sqlite3
import os
import re
from dearpygui.dearpygui import *
from . configs import Config_Read
from . passive import Passive_Skill
from . specials import Card_Specials
from . active_skill import Active_Skill_Set
from . classes import Causality, Widget_Aliases, String_Length, Database
from . functions import Delete_Items, Row_Checker, Table_ID, Text_Resize, Card_Checker
from . leader import Leader_Skill_Info

os.system("")

class style():
    
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
class Tooltip_Info:
    
    tag_id = []
    
# colorama_init()
#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################


# print(f'{style.RED}Hello everyone!{style.RESET} it\'s a {style.BLUE} beautiful')
def Causality_Query(causality):
    
    config = Config_Read()
    
    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
    cur = con.cursor()
    
    cur.execute("SELECT causality_type, cau_val1, cau_val2, cau_val3 FROM skill_causalities WHERE id = " + str(causality))
    causality_type = cur.fetchall()
    # cau_val1
    cur.execute("SELECT cau_val1 FROM skill_causalities WHERE id = " + str(causality))
    cau_val1 = cur.fetchall()
    #cau_val2
    cur.execute("SELECT cau_val2 FROM skill_causalities WHERE id = " + str(causality))
    cau_val2 = cur.fetchall()
    #cau_val3
    cur.execute("SELECT cau_val3 FROM skill_causalities WHERE id = " + str(causality))
    cau_val3 = cur.fetchall()

    # counter = 0
    # while counter < 1:
    for i in cau_val1:
        cau_val1 = cau_val1[0]
    for i in cau_val2:
        cau_val2 = cau_val2[0]
    for i in cau_val3:
        cau_val3 = cau_val3[0]

    info = 0
    
    for item in causality_type:

        if item[0] == 0:
            causality_type = f'(Type: 0) Is None Rule'

        elif item[0] == 1:
            causality_type = f'(Type: 1) When HP is over {str(cau_val1[0])}%'

        elif item[0] == 2:
            causality_type = f'(Type: 2) When HP is below {str(cau_val1[0])}%'

        elif item[0] == 3:
            
            Ki_Number = (cau_val1[0] / 100) * get_value('eball_mod_num100') 
            
            if get_value('Card_Rarity') == 5 and Ki_Number == 24:
                causality_type = f'(Type: 3) When Ki is {str(int(Ki_Number))}'
            elif get_value('Card_Rarity') == 4 and Ki_Number == 12:
                causality_type = f'(Type: 3) When Ki is {str(int(Ki_Number))}'
            else:
                causality_type = f'(Type: 3) When Ki is over {str(int(Ki_Number))}'
                
            c_val1 = cau_val1[0] / 100
            # Real_Ki = float(c_val1) * Ki[0]
            # extra_info = f'(When Ki is over {c_val1})'
            # info = 1

            # extra_info = f'(cau_val1 = ({str(c_val1)}) * eball_mod_num100)'
            # info = 1

        elif item[0] == 4:
            
            Ki_Number = (cau_val1[0] / 100) * get_value('eball_mod_num100')
            causality_type = f'(Type: 4) When Ki is Under {str(int(Ki_Number))}'

            c_val1 = cau_val1[0] / 100
            # extra_info = f'(When Ki is over {Real_Ki})'
            # info = 1

            # c_val1 = cau_val1[0] / 100
            # extra_info = f'(cau_val1 = ({str(c_val1)}) * eball_mod_num100)'
            # info = 1

        elif item[0] == 5:
            causality_type = f'(Type: 5) When Battle has past {str(cau_val1[0])} turns'

        elif item[0] == 6:
            causality_type = f'(Type: 6) Does deck have {str(cau_val1[0])} link skill'

        elif item[0] == 7:
            causality_type = f'(Type: 7) Does enemy have {str(cau_val1[0])} link skill'

        elif item[0] == 8:
            causality_type = f'(Type: 8) Is ATK & DEF over {str(cau_val1[0])} {str(cau_val2[0])}'

        elif item[0] == 9:
            causality_type = f'(Type: 9) Is ATK & DEF below {str(cau_val1[0])} {str(cau_val2[0])}'

        elif item[0] == 10:
            causality_type = f'(Type: 10) Is HP over {str(cau_val1[0])}% and Ki above {str(cau_val2[0])}'

        elif item[0] == 11:
            causality_type = f'(Type: 11) Is HP over {str(cau_val1[0])}% and Ki below {str(cau_val2[0])}'

        elif item[0] == 12:
            causality_type = f'(Type: 12) Is HP below {str(cau_val1[0])}% and Ki above {str(cau_val2[0])}'

        elif item[0] == 13:
            causality_type = f'(Type: 13) Is HP below {str(cau_val1[0])}% and Ki below {str(cau_val2[0])}'

        elif item[0] == 14:
            causality_type = f'(Type: 14) Card is first attacker in turn {str(cau_val1[0])}'

        elif item[0] == 15:
            if cau_val1[0] == 1:
                causality_type = f'(Type: 15) When facing {str(cau_val1[0])} enemy'
            else:
                causality_type = f'(Type: 15) When facing {str(cau_val1[0])} or more enemies'

        elif item[0] == 16:
            if cau_val1[0] == 1:
                causality_type = f'(Type: 16) When facing {str(cau_val1[0])} enemy'
            elif cau_val2[0] >= 3:
                causality_type = f'(Type: 16) When facing {str(cau_val1[0] - 1)} or less enemies'
            else:
                causality_type = f'(Type: 16) When facing {str(cau_val1[0] - 1)} enemy'
        elif item[0] == 17:
            causality_type = f'(Type: 17) When enemies\' HP is above {str(cau_val1[0])}%'

        elif item[0] == 18:
            causality_type = f'(Type: 18) When enemies\' HP is below {str(cau_val1[0])}%'

        elif item[0] == 19:
            causality_type = f'(Type: 19) When card is in slot {str(cau_val1[0] + 1)}'

        elif item[0] == 20:
            causality_type = f'(Type: 20) When Ki is above {str(cau_val1[0])}%'

        elif item[0] == 21:
            causality_type = f'(Type: 21) When Ki is below {str(cau_val1[0])}%'

        elif item[0] == 22:
            causality_type = f'(Type: 22) When a character is in the deck {str(cau_val1[0])}%' # come back and add query to cau_val1[0], nothing uses this one though, (Maybe later on)

        elif item[0] == 23:
            causality_type = f'(Type: 23) If {str(cau_val1[0])} of links are active'

        elif item[0] == 24:
            causality_type = f'(Type: 24) When card is attacked'

        elif item[0] == 25:
            causality_type = f'(Type: 25) When card does a finishing blow'

        elif item[0] == 26:
            causality_type = f'(Type: 26) When HP is over {str(cau_val1[0])}% and has enough ki to super'

        elif item[0] == 27:
            causality_type = f'(Type: 27) When HP is below {str(cau_val1[0])}% and has enough ki to super'

        elif item[0] == 28:
            causality_type = f'(Type: 28) Checks if {str(cau_val1[0])} element is on rotation'

        elif item[0] == 29:
            causality_type = f'(Type: 29) Checks id {str(cau_val1[0])} is an ememy' # come back and add a query to cau_val1[0], nothing uses this, (Maybe later on)

        elif item[0] == 30:
            causality_type = f'(Type: 30) When guard is activated'

        elif item[0] == 31:
            causality_type = f'(Type: 31) When there are 3 or more enemy attacks'

        elif item[0] == 32:
            causality_type = f'(Type: 32) When there is {str(cau_val1[0])} type Ki on the field'

        elif item[0] == 33:
            causality_type = f'(Type: 33) When HP is between {str(cau_val1[0])}% and {str(cau_val2[0])}%'

        elif item[0] == 34:
            cur.execute(f'SELECT name FROM card_categories WHERE id = {cau_val2[0]}')
            category = cur.fetchone()
            if cau_val1[0] == 0 and cau_val3[0] == 1:
                enemy_type = 'ally on the team'
                causality_type = f'(Type: 34) When there is {str(cau_val3[0])} \'{str(category[0])}\' Category {str(enemy_type)}'
            elif cau_val1[0] == 0 and cau_val3[0] > 1:
                enemy_type = 'allies\' on the team'
                causality_type = f'(Type: 34) When there are {str(cau_val3[0])} \'{str(category[0])}\' Category {str(enemy_type)}'
            elif cau_val1[0] == 1 and cau_val3[0] == 1:
                enemy_type = 'enemy'
                causality_type = f'(Type: 34) When facing {str(cau_val3[0])} \'{str(category[0])}\' Category {str(enemy_type)}'
            elif cau_val1[0] == 1 and cau_val3[0] > 1:
                enemy_type = 'enemies\''
                causality_type = f'(Type: 34) When facing {str(cau_val3[0])} \'{str(category[0])}\' Category {str(enemy_type)}'
            elif cau_val1[0] == 2 and cau_val3[0] == 1:
                enemy_type = 'ally attacking in the same turn'
                causality_type = f'(Type: 34) When there is {str(cau_val3[0])} \'{str(category[0])}\' Category {str(enemy_type)}'
            elif cau_val1[0] == 2 and cau_val3[0] == 2:
                enemy_type = 'allies\' attacking in the same turn'
                causality_type = f'(Type: 34) When there are {str(cau_val3[0])} \'{str(category[0])}\' Category {str(enemy_type)}'
            elif cau_val1[0] == 2 and cau_val3[0] == 3:
                enemy_type = 'allies\'' # attacking in the same turn (Self Included)
                causality_type = f'(Type: 34) When everyone in the attacking turn are in \'{str(category[0])}\' Category'


                # come back later

        elif item[0] == 35:
            if cau_val1[0] == '126976':
                bitset = 'Super Class'
            elif cau_val1[0] == '4063232':
                bitset = 'Extreme Class'
            causality_type = f'(Type: 35) When the team consists of only {str(bitset)}'

        elif item[0] == 36:
            causality_type = f'(Type: 36) When HP is over {str(cau_val1[0])}% and battle has past turn {str(cau_val2[0])}'

        elif item[0] == 37:
            causality_type = f'(Type: 37) When HP is below {str(cau_val1[0])}% and battle has past turn {str(cau_val2[0])}'

        elif item[0] == 38:
            c_val2 ='0'
            c_val22 = '1'
            if cau_val1[0] == 16:
                c_val1 = 'ATK Down'
                causality_type = f'(Type: 38) When the enemy is in {str(c_val1)} status'
            elif cau_val1[0] == 32:
                c_val1 = 'DEF Down'
                causality_type = f'(Type: 38) When the enemy is in {str(c_val1)} status'
            elif cau_val1[0] == 48:
                c_val1 = 'ATK Down or DEF Down'
                causality_type = f'(Type: 38) When the enemy is in {str(c_val1)} status'
            elif cau_val1[0] == 256:
                c_val1 = 'Stunned'
                causality_type = f'(Type: 38) When the enemy is {str(c_val1)}'
            elif cau_val1[0] == 1024:
                c_val1 = 'Sealed'
                causality_type = f'(Type: 38) When the enemy is {str(c_val1)}'
            elif cau_val1[0] == 1040:
                c_val1 = 'Sealed or ATK Down'
                causality_type = f'(Type: 38) When the enemy is {str(c_val1)} status'                
            elif cau_val1[0] == 1072:
                c_val1 = 'Sealed, ATK Down or DEF Down'
                causality_type = f'(Type: 38) When the enemy is {str(c_val1)} status'
            elif cau_val1[0] == 1280:
                c_val1 = 'Stunned or Sealed'
                causality_type = f'(Type: 38) When the enemy is {str(c_val1)}'      
            elif cau_val1[0] == 1328:
                c_val1 = 'Stunned, Sealed, ATK Down, or DEF Down'
                causality_type = f'(Type: 38) When the enemy is {str(c_val1)} status'
            if cau_val2[0] == 0:
                c_val2 = f'0'

            elif cau_val2[0] == 1:
                c_val22 = f'1'    

            extra_info = (f'cau_val1 = {str(cau_val1[0])}\ncau_val2 = {str(cau_val2[0])} ({c_val2} = single status effect, {c_val22} = multiple status effects)\ncau_val3 = {str(cau_val3[0])}')
            # info = 1    

            # causality_type = f'(Type: 38) When the enemy is {str(cau_val1[0])}% and battle has past turn {str(cau_val2[0])}' # come back

        elif item[0] == 39:
            if cau_val1[0] == 32:
                bitset = 'Super Class'
            if cau_val1[0] == 64:
                bitset = 'Extreme Class'        
            causality_type = f'(Type: 39) When there is a {str(bitset)} enemy'

        elif item[0] == 40:
            causality_type = f'(Type: 40) Super Attack has been performed'

        elif item[0] == 41:

            cur.execute(f'SELECT card_unique_info_id FROM card_unique_info_set_relations WHERE card_unique_info_set_id = {cau_val2[0]}')
            Unique_Info = cur.fetchone()

            if Unique_Info is None:
                cur.execute(f'SELECT name FROM cards WHERE card_unique_info_id = {str(cau_val2[0])}')
                Unique_Info = cur.fetchone()

            else:

                cur.execute(f'SELECT name FROM card_unique_infos WHERE id = {str(Unique_Info[0])}')

            Card_Name = cur.fetchone()


            if cau_val1[0] == 0:
                enemy_type = 'on the team'
            elif cau_val1[0] == 1:
                enemy_type = 'an enemy'
            elif cau_val1[0] == 2:
                enemy_type = 'attacking in the same turn'
            if cau_val3[0] == 1:
                num_enemy = 'one'
            elif cau_val3[0] == 2:
                num_enemy = 'two'
            elif cau_val3[0] == 3:
                num_enemy = 'three'

            causality_type = f'(Type: 41) When {num_enemy} \'{str(Card_Name[0])}\' is {str(enemy_type)}'
            extra_info = f'cau_val1 = {str(cau_val1[0])} (0 = Team, 1 = Enemy, 2 = Same Turn)\ncau_val2 = {str(cau_val2[0])} (card_unique_info_set)\ncau_val3 = {str(cau_val3[0])} (# of character)'# Come Back Later
            # info = 1

        elif item[0] == 42:
            if cau_val1[0] == 63:
                sphere = f'Ki Spheres of any type'
                # causality_type = f'(Type: 42) When the card obtains {str(cau_val2[0])} {str(sphere)}'
            elif cau_val1[0] == 32:
                sphere = f'Rainbow Ki Spheres'
                # causality_type = f'(Type: 42) When the card obtains {str(cau_val2[0])} {str(sphere)}'
            elif cau_val1[0] == 16:
                sphere = f'PHY Ki Spheres'
            elif cau_val1[0] == 8:
                sphere = f'STR Ki Spheres'
            elif cau_val1[0] == 4:
                sphere = f'INT Ki Spheres'
            elif cau_val1[0] == 2:
                sphere = f'TEQ Ki Spheres'
            elif cau_val1[0] == 1:
                sphere = f'AGL Ki Spheres'


            causality_type = f'(Type: 42) When the card obtains {str(cau_val2[0])} {str(sphere)}'

        elif item[0] == 43:
            causality_type = f'(Type: 43) When the card evades an attack'

        elif item[0] == 44:
            if cau_val1[0] == 1:
                desc = 'Super Attacks have been performed'
                causality_type = f'(Type: 44) Every time {str(cau_val2[0])} {str(desc)}'
            elif cau_val1[0] == 2:
                desc = 'Attacks have been performed'
                causality_type = f'(Type: 44) Every time {str(cau_val2[0])} {str(desc)}'
            elif cau_val1[0] == 3:
                desc = 'Attacks have been received'
                causality_type = f'(Type: 44) Every time {str(cau_val2[0])} {str(desc)}'
            elif cau_val1[0] == 5:
                desc = 'Attacks have been evaded'
                causality_type = f'(Type: 44) Every time {str(cau_val2[0])} {str(desc)}'
            elif cau_val1[0] == 4:
                desc = 'Guard has been activated'
                causality_type = f'(Type: 44) Every time {str(desc)} {str(cau_val2[0])} times'


            extra_info = f'cau_val1 = {str(cau_val1[0])} (1 = SAs Performed, 2 = Attacks Performed, 3 = Attacks Received, 4 = Times Guard Activated, 5 = Attacks evaded\ncau_val2 = {str(cau_val2[0])} (# of cau_val1)\ncau_val3 = {str(cau_val3[0])}'# Come Back Later
            # info = 1

        elif item[0] == 45:
            if cau_val1[0] == 0:
                enemy_type = 'on the team'
            elif cau_val1[0] == 1:
                enemy_type = 'an enemy'
            elif cau_val1[0] == 2:
                enemy_type = 'attacking in the same turn'
            causality_type = f'(Type: 45) When {str(cau_val3[0])}is {str(enemy_type)} and is on {cau_val2[0]} Category'

        elif item[0] == 46:

            # if cau_val1[0] == 0:
            #     enemy_type = 'on the team'
            # elif cau_val1[0] == 1:
            #     enemy_type = 'an enemy'
            # elif cau_val1[0] == 2:
            #     enemy_type = 'attacking in the same turn'

            if cau_val2[0] == 64:
                element = 'Extreme Class'
            elif cau_val2[0] == 32:
                element = 'Super Class'
            elif cau_val2[0] != 32:
                element = '(' + str(cau_val2[0]) + ')'
            elif cau_val2[0] != 64:
                element = '(' + str(cau_val2[0]) + ')'

            #team/deck    
            if cau_val1[0] == 0 and cau_val3[0] == 1:
                causality_type = f'(Type: 46) When there is {str(cau_val3[0])} {str(element)} ally on the team'

            elif cau_val1[0] == 0 and cau_val3[0] > 1:
                causality_type = f'(Type: 46) When there are {str(cau_val3[0])} {str(element)} allies\' on the team'
            # enemy
            if cau_val1[0] == 1 and cau_val3[0] == 1:
                causality_type = f'(Type: 46) When there is {str(cau_val3[0])} {str(element)} enemy'

            elif cau_val1[0] == 1 and cau_val3[0] > 1:
                causality_type = f'(Type: 46) When there are {str(cau_val3[0])} {str(element)} enemies\''
            # same team
            if cau_val1[0] == 2 and cau_val3[0] == 1:

                causality_type = f'(Type: 46) When there is {str(cau_val3[0])} {str(element)} ally attacking in the same turn'
            elif cau_val1[0] == 2 and cau_val3[0] > 1:
                causality_type = f'(Type: 46) When there are {str(cau_val3[0])} {str(element)} allies\' attacking in the same turn'

            extra_info = f'cau_val1 = {str(cau_val1[0])} (0 = Team, 1 = Enemy, 2 = Same Turn)\ncau_val2 = {str(cau_val2[0])} (Type of Element)\ncau_val3 = {str(cau_val3[0])} (# of Element Type)\n'# Come Back Later
            # info = 1

        elif item[0] == 47:
            causality_type = f'(Type: 47) When the card revives'

        elif item[0] == 48:
            if cau_val1[0] == 1:
                sa_type = 'Ki Blast'

            elif cau_val1[0] == 2:
                sa_type = 'Unarmed'

            elif cau_val3[0] == 3:
                sa_type = 'Physical/Melee'
            else:
                sa_type = 'Undefined'

            causality_type = f'(Type: 48) Enemy Super Type is {str(sa_type)}'
            
        elif item[0] == 49:
            if cau_val1[0] == 1:
                sa_type = 'Ki Blast'

            elif cau_val1[0] == 2:
                sa_type = 'Unarmed'

            elif cau_val3[0] == 3:
                sa_type = 'Physical/Melee'
            else:
                sa_type = 'Undefined'
                
            causality_type = f'(Type: 49) When an {str(sa_type)} is directed at the character'

        elif item[0] == 51:
            if cau_val1[0] == 1:
                causality_type = f'(Type: 51) Skill lasts for {str(cau_val1[0])} turn from start of battle'
            else:
                causality_type = f'(Type: 51) Skill lasts for {str(cau_val1[0])} turns from start of battle'
                
        elif item[0] == 54:
            causality_type = f'(Type: 54) Starting from the turn in which the character\'s or an ally\'s Revival Skill is activated'
            
        elif item[0] == 55:
            causality_type = f'(Type: 55) Starting from the {str(cau_val1[0] + 1)}th turn'
            
        elif item[0] == 56:
            causality_type = f'(Type: 56) When normal attacks are directed at the character'
            
        elif item[0] == 56:
            causality_type = f'(Type: 58) Used with Dokkan Fields'
            
        else:
            causality_type = 'Causality not found in Causality_Query()'
            

        # print(causality_type)
        test = Tooltip_Info.tag_id
        

            
        # index_value = get_value('Query_Index_Number')
        # set_value(test[index_value], causality_type)
        # print(test[index_value])
        # print(index_value)
        
        
        # if operand == '&':
        #     for i in range(causality_list_length):
        #         text = get_value(test[index_value])
        #         if i + 1 == i:
        #             set_value(test[index_value], text + '\n' + text)
        #         else:
        #             set_value(test[index_value], text + '\n' + 'and' + text)
            
        # elif operand == '|':
        #     for i in range(causality_list_length):
        #         text = get_value(test[index_value])
        #         if i + 1 == i:
        #             text = get_value(test[index_value])
        #             set_value(test[index_value], text + '\n' + text)
        #         else:
        #             set_value(test[index_value], text + '\n' + 'or' + text)
            
        # set_value('Query_Index_Number', index_value + 1)
        return causality_type
            

#################################################################################################################################################################################################################################################################

# def Causality_Hint():
#     import json

#     causality = []
#     Tooltip_Info.tag_id.clear()
#     for i in range(get_value('Passive_Row_Check')):
        
#         if get_value(f'p_causality_conditions{i}') != 'NULL':
#             causality.append(get_value(f'p_causality_conditions{i}'))
#             Tooltip_Info.tag_id.append(f'causality_conditions{i}')
#             # print(f'p_causality_conditions{i} is not NULL')
#             # print(causality)
#     parsed_data_list = []

#     # Parse each JSON string and append the parsed object to the list
#     for json_str in causality:
#         parsed_data = json.loads(json_str)
#         parsed_data_list.append(parsed_data)

#     # Now you can work with the parsed JSON objects
#     for parsed_data in parsed_data_list:
#         source = parsed_data['source']
#         compiled = parsed_data['compiled']
        
#     for i in range(len(causality)):
#         causality[i] = causality[i].replace(causality[i].split('\"compiled\": ')[0], '')
#         causality[i] = causality[i].replace('\"compiled\": ', '').replace('}', '')

#     # print(causality[3])
#     import ast
    
    
#     for i in range(len(causality)):
        
#         # if '&' and '|' in causality[i]:
#         #     causality_value = ast.literal_eval(causality[i])
#         #     print('causality_value is ' + str(causality_value))
#         #     del causality_value[0]
#         #     for x in range(len(causality_value)):
                
#         #         text = Causality_Query(causality_value[i])
            
#         if '&' in causality[i]:
#             causality_value = ast.literal_eval(causality[i])
            
#             del causality_value[0]
#             for z in range(len(causality_value)):
#                 # text = get_value(Tooltip_Info.tag_id)
#                 text = Causality_Query(causality_value[z])
#                 if len(causality_value) != z + 1:
#                     # print(text)
#                     set_value(Tooltip_Info.tag_id[i], text + '\n' + 'and')
#                 else:
#                     val = get_value(Tooltip_Info.tag_id[i])
#                     # print(val)
#                     set_value(Tooltip_Info.tag_id[i], val + '\n' + text)
                
#             # print('& found')
#         elif '|' in causality[i]:
#             causality_value = ast.literal_eval(causality[i])

            
#             del causality_value[0]
#             for y in range(len(causality_value)):
#                 text = Causality_Query(causality_value[y])
#                 # print(Tooltip_Info.tag_id[i])
#                 if len(causality_value) != y + 1:
#                     set_value(Tooltip_Info.tag_id[i], text + '\n' + 'or')
#                 else:
#                     val = get_value(Tooltip_Info.tag_id[i])
#                     # print(val)
#                     set_value(Tooltip_Info.tag_id[i], val + '\n' + text)
            
#         else:
#             # print('else' + causality[i])
#             try:
#                 text = Causality_Query(causality[i])
#                 set_value(Tooltip_Info.tag_id[i], text)
#             except SystemError:
#                 pass
    # print(causality)
    # print(item['compiled'])

#################################################################################################################################################################################################################################################################         

def Causality_Hint():
    import json
    import ast
    
    # Creates the list used for Data_Check()
    def Create_List(causality_data):
        causality_list = '[' + causality_data + ']'
        causality_data = causality_list.replace('&',',\'&\',').replace('|',',\'|\',')
        causality_data = ast.literal_eval(causality_data)
        return causality_data
    
    # Rips the source from the causality so it can be used on Create_List()
    def Causality_Source(tag_id):
        causality = get_value(tag_id)
        causality_data = json.loads(causality)
        causality_data = causality_data["source"]
        return causality_data
    
    # Iterates through the list of causality ids and returns them in text for the tootip
    def Data_Check(causality_data):
        text = ''
        if '(' in causality_data:
            causality_data = causality_data.replace('(', '').replace(')', '')
            causality_list = Create_List(causality_data)
            for z in range(len(causality_list)):
                if causality_list[z] != '&' and causality_list[z] != '|':
                    text += Causality_Query(causality_list[z])
                    
                elif causality_list[z] == '&':
                    text += '\n' + 'and' + '\n'
                    
                elif causality_list[z] == '|':
                    text += '\n' + 'or' + '\n'
                    
        else:
            causality_list = Create_List(causality_data)
            for t in range(len(causality_list)):
                
                if causality_list[t] != '&' and causality_list[t] != '|':
                    text += Causality_Query(causality_list[t])
                    
                elif causality_list[t] == '&':
                    text += '\n' + 'and' + '\n'
                    
                elif causality_list[t] == '|':
                    text += '\n' + 'or' + '\n'
        return text
#################################################################################################
    
    # hints = ''
    causality = []
    causality.clear()
    Tooltip_Info.tag_id.clear()
    for card in range(Card_Checker()):
        for i in range(Row_Checker(f'Passive_Causality_Conditions_Card_{card}_Row_')):
            

            if get_value(f'Passive_Causality_Conditions_Card_{card}_Row_{i}') != 'NULL':
                # causality.append(get_value(f'p_causality_conditions{i}'))
                # Tooltip_Info.tag_id.append(f'causality_conditions{i}')

                causality_data = Causality_Source(f'Passive_Causality_Conditions_Card_{card}_Row_{i}')
                text = Data_Check(causality_data)

                if does_alias_exist(f'Passive_Causality_Conditions_Tooltip_{i}'):
                    delete_item(f'Passive_Causality_Conditions_Tooltip_{i}')

                with tooltip(f'Passive_Causality_Conditions_Card_{card}_Row_{i}', tag=f'Passive_Causality_Conditions_Card_{card}_Tooltip_{i}'):
                    add_text(text)
        
        num_of_specials = Row_Checker(f'Special#_Text_Card_{card}_')
        for special in range(num_of_specials):
            for i in range(2):
                if get_value(f'CS_causality_conditions_Card_{card}_Row_{special}{i}') != 'NULL':
                    causality_data = Causality_Source(f'CS_causality_conditions_Card_{card}_Row_{special}{i}')
                    text = Data_Check(causality_data)

                    # if does_alias_exist(f'cs{special_num + 1}_causality_conditions_0'):
                        # delete_item(f'cs{special_num + 1}_causality_conditions_0')
                    # if does_alias_exist(f'cs{special_num + 1}_causality_conditions_1'):
                        # delete_item(f'cs{special_num + 1}_causality_conditions_1')

                    with tooltip(f'CS_causality_conditions_Card_{card}_Row_{special}{i}'):
                        add_text(text)

                    
        # causality.clear() Active_Skill_Set_Causality_Card_0_Row_0
        if does_alias_exist(f'Active_Skill_Set_Card_{card}'):
            if get_value(f'Active_Skill_Set_Causality_Card_{card}_Row_0') != 'NULL':
                # 
                causality_data = Causality_Source(f'Active_Skill_Set_Causality_Card_{card}_Row_0')
                text = Data_Check(causality_data)
                # 
                if does_alias_exist('Active_Causality_Hint'):
                    delete_item('Active_Causality_Hint')
                            # 
                with tooltip(f'Active_Skill_Set_Causality_Card_{card}_Row_0', tag='Active_Causality_Hint'):
                    add_text(text)
            
    # for i in range(len(causality)):
    #     causality_data = json.loads(causality[i])
    #     causality_data = causality_data["source"]
        
    #     if '(' in causality[i]:
            
    #         pass
    
def Card_Unique_Infos():
    
    """Creates the list used in causality type 41 and 45
    
    """
    
    config = Config_Read()
    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)    
    cur = con.cursor()

    final_values = []
    card_unique_info_set_ids = []
    card_unique_infos_names = []
    card_unique_infos_set_lists = []
    card_unique_infos_set_card_names_lists = []

    ### Gets the card_unique_info_set_ids
    query = f'SELECT card_unique_info_set_id FROM card_unique_info_set_relations'
    cur.execute(query, (), )
    values = cur.fetchall()
    for tuple in range(len(values)):
        final_values.append(['NULL' if values[tuple][z] is None else values[tuple][z] for z in range(len(values[tuple]))])


    for item in final_values:
        if item not in card_unique_info_set_ids and item[0] != 0:
            card_unique_info_set_ids.append(item)
    #########################################################################################################################
    ### Gets the card_unique_infos
    for set in range(len(card_unique_info_set_ids)):
        query = f'SELECT name FROM card_unique_infos WHERE id = {str(card_unique_info_set_ids[set][0])}'
        cur.execute(query, (), )
        values = cur.fetchall()
        # print(values)
        for tuple in range(len(values)):
            card_unique_infos_names.append(['NULL' if values[tuple][z] is None else values[tuple][z] for z in range(len(values[tuple]))])

    #########################################################################################################################
    ### Gets all of the character's card_unique_info_ids using the card_unique_info_set_ids
    for set in range(len(card_unique_info_set_ids)):
        query = f'SELECT card_unique_info_id FROM card_unique_info_set_relations WHERE card_unique_info_set_id = {str(card_unique_info_set_ids[set][0])}'
        cur.execute(query, (), )
        values = cur.fetchall()
        # print(values)
        # for tuple in range(len(values)):
        card_unique_infos_set_lists.append(values)

    card_unique_infos_set_lists = [[item[0] for item in sublist] for sublist in card_unique_infos_set_lists]

    ### Gets the names for the card_unique_info_set_ids
    for set in range(len(card_unique_infos_set_lists)):
        means_to_an_end = []
        for unique_info_id in card_unique_infos_set_lists[set]:
            query = f'SELECT name FROM card_unique_infos WHERE id = {str(unique_info_id)}'
            cur.execute(query, (), )
            values = cur.fetchall()
            # print(values)
            # for tuple in range(len(values)):
            means_to_an_end.append(['NULL' if values[tuple][z] is None else values[tuple][z] for z in range(len(values[tuple]))])
        card_unique_infos_set_card_names_lists.append(means_to_an_end)



    # card_unique_infos_set_card_names = {card_unique_infos_names[i]: }

    ### Create a list of character names based on the first index of each list in order to get the first card name of the card_unique_infos_set
    card_unique_infos_first_name_list = []
    for list in range(len(card_unique_infos_set_card_names_lists)):
        card_unique_infos_first_name_list.append(card_unique_infos_set_card_names_lists[list][0])

    final_card_unique_infos_name_sets = []
    ### Create a list format for all of the card names in a set
    for set_of_names in range(len(card_unique_infos_set_card_names_lists)):
        means_to_an_end = []
        for name in card_unique_infos_set_card_names_lists[set_of_names]:
            means_to_an_end.append(name[0])
        final_card_unique_infos_name_sets.append(means_to_an_end)

    # print(final_card_unique_infos_name_sets[0])

    card_unique_infos_name_dict = {card_unique_infos_first_name_list[i][0]: final_card_unique_infos_name_sets[i] for i in range(len(card_unique_infos_set_card_names_lists))}

    return card_unique_infos_name_dict

def Create_JSON_Output(data):
    import ast
    source_text = data
    compiled_text = data
    text = ''
    dictionary = {}
    list_text = []
    if '&' in data and '|' in data and '(' not in data:
        num = ''
        for char in data:
            if char.isdigit():
                num += char
            else:
                if char == '|':
                    list_text.append(str(num) + ']')
                    num = ''
                else:
                    list_text.append('[' + str(num))
                    num = ''
        list_text.append(str(num) + ']')
        
        # list_text = eval(list_text)

        list_text = str(list_text)
        # list_text = list_text[:-1]
        # list_text = list_text[1:]
        list_text = list_text.replace('\'', '')
        list_text = eval(list_text)
        for i in range(len(list_text)):
            list_text[i] = str(list_text[i])[1:]
            list_text[i] = '[\"&\", ' + str(list_text[i])
        # for i in range(len(list_text)):
            # if 
        # print(str(list_text[0]))
        
        # print(list_text)
        # print(str(list_text)[1:])
        text = '[\"|\", ' + str(list_text)[1:].replace('\'', '')
        
        compiled_text = text
        
    elif '&' in data and '|' in data and '(' in data:
        if data[0] == '(':
            data = data.replace('(', '[').replace(')', ']').replace('|', ',').replace('&', ',')
            data = '[' + data + ']'
            data = eval(data)

            test_list = []
            list_text = ['\"|\" ']
            for i in range(len(data)):
                test_list.append(str(data[i]).replace('[', ', '))
            
            # print(test_list.)

            for i in range(len(data)):
                text += '[\"&\"' + test_list[i] + ', '

            
            text = '[\"|\", ' + text
            text = text[:-2] + ']'
            
            # print(text.replace(' , ', ' [\"|\", '))
            if ' , ' in text:
                compiled_text = text.replace(' , ', ' [\"|\", ')
            else:
                compiled_text = text
            
        else:
            data = data.replace('(', '[').replace(')', ']').replace('|', ',')
            dictionary = {}
            
            num = ''
            x = 0
            for char in data:
                x += 1
                num += char
                if char == '&':
                    data = data[x:]
                    break
                
            and_symbol = num[-1]
            
            text = '[\"'
        #             first_operand = 'and'
        #             break
                
        #         elif char == '|':
        #             first_operand = 'or'
        #             break
                
        #     if first_operand == 'and':
        #         pass
                
                # if char.isdigit():
                #     num += char
                # else:
                #     if char is '|':
                #         dictionary = {}
                #     num = ''
        
        print(data)
    
    elif '&' in data and '|' not in data:
        data = data.replace('&', ', ')
        data = '[\"&\", ' + data + ']'
        compiled_text = data
    
        
        
    elif '|' in data and '&' not in data:
        data = data.replace('|', ', ')
        data = '[\"|\", ' + data + ']'
        compiled_text = data
    
        
    compiled_text = '{' + '\"source\": ' + '\"' + source_text + '\"' + ', ' + '\"compiled\": ' + compiled_text + '}'
    return compiled_text

def Create_Causality_JSON():
    data = get_value('Causality_JSON_Input')

    compiled_output = Create_JSON_Output(data)
    set_value('Causality_JSON_Input', compiled_output)
    Text_Resize('Causality_JSON_Input')
    print(compiled_output)


def Ki_Calculation(tag_id, data):
    import math
    if get_value(f'eball_mod_num100_Card_0_Row_0'):
        eball_mod_num100 = int(get_value(f'eball_mod_num100_Card_0_Row_0'))
        
        if len(data) <= 2 and int(data) <= 24:
            causality_ki_value = (int(data) * 100) / eball_mod_num100
            set_value(tag_id, math.ceil(causality_ki_value))
            
    elif ':' in data:
        data = '{' + data + '}'
        data = eval(data)
        for key, value in data.items():
            print(key)
            print(value)
            eball_mod_num100 = value
            causality_ki_value = (key * 100) / eball_mod_num100
            set_value(tag_id, math.ceil(causality_ki_value))
        

def Causality_Preset(Row_Number, *, hide=False, values_to_hide=[], combo=False, combo_cau_vals=[], combo_list=[], callback=None, callback_columns=[], hint_cau_vals=[], hint_text={}):
    """Sets the table row to show the relavant information for the causality type, 
    based on the parameters given.

    Args:
        Row_Number (int|str): _description_
        hide (bool, optional): Enable if you need to hide a cau_val row. Defaults to False.
        values_to_hide (list, optional): List of the cau_vals to hide. Defaults to [].
        combo (bool, optional): Enable if you need to change a row to a combo list. Defaults to False.
        combo_cau_vals (list, optional): List of the row numbers to change to a combo list. Defaults to [].
        combo_list (list, optional): List of items for the combo list. Defaults to [].
        callback (function): Add the function you'd like to use as a callback on cau_vals.
        callback_columns (list): List of cau_vals to add a callback to.
        hint_cau_vals (list): List of cau_vals to add hints to.
        hint_text (dict): Dictionary of cau_vals with the hint text.
        
    """
    

    
    if combo:
        Row_Parent = get_item_parent(f'Causality_ID{Row_Number}')
        delete_me = [f'Causality_Cau_Val1{Row_Number}', f'Causality_Cau_Val2{Row_Number}', f'Causality_Cau_Val3{Row_Number}']
        Delete_Items(delete_me)
        for i in range(3):
            if i + 1 in combo_cau_vals:
                if callback:
                    add_combo(tag=f'Causality_Cau_Val{i + 1}{Row_Number}', items=combo_list[i], default_value=combo_list[i][0], width=String_Length.length[0], parent=Row_Parent, callback=callback)
                else:
                    add_combo(tag=f'Causality_Cau_Val{i + 1}{Row_Number}', items=combo_list[i], default_value=combo_list[i][0], width=String_Length.length[0], parent=Row_Parent)
            else:
                ### Need to fix this part as it doesn't work like the other section
                if callback:
                    if i + 1 in callback_columns:
                        add_input_text(tag=f'Causality_Cau_Val{i + 1}{Row_Number}', default_value='0', width=String_Length.length[0], parent=Row_Parent, callback=callback)
                    else:
                        add_input_text(tag=f'Causality_Cau_Val{i + 1}{Row_Number}', default_value='0', width=String_Length.length[0], parent=Row_Parent)
                else:
                    add_input_text(tag=f'Causality_Cau_Val{i + 1}{Row_Number}', default_value='0', width=String_Length.length[0], parent=Row_Parent)
                
    else:
        Row_Parent = get_item_parent(f'Causality_Cau_Val1{Row_Number}')
        delete_me = [f'Causality_Cau_Val1{Row_Number}', f'Causality_Cau_Val2{Row_Number}', f'Causality_Cau_Val3{Row_Number}']
        Delete_Items(delete_me)
        for i in range(3):
            if callback:
                ### Allows selection of cau_val rows to add a call back to.
                if i + 1 in callback_columns:
                    add_input_text(tag=f'Causality_Cau_Val{i + 1}{Row_Number}', default_value='0', width=String_Length.length[0], parent=Row_Parent, callback=callback)
                else:
                    add_input_text(tag=f'Causality_Cau_Val{i + 1}{Row_Number}', default_value='0', width=String_Length.length[0], parent=Row_Parent)
            else:
                add_input_text(tag=f'Causality_Cau_Val{i + 1}{Row_Number}', default_value='0', width=String_Length.length[0], parent=Row_Parent)
                
    if hint_cau_vals:
        for hint in hint_cau_vals:
            with tooltip(f'Causality_Cau_Val{hint}{Row_Number}'):
                add_text(hint_text[hint], tag=f'Causality_Cau_Val{hint}{Row_Number}_hint')
    if hide:
        for value_to_hide in values_to_hide:
            configure_item(f'Causality_Cau_Val{value_to_hide}{Row_Number}', show=False)


def Hint_Change(tag_id, data):
    Row_Number = Table_ID(tag_id)
    hint_text = '(Cards in Set)\n'
    for name in Causality.card_unique_info_set_names[data]:
        hint_text += name + '\n'
        
    ### Remove new line for the last string
    hint_text = hint_text[:-1]
    
    set_value(tag_id + '_hint', hint_text)

Database = Database()
### For the Causality_Type to change the Cau_Val rows based on the row ID
def Causality_Type_Callback(tag_id, data):
    text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIAL.ttf')
    set_item_width(tag_id, text_width + 27)
    ### Table_ID() will grab all numbers from the end of a tag_id, thus resulting in the row number based on how I did the tags.
    Row_Number = Table_ID(tag_id)
    Number_of_Rows = Row_Checker(Causality.row_names[0])
    
    # Checking all of the widgets widths in a row combined
    widget_widths_list = []
    for row in range(Number_of_Rows):
        widget_widths = 0
        for column in range(len(Causality.row_names)):
            widget_widths += get_item_width(Causality.row_names[column] + str(row))
        widget_widths_list.append(widget_widths)
        
    # Finding the max width out of all widgets
    max_width = 0
    for width in widget_widths_list:
        max_width = width
        if width > max_width:
            max_width = width
            
    # print(widget_widths_list)
    # print(max_width)
    set_item_width(Causality.column_names[4], max_width)
    # print(get_item_children('Causality_Table'))
    Table_Children = get_item_children('Causality_Table')
    # print(get_item_alias(Table_Children[0][1]))
    # print(get_item_width(Table_Children[0][2]))
    
    # Causality_Preset(Row_Number, combo=True, combo_cau_vals=[1], combo_list=['test'], hide=True, values_to_hide=[2,3])
    
    if '(1)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
        
    if '(2)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
    
    if '(3)' in data:
        hint_3 = f'If you have a unit queried and type the exact Ki Number, this will automatically calculate it\n(If you don\'t have a unit queried, you can do "Ki Number : eball_num_100" instead)\nEx. "24 : 3" which equates to 800'
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3], callback=Ki_Calculation, callback_columns=[1], hint_cau_vals=[1], hint_text={1 : hint_3})
        
    if '(4)' in data:
        hint_4 = f'If you have a unit queried and type the exact Ki Number this will automatically calculate it\n(If you don\'t have a unit queried, you can do "Ki Number : eball_num_100" instead)\nEx. "24 : 3" which equates to 800'
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3], callback=Ki_Calculation, callback_columns=[1], hint_cau_vals=[1], hint_text={1 : hint_4})
    
    if '(5)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
        
    ### Not really used in game
    if '(6)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
    
    ### Not really used in game
    if '(7)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
    
    ### Not really used in game
    if '(8)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3])
    
    ### Not really used in game
    if '(9)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3])

    ### Not really used in game
    if '(10)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3])

    ### Not really used in game
    if '(11)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3])

    ### Not really used in game
    if '(12)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3])

    ### Not really used in game
    if '(13)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3])
    
    ### Two instances (id : 16, 39) in database. One has '0' and the other has '1' in the cau_val1. Not sure if it's a boolean check because that would be odd.
    if '(14)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
        
    if '(15)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
        
    if '(16)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
        
    if '(17)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
        
    if '(18)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
    
    if '(19)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3], combo=True, combo_cau_vals=[1], combo_list=[['Slot 1', 'Slot 2', 'Slot 3']])
        
    ### Not really used in game
    if '(20)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
        
    ### Not really used in game    
    if '(21)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
    
    ### Not really used in game (Would need testing to whether it's a card_unique_infos or the set, think it's just the infos)
    if '(22)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
    
    ### Not really used in game 
    if '(23)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
    
    ### Hide all since they are all 0
    if '(24)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
    
    ### Hide all since they are all 0    
    if '(25)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
    
    ### Not really used in game
    if '(26)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
    
    ### Not really used in game
    if '(27)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])

    ### Not really used in game
    if '(28)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
    
    ### Not really used in game
    if '(29)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
    
    ### Hide all since they are all 0
    if '(30)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
    
    ### Hide all since they are all 0   
    if '(31)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
    
    ### Not really used in game
    if '(32)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
        
    if '(33)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3])
        
    if '(34)' in data:
        combo_1 = ['Team', 'Enemy', 'Rotation']
        combo_2 = Leader_Skill_Info.cat_list
        combo_3 = ['1', '2', '3', '4', '5', '6', '7']
        Causality_Preset(Row_Number, combo=True, combo_cau_vals=[1,2,3], combo_list=[combo_1, combo_2, combo_3], hint_cau_vals=[3], hint_text={3 : 'The amount of said category'})
        
    if '(35)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3], combo=True, combo_cau_vals=[1], combo_list=[['Super Class', 'Extreme Class']])
    
    ### Not really used in game    
    if '(36)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3])
    
    if '(37)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3])
        
    if '(38)' in data:
        hint_37 = f'''(16 = ATK Down)\n(32 = DEF Down)\n(256 = Eff 9(Stunned))\n(512 = Eff 47(Guard disabled))\n(1024 = Eff 48 (Sealed))\n(2048 = Eff 8(Delay/"ghost usher"))\n(8192 = Eff 53(Def 0/"Ignore Defense"))\n(16384 = Eff 75(Swap Disabled))\n(32768 = Eff 94(Invalidate Stun))\n(65536 = Eff 96(Ki Value Changed/Ki +2 per sphere obtained))\n(524288 = Eff 100(Invalidate Astute))\n(1048576 = Eff 101(Forsee Supers))\nIf using "Multiple Skills; add the status numbers together'''
                   
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3], combo=True, combo_cau_vals=[2], combo_list=[[],['Single Status', 'Multiple Statuses']], hint_cau_vals=[1], hint_text={1 : hint_37})
        
    if '(39)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3], combo=True, combo_cau_vals=[1], combo_list=[['Super Class', 'Extreme Class']])
        
    if '(40)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
    
    if '(41)' in data:
        combo_1 = ['Team', 'Enemy', 'Rotation']
        combo_2 = []
        combo_3 = [1,2,3,4,5,6,7]
        hint_text = f'(Cards in Set)\nPiccolo\nPiccolo\nPiccolo (Fused with Kami)\nUltimate Gohan & Piccolo\nGoku & Piccolo\nPiccolo & Krillin\nGoku & Piccolo/Piccolo\nPiccolo (Exchange)\nPiccolo (Power Awakening)\nSuper Saiyan 3 Gotenks & Piccolo\nPiccolo (Power Awakening)\nOrange Piccolo'
        for key, value in Causality.card_unique_info_set_names.items():
            combo_2.append(key)
        Causality_Preset(Row_Number, combo=True, combo_cau_vals=[1,2,3], combo_list=[combo_1, combo_2, combo_3], hint_text={2 : hint_text}, hint_cau_vals=[2], callback_columns=[2], callback=Hint_Change)
    
    ### Come back to attempt making easier to do; separate calculation method like Ki Number
    if '(42)' in data:
        combo_1 = []
        combo_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        hint_text = f'Element IDs\n(Add IDs together to combine Ki types)\n(1 - AGL)\n(2 - TEQ)\n(4 - INT)\n(8 - STR)\n(16 - PHY)\n(31 - All but Rainbow Spheres)\n(32 - Rainbow)\n(63 - All Ki Spheres)'

        Causality_Preset(Row_Number, hide=True, values_to_hide=[3], combo=True, combo_cau_vals=[2], combo_list=[combo_1, combo_2], hint_text={1 : hint_text}, hint_cau_vals=[1])
        
    if '(43)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
        
    if '(44)' in data:
        combo_1 = ['Supers Performed', 'Atks Performed', 'Atks Received', 'Guard Activated', 'Dodges']
        combo_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        Causality_Preset(Row_Number, hide=True, values_to_hide=[3], combo=True, combo_cau_vals=[1,2], combo_list=[combo_1, combo_2])
        
    if '(45)' in data:
        combo_1 = ['Team', 'Enemy', 'Rotation']
        combo_2 = Leader_Skill_Info.cat_list
        combo_3 = []
        hint_text = f'(Cards in Set)\nPiccolo\nPiccolo\nPiccolo (Fused with Kami)\nUltimate Gohan & Piccolo\nGoku & Piccolo\nPiccolo & Krillin\nGoku & Piccolo/Piccolo\nPiccolo (Exchange)\nPiccolo (Power Awakening)\nSuper Saiyan 3 Gotenks & Piccolo\nPiccolo (Power Awakening)\nOrange Piccolo'
        for key, value in Causality.card_unique_info_set_names.items():
            combo_3.append(key)
        Causality_Preset(Row_Number, combo=True, combo_cau_vals=[1,2,3], combo_list=[combo_1, combo_2, combo_3], hint_text={3 : hint_text}, hint_cau_vals=[3], callback=Hint_Change, callback_columns=[3])
        
    if '(46)' in data:
        combo_1 = ['Team', 'Enemy', 'Rotation']
        combo_2 = ['Super Class', 'Extreme Class']
        combo_3 = [1,2,3,4,5,6,7]
        Causality_Preset(Row_Number, combo=True, combo_cau_vals=[1,2,3], combo_list=[combo_1, combo_2, combo_3])
        
    if '(47)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
        
    if '(48)' in data:
        combo_1 = ['Ki Blast', 'Unarmed', 'Physical', 'Unit Super']
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3], combo=True, combo_cau_vals=[1], combo_list=[combo_1])
        
    if '(49)' in data:
        combo_1 = ['Ki Blast', 'Unarmed', 'Physical', 'Unit Super']
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3], combo=True, combo_cau_vals=[1], combo_list=[combo_1])
        
    if '(50)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
        
    if '(51)' in data:
        combo_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3], combo=True, combo_cau_vals=[1], combo_list=[combo_1])
        
    if '(52)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
        
    if '(53)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
        
    if '(54)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
        
    if '(55)' in data:
        combo_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3], combo=True, combo_cau_vals=[1], combo_list=[combo_1])
        
    if '(56)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
        
    if '(57)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
        
    if '(58)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
        
    if '(59)' in data:
        combo_1 = ['Super Class', 'Extreme Class']
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3], combo=True, combo_cau_vals=[1], combo_list=[combo_1])
        
    if '(60)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[2,3])
        
    if '(61)' in data:
        Causality_Preset(Row_Number, hide=True, values_to_hide=[1,2,3])
        
#################################################################################################################################################################################################################################################################

def Causality_Creator():
    
    causality_combo_list = ['(0) None', '(1) Is HP Over %','(2) Is HP Under %','(3) Ki Over #','(4) Ki Under #','(5) Past Turn #','(6) Deck Has Link Skill',
                           '(7) Enemy Has Link Skill','(8) Is ATK & DEF Over %','(9) Is ATK & DEF Under %',f'(10) Is HP Over % and Ki Above #',
                           f'(11) Is HP Over % and Ki Below #',f'(12) Is HP Below % and Ki Above #',f'(13) Is HP Below % and Ki Below #',
                           '(14) Is First Slot','(15) Over # Enemies','(16) Under # Enemies','(17) Target Over HP %','(18) Target Under HP %',
                           '(19) Card Slot','(20) When Ki is above %','(21) When Ki is below %','(22) Character on team','(23) If # of links are active',
                           '(24) Hit Received','(25) Target Killed',f'(26) When HP is over % and has enough ki to super',f'(27) When HP is below % and has enough ki to super',
                           '(28) Checks if ID# element is on rotation','(29) Character is Enemy','(30) Check if Guarding','(31) When there are 3 or more enemy attacks',
                           '(32) When there is ID# type Ki on the field',f'(33) When HP is between % and %','(34) Category Card Present',
                           '(35) When the team consists of only X Class',f'(36) When HP is over % and battle has past turn #',f'(37) When HP is below % and battle has past turn #',
                           '(38) Enemy Status Effect','(39) When there is a X Class enemy','(40) Special Attack','(41) Character Name on team','(42) Ki Orbs Obtained',
                           '(43) Dodge Success','(44) Count Up','(45) Card is Name + Cat','(46) Type of Unit','(47) Revival Activated','(48) Super Attack Type',
                           '(49) When a (Super Type) is directed at the character', '(50) When Passive Skill Effect has been activated', '(51) Skill lasts for # turns from start of battle', 
                           '(52) Charge Count', '(53) When in Standby Mode', '(54) Starting from the turn in which the character\'s or an ally\'s Revival Skill is activated',
                           '(55) Starting from the # turn', '(56) When normal attacks are directed at the character','(57) When a unit is in a specific Dokkan Field', '(58) Used with Dokkan Fields',
                           '(59) When a unit is in a specific class', '(60) When a unit is in a specific sub target type', '(61) When a unit receives in attack during the turn']
    
    ### Queries the database to gather all of the card_unique_info stuff to be used in the rest of the Causality Creator
    Causality.card_unique_info_set_names = Card_Unique_Infos()

    Delete_Items('Causality_Creator_Window');Delete_Items('Causality_Button_Group');Delete_Items('Causality_Add')
    Delete_Items('Causality_Del');Delete_Items('Causality_JSON_Input');Delete_Items('Causality_JSON_Button')
    
    with window(label='Causality Creator',tag='Causality_Creator_Window', width=900, height=400):
        with group(horizontal=True, tag='Causality_Button_Group'):
            add_button(label='Add Causality', tag='Causality_Add', callback=Causality_Add)
            add_button(label='Del Causality', tag='Causality_Del', callback=Causality_Del)
            add_text('(?)', tag='Causality_?_Text')
            add_input_text(tag='Causality_JSON_Input', width=String_Length.length[0], hint='Ex. 4&21')
            add_button(label='Create Causality', tag='Causality_JSON_Button', callback=Create_Causality_JSON)
            with tooltip('Causality_?_Text'):
                add_text('The table will only display "cau_val" that are required\nIf none appear it''s because that causality is all 0s' )
            with tooltip('Causality_JSON_Input'):
                add_text('\t\t\t\t\t\t(WIP)\n---------------------------------------------------------\nExamples of what currently works\n4&1&69\n5|21|16\n1937&1938|1939&1940\n(1937&1938)|(1939&1940)|(5555&5523)\n(385&(386|387))|(388&9)\n')



        
        
        list_of_inputs = []
        if does_alias_exist('Causality_Table'):
            delete_item('Causality_Table')

        for last_rows in range(Causality.last_rows):

            for u in range(len(Causality.row_names)):
                if does_alias_exist(Causality.row_names[u] + '0' + str(last_rows)):
                    delete_item(Causality.row_names[u] + '0' + str(last_rows))

        Delete_Items('Causality_Table')
        with table(tag='Causality_Table', width=663, height=46, resizable=True, header_row=True, parent='Causality_Creator_Window'):
            # Widget_Aliases.tags_to_delete.append('Causality_Table')
            list_of_inputs.append('Causality_Table')
            
            for i in range(len(Causality.row_names)):
                if Causality.column_names[i] == 'Causality Type':
                    Delete_Items(Causality.column_names[i])
                    add_table_column(label=Causality.column_names[i], init_width_or_weight=300, tag=Causality.column_names[i])
                    list_of_inputs.append(Causality.column_names[i])
                    # Widget_Aliases.tags_to_delete.append(Causality.column_names[i])
                else:
                    add_table_column(label=Causality.column_names[i], init_width_or_weight=75, tag=Causality.column_names[i])
                    
            for o in range(Causality.rows):
                Delete_Items('Causality_Row' + str(o))
                with table_row(tag='Causality_Row' + str(o)):
                    # Widget_Aliases.tags_to_delete.append('Causality_Row' + str(o))
                    list_of_inputs.append('Causality_Row' + str(o))
                
            for z in range(Causality.rows):
                for t in range(len(Causality.row_names)):
                    # The last number is always 0
                    if Causality.row_names[t] == 'Causality_Causality_Type':
                        Delete_Items(Causality.row_names[t] + str(z))
                        add_combo(tag=Causality.row_names[t] + str(z), items=causality_combo_list, default_value=causality_combo_list[0], width=149, parent='Causality_Row' + str(z), callback=Causality_Type_Callback)
                        # Widget_Aliases.tags_to_delete.append(Causality.row_names[t] + str(z))
                        list_of_inputs.append(Causality.row_names[t] + str(z))

                    elif Causality.row_names[t] == 'Causality_Cau_Val1':
                        Delete_Items(Causality.row_names[t] + str(z))
                        add_input_text(tag=Causality.row_names[t] + str(z), hint=Causality.column_names[t], default_value='69', width=String_Length.length[0], parent='Causality_Row' + str(z), show=False)
                        # Widget_Aliases.tags_to_delete.append(Causality.row_names[t] + str(z))
                        list_of_inputs.append(Causality.row_names[t] + str(z))
                        
                    elif Causality.row_names[t] == 'Causality_ID':
                        Delete_Items(Causality.row_names[t] + str(z))
                        add_input_text(tag=Causality.row_names[t] + str(z), hint=Causality.column_names[t], default_value='0', width=String_Length.length[0], parent='Causality_Row' + str(z))
                        # Widget_Aliases.tags_to_delete.append(Causality.row_names[t] + str(z))
                        list_of_inputs.append(Causality.row_names[t] + str(z))
                    else:
                        Delete_Items(Causality.row_names[t] + str(z))
                        add_input_text(tag=Causality.row_names[t] + str(z), hint=Causality.column_names[t], default_value='0', width=String_Length.length[0], parent='Causality_Row' + str(z), show=False)
                        # Widget_Aliases.tags_to_delete.append(Causality.row_names[t] + str(z))
                        list_of_inputs.append(Causality.row_names[t] + str(z))
                        
def Causality_Add():
    Row_Number = Row_Checker('Causality_Row')
    add_table_row(tag=f'Causality_Row{Row_Number}', parent=f'Causality_Table')
    if does_alias_exist(Causality.row_names[0] + str(Row_Number - 1)):
        add_input_text(tag=Causality.row_names[0] + str(Row_Number), hint=Causality.column_names[0], default_value=str(int(get_value(Causality.row_names[0] + str(Row_Number - 1))) + 1), width=String_Length.length[0], parent='Causality_Row' + str(Row_Number))
    else:
        add_input_text(tag=Causality.row_names[0] + str(Row_Number), hint=Causality.column_names[0], default_value='0', width=String_Length.length[0], parent='Causality_Row' + str(Row_Number))
    add_combo(tag=Causality.row_names[1] + str(Row_Number), items=Causality.causality_combo_list, default_value=Causality.causality_combo_list[0], width=149, parent='Causality_Row' + str(Row_Number), callback=Causality_Type_Callback)
    add_input_text(tag=Causality.row_names[2] + str(Row_Number), hint=Causality.column_names[2], default_value='69', width=String_Length.length[0], parent='Causality_Row' + str(Row_Number))
    add_input_text(tag=Causality.row_names[3] + str(Row_Number), hint=Causality.column_names[3], default_value='0', width=String_Length.length[0], parent='Causality_Row' + str(Row_Number), show=False)
    add_input_text(tag=Causality.row_names[4] + str(Row_Number), hint=Causality.column_names[4], default_value='0', width=String_Length.length[0], parent='Causality_Row' + str(Row_Number), show=False)
    # Widget_Aliases.tags_to_delete.append(Causality.row_names[0] + str(Row_Number))
    # Widget_Aliases.tags_to_delete.append(Causality.row_names[1] + str(Row_Number))
    # Widget_Aliases.tags_to_delete.append(Causality.row_names[2] + str(Row_Number))
    # Widget_Aliases.tags_to_delete.append(Causality.row_names[3] + str(Row_Number))
    # Widget_Aliases.tags_to_delete.append(Causality.row_names[4] + str(Row_Number))
    
    set_item_height('Causality_Table', 24 * (Row_Number + 1) + 23)
        
        
def Causality_Del():
    Row_Number = Row_Checker('Causality_Row')
    ### Only delte row when there are widgets available to delete. Prevents the table from going -1 and having lines render all the way to the bottom.
    if Row_Number != 0:
        delete_item(f'Causality_Row{Row_Number - 1}')
        delete_item(Causality.row_names[0] + str(Row_Number - 1))
        delete_item(Causality.row_names[1] + str(Row_Number - 1))
        delete_item(Causality.row_names[2] + str(Row_Number - 1))
        delete_item(Causality.row_names[3] + str(Row_Number - 1))
        delete_item(Causality.row_names[4] + str(Row_Number - 1))

        set_item_height('Causality_Table', 24 * (Row_Number - 1) + 23)
    else:
        pass