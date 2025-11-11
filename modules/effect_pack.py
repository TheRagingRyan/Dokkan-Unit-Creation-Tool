from dearpygui.dearpygui import *
from . functions import Table_Combo_Inputs, Table_ID, Row_Checker, Delete_Items
from . classes import Effect_Pack



def Effect_Pack_Add(tag_id):
    card = Table_ID(tag_id)
    
    Rows = Row_Checker(Effect_Pack.row_names[0] + '_Card_' + str(card) + '_Row_')
    eff_categories = ['Battle/Support Packs', 'SP Effect Packs']
    
    
    if get_value(Effect_Pack.row_names[0] + '_Card_' + str(card) + '_Row_' + str(Rows - 1)):
            effect_pack_tags = [Effect_Pack.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows - 1) for i in range(len(Effect_Pack.row_names))]
            previous_row_values = get_values(effect_pack_tags)
            previous_row_values[0] = str(int(previous_row_values[0]) + 1)
    else:
            previous_row_values = []
    
    add_table_row(tag=f'Effect_Packs_Table_Row_{card}{Rows}', parent=f'Effect_Packs_Table_{card}')
    
    for i in range(len(Effect_Pack.row_names)):
        
            if get_value(Effect_Pack.row_names[0] + '_Card_' + str(card) + '_Row_' + str(Rows - 1)):
                    if Effect_Pack.row_names[i] == Effect_Pack.row_names[1]:
                            add_combo(tag=Effect_Pack.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows), items=eff_categories, default_value=previous_row_values[i], width=149, parent=f'Effect_Packs_Table_Row_{card}{Rows}')
                    else:
                            add_input_text(tag=Effect_Pack.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows), hint=Effect_Pack.column_names[i], width=105, default_value=previous_row_values[i], parent=f'Effect_Packs_Table_Row_{card}{Rows}')
            else:
                    if Effect_Pack.row_names[i] == Effect_Pack.row_names[1]:
                            add_combo(tag=Effect_Pack.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows), items=eff_categories, default_value=eff_categories[0], width=149, parent=f'Effect_Packs_Table_Row_{card}{Rows}')
                    else:
                            add_input_text(tag=Effect_Pack.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows), hint=Effect_Pack.column_names[i], width=105, default_value='', parent=f'Effect_Packs_Table_Row_{card}{Rows}') 

    set_item_height(f'Effect_Packs_Table_{card}', (24 * (Rows + 1) + 23))

########################################################################################################################################################################################################
def Effect_Pack_Del(tag_id):
    card = Table_ID(tag_id)
    
    # Dynamically check existing rows
    Rows = Row_Checker(Effect_Pack.row_names[0] + '_Card_' + str(card) + '_Row_')
    
    if Rows > 1:
            delete_item(f'Effect_Packs_Table_Row_{card}{Rows - 1}')
            for i in range(len(Effect_Pack.row_names)):
                    # Passive_Skill.row_names[2] is Efficacy Type
                            delete_item(Effect_Pack.row_names[i] + '_Card_' + str(card) + '_Row_' + str(Rows - 1))
                            
            set_item_height(f'Effect_Packs_Table_{card}', (24 * (Rows - 1) + 23))

########################################################################################################################################################################################################
def Effect_Packs_Widgets(card):
    eff_categories = ['Battle/Support Packs', 'SP Effect Packs']
    
    Delete_Items([f'Effect_Buttons_Group_{card}', f'Effect_Pack_Add_Button_{card}', f'Effect_Pack_Del_Button_{card}'])
    with group(horizontal=True, tag=f'Effect_Buttons_Group_{card}', parent=f'Effect_Packs_{card}'):
        add_button(label='+', tag=f'Effect_Pack_Add_Button_{card}', callback=Effect_Pack_Add)
        add_button(label='-', tag=f'Effect_Pack_Del_Button_{card}', callback=Effect_Pack_Del)
        
        
    tt = Table_Combo_Inputs(table_name=f'Effect_Packs_Table_{card}', row_name=f'Effect_Packs_Table_Row_{card}', table_parent=f'Effect_Packs_{card}', 
                       class_name=Effect_Pack, table_width=612, row_width=105, table_height=45, freeze_rows=1, table_policy=mvTable_SizingFixedFit,
                       combo_columns=[1], combo=True, combo_list=[[], eff_categories], transformation_card_num=card)
    
    set_item_height(f'Effect_Packs_Table_{card}', (24 * (Effect_Pack.rows) + 23))
    configure_item(f'Effect_Packs_{card}', show=True)
    set_value(f'Custom_Unit_Effect_Packs_Checkbox_{card}', True)
    
