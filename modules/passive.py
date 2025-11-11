from dearpygui.dearpygui import *
from . configs import Config_Read
# from download import Category_Downloads
from .classes import String_Length, Efficacy_Values, Card_Checks, Widget_Aliases, Passive_Skill, Custom_Unit
import sqlite3
import requests
import re
from . functions import Table_Inputs, Delete_Items, Table_ID, Row_Checker, Table_Combo_Inputs, Grab_Tag_Numbers
str_length = String_Length.length


# Temporaily making this a function and not using it to avoid making unnecessary requests every time I restart the program to test.

    
# Example of how to use the combo value to get category name
# print(categories_name[categories_name_list[0]])

def Text_Resize(tag_id):
    text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIAL.ttf')
    set_item_width(tag_id, text_width + 5)
    return text_width

def Passive_Widgets():
        cards = Custom_Unit.card_number
        config = Config_Read()

        con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
        cur = con.cursor()
        
        Passive_IDs_list = Card_Checks.passive_ids
        
                
        # if not get_value('Custom_Unit'):
                # cur.execute("SELECT passive_skill_id FROM passive_skill_set_relations WHERE passive_skill_set_id = " + str(Passive_IDs_list[cards]))
                # Passive_IDs = cur.fetchall()
# 
                # Passive_IDs = [item[0] for item in Passive_IDs]
# 
                # Passive_Skill.rows = len(Passive_IDs)
        # else:
                # Passive_Skill.rows = 0
                
        
        Delete_Items(f'Passive_Desc_Text_{cards}')    
        Delete_Items(f'Passive_Desc_Text_Input_{cards}')
        Delete_Items(f'Passive_Text_Group_{cards}')
        Delete_Items(f'Passive_Skills_{cards}')
        Delete_Items(f'Passive_Rows_in_Table_{cards}')
        Delete_Items(f'Passive_Add_{cards}')
        Delete_Items(f'Passive_Del_{cards}')
        with group(horizontal=True, tag=f'Passive_Text_Group_{cards}', parent=f'Card_Input_Tab_{cards}'):
        
                add_text('Passive Skills', tag=f'Passive_Skills_{cards}', color=(255,50,50), parent=f'Passive_Text_Group_{cards}')
                add_text(default_value='Rows: 0', tag=f'Passive_Rows_in_Table_{cards}', parent=f'Passive_Text_Group_{cards}')
                add_button(label='Passive Add', callback=Passive_Add, tag=f'Passive_Add_{cards}', parent=f'Passive_Text_Group_{cards}')
                add_button(label='Passive Del', callback=Passive_Del, tag=f'Passive_Del_{cards}', parent=f'Passive_Text_Group_{cards}')
                Widget_Aliases.tags_to_delete.append(f'Passive_Skills_{cards}')
                Widget_Aliases.tags_to_delete.append(f'Passive_Rows_in_Table_{cards}')
                Widget_Aliases.tags_to_delete.append(f'Passive_Add_{cards}')
                Widget_Aliases.tags_to_delete.append(f'Passive_Del_{cards}')

        sss = Table_Inputs(table_name=f'Passive_Skill_Table_{cards}', row_name=f'Passive_Skill_Table_Row_{cards}', table_parent=f'Card_Input_Tab_{cards}', use_child_window=False, 
                        class_name=Passive_Skill, combo=True, combo_tag=Passive_Skill.row_names[2], combo_list=Efficacy_Values.combo_list, combo_column_name=Passive_Skill.column_names[2],
                        table_width=1775, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=cards)
        # print(sss[1])
        ### 5 Rarity, 12 Element, 23,24,25,26,27,28,29 Link Skills, 52 Potential Board
                # Table_Combo_Inputs(table_name=f'Passive_Skill_Table_{cards}', row_name=f'Passive_Skill_Table_Row_{cards}', table_parent=f'Card_Input_Tab_{cards}', class_name=Passive_Skill,
                #                    combo_columns=[5,12,23,24,25,26,27,28,29,52])
        set_item_height(f'Passive_Skill_Table_{cards}', (24 * Passive_Skill.rows + 23))
        

        Delete_Items(f'Passive_Desc_Text_{cards}')
        Delete_Items(f'Passive_Desc_Text_Input_{cards}')
        add_text('Passive Skill Description', color=(255,50,0), parent=f'Card_Input_Tab_{cards}', tag=f'Passive_Desc_Text_{cards}')
        add_input_text(tag=f'Passive_Desc_Text_Input_{cards}', multiline=True, width=500, height=250, parent=f'Card_Input_Tab_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Passive_Desc_Text_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Passive_Desc_Text_Input_{cards}')

def Passive_Skill_Query():
    Passive_Widgets()
    config = Config_Read()

    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
    # con.row_factory = lambda cursor, row: row
    cur = con.cursor()
            
    Passive_IDs_list = Card_Checks.passive_ids
    Passive_names_list = Card_Checks.passive_names
    Passive_desc_list = Card_Checks.passive_descriptions
    
    for cards in range(len(Card_Checks.card_ids)):
            cur.execute("SELECT passive_skill_id FROM passive_skill_set_relations WHERE passive_skill_set_id = " + str(Passive_IDs_list[cards]))
            Passive_IDs = cur.fetchall()

            Passive_IDs = [item[0] for item in Passive_IDs]

            Passive_Skill.rows = len(Passive_IDs)


            # Always clear the list before appending to it. This is to prevent a second query from appending on top of old values
            Passive_Skill.query_values.clear()
            for i in range(len(Passive_IDs)):
                    cur.execute('SELECT exec_timing_type,efficacy_type,target_type,sub_target_type_set_id,passive_skill_effect_id,calc_option,turn,is_once,probability,causality_conditions,eff_value1,eff_value2,eff_value3,efficacy_values FROM passive_skills WHERE id = ' + str(Passive_IDs[i]))
                    Passive_Skills_Info = cur.fetchall()
                    Passive_Skill.query_values.append(Passive_Skills_Info[0])

        #     Delete_Items(f'Passive_Desc_Text_{cards}')    
        #     Delete_Items(f'Passive_Desc_Text_Input_{cards}')
        #     Delete_Items(f'Passive_Text_Group_{cards}')
        #     Delete_Items(f'Passive_Skills_{cards}')
        #     Delete_Items(f'Passive_Rows_in_Table_{cards}')
        #     Delete_Items(f'Passive_Add_{cards}')
        #     Delete_Items(f'Passive_Del_{cards}')
        #     with group(horizontal=True, tag=f'Passive_Text_Group_{cards}', parent=f'Card_Input_Tab_{cards}'):
            
        #             add_text('Passive Skills', tag=f'Passive_Skills_{cards}', color=(255,50,50), parent=f'Passive_Text_Group_{cards}')
        #             add_text(default_value='Rows: 0', tag=f'Passive_Rows_in_Table_{cards}', parent=f'Passive_Text_Group_{cards}')
        #             add_button(label='Passive Add', callback=Passive_Add, tag=f'Passive_Add_{cards}', parent=f'Passive_Text_Group_{cards}')
        #             add_button(label='Passive Del', callback=Passive_Del, tag=f'Passive_Del_{cards}', parent=f'Passive_Text_Group_{cards}')
        #             Widget_Aliases.tags_to_delete.append(f'Passive_Skills_{cards}')
        #             Widget_Aliases.tags_to_delete.append(f'Passive_Rows_in_Table_{cards}')
        #             Widget_Aliases.tags_to_delete.append(f'Passive_Add_{cards}')
        #             Widget_Aliases.tags_to_delete.append(f'Passive_Del_{cards}')

        #     sss = Table_Inputs(table_name=f'Passive_Skill_Table_{cards}', row_name=f'Passive_Skill_Table_Row_{cards}', table_parent=f'Card_Input_Tab_{cards}', use_child_window=False, 
        #              class_name=Passive_Skill, combo=True, combo_tag=Passive_Skill.row_names[2], combo_list=Efficacy_Values.combo_list, combo_column_name=Passive_Skill.column_names[2],
        #              table_width=1775, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=cards)
            

        #     Delete_Items(f'Passive_Desc_Text_{cards}')
        #     Delete_Items(f'Passive_Desc_Text_Input_{cards}')
        #     add_text('Passive Skill Description', color=(255,50,0), parent=f'Card_Input_Tab_{cards}', tag=f'Passive_Desc_Text_{cards}')
        #     add_input_text(tag=f'Passive_Desc_Text_Input_{cards}', multiline=True, width=500, height=250, parent=f'Card_Input_Tab_{cards}')
        #     Widget_Aliases.tags_to_delete.append(f'Passive_Desc_Text_{cards}')
        #     Widget_Aliases.tags_to_delete.append(f'Passive_Desc_Text_Input_{cards}')
            
            set_item_height(f'Passive_Skill_Table_{cards}', (24 * len(Passive_IDs)) + 23)
            set_value(f'Passive_Desc_Text_Input_{cards}', Passive_desc_list[cards])

            for i in range(Passive_Skill.rows):
                    set_value(Passive_Skill.row_names[0] + '_Card_' + str(cards) + '_Row_' + str(i), Passive_names_list[cards])
                    Text_Resize(Passive_Skill.row_names[0] + '_Card_' + str(cards) + '_Row_' + str(i))
                    for z in range(len(Passive_Skill.query_row_names)):
                            # if Passive_Skill.row_names[z] == Passive_Skill.row_names[0]:
                                    # set_value(Passive_Skill.row_names[0] + str(i), get_value('Passive_Name'))

                            if Passive_Skill.query_values[i][z] is None:
                                    set_value(Passive_Skill.query_row_names[z] + '_Card_' + str(cards) + '_Row_' + str(i), 'NULL')
                            else:
                                    # Setting the Eff_Type combo list using the dictionary
                                    if Passive_Skill.query_row_names[z] == Passive_Skill.query_row_names[1]:
                                            # print(eff_dict[Passive_Skill.query_values[i][z]])
                                            set_value(Passive_Skill.query_row_names[z] + '_Card_' + str(cards) + '_Row_' + str(i), Efficacy_Values.eff_dict[Passive_Skill.query_values[i][z]])
                                            # Text_Resize(Passive_Skill.query_row_names[z] + str(i))
                                    elif Passive_Skill.query_row_names[z] == Passive_Skill.query_row_names[9]:
                                            set_value(Passive_Skill.query_row_names[z] + '_Card_' + str(cards) + '_Row_' + str(i), Passive_Skill.query_values[i][z])
                                            Text_Resize(Passive_Skill.query_row_names[z] + '_Card_' + str(cards) + '_Row_' + str(i))
                                    # Every other value in passive  
                                    else:
                                            set_value(Passive_Skill.query_row_names[z] + '_Card_' + str(cards) + '_Row_' + str(i), Passive_Skill.query_values[i][z])

            configure_item(f'Passive_Rows_in_Table_{cards}', default_value=f'Rows: {len(Passive_IDs)}')
            
            widget_widths_list = []
            for row in range(Passive_Skill.rows):
                widget_widths = 0
                for column in range(len(Passive_Skill.row_names)):
                    widget_widths += get_item_width(Passive_Skill.row_names[column] + '_Card_' + str(cards) + '_Row_' + str(row))
                widget_widths_list.append(widget_widths)
    
    
            # Finding the max width out of all widgets
            max_width = 0
            for width in widget_widths_list:
                max_width = width
                if width > max_width:
                    max_width = width
            print(max_width)
            set_item_width(f'Passive_Skill_Table_{cards}', max_width + 140)
            #configure_item(f'Passive_Skill_{Passive_Skill.column_names[0]}', init_width_or_weight=Name_Width)
            # set_value(f'Passive_Desc_Text_Input_{cards}', Passive_desc_list[cards])
            #####################################################################################################################################

        
def Passive_Add(app_data):
        # print(Passive_Skill.table_row_tags)
        # Use app_data to get last digit, which tells which card tab to add the table rows to.
        Table_Number = Table_ID(app_data)
        # print(f'Table Number: {Table_Number}')
        
        # Dynamically check existing rows
        Rows = Row_Checker(Passive_Skill.row_names[0] + '_Card_' + str(Table_Number) + '_Row_')
        
        ### Getting previous row's values
        if get_value(Passive_Skill.row_names[0] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows - 1)):
                passive_tags = [Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows - 1) for i in range(len(Passive_Skill.row_names))]
                previous_row_values = get_values(passive_tags)
        else:
                previous_row_values = []
        
        
        
        # print(str(Rows))
        # print(f'Rows: {Rows}')
        # print(f'Table Row Name: Passive_Skill_Table_Row_{Table_Number}{Rows}')
        # print(f'Passive_Skill_Table_{Table_Number}')
        # print(f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
        add_table_row(tag=f'Passive_Skill_Table_Row_{Table_Number}{Rows}', parent=f'Passive_Skill_Table_{Table_Number}')
        table_rows = []
        for i in range(len(Passive_Skill.row_names)):
                # Passive_Skill.row_names[2] is Efficacy Type
                if get_value(Passive_Skill.row_names[0] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows - 1)):
                        if Passive_Skill.row_names[i] == Passive_Skill.row_names[2]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Efficacy_Values.combo_list, default_value=previous_row_values[i], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        else:
                                add_input_text(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), hint=Passive_Skill.column_names[i], width=82, default_value=previous_row_values[i], parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                else:
                        if Passive_Skill.row_names[i] == Passive_Skill.row_names[2]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Efficacy_Values.combo_list, default_value=Efficacy_Values.combo_list[0], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        else:
                                add_input_text(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), hint=Passive_Skill.column_names[i], width=82, default_value='', parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')   
                                
                table_rows.append(Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows))
                
        configure_item(f'Passive_Rows_in_Table_{Table_Number}', default_value=f'Rows: {Rows + 1}')
        set_item_height(f'Passive_Skill_Table_{Table_Number}', (24 * (Rows + 1) + 23))
                        
        # Check previous row value for a name, set the new row name if it exists
        # print(Passive_Skill.row_names[0] + str(Rows - 1))
        if get_value(Passive_Skill.row_names[0] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows - 1)):
                set_value(Passive_Skill.row_names[0] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), get_value(Passive_Skill.row_names[0] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows - 1)))
                Text_Resize(Passive_Skill.row_names[0] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows))
        
        Passive_Skill.table_row_tags[int(Table_Number)].append(table_rows)
                
def Passive_Del(app_data):
        # Use app_data to get last digit, which tells which card tab to add the table rows to.
        Table_Number = Table_ID(app_data)
        # print(f'Table Number: {Table_Number}')
        
        # Dynamically check existing rows
        Rows = Row_Checker(Passive_Skill.row_names[0] + '_Card_' + str(Table_Number) + '_Row_')
        # print(f'Rows: {Rows}')
        # print(f'Table Row Name: Passive_Skill_Table_Row_{Table_Number}{Rows}')
        if Rows > 1:
                delete_item(f'Passive_Skill_Table_Row_{Table_Number}{Rows - 1}')
                for i in range(len(Passive_Skill.row_names)):
                        # Passive_Skill.row_names[2] is Efficacy Type
                                delete_item(Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows - 1))
                configure_item(f'Passive_Rows_in_Table_{Table_Number}', default_value=f'Rows: {Rows - 1}')
                set_item_height(f'Passive_Skill_Table_{Table_Number}', (24 * (Rows - 1) + 23))
                last_list_row = len(Passive_Skill.table_row_tags[int(Table_Number)])
                del Passive_Skill.table_row_tags[int(Table_Number)][last_list_row - 1]
        else:
                pass
        




