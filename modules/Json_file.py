import json
from dearpygui.dearpygui import *
from . passive import Passive_Skill
from . functions import Card_Checker, Row_Checker, Delete_Items
from . classes import Custom_Unit, Card_Checks, Card, Passive_Skill, Active_Skill, Active_Skill_Set, Leader_Skill_Info, Standby_Skill_Set, Standby_Skill, Finish_Skill_Set, Finish_Skill, Transformation_Descriptions, Battle_Params, Widget_Aliases, Special_Set, Specials, Card_Specials, Dokkan_Field, Effect_Pack, Special_Views, Causality
from . categories import Categories_Activated
from . effect_pack import Effect_Packs_Widgets
from . json_functions import Card_Thumb_Display, Card_Widgets, Passive_Widgets, Specials_Widgets, Active_Skill_Widgets, Standby_Skill_Widgets, Finish_Skill_Set_Widgets, Dokkan_Field_Widgets, Battle_Params_Widgets, Leader_Skill_Widgets, Custom_Unit_Categories_Load, Json_Load_Effect_Packs, Json_Load_Special_Views
from . special_views import Special_View_Widgets
from . causality import Load_Causalities
from . configs import Config_Path
import easygui
from pypresence import Presence
import time
from . configs import Config_Read
from . custom_unit import Custom_Unit_Create_Tabs, Custom_Card_Thumb_Display, Custom_Unit_Card_Thumb_Display
import os
# from . discord import RPC
# try:
#     RPC = Presence(774666488690769930)
#     RPC.connect()
# except Exception as e:
#     Discord_Presence = False


def JSON_Save():
    print('Cards' + str(Card_Checker()))
    data = {}
    for card in range(Card_Checker()):
        ############
        ### Card ###
        ############
        
        card_rows = []
        
        card_row_names = [Card.row_names[z] + '_Card_' + str(card) + '_Row_1' for z in range(len(Card.row_names))]
        card_rows.append(get_values(card_row_names))
            
        card_rows = {Card.column_names[z]: card_rows[0][z] for z in range(len(Card.column_names))}
        
        
        ### Delete from dictionary and assign to a variable so I can use it as the whole dictionary list instead
        
        ##########################################################################################################
        ###############
        ### Passive ###
        ###############
        
        passive_name = get_value(Passive_Skill.row_names[0] + '_Card_' + str(card) + '_Row_' + '0')
        passive_desc = get_value(f'Passive_Desc_Text_Input_{card}')
        passive_row_dict = {'Name' : passive_name,
                            'Desc' : passive_desc,
                            'Skills' : []}
        
        for row in range(Row_Checker(Passive_Skill.row_names[0] + '_Card_' + str(card) + '_Row_')):
            passive_row = [Passive_Skill.row_names[z + 1] + '_Card_' + str(card) + '_Row_' + str(row) for z in range(len(Passive_Skill.row_names) - 1)]
        
            passive_rows_values = (get_values(passive_row))
            ### Instead I'll leave the text in the efficacy type, then when I code the loading portion of the json, I'll just remove the text then use the number to set the eff value in the combo.
            ### This way if someone were to want to change the efficacy type in the json, they still can as it will just grab the number still
            
            # number_match = re.search(r'\d+', passive_rows_values[2])
            # if number_match:
                # extracted_number = number_match.group()
                # passive_rows_values[2] = extracted_number
                
            passive_row_dict_row = {Passive_Skill.column_names[z + 1] : passive_rows_values[z] for z in range(len(passive_rows_values))}
            passive_row_dict['Skills'].append(passive_row_dict_row)
            
            
        
        ##########################################################################################################
        ################
        ### Specials ###
        ################
        specials_rows = []
        
        specials_final_output = []
        for special in range(Row_Checker(f'Special#_Text_Card_{card}_')):
            special_set_name = get_value(f'Special_Set_Name_Input_Card_{card}_{special}')
            special_set_desc = get_value(f'Special_Set_Desc_Input_Card_{card}_{special}')
            special_set_cond = get_value(f'Special_Set_Cond_Input_Card_{card}_{special}')
            special_set_target = get_value(f'Special_Set_Aim_Target_Input_Card_{card}_{special}')
            special_set_increase_rate = get_value(f'Special_Set_Increase_Rate_Input_Card_{card}_{special}')
            special_set_level_bonus = get_value(f'Special_Set_Level_Bonus_Input_Card_{card}_{special}')
            card_specials_rows_values = []
            specials_rows_values = []
            
            ### Grab Card Specials values for this 'special'
            for card_special_row in range(Row_Checker(Card_Specials.row_names[0] + '_Card_' + str(card) + '_Row_' + str(special))):
                card_specials_rows = ([Card_Specials.row_names[z] + '_Card_' + str(card) + '_Row_' + str(special) + str(card_special_row) for z in range(len(Card_Specials.row_names))])
                card_specials_values = get_values(card_specials_rows)
                card_specials_dict = {Card_Specials.column_names[z] : card_specials_values[z] for z in range(len(card_specials_values))}
                card_specials_rows_values.append(card_specials_dict)
            
            for special_skill_row in range(Row_Checker(Specials.row_names[0] + '_Card_' + str(card) + '_Row_' + str(special))):
                specials_rows = ([Specials.row_names[z] + '_Card_' + str(card) + '_Row_' + str(special) + str(special_skill_row) for z in range(len(Specials.row_names))])
                specials_skills_values = get_values(specials_rows)
                specials_skills_dict = {Specials.column_names[z] : specials_skills_values[z] for z in range(len(specials_skills_values))}
                specials_rows_values.append(specials_skills_dict)
        
            
            specials_dict = {'Name' : special_set_name,
                             'Desc' : special_set_desc,
                             'Cond' : special_set_cond,
                             'Target' : special_set_target,
                             'Inc Rate' : special_set_increase_rate,
                             'Lvl Bonus' : special_set_level_bonus,
                             'Card Specials' : card_specials_rows_values,
                             'Skills' : specials_rows_values
                             }
            
            specials_final_output.append(specials_dict)
            
        ##########################################################################################################
        ####################
        ### Leader Skill ###
        ####################
        if does_alias_exist(f'Leader_Skill_Text_{card}'):
            leader_skill_values_final_output = []
            ### Will need to modify later when custom unit gets multiple leader skill as a possibility
            leader_skill_description = get_value(f'Leader_Desc_Text_Input_{card}')
            leader_skill_name = get_value(f'Leader_Name_Text_Input_{card}')

            leader_skill_category_presets = [f'Leader_Skill_Category_Selection_{card}_{z}' for z in range(Row_Checker(f'Leader_Skill_Category_Selection_{card}_'))]
            leader_skill_category_presets = get_values(leader_skill_category_presets)
            leader_skill_dict = {'Preset' : get_value(f'Leader_Skill_Preset_List_{card}')}
            leader_skill_dict['Categories'] = leader_skill_category_presets
            leader_skill_dict['Name'] = leader_skill_name
            leader_skill_dict['Desc'] = leader_skill_description
            
            for leader_row in range(Row_Checker(Leader_Skill_Info.row_names[0] + '_Card_' + str(card) + '_Row_')):
                leader_skill_row = [Leader_Skill_Info.row_names[z] + '_Card_' + str(card) + '_Row_' + str(leader_row) for z in range(len(Leader_Skill_Info.row_names))]
                leader_skill_values = (get_values(leader_skill_row))
                leader_skill_values_final_output.append({Leader_Skill_Info.column_names[z] : leader_skill_values[z] for z in range(len(leader_skill_values))})
            
            leader_skill_dict['Skills'] = leader_skill_values_final_output
        else:
            leader_skill_dict = {}
            
        ##########################################################################################################
        ##################
        ### Categories ###
        ##################
        categories_dict = []
        if Categories_Activated.card_categories_dict[card]:
            for cat in Categories_Activated.card_categories_dict[card]:
                categories_dict.append(cat)
                    
        
        ##########################################################################################################
        ####################
        ### Active Skill ###
        ####################
        if does_alias_exist(f'Active_Skill_Text_Card_{card}'):
            active_skill_name = get_value(f'Active_Name_Card_{card}')
            active_skill_desc = get_value(f'Active_Desc_Card_{card}')
            active_skill_cond = get_value(f'Active_Cond_Card_{card}')
            
            active_skill_dict = {'Name' : active_skill_name,
                                 'Desc' : active_skill_desc,
                                 'Cond' : active_skill_cond,
                                 'Set' : {},
                                 'Skills' : []}
            
            ### Active Skill Set
            active_skill_row = [Active_Skill_Set.row_names[z] + '_Card_' + str(card) + '_Row_0' for z in range(len(Active_Skill_Set.row_names))]
            active_skill_row = get_values(active_skill_row)
            # active_skill_dict['Set'].append({Active_Skill_Set.column_names[z] : active_skill_row[z] for z in range(len(active_skill_row))})
            active_skill_dict['Set'] = {Active_Skill_Set.column_names[z] : active_skill_row[z] for z in range(len(active_skill_row))}
            
            ### Active Skill
            num_of_active_skill_rows = Row_Checker(Active_Skill.row_names[0] + '_Card_' + str(card) + '_Row_')
            if num_of_active_skill_rows != 0:
                for row in range(num_of_active_skill_rows):
                    active_skill_row = [Active_Skill.row_names[z] + '_Card_' + str(card) + '_Row_' + str(row) for z in range(len(Active_Skill.row_names))]
                    active_skill_row = get_values(active_skill_row)
                    active_skill_dict['Skills'].append({Active_Skill.column_names[z] : active_skill_row[z] for z in range(len(active_skill_row))})
            else:
                active_skill_dict['Skills'] = []
                
            if does_alias_exist(f'Ultimate_Special_Text_Card_{card}'):
                ultimate_skill_row = [Active_Skill.ultimate_names[z] + '_Card_' + str(card) for z in range(len(Active_Skill.ultimate_names))]
                ultimate_skill_row = get_values(ultimate_skill_row)
                ultimate_skill_dict = {Active_Skill.ultimate_hints[z] : ultimate_skill_row[z] for z in range(len(ultimate_skill_row))}
            else:
                ultimate_skill_dict = {}
            
        else:
            active_skill_dict = []
            ultimate_skill_dict = {}
            
        ##########################################################################################################
        #####################
        ### Standby Skill ###
        #####################
        ### Just going to use 0 for the standby skill as it should theoretically act like an active skill, and if you do more than one active skill on a unit, it will crash.
        if does_alias_exist(f'Standby_Skill_Set_Text_{card}_0'):
            standby_skill_name = get_value(f'Standby_Set_Name_Input_Text_{card}_0')
            standby_skill_desc = get_value(f'Standby_Set_Desc_Input_Text_{card}_0')
            standby_skill_cond = get_value(f'Standby_Set_Cond_Input_Text_{card}_0')
            standby_skill_dict = {'Name' : standby_skill_name,
                                  'Desc' : standby_skill_desc,
                                  'Cond' : standby_skill_cond,
                                  'Set' : '',
                                  'Skills' : []}
            
            ### Standby Skill Set
            standby_skill_row = [Standby_Skill_Set.row_names[z] + '_Card_' + str(card) + '_Row_' + '00' for z in range(len(Standby_Skill_Set.row_names))]
            standby_skill_row = get_values(standby_skill_row)
            standby_skill_dict['Set'] = {Standby_Skill_Set.column_names[z] : standby_skill_row[z] for z in range(len(standby_skill_row))}
            
            ### Standby Skills
            for skill in range(Row_Checker(Standby_Skill.row_names[0] + '_Card_' + str(card) + '_Row_' + '0')):
                standby_skill_row = [Standby_Skill.row_names[z] + '_Card_' + str(card) + '_Row_0' + str(skill) for z in range(len(Standby_Skill.row_names))]
                standby_skill_row = get_values(standby_skill_row)
                standby_skill_dict['Skills'].append({Standby_Skill.column_names[z] : standby_skill_row[z] for z in range(len(standby_skill_row))})
        else:
            standby_skill_dict = []
            
        ##########################################################################################################
        ####################
        ### Finish Skill ###
        ####################
        if does_alias_exist(f'Finish_Skill_Set_Text_{card}_0'):
            finish_skill_dict = []

            for finish_skill in range(Row_Checker(f'Finish_Skill_Set_Text_{card}_')):
                finish_skill_name = get_value(f'Finish_Set_Name_{card}_{finish_skill}')
                finish_skill_desc = get_value(f'Finish_Set_Desc_{card}_{finish_skill}')
                finish_skill_cond = get_value(f'Finish_Set_Cond_{card}_{finish_skill}')
                finish_skill_dict_set = {'Name' : finish_skill_name,
                                      'Desc' : finish_skill_desc,
                                      'Cond' : finish_skill_cond,
                                      'Set' : '',
                                      'Skills' : []}
        
                ### Finish Skill Set
                finish_skill_row = [Finish_Skill_Set.row_names[z] + '_Card_' + str(card) + '_Row_' + str(finish_skill) + '0' for z in range(len(Finish_Skill_Set.row_names))]
                finish_skill_row = get_values(finish_skill_row)
                finish_skill_dict_set['Set'] = {Finish_Skill_Set.column_names[z] : finish_skill_row[z] for z in range(len(finish_skill_row))}  

                ### Finish Skills
                for skill in range(Row_Checker(Finish_Skill.row_names[0] + '_Card_' + str(card) + '_Row_' + str(finish_skill))):
                    finish_skill_row = [Finish_Skill.row_names[z] + '_Card_' + str(card) + '_Row_' + str(finish_skill) + str(skill) for z in range(len(Finish_Skill.row_names))]
                    finish_skill_row = get_values(finish_skill_row)
                    finish_skill_dict_set['Skills'].append({Finish_Skill.column_names[z] : finish_skill_row[z] for z in range(len(finish_skill_row))}) 
                finish_skill_dict.append(finish_skill_dict_set)
        else:
            finish_skill_dict = []
            
        ##########################################################################################################
        ####################
        ### Dokkan Field ###
        ####################
        if does_alias_exist(f'Dokkan_Field_Text_{card}_0'):
            dokkan_field_dict = []
            for field in range(Row_Checker(f'Dokkan_Field_Text_{card}_')):
                dokkan_field_name = get_value(f'Dokkan_Field_Name_Input_Text_{card}_{field}')
                dokkan_field_desc = get_value(f'Dokkan_Field_Desc_Input_Text_{card}_{field}')
                dokkan_field_resource_id = get_value(f'Dokkan_Field_Resource_ID_{card}_{field}')
                link_to_active = get_value(f'Link_to_Active_Button_{card}_{field}')
                link_to_passive = get_value(f'Link_to_Passive_Button_{card}_{field}')
                
                dokkan_field_dict_set = {'Name' : dokkan_field_name,
                                         'Desc' : dokkan_field_desc,
                                         'Resource ID' : dokkan_field_resource_id,
                                         'Link to Active' : link_to_active,
                                         'Link to Passive' : link_to_passive,
                                         'Skills' : []}
                
                for skill in range(Row_Checker(Dokkan_Field.row_names[0] + '_Card_' + str(card) + '_Row_' + str(field))):
                    dokkan_field_row = [Dokkan_Field.row_names[z] + '_Card_' + str(card) + '_Row_' + str(field) + str(skill) for z in range(len(Dokkan_Field.row_names))]
                    dokkan_field_row = get_values(dokkan_field_row)
                    dokkan_field_dict_set['Skills'].append({Dokkan_Field.column_names[z] : dokkan_field_row[z] for z in range(len(dokkan_field_row))})
                dokkan_field_dict.append(dokkan_field_dict_set)
        else:
            dokkan_field_dict = []
                
        ##########################################################################################################
        #####################
        ### Battle Params ###
        #####################
        if does_alias_exist(f'Transformation_Information_Text_{card}'):
            transformation_dict = []
            
            
            for row in range(Row_Checker(Transformation_Descriptions.row_names[0] + '_Card_' + str(card) + '_Row_')):
                transformation_skill_type = get_value(Transformation_Descriptions.row_names[0] + '_Card_' + str(card) + '_Row_' + str(row))
                transformation_desc = get_value(Transformation_Descriptions.row_names[1] + '_Card_' + str(card) + '_Row_' + str(row))
                transformation_dict_set = {'Skill Type' : transformation_skill_type,
                                       'Desc' : transformation_desc}
                transformation_dict.append(transformation_dict_set)
        else:
            transformation_dict = []
            
        if does_alias_exist(f'Battle_Params_Text_{card}'):
            battle_params_dict = {}
            for battle_param in range(Row_Checker(f'Battle_Params_Table_{card}_')):
                battle_params_dict_set = []
                for battle_param_row in range(Row_Checker(Battle_Params.row_names[0] + '_Card_' + str(card) + '_Row_' + str(battle_param))):
                    battle_params_row = [Battle_Params.row_names[z + 1] + '_Card_' + str(card) + '_Row_' + str(battle_param) + str(battle_param_row) for z in range(len(Battle_Params.row_names) - 1)]
                    battle_params_row = get_values(battle_params_row)
                    battle_params_dict_set.append({Battle_Params.column_names[z + 1] : battle_params_row[z] for z in range(len(battle_params_row))})
                battle_params_dict[get_value(Battle_Params.row_names[0] + '_Card_' + str(card) + '_Row_' + str(battle_param) + '0')] = battle_params_dict_set
        else:
            battle_params_dict = {}
            
        ##########################################################################################################
        ####################
        ### Effect Packs ###
        ####################
        if does_alias_exist(f'Effect_Packs_Table_{card}'):
            effect_packs_dict = []
            for row in range(Row_Checker(f'Effect_Packs_Table_Row_{card}')):
                effect_packs_set = {Effect_Pack.column_names[i] : get_value(Effect_Pack.row_names[i] + '_Card_' + str(card) + '_Row_' + str(row)) for i in range(len(Effect_Pack.row_names))}
                effect_packs_dict.append(effect_packs_set)
        
        else:
            effect_packs_dict = []
        
        
        ##########################################################################################################
        #####################
        ### Special Views ###
        #####################
        if does_alias_exist(f'Special_Views_Table_{card}'):
            special_views_dict = []
            for row in range(Row_Checker(f'Special_Views_Table_Row_{card}')):
                special_views_set = {Special_Views.column_names[i] : get_value(Special_Views.row_names[i] + '_Card_' + str(card) + '_Row_' + str(row)) for i in range(len(Special_Views.row_names))}
                special_views_dict.append(special_views_set)
        
        else:
            special_views_dict = []

        
        ##########################################################################################################
        ##################
        ### Causality ###
        ##################
        causality_dict = []
        if get_value(f'{Causality.row_names[1]}0') == '(0) None':
           causality_dict = {}

        else:
            for row in range(Row_Checker(f'{Causality.row_names[1]}')):
                causality_set = {Causality.column_names[i] : get_value(Causality.row_names[i] + str(row)) for i in range(len(Causality.row_names))}
                causality_dict.append(causality_set)
        #     for u in range(len(Causality.row_names)):
        #         if does_alias_exist(Causality.row_names[u] + '0' + str(last_rows)):
        #             delete_item(Causality.row_names[u] + '0' + str(last_rows))
                
        
        ##########################################################################################################
        ######################
        ### Output Section ###
        ######################
        print(Custom_Unit.card_thumb_dict)
        card_thumb = Custom_Unit.card_thumb_dict[card]
        
        card_info = {
            'EZA' : get_value(f'EZA_Checkbox_{card}'),
            'Card Thumb' : card_thumb,
            'Card' : card_rows,
            'Passive' : passive_row_dict,
            'Specials' : specials_final_output,
            'Leader Skill' : leader_skill_dict,
            'Categories' : categories_dict,
            'Active Skill' : active_skill_dict,
            'Ultimate Special' : ultimate_skill_dict,
            'Standby Skill' : standby_skill_dict,
            'Finish Skill' : finish_skill_dict,
            'Dokkan Field' : dokkan_field_dict,
            'Transformation' : transformation_dict,
            'Battle Params' : battle_params_dict,
            'Effect Packs' : effect_packs_dict,
            'Special Views' : special_views_dict,
            'Causalities' : causality_dict
        }
        
        data[f'Card {card + 1}'] = card_info 

    json_string = json.dumps(data, indent=4)
    
    ### Temporary
    filename = get_value(Card.row_names[1] + '_Card_0_Row_0') + ' (' + get_value(Card.row_names[0] + '_Card_0_Row_0') + ')'
    config = Config_Read()
    ### Checks the config for the saved JSON save location, if it doesn't exist it creates it so the next time it opens in the same spot.
    if config.has_option('DEFAULT', 'JSON_Save_Location'):
        
        filepath = config.get('DEFAULT', 'JSON_Save_Location')
        json_file_name = easygui.filesavebox(msg='Input the name of your JSON', default=filepath + '\\' + filename + '.json', filetypes=['*.json'])
        
        if json_file_name and '.json' in json_file_name:
            directory_path = os.path.dirname(json_file_name)
            # file_name = os.path.basename(json_file)

            if directory_path != filepath:
                config.set('DEFAULT', 'JSON_Save_Location', directory_path)
                with open(Config_Path(), 'w') as config_file:
                    config.write(config_file)


            with open(f"{json_file_name}", "w") as json_file:
                json_file.write(json_string)
    else:
                
        json_file_name = easygui.filesavebox(msg='Input the name of your JSON', default=f'{filename}.json', filetypes=['*.json'])
        if json_file_name and '.json' in json_file_name:
            # Extract the directory path and file name
            directory_path = os.path.dirname(json_file_name)
            file_name = os.path.basename(json_file_name)

            config.set('DEFAULT', 'JSON_Save_Location', directory_path)
            with open(Config_Path(), 'w') as config_file:
                config.write(config_file)
                
            with open(f"{json_file_name}", "w") as json_file:
                json_file.write(json_string)

            # Now you have both the directory path and file name
            # print("Directory Path:", directory_path)
            # print("File Name:", file_name)

        

        

    
    # with open(f"cards.json", "w") as json_file:
    #     json_file.write(json_string)
        
####################################################################################################################################################################################################################

def JSON_Load():
    from modules import RPC
    Custom_Unit.json = True
    config = Config_Read()
    if config.has_option('DEFAULT', 'JSON_Save_Location'):
        
        file_path = config.get("DEFAULT", 'JSON_Save_Location')
        json_file = easygui.fileopenbox(msg='Select a unit JSON to load', filetypes=['*.json'], default=f'{file_path}\*.json')
        if json_file:
            directory_path = os.path.dirname(json_file)
            # file_name = os.path.basename(json_file)
            
            if directory_path != file_path:
                config.set('DEFAULT', 'JSON_Save_Location', directory_path)
                with open(Config_Path(), 'w') as config_file:
                    config.write(config_file)

            with open(json_file, "r") as json_file:
                data = json.load(json_file)
                
            if len(Widget_Aliases.tags_to_delete) > 0:
                Delete_Items(Widget_Aliases.tags_to_delete)
                Widget_Aliases.tags_to_delete.clear()

            
            Custom_Unit.card_number = 0
            number_of_cards = len(data)
            for card in range(number_of_cards):
                Custom_Unit_Create_Tabs(json_dict=data)
                configure_item(f'Main_Card_Tab_{card}', label=data[f'Card {card + 1}']['Card']['Name'])
                Custom_Unit.card_thumb_dict[card] = data[f'Card {card + 1}']['Card Thumb']
                Custom_Unit.card_number += 1
                
            Custom_Unit.card_number = 0
            for card in range(number_of_cards):
                Card_Thumb_Display(number_of_cards, data)
                
            for card in range(number_of_cards):
                if Custom_Unit.card_number == 0:
                    pass
                
                Custom_Unit_Card_Thumb_Display()
                Custom_Unit.card_number += 1
                pass
                
                
            # Custom_Unit_Selectables(number_of_cards)
            # Card_Thumb_Display(number_of_cards, data)
            Card_Widgets(number_of_cards, data)
            Passive_Widgets(number_of_cards, data)
            Specials_Widgets(number_of_cards, data)
            Custom_Unit_Categories_Load(number_of_cards, data)
            Active_Skill_Widgets(number_of_cards, data)
            Standby_Skill_Widgets(number_of_cards, data)
            Finish_Skill_Set_Widgets(number_of_cards, data)
            Dokkan_Field_Widgets(number_of_cards, data)
            Battle_Params_Widgets(number_of_cards, data)
            Leader_Skill_Widgets(number_of_cards, data)
            Load_Causalities(data)
            for card in range(number_of_cards):
                Json_Load_Effect_Packs(card, data)
                Json_Load_Special_Views(card, data)
            
            card_name = data['Card 1']['Card']['Name']
            card_id = str(Card_Checks.json_unit_card_ids[0])[:-1] + '1' 
            wiki_link = f'https://dokkan.wiki/cards/{card_id}'
            
            if RPC:
                RPC.update(
                    state='Creating a Unit',
                    details=card_name,
                    large_image="zamasu_and_vegito",
                    small_image="gold_small_image",
                    start=time.time(),
                    buttons=[{"label": "Wiki Link", "url": wiki_link}, {"label": "Discord", "url": "https://discord.gg/fGdxkZpUyz"}]
                    # https://discord.gg/EWTyTnPhn7
                )
            Custom_Unit.card_number = number_of_cards - 1
        
    else:
        json_file = easygui.fileopenbox(msg='Select a unit JSON to load', filetypes=['*.json'], default='*.json')
        if json_file and '.json' in json_file:
            
            directory_path = os.path.dirname(json_file)
            file_name = os.path.basename(json_file)

            config.set('DEFAULT', 'JSON_Save_Location', directory_path)
            with open(Config_Path(), 'w') as config_file:
                config.write(config_file)
                
            with open(json_file, "r") as json_file:
                data = json.load(json_file)
                
            if len(Widget_Aliases.tags_to_delete) > 0:
                Delete_Items(Widget_Aliases.tags_to_delete)
                Widget_Aliases.tags_to_delete.clear()
                
            card_name = data['Card 1']['Card']['Name']
            card_id = str(Card_Checks.json_unit_card_ids[0])[:-1] + '1' 
            wiki_link = f'https://dokkan.wiki/cards/{card_id}'
            
            if RPC:
                RPC.update(
                    state='Creating a Unit',
                    details=card_name,
                    large_image="zamasu_and_vegito",
                    small_image="gold_small_image",
                    start=time.time(),
                    buttons=[{"label": "Wiki Link", "url": wiki_link}, {"label": "Discord", "url": "https://discord.gg/fGdxkZpUyz"}]
                    # https://discord.gg/EWTyTnPhn7
                )
                
            Custom_Unit.card_number = 0
            number_of_cards = len(data)
            for card in range(number_of_cards):
                Custom_Unit_Create_Tabs(json_dict=data)
                configure_item(f'Main_Card_Tab_{card}', label=data[f'Card {card + 1}']['Card']['Name'])
                Custom_Unit.card_thumb_dict[card] = data[f'Card {card + 1}']['Card Thumb']
                Custom_Unit.card_number += 1
                
            Custom_Unit.card_number = 0
            for card in range(number_of_cards):
                Card_Thumb_Display(number_of_cards, data)
                
            for card in range(number_of_cards):
                if Custom_Unit.card_number == 0:
                    pass
                
                Custom_Unit_Card_Thumb_Display()
                Custom_Unit.card_number += 1
                pass
                
                
            # Custom_Unit_Selectables(number_of_cards)
            # Card_Thumb_Display(number_of_cards, data)
            Card_Widgets(number_of_cards, data)
            Passive_Widgets(number_of_cards, data)
            Specials_Widgets(number_of_cards, data)
            Custom_Unit_Categories_Load(number_of_cards, data)
            Active_Skill_Widgets(number_of_cards, data)
            Standby_Skill_Widgets(number_of_cards, data)
            Finish_Skill_Set_Widgets(number_of_cards, data)
            Dokkan_Field_Widgets(number_of_cards, data)
            Battle_Params_Widgets(number_of_cards, data)
            Leader_Skill_Widgets(number_of_cards, data)
            Load_Causalities(data)
            for card in range(number_of_cards):
                Json_Load_Effect_Packs(card, data)
                Json_Load_Special_Views(card, data)
            Custom_Unit.card_number = number_of_cards - 1
            
    
    # if json_file and '.json' in json_file:
        # with open(json_file, "r") as json_file:
            # data = json.load(json_file)
            
    # with open(f"cards.json", "r") as json_file:
    #     data = json.load(json_file)
        
