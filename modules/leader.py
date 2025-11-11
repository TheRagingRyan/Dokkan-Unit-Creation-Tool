from dearpygui.dearpygui import *
from . configs import Config_Read
from . classes import String_Length, Leader_Skill_Info, Widget_Aliases, Card_Checks
from . functions import Delete_Items, Table_Inputs, Row_Checker, Table_ID
# from . categories import Category_Icon_Download
import sqlite3
import ast
import re


def Define_Leader_Skill_Type(leader_desc):
    categories = re.findall(r'"([^"]*)"', leader_desc)
    num_of_categories = len(categories)
    element_found = False
    element_type = ''
    
    if any(element in leader_desc for element in ['INT', 'AGL', 'TEQ', 'STR', 'PHY']):
        element_found = True
    
    if 'STR' in leader_desc:
        Card_Checks.leader_skill_element_type == 'STR'
        
    elif 'TEQ' in leader_desc:
        Card_Checks.leader_skill_element_type == 'TEQ'
        
    elif 'PHY' in leader_desc:
        Card_Checks.leader_skill_element_type == 'PHY'
        
    elif 'AGL' in leader_desc:
        Card_Checks.leader_skill_element_type == 'AGL'
        
    elif 'INT' in leader_desc:
        Card_Checks.leader_skill_element_type == 'INT'
    
    if num_of_categories == 8:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[10]
    
    elif num_of_categories == 5:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[9]
        
    elif num_of_categories == 4:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[8]
        
    elif num_of_categories == 3:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[7]
        
    elif num_of_categories == 2:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[6]
        
    elif num_of_categories == 1 and element_found:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[5]
        
    elif num_of_categories == 1 and not element_found:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[4]
    
    elif num_of_categories == 0 and 'All' in leader_desc:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[3]
        
    elif num_of_categories == 0 and 'Super Class' in leader_desc:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[2]
        
    elif num_of_categories and 'Extreme Class' in leader_desc:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[1]
        
    elif num_of_categories == 0 and element_found:
        Card_Checks.leader_skill_type = Leader_Skill_Info.leader_cat_combo_names[0]
        

def Text_Resize(tag_id):
    text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIAL.ttf')
    set_item_width(tag_id, text_width + 27)
    
def Leader_Widget_Alias_Check_List(tag_id_list, leader_rows):
    for i in range(leader_rows):
        for z in range(len(tag_id_list)):
            if does_alias_exist(tag_id_list[z] + str(i)):
                delete_item(tag_id_list[z] + str(i))
                
    
def Leader_Widget_Alias_Check(tag_id, leader_rows):
    for i in range(leader_rows):
        if does_alias_exist(tag_id + str(i)):
            delete_item(tag_id + str(i))

def Resize_Description(tag_id, leader_description):
        newline_count = leader_description.count('\n')
        set_item_height(tag_id, 14.5 * newline_count + 20)
        width, height = get_text_size(leader_description, font='fonts/ARIAL.ttf')
        set_item_width(tag_id, width + 4)
            
def Leader_Resize(tag_id):
        str_length = String_Length.length
        tag_value = get_value(tag_id)
        name = len(tag_value)
        set_item_width(tag_id, str_length[name])
        
def Leader_Skill_Set_Resize(tag_id, sender):
    for i in range(Leader_Skill_Info.rows):
        
        text_width, text_height = get_text_size(get_value(f'l_leader_skill_set_id_{i}'), font='fonts/ARIALBD.ttf')
        set_item_width(f'l_leader_skill_set_id_Card_0_Row_{i}', text_width + 10)
        set_value('l_leader_skill_set_id_' + '_Card_' + '0' + '_Row_' + str(i), sender)
        
def Resize_Widget(tag_id):
    text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIALBD.ttf')
    if text_width == 0.0:
        set_item_width(tag_id, String_Length.length[0])
    else:
        set_item_width(tag_id, text_width + 10)
    # print(text_width)
    
def Leader_Skills_Value_Presets(card, row_num, exec_timing_type, target_type, sub_target, causality, efficacy_type, efficacy_values, calc_option):
    card = str(card)
    # configure_item('l_efficacy_values_' + str(row_num), width=String_Length.length[15])
    # configure_item('l_efficacy_values_' + '1', width=String_Length.length[15])
    set_value(Leader_Skill_Info.row_names[0] + '_Card_' + card + '_Row_' + row_num, exec_timing_type)
    # Resize_Widget('l_exec_timing_type_' + row_num)
    set_value(Leader_Skill_Info.row_names[1] + '_Card_' + card + '_Row_' + row_num, target_type)
    # Resize_Widget('l_target_type_' + row_num)
    set_value(Leader_Skill_Info.row_names[2] + '_Card_' + card + '_Row_' + row_num, sub_target)
    # Resize_Widget('l_sub_target_type_set_id_' + row_num)
    set_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + row_num, causality)
    # Resize_Widget('l_causality_conditions_' + row_num)
    set_value(Leader_Skill_Info.row_names[4] + '_Card_' + card + '_Row_' + row_num, efficacy_type)
    # Resize_Widget('l_efficacy_type_' + row_num)
    set_value(Leader_Skill_Info.row_names[5] + '_Card_' + card + '_Row_' + row_num, efficacy_values)
    # Resize_Widget('l_efficacy_values_' + row_num)
    set_value(Leader_Skill_Info.row_names[6] + '_Card_' + card + '_Row_' + row_num, calc_option)
    # Resize_Widget('l_calc_option_' + row_num)

        
def Leader_Create_Combos(*, card=0, custom_combo=[], num_of_combos=1, custom_combo_default_value='', custom_combo_callback=None, custom_combo_num=[]):
    for i in range(6):
        Delete_Items(f'Leader_Skill_Category_Selection_{card}_{i}')
    for t in range(num_of_combos):
        if not custom_combo:
            add_combo(Leader_Skill_Info.cat_list, default_value='Categories', tag=f'Leader_Skill_Category_Selection_{card}_{t}', width=String_Length.length[11], callback=Leader_Cat_Selection, parent=f'Leader_Skill_Widgets_Group_{card}_1')
            bind_item_font(f'Leader_Skill_Category_Selection_{card}_{t}', font='fonts/ARIALBD.ttf')
        else:
            # print(t)
            # print(custom_combo_num)
            if t + 1 in custom_combo_num:
                add_combo(custom_combo, tag=f'Leader_Skill_Category_Selection_{card}_{t}', default_value=custom_combo_default_value, width=String_Length.length[0], callback=custom_combo_callback, parent=f'Leader_Skill_Widgets_Group_{card}_1')
            else:
                add_combo(Leader_Skill_Info.cat_list, default_value='Categories', tag=f'Leader_Skill_Category_Selection_{card}_{t}', width=String_Length.length[11], callback=Leader_Cat_Selection, parent=f'Leader_Skill_Widgets_Group_{card}_1')
                bind_item_font(f'Leader_Skill_Category_Selection_{card}_{t}', font='fonts/ARIALBD.ttf')

def Leader_Skills_User_Data_Check(user_data, tag_id):
    ### Defaults to 0, thus can be used in this instance for both custom unit and regular EZAs
    card = Table_ID(tag_id)
    # for i in range(10):
        # Delete_Items(f'Leader_Skill_Category_Selection_0_{i + 1}')
    sub_target_set = ''
    if not get_value('CardID1'):
        sub_target_set = 'CardID from Card Input not found'
    else:
        sub_target_set = get_value('CardID1')
    # if not get_value('Custom_Unit'):
        # Leader_Skill_Widgets()
    # Element Type uses the Bitsets AGL = 1, TEQ = 2, INT = 4, STR = 8, PHY = 16
    # Not the Element ID
    ###################################################################################################################################################################################################
    if user_data == 'Element Type':
        Delete_Items(f'Leader_Skill_Category_Selection_{card}_0')
        Leader_Skill_Info.rows = 2
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=66, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='2', sub_target='0', causality='NULL', efficacy_type='83', efficacy_values='[4, 3, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='2', sub_target='0', causality='NULL', efficacy_type='82', efficacy_values='[4, 170, 0]', calc_option='2')
        leader_description = 'PHY Type Ki +3 and HP, ATK, DEF +170%'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        combo = ['Super AGL (4096)', 'Super TEQ (8192)', 'Super INT (16384)', 'Super STR (32768)', 'Super PHY (65536)', 'Extreme AGL (131072)', 'Extreme TEQ (262144)', 'Extreme INT (524288)', 'Extreme STR (1048576)', 'Extreme PHY (2097512)','AGL (0)', 'TEQ (1)', 'INT (2)', 'STR (3)', 'PHY (4)']
        result_dict = {re.search(r'\((\d+)\)', item).group(1): item for item in combo}
        element_bitset = ast.literal_eval(get_value(Leader_Skill_Info.row_names[6] + '00'))[0]
        
        Leader_Create_Combos(card=card, custom_combo=combo, num_of_combos=1, custom_combo_default_value='PHY (4)', custom_combo_callback=Leader_Ki_Selection)
        # add_combo(combo, default_value='TEQ', tag=f'Leader_Skill_Category_Selection_{card}_0', width=String_Length.length[11], callback=Leader_Ki_Selection, parent='Leader_Skill_Widgets_Group_1')
        set_value(f'Leader_Skill_Category_Selection_{card}_0', result_dict[str(element_bitset)])
        Text_Resize(f'Leader_Skill_Category_Selection_{card}_0')
        Leader_Skill_Info.last_rows = 2
    ###################################################################################################################################################################################################
    elif user_data == 'Extreme Class':
        Delete_Items(f'Leader_Skill_Category_Selection_{card}_0')
        Leader_Skill_Info.rows = 2
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=66, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='13', sub_target='0', causality='NULL', efficacy_type='83', efficacy_values='[64, 3, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='13', sub_target='0', causality='NULL', efficacy_type='82', efficacy_values='[64, 170, 0]', calc_option='2')
        leader_description = 'Extreme Class Ki +3 and HP, ATK, DEF +170%'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        
        Leader_Skill_Info.last_rows = 2
        
    ###################################################################################################################################################################################################     
    elif user_data == 'Super Class':
        Delete_Items(f'Leader_Skill_Category_Selection_{card}_0')
        Leader_Skill_Info.rows = 2
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=66, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='12', sub_target='0', causality='NULL', efficacy_type='83', efficacy_values='[32, 3, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='12', sub_target='0', causality='NULL', efficacy_type='82', efficacy_values='[32, 170, 0]', calc_option='2')
        leader_description = 'Super Class Ki +3 and HP, ATK, DEF +170%'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        Leader_Skill_Info.last_rows = 2
        
    ###################################################################################################################################################################################################  
    elif user_data == 'All Types':
        Delete_Items(f'Leader_Skill_Category_Selection_{card}_0')
        Leader_Skill_Info.rows = 2
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=66, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='2', sub_target='0', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='2', sub_target='0', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        leader_description = 'All Types Ki +3 and HP, ATK, DEF +170%'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        Leader_Skill_Info.last_rows = 2
        
    ###################################################################################################################################################################################################
    elif user_data == '1 Category':
        Leader_Skill_Info.rows = 2
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=66, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='83', efficacy_values='[31, 3, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        leader_description = '\"XXX0\" Category Ki +3 and HP, ATK, DEF +170%'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        Leader_Create_Combos(card=card, num_of_combos=1)
        Leader_Skill_Info.last_rows = 2
        
    ###################################################################################################################################################################################################
    elif user_data == '1 Category & 1 Element':
        Leader_Skill_Info.rows = 4
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=115, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='83', efficacy_values='[31, 3, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='2', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='83', efficacy_values='[4, 3, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='3', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='82', efficacy_values='[4, 170, 0]', calc_option='2')
        leader_description = '\"XXX0\" Category Ki +3 \nand HP, ATK, DEF +170%; \nor INT Type Ki +3 \nand HP, ATK, DEF +170%'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        
        combo = ['Super AGL (4096)', 'Super TEQ (8192)', 'Super INT (16384)', 'Super STR (32768)', 'Super PHY (65536)', 'Extreme AGL (131072)', 'Extreme TEQ (262144)', 'Extreme INT (524288)', 'Extreme STR (1048576)', 'Extreme PHY (2097512)','AGL (0)', 'TEQ (1)', 'INT (2)', 'STR (3)', 'PHY (4)']
        result_dict = {re.search(r'\((\d+)\)', item).group(1): item for item in combo}
        element_bitset = ast.literal_eval(get_value(Leader_Skill_Info.row_names[5] + '_Card_' + str(card) + '_Row_2'))[0]
        Leader_Create_Combos(card=card, custom_combo=combo, num_of_combos=2, custom_combo_default_value='INT (2)',custom_combo_num=[2], custom_combo_callback=Leader_Ki_Selection)
        set_value(f'Leader_Skill_Category_Selection_{card}_1', result_dict[str(element_bitset)])
        Leader_Skill_Info.last_rows = 4
       
    ###################################################################################################################################################################################################
    elif user_data == '2 Categories':
        Leader_Skill_Info.rows = 4
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=115, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='104', efficacy_values='[170, 170, 170]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='2', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='3', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='104', efficacy_values='[170, 170, 170]', calc_option='2')
        leader_description = '\"XXX0\" or \"XXX1\" Category \nKi +3 and HP, ATK & DEF +170%'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        Leader_Create_Combos(card=card, num_of_combos=2)
        Leader_Skill_Info.last_rows = 4
        
    ###################################################################################################################################################################################################
    elif user_data == '2 Categories & 1 Extra':
        Leader_Skill_Info.rows = 6
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=163, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='2', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='3', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='4', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '3', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='5', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '4', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        leader_description = f'\"XXX0\" or \"XXX1\" \nCategory Ki +3 and HP, ATK & DEF +170%, \nplus an additional HP, ATK & DEF +30% \nfor characters who also belong to the \n\"XXX2\" Category'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        Leader_Create_Combos(card=card, num_of_combos=3)
        Leader_Skill_Info.last_rows = 6
        
    ###################################################################################################################################################################################################
    elif user_data == '2 Categories & 2 Extra':
        Leader_Skill_Info.rows = 8
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=(24 * 8) + 23, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='2', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='3', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='4', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '3', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='5', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '4', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='6', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '5', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='7', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '6', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        leader_description = f'\"XXX0\" or \"XXX1\" \nCategory Ki +3 and HP, ATK & DEF +170%, \nplus an additional HP, ATK & DEF +30% \nfor characters who also belong to the \n\"XXX2\" or \"XXX3\" Category'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        Leader_Create_Combos(card=card, num_of_combos=4)
        Leader_Skill_Info.last_rows = 8
        
    ###################################################################################################################################################################################################
    elif user_data == '3 Categories & 2 Extra':
        Leader_Skill_Info.rows = 12
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=307, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='2', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='3', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='4', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '3', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='5', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '3', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='6', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '4', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='7', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '5', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='8', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '6', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='9', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '7', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='10', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '8', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='11', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '9', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        leader_description = f'\"XXX0\", \"XXX1\" or \"XXX2\" \nCategory Ki +3 and HP, ATK & DEF +170%, \nplus an additional HP, ATK & DEF +30% \nfor characters who also belong to the \n\"XXX3\" or \"XXX4\" Category'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        Leader_Create_Combos(card=card, num_of_combos=5)
        Leader_Skill_Info.last_rows = 12
        
    ###################################################################################################################################################################################################
    elif user_data == '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)':
        Leader_Skill_Info.rows = 14
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=360, table_width=760)
        Leader_Skills_Value_Presets(card=card, row_num='0', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='1', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '1', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='2', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='3', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '2', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='4', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '3', causality='NULL', efficacy_type='5', efficacy_values='[3, 0, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='5', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '3', causality='NULL', efficacy_type='82', efficacy_values='[31, 170, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='6', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '4', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='7', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '5', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='8', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '6', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='9', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '7', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='10', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '8', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='11', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '9', causality='NULL', efficacy_type='82', efficacy_values='[31, 30, 0]', calc_option='2')
        Leader_Skills_Value_Presets(card=card, row_num='12', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '10', causality='NULL', efficacy_type='83', efficacy_values='[64, 3, 0]', calc_option='0')
        Leader_Skills_Value_Presets(card=card, row_num='13', exec_timing_type='1', target_type='2', sub_target=sub_target_set + '10', causality='NULL', efficacy_type='82', efficacy_values='[64, 150, 0]', calc_option='2')
        leader_description = f'\"XXX0\", \"XXX1\" or \n\"XXX2\" Category Ki +3 and \nHP, ATK & DEF +170%, \nplus an additional \nHP, ATK & DEF +30% for characters who \nalso belong to the \"XXX3\" or \n\"XXX4\" Category; Extreme Class \nKi +3 and HP, ATK & DEF +150% \n(\"XXX0\", \"XXX1\", or \n\"XXX2\" Category characters excluded)'
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
        Resize_Description(f'Leader_Desc_Text_Input_{card}', leader_description)
        Leader_Create_Combos(card=card, num_of_combos=6, custom_combo=['Extreme Class', 'Super Class'], custom_combo_default_value='Extreme Class', custom_combo_num=[6], custom_combo_callback=Leader_Class_Selection)
        Leader_Skill_Info.last_rows = 14
        # add_combo(['Extreme Class', 'Super Class'], default_value='Extreme Class', tag=f'Leader_Skill_Category_Selection_0_5', width=String_Length.length[11], callback=Leader_Class_Selection, parent='Leader_Skill_Widgets_Group_1')
        Text_Resize(f'Leader_Skill_Category_Selection_{card}_5')
        # print('Leader_Skill_Category_Selection_0_5')
    ###################################################################################################################################################################################################
   
def Leader_Combo(tag_id, user_data):
    card = Table_ID(tag_id)
    Text_Resize(tag_id)
    try:
        if does_alias_exist(Leader_Skill_Info.last_selection_groups[0]):
            for y in range(len(Leader_Skill_Info.last_selection_groups)):
                delete_item(Leader_Skill_Info.last_selection_groups[y])
            for x in range(len(Leader_Skill_Info.last_selection_tags)):
                delete_item(Leader_Skill_Info.last_selection_tags[x])

    except IndexError:
        pass
    

    Leader_Skill_Info.last_selection_groups.clear()
    Leader_Skill_Info.last_selection_tags.clear()

    Leader_Skills_User_Data_Check(user_data, tag_id)
    # Leader_Skill_Info.last_selection_groups.append(Leader_Skill_Info.input_text_widgets[z] + str(i))
    
    
    
    if get_value(f'Leader_Efficacy_Value_Changer_{card}'):
        Leader_Efficacy_Value_Changer(f'Leader_Efficacy_Value_Changer_{card}', get_value(f'Leader_Efficacy_Value_Changer_{card}'))
    # for y in range(Leader_Skill_Info.rows):
        # set_value(Leader_Skill_Info.row_names[0] + '_Card_' + str(card) + '_Row_' + str(y), get_value('CardID1'))

    # Removing any existing combos from below this, in order to avoid 'alias exists' errors.
    # for g in range(5):
        # if does_alias_exist(f'Leader_Skill_Category_Selection_0_{g + 1}'):
            # delete_item(f'Leader_Skill_Category_Selection_0_{g + 1}')
            
    # Adding combo lists for 'Categories' based on the selected preset.

        
    # Resetting the Category combo lists to 'Categories' whenever a new preset is selected.
    # In order to avoid possible incorrect value grabbing in SQL outputting.
    # for u in range(5):
        # if does_alias_exist(f'Leader_Skill_Category_Selection_0_{u}'):
            # set_value(f'Leader_Skill_Category_Selection_0_{u}', 'Categories')
            # set_item_width(f'Leader_Skill_Category_Selection_0_{u}',String_Length.length[11])

    
### Needs modification of card number should I re-add this
def Leader_Efficacy_Value_Changer(tag_id, sender):
    card = Table_ID(tag_id)
    efficacy_values = ''
    Text_Resize(tag_id)
    for i in range(Row_Checker(Leader_Skill_Info.row_names[0] + '_Card_' + card + '_Row_')):
        if get_value(Leader_Skill_Info.row_names[4] + '_Card_' + str(card) + '_Row_' + str(i)) == '82':
            efficacy_values = get_value(Leader_Skill_Info.row_names[5] + '_Card_' + str(card) + '_Row_' + str(i))
            efficacy_values = ast.literal_eval(efficacy_values)
            if efficacy_values[1] == 30:
                pass
            else:
                try:
                    efficacy_values[1] = int(sender)
                except ValueError:
                    efficacy_values[1] = 0
                set_value(Leader_Skill_Info.row_names[6] + '_Card_' + str(card) + '_Row_' + str(i), efficacy_values)
                
        elif get_value(Leader_Skill_Info.row_names[4] + '_Card_' + str(card) + '_Row_' + str(i)) == '104':
            efficacy_values = get_value(Leader_Skill_Info.row_names[5] + '_Card_' + str(card) + '_Row_' + str(i))
            if efficacy_values[1] == 30:
                pass
            else:
                efficacy_values = ast.literal_eval(efficacy_values)
                try:
                    efficacy_values = [int(sender), int(sender), int(sender)]
                except ValueError:
                    efficacy_values = [0, 0, 0]
                set_value(Leader_Skill_Info.row_names[5] + '_Card_' + str(card) + '_Row_' + str(i), efficacy_values)

def Leader_Cat_Selection(tag_id, user_data):
    ### Remove the last 2 characters to get card number from the tag_id string
    card = Table_ID(tag_id[:-2])
    Text_Resize(tag_id)
    
    def Desc_Replace(cat_num):
        pattern = r'\((\d+)\)'
        cat = get_value(f'Leader_Desc_Text_Input_{card}')
        unit_category_names = re.findall(r'"(.*?)"', cat)
        if 'XXX' + cat_num in cat:
            cat_re = re.sub(pattern, '', user_data)
            cat_re = cat_re[:-1]
            # print(cat_re)
            cat = cat.replace(f'XXX{cat_num}', cat_re)
            # print(cat)
            set_value(f'Leader_Desc_Text_Input_{card}', cat)
            # set_value('leader_last_selection_' + cat_num, cat_re)
            Text_Resize(f'Leader_Desc_Text_Input_{card}')
        else:
            
            cat_re = re.sub(pattern, '', user_data)
            cat_re = cat_re[:-1]
            cat = cat.replace(unit_category_names[int(cat_num)], cat_re)
            # print(cat_re)
            # print(cat)
            set_value(f'Leader_Desc_Text_Input_{card}', cat)
            # print(get_value('leader_last_selection_' + cat_num))
            # set_value('leader_last_selection_' + cat_num, cat_re)
            Text_Resize(f'Leader_Desc_Text_Input_{card}')
            
    if tag_id == f'Leader_Skill_Category_Selection_{card}_0':
        Desc_Replace('0')
        Text_Resize(tag_id)
    elif tag_id == f'Leader_Skill_Category_Selection_{card}_1':
        Desc_Replace('1')
        Text_Resize(tag_id)
    elif tag_id == f'Leader_Skill_Category_Selection_{card}_2':
        Desc_Replace('2')
        Text_Resize(tag_id)
    elif tag_id == f'Leader_Skill_Category_Selection_{card}_3':
        Desc_Replace('3')
        Text_Resize(tag_id)
    elif tag_id == f'Leader_Skill_Category_Selection_{card}_4':
        Desc_Replace('4')
        Text_Resize(tag_id)
    pass

def Leader_Class_Selection(tag_id, user_data):
    card = Table_ID(tag_id[:-2])
    leader_description = get_value(f'Leader_Desc_Text_Input_{card}')
    if user_data == 'Extreme Class':
        leader_description = leader_description.replace('Super Class', 'Extreme Class')
    else:
        leader_description = leader_description.replace('Extreme Class', 'Super Class')
    set_value(f'Leader_Desc_Text_Input_{card}', leader_description)
    Text_Resize(tag_id)

def Leader_Ki_Selection(tag_id, user_data):
    card = Table_ID({tag_id[:-2]})
    combo = ['Super AGL', 'Super TEQ', 'Super INT', 'Super STR', 'Super PHY', 'Extreme AGL', 'Extreme TEQ', 'Extreme INT', 'Extreme STR', 'Extreme PHY','AGL', 'TEQ', 'INT', 'STR', 'PHY']
    pattern = r' \(\d+\)'
    leader_description = get_value(f'Leader_Desc_Text_Input_{card}')
    combo_index = None
    element_type_in_description = ''
    
    # Iterate through the combo list
    for index, element in enumerate(combo):
        if element in leader_description:
            combo_index = index
            break 
        
    element_type_in_description = combo[combo_index]
    element_type = re.sub(pattern, '', user_data)
    efficacy_values = []
    replaced_efficacy_values = []
    
    # Use a regular expression to extract the numbers within parentheses
    numbers_in_parentheses = re.findall(r'\((\d+)\)', user_data)

    # Join the extracted numbers to create a new string
    result_string = ' '.join(numbers_in_parentheses)
    
    ### This skips the first 2 rows to change only row 3 and 4 with the elements
    if get_value(f'Leader_Skill_Preset_List_{card}') == '1 Category & 1 Element':
        for i in range(Leader_Skill_Info.rows):
            efficacy_values.append(get_value(Leader_Skill_Info.row_names[5] + str(card) + str(i)))
        for i in range(len(efficacy_values)):
            index_to_replace = ast.literal_eval(efficacy_values[i])
            if index_to_replace[0] != 0:
                index_to_replace[0] = int(result_string)
            replaced_efficacy_values.append(index_to_replace)

        for i in range(len(replaced_efficacy_values) - 3):
            set_value(Leader_Skill_Info.row_names[5] + str(card) + str(i + 2), replaced_efficacy_values[i])
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description.replace(element_type_in_description, element_type))
        Text_Resize(tag_id)
        
    else:
        for i in range(Leader_Skill_Info.rows):
            efficacy_values.append(get_value(Leader_Skill_Info.row_names[5] + str(card) + str(i)))
        for i in range(len(efficacy_values)):
            index_to_replace = ast.literal_eval(efficacy_values[i])
            if index_to_replace[0] != 0:
                index_to_replace[0] = int(result_string)
            replaced_efficacy_values.append(index_to_replace)

        for i in range(len(replaced_efficacy_values)):
            set_value(Leader_Skill_Info.row_names[5] + str(card) + str(i), replaced_efficacy_values[i])
        set_value(f'Leader_Desc_Text_Input_{card}', leader_description.replace(element_type_in_description, element_type))
        Text_Resize(tag_id)
    
    
    # print(replaced_efficacy_values)
    # print(element_type_in_description)
    

def Leader_Skill_Widgets():
    str_length = String_Length.length
    leader_options = ['Element Type', 'Extreme Class', 'Super Class', 'All Types', '1 Category', '1 Category & 1 Element', '2 Categories', '2 Categories & 1 Extra', '2 Categories & 2 Extra', '3 Categories & 2 Extra', '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)']
    leader_categories = Leader_Skill_Info.cat_list
    ### Defaults to 0 so can be used in both custom and EZA as queried units will only have one leader skill
    card = 0
    # for i in range(len(Leader_Skill_Info.tags_to_remove)):
        # Delete_Items(Leader_Skill_Info.tags_to_remove[i])
    Delete_Items(f'Leader_Skill_Widgets_Group_{card}_1')
    Delete_Items(f'Leader_Skill_Widgets_Group_{card}_2')
    Delete_Items(f'Leader_Skill_Text_{card}')
    Delete_Items(f'Leader_Skill_Preset_List_{card}')
    Delete_Items(f'Leader_Skill_Category_Selection_{card}_0')
    Delete_Items(f'Leader_Name_Text_Input_{card}')
    Delete_Items(f'Leader_Desc_Text_Input_{card}')
    
    with group(horizontal=True, tag=f'Leader_Skill_Widgets_Group_{card}_1', parent=f'Leader_Skill_{card}'):
        add_text('Leader Skill', tag=f'Leader_Skill_Text_{card}', color=(255,50,50), parent=f'Leader_Skill_Widgets_Group_{card}_1')
        
        
        add_combo(leader_options, default_value='Presets', tag=f'Leader_Skill_Preset_List_{card}', width=str_length[9], callback=Leader_Combo, parent=f'Leader_Skill_Widgets_Group_{card}_1')
        
        add_combo(leader_categories, default_value='Categories', tag=f'Leader_Skill_Category_Selection_{card}_0', width=str_length[11], callback=Leader_Cat_Selection, parent=f'Leader_Skill_Widgets_Group_{card}_1')
        
        
        # for t in range(4):
        #     add_combo(leader_categories, default_value='Categories', tag=f'Leader_Skill_Category_Selection_0_{t + 1}', width=str_length[11], callback=Leader_Cat_Selection)
        

    
    with group(horizontal=True, parent=f'Leader_Skill_{card}', tag=f'Leader_Skill_Widgets_Group_{card}_3'):
        add_text('Name:  ', tag=f'Leader_Skill_Name_Text_{card}')
        add_input_text(default_value='', tag=f'Leader_Name_Text_Input_{card}', hint='Name', width=str_length[0], callback=Leader_Resize)
    with group(horizontal=True, parent=f'Leader_Skill_{card}', tag=f'Leader_Skill_Widgets_Group_{card}_4'):
        add_text('Desc:   ', tag=f'Leader_Skill_Desc_Text_{card}')
        add_input_text(default_value='', tag=f'Leader_Desc_Text_Input_{card}', hint='Description', width=str_length[0], callback=Resize_Widget, multiline=True)

    with group(horizontal=True, parent=f'Leader_Skill_{card}', tag=f'Leader_Skill_Widgets_Group_{card}_2'):
        add_text('Percent', tag=f'Leader_Skill_Percentage_Text_{card}')
        add_input_text(hint='XXX%', width=str_length[0], callback=Leader_Efficacy_Value_Changer, tag=f'Leader_Efficacy_Value_Changer_{card}', parent=f'Leader_Skill_Widgets_Group_{card}_2')
        
        add_text('%', tag=f'Leader_Efficacy_Value_Changer_Text_{card}', parent=f'Leader_Skill_Widgets_Group_{card}_2')
        
        with tooltip(f'Leader_Efficacy_Value_Changer_Text_{card}', tag=f'Leader_Efficacy_Value_Changer_Tooltip_{card}'):
            add_text('Type what percent you want the leader skill to use')
            
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Widgets_Group_{card}_1')
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Widgets_Group_{card}_2')
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Widgets_Group_{card}_3')
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Widgets_Group_{card}_4')
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Text_{card}')
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Preset_List_{card}')
    Widget_Aliases.tags_to_delete.append(f'Leader_Name_Text_Input_{card}')
    Widget_Aliases.tags_to_delete.append(f'Leader_Desc_Text_Input_{card}')
    Widget_Aliases.tags_to_delete.append(f'Leader_Efficacy_Value_Changer_{card}')
    Widget_Aliases.tags_to_delete.append(f'Leader_Efficacy_Value_Changer_Text_{card}')
    Widget_Aliases.tags_to_delete.append(f'Leader_Efficacy_Value_Changer_Tooltip_{card}')

    

    
def Leader_Skill_Set_Values(list_info, *, card=0):
    print("Leader_Skill_Set_Values called")


    for skill in range(len(list_info)):
        for key, value in list_info[skill].items():
            if value == "":
                set_value(f'l_{key}_Card_{str(card)}_Row_{str(skill)}', 'NULL')
                # print('---------------------------------')
                # print(key,value)
            else:
                set_value(f'l_{key}_Card_{str(card)}_Row_{str(skill)}', value)



    # for skill in range(len(list_info)):
    #     for key, value in skill[skill].items():
    #         set_value(f'l_{key}_Card_{str(card)}_Row_{str(skill)}', value)

    # for i in range(len(list_info)):
    #     # set_value(Leader_Skill_Info.row_names[0] + '_Card_' + card + '_Row_' + str(i), str(get_value('CardID1')))
    #     for z in range(len(Leader_Skill_Info.row_names)):
    #         if not Leader_Skill_Info.row_names[z]:
    #             set_value(Leader_Skill_Info.row_names[z] + '_Card_' + str(card) + '_Row_' + str(i), 'NULL')
    #         else:
    #             if Leader_Skill_Info.row_names[z] == Leader_Skill_Info.row_names[3]:
    #                 set_value(Leader_Skill_Info.row_names[z] + '_Card_' + str(card) + '_Row_' + str(i), 'NULL')
    #             else:
    #                 set_value(Leader_Skill_Info.row_names[z] + '_Card_' + str(card) + '_Row_' + str(i), list_info[i][z])
    
    # last_value = ''
    # for row in range(Leader_Skill_Info.rows):
        # if row == 0:
            # last_value = get_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + '0')
            # set_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + '0', str(get_value('CardID1')) + '1')
        # else:
            # print(get_value(f'l_sub_target_type_set_id_0{row}'))
            # print(get_value(f'l_sub_target_type_set_id_0{row - 1}'))
            # if get_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + str(row)) == last_value:
                # last_value = get_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + str(row))
                # set_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + str(row), get_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + str(row - 1)))
            # else:
                # last_value = get_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + str(row))
                # set_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + str(row), int(get_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + str(row))) + 1)
        

            # print(tag_name[z] + str(i), list_info[i][z])

    
def Leader_Skill_Query():
    # Add a set_value for leader skill rows
    leader_skill_set_id = get_value('Leader_Skill_ID')
    
    config = Config_Read()
    
    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
    cur = con.cursor()
    
    
    cur.execute('SELECT exec_timing_type,target_type,sub_target_type_set_id,causality_conditions,efficacy_type,efficacy_values,calc_option FROM leader_skills WHERE leader_skill_set_id = ' + leader_skill_set_id)
    leader_info = cur.fetchall()
    
    # Removes any lingering rows should there be a preset selected upon query
    # for i in range(Leader_Skill_Info.rows):
        # if does_alias_exist(f'l_exec_timing_type_{i}'):
            # for z in range(len(Leader_Skill_Info.input_text_widgets)):
                # delete_item(Leader_Skill_Info.input_text_widgets[z] + str(i))
    # set_value('Leader_Skill_Preset_List_0', 'Presets')
    # set_item_width('Leader_Skill_Preset_List_0', String_Length.length[9])
                
    
    
    Leader_Skill_Widgets()
    Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_0', row_name=f'Leader_Skill_Row_0_', class_name=Leader_Skill_Info,
                    use_child_window=False, table_parent=f'Leader_Skill_0', transformation=True, transformation_card_num=0, table_height=66, table_width=867)
    # print(Leader_Skill_tags)
    
    Leader_Skill_Set_Values(leader_info)
    set_value('Leader_Skill_Rows', len(leader_info))
    set_item_height('Leader_Skill_Table_0', (24 * len(leader_info)) + 23)
    
    # Part of the category combo callbacks. Grabbing the index of the matching categories strings, as the list is in a specific order. Ex. "DB Saga" Category ID isn't 0 but it's index is.
    category_index_list = []
    leader_skill_description = get_value(f'Leader_Desc_Text_Input_0')
    # category_combos = Row_Checker(f'Leader_Skill_Category_Selection_0_')
    # print(category_combos)
    
    matches = re.findall(r'"(.*?)"', leader_skill_description)
    for z in range(len(matches)):
        category_index_list.append(next((i for i, category in enumerate(Leader_Skill_Info.cat_list) if matches[z] in category), None))
    
    if len(matches) > 5:
        matches = list(set(matches))
        ### Set to 6 just so the bottom section works correctly
        category_combos = 6
    # print(matches)
    for t in range(len(matches) - 1):
        add_combo(Leader_Skill_Info.cat_list, default_value='Categories', tag=f'Leader_Skill_Category_Selection_0_{t + 1}', width=String_Length.length[11], callback=Leader_Cat_Selection, parent='Leader_Skill_Widgets_Group_0_1')
        bind_item_font(f'Leader_Skill_Category_Selection_0_{t + 1}', font='fonts/ARIALBD.ttf')
        
    for i in range(len(matches)):
        # print(Leader_Skill_Info.cat_list[category_index_list[i]])
        set_value(f'Leader_Skill_Category_Selection_0_{i}', Leader_Skill_Info.cat_list[category_index_list[i]])
        Text_Resize(f'Leader_Skill_Category_Selection_0_{i}')
    
    def Reset_Sub_Target_Rows():
        for i in range(Leader_Skill_Info.rows):
            set_value(Leader_Skill_Info.row_names[3] + '_Card_' + '0' + '_Row_' + str(i), '0')
        
    if len(leader_info) == 14:
        add_combo(['Extreme Class', 'Super Class'], default_value='Extreme Class', tag=f'Leader_Skill_Category_Selection_0_5', width=String_Length.length[11], callback=Leader_Cat_Selection, parent='Leader_Skill_Widgets_Group_0_1')
        if 'Super Class' in get_value(f'Leader_Desc_Text_Input_0'):
            set_value(f'Leader_Skill_Category_Selection_0_5', 'Super Class')
        else:
            set_value(f'Leader_Skill_Category_Selection_0_5', 'Extreme Class')
        set_value('Leader_Skill_Preset_List_0', '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)')
        Text_Resize('Leader_Skill_Preset_List_0')
        Text_Resize('Leader_Skill_Category_Selection_0_5')
    elif len(leader_info) == 12:
        set_value('Leader_Skill_Preset_List_0', '3 Categories & 2 Extra')
        Text_Resize('Leader_Skill_Preset_List_0')
    elif len(leader_info) == 8:
        set_value('Leader_Skill_Preset_List_0', '2 Categories & 2 Extra')
        Text_Resize('Leader_Skill_Preset_List_0')
    elif len(leader_info) == 6:
        set_value('Leader_Skill_Preset_List_0', '2 Categories & 1 Extra')
        Text_Resize('Leader_Skill_Preset_List_0')
    elif len(matches) == 2:
        set_value('Leader_Skill_Preset_List_0', '2 Categories')
        Text_Resize('Leader_Skill_Preset_List_0')
    elif len(matches) == 1 and Leader_Skill_Info.rows >= 4:
        set_value('Leader_Skill_Preset_List_0', '1 Category & 1 Element')
        if does_alias_exist(Leader_Skill_Info.row_names[3] + '04'):
            set_value(Leader_Skill_Info.row_names[3] + '_Card_' + '0' + '_Row_' + '4', '0')
        combo = ['Super AGL (4096)', 'Super TEQ (8192)', 'Super INT (16384)', 'Super STR (32768)', 'Super PHY (65536)', 'Extreme AGL (131072)', 'Extreme TEQ (262144)', 'Extreme INT (524288)', 'Extreme STR (1048576)', 'Extreme PHY (2097512)','AGL (0)', 'TEQ (1)', 'INT (2)', 'STR (3)', 'PHY (4)']
        result_dict = {re.search(r'\((\d+)\)', item).group(1): item for item in combo}
        element_bitset = ast.literal_eval(get_value(Leader_Skill_Info.row_names[6] + '_Card_' + '0' + '_Row_' + '0'))[0]
        Leader_Create_Combos(custom_combo=combo, num_of_combos=2, custom_combo_default_value='INT (2)',custom_combo_num=[2], custom_combo_callback=Leader_Ki_Selection)
        
        ### Getting the first category and setting the category combo to it.
        extracted_text = re.findall(r'"([^"]*)"', get_value(f'Leader_Desc_Text_Input_0'))

        # Print the extracted text
        for text in extracted_text:
            text = text
        index_value = ''
        
        for items in range(len(Leader_Skill_Info.cat_list)):
            if text in Leader_Skill_Info.cat_list[items]:
                index_value = Leader_Skill_Info.cat_list[items]
                break
            
        ### Getting Efficacy_Values from leader skill, converting to a list to grab the first index,
        ### then setting it to the combo value later using result_dict
        element_type = get_value(Leader_Skill_Info.row_names[6] + '_Card_' + '0' + '_Row_' + '2')
        element_type_list = ast.literal_eval(element_type)
        element_type = element_type_list[0]
        
        
        set_value('Leader_Skill_Category_Selection_0_0', index_value)
        Text_Resize('Leader_Skill_Category_Selection_0_0')
        try:
            set_value('Leader_Skill_Category_Selection_0_1', result_dict[str(element_type)])
        except KeyError:
            set_value('log_1', 'Leader Skill Not a Preset, can ignore or modify the leader skill')
        Text_Resize('Leader_Skill_Preset_List_0')
        Text_Resize('Leader_Skill_Category_Selection_0_1')
    elif Leader_Skill_Info.rows == 2 and int(get_value(Leader_Skill_Info.row_names[2] + '_Card_' + '0' + '_Row_' + '0')) <= 2:
        set_value('Leader_Skill_Preset_List_0', '1 Category')
        Text_Resize('Leader_Skill_Preset_List_0')
    elif get_value(Leader_Skill_Info.row_names[2] + '_Card_' + '0' + '_Row_' + '0') == '12':
        set_value('Leader_Skill_Preset_List_0', 'Super Class')
        Text_Resize('Leader_Skill_Preset_List_0')
        Reset_Sub_Target_Rows()
        Delete_Items('Leader_Skill_Category_Selection_0_0')
    elif get_value(Leader_Skill_Info.row_names[2] + '_Card_' + '0' + '_Row_' + '0') == '13':
        set_value('Leader_Skill_Preset_List_0', 'Extreme Class')
        Text_Resize('Leader_Skill_Preset_List_0')
        Reset_Sub_Target_Rows()
        Delete_Items('Leader_Skill_Category_Selection_0_0')
    ### Uses ast to turn the efficacy values into a list, then checks the first index; being the element bitset
    elif ast.literal_eval(get_value(Leader_Skill_Info.row_names[6] + '_Card_' + '0' + '_Row_' + '0'))[0] in (0,1,2,3,4,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097512) and int(get_value(Leader_Skill_Info.row_names[5] + '_Card_' + '0' + '_Row_' + '0')) not in (5, 83):
        set_value('Leader_Skill_Preset_List_0', 'Element Type')
        Text_Resize('Leader_Skill_Preset_List_0')
        Reset_Sub_Target_Rows()
        combo = ['AGL (0)', 'TEQ (1)', 'INT (2)', 'STR (3)', 'PHY (4)', 'Super AGL (4096)', 'Super TEQ (8192)', 'Super INT (16384)', 'Super STR (32768)', 'Super PHY (65536)', 'Extreme AGL (131072)', 'Extreme TEQ (262144)', 'Extreme INT (524288)', 'Extreme STR (1048576)', 'Extreme PHY (2097512)']
        result_dict = {re.search(r'\((\d+)\)', item).group(1): item for item in combo}
        element_bitset = ast.literal_eval(get_value(Leader_Skill_Info.row_names[6] + '_Card_' + '0' + '_Row_' + '0'))[0]
        Delete_Items('Leader_Skill_Category_Selection_0_0')
        add_combo(combo, default_value='TEQ', tag=f'Leader_Skill_Category_Selection_0_0', width=String_Length.length[11], callback=Leader_Ki_Selection, parent='Leader_Skill_Widgets_Group_0_1')
        set_value('Leader_Skill_Category_Selection_0_0', result_dict[str(element_bitset)])
        Text_Resize('Leader_Skill_Category_Selection_0_0')
    else: ### All Types
        set_value('Leader_Skill_Preset_List_0', 'All Types')
        Text_Resize('Leader_Skill_Preset_List_0')
        Reset_Sub_Target_Rows()
    
    

# def Leader_Skill_Custom():
    # Leader_Skill_Info.input_text_widgets = ['l_leader_skill_set_id_', 'l_exec_timing_type_', 'l_target_type_', 'l_sub_target_type_set_id_', 'l_causality_conditions_', 'l_efficacy_type_', 'l_efficacy_values_', 'l_calc_option_']
    # Leader_Skill_Info.input_text_widgets_hints = ['leader_skill_set_id', 'exec_timing_type', 'target_type', 'sub_target_type_set_id', 'causality_conditions', 'efficacy_type', 'efficacy_values', 'calc_option']
    
    