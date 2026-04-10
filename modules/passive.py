from dearpygui.dearpygui import *
from . configs import Config_Read
# from download import Category_Downloads
from .classes import String_Length, Efficacy_Values, Card_Checks, Widget_Aliases, Passive_Skill, Custom_Unit, Exec_Timing, Calc_Options, Target_Types, Turns
import sqlite3
import requests
import re
from . functions import Table_Inputs, Delete_Items, Table_ID, Row_Checker, Table_Combo_Inputs, Grab_Tag_Numbers, Get_Card_Number, get_last_number, ResizePassiveTableWidth
str_length = String_Length.length


# Temporaily making this a function and not using it to avoid making unnecessary requests every time I restart the program to test.

    
# Example of how to use the combo value to get category name
# print(categories_name[categories_name_list[0]])

def Text_Resize(tag_id):
    text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIAL.ttf')
    set_item_width(tag_id, text_width + 5)
    return text_width

def Passive_Widgets():
    cards = Custom_Unit.card_number + 1
    passivePresetClass = EfficacyPresets()
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
            
    Passive_Skill.rows = 1
    configure_item(f'Passive_Rows_in_Table_{cards}', default_value=f'Rows: {Passive_Skill.rows}')

    sss = Table_Inputs(table_name=f'Passive_Skill_Table_{cards}', row_name=f'Passive_Skill_Table_Row_{cards}', table_parent=f'Card_Input_Tab_{cards}', use_child_window=False, 
             class_name=Passive_Skill, combo=True, 
             combo_tag={Passive_Skill.row_names[1] : Exec_Timing.combo,Passive_Skill.row_names[2] : Efficacy_Values.combo_list, Passive_Skill.row_names[3] : Target_Types.combo, Passive_Skill.row_names[6] : Calc_Options.combo, Passive_Skill.row_names[7] : Turns.combo, Passive_Skill.row_names[8] : ['False', 'True']},
             combo_list=Efficacy_Values.combo_list, combo_column_name=Passive_Skill.column_names[2],
             table_width=1775, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=cards)
    
    set_item_callback(Passive_Skill.row_names[2] + '_Card_0_Row_0', passivePresetClass.passivePresetsCallback)
    for i in range(3):
        set_value(Passive_Skill.row_names[4] + '_Card_0_Row_0', '0')
        set_value(Passive_Skill.row_names[5] + '_Card_0_Row_0', 'NULL')
        set_value(Passive_Skill.row_names[9] + '_Card_0_Row_0', '100')
        set_value(Passive_Skill.row_names[10] + '_Card_0_Row_0', 'NULL')
        set_value(Passive_Skill.row_names[11] + '_Card_0_Row_0', '0')
        set_value(Passive_Skill.row_names[12] + '_Card_0_Row_0', '0')
        set_value(Passive_Skill.row_names[13] + '_Card_0_Row_0', '0')
        set_value(Passive_Skill.row_names[14] + '_Card_0_Row_0', '{}')
        configure_item(Passive_Skill.row_names[11] + '_Card_0_Row_0', show=False)
        configure_item(Passive_Skill.row_names[12] + '_Card_0_Row_0', show=False)
        configure_item(Passive_Skill.row_names[13] + '_Card_0_Row_0', show=False)
    
    
    set_item_height(f'Passive_Skill_Table_{cards}', (24 * Passive_Skill.rows + 23))
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
    # print(max_width)
    set_item_width(f'Passive_Skill_Table_{cards}', max_width + 140)

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

                            if Passive_Skill.query_values[i][z] is '0':
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
        passivePresetClass = EfficacyPresets()
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
                        if Passive_Skill.row_names[i] == Passive_Skill.row_names[1]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Exec_Timing.combo, default_value=previous_row_values[i], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[2]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Efficacy_Values.combo_list, callback=passivePresetClass.passivePresetsCallback,  default_value=previous_row_values[i], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[3]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Target_Types.combo, default_value=previous_row_values[i], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[6]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Calc_Options.combo, default_value=previous_row_values[i], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[7]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Turns.combo, default_value=previous_row_values[i], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[8]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=['False', 'True'], default_value=previous_row_values[i], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[10]:
                                add_input_text(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), hint=Passive_Skill.column_names[i], width=82, default_value=previous_row_values[i], parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                                Text_Resize(Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows))
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[14]:
                        
                                add_input_text(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), hint=Passive_Skill.column_names[i], width=82, default_value='{}', parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        else:
                                add_input_text(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), hint=Passive_Skill.column_names[i], width=82, default_value=previous_row_values[i], parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')

                else:
                        if Passive_Skill.row_names[i] == Passive_Skill.row_names[1]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Exec_Timing.combo, default_value=Exec_Timing.combo[0], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[2]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Efficacy_Values.combo_list, callback=passivePresetClass.passivePresetsCallback, default_value=Efficacy_Values.combo_list[0], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[3]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Target_Types.combo, default_value=Target_Types.combo[0], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[6]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Calc_Options.combo, default_value=Calc_Options.combo[0], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[7]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=[i + 1 for i in range(99)], default_value=Turns.combo[0], width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[8]:
                                add_combo(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=['False', 'True'], default_value='False', width=149, parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[10]:
                                add_input_text(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), hint=Passive_Skill.column_names[i], width=82, default_value='NULL', parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')
                                Text_Resize(Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows))
                        elif Passive_Skill.row_names[i] == Passive_Skill.row_names[14]:
                                add_input_text(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), hint=Passive_Skill.column_names[i], width=82, default_value='{}', parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')

                        else:
                                add_input_text(tag=Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), hint=Passive_Skill.column_names[i], width=82, default_value='', parent=f'Passive_Skill_Table_Row_{Table_Number}{Rows}')   
                                
                table_rows.append(Passive_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows))
        if previous_row_values:
                passivePresetClass.passivePresetsCallback(Passive_Skill.row_names[2] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), previous_row_values[2])
                
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
                del Passive_Skill.table_row_tags[int(Table_Number) + 1][last_list_row - 1]
        else:
                pass
        


class EfficacyPresets:


        def passivePresetsQueryCallback(self, card_num):
                for passive_row in range(Row_Checker(f'Passive_efficacy_type_Card_{card_num}_Row_')):
                        tags = ['eff_value1', 'eff_value2', 'eff_value3']
                        efficacy_type = get_value(f'Passive_efficacy_type_Card_{card_num}_Row_{passive_row}')
                        for tag in tags:
                                if does_alias_exist(f'Passive_{tag}_Card_{card_num}_Row_{passive_row}_tooltip'):
                                        delete_item(f'Passive_{tag}_Card_{card_num}_Row_{passive_row}_tooltip')
                                
                                efficacy_value = get_value(f'Passive_{tag}_Card_{card_num}_Row_{passive_row}')
                                if self.presetData[efficacy_type][tag]['type'] == 'combo':
                                        delete_item(f'Passive_{tag}_Card_{card_num}_Row_{passive_row}')
                                        add_combo(tag=f'Passive_{tag}_Card_{card_num}_Row_{passive_row}', items=self.presetData[efficacy_type][tag]['options'], default_value=self.presetData[efficacy_type][tag]['queryData'][efficacy_value], width=149, parent=f'Passive_Skill_Table_Row_{passive_row}', before='Passive_efficacy_values_Card_' + str(card_num) + '_Row_' + str(passive_row))

                                elif self.presetData[efficacy_type][tag]['show'] is False:
                                        configure_item(f'Passive_{tag}_Card_{card_num}_Row_{passive_row}', show=False)

                                if self.presetData[efficacy_type][tag].get('tooltip'):
                                        with tooltip(parent=f'Passive_{tag}_Card_{card_num}_Row_{passive_row}', tag=f'Passive_{tag}_Card_{card_num}_Row_{passive_row}_tooltip'):
                                                add_text(self.presetData[efficacy_type][tag]['tooltip'])
                ResizePassiveTableWidth(card_num)

                        

        def passivePresetsCallback(self, tag_id, value):
                row = get_last_number(tag_id)
                cardNum = Get_Card_Number(tag_id)

                # Passive_eff_value1_Card_1_Row_2

                # Eff 1
                delete_item(f'Passive_eff_value1_Card_{cardNum}_Row_{row}')
                delete_item(f'Passive_eff_value2_Card_{cardNum}_Row_{row}')
                delete_item(f'Passive_eff_value3_Card_{cardNum}_Row_{row}')
                if does_alias_exist(f'Passive_eff_value1_Card_{cardNum}_Row_{row}_tooltip'):
                        delete_item(f'Passive_eff_value1_Card_{cardNum}_Row_{row}_tooltip')
                if does_alias_exist(f'Passive_eff_value2_Card_{cardNum}_Row_{row}_tooltip'):
                        delete_item(f'Passive_eff_value2_Card_{cardNum}_Row_{row}_tooltip')
                if does_alias_exist(f'Passive_eff_value3_Card_{cardNum}_Row_{row}_tooltip'):
                        delete_item(f'Passive_eff_value3_Card_{cardNum}_Row_{row}_tooltip')
                        
                if self.presetData[value]['eff_value1']['type'] == 'combo':
                        add_combo(tag=f'Passive_eff_value1_Card_{cardNum}_Row_{row}', items=self.presetData[value]['eff_value1']['options'], default_value=self.presetData[value]['eff_value1']['value'], width=149, parent=f'Passive_Skill_Table_Row_{row}', before=f'Passive_efficacy_values_Card_{cardNum}_Row_{row}')
                else:
                        add_input_text(tag=f'Passive_eff_value1_Card_{cardNum}_Row_{row}', default_value=self.presetData[value]['eff_value1']['value'], parent=f'Passive_Skill_Table_Row_{row}', before=f'Passive_efficacy_values_Card_{cardNum}_Row_{row}')
                        configure_item(f'Passive_eff_value1_Card_{cardNum}_Row_{row}', show = self.presetData[value]['eff_value1']['show'])


                if self.presetData[value]['eff_value1'].get('tooltip'):

                        with tooltip(parent=f'Passive_eff_value1_Card_{cardNum}_Row_{row}', tag=f'Passive_eff_value1_Card_{cardNum}_Row_{row}_tooltip'):
                                add_text(self.presetData[value]['eff_value1']['tooltip'])

                # Eff 2
                if self.presetData[value]['eff_value2']['type'] == 'combo':
                        add_combo(tag=f'Passive_eff_value2_Card_{cardNum}_Row_{row}', items=self.presetData[value]['eff_value2']['options'], default_value=self.presetData[value]['eff_value2']['value'], width=149, parent=f'Passive_Skill_Table_Row_{row}', before=f'Passive_efficacy_values_Card_{cardNum}_Row_{row}')
                else:
                        add_input_text(tag=f'Passive_eff_value2_Card_{cardNum}_Row_{row}', default_value=self.presetData[value]['eff_value2']['value'], parent=f'Passive_Skill_Table_Row_{row}', before=f'Passive_efficacy_values_Card_{cardNum}_Row_{row}')
                        configure_item(f'Passive_eff_value2_Card_{cardNum}_Row_{row}', show = self.presetData[value]['eff_value2']['show'])

                if self.presetData[value]['eff_value2'].get('tooltip'):

                        with tooltip(parent=f'Passive_eff_value2_Card_{cardNum}_Row_{row}', tag=f'Passive_eff_value2_Card_{cardNum}_Row_{row}_tooltip'):
                                add_text(self.presetData[value]['eff_value2']['tooltip'])

                # Eff 3
                if self.presetData[value]['eff_value3']['type'] == 'combo':
                        add_combo(tag=f'Passive_eff_value3_Card_{cardNum}_Row_{row}', items=self.presetData[value]['eff_value3']['options'], default_value=self.presetData[value]['eff_value3']['value'], width=149, parent=f'Passive_Skill_Table_Row_{row}', before=f'Passive_efficacy_values_Card_{cardNum}_Row_{row}')
                else:
                        add_input_text(tag=f'Passive_eff_value3_Card_{cardNum}_Row_{row}', default_value=self.presetData[value]['eff_value3']['value'], parent=f'Passive_Skill_Table_Row_{row}', before=f'Passive_efficacy_values_Card_{cardNum}_Row_{row}')
                        configure_item(f'Passive_eff_value3_Card_{cardNum}_Row_{row}', show = self.presetData[value]['eff_value3']['show'])

                if self.presetData[value]['eff_value3'].get('tooltip'):

                        with tooltip(parent=f'Passive_eff_value3_Card_{cardNum}_Row_{row}', tag=f'Passive_eff_value3_Card_{cardNum}_Row_{row}_tooltip'):
                                add_text(self.presetData[value]['eff_value3']['tooltip'])

                # ResizePassiveTableWidth(cardNum)

                return

        def specialPresetsQueryCallback(self, card_num):
                for special_row in range(Row_Checker(f'Specials_efficacy_type_Card_{card_num}_Row_')):
                        tags = ['eff_value1', 'eff_value2', 'eff_value3']
                        efficacy_type = get_value(f'Specials_efficacy_type_Card_{card_num}_Row_{special_row}')
                        for tag in tags:
                                if does_alias_exist(f'Specials_{tag}_Card_{card_num}_Row_{special_row}_tooltip'):
                                        delete_item(f'Specials_{tag}_Card_{card_num}_Row_{special_row}_tooltip')
                                
                                efficacy_value = get_value(f'Specials_{tag}_Card_{card_num}_Row_{special_row}')
                                if self.presetData[efficacy_type][tag]['type'] == 'combo':
                                        delete_item(f'Specials_{tag}_Card_{card_num}_Row_{special_row}')
                                        add_combo(tag=f'Specials_{tag}_Card_{card_num}_Row_{special_row}', items=self.presetData[efficacy_type][tag]['options'], default_value=self.presetData[efficacy_type][tag]['queryData'][efficacy_value], width=149, parent=f'Specials_Skill_Table_Row_{special_row}', before='Specials_efficacy_values_Card_' + str(card_num) + '_Row_' + str(special_row))

                                elif self.presetData[efficacy_type][tag]['show'] is False:
                                        configure_item(f'Specials_{tag}_Card_{card_num}_Row_{special_row}', show=False)

                                if self.presetData[efficacy_type][tag].get('tooltip'):
                                        with tooltip(parent=f'Specials_{tag}_Card_{card_num}_Row_{special_row}', tag=f'Specials_{tag}_Card_{card_num}_Row_{special_row}_tooltip'):
                                                add_text(self.presetData[efficacy_type][tag]['tooltip'])
                # ResizePassiveTableWidth(card_num)

                        

        def specialPresetsCallback(self, tag_id, value):
                row = get_last_number(tag_id)
                cardNum = Get_Card_Number(tag_id)

                # Specials_eff_value1_Card_1_Row_2

                # Eff 1
                delete_item(f'Specials_eff_value1_Card_{cardNum}_Row_{row}')
                delete_item(f'Specials_eff_value2_Card_{cardNum}_Row_{row}')
                delete_item(f'Specials_eff_value3_Card_{cardNum}_Row_{row}')
                if does_alias_exist(f'Specials_eff_value1_Card_{cardNum}_Row_{row}_tooltip'):
                        delete_item(f'Specials_eff_value1_Card_{cardNum}_Row_{row}_tooltip')
                if does_alias_exist(f'Specials_eff_value2_Card_{cardNum}_Row_{row}_tooltip'):
                        delete_item(f'Specials_eff_value2_Card_{cardNum}_Row_{row}_tooltip')
                if does_alias_exist(f'Specials_eff_value3_Card_{cardNum}_Row_{row}_tooltip'):
                        delete_item(f'Specials_eff_value3_Card_{cardNum}_Row_{row}_tooltip')
                        
                if self.presetData[value]['eff_value1']['type'] == 'combo':
                        add_combo(tag=f'Specials_eff_value1_Card_{cardNum}_Row_{row}', items=self.presetData[value]['eff_value1']['options'], default_value=self.presetData[value]['eff_value1']['value'], width=149, parent=f'Specials_Skill_Table_Row_{row}')
                else:
                        add_input_text(tag=f'Specials_eff_value1_Card_{cardNum}_Row_{row}', default_value=self.presetData[value]['eff_value1']['value'], parent=f'Specials_Skill_Table_Row_{row}')
                        configure_item(f'Specials_eff_value1_Card_{cardNum}_Row_{row}', show = self.presetData[value]['eff_value1']['show'])


                if self.presetData[value]['eff_value1'].get('tooltip'):

                        with tooltip(parent=f'Specials_eff_value1_Card_{cardNum}_Row_{row}', tag=f'Specials_eff_value1_Card_{cardNum}_Row_{row}_tooltip'):
                                add_text(self.presetData[value]['eff_value1']['tooltip'])

                # Eff 2
                if self.presetData[value]['eff_value2']['type'] == 'combo':
                        add_combo(tag=f'Specials_eff_value2_Card_{cardNum}_Row_{row}', items=self.presetData[value]['eff_value2']['options'], default_value=self.presetData[value]['eff_value2']['value'], width=149, parent=f'Specials_Skill_Table_Row_{row}')
                else:
                        add_input_text(tag=f'Specials_eff_value2_Card_{cardNum}_Row_{row}', default_value=self.presetData[value]['eff_value2']['value'], parent=f'Specials_Skill_Table_Row_{row}')
                        configure_item(f'Specials_eff_value2_Card_{cardNum}_Row_{row}', show = self.presetData[value]['eff_value2']['show'])

                if self.presetData[value]['eff_value2'].get('tooltip'):

                        with tooltip(parent=f'Specials_eff_value2_Card_{cardNum}_Row_{row}', tag=f'Specials_eff_value2_Card_{cardNum}_Row_{row}_tooltip'):
                                add_text(self.presetData[value]['eff_value2']['tooltip'])

                # Eff 3
                if self.presetData[value]['eff_value3']['type'] == 'combo':
                        add_combo(tag=f'Specials_eff_value3_Card_{cardNum}_Row_{row}', items=self.presetData[value]['eff_value3']['options'], default_value=self.presetData[value]['eff_value3']['value'], width=149, parent=f'Specials_Skill_Table_Row_{row}')
                else:
                        add_input_text(tag=f'Specials_eff_value3_Card_{cardNum}_Row_{row}', default_value=self.presetData[value]['eff_value3']['value'], parent=f'Specials_Skill_Table_Row_{row}')
                        configure_item(f'Specials_eff_value3_Card_{cardNum}_Row_{row}', show = self.presetData[value]['eff_value3']['show'])

                if self.presetData[value]['eff_value3'].get('tooltip'):

                        with tooltip(parent=f'Specials_eff_value3_Card_{cardNum}_Row_{row}', tag=f'Specials_eff_value3_Card_{cardNum}_Row_{row}_tooltip'):
                                add_text(self.presetData[value]['eff_value3']['tooltip'])

                return



        def __init__(self):

                self.elementData = {
                        'ElementNames' : ['AGL', 'TEQ', 'INT', 'STR', 'PHY'],
                        'ElementIDs' : {'AGL' : '0', 'TEQ' : '1', 'INT' : '2', 'STR' : '3', 'PHY' : '4', 'Rainbow' : '5'},
                        'ElementQueryConversion' : {'0' : 'AGL', '1' : 'TEQ', '2' : 'INT', '3' : 'STR', '4' : 'PHY', '5' :'Rainbow'},
                        'BitsetNames' : ['AGL', 'TEQ', 'INT', 'STR', 'PHY', 'Rainbow', 'Any'],
                        'BitsetIDs' : {'AGL' : '1', 'TEQ' : '2', 'INT' : '4', 'STR' : '8', 'PHY' : '16', 'Rainbow' : '32', 'Any' : '63'},
                        'BitsetQueryConversion' : {'1' : 'AGL', '2' : 'TEQ', '4' : 'INT', '8' : 'STR', '16' : 'PHY', '32' : 'Rainbow', '63' : 'Any'},
                        'BitsetNames' : [
                                                "AGL",
                                                "AGL, INT",
                                                "AGL, INT, PHY",
                                                "AGL, INT, PHY, Rainbow",
                                                "AGL, INT, PHY, Rainbow, STR",
                                                "Any",
                                                "AGL, INT, PHY, Rainbow, TEQ",
                                                "AGL, INT, PHY, STR",
                                                "All Except Rainbow",
                                                "AGL, INT, PHY, TEQ",
                                                "AGL, INT, Rainbow",
                                                "AGL, INT, Rainbow, STR",
                                                "AGL, INT, Rainbow, STR, TEQ",
                                                "AGL, INT, Rainbow, TEQ",
                                                "AGL, INT, STR",
                                                "AGL, INT, STR, TEQ",
                                                "AGL, INT, TEQ",
                                                "AGL, PHY",
                                                "AGL, PHY, Rainbow",
                                                "AGL, PHY, Rainbow, STR",
                                                "AGL, PHY, Rainbow, STR, TEQ",
                                                "AGL, PHY, Rainbow, TEQ",
                                                "AGL, PHY, STR",
                                                "AGL, PHY, STR, TEQ",
                                                "AGL, PHY, TEQ",
                                                "AGL, Rainbow",
                                                "AGL, Rainbow, STR",
                                                "AGL, Rainbow, STR, TEQ",
                                                "AGL, Rainbow, TEQ",
                                                "AGL, STR",
                                                "AGL, STR, TEQ",
                                                "AGL, TEQ",
                                                "INT",
                                                "INT, PHY",
                                                "INT, PHY, Rainbow",
                                                "INT, PHY, Rainbow, STR",
                                                "INT, PHY, Rainbow, STR, TEQ",
                                                "INT, PHY, Rainbow, TEQ",
                                                "INT, PHY, STR",
                                                "INT, PHY, STR, TEQ",
                                                "INT, PHY, TEQ",
                                                "INT, Rainbow",
                                                "INT, Rainbow, STR",
                                                "INT, Rainbow, STR, TEQ",
                                                "INT, Rainbow, TEQ",
                                                "INT, STR",
                                                "INT, STR, TEQ",
                                                "INT, TEQ",
                                                "PHY",
                                                "PHY, Rainbow",
                                                "PHY, Rainbow, STR",
                                                "PHY, Rainbow, STR, TEQ",
                                                "PHY, Rainbow, TEQ",
                                                "PHY, STR",
                                                "PHY, STR, TEQ",
                                                "PHY, TEQ",
                                                "Rainbow",
                                                "Rainbow, STR",
                                                "Rainbow, STR, TEQ",
                                                "Rainbow, TEQ",
                                                "STR",
                                                "STR, TEQ",
                                                "TEQ",
                                                ],
                        'BitSetCombinations' : {
                                                "AGL": 1,
                                                "AGL, INT": 5,
                                                "AGL, INT, PHY": 21,
                                                "AGL, INT, PHY, Rainbow": 53,
                                                "AGL, INT, PHY, Rainbow, STR": 61,
                                                "Any": 63,
                                                "AGL, INT, PHY, Rainbow, TEQ": 39,
                                                "AGL, INT, PHY, STR": 29,
                                                "All Except Rainbow": 31,
                                                "AGL, INT, PHY, TEQ": 23,
                                                "AGL, INT, Rainbow": 37,
                                                "AGL, INT, Rainbow, STR": 45,
                                                "AGL, INT, Rainbow, STR, TEQ": 47,
                                                "AGL, INT, Rainbow, TEQ": 39,
                                                "AGL, INT, STR": 13,
                                                "AGL, INT, STR, TEQ": 15,
                                                "AGL, INT, TEQ": 7,
                                                "AGL, PHY": 17,
                                                "AGL, PHY, Rainbow": 49,
                                                "AGL, PHY, Rainbow, STR": 57,
                                                "AGL, PHY, Rainbow, STR, TEQ": 59,
                                                "AGL, PHY, Rainbow, TEQ": 51,
                                                "AGL, PHY, STR": 25,
                                                "AGL, PHY, STR, TEQ": 27,
                                                "AGL, PHY, TEQ": 19,
                                                "AGL, Rainbow": 33,
                                                "AGL, Rainbow, STR": 41,
                                                "AGL, Rainbow, STR, TEQ": 43,
                                                "AGL, Rainbow, TEQ": 35,
                                                "AGL, STR": 9,
                                                "AGL, STR, TEQ": 11,
                                                "AGL, TEQ": 3,
                                                "INT": 4,
                                                "INT, PHY": 20,
                                                "INT, PHY, Rainbow": 52,
                                                "INT, PHY, Rainbow, STR": 60,
                                                "INT, PHY, Rainbow, STR, TEQ": 62,
                                                "INT, PHY, Rainbow, TEQ": 54,
                                                "INT, PHY, STR": 28,
                                                "INT, PHY, STR, TEQ": 30,
                                                "INT, PHY, TEQ": 22,
                                                "INT, Rainbow": 36,
                                                "INT, Rainbow, STR": 44,
                                                "INT, Rainbow, STR, TEQ": 46,
                                                "INT, Rainbow, TEQ": 38,
                                                "INT, STR": 12,
                                                "INT, STR, TEQ": 14,
                                                "INT, TEQ": 6,
                                                "PHY": 16,
                                                "PHY, Rainbow": 48,
                                                "PHY, Rainbow, STR": 56,
                                                "PHY, Rainbow, STR, TEQ": 58,
                                                "PHY, Rainbow, TEQ": 50,
                                                "PHY, STR": 24,
                                                "PHY, STR, TEQ": 26,
                                                "PHY, TEQ": 18,
                                                "Rainbow": 32,
                                                "Rainbow, STR": 40,
                                                "Rainbow, STR, TEQ": 42,
                                                "Rainbow, TEQ": 34,
                                                "STR": 8,
                                                "STR, TEQ": 10,
                                                "TEQ": 2,
                                        },
                        'BitsetQueryConversion' : {'1' : 'AGL',
                                                    '5' : 'AGL, INT',
                                                    '21' : 'AGL, INT, PHY',
                                                    '53' : 'AGL, INT, PHY, Rainbow',
                                                    '61' : 'AGL, INT, PHY, Rainbow, STR',
                                                    '63' : 'Any',
                                                    '39' : 'AGL, INT, PHY, Rainbow, TEQ',
                                                    '29' : 'AGL, INT, PHY, STR',
                                                    '31' : 'All Except Rainbow',
                                                    '23' : 'AGL, INT, PHY, TEQ',
                                                    '37' : 'AGL, INT, Rainbow',
                                                    '45' : 'AGL, INT, Rainbow, STR',
                                                    '47' : 'AGL, INT, Rainbow, STR, TEQ',
                                                    '39' : 'AGL, INT, Rainbow, TEQ',
                                                    '13' : 'AGL, INT, STR',
                                                    '15' : 'AGL, INT, STR, TEQ',
                                                    '7' : 'AGL, INT, TEQ',
                                                    '17' : 'AGL, PHY',
                                                    '49' : 'AGL, PHY, Rainbow',
                                                    '57' : 'AGL, PHY, Rainbow, STR',
                                                    '59' : 'AGL, PHY, Rainbow, STR, TEQ',
                                                    '51' : 'AGL, PHY, Rainbow, TEQ',
                                                    '25' : 'AGL, PHY, STR',
                                                    '27' : 'AGL, PHY, STR, TEQ',
                                                    '19' : 'AGL, PHY, TEQ',
                                                    '33' : 'AGL, Rainbow',
                                                    '41' : 'AGL, Rainbow, STR',
                                                    '43' : 'AGL, Rainbow, STR, TEQ',
                                                    '35' : 'AGL, Rainbow, TEQ',
                                                    '9' : 'AGL, STR',
                                                    '11' : 'AGL, STR, TEQ',
                                                    '3' : 'AGL, TEQ',
                                                    '4' : 'INT',
                                                    '20' : 'INT, PHY',
                                                    '52' : 'INT, PHY, Rainbow',
                                                    '60' : 'INT, PHY, Rainbow, STR',
                                                    '62' : 'INT, PHY, Rainbow, STR, TEQ',
                                                    '54' : 'INT, PHY, Rainbow, TEQ',
                                                    '28' : 'INT, PHY, STR',
                                                    '30' : 'INT, PHY, STR, TEQ',
                                                    '22' : 'INT, PHY, TEQ',
                                                    '36' : 'INT, Rainbow',
                                                    '44' : 'INT, Rainbow, STR',
                                                    '46' : 'INT, Rainbow, STR, TEQ',
                                                    '38' : 'INT, Rainbow, TEQ',
                                                    '12' : 'INT, STR',
                                                    '14' : 'INT, STR, TEQ',
                                                    '6' : 'INT, TEQ',
                                                    '16' : 'PHY',
                                                    '48' : 'PHY, Rainbow',
                                                    '56' : 'PHY, Rainbow, STR',
                                                    '58' : 'PHY, Rainbow, STR, TEQ',
                                                    '50' : 'PHY, Rainbow, TEQ',
                                                    '24' : 'PHY, STR',
                                                    '26' : 'PHY, STR, TEQ',
                                                    '18' : 'PHY, TEQ',
                                                    '32' : 'Rainbow',
                                                    '40' : 'Rainbow, STR',
                                                    '42' : 'Rainbow, STR, TEQ',
                                                    '34' : 'Rainbow, TEQ',
                                                    '8' : 'STR',
                                                    '10' : 'STR, TEQ',
                                                    '2' : 'TEQ'},

                }
                self.presetData = {
                '0 - IDK' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0' , 'show' : False}},
                '1 - ATK' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0' , 'show' : False}},
                '2 - DEF' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'DEF Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}}, 
                '3 - ATK & DEF' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'DEF Value'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '4 - Heal HP' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Heal Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '5 - Ki' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Ki Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '8 - Ghost Usher' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '9 - Stun' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '11 - Attack Order' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '12 - Pain Attack' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '13 - DR' : {
                        'eff_value1' : {'type' : 'input', 'value' : '70', 'show' : True, 'tooltip' : 'DR Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '16 - Element Type ATK' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type to increase ATK'}, # Element type not bitpatterns
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK Value'}, # ATK value
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '17 - Element Type DEF' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type to increase DEF'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'DEF Value'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '18 - Element Type ATK & DEF' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type to increase ATK & DEF'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK Value'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'DEF Value'}},
                '19 - Element Type HP' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type to increase ATK'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'HP Value'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '20 - Element Type Ki' : {
                        'eff_value1' : {'type' : 'combo', 'value' : '0', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type to increase Ki'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Ki Value'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '21 - Recovery' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '22 - Condition Heal' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '24 - Guard Break' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '26 - Absorb Special Energy' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '27 - Resist Special Damage' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Reduction Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '28 - Absorb Deal Damage' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Recovery Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '34 - Dokkan Gauge Bonus' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '35 - Heal Bonus' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '36 - Special Bonus' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '37 - Energy Bonus' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '38 - Link Skill Bonus' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Link Effect Value Boost'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '39 - Element Type Energy Bonus' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '40 - Element Type Linkage Bonus' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '43 - HP ATK' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '44 - Element Type HP ATK' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '46 - Passive Probability Bonus' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '47 - Disable enemy\'s guard' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '48 - Seal' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '50 - Immune to Neg. Effects' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '51 - Energy Ball Color' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Ki Sphere Element to Change'},
                        'eff_value2' : {'type' : 'combo', 'value' : 'TEQ', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Ki Sphere Element to Change to'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '52 - Survive K.O Attacks' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '53 - Ignore Enemy Defense' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '54 - Invalid Combination Attack Bonus' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '55 - Target DEF & Self ATK' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '56 - Target DEF & Self DEF' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '57 - Target DEF & Self Ki' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '58 - Energy Ball Heal' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '59 - Energy Ball Proportional ATK' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '60 - Energy Ball Proportional DEF' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'DEF Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '61 - Energy Ball Proportional ATK & DEF' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'DEF Value'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '63 - Special Energy Cost' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '64 - Element Type Energy Ball Proportional ATK' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type Ki Sphere to increase ATK'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK Value'},
                        'eff_value3' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type Ki Sphere to increase ATK'}},
                '65 - Element Type Energy Ball Proportional DEF' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type Ki Sphere to increase DEF'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'DEF Value'},
                        'eff_value3' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type Ki Sphere to increase DEF'}},
                '66 - Element Type Energy Ball Proportional ATK DEF' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type Ki Sphere to increase ATK & DEF'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK & DEF Value'},
                        'eff_value3' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type Ki Sphere to increase ATK & DEF'}},
                '67 - Energy Ball Color Bitpattern' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'Any', 'show' : True, 'options' : self.elementData['BitsetNames'], 'exportData' : self.elementData['BitSetCombinations'], 'queryData' : self.elementData['BitsetQueryConversion'], 'tooltip' : 'Element Type Ki Sphere(s) to Change'},
                        'eff_value2' : {'type' : 'combo', 'value' : 'Any', 'show' : True, 'options' : self.elementData['BitsetNames'], 'exportData' : self.elementData['BitSetCombinations'], 'queryData' : self.elementData['BitsetQueryConversion'], 'tooltip' : 'Element Type Ki Sphere(s) to Change to'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '68 - Energy Ball Proportional Bitpattern' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'Any', 'show' : True, 'options' : self.elementData['BitsetNames'], 'exportData' : self.elementData['BitSetCombinations'], 'queryData' : self.elementData['BitsetQueryConversion'], 'tooltip' : 'Element Type Ki Sphere(s) to Benefit from Eff_Value 2'},
                        'eff_value2' : {'type' : 'combo', 'value' : 'ATK', 'show' : True, 'options' : ['ATK', 'DEF', 'HP', 'CRIT', 'DODGE', 'DR'], 'exportData' : {'ATK' : '1', 'DEF' : '3', 'HP' : '2', 'CRIT' : '4', 'DODGE' : '5', 'DR' : '6'}, 'queryData' : {'1' : 'ATK', '3' : 'DEF', '2' : 'HP', '4' : 'CRIT', '5' : 'DODGE', '6' : 'DR'}},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Value to increase or decrease by'}},
                '69 - Energy Ball Color Specify Random' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'AGL', 'show' : True, 'options' : self.elementData['ElementNames'], 'exportData' : self.elementData['ElementIDs'], 'queryData' : self.elementData['ElementQueryConversion'], 'tooltip' : 'Element Type Ki Sphere to Change Entire Field to'},
                        'eff_value2' : {'type' : 'input', 'value' : '-1', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '-1', 'show' : False}},
                '70 - Energy Ball Color Specify Random Without Obstacles' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '71 - HP Range ATK' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK Boost at Min HP'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK Boost at Max HP'},
                        'eff_value3' : {'type' : 'input', 'value' : '1100', 'show' : False}},
                '72 - HP Range DEF' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'DEF Boost at Min HP'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'DEF Boost at Max HP'},
                        'eff_value3' : {'type' : 'input', 'value' : '1100', 'show' : False}},
                '73 - HP Range ATK DEF' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK & DEF Boost at Min HP'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'ATK & DEF Boost at Max HP'},
                        'eff_value3' : {'type' : 'input', 'value' : '1100', 'show' : False}},
                '74 - HP Range Ball Heal' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '75 - Disable Swap' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '76 - ATK Super Effective' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '77 - Reset Ball Color' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '78 - Guard' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '79 - Rage Transformation' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Transformation Card ID'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Battle Param Set 1'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Battle Param Set 2'}},
                '81 - Additional Attack' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Chance for Second Attack'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Chance of Attack becoming a Super Attack'}},
                '82 - Element Type HP ATK DEF' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True}, # Finish Later
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '83 - Element Type Energy Bitpattern' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True}, # Finish Later
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '84 - Sacrifice HP' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '85 - Step Extra Attack' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '86 - Special ATK Rate' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '87 - Element Type Attack Coef' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '88 - Element Type Defense Coef' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '89 - Element Type Attack Defense Coef' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '90 - Critical Attack' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Chance for Critical Attack'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '91 - Dodge' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Chance for Dodge'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '92 - Always Hit' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '93 - Element Type Bitpattern HP' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '94 - Immune to Stun' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '96 - Ki Sphere Additional Point' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'Any', 'show' : True, 'options' : self.elementData['BitsetNames'], 'exportData' : self.elementData['BitSetCombinations'], 'queryData' : self.elementData['BitsetQueryConversion'],},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Ki Value'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '97 - Super Nullification & Heal' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'HP Recovery Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '1', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Nullification Lua ID\nEx. as0015.lua = 15'}},
                '98 - Incremental Param' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Increment Amount'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Increment Value Cap'},
                        'eff_value3' : {'type' : 'combo', 'value' : '0', 'show' : True, 'options' : ['ATK', 'DEF', 'KI', 'CRIT', 'DODGE', 'DR'], 'exportData' : {'ATK' : '0', 'DEF' : '1', 'KI' : '5', 'CRIT' : '2', 'DODGE' : '3', 'DR' : '4'}, 'queryData' : {'0' : 'ATK', '1' : 'DEF', '5' : 'KI', '2' : 'CRIT', '3' : 'DODGE', '4' : 'DR'}}},
                '99 - Immune to Status Down' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '100 - Invalidate Astute' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '101 - Forsee Super Attacks' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '102 - Metamorphic Probability Count Limit' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '103 - Transformation' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Transformation Card ID'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Turn Requirement'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Battle Param Set ID'}},
                # '104 - HP ATK DEF' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '105 - Change Ki Sphere' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'TO DO'}, # Changes the entire field to these Ki Spheres
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'TO DO'}, # Used bitpatterns
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'TO DO'}}, # Not gonna bother with this for now
                # '106 - Potential Heal' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '107 - Delay (Stackable)' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Delay X Turn(s)'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                # '108 - Add Potential Skill' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '109 - Revive' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'HP Recovery Amount'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Effect Pack ID'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'BGM ID'}},
                '110 - Passive Reset' : {
                        'eff_value1' : {'type' : 'combo', 'value' : 'Passive Skill Row', 'show' : True, 'options' : ['Passive Skill Row', 'Finish Skill Row'], 'exportData' : {'Passive Skill Row' : '2', 'Finish Skill Row' : '15'}, 'queryData' : {'2' : 'Passive Skill Row', '15' : 'Finish Skill Row'}},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Skill Row ID'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '111 - Disable Action' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '112 - Immune to Attack Break' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '113 - Threshold Damage' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '114 - Unable to Attack' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '115 - Update Standby Mode' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '1', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '116 - Charge Start' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '117 - End Transformation' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '118 - ATK Rate per Charge Count' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '119 - Nullify Super' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Nullification Lua ID\nEx. as0015.lua = 15\nIf using 120 - Counter Attack, set to 0'}},
                '120 - Counter Attack' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'DR Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Counter Damage Multiplier\nEx. 600'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Counter Lua ID\nEx. c0015.lua = 15'}},
                # '121 - ???' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '122 - Increased Received DMG' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Received DMG Value'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '123 - Target Focus' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                # '124 - ???' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                # '125 - ???' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                # '126 - ???' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                # '127 - ???' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '128 - Dodge Counter' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Counter Damage Multiplier\nEx. 600'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Counter Lua ID\nEx. c0015.lua = 15'}},
                '129 - Invalidate Guaranteed Hits' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                # '130 - ???' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                '131 - Reversible Exchange' : {
                        'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Exchange Card ID'},
                        'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : True, 'tooltip' : 'Voice ID'},
                        'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                # '132 - ???' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                # '133 - ???' : {
                #         'eff_value1' : {'type' : 'input', 'value' : '0', 'show' : True},
                #         'eff_value2' : {'type' : 'input', 'value' : '0', 'show' : False},
                #         'eff_value3' : {'type' : 'input', 'value' : '0', 'show' : False}},
                }


