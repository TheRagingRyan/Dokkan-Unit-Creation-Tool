from dearpygui.dearpygui import *
from . classes import Special_Views
from . functions import Table_ID, Row_Checker, Table_Combo_Inputs, Delete_Items


def Special_Views_Add(tag_id):
    card = Table_ID(tag_id)
    
    Rows = Row_Checker(Special_Views.row_names[0] + '_Card_' + str(card) + '_Row_')
    special_category_ids = ['Undefined', 'Ki Blast', 'Unarmed', 'Physical/Melee']
    
    
    if get_value(Special_Views.row_names[2] + '_Card_' + str(card) + '_Row_' + str(Rows - 1)):
            passive_tags = [Special_Views.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows - 1) for i in range(len(Special_Views.row_names))]
            previous_row_values = get_values(passive_tags)
            previous_row_values[0] = str(int(previous_row_values[0]) + 1)
    else:
            previous_row_values = []
    
    add_table_row(tag=f'Special_Views_Table_Row_{card}{Rows}', parent=f'Special_Views_Table_{card}')
    
    for i in range(len(Special_Views.row_names)):
        
            if get_value(Special_Views.row_names[2] + '_Card_' + str(card) + '_Row_' + str(Rows - 1)):
                    if Special_Views.row_names[i] == Special_Views.row_names[7]:
                            add_combo(tag=Special_Views.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows), items=special_category_ids, default_value=previous_row_values[i], width=149, parent=f'Special_Views_Table_Row_{card}{Rows}')
                    else:
                            add_input_text(tag=Special_Views.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows), hint=Special_Views.column_names[i], width=105, default_value=previous_row_values[i], parent=f'Special_Views_Table_Row_{card}{Rows}')
            else:
                    if Special_Views.row_names[i] == Special_Views.row_names[7]:
                            add_combo(tag=Special_Views.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows), items=special_category_ids, default_value=special_category_ids[0], width=149, parent=f'Special_Views_Table_Row_{card}{Rows}')
                    else:
                            add_input_text(tag=Special_Views.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows), hint=Special_Views.column_names[i], width=105, default_value='', parent=f'Special_Views_Table_Row_{card}{Rows}') 

    set_item_height(f'Special_Views_Table_{card}', (24 * (Rows + 1) + 23))
    pass

########################################################################################################################################################################################################
def Special_Views_Del(tag_id):
    card = Table_ID(tag_id)
    
    # Dynamically check existing rows
    Rows = Row_Checker(Special_Views.row_names[0] + '_Card_' + str(card) + '_Row_')
    
    if Rows > 1:
            delete_item(f'Special_Views_Table_Row_{card}{Rows - 1}')
            for i in range(len(Special_Views.row_names)):
                    # Passive_Skill.row_names[2] is Efficacy Type
                            delete_item(Special_Views.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows - 1))
                            
            set_item_height(f'Special_Views_Table_{card}', (24 * (Rows - 1) + 23))

########################################################################################################################################################################################################
def Special_View_Widgets(card):
    # SpecialCategoryID = Type of Super Attack, 1 = Ki Blast, 2 = Unarmed, 3 = Physical/Melee, NULL = Undefined)
    special_category_ids = ['Undefined', 'Ki Blast', 'Unarmed', 'Physical/Melee']
    
    Delete_Items([f'Special_Views_Buttons_Group_{card}', f'Special_Views_Add_Button_{card}', f'Special_Views_Del_Button_{card}'])
    with group(horizontal=True, tag=f'Special_Views_Buttons_Group_{card}', parent=f'Special_Views_{card}'):
        add_button(label='+', tag=f'Special_Views_Add_Button_{card}', callback=Special_Views_Add)
        add_button(label='-', tag=f'Special_Views_Del_Button_{card}', callback=Special_Views_Del)
        
        
    tt = Table_Combo_Inputs(table_name=f'Special_Views_Table_{card}', row_name=f'Special_Views_Table_Row_{card}', table_parent=f'Special_Views_{card}', 
                       class_name=Special_Views, table_width=920, row_width=100, table_height=45, freeze_rows=1, table_policy=mvTable_SizingFixedFit,
                       combo_columns=[7], combo=True, combo_list=[[], [], [], [], [], [], [], special_category_ids], transformation_card_num=card)
    
    # Set values to the most common value found in database
    set_value(Special_Views.row_names[2] + '_Card_' + str(card) + '_Row_0', '0')
    set_value(Special_Views.row_names[3] + '_Card_' + str(card) + '_Row_0', '0')
    set_value(Special_Views.row_names[5] + '_Card_' + str(card) + '_Row_0', '70')
    set_value(Special_Views.row_names[6] + '_Card_' + str(card) + '_Row_0', 'NULL')
    
    set_item_height(f'Special_Views_Table_{card}', (24 * (Special_Views.rows) + 23))
    configure_item(f'Special_Views_{card}', show=True)
    