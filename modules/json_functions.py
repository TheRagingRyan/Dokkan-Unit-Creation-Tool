from dearpygui.dearpygui import *
from . cards import Card_Table_Combos, Link_Skills_Query, Synced_Callback, EZA_Callback, Rarity_Callback, Element_Callback, Name_Change_Callback,Ex_Super_Callback, Ex_Super_Combo_Callback, Ex_Super_Probablity_Callback
from . categories import Categories_Activated
from . effect_pack import Effect_Packs_Widgets
from . passive import Passive_Add, Passive_Del
from . specials import Special_Skills_Add, Special_Skills_Del, Specials_Add, Specials_Del
from . special_views import Special_View_Widgets
from . leader import Leader_Combo, Leader_Cat_Selection, Leader_Efficacy_Value_Changer, Leader_Resize, Resize_Widget, Resize_Description
from . download import download_image
from . active_skill import Active_Skill_Add, Active_Skill_Del
import os
from . classes import Card_Checks, Card, Passive_Skill, Active_Skill, Active_Skill_Set, Leader_Skill_Info, Standby_Skill_Set, Standby_Skill, Finish_Skill_Set, Finish_Skill, Efficacy_Values, String_Length, Transformation_Descriptions, Battle_Params, Widget_Aliases, Special_Set, Specials, Card_Specials, Dokkan_Field, Special_Views, Effect_Pack
from . functions import Delete_Items, Text_Resize, Table_Combo_Inputs, Table_Inputs, Resize_Table
from . custom_unit import Main_Tab_Bar_Callback
import re

########################################################################################################################################################################################################
def Transformation_Texture_Registry(json_length):
    for i in range(json_length):
        if not does_alias_exist(f'Placeholder_Image_Texture_{i + 1}'):
            with texture_registry():
                width, height, channels, data = load_image('logo/Placeholder.png')
                add_dynamic_texture(width=250, height=250, default_value=data, tag=f'Placeholder_Image_Texture_{i + 1}')
                ### Checking Element ID to change the border color
                # if Card_Checks.element_id[i] in (0, 10, 20):
                    # print(f'Element: {Card_Checks.element_id[i]}')
                width, height, channels, data = load_image('logo/Custom_Border_Border_AGL.png')
                add_dynamic_texture(width=250, height=250, default_value=data, tag=f'Custom_Border_Thumb_Border_Texture_{i + 1}')
                width, height, channels, data = load_image('logo/Custom_Border_Background_AGL.png')
                add_dynamic_texture(width=250, height=250, default_value=data, tag=f'Custom_Border_Thumb_Background_Texture_{i + 1}')
                width, height, channels, data = load_image('logo/Placeholder.png')
                add_dynamic_texture(width=250, height=250, default_value=data, tag=f'Card_Thumb_Texture_{i + 1}')
        # Widget_Aliases.tags_to_delete.append(f'Placeholder_Image_Texture_{i + 1}')
        # Widget_Aliases.tags_to_delete.append(f'Custom_Border_Thumb_Border_Texture_{i + 1}')
        # Widget_Aliases.tags_to_delete.append(f'Custom_Border_Thumb_Background_Texture_{i + 1}')
        # Widget_Aliases.tags_to_delete.append(f'Card_Thumb_Texture_{i + 1}')
        
######################################################################################################################################################################################################## 
def Create_Tabs(json_length):
    Transformation_Texture_Registry(json_length)
    # Minus 1 because there will always be a main tab, which counts as a unit.
    Delete_Items('Add_Card_Tab')
    
    for i in range(json_length - 1):
        with tab(label=f'Unit {i + 2}', tag=f'Main_Card_Tab_{i + 1}', parent='Main_Tab_Bar'):

            Widget_Aliases.tags_to_delete.append(f'Main_Card_Tab_{i + 1}')
            

            with tab_bar(label=f'Card {i + 2}', tag=f'Card_Input_Tab_Bar_{i + 1}'):
                Widget_Aliases.tags_to_delete.append(f'Card_Input_Tab_Bar_{i + 1}')
                
                with tab(label=f'Card Input', tag=f'Card_Input_Tab_{i + 1}'):
                    Widget_Aliases.tags_to_delete.append(f'Card_Input_Tab_{i + 1}')
                    add_text(default_value='',tag=f'Card_Name_Display_{i + 1}', color=(255, 215, 0), parent=f'Card_Input_Tab_{i + 1}')
                    Widget_Aliases.tags_to_delete.append(f'Card_Name_Display_{i + 1}')
                    bind_item_font(f'Card_Name_Display_{i + 1}', 'Arial_Bold_Font')
                    # with group(tag=f'Card_Input_Image_Widget_Group_{i + 1}', horizontal=True, parent=f'Card_Input_Tab_{i + 1}'):
                    add_image(f'Placeholder_Image_Texture_{i + 1}', tag=f'Placeholder_Image_{i + 1}')
                    add_image(f'Custom_Border_Thumb_Background_Texture_{i + 1}', tag=f'Custom_Border_Thumb_Background_{i + 1}', show=False)
                    add_image(f'Card_Thumb_Texture_{i + 1}', tag=f'card_thumb_display_{i + 1}', show=False)
                    add_image(f'Custom_Border_Thumb_Border_Texture_{i + 1}', tag=f'Custom_Border_Thumb_Border_{i + 1}', show=False)
                    add_separator()
                    

                with tab(label=f'Specials', tag=f'Specials_Tab_Card_{i + 1}'):
                    pass

                with tab(label=f'Leader Skill', tag=f'Leader_Skill_{i + 1}', show=False):
                    pass

                with tab(label=f'Active Skill', tag=f'Active_Skill_Card_{i + 1}', show=False):
                    pass

                with tab(label=f'Standby/Finish Skill', tag=f'Standby/Finish_Skill_{i + 1}', show=False):
                    pass
                
                with tab(label='Dokkan Field', tag=f'Dokkan_Field_{i + 1}', show=False):
                    pass
                
                with tab(label='Battle Params', tag=f'Battle_Params_{i + 1}', show=False):
                    pass
                
                with tab(label='Categories', tag=f'Categories_{i + 1}', show=True):
                    pass
                
    add_tab_button(tag=f'Add_Card_Tab', label='+', parent='Main_Tab_Bar', callback=Main_Tab_Bar_Callback, trailing=True)
########################################################################################################################################################################################################       
def Card_Thumb_Display(json_length, json_dict):
    card_id_0_assets = json_dict[f'Card 1']['Card Thumb']
    width, height, channels, thumb_data = load_image(f'thumbs/thumb/{card_id_0_assets}')
    Card_Checks.json_unit_card_ids.clear()
    
    for i in range(json_length):
        card_id_0_assets = json_dict[f'Card {i + 1}']['Card Thumb']
        ### Appending just the card ID to this for the sake of units loaded from a JSON being saved again. Otherwise an error will occur as I use Card_Checks.card_ids for saving a queried unit.
        numbers_only = re.sub(r'\D', '', card_id_0_assets)
        Card_Checks.json_unit_card_ids.append(numbers_only)
        set_value(f'Card_Name_Display_{i}', json_dict[f'Card {i + 1}']['Card']['Name'])
        element_type = json_dict[f'Card {i + 1}']['Card']['Element']
        if 'AGL' in element_type:
            element_type = 'AGL'
        elif 'TEQ' in element_type:
            element_type = 'TEQ'
        elif 'INT' in element_type:
            element_type = 'INT'
        elif 'PHY' in element_type:
            element_type = 'PHY'
        else:
            element_type = 'STR'
            
        if i == 0:
            width, height, channels, thumb_data = load_image(f'thumbs/thumb/{card_id_0_assets}')
        else:
            if os.path.exists(f'assets/character/thumb/{card_id_0_assets}'):
                width, height, channels, thumb_data = load_image(f'thumbs/thumb/{card_id_0_assets}')
            else:
                url = f'https://dokkaninfo.com/assets/japan/character/thumb/{card_id_0_assets}'
                # download_image('assets/character/thumb/', url, f'{card_id_0_assets}')
                width, height, channels, thumb_data = load_image(f'thumbs/thumb/{card_id_0_assets}')
        with texture_registry():
            Delete_Items(f'Custom_Border_Thumb_Border_Texture_{element_type}')
            Delete_Items(f'Custom_Border_Thumb_Background_Texture_{element_type}')
            width, height, channels, border_data = load_image(f'logo/Custom_Border_Border_{element_type}.png')
            add_dynamic_texture(width=250, height=250, default_value=border_data, tag=f'Custom_Border_Thumb_Border_Texture_{element_type}')
            width, height, channels, bg_data = load_image(f'logo/Custom_Border_Background_{element_type}.png')
            add_dynamic_texture(width=250, height=250, default_value=bg_data, tag=f'Custom_Border_Thumb_Background_Texture_{element_type}')
                
        # Just grab this 'Placeholder_Image_0' to get the same position, don't know why I was trying to grab the other ones when I can just use this one.
        # This image shit was coded pretty poorly by me, may have to recode it later, hopefully not.
        set_value(f'Card_Thumb_Texture_{i}', thumb_data)
        set_value(f'Custom_Border_Thumb_Border_Texture_{i}', border_data)
        set_value(f'Custom_Border_Thumb_Background_Texture_{i}', bg_data)
        set_item_pos(f'Custom_Border_Thumb_Background_{i}', [8,110])
        set_item_pos(f'card_thumb_display_{i}', [8,110])
        set_item_pos(f'Custom_Border_Thumb_Border_{i}', [8,110])
        configure_item(f'card_thumb_display_{i}', show=True)
        configure_item(f'Custom_Border_Thumb_Background_{i}', show=True)
        configure_item(f'card_thumb_display_{i}', show=True)
        configure_item(f'Custom_Border_Thumb_Border_{i}', show=True)
    
########################################################################################################################################################################################################

def Card_Widgets(json_length, json_dict):
    rarity_combo = ['(N)', '(R)', '(SR)', '(SSR)', '(TUR)', '(LR)']
    element_combo = ['AGL', 'TEQ', 'INT', 'STR', 'PHY', 'Super AGL', 'Super TEQ', 'Super INT', 'Super STR', 'Super PHY', 'Extreme AGL', 'Extreme TEQ', 'Extreme INT', 'Extreme STR', 'Extreme PHY']
    element_dict = {'0': 'AGL', '1': 'TEQ', '2': 'INT', '3': 'STR', '4': 'PHY', '10': 'Super AGL', '11': 'Super TEQ', '12': 'Super INT', '13': 'Super STR', '14': 'Super PHY', '20': 'Extreme AGL', '21': 'Extreme TEQ', '22': 'Extreme INT', '23': 'Extreme STR', '24' : 'Extreme PHY'}
    link_skill_combo = Link_Skills_Query()
    potential_board_combo = ['+3k to stats', '+5k to stats', '+7k to stats']
    combos = {5 : rarity_combo, 12 : element_combo, 23 : link_skill_combo, 24 : link_skill_combo, 25 : link_skill_combo, 26 : link_skill_combo, 27 : link_skill_combo, 28 : link_skill_combo, 29 : link_skill_combo, 52 : potential_board_combo}
    Card_Table_Combos.rarity_combo = rarity_combo
    Card_Table_Combos.element_combo = element_combo
    Card_Table_Combos.element_dict = element_dict
    Card_Table_Combos.link_skill_combo = link_skill_combo
    Card_Table_Combos.potential_board_combo = potential_board_combo
    
    
    for card_num in range(json_length):
        with group(horizontal=True, tag=f'Card_Information_Text_Group_{card_num}', parent=f'Card_Input_Tab_{card_num}'):
            add_text('Card Information', color=(255,50,50), parent=f'Card_Information_Text_Group', tag=f'Card_Information_Text_{card_num}')
            add_checkbox(label='EZA', default_value=False, tag=f'EZA_Checkbox_{card_num}', callback=EZA_Callback, parent='Card_Information_Text_Group')
            set_value(f'EZA_Checkbox_{card_num}', json_dict[f'Card {card_num + 1}']['EZA'])
        Widget_Aliases.tags_to_delete.append(f'Card_Information_Text_{card_num}')
        Widget_Aliases.tags_to_delete.append(f'EZA_Checkbox_{card_num}')
        Widget_Aliases.tags_to_delete.append(f'Card_Information_Text_Group_{card_num}')

            ## 5 Rarity, 12 Element, 23,24,25,26,27,28,29 Link Skills, 52 Potential Board
        sss = Table_Combo_Inputs(table_name=f'Card{card_num}_Table', row_name=f'Card{card_num}_Table_Row', class_name=Card,
                     table_parent=f'Card_Input_Tab_{card_num}', table_height=83, table_width=1650,
                     row_width=85, transformation_card_num=card_num, combo_columns=[5,12,23,24,25,26,27,28,29,52], 
                     callback_columns=[1, 5, 12, 23, 24, 25, 26, 27, 28, 29, 52], callback={1 : Name_Change_Callback, 5 : Rarity_Callback, 12 : Element_Callback, 23 : Synced_Callback, 24 : Synced_Callback, 25 : Synced_Callback, 26 : Synced_Callback, 27 : Synced_Callback, 28 : Synced_Callback, 29 : Synced_Callback, 52 : Synced_Callback}, combo_list=combos)
        z = 0
        for key, value in json_dict[f'Card {card_num + 1}']['Card'].items():
            if key == 'Card ID':
                set_value(Card.row_names[z] + '_Card_' + str(card_num) + '_Row_0', value[:-1] + '0')
                set_value(Card.row_names[z] + '_Card_' + str(card_num) + '_Row_1', value)
            else:
                set_value(Card.row_names[z] + '_Card_' + str(card_num) + '_Row_0', value)
                set_value(Card.row_names[z] + '_Card_' + str(card_num) + '_Row_1', value)
            z += 1

########################################################################################################################################################################################################       
def Passive_Widgets(json_length, json_dict):
        for cards in range(json_length):
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
                        
                Passive_Skill.rows = len(json_dict[f'Card {cards + 1}']['Passive']['Skills'])
                configure_item(f'Passive_Rows_in_Table_{cards}', default_value=f'Rows: {Passive_Skill.rows}')

                sss = Table_Inputs(table_name=f'Passive_Skill_Table_{cards}', row_name=f'Passive_Skill_Table_Row_{cards}', table_parent=f'Card_Input_Tab_{cards}', use_child_window=False, 
                         class_name=Passive_Skill, combo=True, combo_tag=Passive_Skill.row_names[2], combo_list=Efficacy_Values.combo_list, combo_column_name=Passive_Skill.column_names[2],
                         table_width=1775, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=cards)
                
                for row in range(len(json_dict[f'Card {cards + 1}']['Passive']['Skills'])):
                    z = 0
                    set_value(Passive_Skill.row_names[0] + '_Card_' + str(cards) + '_Row_' + str(row), json_dict[f'Card {cards + 1}']['Passive']['Name'])
                    Text_Resize(Passive_Skill.row_names[0] + '_Card_' + str(cards) + '_Row_' + str(row))
                    
                    for key, value in json_dict[f'Card {cards + 1}']['Passive']['Skills'][row].items():
                        if Passive_Skill.row_names[z + 1] == Passive_Skill.row_names[10]:
                            set_value(Passive_Skill.row_names[z + 1] + '_Card_' + str(cards) + '_Row_' + str(row), value)
                            Text_Resize(Passive_Skill.row_names[10] + '_Card_' + str(cards) + '_Row_' + str(row))
                        else:
                            set_value(Passive_Skill.row_names[z + 1] + '_Card_' + str(cards) + '_Row_' + str(row), value)
                        z += 1
                # set_value(f'Passive_Desc_Text_Input_{cards}', json_dict[f'Card {cards + 1}']['Passive']['Desc'])
                        
                # print(sss[1])
                ### 5 Rarity, 12 Element, 23,24,25,26,27,28,29 Link Skills, 52 Potential Board
                        # Table_Combo_Inputs(table_name=f'Passive_Skill_Table_{cards}', row_name=f'Passive_Skill_Table_Row_{cards}', table_parent=f'Card_Input_Tab_{cards}', class_name=Passive_Skill,
                        #                    combo_columns=[5,12,23,24,25,26,27,28,29,52])
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
                print(max_width)
                set_item_width(f'Passive_Skill_Table_{cards}', max_width + 140)

                Delete_Items(f'Passive_Desc_Text_{cards}')
                Delete_Items(f'Passive_Desc_Text_Input_{cards}')
                add_text('Passive Skill Description', color=(255,50,0), parent=f'Card_Input_Tab_{cards}', tag=f'Passive_Desc_Text_{cards}')
                add_input_text(tag=f'Passive_Desc_Text_Input_{cards}', multiline=True, width=500, height=250, parent=f'Card_Input_Tab_{cards}')
                set_value(f'Passive_Desc_Text_Input_{cards}', json_dict[f'Card {cards + 1}']['Passive']['Desc'])
                Widget_Aliases.tags_to_delete.append(f'Passive_Desc_Text_{cards}')
                Widget_Aliases.tags_to_delete.append(f'Passive_Desc_Text_Input_{cards}')

########################################################################################################################################################################################################             
def Specials_Widgets(json_length, json_dict):
    
    for cards in range(json_length):
        with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Button_Add_Group_Card_{cards}'):
            add_button(label='Add Super', tag=f'Specials_Button_Add_Card_{cards}', callback=Specials_Add, parent=f'Specials_Button_Add_Group_Card_{cards}')
            add_button(label='Del Super', tag=f'Specials_Button_Del_Card_{cards}', callback=Specials_Del, parent=f'Specials_Button_Add_Group_Card_{cards}')
            Widget_Aliases.tags_to_delete.append(f'Specials_Button_Add_Group_Card_{cards}')
            Widget_Aliases.tags_to_delete.append(f'Specials_Button_Add_Card_{cards}')
            Widget_Aliases.tags_to_delete.append(f'Specials_Button_Del_Card_{cards}')

            Number_Of_Special_Sets = len(json_dict[f'Card {cards + 1}']['Specials'])


        for i in range(Number_Of_Special_Sets):
            rows_to_check = [f'Special#_Text_Card_{cards}_{i}',f'Special_Name_Text_Card_{cards}_{i}',f'Special_Set_Name_Input_Card_{cards}_{i}',f'Special_Aim_Target_Text_Card_{cards}_{i}',f'Special_Set_Aim_Target_Input_Card_{cards}_{i}',f'Special_Desc_Text_Card_{cards}_{i}',f'Special_Set_Desc_Input_Card_{cards}_{i}',f'Special_Increase_Rate_Text_Card_{cards}_{i}',
                         f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}',f'Special_Cond_Text_Card_{cards}_{i}',f'Special_Set_Cond_Input_Card_{cards}_{i}',f'Special_Level_Bonus_Text_Card_{cards}_{i}',f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}',f'Card_Specials_Text_Card_{cards}_{i}',f'Special_Skills_Text_Card_{cards}_{i}',f'Specials_Separator_Card_{cards}_{i}',
                         f'Special_Set_Group_Card_{cards}_1_{i}', f'Special_Set_Group_Card_{cards}_2_{i}', f'Special_Set_Group_Card_{cards}_3_{i}', f'Specials_Table_Group_Card_{cards}_{i}', f'Specials_Aim_Target_Group_Card_{cards}_{i}',
                         f'Special_Aim_Target_Text_Card_{cards}_{i}',f'Special_Set_Aim_Target_Input_Card_{cards}_{i}',f'Specials_Increase_Rate_Group_Card_{cards}_{i}',f'Special_Increase_Rate_Text_Card_{cards}_{i}',
                         f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}', f'Specials_Level_Bonus_Group_Card_{cards}_{i}', f'Special_Level_Bonus_Text_Card_{cards}_{i}', f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}',
                         f'Ex_Super_Checkbox_Card_{cards}_{i}', f'Ex_Super_Combo_Card_{cards}_{i}', f'Card_Specials_Text_Group_Card_{cards}_{i}', f'Ex_Super_Combo2_Card_{cards}_{i}',
                         f'Card_Specials_BGM_Text_Card_{cards}_{i}']

            for item in range(len(rows_to_check)):
                Delete_Items(rows_to_check[item])

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
            set_value(f'Special_Set_Name_Input_Card_{cards}_{i}', json_dict[f'Card {cards + 1}']['Specials'][i]['Name'])
            set_value(f'Special_Set_Desc_Input_Card_{cards}_{i}', json_dict[f'Card {cards + 1}']['Specials'][i]['Desc'])
            set_value(f'Special_Set_Cond_Input_Card_{cards}_{i}', json_dict[f'Card {cards + 1}']['Specials'][i]['Cond'])
            Text_Resize(f'Special_Set_Name_Input_Card_{cards}_{i}')
            Text_Resize(f'Special_Set_Desc_Input_Card_{cards}_{i}')
            Text_Resize(f'Special_Set_Cond_Input_Card_{cards}_{i}')

            with group(tag=f'Card_Specials_Text_Group_Card_{cards}_{i}', parent=f'Specials_Tab_Card_{cards}', horizontal=True):
                add_text('Card Specials', color=(255,50,50), parent=f'Card_Specials_Text_Group_Card_{cards}_{i}', tag=f'Card_Specials_Text_Card_{cards}_{i}')
                add_checkbox(label='Ex Super', default_value=False, tag=f'Ex_Super_Checkbox_Card_{cards}_{i}', callback=Ex_Super_Callback, parent=f'Card_Specials_Text_Group_Card_{cards}_{i}')
                add_combo(['When Super', 'When Additional', 'When Crit'], tag=f'Ex_Super_Combo_Card_{cards}_{i}', callback=Ex_Super_Combo_Callback,parent=f'Card_Specials_Text_Group_Card_{cards}_{i}', default_value='When Super', show=False, width=125)
                add_combo(['10','20','30','40','50', '60', '70', '80', '90', '100'], tag=f'Ex_Super_Combo2_Card_{cards}_{i}', callback=Ex_Super_Combo_Callback,parent=f'Card_Specials_Text_Group_Card_{cards}_{i}', default_value='60', show=False, width=50)
                add_input_text(tag=f'Card_Specials_BGM_Text_Card_{cards}_{i}', width=50, callback=Ex_Super_Combo_Callback, default_value='69', show=False, parent=f'Card_Specials_Text_Group_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Card_Specials_Text_Card_{cards}_{i}')
    
            Card_Specials.rows = len(json_dict[f'Card {cards + 1}']['Specials'][i]['Card Specials'])
            CS_tags = Table_Inputs(table_name=f'Card_Specials_Card_{cards}_{i}', row_name=f'Card_Specials_Table_Row_Card_{cards}_{i}', class_name=Card_Specials,
                                 used_in_loop=True, loop_number=i, use_child_window=False, table_parent=f'Specials_Tab_Card_{cards}', table_height=67, table_width=1150,
                                 row_width=75, table_policy=mvTable_SizingStretchSame, transformation=True, transformation_card_num=cards)
            for row in range(Card_Specials.rows):
                z = 0
                for key, value in json_dict[f'Card {cards + 1}']['Specials'][i]['Card Specials'][row].items():
                    set_value(Card_Specials.row_names[z] + '_Card_' + str(cards) + '_Row_' + str(i) + str(row), value)
                    z += 1
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
            Widget_Aliases.tags_to_delete.append(f'Ex_Super_Checkbox_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Ex_Super_Combo_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Card_Specials_Text_Group_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Ex_Super_Combo2_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Card_Specials_BGM_Text_Card_{cards}_{i}')
            
            Specials.rows = len(json_dict[f'Card {cards + 1}']['Specials'][i]['Skills'])
            with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Table_Group_Card_{cards}_{i}'):
                Specials_tags = Table_Inputs(table_name=f'Specials_Card_{cards}_{i}', row_name=f'Specials_Table_Row_Card_{cards}_{i}', class_name=Specials,
                             used_in_loop=True, loop_number=i, use_child_window=True, child_parent=f'Specials_Table_Group_Card_{cards}_{i}', child_tag=f'Specials_Child_Window_Card_{cards}_{i}',
                             table_height=90, table_width=1134, child_height=87, child_width=1139, combo=True, combo_tag=Specials.row_names[1], combo_list=Efficacy_Values.combo_list,
                             transformation=True, transformation_card_num=cards)
                
                set_item_height(f'Specials_Card_{cards}_{i}', (24 * (Specials.rows)) + 23)
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
            set_value(f'Special_Set_Aim_Target_Input_Card_{cards}_{i}', json_dict[f'Card {cards + 1}']['Specials'][i]['Target'])
            set_value(f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}', json_dict[f'Card {cards + 1}']['Specials'][i]['Inc Rate'])
            set_value(f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}', json_dict[f'Card {cards + 1}']['Specials'][i]['Lvl Bonus'])
            ### Had to placed down here as it was interrupting the group f'Specials_Group_Card_{cards}_{i}' 
            if json_dict[f'Card {cards + 1}']['Specials'][i]['Skills']:
                for row in range(Specials.rows):
                    z = 0
                    for key, value in json_dict[f'Card {cards + 1}']['Specials'][i]['Skills'][row].items():
                        set_value(Specials.row_names[z] + '_Card_' + str(cards) + '_Row_' + str(i) + str(row), value)
                        z += 1
                    
            add_separator(parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Separator_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Specials_Separator_Card_{cards}_{i}')
            
########################################################################################################################################################################################################        
def Active_Skill_Widgets(json_length, json_dict):
    
    for card in range(json_length):
        if json_dict[f'Card {card + 1}']['Active Skill']:
            # print(card)
            add_text('Active Skill Set', color=(255,50,50), tag=f'Active_Skill_Text_Card_{card}', parent=f'Active_Skill_Card_{card}')
            # with group(horizontal=True, tag=f'Active_Skill_Group'):
            with group(horizontal=True, parent=f'Active_Skill_Card_{card}', tag=f'Active_Skill_Group_1_Card_{card}'):

                with group(horizontal=True, parent=f'Active_Skill_Card_{card}', tag=f'Active_Skill_Group_2_Card_{card}'):
                    add_text('Name:', color=(255, 174, 26), tag=f'Active_Skill_Name_Text_Card_{card}')
                    add_input_text(tag=f'Active_Name_Card_{card}', default_value='', hint='Name', width=String_Length.length[0], callback=Text_Resize)

                with group(horizontal=True, parent=f'Active_Skill_Card_{card}', tag=f'Active_Skill_Group_3_Card_{card}'):
                    add_text('Desc: ', color=(255, 174, 26), tag=f'Active_Skill_Desc_Text_Card_{card}')
                    add_input_text(tag=f'Active_Desc_Card_{card}', default_value='', hint='Description', width=String_Length.length[0], callback=Text_Resize)

                with group(horizontal=True, parent=f'Active_Skill_Card_{card}', tag=f'Active_Skill_Group_4_Card_{card}'):
                    add_text('Cond: ', color=(255, 174, 26), tag=f'Active_Skill_Cond_Text_Card_{card}')
                    add_input_text(tag=f'Active_Cond_Card_{card}', default_value='', hint='Condition', width=String_Length.length[0], callback=Text_Resize)
            add_separator(tag=f'Active_Skill_Separator_Card_{card}', parent=f'Active_Skill_Card_{card}')
            set_value(f'Active_Name_Card_{card}', json_dict[f'Card {card + 1}']['Active Skill']['Name'])
            set_value(f'Active_Desc_Card_{card}', json_dict[f'Card {card + 1}']['Active Skill']['Desc'])
            set_value(f'Active_Cond_Card_{card}', json_dict[f'Card {card + 1}']['Active Skill']['Cond'])
            Text_Resize(f'Active_Name_Card_{card}')
            Text_Resize(f'Active_Desc_Card_{card}')
            Text_Resize(f'Active_Cond_Card_{card}')

            ttt = Table_Inputs(table_name=f'Active_Skill_Set_Card_{card}', row_name=f'Active_Skill_Set_Row_Card_{card}_', class_name=Active_Skill_Set,
                        use_child_window=False, table_parent=f'Active_Skill_Card_{card}', table_height=47, table_width=755, transformation=True, transformation_card_num=card)
            z = 0
            for key, value in json_dict[f'Card {card + 1}']['Active Skill']['Set'].items():
                set_value(Active_Skill_Set.row_names[z] + '_Card_' + str(card) + '_Row_0', value)
                z += 1

            with group(horizontal=True, tag=f'Active_Skills_Group_Card_{card}', parent=f'Active_Skill_Card_{card}'):
                add_text('Active Skills', tag=f'Active_Skills_Text_Card_{card}', color=(255,50,50), parent=f'Active_Skills_Group_Card_{card}')
                add_button(label='Add Skill', tag=f'Active_Skills_Button_Add_Card_{card}', parent=f'Active_Skills_Group_Card_{card}', callback=Active_Skill_Add)
                add_button(label='Del Skill', tag=f'Active_Skills_Button_Del_Card_{card}', parent=f'Active_Skills_Group_Card_{card}', callback=Active_Skill_Del)
            Widget_Aliases.tags_to_delete.append(f'Active_Skills_Group_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skills_Text_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skills_Button_Add_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skills_Button_Del_Card_{card}')

            Active_Skill.rows = len(json_dict[f'Card {card + 1}']['Active Skill']['Skills'])
            sss = Table_Inputs(table_name=f'Active_Skill_Table_Card_{card}', row_name=f'Active_Skill_Row_Card_{card}_', class_name=Active_Skill,
                                use_child_window=False, table_parent=f'Active_Skill_Card_{card}', table_height=80, table_width=1132,
                                combo=True, combo_list=Efficacy_Values.combo_list, combo_tag=Active_Skill.row_names[3], transformation=True, transformation_card_num=card)
            
            if json_dict[f'Card {card + 1}']['Active Skill']['Skills']:
                # z = 0
                # for row in range(Active_Skill.rows):
                #     for key, value in json_dict[f'Card {card + 1}']['Active Skill']['Skills'][row].items():
                #         set_value(Active_Skill.row_names[z] + '_Card_' + str(card) + '_Row_' + str(row), value)
                #         z += 1

                for skill_num, skill in enumerate(json_dict[f'Card {card + 1}']['Active Skill']['Skills']):
                    print(skill_num)
                    print(skill)
                    for index, (key, value) in enumerate(skill.items()):
                        set_value(Active_Skill.row_names[index] + '_Card_' + str(card) + '_Row_' + str(skill_num), value)

                    
            set_item_height(f'Active_Skill_Table_Card_{card}', (24 * Active_Skill.rows + 23))

            Widget_Aliases.tags_to_delete.append(f'Active_Skill_Text_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skill_Name_Text_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skill_Desc_Text_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skill_Cond_Text_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Name_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Desc_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Cond_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skill_Separator_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skill_Group_1_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skill_Group_2_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skill_Group_3_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skill_Group_4_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Skill_Text_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Skill_Name_Text_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Skill_Desc_Text_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Skill_Cond_Text_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Name_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Desc_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Cond_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Skill_Separator_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Skill_Group_1_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Skill_Group_2_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Skill_Group_3_Card_{card}')
            Active_Skill.tags_to_delete.append(f'Active_Skill_Group_4_Card_{card}')

            if json_dict[f'Card {card + 1}']['Ultimate Special']:
                Delete_Items(f'Ultimate_Special_Separator_Card_{card}')
                Delete_Items(f'Ultimate_Special_Text_Card_{card}')
                Delete_Items(f'Ultimate_Special_Group_Card_{card}')
                for u in range(len(Active_Skill.ultimate_names)):
                    Delete_Items(Active_Skill.ultimate_hints[u] + '_Card_' + str(card) + '_Text')
                    Delete_Items(Active_Skill.ultimate_names[u] + '_Card_' + str(card))

                add_separator(tag=f'Ultimate_Special_Separator_Card_{card}', parent=f'Active_Skill_Card_{card}')
                add_text('Ultimate Special', color=(255,50,50), parent=f'Active_Skill_Card_{card}', tag=f'Ultimate_Special_Text_Card_{card}')
                Widget_Aliases.tags_to_delete.append(f'Ultimate_Special_Separator_Card_{card}')
                Widget_Aliases.tags_to_delete.append(f'Ultimate_Special_Text_Card_{card}')

                with group(horizontal=True, parent=f'Active_Skill_Card_{card}', tag=f'Ultimate_Special_Group_Card_{card}'):
                    for z in range(len(Active_Skill.ultimate_names)):
                        add_text(Active_Skill.ultimate_hints[z] + ':', color=(255, 174, 26), parent=f'Ultimate_Special_Group_Card_{card}', tag=Active_Skill.ultimate_hints[z] + '_Card_' + str(card) + '_Text')
                        add_input_text(tag=Active_Skill.ultimate_names[z] + '_Card_' + str(card), default_value=json_dict[f'Card {card + 1}']['Ultimate Special'][Active_Skill.ultimate_hints[z]], hint=Active_Skill.ultimate_hints[z], width=String_Length.length[0], callback=Text_Resize, parent=f'Ultimate_Special_Group_Card_{card}')
                        Widget_Aliases.tags_to_delete.append(Active_Skill.ultimate_hints[z] + '_Card_' + str(card) + '_Text')
                        Widget_Aliases.tags_to_delete.append(Active_Skill.ultimate_names[z] + '_Card_' + str(card))
            configure_item(f'Active_Skill_Card_{card}', show=True)
            set_value(f'Custom_Unit_Active_Skill_Checkbox_{card}', True)

########################################################################################################################################################################################################      
def Standby_Skill_Widgets(json_length, json_dict):
    for card in range(json_length):
        if json_dict[f'Card {card + 1}']['Standby Skill']:
            standby_skill = 0
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
                
            set_value(f'Standby_Set_Name_Input_Text_{card}_{standby_skill}', json_dict[f'Card {card + 1}']['Standby Skill']['Name'])
            set_value(f'Standby_Set_Desc_Input_Text_{card}_{standby_skill}', json_dict[f'Card {card + 1}']['Standby Skill']['Desc'])
            set_value(f'Standby_Set_Cond_Input_Text_{card}_{standby_skill}', json_dict[f'Card {card + 1}']['Standby Skill']['Cond'])
            Text_Resize(f'Standby_Set_Name_Input_Text_{card}_{standby_skill}')
            Text_Resize(f'Standby_Set_Desc_Input_Text_{card}_{standby_skill}')
            Text_Resize(f'Standby_Set_Cond_Input_Text_{card}_{standby_skill}')

            add_separator(tag=f'Standby_Skill_Set_Separator_{card}_{standby_skill}', parent=f'Standby_Skill_{card}')
            add_text('Standby Skill', color=(255,50,50), parent=f'Standby_Skill_{card}', tag=f'Standby_Skill_Text_{card}_{standby_skill}')
                
            ttt = Table_Inputs(table_name=f'Standby_Skill_Set_Table_{card}_{standby_skill}', row_name=f'Standby_Skill_Set_Table_Row_{card}_{standby_skill}', table_parent=f'Standby_Skill_{card}', use_child_window=False, 
                        class_name=Standby_Skill_Set, table_width=500, table_height=49, row_width=85, freeze_rows=1, table_policy=mvTable_SizingStretchSame, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=card)
            z = 0
            for key, value in json_dict[f'Card {card + 1}']['Standby Skill']['Set'].items():
                set_value(Standby_Skill_Set.row_names[z] + '_Card_' + str(card) + '_Row_00', value)
                z += 1
            
            Standby_Skill.rows = len(json_dict[f'Card {card + 1}']['Standby Skill']['Skills'])
            Table_Inputs(table_name=f'Standby_Skill_Table_{card}_{standby_skill}', row_name=f'Standby_Skill_Table_Row_{card}_{standby_skill}', table_parent=f'Standby_Skill_{card}', use_child_window=False, 
                        class_name=Standby_Skill, table_width=825, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=card)

            for row in range(Standby_Skill.rows):
                z = 0
                for key, value in json_dict[f'Card {card + 1}']['Standby Skill']['Skills'][row].items():
                    set_value(Standby_Skill.row_names[z] + '_Card_' + str(card) + '_Row_0' + str(row), value)
                    z += 1

            set_item_height(f'Standby_Skill_Table_{card}_{standby_skill}', (24 * Standby_Skill.rows) + 23)
            configure_item(f'Standby_Skill_{card}', show=True)
            set_value(f'Custom_Unit_Standby_Skill_Checkbox_{card}', True)

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
            
########################################################################################################################################################################################################   
def Finish_Skill_Set_Widgets(json_length, json_dict):
    for card in range(json_length):
        if json_dict[f'Card {card + 1}']['Finish Skill']:
            for finish_skill in range(len(json_dict[f'Card {card + 1}']['Finish Skill'])):
                Delete_Items(f'Finish_Skill_Set_Text_{card}_{finish_skill}')
                add_text('Finish Skill Set', color=(255,50,50), parent=f'Finish_Skill_{card}', tag=f'Finish_Skill_Set_Text_{card}_{finish_skill}')


                Delete_Items(f'Finish_Skill_Set_Group_{card}_{finish_skill}')
                with group(horizontal=True, parent=f'Finish_Skill_{card}', tag=f'Finish_Skill_Set_Group_{card}_{finish_skill}'):
                
                    Delete_Items(f'Finish_Skill_Set_Name_{card}_{finish_skill}')
                    Delete_Items(f'Finish_Set_Name_{card}_{finish_skill}')

                    add_text('Name:', color=(255, 174, 26), tag=f'Finish_Skill_Set_Name_{card}_{finish_skill}', parent=f'Finish_Skill_Set_Group_{card}_{finish_skill}')
                    add_input_text(default_value='', hint='Name', tag=f'Finish_Set_Name_{card}_{finish_skill}', parent=f'Finish_Skill_Set_Group_{card}_{finish_skill}')

                Delete_Items(f'Finish_Skill_Desc_Group_{card}_{finish_skill}')
                with group(horizontal=True, parent=f'Finish_Skill_{card}', tag=f'Finish_Skill_Desc_Group_{card}_{finish_skill}'):       
                
                    Delete_Items(f'Finish_Skill_Set_Desc_{card}_{finish_skill}')
                    Delete_Items(f'Finish_Set_Desc_{card}_{finish_skill}')

                    add_text('Desc: ', color=(255, 174, 26), tag=f'Finish_Skill_Set_Desc_{card}_{finish_skill}', parent=f'Finish_Skill_Desc_Group_{card}_{finish_skill}')        
                    add_input_text(tag=f'Finish_Set_Desc_{card}_{finish_skill}', hint='Description', default_value='', width=String_Length.length[0], callback=Text_Resize, parent=f'Finish_Skill_Desc_Group_{card}_{finish_skill}')

                Delete_Items(f'Finish_Skill_Cond_Group_{card}_{finish_skill}')
                with group(horizontal=True, parent=f'Finish_Skill_{card}', tag=f'Finish_Skill_Cond_Group_{card}_{finish_skill}'):
                    Delete_Items(f'Finish_Skill_Set_Cond_{card}_{finish_skill}')
                    Delete_Items(f'Finish_Set_Cond_{card}_{finish_skill}')
                    add_text('Cond: ', color=(255, 174, 26), tag=f'Finish_Skill_Set_Cond_{card}_{finish_skill}', parent=f'Finish_Skill_Cond_Group_{card}_{finish_skill}')
                    add_input_text(tag=f'Finish_Set_Cond_{card}_{finish_skill}', hint='Condition', default_value='', width=String_Length.length[0], callback=Text_Resize, parent=f'Finish_Skill_Cond_Group_{card}_{finish_skill}')
                
                set_value(f'Finish_Set_Name_{card}_{finish_skill}', json_dict[f'Card {card + 1}']['Finish Skill'][finish_skill]['Name'])
                set_value(f'Finish_Set_Desc_{card}_{finish_skill}', json_dict[f'Card {card + 1}']['Finish Skill'][finish_skill]['Desc'])
                set_value(f'Finish_Set_Cond_{card}_{finish_skill}', json_dict[f'Card {card + 1}']['Finish Skill'][finish_skill]['Cond'])
                Text_Resize(f'Finish_Set_Name_{card}_{finish_skill}')
                Text_Resize(f'Finish_Set_Desc_{card}_{finish_skill}')
                Text_Resize(f'Finish_Set_Cond_{card}_{finish_skill}')
                    
                ttt = Table_Inputs(table_name=f'Finish_Skill_Set_Table_{card}_{finish_skill}', row_name=f'Finish_Skill_Set_Table_Row_{card}_{finish_skill}', table_parent=f'Finish_Skill_{card}', use_child_window=False, 
                            class_name=Finish_Skill_Set, table_width=927, table_height=47, row_width=80, freeze_rows=1, loop_number=finish_skill, used_in_loop=True, table_policy=mvTable_SizingFixedFit,
                            transformation=True, transformation_card_num=card)
                z = 0
                for key, value in json_dict[f'Card {card + 1}']['Finish Skill'][finish_skill]['Set'].items():
                    set_value(Finish_Skill_Set.row_names[z] + '_Card_' + str(card) + '_Row_' + str(finish_skill) + '0', value)
                    z += 1

                # print(ttt)

                add_text('Finish Skill', tag=f'Finish_Skill_Skill_Text_{card}_{finish_skill}', color=(255,50,50), parent=f'Finish_Skill_{card}')
                Widget_Aliases.tags_to_delete.append(f'Finish_Skill_Skill_Text_{card}_{finish_skill}')
                
                ### Same logic from Finish Skill Set Table applies to these aliases.
                Finish_Skill.rows = len(json_dict[f'Card {card + 1}']['Finish Skill'][finish_skill]['Skills'])
                sss = Table_Inputs(table_name=f'Finish_Skill_Table_{card}_{finish_skill}', row_name=f'Finish_Skill_Table_Row_{card}_{finish_skill}', table_parent=f'Finish_Skill_{card}', use_child_window=False, 
                            class_name=Finish_Skill, table_width=836, row_width=82, table_height=114, freeze_rows=1, loop_number=finish_skill, used_in_loop=True, transformation=True, transformation_card_num=card)
                for row in range(Finish_Skill.rows):
                    z = 0
                    for key, value in json_dict[f'Card {card + 1}']['Finish Skill'][finish_skill]['Skills'][row].items():
                        set_value(Finish_Skill.row_names[z] + '_Card_' + str(card) + '_Row_' + str(finish_skill) + str(row), value)
                        z += 1
                
                set_item_height(f'Finish_Skill_Table_{card}_{finish_skill}', (24 * Finish_Skill.rows) + 23)
                configure_item(f'Finish_Skill_{card}', show=True)
                set_value(f'Custom_Unit_Finish_Skill_Checkbox_{card}', True)

########################################################################################################################################################################################################
def Dokkan_Field_Widgets(json_length, json_dict):
    ### In case a unit comes out with more than 1 dokkan field
    # for card in range(len(Card_Checks.card_ids)):
        # for field in range(len(Card_Checks.dokkan_field_cards)):
    for card in range(json_length):
        if json_dict[f'Card {card + 1}']['Dokkan Field']:
            for field in range(len(json_dict[f'Card {card + 1}']['Dokkan Field'])):
                add_text('Dokkan Field', tag=f'Dokkan_Field_Text_{card}_{field}', parent=f'Dokkan_Field_{card}', color=(255,50,50))
                with group(tag=f'Dokkan_Field_Name_Text_Group_{card}_{field}', horizontal=True, parent=f'Dokkan_Field_{card}'):
                    add_text('Name:', tag=f'Dokkan_Field_Name_Text_{card}_{field}', parent=f'Dokkan_Field_Name_Text_Group_{card}_{field}', color=(255, 174, 26))
                    add_input_text(tag=f'Dokkan_Field_Name_Input_Text_{card}_{field}', hint='Name', width=String_Length.length[0], callback=Text_Resize, parent=f'Dokkan_Field_Name_Text_Group_{card}_{field}')

                with group(tag=f'Dokkan_Field_Desc_Text_Group_{card}_{field}', horizontal=True, parent=f'Dokkan_Field_{card}'):
                    add_text('Desc: ', tag=f'Dokkan_Field_Desc_Text_{card}_{field}', parent=f'Dokkan_Field_Desc_Text_Group_{card}_{field}', color=(255, 174, 26))
                    add_input_text(tag=f'Dokkan_Field_Desc_Input_Text_{card}_{field}', hint='Desc', width=String_Length.length[0], callback=Text_Resize, parent=f'Dokkan_Field_Desc_Text_Group_{card}_{field}', multiline=True)

                with group(tag=f'Dokkan_Field_Resource_Text_Group_{card}_{field}', horizontal=True, parent=f'Dokkan_Field_{card}'):
                    add_text('Resource ID: ', tag=f'Dokkan_Field_Resource_Text_{card}_{field}', parent=f'Dokkan_Field_Resource_Text_Group_{card}_{field}', color=(255, 174, 26))
                    add_input_text(tag=f'Dokkan_Field_Resource_ID_{card}_{field}', hint='Resource ID', width=String_Length.length[0], callback=Text_Resize, parent=f'Dokkan_Field_Resource_Text_Group_{card}_{field}')

                add_separator(tag=f'Dokkan_Field_Separtor_1_{card}_{field}', parent=f'Dokkan_Field_{card}')
                with group(tag=f'Dokkan_Field_Checkbox_Group_{card}_{field}', horizontal=True, parent=f'Dokkan_Field_{card}'):
                    add_checkbox(label='Link to Active', tag=f'Link_to_Active_Button_{card}_{field}', parent=f'Dokkan_Field_Checkbox_Group_{card}_{field}')
                    add_checkbox(label='Link to Passive', tag=f'Link_to_Passive_Button_{card}_{field}', parent=f'Dokkan_Field_Checkbox_Group_{card}_{field}')
                
                set_value(f'Dokkan_Field_Name_Input_Text_{card}_{field}', json_dict[f'Card {card + 1}']['Dokkan Field'][field]['Name'])
                set_value(f'Dokkan_Field_Desc_Input_Text_{card}_{field}', json_dict[f'Card {card + 1}']['Dokkan Field'][field]['Desc'])
                set_value(f'Dokkan_Field_Resource_ID_{card}_{field}', json_dict[f'Card {card + 1}']['Dokkan Field'][field]['Resource ID'])
                set_value(f'Link_to_Active_Button_{card}_{field}', json_dict[f'Card {card + 1}']['Dokkan Field'][field]['Link to Active'])
                set_value(f'Link_to_Passive_Button_{card}_{field}', json_dict[f'Card {card + 1}']['Dokkan Field'][field]['Link to Passive'])
                Text_Resize(f'Dokkan_Field_Name_Input_Text_{card}_{field}')
                Text_Resize(f'Dokkan_Field_Desc_Input_Text_{card}_{field}')
                Text_Resize(f'Dokkan_Field_Resource_ID_{card}_{field}')
                Resize_Description(f'Dokkan_Field_Desc_Input_Text_{card}_{field}', json_dict[f'Card {card + 1}']['Dokkan Field'][field]['Desc'])

                add_separator(tag=f'Dokkan_Field_Separtor_2_{card}_{field}', parent=f'Dokkan_Field_{card}')
                
                Dokkan_Field.rows = len(json_dict[f'Card {card + 1}']['Dokkan Field'][field]['Skills'])
                t = Table_Inputs(table_name=f'Dokkan_Field_Table_{card}_{field}', row_name=f'Dokkan_Field_Table_Row_{card}_{field}', table_parent=f'Dokkan_Field_{card}', use_child_window=False, 
                            class_name=Dokkan_Field, table_width=1100, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=field, table_policy=mvTable_SizingFixedFit)
                
                for row in range(Dokkan_Field.rows):
                    z = 0
                    for key, value in json_dict[f'Card {card + 1}']['Dokkan Field'][field]['Skills'][row].items():
                        if Dokkan_Field.row_names[z] == Dokkan_Field.row_names[10]:
                            set_value(Dokkan_Field.row_names[z] + '_Card_' + str(card) + '_Row_' + str(field) + str(row), value)
                            Text_Resize(Dokkan_Field.row_names[z] + '_Card_' + str(card) + '_Row_' + str(field) + str(row))
                        else:
                            set_value(Dokkan_Field.row_names[z] + '_Card_' + str(card) + '_Row_' + str(field) + str(row), value)
                        z += 1
                
                set_item_height(f'Dokkan_Field_Table_{card}_{field}', (24 * (Dokkan_Field.rows)) + 23)
                configure_item(f'Dokkan_Field_{card}', show=True)

                widget_widths_list = []
                for row in range(Dokkan_Field.rows):
                    widget_widths = 0
                    for column in range(len(Dokkan_Field.row_names)):
                        widget_widths += get_item_width(Dokkan_Field.row_names[column] + '_Card_' + str(card) + '_Row_0' + str(row))
                    widget_widths_list.append(widget_widths)
    
        
                # Finding the max width out of all widgets
                max_width = 0
                for width in widget_widths_list:
                    max_width = width
                    if width > max_width:
                        max_width = width
                # print(max_width)
                set_item_width(f'Dokkan_Field_Table_{card}_{field}', max_width + 100)
                
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Text_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Name_Input_Text_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Desc_Input_Text_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Resource_ID_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Name_Text_Group_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Desc_Text_Group_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Resource_Text_Group_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Name_Text_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Desc_Text_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Resource_Text_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Checkbox_Group_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Link_to_Active_Button_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Link_to_Passive_Button_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Separtor_2_{card}_{field}')
                Widget_Aliases.tags_to_delete.append(f'Dokkan_Field_Separtor_1_{card}_{field}')
                set_value(f'Custom_Unit_Dokkan_Field_Checkbox_{card}', True)
                
########################################################################################################################################################################################################
def Battle_Params_Widgets(json_length, json_dict):
    for card in range(json_length):
        # print(battle_params_dictionary[card])
        if json_dict[f'Card {card + 1}']['Transformation']:
            add_text('Transformation Information', tag=f'Transformation_Information_Text_{card}', color=(255,50,50), parent=f'Battle_Params_{card}')
            
            
            Transformation_Descriptions.rows = len(json_dict[f'Card {card + 1}']['Transformation'])
            skill_type_combo_list = ['Active Skill', 'Passive Skill', 'Standby Skill', 'Finish Skill']
            tt = Table_Combo_Inputs(table_name=f'Transformation_Descriptions_Table_{card}', row_name=f'Transformation_Descriptions_Table_Row_{card}', table_parent=f'Battle_Params_{card}', 
                               class_name=Transformation_Descriptions, table_width=600, row_width=82, table_height=45, freeze_rows=1, table_policy=mvTable_SizingFixedFit,
                               combo_columns=[0], combo=True, combo_list=[skill_type_combo_list], transformation_card_num=card)
            # print(tt)
            for transformation in range(Transformation_Descriptions.rows):
                set_value(Transformation_Descriptions.row_names[0] + '_Card_' + str(card) + '_Row_0', json_dict[f'Card {card + 1}']['Transformation'][transformation]['Skill Type'])
                set_value(Transformation_Descriptions.row_names[1] + '_Card_' + str(card) + '_Row_0', json_dict[f'Card {card + 1}']['Transformation'][transformation]['Desc'])
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
        if json_dict[f'Card {card + 1}']['Battle Params']:
            ### key = param_no 
            param_num = 0
            for key, value in json_dict[f'Card {card + 1}']['Battle Params'].items():
                param_no_dict = value

                Battle_Params.rows = len(param_no_dict)
                ttt = Table_Combo_Inputs(table_name=f'Battle_Params_Table_{card}_{param_num}', row_name=f'Battle_Params_Table_Row_{card}_{param_num}', table_parent=f'Battle_Params_{card}', 
                             class_name=Battle_Params, table_width=270, row_width=82, freeze_rows=1, transformation_card_num=card, loop_number=param_num, used_in_loop=True, table_policy=mvTable_SizingFixedFit)
                Resize_Table(f'Battle_Params_Table_{card}_{param_num}', Battle_Params.rows)
                # print(ttt)
                ### This is a dictionary
                for dictionary in range(len(param_no_dict)):
                    # print(Battle_Params.row_names[0] + '_Card_' + str(card) + '_Row_' + str(param) + str(key))
                    set_value(Battle_Params.row_names[0] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(dictionary), key)
                    set_value(Battle_Params.row_names[1] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(dictionary), json_dict[f'Card {card + 1}']['Battle Params'][key][dictionary]['idx'])
                    #  Length of Card ID
                    if len(str(value)) == 7:
                        set_value(Battle_Params.row_names[2] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(dictionary), str(json_dict[f'Card {card + 1}']['Battle Params'][key][dictionary]['value']).replace(str(json_dict[f'Card {card + 1}']['Battle Params'][key][dictionary]['value'])[1], '3'))
                    else:
                        set_value(Battle_Params.row_names[2] + '_Card_' + str(card) + '_Row_' + str(param_num) + str(dictionary), json_dict[f'Card {card + 1}']['Battle Params'][key][dictionary]['value'])
                    configure_item(f'Battle_Params_{card}', show=True)
                param_num += 1
                
            set_value(f'Custom_Unit_Battle_Params_Checkbox_{card}', True)

########################################################################################################################################################################################################
def Leader_Skill_Widgets(json_length, json_dict):
    def Leader_Preset_Resize(tag_id):
        text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIAL.ttf')
        set_item_width(tag_id, text_width + 27)
    
    leader_options = ['Element Type', 'Extreme Class', 'Super Class', 'All Types', '1 Category', '1 Category & 1 Element', '2 Categories', '2 Categories & 1 Extra', '2 Categories & 2 Extra', '3 Categories & 2 Extra', '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)']
    leader_categories = Leader_Skill_Info.cat_list
        
    for card in range(json_length):
        if json_dict[f'Card {card + 1}']['Leader Skill']:
            with group(horizontal=True, tag=f'Leader_Skill_Widgets_Group_{card}_1', parent=f'Leader_Skill_{card}'):
                add_text('Leader Skill', tag=f'Leader_Skill_Text_{card}', color=(255,50,50), parent=f'Leader_Skill_Widgets_Group_{card}_1')


                add_combo(leader_options, default_value=json_dict[f'Card {card + 1}']['Leader Skill']['Preset'], tag=f'Leader_Skill_Preset_List_{card}', width=String_Length.length[9], callback=Leader_Combo, parent=f'Leader_Skill_Widgets_Group_{card}_1')
                Leader_Preset_Resize(f'Leader_Skill_Preset_List_{card}')
                for combo in range(len(json_dict[f'Card {card + 1}']['Leader Skill']['Categories'])):
                    add_combo(leader_categories, default_value='Categories', tag=f'Leader_Skill_Category_Selection_{card}_{combo}', width=String_Length.length[11], callback=Leader_Cat_Selection, parent=f'Leader_Skill_Widgets_Group_{card}_1')
                    set_value(f'Leader_Skill_Category_Selection_{card}_{combo}', json_dict[f'Card {card + 1}']['Leader Skill']['Categories'][combo])
                    Leader_Preset_Resize(f'Leader_Skill_Category_Selection_{card}_{combo}')


            with group(horizontal=True, parent=f'Leader_Skill_{card}', tag=f'Leader_Skill_Widgets_Group__{card}_2'):
                add_input_text(default_value='', hint='XXX%', width=String_Length.length[0], callback=Leader_Efficacy_Value_Changer, tag=f'Leader_Efficacy_Value_Changer_{card}', parent=f'Leader_Skill_Widgets_Group_{card}_2')

                add_text('%', tag=f'Leader_Efficacy_Value_Changer_Text_{card}', parent=f'Leader_Skill_Widgets_Group_{card}_2')

                with tooltip(f'Leader_Efficacy_Value_Changer_{card}', tag=f'Leader_Efficacy_Value_Changer_Tooltip_{card}'):
                    add_text('Type what percent you want the leader skill to use')

            add_input_text(default_value='', tag=f'Leader_Name_Text_Input_{card}',hint='Name', width=String_Length.length[0], callback=Leader_Resize, parent=f'Leader_Skill_{card}')
            add_input_text(default_value='', tag=f'Leader_Desc_Text_Input_{card}',hint='Description', width=String_Length.length[0], callback=Resize_Widget, parent=f'Leader_Skill_{card}', multiline=True)
            set_value(f'Leader_Name_Text_Input_{card}', json_dict[f'Card {card + 1}']['Leader Skill']['Name'])
            set_value(f'Leader_Desc_Text_Input_{card}', json_dict[f'Card {card + 1}']['Leader Skill']['Desc'])
            Text_Resize(f'Leader_Desc_Text_Input_{card}')
            Resize_Description(f'Leader_Desc_Text_Input_{card}', json_dict[f'Card {card + 1}']['Leader Skill']['Desc'])
            Leader_Resize(f'Leader_Name_Text_Input_{card}')

            Leader_Skill_Info.rows = len(json_dict[f'Card {card + 1}']['Leader Skill']['Skills'])
            Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                            use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=66, table_width=867)
            set_item_height(f'Leader_Skill_Table_{card}', (24 * (Leader_Skill_Info.rows)) + 23)
            
            for row in range(Leader_Skill_Info.rows):
                z = 0
                for key, value in json_dict[f'Card {card + 1}']['Leader Skill']['Skills'][row].items():
                    set_value(Leader_Skill_Info.row_names[z] + '_Card_' + str(card) + '_Row_' + str(row), value)
                    z += 1
            configure_item(f'Leader_Skill_{card}', show=True)
            set_value(f'Custom_Unit_Leader_Skill_Checkbox_{card}', True)
                    
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Widgets_Group_{card}_1')    
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Widgets_Group_{card}_2')    
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Text_{card}')        
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Preset_List_{card}')        
    Widget_Aliases.tags_to_delete.append(f'Leader_Name_Text_Input_{card}')        
    Widget_Aliases.tags_to_delete.append(f'Leader_Desc_Text_Input_{card}')   
    Widget_Aliases.tags_to_delete.append(f'Leader_Efficacy_Value_Changer_{card}')   
    Widget_Aliases.tags_to_delete.append(f'Leader_Efficacy_Value_Changer_Text_{card}')   
    Widget_Aliases.tags_to_delete.append(f'Leader_Efficacy_Value_Changer_Tooltip_{card}')
    

def Custom_Unit_Categories_Load(json_length, json_dict):
    for card in range(json_length):
        if json_dict[f'Card {str(card + 1)}']['Categories']:
            Categories_Activated.card_categories_dict[card] = json_dict[f'Card {str(card + 1)}']['Categories']
            for category in json_dict[f'Card {str(card + 1)}']['Categories']:
                if does_alias_exist(f'Category_Card_{card}_{category}_left'):
                        configure_item(f'Category_Card_{card}_{category}_left', texture_tag=f'Category_{category}_on')
                        set_value(f'Image_State_Check_{category}', 1)
                elif does_alias_exist(f'Category_Card_{card}_{category}_right'):
                        configure_item(f'Category_Card_{card}_{category}_right', texture_tag=f'Category_{category}_on')
                        set_value(f'Image_State_Check_{category}', 1)
                

def Json_Load_Effect_Packs(card, json_dict):
    
    if json_dict[f'Card {card + 1}']['Effect Packs']:
        Effect_Pack.rows = len(json_dict[f'Card {card + 1}']['Effect Packs'])
        Effect_Packs_Widgets(card)
        for row in range(len(json_dict[f'Card {card + 1}']['Effect Packs'])):
            i = 0
            for key, value in json_dict[f'Card {card + 1}']['Effect Packs'][row].items():
                set_value(Effect_Pack.row_names[i] + '_Card_' + str(card) + '_Row_' + str(row), value)
                i += 1
    
            
def Json_Load_Special_Views(card, json_dict):
    
    if json_dict[f'Card {card + 1}']['Special Views']:
        Special_Views.rows = len(json_dict[f'Card {card + 1}']['Special Views'])
        Special_View_Widgets(card)
        for row in range(len(json_dict[f'Card {card + 1}']['Special Views'])):
            i = 0
            for key, value in json_dict[f'Card {card + 1}']['Special Views'][row].items():
                set_value(Special_Views.row_names[i] + '_Card_' + str(card) + '_Row_' + str(row), value)
                i += 1
                
