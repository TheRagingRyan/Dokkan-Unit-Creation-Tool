from dearpygui.dearpygui import *
import re
from .functions import Widget_Value_Grabber, Card_Checker, Row_Checker, Value_Grabber
from .categories import Categories_Activated
from . classes import Causality, Card_Checks, Card, Passive_Skill, Active_Skill, Active_Skill_Set, Leader_Skill_Info, Standby_Skill_Set, Standby_Skill, Finish_Skill_Set, Finish_Skill, Battle_Params, Specials, Card_Specials, Export, Special_Views, Effect_Pack
from .cards import Card
import ast
left_bracket = '{'
right_bracket = '}'
brackets = left_bracket + right_bracket

def SQL_Spacer():
    # string = ''
    # for i in range(71):
        # string += '--------------'
    string = '-' * 994
        
    return string

def sql_output_data(CardName):
    sql_file_data = f'-- {CardName}'
    num_of_cards = Card_Checker()
    active_skill = False
    ultimate_special = False
    standby_skill = False
    finish_skill = False
    causalities = False
    dokkan_field = False
    eza = False
    
    
    
    # print(len(Cat_Icons_Activated))
    
    for card in range(num_of_cards):
        if does_alias_exist(f'Active_Skill_Text_Card_{card}'):
            active_skill = True
        if does_alias_exist(f'Standby_Skill_Set_Text_{card}_0'):
            standby_skill = True
            battle_params = Battle_Params_Output()
        if does_alias_exist(f'Finish_Skill_Set_Text_{card}_0'):
            finish_skill = True
        if does_alias_exist(f'Dokkan_Field_Name_Text_{card}_0'):
            dokkan_field = True
        # if does_alias_exist(Active_Skill.ultimate_names[0] + '_Card_' + str(card)):
            # ultimate_special = True
    
    if does_alias_exist('Causality_ID0'):
        if get_value('Causality_Causality_Type0') == '(0) None':
            causalities = False
        else:
            causalities = True
    
    if get_value(Card.row_names[16] + '_Card_' + str(0) + '_Row_' + '1'):
        eza = True
        
    if causalities:
        causalities = Causality_Output()
    cards = Card_Output()
    if eza:
        optimal_awakening = Optimal_Awakening_Growth_Output()
    passive = Passive_Output()
    specials = Specials_Output()
    leader = Leader_Output()
    categories = Categories_Output()
    
    # This checks for existing skills within the function.
    standby_finish = Standby_Finish_Output()


    if active_skill:
        active_skill = Active_Skill_Output()
        ultimate_special = Ultimate_Special_Output()
        
    if dokkan_field:
        dokkan_field = Dokkan_Field_Output()
        
    battle_params = Battle_Params_Output()
    
    effect_pack = Effect_Pack_Output()
    special_views = Special_Views_Output()
    
    sql_file_data += cards + '\n'
    if eza:
        sql_file_data += optimal_awakening + '\n\n'
        
    sql_file_data += SQL_Spacer() + '\n'
        
    sql_file_data += passive[2] + '\n'
    sql_file_data += passive[0] + '\n'
    sql_file_data += passive[1] + '\n\n'
    
    sql_file_data += SQL_Spacer() + '\n'
    
    sql_file_data += specials[0] + '\n'
    sql_file_data += specials[1] + '\n'
    sql_file_data += specials[2] + '\n\n'
    
    sql_file_data += SQL_Spacer() + '\n'
    
    if active_skill:
        sql_file_data += active_skill[2] + '\n'
        sql_file_data += active_skill[0] + '\n'
        sql_file_data += active_skill[1] + '\n\n'
        
        if ultimate_special:
            sql_file_data += ultimate_special + '\n\n'
            
        sql_file_data += SQL_Spacer() + '\n\n'
            
            
    if dokkan_field:
        sql_file_data += dokkan_field + '\n\n'
        
        sql_file_data += SQL_Spacer() + '\n'
    
    if standby_skill:
        sql_file_data += standby_finish[0] + '\n'
        sql_file_data += standby_finish[1] + '\n'
        sql_file_data += standby_finish[2] + '\n\n'
        sql_file_data += standby_finish[3] + '\n'
        sql_file_data += standby_finish[4] + '\n\n'
        sql_file_data += standby_finish[5] + '\n'
        sql_file_data += standby_finish[6] + '\n'
        sql_file_data += standby_finish[7] + '\n\n'
        
        sql_file_data += SQL_Spacer() + '\n'
        
    if battle_params:
        sql_file_data += battle_params + '\n\n'
        
        sql_file_data += SQL_Spacer() + '\n'
        
    sql_file_data += leader[0] + '\n'
    sql_file_data += leader[1] + '\n\n'
    sql_file_data += leader[2] + '\n'
    sql_file_data += leader[3] + '\n\n'
    
    sql_file_data += SQL_Spacer() + '\n'
    
    if categories:
        sql_file_data += categories + '\n\n'
    
        sql_file_data += SQL_Spacer() + '\n'
    
    if causalities:
        sql_file_data += causalities + '\n\n'
        
        sql_file_data += SQL_Spacer() + '\n'
        
    if effect_pack:
        sql_file_data += effect_pack + '\n\n'
        
        sql_file_data += SQL_Spacer() + '\n'
        
    if special_views:
        sql_file_data += special_views + '\n\n'
        
        sql_file_data += SQL_Spacer() + '\n'
        
    
        
    
    CardID_Replace = get_value('CardID1')
    CardID_Replace[:-1]
    sql_file_data = sql_file_data.replace('CardID', CardID_Replace)
    
    
    return sql_file_data



def sql_write_to_file(sql_file_name, sql_file_data):
    from .configs import Config_Read, Config_Path
    import easygui
    import os
    
    if '.' in sql_file_name:
        dot_index = sql_file_name.index('.')
        sql_file_name = sql_file_name[:dot_index] + '.sql'
    else:
        print('You need to revise your \'sql_write_to_file()\' \'if\' statements, dumbass')
    
    config = Config_Read()
    ### Checks the config for the saved JSON save location, if it doesn't exist it creates it so the next time it opens in the same spot.
    if config.has_option('DEFAULT', 'SQL_Save_Location'):
        
        filepath = config.get('DEFAULT', 'SQL_Save_Location')
        sql_file_name = easygui.filesavebox(msg='Input the name of your SQL', default=filepath + '\\' + sql_file_name + '.sql', filetypes=['*.sql'])
        
        if sql_file_name and '.sql' in sql_file_name:
            directory_path = os.path.dirname(sql_file_name)
            # file_name = os.path.basename(json_file)

            if directory_path != filepath:
                config.set('DEFAULT', 'SQL_Save_Location', directory_path)
                with open(Config_Path(), 'w') as config_file:
                    config.write(config_file)


            with open(f"{sql_file_name}", "w") as sql_file:
                sql_file.write(sql_file_data)
    else:
                
        sql_file_name = easygui.filesavebox(msg='Input the name of your SQL', default=f'{sql_file_name}.sql', filetypes=['*.sql'])
        if sql_file_name and '.sql' in sql_file_name:
            # Extract the directory path and file name
            directory_path = os.path.dirname(sql_file_name)
            file_name = os.path.basename(sql_file_name)

            config.set('DEFAULT', 'SQL_Save_Location', directory_path)
            with open(Config_Path(), 'w') as config_file:
                config.write(config_file)
                
            with open(f"{sql_file_name}", "w") as sql_file:
                sql_file.write(sql_file_data)

    
    # with open(sql_file_name, 'w', encoding='utf-8') as f:
    #     filedata = sql_file_data
    #     # print(filedata)
    #     # filedata.encode('utf-8', errors='ignore')
    #     f.write(filedata)

def replace_whitespace_55(description):
    # modified_text = re.sub(r"(.{55}) {2}", r"\1\n", text)
    description = description.replace('\r', '').replace('\n', '').replace('\'', '\'\'')
    modified_text = re.sub(r"(.{55}) ", r"\1 ' || char(10) ||\n\t\t'", description)
    return modified_text

def replace_whitespace_45(description):
    # modified_text = re.sub(r"(.{55}) {2}", r"\1\n", text)
    description = description.replace('\r', '').replace('\n', '').replace('\'', '\'\'')
    modified_text = re.sub(r"(.{45}) ", r"\1 ' || char(10) ||\n\t\t'", description)
    return modified_text

def replace_whitespace_modified(description):
    # remove carriage returns, escape quotes for SQL strings
    description = description.replace('\r', '').replace("'", "''")

    # replace actual newlines with formatted SQL newline break
    modified_text = description.replace(
        "\n",
        "' || char(10) ||\n\t\t'"
    )

    return modified_text

def Categories_Output():
    Cat_Icons_Activated = Categories_Activated.Cats
    num_of_cards = Card_Checker()
    categories =     f'''\n\t-- Card Categories
    \tINSERT OR REPLACE INTO card_card_categories (id, card_id, card_category_id, num, created_at, updated_at)
    \tVALUES'''
    
    for cards in range(num_of_cards):
        if Categories_Activated.card_categories_dict[cards]:
            CardID0 = get_value(Card.row_names[0] + '_Card_' + str(cards) + '_Row_' + '0')
            CardID1 = get_value(Card.row_names[0] + '_Card_' + str(cards) + '_Row_' + '1')
            RowID0 = int(CardID0 + '000')
            RowID1 = int(CardID1 + '000')
            card_categories = Categories_Activated.card_categories_dict[cards]
            for i in range(len(card_categories)):
                RowID0 += 1
                categories_row = f'\n\t\t({str(RowID0)},{str(CardID0)},{card_categories[i]},{i + 1}, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),'
                categories += categories_row

            categories += '\n'

            for i in range(len(card_categories)):
                RowID1 += 1
                categories_row = f'\n\t\t({str(RowID1)},{str(CardID1)},{card_categories[i]},{i + 1}, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),'
                categories += categories_row


            categories += '\n\n'
            
            
            if num_of_cards - 1 == cards:
                categories = categories[:-3] + ';'
                
        else:
            categories = ''
        
    return categories


def Card_Output():
    Card_ID = ''
    cards = Widget_Value_Grabber(class_name=Card)
    text = f'''\n\t-- Cards
    \tINSERT OR REPLACE INTO cards ("id", "name", "character_id", "card_unique_info_id", "cost", "rarity", "hp_init", "hp_max", "atk_init", "atk_max", "def_init", "def_max", "element", "lv_max", "skill_lv_max", "grow_type", "optimal_awakening_grow_type", "price", "exp_type", "training_exp", "special_motion", "passive_skill_set_id", "leader_skill_set_id", "link_skill1_id", "link_skill2_id", "link_skill3_id", "link_skill4_id", "link_skill5_id", "link_skill6_id", "link_skill7_id", "eball_mod_min", "eball_mod_num100", "eball_mod_mid", "eball_mod_mid_num", "eball_mod_max", "eball_mod_max_num", "max_level_reward_id", "max_level_reward_type", "collectable_type", "face_x", "face_y", "aura_id", "aura_scale", "aura_offset_x", "aura_offset_y", "is_aura_front", "is_selling_only", "awakening_number", "resource_id", "bg_effect_id", "selling_exchange_point", "awakening_element_type", "potential_board_id", "open_at", "created_at", "updated_at")
    \tVALUES'''
    
    if len(Card_Checks.card_ids) == 1:
        Card_ID = get_value(Card.row_names[1] + '_Card_0_Row_0')[:-1]
        
    for card_rows in range(len(cards)):

        cards[card_rows][1] = f'\'{cards[card_rows][1]}\''
        
        ### Rarity Combo Check and Conversion
        if cards[card_rows][5] == '(LR)':
            cards[card_rows][5] = '5'
        elif cards[card_rows][5] == '(TUR)':
            cards[card_rows][5] = '4'
        elif cards[card_rows][5] == '(SSR)':
            cards[card_rows][5] = '3'
        elif cards[card_rows][5] == '(SR)':
            cards[card_rows][5] = '2'
        elif cards[card_rows][5] == '(R)':
            cards[card_rows][5] = '1'
        elif cards[card_rows][5] == '(N)':
            cards[card_rows][5] = '0'
            
        ### Element Combo Check and Conversion
        if cards[card_rows][12] == 'AGL':
            cards[card_rows][12] = '0'
        elif cards[card_rows][12] == 'TEQ':
            cards[card_rows][12] = '1'
        elif cards[card_rows][12] == 'INT':
            cards[card_rows][12] = '2'
        elif cards[card_rows][12] == 'STR':
            cards[card_rows][12] = '3'
        elif cards[card_rows][12] == 'PHY':
            cards[card_rows][12] = '4'
        elif cards[card_rows][12] == 'Super AGL':
            cards[card_rows][12] = '10'
        elif cards[card_rows][12] == 'Super TEQ':
            cards[card_rows][12] = '11'
        elif cards[card_rows][12] == 'Super INT':
            cards[card_rows][12] = '12'
        elif cards[card_rows][12] == 'Super STR':
            cards[card_rows][12] = '13'
        elif cards[card_rows][12] == 'Super PHY':
            cards[card_rows][12] = '14'
        elif cards[card_rows][12] == 'Extreme AGL':
            cards[card_rows][12] = '20'
        elif cards[card_rows][12] == 'Extreme TEQ':
            cards[card_rows][12] = '21'
        elif cards[card_rows][12] == 'Extreme INT':
            cards[card_rows][12] = '22'
        elif cards[card_rows][12] == 'Extreme STR':
            cards[card_rows][12] = '23'
        elif cards[card_rows][12] == 'Extreme PHY':
            cards[card_rows][12] = '24'
        
        ### Quick check for the link number using a char isdigit() loop
        link_skill_columns = [23, 24, 25, 26, 27, 28, 29]
        link_skill_numbers = []
        num = ''
        for item in link_skill_columns:
            for char in cards[card_rows][item]:
                if char.isdigit():
                    num += char
                else:
                    link_skill_numbers.append(num)
                    num = ''
                    break
        x = 0
        for items in link_skill_columns:
            if not link_skill_numbers[x]:
                cards[card_rows][items] = 'NULL'
            else:
                cards[card_rows][items] = link_skill_numbers[x]
            x += 1
        
        ### Potential Board Check
        if cards[card_rows][52] == '+3k to stats':
            # Element Check
            if cards[card_rows][12] in ('0','10','20'):
                cards[card_rows][52] = '10'
            elif cards[card_rows][12] in ('1','11','21'):
                cards[card_rows][52] = '11'
            elif cards[card_rows][12] in ('2','12','22'):
                cards[card_rows][52] = '12'
            elif cards[card_rows][12] in ('3','13','23'):
                cards[card_rows][52] = '13'
            elif cards[card_rows][12] in ('4','14','24'):
                cards[card_rows][52] = '14'
                
        elif cards[card_rows][52] == '+5k to stats':
            if cards[card_rows][12] in ('0','10','20'):
                cards[card_rows][52] = '20'
            elif cards[card_rows][12] in ('1','11','21'):
                cards[card_rows][52] = '21'
            elif cards[card_rows][12] in ('2','12','22'):
                cards[card_rows][52] = '22'
            elif cards[card_rows][12] in ('3','13','23'):
                cards[card_rows][52] = '23'
            elif cards[card_rows][12] in ('4','14','24'):
                cards[card_rows][52] = '24'
                
        elif cards[card_rows][52] == '+7k to stats':
            if cards[card_rows][12] in ('0','10','20'):
                cards[card_rows][52] = '30'
            elif cards[card_rows][12] in ('1','11','21'):
                cards[card_rows][52] = '31'
            elif cards[card_rows][12] in ('2','12','22'):
                cards[card_rows][52] = '32'
            elif cards[card_rows][12] in ('3','13','23'):
                cards[card_rows][52] = '33'
            elif cards[card_rows][12] in ('4','14','24'):
                cards[card_rows][52] = '34'
        
            
        
        card_values = ', '.join(map(str, cards[card_rows]))  # Convert card values to a comma-separated string
        card_sql = f'\n\t\t({card_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
        if card_rows % 2 == 0:
            text += card_sql
        else:
            text += card_sql + '\n'
            
    # Making the last SQL row have a semicolon
    text = text[:-2] + ';'
    
    # print(text)
    return text

def Optimal_Awakening_Growth_Output():
    optimal_awakening_growth_text =f'''\n\t\tINSERT OR REPLACE INTO optimal_awakening_growths ("id", "optimal_awakening_grow_type", "step", "lv_max", "skill_lv_max", "passive_skill_set_id", "leader_skill_set_id")
    \tVALUES'''
    cards = Card_Checker()
    for card in range(cards):
        if get_value(f'EZA_Checkbox_{card}'):
            CardID = get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '1')
            CardID0 = get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '0')
            if get_value(Card.row_names[5] + '_Card_' + str(card) + '_Row_' + '1') == '(LR)':
                optimal_awakening_growth_sql = f'\n\t\t({CardID}, {CardID0}, 1, 150, 25, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 1)}, {CardID0}, 2, 150, 25, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 2)}, {CardID0}, 3, 150, 25, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_text += optimal_awakening_growth_sql
            else:
                optimal_awakening_growth_sql = f'\n\t\t({CardID}, {CardID0}, 1, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 1)}, {CardID0}, 2, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 2)}, {CardID0}, 3, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 3)}, {CardID0}, 4, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 4)}, {CardID0}, 5, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 5)}, {CardID0}, 6, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 6)}, {CardID0}, 7, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_text += optimal_awakening_growth_sql
                
            if cards - 1 == card:
                optimal_awakening_growth_text = optimal_awakening_growth_text[:-1] + ';'

        elif get_value(f'Super_EZA_Checkbox_{card}'):
            CardID = get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '1')
            CardID0 = get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '0')
            if get_value(Card.row_names[5] + '_Card_' + str(card) + '_Row_' + '1') == '(LR)':
                optimal_awakening_growth_sql = f'\n\t\t({CardID}, {CardID0}, 1, 150, 25, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 1)}, {CardID0}, 2, 150, 25, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 2)}, {CardID0}, 3, 150, 25, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 3)}, {CardID0}, 4, 150, 25, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_text += optimal_awakening_growth_sql
            else:
                optimal_awakening_growth_sql = f'\n\t\t({CardID}, {CardID0}, 1, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 1)}, {CardID0}, 2, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 2)}, {CardID0}, 3, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 3)}, {CardID0}, 4, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 4)}, {CardID0}, 5, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 5)}, {CardID0}, 6, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 6)}, {CardID0}, 7, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_sql += f'\n\t\t({str(int(CardID) + 7)}, {CardID0}, 8, 140, 15, {CardID[:-1]}, {CardID}),'
                optimal_awakening_growth_text += optimal_awakening_growth_sql

            if cards - 1 == card:
                optimal_awakening_growth_text = optimal_awakening_growth_text[:-1] + ';'
                
    if len(optimal_awakening_growth_text) < 200:
        optimal_awakening_growth_text = ''

            
    return optimal_awakening_growth_text

def Passive_Output():
    num_of_cards = Card_Checker()
    
    # passive_skills = Widget_Value_Grabber(class_name=Passive_Skill, combo=True, combo_tag=Passive_Skill.row_names[2])
    passive = f'''\n\t\tINSERT OR REPLACE INTO passive_skills ("id", "name", "exec_timing_type", "efficacy_type", "target_type", "sub_target_type_set_id", "passive_skill_effect_id", "calc_option", "turn", "is_once", "probability", "causality_conditions", "eff_value1", "eff_value2", "eff_value3", "efficacy_values", "created_at", "updated_at")
    \tVALUES'''
    
    passive_set = f'''\n\t-- Passive Skill (passive_skill_sets, passive_skill_effects, passive_skills, passive_skill_set_relations, transformation_descriptions)
    \tINSERT OR REPLACE INTO passive_skill_sets ("id", "name", "itemized_description", "created_at", "updated_at")
    \tVALUES'''
    
    passive_relations = f'''\n\t\tINSERT OR REPLACE INTO passive_skill_set_relations ("id", "passive_skill_set_id", "passive_skill_id", "created_at", "updated_at")
    \tVALUES'''
    
    passive_skill_effects = f'''\n\t-- Passive Skill Effect
    \tINSERT OR REPLACE INTO passive_skill_effects ("id", "script_name", "lite_flicker_rate", "bgm_id", "created_at", "updated_at")
    \tVALUES'''
    passive_desc = []
    
    for i in range(num_of_cards):
        # print(get_value(f'Passive_Desc_Text_Input_{i}'))
        # passive_desc.append(replace_whitespace_55(get_value(f'Passive_Desc_Text_Input_{i}')))
        passive_desc.append(replace_whitespace_modified(get_value(f'Passive_Desc_Text_Input_{i}')))
        # passive_desc.append(get_value(f'Passive_Desc_Text_Input_{i}'))

    for cards in range(num_of_cards):
        Row_ID = get_value(Card.row_names[0] + '_Card_' + str(cards) + '_Row_' + '1')[:-1]
        passive_name = get_value(Passive_Skill.row_names[0] + '_Card_' + str(cards) + '_Row_' + '0').replace('\'', '\'\'')
        passive_set_sql = f'\n\t\t({Row_ID}, \'{passive_name}\', \'{passive_desc[cards]}\', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
        passive_set += passive_set_sql + '\n'
        
        Passive_ID = int(get_value(Card.row_names[0] + '_Card_' + str(cards) + '_Row_' + '1'))
        num_of_skills = Row_Checker(Passive_Skill.row_names[i] + '_Card_' + str(cards) + '_Row_')
        for rows in range(num_of_skills):
            passive_values = [re.sub(r'\D', '', get_value(Passive_Skill.row_names[i] + '_Card_' + str(cards) + '_Row_' + str(rows))) if Passive_Skill.row_names[i] == Passive_Skill.row_names[2] else get_value(Passive_Skill.row_names[i] + '_Card_' + str(cards) + '_Row_' + str(rows)) for i in range(len(Passive_Skill.row_names))]
            passive_values[0] = passive_values[0].replace('\'', '\'\'')
            passive_values[0] = f'\'{passive_values[0]}\''
            
            if passive_values[10] != 'NULL':
                passive_values[10] = f'\'{passive_values[10]}\''
                
            passive_values[14] = f'\'{passive_values[14]}\''
            
            ### Add a period to the list for passive descriptions
            # passive_values.insert(1, '\'.\'')
            
            passive_values = ', '.join(map(str, passive_values))
            passive_sql = f'\n\t\t({str(Passive_ID + rows)}, {passive_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
            passive += passive_sql
            
            passive_relations_sql = f'\n\t\t({str(Passive_ID + rows)}, {Row_ID}, {str(Passive_ID + rows)}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
            passive_relations += passive_relations_sql
        passive += '\n'
        passive_relations += '\n'
        
    # Making the last SQL row have a semicolon
    passive = passive[:-2] + ';'
    passive_relations = passive_relations[:-2] + ';'
    passive_set = passive_set[:-2] + ';'
    
    
    return passive, passive_relations, passive_set

def Specials_Output():
    num_of_cards = Card_Checker()
    # Card_ID0 = int(get_value('CardID0'))
    # Card_ID1 = int(get_value('CardID1'))
    
    
    card_specials_text = f'''\n\t-- Specials (card_specials, specials, special_sets, special_views)
    \tINSERT OR REPLACE INTO card_specials ("id", "card_id", "special_set_id", "priority", "style", "lv_start", "eball_num_start", "view_id", "card_costume_condition_id", "special_bonus_id1", "special_bonus_lv1", "bonus_view_id1", "special_bonus_id2", "special_bonus_lv2", "bonus_view_id2", "causality_conditions", "special_asset_id", "created_at", "updated_at")
    \tVALUES'''
    
    special_set_text = f'''\n\t\tINSERT OR REPLACE INTO special_sets ("id", "name", "description", "causality_description", "aim_target", "increase_rate", "lv_bonus", "is_inactive", "created_at", "updated_at")
    \tVALUES'''
    
    special_skills_text = f'''\n\t\tINSERT OR REPLACE INTO specials ("id", "special_set_id", "type", "efficacy_type", "target_type", "calc_option", "turn", "prob", "causality_conditions", "eff_value1", "eff_value2", "eff_value3", "created_at", "updated_at")
    \tVALUES'''
    # special_set_desc = []
    # special_set_cond = []
    # for i in range(num_of_cards):
    
        
    for cards in range(num_of_cards):
        CardID0 = int(get_value(Card.row_names[0] + '_Card_' + str(cards) + '_Row_' + '0'))
        CardID1 = int(get_value(Card.row_names[0] + '_Card_' + str(cards) + '_Row_' + '1'))
        Special_Set_ID = CardID1
        number_of_specials = Row_Checker(f'Special_Set_Name_Input_Card_{cards}_')
        Row_ID = int(get_value(Card.row_names[0] + '_Card_' + str(cards) + '_Row_' + '1'))
        card_special_row_id = int(get_value(Card.row_names[0] + '_Card_' + str(cards) + '_Row_' + '1'))
        special_skill_row_id = int(get_value(Card.row_names[0] + '_Card_' + str(cards) + '_Row_' + '1'))
        
        for special_num in range(number_of_specials):
            special_sets_values = [f'Special_Set_Aim_Target_Input_Card_{cards}_{special_num}', f'Special_Set_Increase_Rate_Input_Card_{cards}_{special_num}', f'Special_Set_Level_Bonus_Input_Card_{cards}_{special_num}']
        
            special_set_name = get_value(f'Special_Set_Name_Input_Card_{cards}_{special_num}').replace('\'', '\'\'')
            special_set_desc = (replace_whitespace_45(get_value(f'Special_Set_Desc_Input_Card_{cards}_{special_num}')))
            special_set_cond = (replace_whitespace_45(get_value(f'Special_Set_Cond_Input_Card_{cards}_{special_num}')))
            special_set_values = [get_value(special_sets_values[i]) for i in range(len(special_sets_values))]
            special_set_values = ', '.join(map(str, special_set_values))
            # print(special_values)
            
            
            special_set_sql = f'\n\t\t({str(Row_ID)}, \'{special_set_name}\', \'{special_set_desc}\', \'{special_set_cond}\', {special_set_values}, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
            special_set_text += special_set_sql + '\n'
            Row_ID += 1
            
            
            num_of_rows = Row_Checker(Card_Specials.row_names[0] + '_Card_' + str(cards) + '_Row_' + str(special_num))
            for rows in range(num_of_rows):
                card_special_row = ([get_value(Card_Specials.row_names[i] + '_Card_' + str(cards) + '_Row_' + str(special_num) + str(rows)) for i in range(len(Card_Specials.row_names))])
                card_special_row[1] = f'\'{card_special_row[1]}\''
                if card_special_row[12] != 'NULL':
                    card_special_row[12] = f'\'{card_special_row[12]}\''
                card_specials_values = ', '.join(map(str, card_special_row))
                
                if rows % 2 == 0:
                    # print('First Option')
                    card_specials_sql = f'\n\t\t({str(card_special_row_id)}, {str(CardID0)}, {str(Special_Set_ID)}, {card_specials_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                    card_specials_text += card_specials_sql
                    card_special_row_id += 1
                    # 
                else:
                    card_specials_sql = f'\n\t\t({str(card_special_row_id)}, {str(CardID1)}, {str(Special_Set_ID)}, {card_specials_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                    card_specials_text += card_specials_sql + '\n'
                    card_special_row_id += 1
                    Special_Set_ID += 1
                    
            num_of_rows = Row_Checker(Specials.row_names[0] + '_Card_' + str(cards) + '_Row_' + str(special_num))
            Special_Set_ID_ = CardID1
            for rows in range(num_of_rows):
                
                special_skill_row = [re.sub(r'\D', '', get_value(Specials.row_names[i] + '_Card_' + str(cards) + '_Row_' + str(special_num) + str(rows))) if Specials.row_names[i] == Specials.row_names[1] else get_value(Specials.row_names[i] + '_Card_' + str(cards) + '_Row_' + str(special_num) + str(rows)) for i in range(len(Specials.row_names))]
                special_skill_row[0] = f'\'{special_skill_row[0]}\''
                special_skills_values = ', '.join(map(str, special_skill_row))
                
                special_skill_sql = f'\n\t\t({str(special_skill_row_id)}, {str(Special_Set_ID_ + special_num)}, {special_skills_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                special_skills_text += special_skill_sql
                special_skill_row_id += 1
            
            special_skills_text += '\n'
            
    special_set_text = special_set_text[:-2] + ';'
    card_specials_text = card_specials_text[:-2] + ';'
    special_skills_text = special_skills_text[:-2] + ';'

    special_skills_text = check_sql_endings(special_skills_text)
    # print(special_set_text)
    # print(card_specials_text)
    # print(special_skills_text)
    
    return card_specials_text, special_set_text, special_skills_text



################################################################################################################################################################
def Active_Skill_Output():
    active_skill_text = f'''\n\t\tINSERT OR REPLACE INTO active_skills ("id", "active_skill_set_id", "target_type", "sub_target_type_set_id", "calc_option", "efficacy_type", "eff_val1", "eff_val2", "eff_val3", "efficacy_values", "thumb_effect_id", "effect_se_id", "created_at", "updated_at")
    \tVALUES '''
    active_skill_set_text = f'''\n\t\tINSERT OR REPLACE INTO active_skill_sets ("id", "name", "effect_description", "condition_description", "turn", "exec_limit", "causality_conditions", "ultimate_special_id", "special_view_id", "costume_special_view_id", "bgm_id", "created_at", "updated_at")
    \tVALUES'''
    card_active_skill_text = f'''\n\t-- Active Skill
    \tINSERT OR REPLACE INTO card_active_skills ("id", "card_id", "active_skill_set_id", "created_at", "updated_at")
    \tVALUES'''

    
    
    num_of_cards = Card_Checker()
    number_of_active_skills = 0
    
    for card in range(num_of_cards):
        if does_alias_exist(f'Active_Skill_Text_Card_{card}'):
            number_of_active_skills += 1
            
    # for card in range(num_of_cards):
            Row_ID = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '1'))
            
            # Active Skill Set
            active_skill_set_name = get_value(f'Active_Name_Card_{card}').replace('\'', '\'\'')
            active_skill_set_desc = replace_whitespace_45(get_value(f'Active_Desc_Card_{card}'))
            active_skill_set_cond = replace_whitespace_45(get_value(f'Active_Cond_Card_{card}'))
            active_skill_values = [get_value(Active_Skill_Set.row_names[i] + '_Card_' + str(card) + '_Row_0') for i in range(len(Active_Skill_Set.row_names))]
            if active_skill_values[2] != 'NULL':
                active_skill_values[2] = f'\'{active_skill_values[2]}\''
                
                
            active_skill_values = ', '.join(map(str, active_skill_values))
            
            active_skill_set_sql = f'\n\t\t({str(Row_ID)}, \'{active_skill_set_name}\', \'{active_skill_set_desc}\', \'{active_skill_set_cond}\', {active_skill_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
            active_skill_set_text += active_skill_set_sql + '\n'
    
            # Active Skills
            active_skill_set_id = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '1'))
            active_skill_rows = Row_Checker(Active_Skill.row_names[0] + '_Card_' + str(card) + '_Row_')
            for rows in range(active_skill_rows):
                active_skill_values = [re.sub(r'\D', '', get_value(Active_Skill.row_names[i] + '_Card_' + str(card) + '_Row_' + str(rows))) if Active_Skill.row_names[i] == Active_Skill.row_names[3] else get_value(Active_Skill.row_names[i] + '_Card_' + str(card) + '_Row_' + str(rows)) for i in range(len(Active_Skill.row_names))]
                # active_skill_values = [get_value(Active_Skill.row_names[i] + '_Card_' + str(card) + '_Row_' + str(rows)) for i in range(len(Active_Skill.row_names))]
                active_skill_values[7] = f'\'{active_skill_values[7]}\''
                active_skill_values = ', '.join(map(str, active_skill_values))  # Convert card values to a comma-separated string
                active_skill_sql = f'\n\t\t({str(active_skill_set_id + rows)}, {str(active_skill_set_id)}, {active_skill_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                active_skill_text += active_skill_sql
            active_skill_text += '\n'
            
            # Card Active Skill
            card_active_card_id = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '0'))
            for i in range(2):
                card_active_skill_sql = f'\n\t\t({str(card_active_card_id + i)}, {str(card_active_card_id + i)}, {active_skill_set_id}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                card_active_skill_text += card_active_skill_sql
            card_active_skill_text += '\n'
            
            # Ultimate Special
                # ultimate_row_id = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '1'))
                # ultimate_values = []
                # for i in range(4):
                #     ultimate_values.append(get_value(Active_Skill.ultimate_names[i] + '_Card_' + str(card)))
                # ultimate_special_sql = f'\n\t\t({ultimate_row_id}, \'{ultimate_values[0]}\', \'{ultimate_values[1]}\', {ultimate_values[2]}, {ultimate_values[3]}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                # ultimate_special_text += ultimate_special_sql + '\n'
            # else:
                # ultimate_special_text = ''
        

        
    card_active_skill_text = card_active_skill_text[:-2] + ';'
    active_skill_set_text = active_skill_set_text[:-2] + ';'
    active_skill_text = active_skill_text[:-2] + ';'
    
    ### Happens when a dokkan field has an active skill with nothing
    if len(active_skill_text) < 280:
        active_skill_text = ''
    
    return active_skill_set_text, active_skill_text, card_active_skill_text
################################################################################################################################################################
def Ultimate_Special_Output():
    ultimate_special_text = f'''\t-- Ultimate Specials
    \tINSERT OR REPLACE INTO ultimate_specials ("id", "name", "description", "increase_rate", "aim_target", "created_at", "updated_at")
    \tVALUES'''
    ultimate_special_text_check = ultimate_special_text
    
    num_of_cards = Card_Checker()
    
    for card in range(num_of_cards):
        if does_alias_exist(Active_Skill.ultimate_names[0] + '_Card_' + str(card)):
            ultimate_row_id = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '1'))
            ultimate_values = []
            for i in range(4):
                ultimate_values.append(get_value(Active_Skill.ultimate_names[i] + '_Card_' + str(card)))
            ultimate_special_sql = f'\n\t\t({ultimate_row_id}, \'{ultimate_values[0]}\', \'{ultimate_values[1]}\', {ultimate_values[2]}, {ultimate_values[3]}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
            ultimate_special_text += ultimate_special_sql + '\n'
            
    if ultimate_special_text_check == ultimate_special_text:
        ultimate_special_text = ''
    else:
        ultimate_special_text = ultimate_special_text[:-2] + ';'
    print(ultimate_special_text)
    return ultimate_special_text
            
################################################################################################################################################################
def Leader_Output():
    leader_skill_sub_target_set_ids = []
    leader_skill_set_text = f'''\n\t-- Leader Skill
    \tINSERT OR REPLACE INTO leader_skill_sets ("id", "name", "description", "created_at", "updated_at")
    \tVALUES'''
    leader_skill_text = f'''\t\tINSERT OR REPLACE INTO leader_skills ("id", "leader_skill_set_id", "exec_timing_type", "target_type", "sub_target_type_set_id", "causality_conditions", "efficacy_type", "efficacy_values", "calc_option", "created_at", "updated_at")
    \tVALUES'''
    sub_target_type_text = f'''\tINSERT OR REPLACE INTO sub_target_types ("id", "sub_target_type_set_id", "target_value_type", "target_value", "created_at", "updated_at")
    \tVALUES'''
    sub_target_type_set_text = f'''\tINSERT OR REPLACE INTO sub_target_type_sets ("id", "created_at", "updated_at")
    \tVALUES'''
    for card in range(Card_Checker()):
        leader_skill = []
        if does_alias_exist(f'Leader_Skill_Text_{card}'):
            card = str(card)
            leader_skill_rows = Row_Checker(Leader_Skill_Info.row_names[0] + '_Card_' + card + '_Row_')
            for t in range(leader_skill_rows):
                # print(Leader_Skill_Info.row_names[0] + '0' + str(t))
                leader_skill.append([get_value(Leader_Skill_Info.row_names[i] + '_Card_' + card + '_Row_' + str(t)) for i in range(len(Leader_Skill_Info.row_names))])
                leader_skill_sub_target_set_ids.append(get_value(Leader_Skill_Info.row_names[3] + '_Card_' + card + '_Row_' + str(t)))

            leader_name = get_value(f'Leader_Name_Text_Input_{card}').replace('\'', '\'\'')
            leader_desc = replace_whitespace_45(get_value(f'Leader_Desc_Text_Input_{card}').replace('\'', '\'\''))
            leader_set_id = get_value(Card.row_names[0] + '_Card_' + card + '_Row_' + '1')
            
            leader_skill_set_sql = f'\n\t\t({str(leader_set_id)}, \'{leader_name}\', \'{leader_desc}\', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
            leader_skill_set_text += leader_skill_set_sql + '\n'

            for rows in range(Row_Checker(Leader_Skill_Info.row_names[0] + '_Card_' + card + '_Row_')):

                leader_skill[rows][5] = f'\'{leader_skill[rows][5]}\''
                print(leader_skill[rows][5])
                if leader_skill[rows][3] == '0':
                    leader_skill[rows][3] = 'NULL'
                
                leader_skill_values = ', '.join(map(str, leader_skill[rows]))  # Convert card values to a comma-separated string
                leader_skill_sql = f'\n\t\t({str(int(leader_set_id) + int(rows))}, {leader_set_id}, {leader_skill_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                leader_skill_text += leader_skill_sql
            
            leader_skill_text += '\n'
            
            #################################################################################
            leader_skill_categories_ids = []
            leader_skill_combo_lists = Row_Checker(f'Leader_Skill_Category_Selection_{card}_')
            # Based on the category selection combo lists
            for category_combos in range(leader_skill_combo_lists):
                # Removing everything but the number from the combo list value
                match = re.search(r'\((\d+)\)', get_value(f'Leader_Skill_Category_Selection_{card}_{category_combos}'))

                if match:
                    number_in_parentheses = match.group(1)
                    leader_skill_categories_ids.append(number_in_parentheses)
                else:
                    print("No match found.")
                # leader_skill_categories_ids.append(re.sub(r'\D', '', get_value(f'Leader_Skill_Category_Selection_{category_combos}')))

            Row_ID = int(get_value(Card.row_names[0] + '_Card_' + card + '_Row_' + '1'))
            leader_skill_set_id = str(Row_ID)
            leader_skill_preset_selection = get_value(f'Leader_Skill_Preset_List_{card}')
            # print(leader_skill_preset_selection)
            category_list_1 = ['cat1', 'cat1', 'cat2', 'cat1', 'extra1', 'cat1', 'cat2', 'extra1']
            target_value_Type_1 = ['1','2','1','1','1','2','1','1']


            # print(leader_skill_categories_ids)
            try:
                # 3 Categories & 2 Extra & 1 Class (3 Categories Excluded)
                if Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection] == 30:
                
                    sub_target_type_set_ids = ['leadid11','leadid12','leadid12','leadid13','leadid13','leadid13','leadid14','leadid14','leadid15','leadid15','leadid15','leadid16','leadid16','leadid16','leadid17','leadid17','leadid17','leadid17','leadid18','leadid18','leadid18','leadid18','leadid19','leadid19','leadid19','leadid19','leadid19','leadid20','leadid20','leadid20']
                    target_value_type = ['1','1','2','1','2','2','1','1','1','1','2','1','1','2','1','1','2','2','1','1','2','2','1','1','2','2','2','2','2','2']
                    category_list = ['cat1','cat2','cat1','cat3','cat1','cat2','cat1','extra1','cat1','extra2','extra1','cat2','extra1','cat1','cat2','extra2','cat1','extra1','cat3','extra1','cat1','cat2','cat3','extra2','cat1','cat2','extra1','cat1','cat2','cat3']

                    for i in range(Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection]):
                        sub_target_type_sql = f'\n\t\t({Row_ID}, {sub_target_type_set_ids[i]}, {target_value_type[i]}, {category_list[i]}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                        sub_target_type_text += sub_target_type_sql
                        Row_ID += 1

                    sub_target_type_text = sub_target_type_text.replace('leadid', leader_skill_set_id[:-1]).replace('cat1', leader_skill_categories_ids[0]).replace('cat2', leader_skill_categories_ids[1]).replace('cat3', leader_skill_categories_ids[2]).replace('extra1', leader_skill_categories_ids[3]).replace('extra2', leader_skill_categories_ids[4]) + '\n'

                    sub_target_type_set_text = Create_Sub_Target_Type_Set(10)

                # 3 Categories 2 Extra
                elif Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection] == 27:
                
                    sub_target_type_set_ids = ['leadid1','leadid2','leadid2','leadid3','leadid3','leadid3','leadid4','leadid4','leadid5','leadid5','leadid5','leadid6','leadid6','leadid6','leadid7','leadid7','leadid7','leadid7','leadid8','leadid8','leadid8','leadid8','leadid9','leadid9','leadid9','leadid9','leadid9']
                    target_value_type = ['1','1','2','2','2','1','1','1','1','2','1','2','1','1','2','1','2','1','2','2','1','1','2','2','1','2','1']
                    category_list = ['cat1', 'cat2', 'cat1', 'cat1', 'cat2', 'cat3', 'cat1', 'extra1', 'cat1', 'extra1', 'extra2', 'cat1', 'cat2', 'extra1', 'cat1', 'cat2', 'extra1', 'extra2', 'cat1', 'cat2', 'cat3', 'extra1', 'cat1', 'cat2', 'cat3', 'extra1', 'extra2']

                    for i in range(Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection]):
                        sub_target_type_sql = f'\n\t\t({Row_ID}, {sub_target_type_set_ids[i]}, {target_value_type[i]}, {category_list[i]}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                        sub_target_type_text += sub_target_type_sql
                        Row_ID += 1
                    sub_target_type_text = sub_target_type_text.replace('leadid', leader_skill_set_id).replace('cat1', leader_skill_categories_ids[0]).replace('cat2', leader_skill_categories_ids[1]).replace('cat3', leader_skill_categories_ids[2]).replace('extra1', leader_skill_categories_ids[3]).replace('extra2', leader_skill_categories_ids[4]) + '\n'

                    sub_target_type_set_text = Create_Sub_Target_Type_Set(9)

                # 2 Categories 2 Extra
                elif Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection] == 15:
                    sub_target_type_set_ids = ['leadid1','leadid2','leadid2','leadid3','leadid3','leadid4','leadid4','leadid4','leadid5','leadid5','leadid5','leadid5','leadid6','leadid6','leadid6']
                    target_value_type = ['1','2','1','1','1','1','2','1','2','1','1','2','1','2','1']
                    category_list = ['cat1','cat1','cat2','cat1','extra1','cat1','extra1','extra2','cat1','cat2','extra1','extra2','cat2','cat1','extra2']


                    for i in range(Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection]):
                        sub_target_type_sql = f'\n\t\t({Row_ID}, {sub_target_type_set_ids[i]}, {target_value_type[i]}, {category_list[i]}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                        sub_target_type_text += sub_target_type_sql
                        Row_ID += 1

                    sub_target_type_text = sub_target_type_text.replace('leadid', leader_skill_set_id).replace('cat1', leader_skill_categories_ids[0]).replace('cat2', leader_skill_categories_ids[1]).replace('extra1', leader_skill_categories_ids[2]).replace('extra2', leader_skill_categories_ids[3]) + '\n'

                    sub_target_type_set_text = Create_Sub_Target_Type_Set(6)

                # 2 Categories 1 Extra
                elif Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection] == 8: 
                    sub_target_type_set_ids = ['leadid1','leadid2','leadid2','leadid3','leadid3','leadid4','leadid4','leadid4']
                    target_value_type = ['1','2','1','1','1','2','1','1']
                    category_list = ['cat1','cat1','cat2','cat1','extra1','cat1','cat2','extra1']


                    for i in range(Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection]):
                        sub_target_type_sql = f'\n\t\t({Row_ID}, {sub_target_type_set_ids[i]}, {target_value_type[i]}, {category_list[i]}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                        sub_target_type_text += sub_target_type_sql
                        Row_ID += 1

                    sub_target_type_text = sub_target_type_text.replace('leadid', leader_skill_set_id).replace('cat1', leader_skill_categories_ids[0]).replace('cat2', leader_skill_categories_ids[1]).replace('extra1', leader_skill_categories_ids[2]) + '\n'

                    sub_target_type_set_text = Create_Sub_Target_Type_Set(4)

                # 2 Categories    
                elif Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection] == 3:
                    sub_target_type_set_ids = ['leadid1','leadid2','leadid2']
                    target_value_type = ['1','2','1']
                    category_list = ['cat1','cat1','cat2']

                    for i in range(Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection]):
                        sub_target_type_sql = f'\n\t\t({Row_ID}, {sub_target_type_set_ids[i]}, {target_value_type[i]}, {category_list[i]}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                        sub_target_type_text += sub_target_type_sql
                        Row_ID += 1

                    sub_target_type_text = sub_target_type_text.replace('leadid', leader_skill_set_id).replace('cat1', leader_skill_categories_ids[0]).replace('cat2', leader_skill_categories_ids[1]) + '\n'

                    sub_target_type_set_text = Create_Sub_Target_Type_Set(2)

                # 1 Category 1 Element
                elif Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection] == 2:
                    sub_target_type_set_ids = ['leadid1','leadid2']
                    target_value_type = ['1','2']
                    category_list = ['cat1','cat1']

                    for i in range(Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection]):
                        sub_target_type_sql = f'\n\t\t({Row_ID}, {sub_target_type_set_ids[i]}, {target_value_type[i]}, {category_list[i]}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                        sub_target_type_text += sub_target_type_sql
                        Row_ID += 1

                    sub_target_type_text = sub_target_type_text.replace('leadid', leader_skill_set_id).replace('cat1', leader_skill_categories_ids[0]) + '\n'

                    sub_target_type_set_text = Create_Sub_Target_Type_Set(2)

                elif Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection] == 1:
                    sub_target_type_set_ids = ['leadid1']
                    target_value_type = ['1']
                    category_list = ['cat1']

                    for i in range(Leader_Skill_Info.leader_sub_target_types_rows[leader_skill_preset_selection]):
                        sub_target_type_sql = f'\n\t\t({Row_ID}, {sub_target_type_set_ids[i]}, {target_value_type[i]}, {category_list[i]}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                        sub_target_type_text += sub_target_type_sql
                        Row_ID += 1

                    sub_target_type_text = sub_target_type_text.replace('leadid', leader_skill_set_id).replace('cat1', leader_skill_categories_ids[0]) + '\n'

                    sub_target_type_set_text = Create_Sub_Target_Type_Set(1)

                else:
                    sub_target_type_text = ''
                    sub_target_type_set_text = ''
            except Exception as e:
                sub_target_type_text = ''
                sub_target_type_set_text = ''
                set_value('log_1', f'{e} Ignore, means the key wasn\'t leader skill preset doesn\'t need sub_targets')

    if sub_target_type_text: 
        sub_target_type_text = sub_target_type_text[:-1] + ';'
        sub_target_type_set_text = sub_target_type_set_text[:-1] +';'
                
    leader_skill_set_text = leader_skill_set_text[:-2] + ';' + '\n'
    leader_skill_text = leader_skill_text[:-2] + ';'
    sub_target_type_text = sub_target_type_text[:-2] + ';'
    sub_target_type_set_text = sub_target_type_set_text[:-1] + ';'
    
    if sub_target_type_text == ';':
        sub_target_type_text = ''
        
    if sub_target_type_set_text == ';':
        sub_target_type_set_text = ''
        
    return leader_skill_set_text, leader_skill_text, sub_target_type_text, sub_target_type_set_text
################################################################################################################################################################
Export = Export()
def Standby_Finish_Output():
    num_of_cards = Card_Checker()
    standby_skill_set_text = f'''\n\t-- Standby Skill
    \tINSERT OR REPLACE INTO standby_skill_sets ("id", "name", "ingame_icon_path" , "effect_description", "condition_description", "exec_limit", "causality_conditions", "special_view_id", "costume_special_view_id", "bgm_id", "created_at", "updated_at")
    \tVALUES'''
    
    standby_skills_text = f'''\n\t\tINSERT OR REPLACE INTO standby_skills ("id", "standby_skill_set_id", "target_type", "target_type_values", "sub_target_type_set_id", "turn", "efficacy_type", "calc_option", "efficacy_values", "thumb_effect_id", "effect_se_id", "created_at", "updated_at")
    \tVALUES'''
    
    standby_skill_set_finish_skills_set_relations_text = f'''\n\t\tINSERT OR REPLACE INTO standby_skill_set_finish_skill_set_relations ("id", "standby_skill_set_id", "finish_skill_set_id", "created_at", "updated_at")
    \tVALUES'''
    
    finish_skill_set_text = f'''\n\t\tINSERT OR REPLACE INTO finish_skill_sets ("id", "name", "effect_description", "condition_description", "dialog_order", "dialog_images", "exec_timing_type", "exec_limit", "causality_conditions", "finish_special_id", "special_view_id", "costume_special_view_id", "bgm_id", "is_dialog_view_visible", "created_at", "updated_at")
    \tVALUES'''
    
    finish_skills_text = f'''\t-- Finish Skill
    \tINSERT OR REPLACE INTO finish_skills ("id", "finish_skill_set_id", "target_type", "target_type_values", "sub_target_type_set_id", "turn", "efficacy_type", "calc_option", "efficacy_values", "thumb_effect_id", "effect_se_id", "created_at", "updated_at")
    \tVALUES'''
    
    card_finish_skills_set_relations_text = f'''\n\t\tINSERT OR REPLACE INTO card_finish_skill_set_relations ("id", "card_id", "finish_skill_set_id", "created_at", "updated_at")
    \tVALUES'''
    
    finish_specials_text =f'''\n\t\tINSERT OR REPLACE INTO finish_specials ("id", "increase_rate", "aim_target", "created_at", "updated_at")
    \tVALUES'''
    
    card_standby_skill_set_relations_text = f'''\t-- Standby/Finish Relations
    \tINSERT OR REPLACE INTO card_standby_skill_set_relations ("id", "card_id", "standby_skill_set_id", "created_at", "updated_at")
	\tVALUES'''
    
    # Standby Skill Sets (If they ever add the possibility of multiple standby skills I'll have to come back here an modify it)(I doubt it happens; they act like actives which is only one per unit or it breaks the unit)
    for card in range(num_of_cards):
        # Check if there is a standby skill
        if does_alias_exist(f'Standby_Skill_Set_Text_{card}_0'):
            num_of_standby_skills = Row_Checker(f'Standby_Skill_Set_Text_{card}_')
            standby_skill_set_id = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '1'))
            
            for standby_skill in range(num_of_standby_skills):
                standby_skill_set_name = replace_whitespace_45(get_value(f'Standby_Set_Name_Input_Text_{card}_{standby_skill}'))
                standby_skill_set_desc = replace_whitespace_45(get_value(f'Standby_Set_Desc_Input_Text_{card}_{standby_skill}'))
                standby_skill_set_cond = replace_whitespace_45(get_value(f'Standby_Set_Cond_Input_Text_{card}_{standby_skill}'))
                # '_Row_00' because there will always be 1 row in Standby Skill Set
                # standby_skill_set_value = [get_value(Standby_Skill_Set.row_names[i] + '_Card_' + str(card) + '_Row_00') for i in range(len(Standby_Skill_Set.row_names))]
                standby_skill_set_values = Export.List_of_Values(Standby_Skill_Set, card=card, skill_number=standby_skill, Row=0, add_quotes=True, quote_indexes=[1])

                # Base game has a standby skill set for both Card IDs, but modders have used just the Card ID ending in 1. We'll see if it messes with UI stuff (may have to revist this)
                for row in range(2):
                    if row == 0:
                        standby_skill_set_sql = f'\n\t\t({standby_skill_set_id - 1}, \'{standby_skill_set_name}\', \'ingame/common/uniqueskill/ing_uniqueskill_icon_1.png\', \'{standby_skill_set_desc}\', \'{standby_skill_set_cond}\', {standby_skill_set_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                        standby_skill_set_text += standby_skill_set_sql
                        standby_skill_set_text += '\n'
                    else:
                        standby_skill_set_sql = f'\n\t\t({standby_skill_set_id}, \'{standby_skill_set_name}\', \'ingame/common/uniqueskill/ing_uniqueskill_icon_1.png\', \'{standby_skill_set_desc}\', \'{standby_skill_set_cond}\', {standby_skill_set_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                        standby_skill_set_text += standby_skill_set_sql
                        standby_skill_set_text += '\n'
                        
                
        # Standby Skills
                standby_skill_table_rows = Row_Checker(Standby_Skill.row_names[0] + '_Card_' + str(card) + '_Row_' + str(standby_skill))

                standby_skills_row_ids = Export.Create_RowIDs(standby_skill_table_rows * 2)

                # print(standby_skills_values)
                for i in range(2):
                    if i == 0:
                        for standby_skills in range(standby_skill_table_rows):
                            standby_skills_values = [get_value(Standby_Skill.row_names[i] + '_Card_' + str(card) + '_Row_0' + str(standby_skills)) for i in range(len(Standby_Skill.row_names))]
                            if standby_skills_values[4] == '103':
                                test = ast.literal_eval(standby_skills_values[6])
                                test[0] = int(str(test[0])[:-1] + '0')
                                test[2] = int(str(test[2])[:-1] + '0')
                                standby_skills_values[6] = test
                                standby_skills_values[6] = f'\'{standby_skills_values[6]}\''
                                standby_skills_values[1] = f'\'{standby_skills_values[1]}\''
                                standby_skills_values = ', '.join(map(str, standby_skills_values))
                                print(standby_skills_values)
                            else:
                                standby_skills_values = Export.List_of_Values(Standby_Skill, card=card, skill_number=standby_skill, Row=standby_skills, add_quotes=True, quote_indexes=[1,6])
                            # standby_skills_values = Export.List_of_Values(Standby_Skill, card=card, skill_number=standby_skill, Row=standby_skills, add_quotes=True, quote_indexes=[1,6])
                            standby_skills_sql = f'\n\t\t({standby_skills_row_ids[standby_skills]}, {standby_skill_set_id - 1}, {standby_skills_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                            standby_skills_text += standby_skills_sql
                        standby_skills_text += '\n'
                    else:
                        for standby_skills in range(standby_skill_table_rows):
                            standby_skills_values = Export.List_of_Values(Standby_Skill, card=card, skill_number=standby_skill, Row=standby_skills, add_quotes=True, quote_indexes=[1,6])
                            standby_skills_sql = f'\n\t\t({standby_skills_row_ids[standby_skills] + standby_skill_table_rows}, {standby_skill_set_id}, {standby_skills_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                            standby_skills_text += standby_skills_sql
                        standby_skills_text += '\n'
                
        # Card Standby Skill Set Relations
                card_standby_skill_set_relations_sql = f'\n\t\t({standby_skill_set_id - 1}, {standby_skill_set_id - 1}, {standby_skill_set_id - 1}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                card_standby_skill_set_relations_text += card_standby_skill_set_relations_sql
                card_standby_skill_set_relations_sql = f'\n\t\t({standby_skill_set_id}, {standby_skill_set_id}, {standby_skill_set_id}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                card_standby_skill_set_relations_text += card_standby_skill_set_relations_sql
                
            standby_skill_set_text = standby_skill_set_text[:-2] + ';'
            standby_skills_text = standby_skills_text[:-2] + ';'
            card_standby_skill_set_relations_text = card_standby_skill_set_relations_text[:-1] + ';'
                
        
        # Check if there is a finish skill (should be if standby skill is true but never too safe)
        if does_alias_exist(f'Finish_Skill_Set_Text_{card}_0'):
            num_of_finish_skills = Row_Checker(f'Finish_Skill_Set_Text_{card}_')
            finish_skill_set_id = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '0'))
            standby_skill_set_id = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '1'))
            finish_skills_row_ids = finish_skill_set_id
            card_finish_skills_set_relations_row_ids = finish_skill_set_id
            ### Remove this later, gotta add the increase rate and aim target as widgets on the GUI
            increase_rate = [550, 750]
            for finish_skill in range(num_of_finish_skills):
                
        # Finish Skill Sets
                finish_skill_set_name = replace_whitespace_45(get_value(f'Finish_Set_Name_{card}_{finish_skill}'))
                finish_skill_set_desc = replace_whitespace_45(get_value(f'Finish_Set_Desc_{card}_{finish_skill}'))
                finish_skill_set_cond = replace_whitespace_45(get_value(f'Finish_Set_Cond_{card}_{finish_skill}'))
                finish_skill_set_values = Export.List_of_Values(Finish_Skill_Set, card=card, skill_number=finish_skill, add_quotes=True, quote_indexes=[1,2,4])
                finish_skill_set_sql = f'\n\t\t({finish_skill_set_id + finish_skill}, \'{finish_skill_set_name}\', \'{finish_skill_set_desc}\', \'{finish_skill_set_cond}\', {finish_skill_set_values}, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                finish_skill_set_text += finish_skill_set_sql + '\n'
                
        # Finish Skills
                
                finish_skill_table_rows = Row_Checker(Finish_Skill.row_names[0] + '_Card_' + str(card) + '_Row_' + str(finish_skill))
                

                for finish_skills in range(finish_skill_table_rows):
                    finish_skills_values = Export.List_of_Values(Finish_Skill, card=card, skill_number=finish_skill, Row=finish_skills, add_quotes=True, quote_indexes=[1,6])
                    finish_skills_sql = f'\n\t\t({finish_skills_row_ids}, {finish_skill_set_id + finish_skill}, {finish_skills_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                    finish_skills_text += finish_skills_sql
                    finish_skills_row_ids += 1
                finish_skills_text += '\n'  
                
        # Finish Specials
                finish_specials_sql = f'\n\t\t({finish_skill_set_id + finish_skill}, {increase_rate[finish_skill]}, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                finish_specials_text += finish_specials_sql
                
        # Card Finish Skill Set Relations
                card_finish_skill_set_relations_sql = f'\n\t\t({card_finish_skills_set_relations_row_ids}, {finish_skill_set_id}, {finish_skill_set_id + finish_skill}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                card_finish_skills_set_relations_row_ids += 1
                card_finish_skill_set_relations_sql = f'\n\t\t({card_finish_skills_set_relations_row_ids}, {finish_skill_set_id + 1}, {finish_skill_set_id + finish_skill}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                card_finish_skills_set_relations_text += card_finish_skill_set_relations_sql
                
        # Standby Skill Set Finish Skill Set Relations
                for i in range(2):
                    i + 1
                    standby_skill_set_finish_skills_set_relations_sql = f'\n\t\t({finish_skill_set_id  + i + 1 +  finish_skill + finish_skill}, {standby_skill_set_id - 1 + i}, {finish_skill_set_id + finish_skill}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                    standby_skill_set_finish_skills_set_relations_text += standby_skill_set_finish_skills_set_relations_sql
                    
            finish_skill_set_text = finish_skill_set_text[:-2] + ';'
            finish_skills_text = finish_skills_text[:-2] + ';'
            finish_specials_text = finish_specials_text[:-1] + ';'
            card_finish_skills_set_relations_text = card_finish_skills_set_relations_text[:-1] + ';'
            standby_skill_set_finish_skills_set_relations_text = standby_skill_set_finish_skills_set_relations_text[:-1] + ';'
        
            
    return standby_skill_set_text, standby_skills_text, finish_skill_set_text, finish_skills_text, finish_specials_text, card_standby_skill_set_relations_text, card_finish_skills_set_relations_text, standby_skill_set_finish_skills_set_relations_text
    

################################################################################################################################################################
def Create_Sub_Target_Type_Set(rows):
    sub_target_type_set_text = f'''\n\t\tINSERT OR REPLACE INTO sub_target_type_sets ("id", "created_at", "updated_at")
    \tVALUES'''
    Row_ID = get_value(Card.row_names[0] + '_Card_' + '0' + '_Row_' + '1')
    Row_ID += '1'
    Row_ID = int(Row_ID)
    for i in range(rows):
        sub_target_type_set_sql = f'\n\t\t({str((Row_ID + i))}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
        sub_target_type_set_text += sub_target_type_set_sql
        
    return sub_target_type_set_text

def Dokkan_Field_Output():
    from . classes import Dokkan_Field
    dokkan_field_efficacies_text = f'''\t-- (Dokkan Fields)
    \tINSERT OR REPLACE INTO dokkan_field_efficacies ("id", "dokkan_field_efficacy_set_id", "exec_timing_type", "efficacy_type", "calc_option", "turn", "is_once", "probability", "eff_value1", "eff_value2", "eff_value3", "efficacy_values", "causality_conditions", "created_at", "updated_at")
    \tVALUES'''
    
    dokkan_fields_text = f'''\n\t\tINSERT OR REPLACE INTO dokkan_fields ("id", "dokkan_field_efficacy_set_id", "name", "description", "resource_id", "created_at", "updated_at")
    \tVALUES'''
    
    dokkan_field_efficacy_sets_text = f'''\n\t\tINSERT OR REPLACE INTO dokkan_field_efficacy_sets ("id", "created_at", "updated_at")
    \tVALUES'''
    
    dokkan_field_active_skill_set_relations_text = f'''\n\t\tINSERT OR REPLACE INTO dokkan_field_active_skill_set_relations ("id", "dokkan_field_id", "active_skill_set_id", "created_at", "updated_at")
    \tVALUES'''
    
    dokkan_field_passive_skill_relations_text = f'''\n\t\tINSERT OR REPLACE INTO dokkan_field_passive_skill_relations ("id", "dokkan_field_id", "passive_skill_id", "created_at", "updated_at")
    \tVALUES'''
    
    num_of_cards = Card_Checker()
    for card in range(num_of_cards):
        Row_ID = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '1'))
        efficacy_set_id = Row_ID
        num_of_dokkan_fields = Row_Checker(f'Dokkan_Field_Text_{card}_')
        ### In case there are more than 1 Dokkan Field (future proofing)
        for dokkan_field in range(num_of_dokkan_fields):
            
            ### Dokkan Field Efficacies
            for field_efficacy in range(Row_Checker(Dokkan_Field.row_names[0] + '_Card_' + str(card) + '_Row_' + str(dokkan_field))):
                field_efficacy_values = [get_value(Dokkan_Field.row_names[i] + '_Card_' + str(card) + '_Row_' + str(dokkan_field) + str(field_efficacy)) for i in range(len(Dokkan_Field.row_names))]

                field_efficacy_values[9] = f'\'{field_efficacy_values[9]}\''

                if field_efficacy_values[10] != 'NULL':
                    field_efficacy_values[10] = f'\'{field_efficacy_values[10]}\''

                field_efficacy_values = ', '.join(map(str, field_efficacy_values))
                field_efficacies_sql = f'\n\t\t({Row_ID + field_efficacy}, {Row_ID}, {field_efficacy_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                dokkan_field_efficacies_text += field_efficacies_sql

            dokkan_field_efficacies_text += '\n'

            ### Dokkan Fields
            dokkan_fields_values_to_grab = [f'Dokkan_Field_Name_Input_Text_{card}_{dokkan_field}', f'Dokkan_Field_Desc_Input_Text_{card}_{dokkan_field}', f'Dokkan_Field_Resource_ID_{card}_{dokkan_field}']
            dokkan_fields_values = [get_values(dokkan_fields_values_to_grab) for i in range(num_of_dokkan_fields)]
            ### Qoutes around strings
            dokkan_fields_values[0][0] = f'\'{replace_whitespace_45(dokkan_fields_values[0][0])}\''
            dokkan_fields_values[0][1] = f'\'{replace_whitespace_45(dokkan_fields_values[0][1])}\''
            dokkan_fields_values = ', '.join(map(str, dokkan_fields_values[0]))
            dokkan_fields_sql = f'\n\t\t({Row_ID + dokkan_field}, {efficacy_set_id}, {dokkan_fields_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
            dokkan_fields_text += dokkan_fields_sql
        
            ### Dokkan Field Efficacy Sets
            dokkan_field_efficacy_sets_sql = f'\n\t\t({Row_ID + dokkan_field}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
            dokkan_field_efficacy_sets_text += dokkan_field_efficacy_sets_sql
            
            ### Dokkan Field Active Skill Set Relations
            if get_value(f'Link_to_Active_Button_{card}_{dokkan_field}'):
                ### Adding dokkan_field to the last 2 in case multiple skills
                dokkan_field_active_skill_set_relations_sql = f'\n\t\t({Row_ID + dokkan_field}, {Row_ID + dokkan_field}, {Row_ID + dokkan_field}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                dokkan_field_active_skill_set_relations_text += dokkan_field_active_skill_set_relations_sql
            
            ### Dokkan Field Passive Skill Relations
            if get_value(f'Link_to_Passive_Button_{card}_{dokkan_field}'):
                dokkan_field_passive_skill_relations_sql = f'\n\t\t({Row_ID + dokkan_field}, {Row_ID + dokkan_field}, {Row_ID + dokkan_field}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                dokkan_field_passive_skill_relations_text += dokkan_field_passive_skill_relations_sql
        ### For the sake of a new line should there be multiple units in one SQL
        dokkan_fields_text += '\n'
        dokkan_field_efficacy_sets_text += '\n'
        dokkan_field_active_skill_set_relations_text += '\n'
        dokkan_field_passive_skill_relations_text += '\n'
        
    dokkan_field_efficacies_text = dokkan_field_efficacies_text[:-2] + ';'
    dokkan_fields_text = dokkan_fields_text[:-2] + ';'
    dokkan_field_efficacy_sets_text = dokkan_field_efficacy_sets_text[:-2] + ';'
    dokkan_field_active_skill_set_relations_text = dokkan_field_active_skill_set_relations_text[:-2] + ';'
    dokkan_field_passive_skill_relations_text = dokkan_field_passive_skill_relations_text[:-2] + ';'

    dokkan_fields_text = check_sql_endings(dokkan_fields_text)
    dokkan_field_efficacy_sets_text = check_sql_endings(dokkan_field_efficacy_sets_text)
    dokkan_field_passive_skill_relations_text = check_sql_endings(dokkan_field_passive_skill_relations_text)
    dokkan_field_active_skill_set_relations_text = check_sql_endings(dokkan_field_active_skill_set_relations_text)

    ### Making sure it got a value that isn't the preset SQL text
    final_dokkan_field_text = ''
    if len(dokkan_field_active_skill_set_relations_text) > 165 and len(dokkan_field_passive_skill_relations_text) > 165:
        final_dokkan_field_text = dokkan_field_efficacies_text + '\n' +  dokkan_fields_text + '\n' +  dokkan_field_efficacy_sets_text + '\n' +  dokkan_field_active_skill_set_relations_text + '\n' +  dokkan_field_passive_skill_relations_text
    elif len(dokkan_field_active_skill_set_relations_text) > 165:
        final_dokkan_field_text = dokkan_field_efficacies_text + '\n' +  dokkan_fields_text + '\n' +  dokkan_field_efficacy_sets_text + '\n' +  dokkan_field_active_skill_set_relations_text
        
    elif len(dokkan_field_passive_skill_relations_text) > 165:
        final_dokkan_field_text = dokkan_field_efficacies_text + '\n' +  dokkan_fields_text + '\n' +  dokkan_field_efficacy_sets_text + '\n' +  dokkan_field_passive_skill_relations_text



    return final_dokkan_field_text
    


################################################################################################################################################################
def Causality_Output():
    # Make sure to add checks for combo list causalities such as (19)
    causality_text = f'''\t-- Skill Causalities
    \tINSERT OR REPLACE INTO skill_causalities ("id", "causality_type", "cau_val1", "cau_val2", "cau_val3", "created_at", "updated_at")
    \tVALUES\n\t\t'''
    causality_list = []
    rows = Row_Checker('Causality_Row')
    pattern = r'\((\d+)\)'
    
    ### Creating a dictionary with set ids based on the class dictionary (Used for exporting Causality Type 41 and 45)
    # for item in range(len(Causality.card_unique_info_set_names)):
        # for key, value in Causality.card_unique_info_set_names.items():
    card_unique_infos_id_dict = {key: index + 1 for index, (key, value) in enumerate(Causality.card_unique_info_set_names.items())}
    
    
    for z in range(rows):
        values_list = [Causality.row_names[i] + str(z) for i in range(len(Causality.row_names))]
        values = get_values(values_list)
        
        match = re.search(pattern, values[1])
        if match:
            number_within_parentheses = match.group(1)
            values[1] = number_within_parentheses
        else:
            print("No match found")
            
        print(values)

##################################################################################################
        ### cau_val1 = [2], cau_val2 = [3], cau_val3 = [4]
        
        ### Causality Type 19 (Check the slots combo)
        if values[2] == 'Slot 1':
            values[2] = '0'
            
        elif values[2] == 'Slot 2':
            values[2] = '1'
            
        elif values[2] == 'Slot 3':
            values[2] = '2'
            
##################################################################################################
        ### Causality Type 34
        if values[2] == 'Team':
            values[2] = '0'
            
        elif values[2] == 'Enemy':
            values[2] = '1'

        elif values[2] == 'Rotation':
            values[2] = '2'
        
        ### Removing the text from the categories combo list value to get the category ID
        if values[1] == '34':
            match = re.search(pattern, values[3])
            if match:
                number_within_parentheses = match.group(1)
                values[3] = number_within_parentheses
            else:
                print("No match found")
        
##################################################################################################
        ### Causality Type 35
        if values[1] == '35' and values[2] == 'Super Class':
            values[2] = '126976'
            
        elif values[1] == '35' and values[2] == 'Extreme Class':
            values[2] = '4063232'
            
##################################################################################################
        ### Causality Type 38
        # ['Single Status', 'Multiple Statuses']
        if values[3] == 'Single Status':
            values[3] = '0'
        
        elif values[3] == 'Multiple Status':
            values[3] = '1'
            
##################################################################################################
        ### Causality Type 39
        # ['Super Class', 'Extreme Class']
        if values[1] == '39' and values[2] == 'Super Class':
            values[2] = '64'
        
        elif values[1] == '39' and values[2] == 'Extreme Class':
            values[2] = '32'
            
##################################################################################################
        ### Causality Type 41
        ### combo_1 = ['Team', 'Enemy', 'Rotation'] already checked in Causality Type 34
        if values[1] == '41':
            values[3] = card_unique_infos_id_dict[values[3]]

##################################################################################################     
        ### Causality Type 44
        # ['Supers Performed', 'Atks Performed', 'Atks Received', 'Guard Activated', 'Dodges']
        if values[2] == 'Supers Performed':
            values[2] = '1'
            
        elif values[2] == 'Atks Performed':
            values[2] = '2'

        elif values[2] == 'Atks Received':
            values[2] = '3'
            
        elif values[2] == 'Guard Activated':
            values[2] = '4'
            
        elif values[2] == 'Dodges':
            values[2] = '5'
            
################################################################################################## 
        ### Causality Type 45
        ### combo_1 = ['Team', 'Enemy', 'Rotation'] already checked in Causality Type 34
        if values[1] == '45':
            match = re.search(pattern, values[3])
            if match:
                number_within_parentheses = match.group(1)
                values[3] = number_within_parentheses
            else:
                print("No match found")

            values[4] = card_unique_infos_id_dict[values[4]]
        
##################################################################################################
        ### Causality Type 46
        ### ['Team', 'Enemy', 'Rotation'] checked in Causality Type 34
        if values[3] == 'Super Class':
            values[3] = '64'
            
        elif values[3] == 'Extreme Class':
            values[3] = '32'
            
##################################################################################################
        ### Causality Type 48 and 49
        # ['Ki Blast', 'Unarmed', 'Physical', 'Unit Super']
        if values[2] == 'Ki Blast':
            values[2] = '1'
            
        elif values[2] == 'Unarmed':
            values[2] = '2'
            
        elif values[2] == 'Physical':
            values[2] = '3'
            
        elif values[2] == 'Unit Super':
            values[2] = '4'
            
##################################################################################################
        ### Causality Type 59
        if values[1] == '59' and values[2] == 'Super Class':
            values[2] = '1'
            
        elif values[1] == '59' and values[2] == 'Extreme Class':
            values[2] = '2'
        
        causality_list.append(values)
        
        
    for z in range(rows):
        causality_values = ', '.join(map(str, causality_list[z]))  # Convert card values to a comma-separated string
        causality_sql = f'({causality_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
        causality_text += causality_sql + '\n\t\t'
        
    causality_text = causality_text[:-4] + ';'
    
    return causality_text
        
        
def Effect_Pack_Output():
    effect_pack_text = f'''\n\t-- Effect Packs
    \tINSERT OR REPLACE INTO effect_packs ("id", "category", "name", "pack_name", "scene_name", "red", "green", "blue", "alpha", "lite_flicker_rate", "created_at", "updated_at")
    \tVALUES'''
    
    for card in range(Card_Checker()):
        # Effect Packs
        if does_alias_exist(f'Effect_Packs_Table_{card}'):
            effect_pack_rows = Row_Checker(Effect_Pack.row_names[0] + '_Card_' + str(card) + '_Row_')
            for row in range(effect_pack_rows):
                effect_packs_values = [get_value(Effect_Pack.row_names[i] + '_Card_' + str(card) + '_Row_' + str(row)) for i in range(len(Effect_Pack.row_names))]
                # Change combo value to corresponding value
                if effect_packs_values[1] == 'Battle/Support Packs':
                    effect_packs_values[1] = 1
                    
                elif effect_packs_values[1] == 'SP Effect Packs':
                    effect_packs_values[1] = 5
                
                # Set strings to have quotes around them
                effect_packs_values[2] = f'\'{effect_packs_values[2]}\''
                effect_packs_values[3] = f'\'{effect_packs_values[3]}\''
                effect_packs_values[4] = f'\'{effect_packs_values[4]}\''

                effect_packs_values = ', '.join(map(str, effect_packs_values))
                effect_pack_sql_row = f'\n\t\t({effect_packs_values}, 255, 255, 255, 255, 70, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                effect_pack_text += effect_pack_sql_row
    
    effect_pack_text = effect_pack_text[:-1] + ';'
    
    if len(effect_pack_text) < 211:
        effect_pack_text = None

    return effect_pack_text

def Special_Views_Output():
    special_views_text = f'''\n\t-- Special Views
    \tINSERT OR REPLACE INTO special_views ("id", "script_name", "cut_in_card_id", "special_name_no", "special_motion", "lite_flicker_rate", "energy_color", "special_category_id", "created_at", "updated_at")
    \tVALUES'''
    
    for card in range(Card_Checker()):
        # Special Views
        if does_alias_exist(f'Special_Views_Table_{card}'):
            special_views_rows = Row_Checker(Special_Views.row_names[0] + '_Card_' + str(card) + '_Row_')
            for row in range(special_views_rows):
                special_views_values = [get_value(Special_Views.row_names[i] + '_Card_' + str(card) + '_Row_' + str(row)) for i in range(len(Special_Views.row_names))]
                # Change combo value to corresponding value
                if special_views_values[7] == 'Undefined':
                    special_views_values[7] = 'NULL'
                
                elif special_views_values[7] == 'Ki Blast':
                    special_views_values[7] = 1
                    
                elif special_views_values[7] == 'Unarmed':
                    special_views_values[7] = 2
                    
                elif special_views_values[7] == 'Physical/Melee':
                    special_views_values[7] = 3
                
                special_views_values[1] = f'\'{special_views_values[1]}\''
                special_views_values = ', '.join(map(str, special_views_values))
                special_views_sql = f'\n\t\t({special_views_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                special_views_text += special_views_sql
                
    special_views_text = special_views_text[:-1] + ';'
    
    if len(special_views_text) < 336:
        special_views_text = None
        
    return special_views_text
    

def Battle_Params_Output():
    
    battle_params_text = f'''\n\t-- Battle Params
    \tINSERT OR REPLACE INTO battle_params ("id", "param_no", "idx", "value", "created_at", "updated_at")
    \tVALUES'''
    
    transformation_desc_text = f'''\n\t-- Transformation Descriptions (Choose one according to the type of transformation. TransformationSkillID is the passive_skills ID that does the transformation)
    \tINSERT OR REPLACE INTO transformation_descriptions ("id", "skill_type", "skill_id", "description", "created_at", "updated_at")
    \tVALUES'''
    card_with_finish_skill = ''
    for card in range(Card_Checker()):
        if does_alias_exist(f'Finish_Skill_Set_Text_{card}_0'):
            card_with_finish_skill = str(card)
            break
            
    cards = Card_Checker()
    for card in range(Card_Checker()):
        Row_ID = int(get_value(Card.row_names[0] + '_Card_' + str(card) + '_Row_' + '1'))
        if does_alias_exist(f'Battle_Params_Text_{card}'):
            for param in range(Row_Checker(f'Battle_Params_Table_{card}_')):
                for param_row in range(Row_Checker(Battle_Params.row_names[0] + '_Card_' + str(card) + '_Row_' + str(param))):
                    battle_param_values = [get_value(Battle_Params.row_names[i] + '_Card_' + str(card) + '_Row_' + str(param) + str(param_row)) for i in range(len(Battle_Params.row_names))]
                    battle_param_values = ', '.join(map(str, battle_param_values))
                    
                    battle_params_sql = f'\n\t\t({Row_ID}, {battle_param_values}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),'
                    battle_params_text += battle_params_sql
                    Row_ID += 1
                    
            
                battle_params_text += '\n'
        if cards - 1 == card:
            battle_params_text = battle_params_text[:-2] + ';'
            
    if len(battle_params_text) < 137:
        battle_params_text = None
        
            
    return battle_params_text
                        

def Character_Output():
    character_text = f'''\n\t-- Character
    \tINSERT OR REPLACE INTO characters ("id", "name", "race", "sex", "size", "created_at", "updated_at")
    \tVALUES'''
    
    card_unique_info_text = f'''\n\t-- Card Unique Infos
    \tINSERT OR REPLACE INTO card_unique_infos ("id", "name", "kana", "created_at", "updated_at")
    \tVALUES'''

    card_unique_info_set_text = f'''\n\t-- Card Unique Info Set Relations
    \tINSERT OR REPLACE INTO card_unique_info_set_relations ("id", "card_unique_info_id", "card_unique_info_set_id", "created_at", "updated_at")
    \tVALUES'''

    card_decoration_text = f'''\n\t-- Card Decorations (sticker)
    \tINSERT OR REPLACE INTO card_decorations ("id", "card_id", "priority", "created_at", "updated_at")
    \tVALUES'''
    
    pass


def safe_to_list(value_str):
    value_str = value_str.strip()

    # If it looks like a list (has [ and ])
    if value_str.startswith('[') and value_str.endswith(']'):
        return ast.literal_eval(value_str)

    # Otherwise, try to make it a list by wrapping brackets around it
    # Split by commas and strip whitespace/quotes
    items = [item.strip().strip("'").strip('"') for item in value_str.split(',')]
    return items

# check if sql text ends with ,; and fix it
def check_sql_endings(sql_text) -> str:
    if sql_text.rstrip().endswith(",;"):
        return sql_text.rstrip()[:-2] + ";"
    return sql_text