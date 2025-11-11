import sqlite3
from dearpygui.dearpygui import *
from . configs import Config_Read
from .classes import String_Length, Widget_Aliases, Database, Card_Table_Combos, Card, Custom_Unit
from . functions import Text_Resize, Table_Inputs, Delete_Items, Table_Combo_Inputs, Table_ID, Row_Checker
from . download import Card_Checks
# from modules import RPC
import time
# str_length = String_Length.str_length


str_length = String_Length.length


 
    
# Card Table Additions

    
#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################    
Database = Database()

def Synced_Callback(tag_id, user_data):
    tag_id = tag_id[:-1]
    set_value(tag_id + '0', user_data)
    set_value(tag_id + '1', user_data)
    
def Name_Change_Callback(tag_id):
    card = Table_ID(tag_id[:-6])
    card_name = get_value(tag_id)
    set_value(f'{Card.row_names[1]}_Card_{str(card)}_Row_0', card_name)
    set_value(f'{Card.row_names[1]}_Card_{str(card)}_Row_1', card_name)
    set_value(f'Card_Name_Display_{card}', card_name)
    configure_item(f'Main_Card_Tab_{card}', label=card_name)

    
def Rarity_Callback(tag_id, user_data):
    import random
    tag_id = str(tag_id[:-6])
    Card_Number = Table_ID(tag_id)
    set_value(Card.row_names[5] + '_Card_' + str(Card_Number) + '_Row_0', user_data)
    set_value(Card.row_names[5] + '_Card_' + str(Card_Number) + '_Row_1', user_data)
    rarity = ['(N)', '(R)', '(SR)', '(SSR)', '(TUR)', '(LR)']
    lvl_max = ['20', '40', '60', '100', '120', '150']
    skill_max = ['10', '10', '10', '10', '10', '20']
    HP_init = [random.randrange(400, 700), random.randrange(800, 2000), random.randrange(1500, 5500), random.randrange(2000, 8000), random.randrange(3000, 17500), random.randrange(3000, 7500)]
    HP_Max = [random.randrange(1200, 2000), random.randrange(1800, 5500), random.randrange(3000, 8000), random.randrange(4000, 13200), random.randrange(4500, 20000), random.randrange(6500, 24500)]
    
    ATK_init = [random.randrange(150, 500), random.randrange(600, 1500), random.randrange(1000, 3500), random.randrange(1500, 5600), random.randrange(2000, 13000), random.randrange(2500, 7000)]
    ATK_Max = [random.randrange(500, 1400), random.randrange(1850, 3600), random.randrange(3000, 5600), random.randrange(4700, 10000), random.randrange(4500, 15000), random.randrange(8000, 18000)]
    
    DEF_init = [random.randrange(150, 350), random.randrange(400, 1200), random.randrange(700, 3500), random.randrange(1000, 4400), random.randrange(1500, 7000), random.randrange(2000, 4200)]
    DEF_Max = [random.randrange(500, 1200), random.randrange(1300, 3500), random.randrange(2000, 5000), random.randrange(2500, 6000), random.randrange(3000, 12000), random.randrange(4500, 13500)]
    
    for i in range(len(rarity)):
        if user_data == rarity[i]:
            ### HP Init
            set_value(Card.row_names[6] + '_Card_' + str(Card_Number) + '_Row_0', str(HP_init[i]))
            set_value(Card.row_names[6] + '_Card_' + str(Card_Number) + '_Row_1', str(HP_init[i]))
            ### HP Max
            set_value(Card.row_names[7] + '_Card_' + str(Card_Number) + '_Row_0', str(HP_Max[i]))
            set_value(Card.row_names[7] + '_Card_' + str(Card_Number) + '_Row_1', str(HP_Max[i]))
            ### ATK Init
            set_value(Card.row_names[8] + '_Card_' + str(Card_Number) + '_Row_0', str(ATK_init[i]))
            set_value(Card.row_names[8] + '_Card_' + str(Card_Number) + '_Row_1', str(ATK_init[i]))
            ### ATK Max
            set_value(Card.row_names[9] + '_Card_' + str(Card_Number) + '_Row_0', str(ATK_Max[i]))
            set_value(Card.row_names[9] + '_Card_' + str(Card_Number) + '_Row_1', str(ATK_Max[i]))
            ### DEF Init
            set_value(Card.row_names[10] + '_Card_' + str(Card_Number) + '_Row_0', str(DEF_init[i]))
            set_value(Card.row_names[10] + '_Card_' + str(Card_Number) + '_Row_1', str(DEF_init[i]))
            ### DEF Max
            set_value(Card.row_names[11] + '_Card_' + str(Card_Number) + '_Row_0', str(DEF_Max[i]))
            set_value(Card.row_names[11] + '_Card_' + str(Card_Number) + '_Row_1', str(DEF_Max[i]))
            ### Max Level
            set_value(Card.row_names[13] + '_Card_' + str(Card_Number) + '_Row_0', lvl_max[i])
            set_value(Card.row_names[13] + '_Card_' + str(Card_Number) + '_Row_1', lvl_max[i])
            ### Max Skill Level
            set_value(Card.row_names[14] + '_Card_' + str(Card_Number) + '_Row_0', skill_max[i])
            set_value(Card.row_names[14] + '_Card_' + str(Card_Number) + '_Row_1', skill_max[i])
            
def Element_Callback(tag_id, user_data):
    card = Table_ID(tag_id[:-6])
    element_combo_tags =[f'element_Card_{card}_Row_0', f'element_Card_{card}_Row_1']
    for tag in element_combo_tags:
        set_value(tag, user_data)
    
    if 'Super' in user_data:
        user_data = user_data.replace('Super ', '')
    elif 'Extreme' in user_data:
        user_data = user_data.replace('Extreme ', '')
    
    with texture_registry():
        Delete_Items(f'Custom_Border_Thumb_Border_Texture_{user_data}')
        Delete_Items(f'Custom_Border_Thumb_Background_Texture_{user_data}')
        width, height, channels, border_data = load_image(f'logo/Custom_Border_Border_{user_data}.png')
        add_dynamic_texture(width=250, height=250, default_value=border_data, tag=f'Custom_Border_Thumb_Border_Texture_{user_data}')
        width, height, channels, bg_data = load_image(f'logo/Custom_Border_Background_{user_data}.png')
        add_dynamic_texture(width=250, height=250, default_value=bg_data, tag=f'Custom_Border_Thumb_Background_Texture_{user_data}')
    set_value(f'Custom_Border_Thumb_Border_Texture_{card}', border_data)
    set_value(f'Custom_Border_Thumb_Background_Texture_{card}', bg_data)
    configure_item(f'Custom_Border_Thumb_Background_{card}', pos=[8,110], show=True)
    configure_item(f'Custom_Border_Thumb_Border_{card}', pos=[8,110], show=True)
    configure_item(f'card_thumb_display_{card}', pos=[8,110], show=True)
    
        
    
def EZA_Callback(tag_id, user_data, data, sender, app_data):
    num_of_cards = Row_Checker(tag_id[:-1])
    Card_Number = Table_ID(tag_id)

    num_of_specials = Row_Checker(f'Special#_Text_Card_{Card_Number}_')
    configure_item(f'EZA_Checkbox_{Card_Number}', default_value=user_data)
    if user_data:
        configure_item(f'Super_EZA_Checkbox_{Card_Number}', default_value=False)
        print(Card.row_names[16] + '_Card_' + str(Card_Number) + '_Row_0')
        optimal_awakening_growth_id = get_value(Card.row_names[0] + '_Card_' + str(Card_Number) + '_Row_0')
        ### Row 1 because that's the won that uses the optimal awakening growth

        set_value(Card.row_names[16] + '_Card_' + str(Card_Number) + '_Row_0', optimal_awakening_growth_id)
        set_value(Card.row_names[16] + '_Card_' + str(Card_Number) + '_Row_1', optimal_awakening_growth_id)
        
        ### Check number of supers and change the lvl start based on rarity
        
        for special in range(num_of_specials):
            rarity = get_value(Card.row_names[5] + '_Card_' + str(Card_Number) + '_Row_1')
            if rarity == '(LR)':
                lvl_start = '24'
            else:
                lvl_start = '14'
            
            ### Add (Extreme) to super name if it has a value
            if get_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}') and '(Extreme)' not in get_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}'):
                set_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}', get_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}') + ' (Extreme)')
                Text_Resize(f'Special_Set_Name_Input_Card_{Card_Number}_{special}')
                
            ### Because of rage unitsm this needs to be row checked
            for i in range(Row_Checker(f'CS_lv_start_Card_{Card_Number}_Row_{special}')):
                set_value(f'CS_lv_start_Card_{Card_Number}_Row_{special}{i}', lvl_start)
            
        
    else: ### checkbox is False
        set_value(Card_Number.row_names[16] + '_Card_' + str(Card_Number) + '_Row_1', 'NULL')
        for special in range(num_of_specials):
            for i in range(Row_Checker(f'CS_lv_start_Card_{Card_Number}_Row_{special}')):
                set_value(f'CS_lv_start_Card_{Card_Number}_Row_{special}{i}', '0')
        ### Remove (Extreme) from super name
            if get_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}'):
                set_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}', get_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}').replace(' (Extreme)', ''))
                Text_Resize(f'Special_Set_Name_Input_Card_{Card_Number}_{special}')


def Super_EZA_Callback(tag_id, user_data, data, sender, app_data):
    num_of_cards = Row_Checker(tag_id[:-1])
    Card_Number = Table_ID(tag_id)

    num_of_specials = Row_Checker(f'Special#_Text_Card_{Card_Number}_')
    configure_item(f'Super_EZA_Checkbox_{Card_Number}', default_value=user_data)
    if user_data:
        set_value(f'EZA_Checkbox_{Card_Number}', False)
        print(Card.row_names[16] + '_Card_' + str(Card_Number) + '_Row_0')
        optimal_awakening_growth_id = get_value(Card.row_names[0] + '_Card_' + str(Card_Number) + '_Row_0')
        ### Row 1 because that's the won that uses the optimal awakening growth

        set_value(Card.row_names[16] + '_Card_' + str(Card_Number) + '_Row_0', optimal_awakening_growth_id)
        set_value(Card.row_names[16] + '_Card_' + str(Card_Number) + '_Row_1', optimal_awakening_growth_id)

        for special in range(num_of_specials):
            rarity = get_value(Card.row_names[5] + '_Card_' + str(Card_Number) + '_Row_1')
            if rarity == '(LR)':
                lvl_start = '24'
            else:
                lvl_start = '14'

            if get_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}') and '(Extreme)' not in get_value(
                    f'Special_Set_Name_Input_Card_{Card_Number}_{special}'):
                set_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}',
                          get_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}') + ' (Extreme)')
                Text_Resize(f'Special_Set_Name_Input_Card_{Card_Number}_{special}')

            ### Because of rage unitsm this needs to be row checked
            for i in range(Row_Checker(f'CS_lv_start_Card_{Card_Number}_Row_{special}')):
                set_value(f'CS_lv_start_Card_{Card_Number}_Row_{special}{i}', lvl_start)

    else: ### checkbox is False
        set_value(Card_Number.row_names[16] + '_Card_' + str(Card_Number) + '_Row_1', 'NULL')
        for special in range(num_of_specials):
            for i in range(Row_Checker(f'CS_lv_start_Card_{Card_Number}_Row_{special}')):
                set_value(f'CS_lv_start_Card_{Card_Number}_Row_{special}{i}', '0')
        ### Remove (Extreme) from super name
            if get_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}'):
                set_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}', get_value(f'Special_Set_Name_Input_Card_{Card_Number}_{special}').replace(' (Extreme)', ''))
                Text_Resize(f'Special_Set_Name_Input_Card_{Card_Number}_{special}')
            

    
# TODO: Right another script that dumps links. Leave for now I guess.
def Link_Skills_Query():
    links = Database.query(query=f'SELECT id,name,description FROM link_skills', value=None)
    link_skill_dict = {links[i][0]: links[i][1] + ' (' + links[i][2] + ')' for i in range(len(links))}
    Card_Table_Combos.link_skill_dict = link_skill_dict
    link_skill_combo = [str(key) + ': ' + str(value) for key, value in link_skill_dict.items()]
    
    # print(link_skill_dict)
    return link_skill_combo


def Card_Widgets():
    rarity_combo = ['(N)', '(R)', '(SR)', '(SSR)', '(TUR)', '(LR)']
    element_combo = ['AGL', 'TEQ', 'INT', 'STR', 'PHY', 'Super AGL', 'Super TEQ', 'Super INT', 'Super STR', 'Super PHY', 'Extreme AGL', 'Extreme TEQ', 'Extreme INT', 'Extreme STR', 'Extreme PHY']
    element_dict = {'0': 'AGL', '1': 'TEQ', '2': 'INT', '3': 'STR', '4': 'PHY', '10': 'Super AGL', '11': 'Super TEQ', '12': 'Super INT', '13': 'Super STR', '14': 'Super PHY', '20': 'Extreme AGL', '21': 'Extreme TEQ', '22': 'Extreme INT', '23': 'Extreme STR', '24' : 'Extreme PHY'}
    link_skill_combo = Link_Skills_Query()
    potential_board_combo = ['+3k to stats', '+5k to stats', '+7k to stats']
    combos = {5 : rarity_combo, 12 : element_combo, 23 : link_skill_combo, 24 : link_skill_combo, 25 : link_skill_combo, 26 : link_skill_combo, 27 : link_skill_combo, 28 : link_skill_combo, 29 : link_skill_combo, 52 : potential_board_combo}
    Card_Table_Combos.rarity_combo = rarity_combo
    Card_Table_Combos.element_combo = element_combo
    Card_Table_Combos.element_dict = element_dict
    Card_Table_Combos.link_skill_combo = link_skill_combo
    Card_Table_Combos.potential_board_combo = potential_board_combo
    
    if not get_value('Custom_Unit'):
        card_num = Custom_Unit.card_number
        
        with group(horizontal=True, tag=f'Card_Information_Text_Group_{card_num}', parent=f'Card_Input_Tab_{card_num}'):
            add_text('Card Information', color=(255,50,50), parent=f'Card_Information_Text_Group', tag=f'Card_Information_Text_{card_num}')
            add_checkbox(label='EZA', default_value=False, tag=f'EZA_Checkbox_{card_num}', callback=EZA_Callback, parent='Card_Information_Text_Group')
        Widget_Aliases.tags_to_delete.append(f'Card_Information_Text_{card_num}')
        Widget_Aliases.tags_to_delete.append(f'EZA_Checkbox_{card_num}')
        Widget_Aliases.tags_to_delete.append(f'Card_Information_Text_Group_{card_num}')

        # sss = Table_Inputs(table_name=f'Card{card_num}_Table', row_name=f'Card{card_num}_Table_Row', class_name=Card,
                    #  use_child_window=False, table_parent=f'Card_Input_Tab_{card_num}', table_height=83, table_width=1650,
                    #  row_width=85, transformation=True, transformation_card_num=card_num)
        
            ## 5 Rarity, 12 Element, 23,24,25,26,27,28,29 Link Skills, 52 Potential Board
        sss = Table_Combo_Inputs(table_name=f'Card{card_num}_Table', row_name=f'Card{card_num}_Table_Row', class_name=Card,
                        table_parent=f'Card_Input_Tab_{card_num}', table_height=83, table_width=1650,
                        row_width=85, transformation_card_num=card_num, combo_columns=[5,12,23,24,25,26,27,28,29,52], 
                        callback_columns=[5, 12, 23, 24, 25, 26, 27, 28, 29, 52], callback={5 : Rarity_Callback, 12 : Element_Callback, 23 : Synced_Callback, 24 : Synced_Callback, 25 : Synced_Callback, 26 : Synced_Callback, 27 : Synced_Callback, 28 : Synced_Callback, 29 : Synced_Callback, 52 : Synced_Callback}, combo_list=combos)
    else:
        # 1 just for the inital setup, callback for the "Add Unit" will create the new units starting from 1 as this alias will be 0.
        for card_num in range(1):
            add_text('Card Information', color=(255,50,50), parent=f'Card_Input_Tab_{card_num}', tag=f'Card_Information_Text_{card_num}')
            Widget_Aliases.tags_to_delete.append(f'Card_Information_Text_{card_num}')

            Table_Inputs(table_name=f'Card{card_num}_Table', row_name=f'Card{card_num}_Table_Row', class_name=Card,
                         use_child_window=False, table_parent=f'Card_Input_Tab_{card_num}', table_height=83, table_width=1650,
                         row_width=85, transformation=True, transformation_card_num=card_num)
    

#################################################################################################################################################################################################################################################################

def Card_Queries():
    config = Config_Read()
    

    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)    
    cur = con.cursor()
    
    # print(Card_Checks.card_ids)
    # print(Card_Checks.card_names)
    # if get_value('Transformation_Check'):
    # Card_ID_List = Card_Checks.transformation_card_ids
    Card_Widgets()
    for card_num in range(len(Card_Checks.card_ids)):


        for i in range(2):

            data = Card_Checks.json_data[i]

            for row_names in range(len(Card.row_names) - 2):
                if cards[0][row_names] is None:
                    set_value(Card.row_names[row_names + 2] + '_Card_' + str(card_num) + '_Row_' + str(i), 'NULL')
                
                    
                else:
                    if Card.row_names[row_names + 2] == Card.row_names[5]:
                        rarity = cards[0][row_names]
                        set_value(Card.row_names[row_names + 2] + '_Card_' + str(card_num) + '_Row_' + str(i), Card_Table_Combos.rarity_combo[rarity])
                    elif Card.row_names[row_names + 2] == Card.row_names[12]:
                        # print(cards[0][row_names])
                        set_value(Card.row_names[row_names + 2] + '_Card_' + str(card_num) + '_Row_' + str(i), Card_Table_Combos.element_dict[str(cards[0][row_names])])
                    elif Card.row_names[row_names + 2] == Card.row_names[23] or Card.row_names[row_names + 2] == Card.row_names[24] or Card.row_names[row_names + 2] == Card.row_names[25] or Card.row_names[row_names + 2] == Card.row_names[26] or Card.row_names[row_names + 2] == Card.row_names[27] or Card.row_names[row_names + 2] == Card.row_names[28] or Card.row_names[row_names + 2] == Card.row_names[29]:
                        
                        set_value(Card.row_names[row_names + 2] + '_Card_' + str(card_num) + '_Row_' + str(i), str(cards[0][row_names]) + ': ' + str(Card_Table_Combos.link_skill_dict[cards[0][row_names]]))
                    elif Card.row_names[row_names + 2] == Card.row_names[52]:
                        if cards[0][row_names] is None:
                            set_value(Card.row_names[row_names + 2] + '_Card_' + str(card_num) + '_Row_' + str(i), 'NULL')
                        elif 10 <= cards[0][row_names] < 20:
                            set_value(Card.row_names[row_names + 2] + '_Card_' + str(card_num) + '_Row_' + str(i), Card_Table_Combos.potential_board_combo[0])
                        elif 20 <= cards[0][row_names] < 30:
                            set_value(Card.row_names[row_names + 2] + '_Card_' + str(card_num) + '_Row_' + str(i), Card_Table_Combos.potential_board_combo[1])
                        else:
                            set_value(Card.row_names[row_names + 2] + '_Card_' + str(card_num) + '_Row_' + str(i), Card_Table_Combos.potential_board_combo[2])
                    else:
                        set_value(Card.row_names[row_names + 2] + '_Card_' + str(card_num) + '_Row_' + str(i), cards[0][row_names])
                    
            char_list = list(str(Card_Checks.card_ids[card_num]))  
            char_list[1] = '3'  
            new_string = ''.join(char_list)  
            new_string = new_string[:-1] + str(i)
            set_value(Card.row_names[0] + '_Card_' + str(card_num) + '_Row_' + str(i), new_string)
            
            set_value(Card.row_names[1] + '_Card_' + str(card_num) + '_Row_' + str(i), Card_Checks.card_names[card_num][0])
                    
        add_separator(tag=f'Card_Separator_{card_num}', parent=f'Card_Input_Tab_{card_num}')
        Widget_Aliases.tags_to_delete.append(f'Card_Separator_{card_num}')
        
        # Setting Optimal Awakening Growth
        # set_value(Card.row_names[16] + '_Card_' + str(card_num) + '_Row_' + '1', get_value(Card.row_names[0] + '_Card_' + str(card_num) + '_Row_' + '1'))
