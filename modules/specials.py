from dearpygui.dearpygui import *
# from passive import Strings_Length
from . configs import Config_Read
import sqlite3
from .classes import String_Length, Efficacy_Values, Card_Checks, Widget_Aliases, Card_Specials, Special_Set, Specials, Custom_Unit
from . configs import Config_Read
from . functions import Table_Inputs, Delete_Items, Text_Resize, Table_ID, Row_Checker, Get_Card_Number


str_length = String_Length.length
Damage_Types = ['supreme', 'immense', 'colossal', 'mega-colossal']

def Specials_Widgets(*, cards=0, i=0):
    
    # for cards in range(Card_Checks.number_of_cards):
    with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Button_Add_Group_Card_{cards}'):
        add_button(label='Add Super', tag=f'Specials_Button_Add_Card_{cards}', callback=Specials_Add, parent=f'Specials_Button_Add_Group_Card_{cards}')
        add_button(label='Del Super', tag=f'Specials_Button_Del_Card_{cards}', callback=Specials_Del, parent=f'Specials_Button_Add_Group_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Add_Group_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Add_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Del_Card_{cards}')
        
    # if not get_value('Custom_Unit'):
        # print(get_value('Custom_Unit'))
        # Number_Of_Special_Sets = len(Card_Checks.special_set_ids[cards])
    # else:
        # Number_Of_Special_Sets = 1

        
    # for i in range(Number_Of_Special_Sets):
    rows_to_check = [f'Special#_Text_Card_{cards}_{i}',f'Special_Name_Text_Card_{cards}_{i}',f'Special_Set_Name_Input_Card_{cards}_{i}',f'Special_Aim_Target_Text_Card_{cards}_{i}',f'Special_Set_Aim_Target_Input_Card_{cards}_{i}',f'Special_Desc_Text_Card_{cards}_{i}',f'Special_Set_Desc_Input_Card_{cards}_{i}',f'Special_Increase_Rate_Text_Card_{cards}_{i}',
                 f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}',f'Special_Cond_Text_Card_{cards}_{i}',f'Special_Set_Cond_Input_Card_{cards}_{i}',f'Special_Level_Bonus_Text_Card_{cards}_{i}',f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}',f'Card_Specials_Text_Card_{cards}_{i}',f'Special_Skills_Text_Card_{cards}_{i}',f'Specials_Separator_Card_{cards}_{i}',
                 f'Special_Set_Group_Card_{cards}_1_{i}', f'Special_Set_Group_Card_{cards}_2_{i}', f'Special_Set_Group_Card_{cards}_3_{i}', f'Specials_Table_Group_Card_{cards}_{i}', f'Specials_Aim_Target_Group_Card_{cards}_{i}',
                 f'Special_Aim_Target_Text_Card_{cards}_{i}',f'Special_Set_Aim_Target_Input_Card_{cards}_{i}',f'Specials_Increase_Rate_Group_Card_{cards}_{i}',f'Special_Increase_Rate_Text_Card_{cards}_{i}',
                 f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}', f'Specials_Level_Bonus_Group_Card_{cards}_{i}', f'Special_Level_Bonus_Text_Card_{cards}_{i}', f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}']

    for item in range(len(rows_to_check)):
        Delete_Items(rows_to_check[item])

    add_separator(tag=f'Specials_Button_Separtor_Card_{cards}_{i}', parent=f'Specials_Tab_{cards}')
    add_text(f'Special #{i + 1}', color=(255,50,50), parent=f'Specials_Tab_{cards}', tag=f'Special#_Text_Card_{cards}_{i}')
    with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Special_Set_Group_Card_{cards}_1_{i}'):
        add_text('Name:', tag=f'Special_Name_Text_Card_{cards}_{i}')
        add_input_text(tag=f'Special_Set_Name_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Name')
        Widget_Aliases.tags_to_delete.append(f'Special#_Text_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Set_Group_Card_{cards}_1_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Name_Text_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Set_Name_Input_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Separtor_Card_{cards}_{i}')

    with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Special_Set_Group_Card_{cards}_2_{i}'):
        add_text('Desc: ', tag=f'Special_Desc_Text_Card_{cards}_{i}')
        add_input_text(tag=f'Special_Set_Desc_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Description')
        Widget_Aliases.tags_to_delete.append(f'Special_Set_Group_Card_{cards}_2_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Desc_Text_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Set_Desc_Input_Card_{cards}_{i}')

    with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Special_Set_Group_Card_{cards}_3_{i}'):
        add_text('Cond: ', tag=f'Special_Cond_Text_Card_{cards}_{i}')
        add_input_text(tag=f'Special_Set_Cond_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Cond Desc')
        Widget_Aliases.tags_to_delete.append(f'Special_Set_Group_Card_{cards}_3_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Set_Group_Card_{cards}_3_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Set_Group_Card_{cards}_3_{i}')
        
        
    add_text('Card Specials', color=(255,50,50), parent=f'Specials_Tab_Card_{cards}', tag=f'Card_Specials_Text_Card_{cards}_{i}')
    Widget_Aliases.tags_to_delete.append(f'Card_Specials_Text_Card_{cards}_{i}')
    CS_tags = Table_Inputs(table_name=f'Card_Specials_Card_{cards}_{i}', row_name=f'Card_Specials_Table_Row_Card_{cards}_{i}', class_name=Card_Specials,
                         used_in_loop=True, loop_number=i, use_child_window=False, table_parent=f'Specials_Tab_Card_{cards}', table_height=67, table_width=1150,
                         row_width=75, table_policy=mvTable_SizingStretchSame, transformation=True, transformation_card_num=cards)
    # print(CS_tags)


    with group(tag=f'Special_Skills_Button_Group_Card_{cards}_{i}', parent=f'Specials_Tab_Card_{cards}', horizontal=True):
        add_text('Special Skills', color=(255,50,50), parent=f'Special_Skills_Button_Group_Card_{cards}_{i}', tag=f'Special_Skills_Text_Card_{cards}_{i}')
        add_button(label='Add Skill', tag=f'Special_Skills_Button_Add_Card_{cards}_{i}', callback=Special_Skills_Add, parent=f'Special_Skills_Button_Group_Card_{cards}_{i}')
        add_button(label='Del Skill', tag=f'Special_Skills_Button_Del_Card_{cards}_{i}', callback=Special_Skills_Del, parent=f'Special_Skills_Button_Group_Card_{cards}_{i}')
    Widget_Aliases.tags_to_delete.append(f'Special_Skills_Text_Card_{cards}_{i}')
    Widget_Aliases.tags_to_delete.append(f'Specials_Table_Group_Card_{cards}_{i}')
    Widget_Aliases.tags_to_delete.append(f'Special_Skills_Button_Group_Card_{cards}_{i}')
    Widget_Aliases.tags_to_delete.append(f'Special_Skills_Text_Card_{cards}_{i}')
    Widget_Aliases.tags_to_delete.append(f'Special_Skills_Button_Add_Card_{cards}_{i}')
    Widget_Aliases.tags_to_delete.append(f'Special_Skills_Button_Del_Card_{cards}_{i}')
    with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Table_Group_Card_{cards}_{i}'):
        Specials_tags = Table_Inputs(table_name=f'Specials_Card_{cards}_{i}', row_name=f'Specials_Table_Row_Card_{cards}_{i}', class_name=Specials,
                     used_in_loop=True, loop_number=i, use_child_window=True, child_parent=f'Specials_Table_Group_Card_{cards}_{i}', child_tag=f'Specials_Child_Window_Card_{cards}_{i}',
                     table_height=90, table_width=1134, child_height=87, child_width=1139, combo=True, combo_tag=Specials.row_names[1], combo_list=Efficacy_Values.combo_list,
                     transformation=True, transformation_card_num=cards)
        set_item_height(f'Specials_Card_{cards}_{i}', (24 * 1) + 23)
        # print(Specials_tags)
        
        with group(horizontal=False, tag=f'Specials_Group_Card_{cards}_{i}'):
            with group(horizontal=True, tag=f'Specials_Aim_Target_Group_Card_{cards}_{i}'):
                add_text('Aim Target:', tag=f'Special_Aim_Target_Text_Card_{cards}_{i}')
                add_input_text(tag=f'Special_Set_Aim_Target_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Aim Target')
            with group(horizontal=True, tag=f'Specials_Increase_Rate_Group_Card_{cards}_{i}'):
                add_text('Inc Rate:    ', tag=f'Special_Increase_Rate_Text_Card_{cards}_{i}')
                add_input_text(tag=f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Inc Rate')
            with group(horizontal=True, tag=f'Specials_Level_Bonus_Group_Card_{cards}_{i}'):
                add_text('Lvl Bonus:  ', tag=f'Special_Level_Bonus_Text_Card_{cards}_{i}')
                add_input_text(tag=f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Level Bonus')
                Widget_Aliases.tags_to_delete.append(f'Specials_Group_Card_{cards}_{i}')
                Widget_Aliases.tags_to_delete.append(f'Specials_Aim_Target_Group_Card_{cards}_{i}')
                Widget_Aliases.tags_to_delete.append(f'Special_Aim_Target_Text_Card_{cards}_{i}')
                Widget_Aliases.tags_to_delete.append(f'Special_Set_Aim_Target_Input_Card_{cards}_{i}')
                Widget_Aliases.tags_to_delete.append(f'Specials_Increase_Rate_Group_Card_{cards}_{i}')
                Widget_Aliases.tags_to_delete.append(f'Special_Increase_Rate_Text_Card_{cards}_{i}')
                Widget_Aliases.tags_to_delete.append(f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}')
                Widget_Aliases.tags_to_delete.append(f'Specials_Level_Bonus_Group_Card_{cards}_{i}')
                Widget_Aliases.tags_to_delete.append(f'Special_Level_Bonus_Text_Card_{cards}_{i}')
                Widget_Aliases.tags_to_delete.append(f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}')
                
    add_separator(parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Separator_Card_{cards}_{i}')
    Widget_Aliases.tags_to_delete.append(f'Specials_Separator_Card_{cards}_{i}')
    

def Specials_Query():
    config = Config_Read()
    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
    cur = con.cursor()
    cards = Custom_Unit.card_number
        
    # Card_Checks.special_set_ids is a list of special set id lists Ex. [[XX, XX], [XX], [X, XX, X]]
    Number_Of_Special_Sets = len(Card_Checks.special_set_ids[cards])
    # print(Card_Checks.special_set_ids)
    Card_Specials.query_values.clear()
    Special_Set.query_values.clear()
    Specials.query_values.clear()

    

    Card_Specials.skill_rows.clear()
    Special_Set.skill_rows.clear()
    Specials.skill_rows.clear()
    # print(cards)
    with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Button_Add_Group_Card_{cards}'):
        add_button(label='Add Super', tag=f'Specials_Button_Add_Card_{cards}', callback=Specials_Add, parent=f'Specials_Button_Add_Group_Card_{cards}')
        add_button(label='Del Super', tag=f'Specials_Button_Del_Card_{cards}', callback=Specials_Del, parent=f'Specials_Button_Add_Group_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Add_Group_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Add_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Del_Card_{cards}')

    for i in range(Number_Of_Special_Sets):
        # Grabbing value here instead of inside each execution to avoid possible efficiency loss.
        # Otherwise it'd be grabbing the value 3 times each loop versus 1.
        # print(Card_Checks.special_set_ids[cards][i])
        special_set_id = Card_Checks.special_set_ids[cards][i]
        # print('special_set = ' + str(special_set_id))
        # print(Card_Checks.special_set_ids)
        
        ### Before changing to both Card IDs because sometimes a special set id is reused for boss cards
        # cur.execute('SELECT priority,style,lv_start,eball_num_start,view_id,card_costume_condition_id,special_bonus_id1,special_bonus_lv1,bonus_view_id1,special_bonus_id2,special_bonus_lv2,bonus_view_id2,causality_conditions,special_asset_id FROM card_specials WHERE special_set_id = ' + str(special_set_id))
        card_id_0 = str(Card_Checks.card_ids[cards])[:-1] + '0'
        card_id_1 = str(Card_Checks.card_ids[cards])
        cur.execute('''
                    SELECT priority, style, lv_start, eball_num_start, view_id, card_costume_condition_id, special_bonus_id1, special_bonus_lv1, bonus_view_id1, special_bonus_id2, special_bonus_lv2, bonus_view_id2, causality_conditions, special_asset_id
                    FROM card_specials
                    WHERE (card_id = ? AND special_set_id = ?)
                        OR (card_id = ? AND special_set_id = ?)
                ''', (card_id_0, special_set_id, card_id_1, special_set_id))

        card_specials_fetch = cur.fetchall()
        Card_Specials.query_values.append(card_specials_fetch)
        Card_Specials.skill_rows.append(len(card_specials_fetch))
        Card_Specials.rows = (len(card_specials_fetch))
        # print(len(card_specials_fetch))
        # print(card_specials_fetch)

        cur.execute('SELECT aim_target,increase_rate,lv_bonus FROM special_sets WHERE id = ' + str(special_set_id))
        special_set_fetch = cur.fetchall()
        Special_Set.query_values.append(special_set_fetch)
        Special_Set.skill_rows.append(len(special_set_fetch))
        # print(special_set_fetch)

        cur.execute('SELECT type,efficacy_type,target_type,calc_option,turn,prob,causality_conditions,eff_value1,eff_value2,eff_value3 FROM specials WHERE special_set_id = ' + str(special_set_id))
        specials_fetch = cur.fetchall()
        Specials.query_values.append(specials_fetch)
        Specials.skill_rows.append(len(specials_fetch))
        # print(specials_fetch)

        # Only setting the Specials rows to a different value as Card_Specials and Special_Set will always be the same num of rows.
        Specials.rows = len(specials_fetch)
    
        rows_to_check = [f'Special#_Text_Card_{cards}_{i}',f'Special_Name_Text_Card_{cards}_{i}',f'Special_Set_Name_Input_Card_{cards}_{i}',f'Special_Aim_Target_Text_Card_{cards}_{i}',f'Special_Set_Aim_Target_Input_Card_{cards}_{i}',f'Special_Desc_Text_Card_{cards}_{i}',f'Special_Set_Desc_Input_Card_{cards}_{i}',f'Special_Increase_Rate_Text_Card_{cards}_{i}',
                        f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}',f'Special_Cond_Text_Card_{cards}_{i}',f'Special_Set_Cond_Input_Card_{cards}_{i}',f'Special_Level_Bonus_Text_Card_{cards}_{i}',f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}',f'Card_Specials_Text_Card_{cards}_{i}',f'Special_Skills_Text_Card_{cards}_{i}',f'Specials_Separator_Card_{cards}_{i}',
                        f'Special_Set_Group_Card_{cards}_1_{i}', f'Special_Set_Group_Card_{cards}_2_{i}', f'Special_Set_Group_Card_{cards}_3_{i}', f'Specials_Table_Group_Card_{cards}_{i}', f'Specials_Aim_Target_Group_Card_{cards}_{i}',
                        f'Special_Aim_Target_Text_Card_{cards}_{i}',f'Special_Set_Aim_Target_Input_Card_{cards}_{i}',f'Specials_Increase_Rate_Group_Card_{cards}_{i}',f'Special_Increase_Rate_Text_Card_{cards}_{i}',
                        f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}', f'Specials_Level_Bonus_Group_Card_{cards}_{i}', f'Special_Level_Bonus_Text_Card_{cards}_{i}', f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}']
    # class.query_values contains every super from the queries.
    # class.query_values[super_number] would return the super.
    # class.query_values[super_number][query_values] would return the whole row of specified super number.
    # class.query_values[super_number][query_values][query_values_info] would return the single value used to set values with.
    # Note these are lists, index numbers start at 0, thus super 1 is [0].
        for item in range(len(rows_to_check)):
            Delete_Items(rows_to_check[item])
# 
        add_separator(tag=f'Specials_Button_Separtor_Card_{cards}_{i}', parent=f'Specials_Tab_Card_{cards}')
        add_text(f'Special #{i + 1}', color=(255,50,50), parent=f'Specials_Tab_Card_{cards}', tag=f'Special#_Text_Card_{cards}_{i}')
        with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Special_Set_Group_Card_{cards}_1_{i}'):
            add_text('Name:', tag=f'Special_Name_Text_Card_{cards}_{i}')
            add_input_text(tag=f'Special_Set_Name_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Name')
            Widget_Aliases.tags_to_delete.append(f'Special#_Text_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Special_Set_Group_Card_{cards}_1_{i}')
            Widget_Aliases.tags_to_delete.append(f'Special_Name_Text_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Special_Set_Name_Input_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Specials_Button_Separtor_Card_{cards}_{i}')
# 
        with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Special_Set_Group_Card_{cards}_2_{i}'):
            add_text('Desc: ', tag=f'Special_Desc_Text_Card_{cards}_{i}')
            add_input_text(tag=f'Special_Set_Desc_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Description')
            Widget_Aliases.tags_to_delete.append(f'Special_Set_Group_Card_{cards}_2_{i}')
            Widget_Aliases.tags_to_delete.append(f'Special_Desc_Text_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Special_Set_Desc_Input_Card_{cards}_{i}')
# 
        with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Special_Set_Group_Card_{cards}_3_{i}'):
            add_text('Cond: ', tag=f'Special_Cond_Text_Card_{cards}_{i}')
            add_input_text(tag=f'Special_Set_Cond_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Cond Desc')
            Widget_Aliases.tags_to_delete.append(f'Special_Set_Group_Card_{cards}_3_{i}')
            Widget_Aliases.tags_to_delete.append(f'Special_Set_Group_Card_{cards}_3_{i}')
            Widget_Aliases.tags_to_delete.append(f'Special_Set_Group_Card_{cards}_3_{i}')
# 
        # SS_tags = Table_Inputs(table_name=f'Special_Set_{i}', row_name=f'Special_Set_Table_Row_{i}', class_name=Special_Set, child_tag=f'Special_Set_Child_Window_{i}',
                            #  child_parent=f'Specials_Tab_Card_{cards}',used_in_loop=True, loop_number=i, use_child_window=True)


        add_text('Card Specials', color=(255,50,50), parent=f'Specials_Tab_Card_{cards}', tag=f'Card_Specials_Text_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Card_Specials_Text_Card_{cards}_{i}')
        CS_tags = Table_Inputs(table_name=f'Card_Specials_Card_{cards}_{i}', row_name=f'Card_Specials_Table_Row_Card_{cards}_{i}', class_name=Card_Specials,
                                used_in_loop=True, loop_number=i, use_child_window=False, table_parent=f'Specials_Tab_Card_{cards}', table_height=67, table_width=1150,
                                row_width=75, table_policy=mvTable_SizingStretchSame, transformation=True, transformation_card_num=cards)
        
        set_item_height(f'Card_Specials_Card_{cards}_{i}', (24 * len(card_specials_fetch)) + 23)
        
        with group(tag=f'Special_Skills_Button_Group_Card_{cards}_{i}', parent=f'Specials_Tab_Card_{cards}', horizontal=True):
            add_text('Special Skills', color=(255,50,50), parent=f'Special_Skills_Button_Group_Card_{cards}_{i}', tag=f'Special_Skills_Text_Card_{cards}_{i}')
            add_button(label='Add Skill', tag=f'Special_Skills_Button_Add_Card_{cards}_{i}', callback=Special_Skills_Add, parent=f'Special_Skills_Button_Group_Card_{cards}_{i}')
            add_button(label='Del Skill', tag=f'Special_Skills_Button_Del_Card_{cards}_{i}', callback=Special_Skills_Del, parent=f'Special_Skills_Button_Group_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Skills_Text_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Table_Group_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Skills_Button_Group_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Skills_Text_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Skills_Button_Add_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Special_Skills_Button_Del_Card_{cards}_{i}')
        with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Table_Group_Card_{cards}_{i}'):
            Specials_tags = Table_Inputs(table_name=f'Specials_Card_{cards}_{i}', row_name=f'Specials_Table_Row_Card_{cards}_{i}', class_name=Specials,
                                        used_in_loop=True, loop_number=i, use_child_window=True, child_parent=f'Specials_Table_Group_Card_{cards}_{i}', child_tag=f'Specials_Child_Window_Card_{cards}_{i}',
                                        table_height=90, table_width=1134, child_height=87, child_width=1139, combo=True, combo_tag=Specials.row_names[1], combo_list=Efficacy_Values.combo_list,
                                        transformation=True, transformation_card_num=cards)
            
            set_item_height(f'Specials_Card_{cards}_{i}', (24 * len(specials_fetch)) + 23)
            set_item_height(f'Specials_Child_Window_Card_{cards}_{i}', (25 * len(specials_fetch)) + 38)

            with group(horizontal=False, tag=f'Specials_Group_Card_{cards}_{i}'):
                with group(horizontal=True, tag=f'Specials_Aim_Target_Group_Card_{cards}_{i}'):
                    add_text('Aim Target:', tag=f'Special_Aim_Target_Text_Card_{cards}_{i}')
                    add_input_text(tag=f'Special_Set_Aim_Target_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Aim Target')
                with group(horizontal=True, tag=f'Specials_Increase_Rate_Group_Card_{cards}_{i}'):
                    add_text('Inc Rate:    ', tag=f'Special_Increase_Rate_Text_Card_{cards}_{i}')
                    add_input_text(tag=f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Inc Rate')
                with group(horizontal=True, tag=f'Specials_Level_Bonus_Group_Card_{cards}_{i}'):
                    add_text('Lvl Bonus:  ', tag=f'Special_Level_Bonus_Text_Card_{cards}_{i}')
                    add_input_text(tag=f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}', width=String_Length.length[0], callback=Text_Resize, hint='Level Bonus')
                    Widget_Aliases.tags_to_delete.append(f'Specials_Group_Card_{cards}_{i}')
                    Widget_Aliases.tags_to_delete.append(f'Specials_Aim_Target_Group_Card_{cards}_{i}')
                    Widget_Aliases.tags_to_delete.append(f'Special_Aim_Target_Text_Card_{cards}_{i}')
                    Widget_Aliases.tags_to_delete.append(f'Special_Set_Aim_Target_Input_Card_{cards}_{i}')
                    Widget_Aliases.tags_to_delete.append(f'Specials_Increase_Rate_Group_Card_{cards}_{i}')
                    Widget_Aliases.tags_to_delete.append(f'Special_Increase_Rate_Text_Card_{cards}_{i}')
                    Widget_Aliases.tags_to_delete.append(f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}')
                    Widget_Aliases.tags_to_delete.append(f'Specials_Level_Bonus_Group_Card_{cards}_{i}')
                    Widget_Aliases.tags_to_delete.append(f'Special_Level_Bonus_Text_Card_{cards}_{i}')
                    Widget_Aliases.tags_to_delete.append(f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}')


        add_separator(parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Separator_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Separator_Card_{cards}_{i}')

        # Specials
        ########################################################################################################
        for tag in range(len(specials_fetch)):
            for row_names in range(len(Specials.row_names)):
                if specials_fetch[tag][row_names] is None:
                    set_value(Specials.row_names[row_names] + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), 'NULL')
                elif Specials.row_names[row_names] == Specials.row_names[1]:
                        # print(eff_dict[Passive_Skill.query_values[i][z]])
                        set_value(Specials.row_names[row_names] + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), Efficacy_Values.eff_dict[specials_fetch[tag][row_names]])
                        # Text_Resize(Specials.row_names[row_names] + str(i) + str(tag))
                else:
                    # print(Specials.row_names[row_names] + str(cards) + str(i) + str(tag))
                    set_value(Specials.row_names[row_names] + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), specials_fetch[tag][row_names])
        # Card Specials
        ########################################################################################################
        for tag in range(len(card_specials_fetch)):
            for row_names in range(len(Card_Specials.row_names)):
                # print(Card_Specials.row_names[row_names] + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag))
                if card_specials_fetch[tag][row_names] is None:
                    set_value(Card_Specials.row_names[row_names] + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), 'NULL')
                else:
                    pass
                    set_value(Card_Specials.row_names[row_names] + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), card_specials_fetch[tag][row_names])
        # Special_Sets
        ########################################################################################################
        set_value(f'Special_Set_Name_Input_Card_{cards}_{i}', Card_Checks.special_set_names[cards][i].replace('\n', ''))
        Text_Resize(f'Special_Set_Name_Input_Card_{cards}_{i}')
        set_value(f'Special_Set_Desc_Input_Card_{cards}_{i}', Card_Checks.special_set_descriptions[cards][i].replace('\n', ''))
        Text_Resize(f'Special_Set_Desc_Input_Card_{cards}_{i}')
        # print(Card_Checks.special_set_conditions)
        
        if not Card_Checks.special_set_conditions[cards]:
            set_value(f'Special_Set_Cond_Input_Card_{cards}_{i}', 'NULL')
            Text_Resize(f'Special_Set_Cond_Input_Card_{cards}_{i}')
            
        # If the list index is empty
        elif not Card_Checks.special_set_conditions[cards][i]:
            set_value(f'Special_Set_Cond_Input_Card_{cards}_{i}', 'NULL')
            Text_Resize(f'Special_Set_Cond_Input_Card_{cards}_{i}')
            
        else:
            # print(Card_Checks.special_set_conditions[cards])
            set_value(f'Special_Set_Cond_Input_Card_{cards}_{i}', Card_Checks.special_set_conditions[cards][i].replace('\n', ''))
            Text_Resize(f'Special_Set_Cond_Input_Card_{cards}_{i}')
            
        for tag in range(len(special_set_fetch)):
            for row_names in range(len(Special_Set.query_tag_names)):
                set_value(Special_Set.query_tag_names[row_names] + '_Card_' + str(cards) + '_' + str(i), special_set_fetch[tag][row_names])

    Specials.last_rows = Number_Of_Special_Sets
            # print(len(specials_fetch))
    
def Specials_Add(app_data):
    Card_Number = Table_ID(app_data)
    Super_Number = Row_Checker(f'Special#_Text_Card_{Card_Number}_')
    print(f'Card Number: Card_{Card_Number}')
    print(f'Super_Number: {Super_Number}')
    
    add_text(f'Special #{Super_Number + 1}', color=(255,50,50), parent=f'Specials_Tab_Card_{Card_Number}', tag=f'Special#_Text_Card_{Card_Number}_{Super_Number}')
    with group(horizontal=True, parent=f'Specials_Tab_Card_{Card_Number}', tag=f'Special_Set_Group_Card_{Card_Number}_1_{Super_Number}'):
        add_text('Name:', tag=f'Special_Name_Text_Card_{Card_Number}_{Super_Number}')
        add_input_text(tag=f'Special_Set_Name_Input_Card_{Card_Number}_{Super_Number}', width=String_Length.length[0], callback=Text_Resize, hint='Name')
    with group(horizontal=True, parent=f'Specials_Tab_Card_{Card_Number}', tag=f'Special_Set_Group_Card_{Card_Number}_2_{Super_Number}'):
        add_text('Desc: ', tag=f'Special_Desc_Text_Card_{Card_Number}_{Super_Number}')
        add_input_text(tag=f'Special_Set_Desc_Input_Card_{Card_Number}_{Super_Number}', width=String_Length.length[0], callback=Text_Resize, hint='Description')
    with group(horizontal=True, parent=f'Specials_Tab_Card_{Card_Number}', tag=f'Special_Set_Group_Card_{Card_Number}_3_{Super_Number}'):
        add_text('Cond: ', tag=f'Special_Cond_Text_Card_{Card_Number}_{Super_Number}')
        add_input_text(tag=f'Special_Set_Cond_Input_Card_{Card_Number}_{Super_Number}', width=String_Length.length[0], callback=Text_Resize, hint='Cond Desc')
    
    add_text('Card Specials', color=(255,50,50), parent=f'Specials_Tab_Card_{Card_Number}', tag=f'Card_Specials_Text_Card_{Card_Number}_{Super_Number}')
    CS_tags = Table_Inputs(table_name=f'Card_Specials_Card_{Card_Number}_{Super_Number}', row_name=f'Card_Specials_Table_Row_Card_{Card_Number}_{Super_Number}', class_name=Card_Specials,
                                 used_in_loop=True, loop_number=Super_Number, use_child_window=False, table_parent=f'Specials_Tab_Card_{Card_Number}', table_height=67, table_width=1150,
                                 row_width=75, table_policy=mvTable_SizingStretchSame, transformation=True, transformation_card_num=Card_Number)
    
    
    
    with group(tag=f'Special_Skills_Button_Group_Card_{Card_Number}_{Super_Number}', parent=f'Specials_Tab_Card_{Card_Number}', horizontal=True):
        add_text('Special Skills', color=(255,50,50), parent=f'Special_Skills_Button_Group_Card_{Card_Number}_{Super_Number}', tag=f'Special_Skills_Text_Card_{Card_Number}_{Super_Number}')
        add_button(label='Add Skill', tag=f'Special_Skills_Button_Add_Card_{Card_Number}_{Super_Number}', callback=Special_Skills_Add, parent=f'Special_Skills_Button_Group_Card_{Card_Number}_{Super_Number}')
        add_button(label='Del Skill', tag=f'Special_Skills_Button_Del_Card_{Card_Number}_{Super_Number}', callback=Special_Skills_Del, parent=f'Special_Skills_Button_Group_Card_{Card_Number}_{Super_Number}')
        # bind_item_theme(f'Special_Skills_Button_Add_Card_{Card_Number}_{Super_Number}', Themes.Buttons)
        # bind_item_theme(f'Special_Skills_Button_Del_Card_{Card_Number}_{Super_Number}',Themes.Buttons)
    Widget_Aliases.tags_to_delete.append(f'Special_Skills_Text_Card_{Card_Number}_{Super_Number}')
    Widget_Aliases.tags_to_delete.append(f'Specials_Table_Group_Card_{Card_Number}_{Super_Number}')
    Widget_Aliases.tags_to_delete.append(f'Special_Skills_Button_Group_Card_{Card_Number}_{Super_Number}')
    Widget_Aliases.tags_to_delete.append(f'Special_Skills_Button_Add_Card_{Card_Number}_{Super_Number}')
    Widget_Aliases.tags_to_delete.append(f'Special_Skills_Button_Del_Card_{Card_Number}_{Super_Number}')
    
    with group(horizontal=True, parent=f'Specials_Tab_Card_{Card_Number}', tag=f'Specials_Table_Group_Card_{Card_Number}_{Super_Number}'):
        Specials_tags = Table_Inputs(table_name=f'Specials_Card_{Card_Number}_{Super_Number}', row_name=f'Specials_Table_Row_Card_{Card_Number}_{Super_Number}', class_name=Specials,
                              used_in_loop=True, loop_number=Super_Number, use_child_window=True, child_parent=f'Specials_Table_Group_Card_{Card_Number}_{Super_Number}', child_tag=f'Specials_Child_Window_Card_{Card_Number}_{Super_Number}',
                              table_height=90, table_width=1134, child_height=110, child_width=1139, combo=True, combo_tag=Specials.row_names[1], combo_list=Efficacy_Values.combo_list,
                              transformation=True, transformation_card_num=Card_Number)
        print(Specials_tags)
        
        with group(horizontal=False, tag=f'Specials_Group_Card_{Card_Number}_{Super_Number}'):
            with group(horizontal=True, tag=f'Specials_Aim_Target_Group_Card_{Card_Number}_{Super_Number}'):
                add_text('Aim Target:', tag=f'Special_Aim_Target_Text_Card_{Card_Number}_{Super_Number}')
                add_input_text(tag=f'Special_Set_Aim_Target_Input_Card_{Card_Number}_{Super_Number}', width=String_Length.length[0], callback=Text_Resize, hint='Aim Target')
            with group(horizontal=True, tag=f'Specials_Increase_Rate_Group_Card_{Card_Number}_{Super_Number}'):
                add_text('Inc Rate:    ', tag=f'Special_Increase_Rate_Text_Card_{Card_Number}_{Super_Number}')
                add_input_text(tag=f'Special_Set_Increase_Rate_Input_Card_{Card_Number}_{Super_Number}', width=String_Length.length[0], callback=Text_Resize, hint='Inc Rate')
            with group(horizontal=True, tag=f'Specials_Level_Bonus_Group_Card_{Card_Number}_{Super_Number}'):
                add_text('Lvl Bonus:  ', tag=f'Special_Level_Bonus_Text_Card_{Card_Number}_{Super_Number}')
                add_input_text(tag=f'Special_Set_Level_Bonus_Input_Card_{Card_Number}_{Super_Number}', width=String_Length.length[0], callback=Text_Resize, hint='Level Bonus')
                
    add_separator(parent=f'Specials_Tab_Card_{Card_Number}', tag=f'Specials_Separator_Card_{Card_Number}_{Super_Number}')
    
    items_to_delete = [f'Specials_Group_Card_{Card_Number}_{Super_Number}', f'Specials_Aim_Target_Group_Card_{Card_Number}_{Super_Number}', 
                       f'Special_Aim_Target_Text_Card_{Card_Number}_{Super_Number}', f'Special_Set_Aim_Target_Input_Card_{Card_Number}_{Super_Number}',
                       f'Specials_Increase_Rate_Group_Card_{Card_Number}_{Super_Number}', f'Special_Increase_Rate_Text_Card_{Card_Number}_{Super_Number}',
                       f'Special_Set_Increase_Rate_Input_Card_{Card_Number}_{Super_Number}', f'Specials_Level_Bonus_Group_Card_{Card_Number}_{Super_Number}',
                       f'Special_Level_Bonus_Text_Card_{Card_Number}_{Super_Number}', f'Special_Set_Level_Bonus_Input_Card_{Card_Number}_{Super_Number}',
                       f'Special_Set_Group_Card_{Card_Number}_1_{Super_Number}', f'Special_Name_Text_Card_{Card_Number}_{Super_Number}',
                       f'Special_Set_Name_Input_Card_{Card_Number}_{Super_Number}', f'Special_Set_Group_Card_{Card_Number}_2_{Super_Number}',
                       f'Special_Desc_Text_Card_{Card_Number}_{Super_Number}', f'Special_Set_Desc_Input_Card_{Card_Number}_{Super_Number}',
                       f'Special_Set_Group_Card_{Card_Number}_3_{Super_Number}', f'Special_Cond_Text_Card_{Card_Number}_{Super_Number}',
                       f'Special_Set_Cond_Input_Card_{Card_Number}_{Super_Number}', f'Card_Specials_Text_Card_{Card_Number}_{Super_Number}',
                       f'Special_Skills_Text_Card_{Card_Number}_{Super_Number}', f'Special#_Text_Card_{Card_Number}_{Super_Number}',
                       f'Specials_Table_Group_Card_{Card_Number}_{Super_Number}', f'Specials_Separator_Card_{Card_Number}_{Super_Number}']
    
    for i in range(len(items_to_delete)):
        Widget_Aliases.tags_to_delete.append(items_to_delete[i])
    
    # Widget_Aliases.button_tags_to_delete.append(f'Specials_Group_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Specials_Aim_Target_Group_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Aim_Target_Text_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Set_Aim_Target_Input_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Specials_Increase_Rate_Group_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Increase_Rate_Text_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Set_Increase_Rate_Input_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Specials_Level_Bonus_Group_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Level_Bonus_Text_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Set_Level_Bonus_Input_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Set_Group_{Card_Number}_1_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Name_Text_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Set_Name_Input_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Set_Group_{Card_Number}_2_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Desc_Text_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Set_Desc_Input_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Set_Group_{Card_Number}_3_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Cond_Text_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Set_Cond_Input_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special#_Text_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Card_Specials_Text_{Card_Number}_{Super_Number}')
    # Widget_Aliases.button_tags_to_delete.append(f'Special_Skills_Text_{Card_Number}_{Super_Number}')
    

def Specials_Del(app_data):
    Card_Number = Table_ID(app_data)
    Super_Number = Row_Checker(f'Special#_Text_Card_{Card_Number}_')
    items_to_delete = [f'Specials_Group_Card_{Card_Number}_{Super_Number - 1}', f'Specials_Aim_Target_Group_Card_{Card_Number}_{Super_Number - 1}', 
                       f'Special_Aim_Target_Text_Card_{Card_Number}_{Super_Number - 1}', f'Special_Set_Aim_Target_Input_Card_{Card_Number}_{Super_Number - 1}',
                       f'Specials_Increase_Rate_Group_Card_{Card_Number}_{Super_Number - 1}', f'Special_Increase_Rate_Text_Card_{Card_Number}_{Super_Number - 1}',
                       f'Special_Set_Increase_Rate_Input_Card_{Card_Number}_{Super_Number - 1}', f'Specials_Level_Bonus_Group_Card_{Card_Number}_{Super_Number - 1}',
                       f'Special_Level_Bonus_Text_Card_{Card_Number}_{Super_Number - 1}', f'Special_Set_Level_Bonus_Input_Card_{Card_Number}_{Super_Number - 1}',
                       f'Special_Set_Group_Card_{Card_Number}_1_{Super_Number - 1}', f'Special_Name_Text_Card_{Card_Number}_{Super_Number - 1}',
                       f'Special_Set_Name_Input_Card_{Card_Number}_{Super_Number - 1}', f'Special_Set_Group_Card_{Card_Number}_2_{Super_Number - 1}',
                       f'Special_Desc_Text_Card_{Card_Number}_{Super_Number - 1}', f'Special_Set_Desc_Input_Card_{Card_Number}_{Super_Number - 1}',
                       f'Special_Set_Group_Card_{Card_Number}_3_{Super_Number - 1}', f'Special_Cond_Text_Card_{Card_Number}_{Super_Number - 1}',
                       f'Special_Set_Cond_Input_Card_{Card_Number}_{Super_Number - 1}', f'Card_Specials_Text_Card_{Card_Number}_{Super_Number - 1}',
                       f'Special_Skills_Text_Card_{Card_Number}_{Super_Number - 1}', f'Special#_Text_Card_{Card_Number}_{Super_Number - 1}',
                       f'Specials_Table_Group_Card_{Card_Number}_{Super_Number - 1}', f'Special_Skills_Button_Add_Card_{Card_Number}_{Super_Number - 1}',
                       f'Special_Skills_Button_Del_Card_{Card_Number}_{Super_Number - 1}', f'Special_Skills_Button_Group_Card_{Card_Number}_{Super_Number - 1}']
    
    for i in range(Row_Checker(f'Specials_Table_Row_Card_{Card_Number}_{Super_Number - 1}')):
        
        for u in range(len(Specials.row_names)):
            if does_alias_exist(Specials.row_names[u] + str(Card_Number) + str(Super_Number - 1) + str(i)):
                delete_item(Specials.row_names[u] + str(Card_Number) + str(Super_Number - 1) + str(i))
    delete_item(f'Specials_Card_{Card_Number}_{Super_Number - 1}')
    delete_item(f'Specials_Child_Window_Card_{Card_Number}_{Super_Number - 1}')
    
    for y in range(2):
        if does_alias_exist(Card_Specials.row_names[y] + str(Card_Number) + str(Super_Number - 1) + str(y)):
            delete_item(Card_Specials.row_names[y] + str(Card_Number) + str(Super_Number - 1) + str(y))
    delete_item(f'Card_Specials_Card_{Card_Number}_{Super_Number - 1}')
    delete_item(f'Specials_Separator_Card_{Card_Number}_{Super_Number - 1}')
    delete_item(f'Specials_Separator_Card_{Card_Number}_{Super_Number - 1}')
    
    Delete_Items(items_to_delete)
    
def Special_Skills_Add(app_data):
        # Use app_data to get last digit, which tells which card tab to add the table rows to.
        # print(app_data)
        Card_Number = Get_Card_Number(app_data)
        Super_Number = Table_ID(app_data)
        # Super_Number = Row_Checker(f'Specials_Table_Row_Card_{Card_Number}_{Super_Number}')
        # print(f'Card Number: Card_{Card_Number}')
        # print(f'Super Number: {Super_Number}')
        
        # Dynamically check existing rows
        Rows = Row_Checker(f'Specials_Table_Row_Card_{Card_Number}_{Super_Number}')
        
        # print(f'Rows: {Rows}')
        # # print(f'Table Row Name: Passive_Skill_Table_Row_Card_{Card_Number}{Rows}')
        add_table_row(tag=f'Specials_Table_Row_Card_{Card_Number}_{Super_Number}{Rows}', parent=f'Specials_Card_{Card_Number}_{Super_Number}')
        for i in range(len(Specials.row_names)):
                # Specials.row_names[2] is Efficacy Type
                if Specials.row_names[i] == Specials.row_names[1]:
                        add_combo(tag=Specials.row_names[i] + str(Card_Number) + str(Super_Number) + str(Rows), items=Efficacy_Values.combo_list, width=149, parent=f'Specials_Table_Row_Card_{Card_Number}_{Super_Number}{Rows}')
                        set_value(Specials.row_names[i] + str(Card_Number) + str(Super_Number) + str(Rows), Efficacy_Values.combo_list[0])
                else:
                        add_input_text(tag=Specials.row_names[i] + str(Card_Number) + str(Super_Number) + str(Rows), hint=Specials.column_names[i], width=99, default_value='', parent=f'Specials_Table_Row_Card_{Card_Number}_{Super_Number}{Rows}')
                        
        # configure_item(f'Passive_Rows_in_Table_Card_{Card_Number}', default_value=f'Rows: {Rows + 1}')
        set_item_height(f'Specials_Card_{Card_Number}_{Super_Number}', (24 * (Rows + 1) + 23))
        set_item_height(f'Specials_Child_Window_Card_{Card_Number}_{Super_Number}', (25 * (Rows + 1) + 38))
                        
        # # Check previous row value for a name, set the new row name if it exists
        # # print(Specials.row_names[0] + str(Rows - 1))
        # if get_value(Specials.row_names[0] + str(Card_Number) + str(Rows - 1)):
        #         set_value(Specials.row_names[0] + str(Card_Number) + str(Rows), get_value(Specials.row_names[0] + str(Card_Number) + str(Rows - 1)))
        #         Text_Resize(Specials.row_names[0] + str(Card_Number) + str(Rows))
                
                
def Special_Skills_Del(app_data):
        # Use app_data to get last digit, which tells which card tab to add the table rows to.
        Card_Number = Get_Card_Number(app_data)
        Super_Number = Table_ID(app_data)
        # print(f'Table Number: {Table_Number}')
        
        # Dynamically check existing rows
        Rows = Row_Checker(f'Specials_Table_Row_Card_{Card_Number}_{Super_Number}')
        # print(f'Rows: {Rows}')
        # print(f'Table Row Name: Passive_Skill_Table_Row_{Table_Number}{Rows}')
        delete_item(f'Specials_Table_Row_Card_{Card_Number}_{Super_Number}{Rows - 1}')
        for i in range(len(Specials.row_names)):
                # Specials.row_names[2] is Efficacy Type
                        delete_item(Specials.row_names[i] + str(Card_Number) + str(Super_Number) + str(Rows - 1))
                        
        # configure_item(f'Passive_Rows_in_Table_{Table_Number}', default_value=f'Rows: {Rows - 1}')
        set_item_height(f'Specials_Card_{Card_Number}_{Super_Number}', (24 * (Rows - 1) + 23))
        set_item_height(f'Specials_Child_Window_Card_{Card_Number}_{Super_Number}', (25 * (Rows - 1) + 38))
    

def Unit_Checks(card_information):
    Lua_Special_View_IDs = []
    LUA_Names = []
    # Passive_ID = ''


    config = Config_Read()
    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
    # con.row_factory = lambda cursor, row: row
    cur = con.cursor()

    if get_value('EZA_Check') is True:
        if len(card_information['specials']) == 2:
            Lua_Special_View_IDs.append(card_information['specials'][1]['special_view_id'])
        elif len(card_information['specials']) == 4:
            Lua_Special_View_IDs.append(card_information['specials'][2]['special_view_id'])
            Lua_Special_View_IDs.append(card_information['specials'][3]['special_view_id'])
        elif len(card_information['specials']) == 6:
            Lua_Special_View_IDs.append(card_information['specials'][3]['special_view_id'])
            Lua_Special_View_IDs.append(card_information['specials'][4]['special_view_id'])
            Lua_Special_View_IDs.append(card_information['specials'][5]['special_view_id'])
    else:
        for i in range(len(card_information['specials'])):
            Lua_Special_View_IDs.append(card_information['specials'][i]['special_view_id'])


    # print(get_value('Active_Skill_Check'))
    if get_value('Active_Skill_Check') is True:
        Lua_Special_View_IDs.append(card_information['card']['active_skill_view_id'])
        # print('Active Skill: ✔')
    else:
        # print('Active Skill: ❌')
        pass

    # print(get_value('Finish_Skill_Check'))
    if get_value('Finish_Skill_Check') is True:
        for i in range(len(card_information['finish_skills'])):
            Lua_Special_View_IDs.append(card_information['finish_skills'][i]['special_view_id'])
        # print('Finish Skill: ✔')
    else:
        # print('Finish Skill: ❌')
        pass

    # print(get_value('Standby_Skill_Check'))
    if get_value('Standby_Skill_Check') is True:
        Lua_Special_View_IDs.append(card_information['standby_skills'][0]['special_view_id'])
        # print('Standby Skill: ✔')
    else:
        # print('Standby Skill: ❌')
        pass



    for i in range(len(Lua_Special_View_IDs)):

        cur.execute('SELECT script_name FROM special_views WHERE id = ' + str(Lua_Special_View_IDs[i]))
        ids = cur.fetchall()

        LUA_Names.append(ids)
    LUA_Names = [item[0][0] for item in LUA_Names]


    if get_value('EZA_Check') is True:
        Passive_ID = card_information['optimal_awakening_growth']['passive_skill_id']
    else:
        Passive_ID = card_information['card']['passive_skill_set_id']


    # Dokkan Wiki used the id of the row in the passive_transformation section of the JSON
    # Noting this in case I feel the need to revise this section of code
    p = []
    cur.execute('SELECT passive_skill_id FROM passive_skill_set_relations WHERE passive_skill_set_id = ' + str(Passive_ID))
    for value in cur.fetchall():
        p.append(value[0])
        # 
    t = []
    for value in p:
        cur.execute('SELECT efficacy_type,passive_skill_effect_id,eff_value3 FROM passive_skills WHERE id = ' + str(value))
        z = cur.fetchall()
        t.append(z[0])

    for i in range(len(t)):
        #Passive Skill Effect Check
        if t[i][1] is not None:
            cur.execute('SELECT script_name FROM passive_skill_effects WHERE id = ' + str(t[i][1]))
            pse = cur.fetchone()
            LUA_Names.append(pse[0])

    con.close()

    if 'passive_animations' in card_information:
        for i in range(len(card_information['passive_animations'])):

            if card_information['passive_animations'][i]['efficacy_type'] == 119:
                if 0 < card_information['passive_animations'][i]['id'] <= 9:
                    LUA_Names.append('as000' + str(card_information['passive_animations'][i]['id']))
                elif 10 <= card_information['passive_animations'][i]['id'] <= 99:
                    LUA_Names.append('as00' + str(card_information['passive_animations'][i]['id']))
                elif 100 <= card_information['passive_animations'][i]['id'] <= 999:
                    LUA_Names.append('as0' + str(card_information['passive_animations'][i]['id']))

            elif card_information['passive_animations'][i]['efficacy_type'] == 120:
                if 0 < card_information['passive_animations'][i]['id'] <= 9:
                    LUA_Names.append('c000' + str(card_information['passive_animations'][i]['id']))
                elif 10 <= card_information['passive_animations'][i]['id'] <= 99:
                    LUA_Names.append('c00' + str(card_information['passive_animations'][i]['id']))
                elif 100 <= card_information['passive_animations'][i]['id'] <= 999:
                    LUA_Names.append('c0' + str(card_information['passive_animations'][i]['id']))


    if does_alias_exist('Number_Of_Luas') is True:
        remove_alias('Number_Of_Luas')
        for i in range(get_value('Lua_alias_to_remove')):
            # if does_alias_exist(f'Lua_{i}') is True:
            remove_alias(f'Lua_{i}')        
    if does_alias_exist('Lua_Downloader_Dir_Name') is True:
        remove_alias('Lua_Downloader_Dir_Name')
    if does_alias_exist('Lua_Downloader_Dir_Name_Card_ID') is True:
        remove_alias('Lua_Downloader_Dir_Name_Card_ID')

    set_value('Lua_alias_to_remove', len(LUA_Names))

    with value_registry():
        add_int_value(default_value=len(LUA_Names), tag="Number_Of_Luas")
        if get_value('ENG_Check'):
            add_string_value(default_value=card_information['card']['name'], tag='Lua_Downloader_Dir_Name')
        else:
            add_string_value(default_value=get_value('CardName'), tag='Lua_Downloader_Dir_Name')

        add_string_value(default_value=card_information['card']['id'], tag='Lua_Downloader_Dir_Name_Card_ID')
        for i in range(len(LUA_Names)):
            add_string_value(default_value=LUA_Names[i], tag=f'Lua_{i}')

    print(LUA_Names)






    return LUA_Names