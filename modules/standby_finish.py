import sqlite3
from dearpygui.dearpygui import *
from . configs import Config_Read
from . functions import Table_Inputs, Delete_Items, Text_Resize
from .classes import String_Length, Card_Checks, Widget_Aliases, Standby_Skill_Set, Standby_Skill, Finish_Skill_Set, Finish_Skill
import ast

#####################################################################################################################################################################################
#####################################################################################################################################################################################
#####################################################################################################################################################################################

def Standby_Skill_Widgets(*, card=0, standby_skill=0):
    add_text('Standby Skill Set', color=(255,50,50), parent=f'Standby_Skill_{card}', tag=f'Standby_Skill_Set_Text_{card}_{standby_skill}')
    
    with group(horizontal=True, parent=f'Standby_Skill_{card}', tag=f'Standby_Skill_Set_Group_1_{card}_{standby_skill}'):
        add_text('Name:', color=(255, 174, 26), parent=f'Standby_Skill_Set_Group_1_{card}_{standby_skill}', tag=f'Standby_Skill_Name_Text_{card}_{standby_skill}')
        add_input_text(tag=f'Standby_Set_Name_Input_Text_{card}_{standby_skill}', hint='Name', default_value='', width=String_Length.length[0], callback=Text_Resize, parent=f'Standby_Skill_Set_Group_1_{card}_{standby_skill}')
        
    with group(horizontal=True, parent=f'Standby_Skill_{card}', tag=f'Standby_Skill_Set_Group_2_{card}_{standby_skill}'):        
        add_text('Desc: ', color=(255, 174, 26), parent=f'Standby_Skill_Set_Group_2_{card}_{standby_skill}', tag=f'Standby_Skill_Desc_Text_{card}_{standby_skill}')        
        add_input_text(tag=f'Standby_Set_Desc_Input_Text_{card}_{standby_skill}', hint='Description', default_value='', width=String_Length.length[0], callback=Text_Resize, parent=f'Standby_Skill_Set_Group_2_{card}_{standby_skill}')
        
    with group(horizontal=True, parent=f'Standby_Skill_{card}', tag=f'Standby_Skill_Set_Group_3_{card}_{standby_skill}'):
        add_text('Cond: ', color=(255, 174, 26), parent=f'Standby_Skill_Set_Group_3_{card}_{standby_skill}', tag=f'Standby_Skill_Cond_Text_{card}_{standby_skill}')
        add_input_text(tag=f'Standby_Set_Cond_Input_Text_{card}_{standby_skill}', hint='Condition', default_value='', width=String_Length.length[0], callback=Text_Resize, parent=f'Standby_Skill_Set_Group_3_{card}_{standby_skill}')
        
    add_separator(tag=f'Standby_Skill_Set_Separator_{card}_{standby_skill}', parent=f'Standby_Skill_{card}')
    add_text('Standby Skill', color=(255,50,50), parent=f'Standby_Skill_{card}', tag=f'Standby_Skill_Text_{card}_{standby_skill}')
    
    Widget_Aliases.tags_to_delete.append(f'Standby_Skill_Set_Text_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Skill_Set_Group_1_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Skill_Name_Text_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Set_Name_Input_Text_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Skill_Set_Group_2_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Skill_Desc_Text_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Set_Desc_Input_Text_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Skill_Set_Group_3_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Skill_Cond_Text_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Set_Cond_Input_Text_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Skill_Set_Separator_{card}_{standby_skill}')
    Widget_Aliases.tags_to_delete.append(f'Standby_Skill_Text_{card}_{standby_skill}')

#####################################################################################################################################################################################
    
def Standby_Skill_Query():
    config = Config_Read()
    
    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
    cur = con.cursor()
    
    for card in range(len(Card_Checks.card_ids)):
        if len(Card_Checks.standby_skill_cards) > 0 and Card_Checks.standby_skill_cards[card]:
            
            for standby_skills in range(len(Card_Checks.standby_skill_ids[card])):
                cur.execute('SELECT exec_limit,compiled_causality_conditions,special_view_id,costume_special_view_id,bgm_id FROM standby_skill_sets WHERE id = ' +  str(Card_Checks.standby_skill_ids[card][standby_skills]))
                standby_skill_set_fetch = cur.fetchall()
                # print(standby_skill_set_fetch)

                cur.execute('SELECT target_type,target_type_values,sub_target_type_set_id,turn,efficacy_type,calc_option,efficacy_values,thumb_effect_id,effect_se_id FROM standby_skills WHERE standby_skill_set_id = ' +  str(Card_Checks.standby_skill_ids[card][standby_skills]))
                standby_skill_fetch = cur.fetchall()

                print(standby_skill_fetch)
                Standby_Skill.rows = len(standby_skill_fetch)
                Standby_Skill_Widgets(card=card, standby_skill=standby_skills)

                ttt = Table_Inputs(table_name=f'Standby_Skill_Set_Table_{card}_{standby_skills}', row_name=f'Standby_Skill_Set_Table_Row_{card}_{standby_skills}', table_parent=f'Standby_Skill_{card}', use_child_window=False, 
                            class_name=Standby_Skill_Set, table_width=500, table_height=49, row_width=85, freeze_rows=1, table_policy=mvTable_SizingStretchSame, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=card)
                # print(ttt)

                Table_Inputs(table_name=f'Standby_Skill_Table_{card}_{standby_skills}', row_name=f'Standby_Skill_Table_Row_{card}_{standby_skills}', table_parent=f'Standby_Skill_{card}', use_child_window=False, 
                            class_name=Standby_Skill, table_width=825, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=card)

                set_item_height(f'Standby_Skill_Table_{card}_{standby_skills}', (24 * len(standby_skill_fetch)) + 23)

                # The "i + 1" is to skip the "Name" as I'm grabbing it from the Wiki JSON
                for i in range(len(standby_skill_set_fetch)):
                    for value in range(len(Standby_Skill_Set.row_names)):
                        set_value(Standby_Skill_Set.row_names[value] + '_Card_' + str(card) + '_Row_' + str(standby_skills) + str(i), standby_skill_set_fetch[standby_skills][value])
                set_value(f'Standby_Set_Name_Input_Text_{card}_{standby_skills}', Card_Checks.standby_skill_names[card][standby_skills])
                set_value(f'Standby_Set_Desc_Input_Text_{card}_{standby_skills}', Card_Checks.standby_skill_desc[card][standby_skills].replace('\n', ''))
                set_value(f'Standby_Set_Cond_Input_Text_{card}_{standby_skills}', Card_Checks.standby_skill_cond[card][standby_skills].replace('\n', ''))
                Text_Resize(f'Standby_Set_Name_Input_Text_{card}_{standby_skills}')
                Text_Resize(f'Standby_Set_Desc_Input_Text_{card}_{standby_skills}')
                Text_Resize(f'Standby_Set_Cond_Input_Text_{card}_{standby_skills}')


                for i in range(len(standby_skill_fetch)):
                    for z in range(len(Standby_Skill.row_names)):
                        if standby_skill_fetch[i][z] is None:
                            set_value(Standby_Skill.row_names[z] + '_Card_' + str(card) + '_Row_' + str(standby_skills) + str(i), 'NULL')
                            # Text_Resize(Standby_Skill.row_names[z + 1] + str(i))
                        ### row_names[6] is efficacy values
                        elif Standby_Skill.row_names[z] == Standby_Skill.row_names[6]:
                            
                            if get_value(Standby_Skill.row_names[4] + '_Card_' + str(card) + '_Row_' + str(standby_skills) + str(i)) == '103':
                                efficacy_values = ast.literal_eval(standby_skill_fetch[i][z])
                                efficacy_values[0] = int(str(efficacy_values[0]).replace(str(efficacy_values[0])[1], '3'))
                                efficacy_values[2] = int(efficacy_values[0])
                                set_value(Standby_Skill.row_names[z] + '_Card_' + str(card) + '_Row_' + str(standby_skills) + str(i), efficacy_values)
                                print(efficacy_values)
                            else:
                                set_value(Standby_Skill.row_names[z] + '_Card_' + str(card) + '_Row_' + str(standby_skills) + str(i), standby_skill_fetch[i][z])
                        
                        else:
                            set_value(Standby_Skill.row_names[z] + '_Card_' + str(card) + '_Row_' + str(standby_skills) + str(i), standby_skill_fetch[i][z])
                            # Text_Resize(Standby_Skill.row_names[z + 1] + str(i))
            configure_item(f'Standby_Skill_{card}', show=True)

#####################################################################################################################################################################################
#####################################################################################################################################################################################
#####################################################################################################################################################################################    
    


#####################################################################################################################################################################################
#####################################################################################################################################################################################    
#####################################################################################################################################################################################        
    
def Finish_Skill_Set_Widgets(*, z=int, finish_skills=int):
    # First attempt at making a decent function I can reuse, kind of aids still XD

    Delete_Items(f'Finish_Skill_Set_Text_{z}_{finish_skills}')
    add_text('Finish Skill Set', color=(255,50,50), parent=f'Finish_Skill_{z}', tag=f'Finish_Skill_Set_Text_{z}_{finish_skills}')
    
    
    Delete_Items(f'Finish_Skill_Set_Group_{z}_{finish_skills}')
    with group(horizontal=True, parent=f'Finish_Skill_{z}', tag=f'Finish_Skill_Set_Group_{z}_{finish_skills}'):
        
        Delete_Items(f'Finish_Skill_Set_Name_{z}_{finish_skills}')
        Delete_Items(f'Finish_Set_Name_{z}_{finish_skills}')
        
        add_text('Name:', color=(255, 174, 26), tag=f'Finish_Skill_Set_Name_{z}_{finish_skills}', parent=f'Finish_Skill_Set_Group_{z}_{finish_skills}')
        add_input_text(default_value='', hint='Name', tag=f'Finish_Set_Name_{z}_{finish_skills}', parent=f'Finish_Skill_Set_Group_{z}_{finish_skills}')
            
    Delete_Items(f'Finish_Skill_Desc_Group_{z}_{finish_skills}')
    with group(horizontal=True, parent=f'Finish_Skill_{z}', tag=f'Finish_Skill_Desc_Group_{z}_{finish_skills}'):       
        
        Delete_Items(f'Finish_Skill_Set_Desc_{z}_{finish_skills}')
        Delete_Items(f'Finish_Set_Desc_{z}_{finish_skills}')
        
        add_text('Desc: ', color=(255, 174, 26), tag=f'Finish_Skill_Set_Desc_{z}_{finish_skills}', parent=f'Finish_Skill_Desc_Group_{z}_{finish_skills}')        
        add_input_text(tag=f'Finish_Set_Desc_{z}_{finish_skills}', hint='Description', default_value='', width=String_Length.length[0], callback=Text_Resize, parent=f'Finish_Skill_Desc_Group_{z}_{finish_skills}')
    
    Delete_Items(f'Finish_Skill_Cond_Group_{z}_{finish_skills}')
    with group(horizontal=True, parent=f'Finish_Skill_{z}', tag=f'Finish_Skill_Cond_Group_{z}_{finish_skills}'):
        Delete_Items(f'Finish_Skill_Set_Cond_{z}_{finish_skills}')
        Delete_Items(f'Finish_Set_Cond_{z}_{finish_skills}')
        add_text('Cond: ', color=(255, 174, 26), tag=f'Finish_Skill_Set_Cond_{z}_{finish_skills}', parent=f'Finish_Skill_Cond_Group_{z}_{finish_skills}')
        add_input_text(tag=f'Finish_Set_Cond_{z}_{finish_skills}', hint='Condition', default_value='', width=String_Length.length[0], callback=Text_Resize, parent=f'Finish_Skill_Cond_Group_{z}_{finish_skills}')

#####################################################################################################################################################################################

def Finish_Skill_Query():
    config = Config_Read()
    
    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
    cur = con.cursor()
    
    ### Number of cards returned from Dokkan Wiki
    for cards in range(len(Card_Checks.card_ids)):
        
        ### Dictionary in download.py that set dictionary values of True or False based on a unit having a finish skill. 
        if len(Card_Checks.finish_skill_cards) > 0 and Card_Checks.finish_skill_cards[cards]:
            print(Card_Checks.finish_skill_cards)
            
            
            for finish_skills in range(len(Card_Checks.finish_skill_ids[cards])):
                # print(finish_skills)
                # print(Card_Checks.finish_skill_names)
                cur.execute('SELECT dialog_order,dialog_images,dialog_label,exec_timing_type,exec_limit,compiled_causality_conditions,finish_special_id,special_view_id,costume_special_view_id,bgm_id FROM finish_skill_sets WHERE id = ' +  str(Card_Checks.finish_skill_ids[cards][finish_skills]))
                finish_skill_set = cur.fetchall()
    
                cur.execute('SELECT target_type,target_type_values,sub_target_type_set_id,turn,efficacy_type,calc_option,efficacy_values,thumb_effect_id,effect_se_id FROM finish_skills WHERE finish_skill_set_id = ' +  str(Card_Checks.finish_skill_ids[cards][finish_skills]))
                finish_skill = cur.fetchall()
    
                Finish_Skill.rows = len(finish_skill)
    
                Finish_Skill_Set_Widgets(cards, finish_skills)
    
                # add_text('Finish Skill Set', tag=f'Finish_Skill_Set_Text_{key}', color=(255,50,50), parent='Finish_Skill_1')
                # Widget_Aliases.tags_to_delete.append(f'Finish_Skill_Set_Text_{key}')
                
                # tt = Table_Inputs(table_name=f'Finish_Skill_Set_Tablee_{cards}_{finish_skills}', row_name=f'Finish_Skill_Set_Tablee_Row_{cards}_{finish_skills}', table_parent=f'Finish_Skill_{cards}', use_child_window=False, 
                            # class_name=Finish_Skill_Set_Test, table_width=838, table_height=47, row_width=80, freeze_rows=1, loop_number=finish_skills, used_in_loop=True, table_policy=mvTable_SizingFixedFit,
                            # transformation=True, transformation_card_num=cards)
                # 
                ### Finish_Set_View_ID_Card_1_Row_10  Row_1 would be the finish skill number, then the 0 after that is the row number.
                ttt = Table_Inputs(table_name=f'Finish_Skill_Set_Table_{cards}_{finish_skills}', row_name=f'Finish_Skill_Set_Table_Row_{cards}_{finish_skills}', table_parent=f'Finish_Skill_{cards}', use_child_window=False, 
                            class_name=Finish_Skill_Set, table_width=927, table_height=47, row_width=80, freeze_rows=1, loop_number=finish_skills, used_in_loop=True, table_policy=mvTable_SizingFixedFit,
                            transformation=True, transformation_card_num=cards)

                # print(ttt)

                add_text('Finish Skill', tag=f'Finish_Skill_Skill_Text_{cards}_{finish_skills}', color=(255,50,50), parent=f'Finish_Skill_{cards}')
                Widget_Aliases.tags_to_delete.append(f'Finish_Skill_Skill_Text_{cards}_{finish_skills}')
                
                ### Same logic from Finish Skill Set Table applies to these aliases.
                sss = Table_Inputs(table_name=f'Finish_Skill_Table_{cards}_{finish_skills}', row_name=f'Finish_Skill_Table_Row_{cards}_{finish_skills}', table_parent=f'Finish_Skill_{cards}', use_child_window=False, 
                            class_name=Finish_Skill, table_width=836, row_width=82, table_height=114, freeze_rows=1, loop_number=finish_skills, used_in_loop=True, transformation=True, transformation_card_num=cards)
                # print(sss)
    
                Finish_Skill.last_rows = (len(finish_skill))
                
    
                # The "i + 1" is to skip the "Name" as I'm grabbing it from the Wiki JSON
                for i in range(len(finish_skill_set)):
                    for value in range(len(Finish_Skill_Set.row_names)):
                        # print(Finish_Skill_Set.row_names[value] + '_Card_' + str(cards) + '_Row_' + str(finish_skills) + str(i))
                        set_value(Finish_Skill_Set.row_names[value] + '_Card_' + str(cards) + '_Row_' + str(finish_skills) + str(i), finish_skill_set[0][value])
                        
                set_value(Finish_Skill_Set.row_names[6] + '_Card_' + str(cards) + '_Row_' + str(finish_skills) + '0', int(get_value(f'id_Card_{cards}_Row_0')) + finish_skills)
                # print(Card_Checks.finish_skill_names)
                set_value(f'Finish_Set_Name_{cards}_{finish_skills}', Card_Checks.finish_skill_names[0][finish_skills])
                set_value(f'Finish_Set_Desc_{cards}_{finish_skills}', Card_Checks.finish_skill_desc[0][finish_skills].replace('\n', ''))
                set_value(f'Finish_Set_Cond_{cards}_{finish_skills}', Card_Checks.finish_skill_cond[0][finish_skills].replace('\n', ''))
                Text_Resize(f'Finish_Set_Name_{cards}_{finish_skills}')
                Text_Resize(f'Finish_Set_Desc_{cards}_{finish_skills}')
                Text_Resize(f'Finish_Set_Cond_{cards}_{finish_skills}')
    
                for i in range(len(finish_skill)):
                    for z in range(len(Finish_Skill.row_names)):
                        if finish_skill[i][z] is None:
                            set_value(Finish_Skill.row_names[z] + '_Card_' + str(cards) + '_Row_' + str(finish_skills) + str(i), 'NULL')
                            # Text_Resize(Standby_Skill.row_names[z + 1] + str(i))
                        else:
                            set_value(Finish_Skill.row_names[z] + '_Card_' + str(cards) + '_Row_' + str(finish_skills) + str(i), finish_skill[i][z])
                            # Text_Resize(Standby_Skill.row_names[z + 1] + str(i))
                
                Widget_Aliases.tags_to_delete.append(f'Finish_Skill_Separator_{cards}_{finish_skills}')
                add_separator(tag=f'Finish_Skill_Separator_{cards}_{finish_skills}', parent=f'Finish_Skill_{cards}')
                configure_item(f'Finish_Skill_{cards}', show=True)