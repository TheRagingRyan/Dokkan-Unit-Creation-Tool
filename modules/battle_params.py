from dearpygui.dearpygui import *
from . functions import Table_Combo_Inputs, Resize_Table, Table_ID, Delete_Items, Row_Checker
from . classes import Card, Widget_Aliases, Card_Checks, Transformation_Descriptions, Battle_Params

##########################################################################################
### WILL NEED TO MODIFY THIS SECTION SHOULD A UNIT EVER GET MORE THAN ONE BATTLE PARAM ###
##########################################################################################

# It happened already dumbass

def Text_Resize(tag_id):
    text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIAL.ttf')
    set_item_width(tag_id, text_width + 27)


def Battle_Param_Sorted_Dictionary():
    param_dict = dict(Card_Checks.battle_params)
    
    sorted_dict = {outer_key: {inner_key: dict(sorted(inner_dict.items(), key=lambda x: int(x[0]))) for inner_key, inner_dict in outer_value.items()} for outer_key, outer_value in param_dict.items()}
        
    return sorted_dict

def Battle_Params_Information():
    battle_params_dictionary = Battle_Param_Sorted_Dictionary()
    # print(battle_params_dictionary)
    
    for card in range(len(Card_Checks.card_ids) - 1):
        # print(battle_params_dictionary[card])
        if battle_params_dictionary[card]:
            add_text('Transformation Information', tag=f'Transformation_Information_Text_{card}', color=(255,50,50), parent=f'Battle_Params_{card}')
            
            
            
            skill_type_combo_list = ['Active Skill', 'Passive Skill', 'Standby Skill', 'Finish Skill']
            tt = Table_Combo_Inputs(table_name=f'Transformation_Descriptions_Table_{card}', row_name=f'Transformation_Descriptions_Table_Row_{card}', table_parent=f'Battle_Params_{card}', 
                               class_name=Transformation_Descriptions, table_width=600, row_width=82, table_height=45, freeze_rows=1, table_policy=mvTable_SizingFixedFit,
                               combo_columns=[0], combo=True, combo_list=[skill_type_combo_list], transformation_card_num=card)
            # print(tt)
            set_value(Transformation_Descriptions.row_names[1] + '_Card_' + str(card) + '_Row_0', Card_Checks.transformation_descriptions[card])
            Text_Resize(Transformation_Descriptions.row_names[1] + '_Card_' + str(card) + '_Row_0')
            description_width = get_item_width(Transformation_Descriptions.row_names[1] + '_Card_' + str(card) + '_Row_0')
            set_item_width(f'Transformation_Descriptions_Table_{card}', description_width + 165)
            
                
            add_separator(tag=f'Transformation_Descriptions_Table_Separator_{card}', parent=f'Battle_Params_{card}')
            add_text('Battle Params', tag=f'Battle_Params_Text_{card}', color=(255,50,50), parent=f'Battle_Params_{card}')
            
            Widget_Aliases.tags_to_delete.append(f'Transformation_Information_Text_{card}')
            Widget_Aliases.tags_to_delete.append(f'Transformation_Descriptions_Table_Separator_{card}')
            Widget_Aliases.tags_to_delete.append(f'Battle_Params_Text_{card}')
            
            # Battle Param Section
            ######################################################################################################################################################################################
            ### key = param_no 
            param_num = 0
            for key, value in battle_params_dictionary[card].items():
                param_no_dict = value

                Battle_Params.rows = len(value)
                ttt = Table_Combo_Inputs(table_name=f'Battle_Params_Table_{card}_{param_num}', row_name=f'Battle_Params_Table_Row_{card}_{param_num}', table_parent=f'Battle_Params_{card}', 
                             class_name=Battle_Params, table_width=270, row_width=82, freeze_rows=1, transformation_card_num=card, loop_number=param_num, used_in_loop=True, table_policy=mvTable_SizingFixedFit)
                Resize_Table(f'Battle_Params_Table_{card}_{param_num}', Battle_Params.rows)
                # print(ttt)
                ### This is a dictionary
                for key2, value in param_no_dict.items():
                    # print(Battle_Params.row_names[0] + '_Card_' + str(card) + '_Row_' + str(param) + str(key))
                    set_value(Battle_Params.row_names[0] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(key2), key)
                    set_value(Battle_Params.row_names[1] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(key2), key2)
                    #  Length of Card ID
                    if len(str(value)) == 7:
                        # print(value)
                        set_value(Battle_Params.row_names[2] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(key2), str(value).replace(str(value)[1], '3'))
                    else:
                        set_value(Battle_Params.row_names[2] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(key2), value)
                configure_item(f'Battle_Params_{card}', show=True)
                param_num += 1
                
            

def Battle_Param_Presets(tag_id, data):
    card = Table_ID(tag_id)
    num_of_params = 0
    rows = []
    default_values = {}
    card_id = 0
    hints = {}
    Text_Resize(tag_id)
    
    if get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_0'):
        card_id = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_0'))
    
    if data == 'Transformation':
        num_of_params = 1
        rows = [9]
        default_values = {0 : ['0', 'EffectPackID', '0', '0', '0', '0', 'CardID1', '1', 'BGM']}
    
    elif data == 'Standby/Finish':
        num_of_params = 1
        rows = [9]
        default_values = {0 : ['0', '0', '0', '0', '0', '0', '23', '0', '0']}
    
    elif data == 'Rage':
        num_of_params = 2
        rows = [11, 7]
        default_values = {0 : ['0', '243', '32', '32', '100', '3', '2', 'XXXX', 'XXXX', 'XXXX', 'XXXX'], 1: ['Min Turns', 'Max Turns', 'Reverse %', '1', '1', '3', '3']}
        
    elif data == 'Giant':
        num_of_params = 2
        rows = [11, 7]
        default_values = {0 : ['0', '243', '32', '32', '100', '3', '2', 'XXXX', 'XXXX', 'XXXX', 'XXXX'], 1: ['Min Turns', 'Max Turns', 'Reverse %', '1', '1', '2', '2']}
    
    for i in range(2):
        Delete_Items(f'Battle_Params_Table_{card}_{i}')
        for rows in range(Row_Checker(Battle_Params.row_names[0] + '_Card_' + str(card) + '_Row_' + str(i))):
            delete_item(f'Battle_Params_Table_Row_{card}_' + str(rows))
            for i in range(len(Battle_Params.row_names)):
                delete_item(Battle_Params.row_names[i] + '_Card_' + str(card) + '_Row_' + str(i) + str(rows))
    
    x = 0
    for param_num in range(num_of_params):
        Battle_Params.rows = rows[param_num]
        ttt = Table_Combo_Inputs(table_name=f'Battle_Params_Table_{card}_{param_num}', row_name=f'Battle_Params_Table_Row_{card}_{param_num}', table_parent=f'Battle_Params_{card}', 
                        class_name=Battle_Params, table_width=270, row_width=82, freeze_rows=1, transformation_card_num=card, loop_number=param_num, used_in_loop=True, table_policy=mvTable_SizingFixedFit)
        Resize_Table(f'Battle_Params_Table_{card}_{param_num}', Battle_Params.rows)
        
        for row in range(rows[param_num]):
            set_value(Battle_Params.row_names[0] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(row), str(card_id + x))
            set_value(Battle_Params.row_names[1] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(row), str(row))
            set_value(Battle_Params.row_names[2] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(row), default_values[param_num][row])
            x += 1