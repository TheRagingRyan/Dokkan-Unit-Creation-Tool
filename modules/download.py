import requests
from .classes import Card_Checks, Widget_Aliases, Custom_Unit
import io
import json
from PIL import Image, UnidentifiedImageError
import os
from dearpygui.dearpygui import *
from . specials import Unit_Checks
from . functions import Delete_Items, load_JSON, read_json_from_zip
from . battle_params import Battle_Param_Sorted_Dictionary
from . leader import Define_Leader_Skill_Type
import ast

#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################
def Transformation_Unit_Card_Information():
    
    json_data = Card_Checks.json_data
    num_of_cards = len(json_data)
    
    # Use 1st card because all other cards would be eza'd as well.
    eza = True if 'optimal_awakening_growth' in json_data[0] else False
    
    # Card Section
    Card_Checks.card_ids = [json_data[i]['card']['id'] for i in range(num_of_cards)]
    Card_Checks.card_names = [json_data[i]['card']['name'].replace('\n', '') for i in range(num_of_cards)]
    Card_Checks.element_id = {i : json_data[i]['card']['element'] for i in range(num_of_cards)}
    
    # Passive Section
    Card_Checks.passive_ids = [[json_data[i]['card']['passive_skill_set_id'] if not eza else json_data[i]['optimal_awakening_growth']['passive_skill_id']] for i in range(num_of_cards)]
    Card_Checks.passive_names = [[json_data[i]['card']['passive_skill_name'] if not eza else json_data[i]['optimal_awakening_growth']['passive_skill_name']] for i in range(num_of_cards)]
    Card_Checks.passive_descriptions = [[json_data[i]['card']['passive_skill_desc'] if not eza else json_data[i]['optimal_awakening_growth']['passive_skill_description']] for i in range(num_of_cards)]
    
    # Specials Section
    if eza:
        Card_Checks.special_set_ids = [[json_data[c]['specials'][i + int((len(json_data[c]['specials']) / 2))]['id'] for i in range(int(len(json_data[c]['specials']) / 2))] for c in range(num_of_cards)]
        Card_Checks.special_set_names = [[json_data[c]['specials'][i + int((len(json_data[c]['specials']) / 2))]['name'] for i in range(int(len(json_data[c]['specials']) / 2))] for c in range(num_of_cards)]
        Card_Checks.special_set_descriptions = [[json_data[c]['specials'][i + int((len(json_data[c]['specials']) / 2))]['description'] for i in range(int(len(json_data[c]['specials']) / 2))] for c in range(num_of_cards)]
        Card_Checks.special_set_conditions = [[json_data[c]['specials'][i + int((len(json_data[c]['specials']) / 2))]['causality_description'] if 'causality_description' in json_data[c]['specials'][i + int((len(json_data[c]['specials']) / 2))] else 'NULL' for i in range(int(len(json_data[c]['specials']) / 2))] for c in range(num_of_cards)]
    
        Card_Checks.leader_skill_id = json_data[0]['optimal_awakening_growth']['leader_skill_id']
        Card_Checks.leader_skill_name = json_data[0]['optimal_awakening_growth']['leader_skill_name']
        Card_Checks.leader_skill_description = json_data[0]['optimal_awakening_growth']['leader_skill_description']
        
    else:
        Card_Checks.special_set_ids = [[json_data[c]['specials'][i]['id'] for i in range(len(json_data[c]['specials']))] for c in range(num_of_cards)]
        Card_Checks.special_set_names = [[json_data[c]['specials'][i]['name'] for i in range(len(json_data[c]['specials']))] for c in range(num_of_cards)]
        Card_Checks.special_set_descriptions = [[json_data[c]['specials'][i]['description'] for i in range(len(json_data[c]['specials']))] for c in range(num_of_cards)]
        Card_Checks.special_set_conditions = [[json_data[c]['specials'][i]['causality_description'] if 'causality_description' in json_data[c]['specials'][i] else 'NULL' for i in range(len(json_data[c]['specials']))] for c in range(num_of_cards)]
        
        Card_Checks.leader_skill_id = json_data[0]['card']['leader_skill_set_id']
        Card_Checks.leader_skill_name = json_data[0]['card']['title']
        Card_Checks.leader_skill_description = json_data[0]['card']['leader_skill']
    
    # Active Skill
    Card_Checks.active_skill_ids = {c : json_data[c]['card']['active_skill_id'] if 'active_skill_id' in json_data[c]['card'] else None for c in range(num_of_cards)}
    Card_Checks.active_skill_name = {c : json_data[c]['card']['active_skill_name'] if 'active_skill_name' in json_data[c]['card'] else 'NULL' for c in range(num_of_cards)}
    Card_Checks.active_skill_desc = {c : json_data[c]['card']['active_skill_effect'] if 'active_skill_effect' in json_data[c]['card'] else 'NULL' for c in range(num_of_cards)}
    Card_Checks.active_skill_cond = {c : json_data[c]['card']['active_skill_condition'] if 'active_skill_condition' in json_data[c]['card'] else 'NULL' for c in range(num_of_cards)}
    Card_Checks.ultimate_special_ids = {c : json_data[c]['card']['ultimate_special_id'] if 'ultimate_special_id' in json_data[c]['card'] else None for c in range(num_of_cards)}
    
    # Standby Skill
    Card_Checks.standby_skill_cards = {c : True if json_data[c]['standby_skills'] else False for c in range(num_of_cards)}
    Card_Checks.standby_skill_ids = [[json_data[c]['standby_skills'][i]['id'] if json_data[c]['standby_skills'] else None for i in range(len(json_data[c]['standby_skills']))] for c in range(num_of_cards)]
    Card_Checks.standby_skill_names = [[json_data[c]['standby_skills'][i]['name'] if json_data[c]['standby_skills'] else 'NULL' for i in range(len(json_data[c]['standby_skills']))] for c in range(num_of_cards)]
    Card_Checks.standby_skill_desc = [[json_data[c]['standby_skills'][i]['effect_description'] if json_data[c]['standby_skills'] else 'NULL' for i in range(len(json_data[c]['standby_skills']))] for c in range(num_of_cards)]
    Card_Checks.standby_skill_cond = [[json_data[c]['standby_skills'][i]['condition_description'] if json_data[c]['standby_skills'] else 'NULL' for i in range(len(json_data[c]['standby_skills']))] for c in range(num_of_cards)]
    
    # Finish Skill
    Card_Checks.finish_skill_cards = {c : True if json_data[c]['finish_skills'] else False for c in range(num_of_cards)}
    Card_Checks.finish_skill_ids = [[json_data[c]['finish_skills'][i]['id'] if json_data[c]['finish_skills'] else None for i in range(len(json_data[c]['finish_skills']))] for c in range(num_of_cards)]
    Card_Checks.finish_skill_names = [[json_data[c]['finish_skills'][i]['name'] if json_data[c]['finish_skills'] else 'NULL' for i in range(len(json_data[c]['finish_skills']))] for c in range(num_of_cards)]
    Card_Checks.finish_skill_desc = [[json_data[c]['finish_skills'][i]['effect_description'] if json_data[c]['finish_skills'] else 'NULL' for i in range(len(json_data[c]['finish_skills']))] for c in range(num_of_cards)]
    Card_Checks.finish_skill_cond = [[json_data[c]['finish_skills'][i]['condition_description'] if json_data[c]['finish_skills'] else 'NULL' for i in range(len(json_data[c]['finish_skills']))] for c in range(num_of_cards)]
    
    # Dokkan Field
    num_of_fields = {c : len(json_data[c]['dokkan_fields']) if 'dokkan_fields' in json_data[c] else 0 for c in range(num_of_cards)}
    Card_Checks.dokkan_field_cards = {c : True if 'dokkan_fields' in json_data[c] else False for c in range(num_of_cards)}
    Card_Checks.dokkan_field_ids = [[json_data[c]['dokkan_fields'][i]['id'] if Card_Checks.dokkan_field_cards else None for i in range(num_of_fields[c])] for c in range(num_of_cards)]
    Card_Checks.dokkan_field_names = [[json_data[c]['dokkan_fields'][i]['name'] if Card_Checks.dokkan_field_cards else 'NULL' for i in range(num_of_fields[c])] for c in range(num_of_cards)]
    Card_Checks.dokkan_field_desc = [[json_data[c]['dokkan_fields'][i]['description'] if Card_Checks.dokkan_field_cards else 'NULL' for i in range(num_of_fields[c])] for c in range(num_of_cards)]
    Card_Checks.dokkan_field_resource_ids = [[json_data[c]['dokkan_fields'][i]['resource_id'] if Card_Checks.dokkan_field_cards else 'NULL' for i in range(num_of_fields[c])] for c in range(num_of_cards)]
    
    # Battle Params
    Card_Checks.battle_params = {c : json_data[0]['transformations'][c + 1]['next_card']['battle_params'] if len(json_data[c]['transformations']) > 1 else None for c in range(len(json_data[0]['transformations']) - 1)}
    Card_Checks.transformation_descriptions = {c : json_data[0]['transformations'][c + 1]['next_card']['description'] if len(json_data[c]['transformations']) > 1 else None for c in range(len(json_data[0]['transformations']) - 1)}
    Card_Checks.battle_params = Battle_Param_Sorted_Dictionary()
    
    Define_Leader_Skill_Type(Card_Checks.leader_skill_description)
    
    
#################################################################################################################################################################################################################################################################
# Grabs all card information from card JSONs generated from the database dump.
def Card_Information(card_id_1):
    # To ensure a clean start every time this function is called
    Card_Checks.json_data.clear()

    # data = load_JSON(f'jsons/{card_id_1}.json')
    data = read_json_from_zip(card_id_1)
    # print(data) # Debugging json data output

    cardID0 = str(card_id_1[:-1]) + '0'

    # Main Card for everything
    Card_Checks.json_data[0] = data
    Card_Checks.card_ids = [data['card']['id']]
    Card_Checks.card_names = [data['card']['name'].replace('\n', '')]
    Card_Checks.element_id = {0 : int(data['card']['element'])}

    Transformation_Check_New(data)
    # Check_EZA_in_Card_Specials()




    # Just needed for Card row 1
    Card_Checks.card0_data[0] = read_json_from_zip(cardID0)

    # print("card 0 data:", Card_Checks.card0_data) # Debugging card 0 data output

    # TODO: When I add the transformation checking, just replace this with a json load from the saved jsons instead of the url shit.
    # if len(data['transformations']) > 1:
    #     for i in range(len(data['transformations']) - 1):
    #
    #         card_id_1 = data['transformations'][i + 1]['next_card']['id']
    #         url = f"https://dokkan.wiki/api/cards/{card_id_1}"
    #
    #         if not get_value('ENG_Check'):
    #             url = f"https://jpn.dokkan.wiki/api/cards/{card_id_1}"
    #
    #         response = requests.request("GET", url, headers=headers)
    #         data = response.json()
    #         Card_Checks.json_data[i + 1] = data
    
    
    # For causality hint
    Delete_Items('eball_mod_num100')
    # TODO: Idk wtf is wrong with this
    # with value_registry():
    #     add_int_value(default_value=data['card']['eball_mod_num100'], tag='eball_mod_num100')


    # if not get_value('Card_ID_Lua'):
    #         # print('Skipping')
    #     card_id_assets = Custom_Unit.card_id
    #     card_id_0_assets = str(card_id_assets[:-1]) + '0'
    #     Asset_Directory_Check(card_id_0_assets)
    #
    #     url = f'https://dokkaninfo.com/assets/japan/character/thumb/card_{card_id_0_assets}_thumb.png'
    #     thumb_exist = os.path.exists(f'assets/character/thumb/card_{card_id_0_assets}_thumb.png')
    #     if thumb_exist == False:
    #         download_image('assets/character/thumb/', url, f'card_{card_id_0_assets}_thumb.png')
    #     if get_value('Transformation_Check'):
    #         for i in range(len(Card_Checks.card_ids)):
    #             Card_ID = str(Card_Checks.card_ids[i])[:-1] + '0'
    #             # print(Card_ID)
    #             url = f'https://dokkaninfo.com/assets/japan/character/thumb/card_{Card_ID}_thumb.png'
    #             thumb_exist = os.path.exists(f'assets/character/thumb/card_{Card_ID}_thumb.png')
    #             if thumb_exist == False:
    #                 download_image('assets/character/thumb/', url, f'card_{Card_ID}_thumb.png')
                    

    # TODO: Honestly probably don't need this garbage anymore. Just gonna make a read from the jsons folder instead of doing all this.
    # Transformation_Unit_Card_Information()
    
    # This Unit_Checks() is meant for just the card input for query, there is a different section of code that checks for the Lua Input Text ID.
    try:
        Unit_Checks(data)
    except Exception as e:
        set_value('log_1', str(e) + '(Make sure database is up to date!)')
    return data

#################################################################################################################################################################################################################################################################

def Transformation_Texture_Registry():
    for i in range(len(Card_Checks.card_ids)):
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

#################################################################################################################################################################################################################################################################

def Create_Tabs():
    Transformation_Texture_Registry()
    # Minus 1 because there will always be a main tab, which counts as a unit.
    for i in range(Card_Checks.number_of_cards - 1):
        with tab(label=f'Unit {i + 2}', tag=f'Main_Card_Tab_Bar_{i + 1}', parent='Main_Tab_Bar'):
            Widget_Aliases.tags_to_delete.append(f'Main_Card_Tab_Bar_{i + 1}')
            

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
                        # add_input_text(tag=f'Card ID{i + 1}', width=95, default_value=Card_Checks.card_ids[0], parent=f'Card_Input_Image_Widget_Group_{i + 1}')
                        # Widget_Aliases.tags_to_delete.append(f'Card ID{i + 1}')
                        # Widget_Aliases.tags_to_delete.append(f'Card_Input_Image_Widget_Group_{i + 1}')
                    # Widget_Aliases.tags_to_delete.append(f'Placeholder_Image_{i + 1}')
                    # Widget_Aliases.tags_to_delete.append(f'Custom_Border_Thumb_Background_{i + 1}')
                    # Widget_Aliases.tags_to_delete.append(f'card_thumb_display_{i + 1}')
                    # Widget_Aliases.tags_to_delete.append(f'Custom_Border_Thumb_Border_{i + 1}')
                    add_separator()
                    

                with tab(label=f'Specials', tag=f'Specials_Tab_Card_{i + 1}'):
                    pass

                with tab(label=f'Leader Skill', tag=f'Leader_Skill_{i + 1}', show=False):
                    pass

                with tab(label=f'Active Skill', tag=f'Active_Skill_Card_{i + 1}', show=False):
                    pass

                with tab(label=f'Standby Skill', tag=f'Standby_Skill_{i + 1}', show=False):
                    pass
                
                with tab(label=f'Finish Skill', tag=f'Finish_Skill_{i + 1}', show=False):
                    pass
                
                with tab(label='Dokkan Field', tag=f'Dokkan_Field_{i + 1}', show=False):
                    pass
                
                with tab(label='Battle Params', tag=f'Battle_Params_{i + 1}', show=False):
                    pass

#################################################################################################################################################################################################################################################################
   
def Card_Thumb_Display():
    card_id_assets = get_value('Card ID')
    card_id_0_assets = str(card_id_assets[:-1]) + '0'
    width, height, channels, thumb_data = load_image(f'assets/character/thumb/card_{card_id_0_assets}_thumb.png')
    if not get_value('Transformation_Check'):
        
        with texture_registry():
            Delete_Items(f'Custom_Border_Thumb_Border_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
            Delete_Items(f'Custom_Border_Thumb_Background_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
            width, height, channels, border_data = load_image(f'logo/Custom_Border_Border_{Card_Checks.element_ids[Card_Checks.element_id[0]]}.png')
            add_dynamic_texture(width=250, height=250, default_value=border_data, tag=f'Custom_Border_Thumb_Border_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
            width, height, channels, bg_data = load_image(f'logo/Custom_Border_Background_{Card_Checks.element_ids[Card_Checks.element_id[0]]}.png')
            add_dynamic_texture(width=250, height=250, default_value=bg_data, tag=f'Custom_Border_Thumb_Background_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
                
            # set_value('Custom_Border_Thumb_Border_0', f'Custom_Border_Thumb_Border_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
            # set_value('Custom_Border_Thumb_Background_0', f'Custom_Border_Thumb_Background_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
            
        x, y = get_item_pos('Placeholder_Image_0')
        set_value('Card_Thumb_Texture_0', thumb_data)
        set_value('Custom_Border_Thumb_Border_Texture_0', border_data)
        set_value('Custom_Border_Thumb_Background_Texture_0', bg_data)
        configure_item('card_thumb_display_0', show=True)
        configure_item('Custom_Border_Thumb_Background_0', pos=(x,y), show=True)
        configure_item('card_thumb_display_0', pos=(x,y), show=True)
        configure_item('Custom_Border_Thumb_Border_0', pos=(x,y), show=True)
    else:
        for i in range(Card_Checks.number_of_cards):
            if i == 0:
                width, height, channels, thumb_data = load_image(f'assets/character/thumb/card_{card_id_0_assets}_thumb.png')
            else:
                if os.path.exists(f'assets/character/thumb/card_{Card_Checks.card_ids[i]}_thumb.png'):
                    width, height, channels, thumb_data = load_image(f'assets/character/thumb/card_{Card_Checks.card_ids[i]}_thumb.png')
                else:
                    Card_ID_Asset = str(Card_Checks.card_ids[i])
                    Card_ID_Asset = Card_ID_Asset[:-1] + '0'
                    url = f'https://dokkaninfo.com/assets/japan/character/thumb/card_{Card_ID_Asset}_thumb.png'
                    download_image('assets/character/thumb/', url, f'card_{Card_ID_Asset}_thumb.png')
                    width, height, channels, thumb_data = load_image(f'assets/character/thumb/card_{Card_ID_Asset}_thumb.png')
            with texture_registry():
                Delete_Items(f'Custom_Border_Thumb_Border_Texture_{Card_Checks.element_ids[Card_Checks.element_id[i]]}')
                Delete_Items(f'Custom_Border_Thumb_Background_Texture_{Card_Checks.element_ids[Card_Checks.element_id[i]]}')
                width, height, channels, border_data = load_image(f'logo/Custom_Border_Border_{Card_Checks.element_ids[Card_Checks.element_id[0]]}.png')
                add_dynamic_texture(width=250, height=250, default_value=border_data, tag=f'Custom_Border_Thumb_Border_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
                width, height, channels, bg_data = load_image(f'logo/Custom_Border_Background_{Card_Checks.element_ids[Card_Checks.element_id[0]]}.png')
                add_dynamic_texture(width=250, height=250, default_value=bg_data, tag=f'Custom_Border_Thumb_Background_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
                    
                # set_value('Custom_Border_Thumb_Border_0', f'Custom_Border_Thumb_Border_Texture_{Card_Checks.element_ids[Card_Checks.element_id[i]]}')
                # set_value('Custom_Border_Thumb_Background_0', f'Custom_Border_Thumb_Background_Texture_{Card_Checks.element_ids[Card_Checks.element_id[i]]}')
                    
            # Just grab this 'Placeholder_Image_0' to get the same position, don't know why I was trying to grab the other ones when I can just use this one.
            # This image shit was coded pretty poorly by me, may have to recode it later, hopefully not.
            x, y = get_item_pos('Placeholder_Image_0')
            set_value(f'Card_Thumb_Texture_{i}', thumb_data)
            set_value(f'Custom_Border_Thumb_Border_Texture_{i}', border_data)
            set_value(f'Custom_Border_Thumb_Background_Texture_{i}', bg_data)
            configure_item(f'card_thumb_display_{i}', show=True)
            configure_item(f'Custom_Border_Thumb_Background_{i}', pos=(x,y), show=True)
            configure_item(f'card_thumb_display_{i}', pos=(x,y), show=True)
            configure_item(f'Custom_Border_Thumb_Border_{i}', pos=(x,y), show=True)
    # add_image('Placeholder_Image_Texture_0', tag='Placeholder_Image_0')
    # add_image('Custom_Border_Thumb_Background_Texture_0', tag='Custom_Border_Thumb_Background_0', show=False)
    # add_image('Card_Thumb_Texture_0', tag='card_thumb_display_0', show=False)
    # add_image('Custom_Border_Thumb_Border_Texture_0', tag='Custom_Border_Thumb_Border_0', show=False)

#################################################################################################################################################################################################################################################################

def Grab_Values(data):
    # May have to come back to this when standby units inevitably get EZAs in the future.
    if get_value('EZA_Check'):
        if 'passive_skill_name' in data['card']:
            Card_Checks.passive_ids.append(data['optimal_awakening_growth']['passive_skill_id'])
            Card_Checks.passive_names.append(data['optimal_awakening_growth']['passive_skill_name'])
            Card_Checks.passive_descriptions.append(data['optimal_awakening_growth']['passive_skill_description'])
        else:
            Card_Checks.passive_ids.append(None)
            Card_Checks.passive_names.append(None)
            Card_Checks.passive_descriptions.append(None)
        Card_Checks.special_set_ids.append([data['specials'][i]['id'] for i in range(len(data['specials'])) if '(Extreme)' in data['specials'][i]['name']])
        Card_Checks.special_set_names.append([data['specials'][i]['name'] for i in range(len(data['specials'])) if '(Extreme)' in data['specials'][i]['name']])
        Card_Checks.special_set_descriptions.append([data['specials'][i]['description'] for i in range(len(data['specials'])) if '(Extreme)' in data['specials'][i]['name']])
        Card_Checks.special_set_conditions.append([data['specials'][i]['causality_description'] for i in range(len(data['specials'])) if '(Extreme)' in data['specials'][i]['name'] and 'causality_description' in data['specials'][i]])
        if len(data['finish_skills']) > 0:
            
            Card_Checks.finish_skill_ids.append([data['finish_skills'][i]['id'] for i in range(len(data['finish_skills']))])
            Card_Checks.finish_skill_names.append([data['finish_skills'][i]['name'] for i in range(len(data['finish_skills']))])
            Card_Checks.finish_skill_desc.append([data['finish_skills'][i]['effect_description'] for i in range(len(data['finish_skills']))])
            Card_Checks.finish_skill_cond.append([data['finish_skills'][i]['condition_description'] for i in range(len(data['finish_skills']))])
        else:
            Card_Checks.finish_skill_ids.append([])
            
        if len(data['standby_skills']) > 0:
            Card_Checks.standby_skill_ids.append([data['standby_skills'][i]['id'] for i in range(len(data['standby_skills']))])
            Card_Checks.standby_skill_names.append([data['standby_skills'][i]['name'] for i in range(len(data['standby_skills']))])
            Card_Checks.standby_skill_desc.append([data['standby_skills'][i]['effect_description'] for i in range(len(data['standby_skills']))])
            Card_Checks.standby_skill_cond.append([data['standby_skills'][i]['condition_description'] for i in range(len(data['standby_skills']))])
        else:
            Card_Checks.standby_skill_ids.append([])
            
        if 'dokkan_fields' in data and len(data['dokkan_fields']) > 0:
            Card_Checks.dokkan_field_ids.append([data['dokkan_fields'][i]['id'] for i in range(len(data['dokkan_fields']))])
            Card_Checks.dokkan_field_names.append([data['dokkan_fields'][i]['name'] for i in range(len(data['dokkan_fields']))])
            Card_Checks.dokkan_field_desc.append([data['dokkan_fields'][i]['description'] for i in range(len(data['dokkan_fields']))])
            Card_Checks.dokkan_field_resource_ids.append([data['dokkan_fields'][i]['resource_id'] for i in range(len(data['dokkan_fields']))])
        else:
            Card_Checks.dokkan_field_ids.append([])

    else:
        if 'passive_skill_name' in data['card']:
            Card_Checks.passive_ids.append(data['card']['passive_skill_set_id'])
            Card_Checks.passive_names.append(data['card']['passive_skill_name'])
            Card_Checks.passive_descriptions.append(data['card']['passive_skill_desc'])
        else:
            Card_Checks.passive_ids.append(None)
            Card_Checks.passive_names.append(None)
            Card_Checks.passive_descriptions.append(None)
            
        Card_Checks.special_set_ids.append([data['specials'][i]['id'] for i in range(len(data['specials']))])
        Card_Checks.special_set_names.append([data['specials'][i]['name'] for i in range(len(data['specials']))])
        Card_Checks.special_set_descriptions.append([data['specials'][i]['description'] for i in range(len(data['specials']))])
        Card_Checks.special_set_conditions.append([data['specials'][i]['causality_description'] if 'causality_description' in data['specials'][i] else [] for i in range(len(data['specials']))])

        # Also if you decide to create units that have multiple standby transformations
        if len(data['finish_skills']) > 0:
            
            Card_Checks.finish_skill_ids.append([data['finish_skills'][i]['id'] for i in range(len(data['finish_skills']))])
            Card_Checks.finish_skill_names.append([data['finish_skills'][i]['name'] for i in range(len(data['finish_skills']))])
            Card_Checks.finish_skill_desc.append([data['finish_skills'][i]['effect_description'] for i in range(len(data['finish_skills']))])
            Card_Checks.finish_skill_cond.append([data['finish_skills'][i]['condition_description'] for i in range(len(data['finish_skills']))])
        else:
            Card_Checks.finish_skill_ids.append([])
            
        if len(data['standby_skills']) > 0:
            Card_Checks.standby_skill_ids.append([data['standby_skills'][i]['id'] for i in range(len(data['standby_skills']))])
            Card_Checks.standby_skill_names.append([data['standby_skills'][i]['name'] for i in range(len(data['standby_skills']))])
            Card_Checks.standby_skill_desc.append([data['standby_skills'][i]['effect_description'] for i in range(len(data['standby_skills']))])
            Card_Checks.standby_skill_cond.append([data['standby_skills'][i]['condition_description'] for i in range(len(data['standby_skills']))])
        else:
            Card_Checks.standby_skill_ids.append([])
            
        if 'dokkan_fields' in data and len(data['dokkan_fields']) > 0:
            Card_Checks.dokkan_field_ids.append([data['dokkan_fields'][i]['id'] for i in range(len(data['dokkan_fields']))])
            Card_Checks.dokkan_field_names.append([data['dokkan_fields'][i]['name'] for i in range(len(data['dokkan_fields']))])
            Card_Checks.dokkan_field_desc.append([data['dokkan_fields'][i]['description'] for i in range(len(data['dokkan_fields']))])
            Card_Checks.dokkan_field_resource_ids.append([data['dokkan_fields'][i]['resource_id'] for i in range(len(data['dokkan_fields']))])
        else:
            Card_Checks.dokkan_field_ids.append([])
            
    
    # When the region doesn't matter
    Card_Checks.card_names.append([data['card']['name'].replace('\n', '')])      


#################################################################################################################################################################################################################################################################

# Download Function with PIL
def download_image(download_path, url, filename):
    
    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    file_path = download_path + filename

    
    with open(file_path, 'wb') as f:
        image.save(f, 'png')

#################################################################################################################################################################################################################################################################

def Asset_Directory_Check(CardID0):
    asset_directory = ['assets', 'assets/character', 'assets/character/thumb', 'assets/character/card', f'assets/character/card/{CardID0}' , f'assets/character/card/{CardID0}/ja']
    for i in range(len(asset_directory)):
        exists = os.path.exists(asset_directory[i])
        if exists is False:
            os.mkdir(asset_directory[i])
        else:
            pass

#################################################################################################################################################################################################################################################################

def Lua_Downloader():
    
    # lua_directory = ['luas', 'luas/' + name + ' (' + get_value('Card ID') + ')']
    
    # def download_and_create_directory(lua_list, url, dir_name):
    #     if lua_list:
    #         dir_path = os.path.join('luas', name, dir_name)
    #         if not os.path.exists(dir_path):
    #             os.makedirs(dir_path)
    #         for item in lua_list:
    #             download_lua_script(url + item + '.lua', os.path.join(dir_path, item + '.lua'))
    #################################################################################
    def download_lua_script(url, save_path):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful

            with open(save_path, 'wb') as file:
                file.write(response.content)

            set_value('log_1', f"Lua script downloaded and saved to: {save_path}")
        except requests.exceptions.RequestException as e:
            set_value('log_1', f"Error occurred while downloading the Lua script: {e}")
    #################################################################################
    # def Lua_Dir_Check():
    #     for i in range(len(lua_directory)):
    #         exists = os.path.exists(lua_directory[i])
    #         if exists is False:
    #             os.mkdir(lua_directory[i])
    #         else:
    #             pass
    #################################################################################        

    def Lua_check_and_download(name):
        
        super_attack_url = f"https://dokkaninfo.com/assets/japan/lua/ab_script/attack_sp/"
        active_skill_url = f"https://dokkaninfo.com/assets/japan/lua/ab_script/active_skill/"
        ultimate_skill_url = f"https://dokkaninfo.com/assets/japan/lua/ab_script/ultimate_special/"
        standby_skill_url = f"https://dokkaninfo.com/assets/japan/lua/ab_script/standby_skill/"
        finish_skill_url = f"https://dokkaninfo.com/assets/japan/lua/ab_script/finish_skill/"
        passive_skill_effect_url = f"https://dokkaninfo.com/assets/japan/lua/ab_script/passive_skill_effect/"
        attack_counter_url = f"https://dokkaninfo.com/assets/japan/lua/ab_script/attack_counter/"
        nullification_url = f"https://dokkaninfo.com/assets/japan/lua/ab_script/ab_sys/"
        super_lua = []
        active_lua = []
        ultimate_lua = []
        standby_lua = []
        finisher_lua = []
        pse_lua = []
        counter_lua = []
        null_lua = []
        
        for i in range(get_value('Number_Of_Luas')):
            luas = (get_value(f'Lua_{i}'))
            # print(luas)
            if luas[:2] == 'sp':
                super_lua.append(luas)
            elif luas[:2] == 'tf':
                active_lua.append(luas)
            elif luas[:2] == 'ut':
                ultimate_lua.append(luas)
            elif luas[:3] == 'stb':
                standby_lua.append(luas)
            elif luas[:2] == 'fi':
                finisher_lua.append(luas)
            elif luas[:3] == 'pse':
                pse_lua.append(luas)
            elif luas[:1] == 'c':
                counter_lua.append(luas)
            elif luas[:2] == 'as':
                null_lua.append(luas)

        # print(finisher_lua)
        if super_lua:
            path = os.path.join('luas', name, 'attack_sp')
            if not os.path.exists(path):
                os.makedirs(path)
            for i in range(len(super_lua)):
                    download_lua_script(super_attack_url + super_lua[i] + '.lua', os.path.join(path, super_lua[i] + '.lua'))

        if active_lua:
            path = os.path.join('luas', name, 'active_skill')
            if not os.path.exists(path):
                os.makedirs(path)
            for i in range(len(active_lua)):
                    download_lua_script(active_skill_url + active_lua[i] + '.lua', os.path.join(path, active_lua[i] + '.lua'))
        
            
        if ultimate_lua:
            path = os.path.join('luas', name, 'ultimate_special')
            if not os.path.exists(path):
                os.makedirs(path)
            for i in range(len(ultimate_lua)):
                    download_lua_script(ultimate_skill_url + ultimate_lua[i] + '.lua', os.path.join(path, ultimate_lua[i] + '.lua'))
        
            
        if standby_lua:
            path = os.path.join('luas', name, 'standby_skill')
            if not os.path.exists(path):
                os.makedirs(path)
            for i in range(len(standby_lua)):
                    download_lua_script(standby_skill_url + standby_lua[i] + '.lua', os.path.join(path, standby_lua[i] + '.lua'))
        
            
        if finisher_lua:
            path = os.path.join('luas', name, 'finish_skill')
            if not os.path.exists(path):
                os.makedirs(path)
            for i in range(len(finisher_lua)):
                    download_lua_script(finish_skill_url + finisher_lua[i] + '.lua', os.path.join(path, finisher_lua[i] + '.lua'))
        
            
        if pse_lua:
            path = os.path.join('luas', name, 'passive_skill_effect')
            if not os.path.exists(path):
                os.makedirs(path)
            for i in range(len(pse_lua)):
                    download_lua_script(passive_skill_effect_url + pse_lua[i] + '.lua', os.path.join(path, pse_lua[i] + '.lua'))
        
            
        if counter_lua:
            path = os.path.join('luas', name, 'attack_counter')
            if not os.path.exists(path):
                os.makedirs(path)
            for i in range(len(counter_lua)):
                    download_lua_script(attack_counter_url + counter_lua[i] + '.lua', os.path.join(path, counter_lua[i] + '.lua'))
        
            
        if null_lua:
            path = os.path.join('luas', name, 'ab_sys')
            if not os.path.exists(path):
                os.makedirs(path)
            for i in range(len(null_lua)):
                    download_lua_script(nullification_url + null_lua[i] + '.lua', os.path.join(path, null_lua[i] + '.lua'))
        

        

        
#################################################################################################################################################################################################################################################################

# Downloads ENG version of Character Assets
def Card_Character_Assets(card_id_0, CardID0):
    # try:
    #     os.mkdir(f'assets');os.mkdir(f'assets/character');os.mkdir(f'assets/character/card');os.mkdir(f'assets/character/card/ja')
    # except FileExistsError:
    #     pass
    
    Asset_Directory_Check(CardID0)
    # Just card folder
    download_path_card = f'assets/character/card/{CardID0}/'
    download_path_ja = f'assets/character/card/{CardID0}/ja/'
    assets_card = [f"{card_id_0}.png",
		f"card_{card_id_0}_bg.png",
		f"card_{card_id_0}_character.png",
		f"card_{card_id_0}_circle.png",
		f"card_{card_id_0}_cutin.png",
		f"card_{card_id_0}_effect.png",
		f"card_{card_id_0}_sticker_mask.png",
		f"card_{card_id_0}_piece.png",
		f"card_{card_id_0}sp_cutin_1.png"]
    
    filename_card = [f"{CardID0}.png",
		f"card_{CardID0}_bg.png",
		f"card_{CardID0}_character.png",
		f"card_{CardID0}_circle.png",
		f"card_{CardID0}_cutin.png",
		f"card_{CardID0}_effect.png",
		f"card_{CardID0}_sticker_mask.png",
		f"card_{CardID0}_piece.png",
		f"card_{CardID0}sp_cutin_1.png"]
    
    assets_en = [
		f"en/card_{card_id_0}_sp_name.png",
		f"en/card_{card_id_0}_sp_phrase.png",
  		f"en/card_{card_id_0}_sp02_name.png",
		f"en/card_{card_id_0}_sp02_phrase.png",
    	f"en/card_{card_id_0}_sp03_name.png",
		f"en/card_{card_id_0}_sp03_phrase.png",
    	f"en/card_{card_id_0}_sp04_name.png",
		f"en/card_{card_id_0}_sp04_phrase.png",
    	f"en/card_{card_id_0}_sp05_name.png",
		f"en/card_{card_id_0}_sp05_phrase.png",]
    
    assets_ja = [
		f"ja/card_{card_id_0}_sp_name.png",
		f"ja/card_{card_id_0}_sp_phrase.png",
  		f"ja/card_{card_id_0}_sp02_name.png",
		f"ja/card_{card_id_0}_sp02_phrase.png",
    	f"ja/card_{card_id_0}_sp03_name.png",
		f"ja/card_{card_id_0}_sp03_phrase.png",
    	f"ja/card_{card_id_0}_sp04_name.png",
		f"ja/card_{card_id_0}_sp04_phrase.png",
    	f"ja/card_{card_id_0}_sp05_name.png",
		f"ja/card_{card_id_0}_sp05_phrase.png",]

    filename_ja = [
		f"card_{CardID0}_sp_name.png",
		f"card_{CardID0}_sp_phrase.png",
  		f"card_{CardID0}_sp02_name.png",
		f"card_{CardID0}_sp02_phrase.png",
    	f"card_{CardID0}_sp03_name.png",
		f"card_{CardID0}_sp03_phrase.png",
    	f"card_{CardID0}_sp04_name.png",
		f"card_{CardID0}_sp04_phrase.png",
    	f"card_{CardID0}_sp05_name.png",
		f"card_{CardID0}_sp05_phrase.png",]


    print('Downloading card assets.')
    for i in range(len(assets_card)):
        try:
            # Cards section
            url = 'https://dokkaninfo.com/assets/japan/character/card/' + str(card_id_0) + '/' + assets_card[i]
            filename = filename_card[i]
            download_image(download_path_card, url, filename)

        except UnidentifiedImageError:
            pass
        
    # Check for ENG Super Names & Phrases
    log = "Checking if ENG Assets Exist"
    set_value("log_1", log)
    ENG_assets = None
    JP_assets = None
    url = 'https://dokkaninfo.com/assets/global/en/character/card/' + str(card_id_0) + '/' + str(card_id_0) +  '.png' 
    status_code = requests.request('GET', url)

    if status_code.status_code == 200:
        ENG_assets = 1
        log = "ENG Assets Found!"
        set_value("log_1", log)
    else:
        log = "ENG Assets Not Found, Downloading JP Assets"
        set_value("log_1", log)
        pass
        

    
    if ENG_assets == 1:
        log = "Downloading ENG Super Names & Phrases"
        set_value("log_1", log)
        for i in range(len(assets_ja)):
            try:
                # Ja section
                url = 'https://dokkaninfo.com/assets/global/en/character/card/' + str(card_id_0) + '/' + assets_en[i]
                filename = filename_ja[i]
                download_image(download_path_ja, url, filename)


            except UnidentifiedImageError:
                pass
        log = "Download Complete!"
        set_value("log_1", log)
        
    else:
        for i in range(len(assets_ja)):
            try:
                # Ja section
                url = 'https://dokkaninfo.com/assets/japan/character/card/' + str(card_id_0) + '/' + assets_ja[i]
                filename = filename_ja[i]
                download_image(download_path_ja, url, filename)


            except UnidentifiedImageError:
                pass
        log = "Download Complete!"
        set_value("log_1", log)
    

# def Card_Thumb_Display():
    
#################################################################################################################################################################################################################################################################

def Category_Downloads(global_categories_id_list, jp_categories_id_list):
    # print(global_categories_id_list)
    
    
    cat_num = jp_categories_id_list[len(jp_categories_id_list) - 1]
    category_asset_check = os.path.exists(f'categories/Category_{cat_num}_on.png')
    if category_asset_check == False: 
        if len(global_categories_id_list) == len(jp_categories_id_list):
            for i in range(len(global_categories_id_list)):
                print(global_categories_id_list[i])
                if global_categories_id_list[i] < 10:
                    download_image('categories/', f'https://dokkan.wiki/assets/global/en/card_category/label/card_category_label_000{global_categories_id_list[i]}_b_on.png', f'Category_{global_categories_id_list[i]}_on.png')
                    download_image('categories/', f'https://dokkan.wiki/assets/global/en/card_category/label/card_category_label_000{global_categories_id_list[i]}_b_off.png', f'Category_{global_categories_id_list[i]}_off.png')
                elif global_categories_id_list[i] >= 10 and global_categories_id_list[i] < 100:
                    download_image('categories/', f'https://dokkan.wiki/assets/global/en/card_category/label/card_category_label_00{global_categories_id_list[i]}_b_on.png', f'Category_{global_categories_id_list[i]}_on.png')
                    download_image('categories/', f'https://dokkan.wiki/assets/global/en/card_category/label/card_category_label_00{global_categories_id_list[i]}_b_off.png', f'Category_{global_categories_id_list[i]}_off.png')
                else:
                    download_image('categories/', f'https://dokkan.wiki/assets/global/en/card_category/label/card_category_label_0{global_categories_id_list[i]}_b_on.png', f'Category_{global_categories_id_list[i]}_on.png')
                    download_image('categories/', f'https://dokkan.wiki/assets/global/en/card_category/label/card_category_label_0{global_categories_id_list[i]}_b_off.png', f'Category_{global_categories_id_list[i]}_off.png')
        if len(global_categories_id_list) != len(jp_categories_id_list):
            diff = len(jp_categories_id_list) - len(global_categories_id_list)
            diff_range = len(jp_categories_id_list) - diff
            for i in range(diff):
                if jp_categories_id_list[diff_range] < 10:
                    download_image('categories/', f'https://jpn.dokkan.wiki/assets/japan/card_category/label/card_category_label_0{jp_categories_id_list[diff_range]}_b_on.png', f'Category_{jp_categories_id_list[diff_range]}_on.png')
                    download_image('categories/', f'https://jpn.dokkan.wiki/assets/japan/card_category/label/card_category_label_0{jp_categories_id_list[diff_range]}_b_off.png', f'Category_{jp_categories_id_list[diff_range]}_off.png')
                elif jp_categories_id_list[diff_range] >= 10 and jp_categories_id_list[diff_range] < 100:
                    download_image('categories/', f'https://jpn.dokkan.wiki/assets/japan/card_category/label/card_category_label_00{jp_categories_id_list[diff_range]}_b_on.png', f'Category_{jp_categories_id_list[diff_range]}_on.png')
                    download_image('categories/', f'https://jpn.dokkan.wiki/assets/japan/card_category/label/card_category_label_00{jp_categories_id_list[diff_range]}_b_off.png', f'Category_{jp_categories_id_list[diff_range]}_off.png')
                else:
                    download_image('categories/', f'https://jpn.dokkan.wiki/assets/japan/card_category/label/card_category_label_0{jp_categories_id_list[diff_range]}_b_on.png', f'Category_{jp_categories_id_list[diff_range]}_on.png')
                    download_image('categories/', f'https://jpn.dokkan.wiki/assets/japan/card_category/label/card_category_label_0{jp_categories_id_list[diff_range]}_b_off.png', f'Category_{jp_categories_id_list[diff_range]}_off.png')
                diff_range += 1
                
#################################################################################################################################################################################################################################################################


def Transformation_Check_New(data : dict, visited=None):
    card_ids = []
    current_data = data['passive_skill']['skills']
    standby_data = {}
    active_data = {}

    if 'standby_skills' in data and data['standby_skills']:
        standby_data = data['standby_skills']

    if 'active_skill' in data and data['active_skill']:
        active_data = data['active_skill']

    for i in range(10):
        for skill in current_data:
            if skill['efficacy_type'] == '103': # Transformation
                card_ids.append(skill['eff_value1'])
                current_data = read_json_from_zip(skill['eff_value1'])['passive_skill']['skills']

            elif skill['efficacy_type'] == '131': # Reversible Exchange
                card_ids.append(skill['eff_value1'])
                current_data = {}

            elif skill['efficacy_type'] == '79': # Rage
                card_ids.append(skill['eff_value1'])
                current_data = {}

        if 'active_skill' in data and data['active_skill']:
            for skill in active_data:
                if skill['efficacy_type'] == '103': # Transformation
                    card_ids.append(skill['eff_val1'])
                    active_data = {}

                elif skill['efficacy_type'] == '131': # Reversible Exchange
                    card_ids.append(skill['eff_val1'])
                    active_data = {}

                elif skill['efficacy_type'] == '79': # Rage
                    card_ids.append(skill['eff_val1'])
                    active_data = {}

        if 'standby_skills' in data and data['standby_skills']:
            for standby_skill in standby_data:
                if standby_skill['efficacy_type'] == '103':
                    card_ids.append(ast.literal_eval(standby_skill['efficacy_values'])[0])
                    standby_data = {}
                    # standby_data = read_json_from_zip(ast.literal_eval(standby_skill['efficacy_values'])[0])['standby_skills']


    if card_ids:
        # set_value('Transformation_Check', True)
        for index, card_id in enumerate(card_ids):
            transformed_card_data = read_json_from_zip(card_id)
            transformed_base_card_data = read_json_from_zip(str(int(card_id) - 1))
            Card_Checks.json_data[index + 1] = transformed_card_data
            Card_Checks.card0_data[index + 1] = transformed_base_card_data
            Card_Checks.card_ids.append(transformed_card_data['card']['id'])
            Card_Checks.card_names.append(transformed_card_data['card']['name'].replace('\n', ''))
            Card_Checks.element_id[index + 1] = int(data['card']['element'])

#################################################################################################################################################################################################################################################################

# Checks the Card_Checks.card0_data for EZA specials (Use after Transformation_Check_New in Card_Information)
# def Check_EZA_in_Card_Specials():
#     for i in range(len(Card_Checks.card_ids)):
#         card_specials = Card_Checks.json_data[i]['card_specials']
#         print('debug')
#         # for card_special in Card_Checks.json_data[i]['card_specials']:
#         #     print(card_special)