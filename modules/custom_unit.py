from dearpygui.dearpygui import *
from . cards import Card_Table_Combos, Link_Skills_Query, Synced_Callback, EZA_Callback, Super_EZA_Callback, Ex_Super_Callback, Ex_Super_Combo_Callback, Ex_Super_Probablity_Callback, Rarity_Callback, Card_Queries, Element_Callback, Name_Change_Callback
from . categories import Card_Categories_Window, Card_Categories_Wiki, Create_New_Category_Tab
from . download import Lua_Downloader, Create_Tabs, Card_Thumb_Display, Card_Character_Assets
from . effect_pack import Effect_Packs_Widgets
from . passive import Passive_Add, Passive_Del, Passive_Skill_Query
from . specials import Special_Skills_Add, Special_Skills_Del, Specials_Add, Specials_Del, Specials_Query
from . special_views import Special_View_Widgets
from . SQL_file import sql_write_to_file,sql_output_data
from . leader import Leader_Combo, Leader_Cat_Selection, Leader_Efficacy_Value_Changer, Leader_Resize, Resize_Widget, Resize_Description, Leader_Skill_Set_Values, Leader_Create_Combos, Leader_Ki_Selection, Leader_Skill_Query
from . active_skill import Active_Skill_Add, Active_Skill_Del, Active_Skill_Query
from . standby_finish import Standby_Skill_Query, Finish_Skill_Query
from . battle_params import Battle_Params_Information, Battle_Param_Presets
from . dokkan_field import Dokkan_Field_Query
from . causality import Causality_Hint
from . download import download_image, Card_Information
import easygui
import os
from . configs import Config_Read
from . classes import Database, Custom_Unit, Card_Checks, Card, Passive_Skill, Active_Skill, Active_Skill_Set, Leader_Skill_Info, Standby_Skill_Set, Standby_Skill, Finish_Skill_Set, Finish_Skill, Efficacy_Values, String_Length, Transformation_Descriptions, Battle_Params, Widget_Aliases, Special_Set, Specials, Card_Specials, Dokkan_Field, Effect_Pack, Special_Views
from .functions import Table_ID, Delete_Items, Text_Resize, Table_Combo_Inputs, Table_Inputs, Resize_Table, \
    Delete_Table, Row_Checker, Traceback_Logging, Clear_Class_Tags_List, Text_Resize_2, Resize_Table_Width, load_JSON, \
    grab_card_id, read_json_from_zip, read_png_from_zip
from . jp_translations import Translations
import re
import ast
import sqlite3
import threading
import time

db = Database()

def Main_Tab_Bar_Callback():
    # if sender == 451:
    # if not Custom_Unit.json:
    Custom_Unit.card_number += 1
    
    Custom_Unit_Create_Tabs()
    # Custom_Unit_Hide_Tabs()
    # Custom_Unit_Selectables(card=Custom_Unit.card_number)
    Widgets_Combined()
    Create_New_Category_Tab()
    
    if Custom_Unit.json:
        Custom_Unit.json = False


def get_card_id(sender, data, app_data):
    global card_id
    Custom_Unit.card_id = data
    card_id = sender
    configure_item('Card_ID_Lua', hint=card_id)
    CardID0 = str(card_id)
    if len(CardID0) > 2:
        CardID0 = CardID0.replace(CardID0[1], '3')
    CardID0 = CardID0[:-1] + '0'
    set_value('CardID0', CardID0)
    CardID1 = CardID0[:-1] + '1'
    set_value('CardID1', CardID1)
    # for i in range(Leader_Skill_Info.rows):
        # set_value(f'l_leader_skill_set_id_{i}', sender)


    try:
        if card_id != None:
            #print('Card ID:', card_id)
            log2 = ('Card ID: ' + card_id)
            # set_value('log2', log2)
    except NameError:
        #sprint('No card ID entered')
        log2 = 'No card ID entered'
        set_value('log2', log2)
    return card_id

       
def save_callback():
    global card_id, config
    
    
    
    CardID0 = card_id
    CardID0 = CardID0

    CardID0 = CardID0.replace(CardID0[1], '3')
    CardID0 = CardID0[:-1] + '0'
    
    set_value('log_1', 'Card ID has been saved')

    ### Prevents it from appearing on re-query if going from transformation unit to single unit.
    configure_item('Standby_Skill_0', show=False)
    configure_item('Finish_Skill_0', show=False)
    configure_item('Active_Skill_Card_0', show=False)
    configure_item('Dokkan_Field_0', show=False)
    configure_item('Battle_Params_0', show=False)
    if len(Widget_Aliases.tags_to_delete) > 0:
        Delete_Items(Widget_Aliases.tags_to_delete)
        Widget_Aliases.tags_to_delete.clear()
        Clear_Class_Tags_List()
    
    
    # Grabs card information from Dokkan.info which is used for various functions
    card_information = Card_Information(card_id)
    card_name = get_value('Card_Name_Display_0')
    wiki_card_id = card_information['card']['id']
    if get_value('ENG_Check'):
        wiki_link = f'https://dokkan.wiki/cards/{wiki_card_id}'
    else:
        wiki_link = f'https://jpn.dokkan.wiki/cards/{wiki_card_id}'
    # user_status = card_name + '\n' + wiki_link
    # Set the Rich Presence information
    # if RPC:
    #     RPC.update(
    #         state='Creating a Unit',
    #         details=card_name,
    #         large_image="zamasu_and_vegito",
    #         small_image="gold_small_image",
    #         start=time.time(),
    #         buttons=[{"label": "Unit Wiki Page", "url": wiki_link}]
    #         # https://discord.gg/EWTyTnPhn7
    #     )
    
    if get_value('Transformation_Check'):
        Create_Tabs()
        # Transformation_Unit_Card_Information()
        # print(Card_Checks.battle_params)
        # print(Card_Checks.standby_skill_ids)
        # print(Card_Checks.finish_skill_ids)
        # print(Card_Checks.card_ids)
        
    
    if not get_value('Custom_Unit'):
        thread1 = threading.Thread(target=Card_Thumb_Display)
        thread2 = threading.Thread(target=Card_Queries)
        thread3 = threading.Thread(target=Passive_Skill_Query)
        thread4 = threading.Thread(target=Specials_Query)
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        # Card_Thumb_Display()
        # Card_Widgets()
        # Card_Queries()
        
        # Passive_Widgets()
        # Passive_Skill_Query()
        
        # Specials_Query()
        # Leader_Skill_Query()
        if Card_Checks.active_skill_ids:
            print(Card_Checks.active_skill_ids)
            Active_Skill_Widgets()
            Active_Skill_Query()
        if Card_Checks.standby_skill_ids:
            print(Card_Checks.standby_skill_ids)
            Standby_Skill_Query()
        if Card_Checks.finish_skill_ids:
            Finish_Skill_Query()
        if Card_Checks.dokkan_field_ids:
            Dokkan_Field_Query()
        if get_value('Transformation_Check'):
            # Set_Param_Type()
            Battle_Params_Information()
            pass
        # if not get_value('Transformation_Check'):
        Causality_Hint()
        Card_Categories_Wiki(card_information)
        Leader_Skill_Query()
    
    set_value('log_1', 'Query Successful!')
    
    Translations.Super_Attacks_Names.clear()
    Translations.Super_Attacks.clear()
    
def download_callback():
    card_id_assets = get_value('Card ID')
    card_id_0_assets = str(card_id_assets[:-1]) + '0'
    # print(card_id_0_assets)
    CardID0_assets = card_id_0_assets.replace(card_id_0_assets[1], '3')
    CardID0_assets = str(CardID0_assets[:-1]) + '0'
    # print(CardID0_assets)


    Card_Character_Assets(card_id_0=card_id_0_assets, CardID0=CardID0_assets)

    # set_value('log_1', log)

def edit_callback():
    #configure_item('Card ID', enabled=True)
    log = 'You can now edit the Card ID'
    #print(log)
    set_value('log_1', log)



def Export_as_SQL():

    sql_file_data = sql_output_data(get_value(Card.row_names[1] + '_Card_0_Row_0'))

    sql_file_name = get_value('Filename')
    sql_write_to_file(sql_file_name, sql_file_data)
    
    set_value('log_1', 'SQL Exported')
    
def Custom_Query_Window(tag_id):
    card = Custom_Unit.card_number
    Custom_Unit.custom_execute_number = Table_ID(tag_id)
    selectable_labels = ['Card', 'Passive', 'Specials', 'Categories', 'Leader Skill', 'Active Skill', 'Standby Skill', 'Finish Skill', 'Dokkan Field', 'Battle Params']
    selectable_tags = ['Card_Query_Selectable', 'Passive_Query_Selectable', 'Specials_Query_Selectable','Category_Query_Selectable', 'Leader_Skill_Query_Selectable', 'Active_Skill_Query_Selectable',
                        'Standby_Skill_Query_Selectable', 'Finish_Skill_Query_Selectable', 'Dokkan_Field_Query_Selectable', 'Battle_Params_Query_Selectable']
    Delete_Items('Custom_Query_Window')
    with window(label='Custom Query', tag='Custom_Query_Window', width=215, height=155, pos=[135,125]):
        with group(tag='Custom_Query_Selectables_Group', horizontal=True):
            with group(tag='Custom_Query_Selectables_Group_1st_Half'):
                for i in range(5):
                    add_selectable(label=selectable_labels[i], tag=selectable_tags[i], width=80)
            with group(tag='Custom_Query_Selectables_Group_2nd_Half'):
                for i in range(5):
                    add_selectable(label=selectable_labels[i + 5], tag=selectable_tags[i + 5], width=80)
        add_separator(tag='Custom_Query_Separator')
        bind_item_theme('Custom_Query_Selectables_Group', 'Custom_Unit_Selectable_Theme')
        with group(horizontal=True, tag='Custom_Query_Execute_Button_Group'):
            add_button(label='Execute', tag=f'Custom_Query_Execute_Button_{card}', callback=Execute_Custom_Query)
            add_button(label='Execute All', tag=f'Custom_Query_Execute_All_Button_{card}', callback=Execute_Custom_Query)

########################################################################################################################################################################################################
def Execute_Custom_Query(tag_id):
    from modules import RPC
    card = Custom_Unit.custom_execute_number
    data = Card_Information(Custom_Unit.card_id)
            
    # data = Card_Information(Custom_Unit.card_id)
    configure_item('Custom_Query_Window', show=False)
    
    if tag_id == f'Custom_Query_Execute_Button_{card}':
        Custom_Unit.execute_all = False
        if get_value('Card_Query_Selectable'):
            Custom_Unit_Card_Queries(card=card)
        if get_value('Passive_Query_Selectable'):
            Custom_Unit_Passive_Skill_Query(card=card)
        if get_value('Specials_Query_Selectable'):
            Custom_Unit_Specials_Query(card=card)
        if get_value('Leader_Skill_Query_Selectable'):
            Custom_Unit_Leader_Skill_Query(card=card)
        if get_value('Active_Skill_Query_Selectable'):
            Custom_Unit_Active_Skill_Query(card=card)
        if get_value('Standby_Skill_Query_Selectable'):
            Custom_Unit_Standby_Skill_Query(card=card)
        if get_value('Finish_Skill_Query_Selectable'):
            Custom_Unit_Finish_Skill_Query(card=card)
        if get_value('Dokkan_Field_Query_Selectable'):
            Custom_Unit_Dokkan_Field_Query(card=card)
        if get_value('Battle_Params_Query_Selectable'):
            Custom_Unit_Battle_Params_Information(card=card)
        if get_value('Category_Query_Selectable'):
            Card_Categories_Wiki(card=card)
            
    elif tag_id == f'Custom_Query_Execute_All_Button_{card}':
        Custom_Unit.execute_all = True
        # json_cards uses the loop range number to grab the correct json information, otherwise when you try to query
        # a second transformation unit there would be issues.
        Custom_Unit_Leader_Skill_Query(card=card)
        for i in range(len(Card_Checks.json_data)):
            card = Custom_Unit.card_number
            Custom_Card_Thumb_Display(card=card, json_cards=i)
            Custom_Unit_Card_Queries(card=card, json_cards=i)
            Custom_Unit_Passive_Skill_Query(card=card, json_cards=i)
            Custom_Unit_Specials_Query(card=card, json_cards=i)
            Custom_Unit_Active_Skill_Query(card=card, json_cards=i)
            Custom_Unit_Standby_Skill_Query(card=card, json_cards=i)
            Custom_Unit_Finish_Skill_Query(card=card, json_cards=i)
            Custom_Unit_Dokkan_Field_Query(card=card, json_cards=i)
            Custom_Unit_Battle_Params_Information(card=card, json_cards=i)
            Card_Categories_Wiki(card=card, json_cards=i)
            
            if i != len(Card_Checks.json_data) - 1:
                Main_Tab_Bar_Callback()
        card_id = data['card']['id']
        # url = f'https://dokkan.wiki/cards/{card_id}'
        # if RPC:
        #     RPC.update(
        #         state=None,
        #         details=get_value(Card.row_names[1] + '_Card_' + str(card) + '_Row_0'),
        #         large_image="zamasu_and_vegito",
        #         small_image="gold_small_image",
        #         start=time.time(),
        #         buttons=[{"label": "Wiki Link", "url": url}, {"label": "Discord", "url": "https://discord.gg/fGdxkZpUyz"}]
        #     )
    # Card_Checks.card_ids.clear()
    


########################################################################################################################################################################################################
def Transformation_Texture_Registry():
    i = Custom_Unit.card_number
    if not does_alias_exist(f'Placeholder_Image_Texture_{i}'):
        with texture_registry():
            width, height, channels, data = load_image('logo/Add_Image.png')
            add_dynamic_texture(width=250, height=250, default_value=data, tag=f'Placeholder_Image_Texture_{i}')
            ### Checking Element ID to change the border color
            # if Card_Checks.element_id[i] in (0, 10, 20):
                # print(f'Element: {Card_Checks.element_id[i]}')
            width, height, channels, data = load_image('logo/Custom_Border_Border_AGL.png')
            add_dynamic_texture(width=250, height=250, default_value=data, tag=f'Custom_Border_Thumb_Border_Texture_{i}')
            width, height, channels, data = load_image('logo/Custom_Border_Background_AGL.png')
            add_dynamic_texture(width=250, height=250, default_value=data, tag=f'Custom_Border_Thumb_Background_Texture_{i}')
            width, height, channels, data = load_image('logo/Placeholder.png')
            add_dynamic_texture(width=250, height=250, default_value=data, tag=f'Card_Thumb_Texture_{i}')
    # Widget_Aliases.tags_to_delete.append(f'Placeholder_Image_Texture_{i + 1}')
    # Widget_Aliases.tags_to_delete.append(f'Custom_Border_Thumb_Border_Texture_{i + 1}')
    # Widget_Aliases.tags_to_delete.append(f'Custom_Border_Thumb_Background_Texture_{i + 1}')
    # Widget_Aliases.tags_to_delete.append(f'Card_Thumb_Texture_{i + 1}')
        
######################################################################################################################################################################################################## 
def Custom_Unit_Create_Tabs(*, json_dict=None):
    Transformation_Texture_Registry()
    i = Custom_Unit.card_number
    label = f'Unit {i + 1}'
    if i == 0:
        Delete_Items(f'Main_Card_Tab_{i}')
        label = f'Unit 1'
    
    with tab(label=label, tag=f'Main_Card_Tab_{i}', parent='Main_Tab_Bar', before='Add_Card_Tab'):
        Widget_Aliases.tags_to_delete.append(f'Main_Card_Tab_{i}')
        bind_item_handler_registry(f'Main_Card_Tab_{i}', 'Tab_Handler')
        

        with tab_bar(label=f'Card {i}', tag=f'Card_Input_Tab_Bar_{i}'):
            Widget_Aliases.tags_to_delete.append(f'Card_Input_Tab_Bar_{i}')
            
            with tab(label=f'Card Input', tag=f'Card_Input_Tab_{i}'):
                Widget_Aliases.tags_to_delete.append(f'Card_Input_Tab_{i}')
                add_text(default_value='',tag=f'Card_Name_Display_{i}', color=(255, 215, 0), parent=f'Card_Input_Tab_{i}')
                Widget_Aliases.tags_to_delete.append(f'Card_Name_Display_{i}')
                bind_item_font(f'Card_Name_Display_{i}', 'Arial_Bold_Font')
                with group(tag=f'Card_Input_Image_Widget_Group_{i}', horizontal=True, parent=f'Card_Input_Tab_{i}'):
                    add_image(f'Placeholder_Image_Texture_{i}', tag=f'Placeholder_Image_{i}')
                    add_image(f'Custom_Border_Thumb_Background_Texture_{i}', tag=f'Custom_Border_Thumb_Background_{i}', show=False)
                    add_image(f'Card_Thumb_Texture_{i}', tag=f'card_thumb_display_{i}', show=False)
                    add_image(f'Custom_Border_Thumb_Border_Texture_{i}', tag=f'Custom_Border_Thumb_Border_{i}', show=False)
                    
                    # add_spacer(width=10)
                    ### Custom Execute Button
                    Custom_Unit_Selectables(card=i)
                    Delete_Items(f'Custom_Query_Widget_Group_{i}')
                    with group(horizontal=False, tag=f'Custom_Query_Widget_Group_{i}'):
                        add_input_text(tag=f'Custom_Query_Text_Input_{i}', width=90, callback=get_card_id)
                        add_button(label='Custom Query', tag=f'Custom_Query_Button_{i}', callback=Custom_Query_Window)
                        
                    
                    # For the first tab only
                    if i == 0:
                        # with group(horizontal=False):
                            # add_input_text(callback=get_card_id, tag='Card ID', hint='Card ID', width=95)
                            # bind_item_font('Card ID', 'Arial_font')
                            # add_button(label='Execute Query', callback=save_callback, tag='Execute_Query')
                            # bind_item_font('Execute_Query', 'Arial_font') 

                        with group(horizontal=True):
                            with group(horizontal=False):
                                with group(horizontal=True):
                                    add_input_text(hint='SQL name', tag='Filename', width=95)
                                    bind_item_font('Filename', 'Arial_font')
                                    add_input_text(hint='Card ID', tag='Card_ID_Lua', width=95)
                                    bind_item_font('Card_ID_Lua', 'Arial_font')

                                with group(horizontal=True):
                                    add_button(label='Export as SQL', callback=Export_as_SQL, tag='Export as SQL button')
                                    bind_item_font('Export as SQL button', 'Arial_font') 

                                    add_button(label='Download Luas', callback=Lua_Downloader, tag='Download_Luas')
                                    bind_item_font('Download_Luas', 'Arial_font')
                        
                    with group(horizontal=True, tag=f'Custom_Unit_Checkbox_Group_Horizontal_True_{i}'):
                        pass
                        with group(horizontal=False, tag=f'Custom_Unit_Checkbox_Group_Horizontal_False_{i}'):
                            pass
                add_text(tag=f'log_{i + 1}', default_value='')
                        # add_checkbox(label='Custom Unit', callback=Custom_Unit_Checkbox, tag=f'Custom_Unit_{i}')
                        # bind_item_font(f'Custom_Unit_{i}', 'Arial_Font')
                    # add_input_text(tag=f'Card ID{i}', width=95, default_value=Card_Checks.card_ids[0], parent=f'Card_Input_Image_Widget_Group_{i}')
                    # Widget_Aliases.tags_to_delete.append(f'Card ID{i}')
                    # Widget_Aliases.tags_to_delete.append(f'Card_Input_Image_Widget_Group_{i}')
                # Widget_Aliases.tags_to_delete.append(f'Placeholder_Image_{i}')
                # Widget_Aliases.tags_to_delete.append(f'Custom_Border_Thumb_Background_{i}')
                # Widget_Aliases.tags_to_delete.append(f'card_thumb_display_{i}')
                # Widget_Aliases.tags_to_delete.append(f'Custom_Border_Thumb_Border_{i}')
                add_separator()
                    

            with tab(label=f'Specials', tag=f'Specials_Tab_Card_{i}'):
                pass
            
            with tab(label=f'Leader Skill', tag=f'Leader_Skill_{i}', show=False):
                pass
            
            with tab(label=f'Active Skill', tag=f'Active_Skill_Card_{i}', show=False):
                pass

            with tab(label=f'Standby Skill', tag=f'Standby_Skill_{i}', show=False):
                pass
            
            with tab(label=f'Finish Skill', tag=f'Finish_Skill_{i}', show=False):
                pass
                
            with tab(label='Dokkan Field', tag=f'Dokkan_Field_{i}', show=False):
                pass
                
            with tab(label='Battle Params', tag=f'Battle_Params_{i}', show=False):
                pass
            
            with tab(label='Categories', tag=f'Categories_{i}', show=True):
                Card_Categories_Window(card=i)
                pass
            
            with tab(label='Effect Packs', tag=f'Effect_Packs_{i}', show=False):
                pass
            
            with tab(label='Special Views', tag=f'Special_Views_{i}', show=False):
                pass
            
            if json_dict:
                if json_dict[f'Card {i + 1}']['Leader Skill']:
                    configure_item(f'Leader_Skill_{i}', show=True)
                    set_value(f'Custom_Unit_Leader_Skill_Checkbox_{i}', True)

########################################################################################################################################################################################################       

        
    
########################################################################################################################################################################################################
def Thumb_Test(tag_id):
    card = Table_ID(tag_id)
    try:
        file_path = easygui.fileopenbox('Select a thumb image to add', 'Add Thumb Image', filetypes=["*.png"])
        width, height, channels, thumb_data = load_image(file_path)
        set_value(f'Card_Thumb_Texture_{card}', thumb_data)
        # if card == 0:
        configure_item(f'card_thumb_display_{card}', show=True)
        configure_item(f'Placeholder_Image_{card}', show=False)
        
        if width != 250 or height != 250:
            set_value('log_1', 'If you are seeing this and there is a pixelated image, you didn\'t open a 250x250 image')
        
        thumb_name = os.path.basename(file_path)

        dest_dir = os.path.join('thumbs', 'thumb')
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, thumb_name)
        if not os.path.exists(dest_path):
            shutil.copy2(file_path, dest_path)


        if thumb_name not in Custom_Unit.card_thumb_dict:
            Custom_Unit.card_thumb_dict[int(card)] = thumb_name

        
            
    except Exception as e:
        set_value(f'Add_Image_Placeholder_{card}', False)
        if does_alias_exist('log_1'):
            set_value('log_1', 'Image not selected, please try again!')
        
    
    print(Custom_Unit.card_thumb_dict)
    set_value(tag_id, False)
########################################################################################################################################################################################################
def Custom_Card_Thumb_Display(*, card=int, json_dict=None, json_cards=0):
    card = card
    if json_dict:
        card_id_0_assets = json_dict[f'Card {card + 1}']['Card Thumb']
        width, height, channels, thumb_data = load_image(f'assets/character/thumb/{card_id_0_assets}')
        Custom_Unit.card_thumb_dict[int(card)] = card_id_0_assets
        set_value(f'Card_Name_Display_{card}', json_dict[f'Card {card + 1}']['Card']['Name'])
        configure_item(f'Card_Name_Display_{card}', show=True)
    else:
        card_id_assets = str(Card_Checks.card_ids[json_cards])
        card_id_0_assets = str(card_id_assets[:-1]) + '0'
        print(card_id_0_assets)

        # width, height, channels, thumb_data = read_png_from_zip(card_id_0_assets)
        width, height, channels, thumb_data = load_image(f'thumbs/thumb/card_{card_id_0_assets}_thumb.png')
        Custom_Unit.card_thumb_dict[int(card)] = f'card_{card_id_0_assets}_thumb.png'
        set_value(f'Card_Name_Display_{card}', Card_Checks.card_names[json_cards])
        configure_item(f'Card_Name_Display_{card}', show=True)
        configure_item(f'Main_Card_Tab_{card}', label=Card_Checks.card_names[json_cards])
        
    
    
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
            
        x, y = get_item_pos(f'Placeholder_Image_{card}')
        set_value(f'Card_Thumb_Texture_{card}', thumb_data)
        set_value(f'Custom_Border_Thumb_Border_Texture_{card}', border_data)
        set_value(f'Custom_Border_Thumb_Background_Texture_{card}', bg_data)
        configure_item(f'card_thumb_display_{card}', show=True)
        configure_item(f'Custom_Border_Thumb_Background_{card}', pos=[8,110], show=True)
        configure_item(f'card_thumb_display_{card}', pos=[8,110], show=True)
        configure_item(f'Custom_Border_Thumb_Border_{card}', pos=[8,110], show=True)
        
        if os.path.exists(f'assets/character/thumb/card_{Card_Checks.card_ids[json_cards]}_thumb.png'):
            width, height, channels, thumb_data = load_image(f'assets/character/thumb/card_{Card_Checks.card_ids[json_cards]}_thumb.png')
        else:
            Card_ID_Asset = str(Card_Checks.card_ids[json_cards])
            Card_ID_Asset = Card_ID_Asset[:-1] + '0'
            # url = f'https://dokkaninfo.com/assets/japan/character/thumb/card_{Card_ID_Asset}_thumb.png'
            # download_image('assets/character/thumb/', url, f'card_{Card_ID_Asset}_thumb.png')
            width, height, channels, thumb_data = load_image(f'thumbs/thumb/card_{Card_ID_Asset}_thumb.png')
    with texture_registry():
        Delete_Items(f'Custom_Border_Thumb_Border_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
        Delete_Items(f'Custom_Border_Thumb_Background_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
        width, height, channels, border_data = load_image(f'logo/Custom_Border_Border_{Card_Checks.element_ids[Card_Checks.element_id[0]]}.png')
        add_dynamic_texture(width=250, height=250, default_value=border_data, tag=f'Custom_Border_Thumb_Border_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
        width, height, channels, bg_data = load_image(f'logo/Custom_Border_Background_{Card_Checks.element_ids[Card_Checks.element_id[0]]}.png')
        add_dynamic_texture(width=250, height=250, default_value=bg_data, tag=f'Custom_Border_Thumb_Background_Texture_{Card_Checks.element_ids[Card_Checks.element_id[0]]}')
                
            # set_value('Custom_Border_Thumb_Border_0', f'Custom_Border_Thumb_Border_Texture_{Card_Checks.element_ids[Card_Checks.element_id[i]]}')
            # set_value('Custom_Border_Thumb_Background_0', f'Custom_Border_Thumb_Background_Texture_{Card_Checks.element_ids[Card_Checks.element_id[i]]}')
                
        # Just grab this 'Placeholder_Image_0' to get the same position, don't know why I was trying to grab the other ones when I can just use this one.
        # This image shit was coded pretty poorly by me, may have to recode it later, hopefully not.
        x, y = get_item_pos(f'Placeholder_Image_{card}')
        set_value(f'Card_Thumb_Texture_{card}', thumb_data)
        set_value(f'Custom_Border_Thumb_Border_Texture_{card}', border_data)
        set_value(f'Custom_Border_Thumb_Background_Texture_{card}', bg_data)
        configure_item(f'card_thumb_display_{card}', show=True)
        configure_item(f'Custom_Border_Thumb_Background_{card}', pos=[8,110], show=True)
        configure_item(f'card_thumb_display_{card}', pos=[8,110], show=True)
        configure_item(f'Custom_Border_Thumb_Border_{card}', pos=[8,110], show=True)
    # add_image('Placeholder_Image_Texture_0', tag='Placeholder_Image_0')
    # add_image('Custom_Border_Thumb_Background_Texture_0', tag='Custom_Border_Thumb_Background_0', show=False)
    # add_image('Card_Thumb_Texture_0', tag='card_thumb_display_0', show=False)
    # add_image('Custom_Border_Thumb_Border_Texture_0', tag='Custom_Border_Thumb_Border_0', show=False)
    
########################################################################################################################################################################################################
def Custom_Unit_Card_Thumb_Display():
    card = Custom_Unit.card_number
    
    width, height, channels, thumb_data = load_image(f'logo/Add_Image.png')
    # add_button(tag=f'Add_Image_Placeholder_{card}', height=250, width=250, parent=f'Card_Input_Tab_{card}', pos=get_item_pos('Placeholder_Image_0'), callback=Thumb_Test)
    # with group(tag='Image_Placeholder_Group', horizontal=True, parent=f'Card_Input_Tab_{card}'):
    add_selectable(tag=f'Add_Image_Placeholder_{card}', height=250, width=250, parent=f'Card_Input_Tab_{card}', pos=[8,110], callback=Thumb_Test)
        
    bind_item_theme(f'Add_Image_Placeholder_{card}','Selectable_Theme')
    Widget_Aliases.tags_to_delete.append(f'Add_Image_Placeholder_{card}')
    Widget_Aliases.tags_to_delete.append(f'Custom_Query_Button_{card}')
    
    
    # width, height, channels, thumb_data = load_image(f'assets/character/thumb/{card_id_0_assets}')
    ### Appending just the card ID to this for the sake of units loaded from a JSON being saved again. Otherwise an error will occur as I use Card_Checks.card_ids for saving a queried unit.
    # numbers_only = re.sub(r'\D', '', card_id_0_assets)
    # if 'AGL' in element_type:
    #     element_type = 'AGL'
    # elif 'TEQ' in element_type:
    #     element_type = 'TEQ'
    # elif 'INT' in element_type:
    #     element_type = 'INT'
    # elif 'PHY' in element_type:
    #     element_type = 'PHY'
    # else:
    #     element_type = 'STR'
        
    # if i == 0:
        # width, height, channels, thumb_data = load_image(f'assets/character/thumb/{card_id_0_assets}')
    # else:
    # if os.path.exists(f'assets/character/thumb/{card_id_0_assets}'):
    #     width, height, channels, thumb_data = load_image(f'assets/character/thumb/{card_id_0_assets}')
    # else:
    #     url = f'https://dokkaninfo.com/assets/japan/character/thumb/{card_id_0_assets}'
    #     download_image('assets/character/thumb/', url, f'{card_id_0_assets}')
    #     width, height, channels, thumb_data = load_image(f'assets/character/thumb/{card_id_0_assets}')
    # with texture_registry():
    #     Delete_Items(f'Custom_Border_Thumb_Border_Texture_{element_type}')
    #     Delete_Items(f'Custom_Border_Thumb_Background_Texture_{element_type}')
    #     width, height, channels, border_data = load_image(f'logo/Custom_Border_Border_{element_type}.png')
    #     add_dynamic_texture(width=250, height=250, default_value=border_data, tag=f'Custom_Border_Thumb_Border_Texture_{element_type}')
    #     width, height, channels, bg_data = load_image(f'logo/Custom_Border_Background_{element_type}.png')
    #     add_dynamic_texture(width=250, height=250, default_value=bg_data, tag=f'Custom_Border_Thumb_Background_Texture_{element_type}')
            
    # Just grab this 'Placeholder_Image_0' to get the same position, don't know why I was trying to grab the other ones when I can just use this one.
    # This image shit was coded pretty poorly by me, may have to recode it later, hopefully not.
    # x, y = get_item_pos('Placeholder_Image_0')
    # set_value(f'Card_Thumb_Texture_{card}', thumb_data)
    # set_value(f'Custom_Border_Thumb_Border_Texture_{card}', border_data)
    # set_value(f'Custom_Border_Thumb_Background_Texture_{card}', bg_data)
    # configure_item(f'card_thumb_display_{card}', show=True)
    # configure_item(f'card_thumb_display_{card}', pos=get_item_pos('Placeholder_Image_0'))
    # configure_item(f'Custom_Border_Thumb_Background_{card}', pos=get_item_pos('Placeholder_Image_0'), show=True)
    # configure_item(f'card_thumb_display_{card}', pos=get_item_pos('Placeholder_Image_0'), show=True)
    # configure_item(f'Custom_Border_Thumb_Border_{card}', pos=get_item_pos('Placeholder_Image_0'), show=True)
    
########################################################################################################################################################################################################

    
########################################################################################################################################################################################################

def Card_Widgets():
    card_num = Custom_Unit.card_number
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
    
    with group(horizontal=True, tag=f'Card_Information_Text_Group_{card_num}', parent=f'Card_Input_Tab_{card_num}'):
        add_text('Card Information', color=(255,50,50), parent='Card_Information_Text_Group', tag=f'Card_Information_Text_{card_num}')
        add_checkbox(label='EZA', default_value=False, tag=f'EZA_Checkbox_{card_num}', callback=EZA_Callback, parent='Card_Information_Text_Group')
        add_checkbox(label='Super EZA', default_value=False, tag=f'Super_EZA_Checkbox_{card_num}', callback=Super_EZA_Callback, parent='Card_Information_Text_Group')
    Widget_Aliases.tags_to_delete.append(f'Card_Information_Text_{card_num}')
    Widget_Aliases.tags_to_delete.append(f'EZA_Checkbox_{card_num}')
    Widget_Aliases.tags_to_delete.append(f'Card_Information_Text_Group_{card_num}')

        ## 5 Rarity, 12 Element, 23,24,25,26,27,28,29 Link Skills, 52 Potential Board
    sss = Table_Combo_Inputs(table_name=f'Card{card_num}_Table', row_name=f'Card{card_num}_Table_Row', class_name=Card,
                 table_parent=f'Card_Input_Tab_{card_num}', table_height=83, table_width=1650,
                 row_width=85, transformation_card_num=card_num, combo_columns=[5,12,23,24,25,26,27,28,29,52], 
                 callback_columns=[1, 5, 12, 23, 24, 25, 26, 27, 28, 29, 52], callback={1 : Name_Change_Callback, 5 : Rarity_Callback, 12 : Element_Callback, 23 : Synced_Callback, 24 : Synced_Callback, 25 : Synced_Callback, 26 : Synced_Callback, 27 : Synced_Callback, 28 : Synced_Callback, 29 : Synced_Callback, 52 : Synced_Callback}, combo_list=combos)
    
########################################################################################################################################################################################################
def Custom_Unit_Card_Queries(*, card=int, json_cards=0):
    card_num = card
    rarity = {'0' : '(N)', '1' : '(R)', '2' : '(SR)', '3' : '(SSR)', '4' : '(TUR)', '5' : '(LR)'}
    element = {'0' : 'AGL', '10' : 'Super AGL', '20' : 'Extreme AGL', '1' : 'TEQ', '11' : 'Super TEQ', '21' : 'Extreme TEQ', '2' : 'INT', '12' : 'Super INT', '22' : 'Extreme INT', '3' : 'STR', '13' : 'Super STR', '23' : 'Extreme STR', '4' : 'PHY', '14' : 'Super PHY', '24' : 'Extreme PHY'}
    
    print('Card Query')

    for i in range(2):
        data = Card_Checks.json_data[json_cards]['card']

        # Use Base Card data for first row
        if i == 0:
            card0 = str(int(Card_Checks.json_data[json_cards]['card']['id']) - 1)
            data = read_json_from_zip(card0)['card']
            # data['id'] = str(int(data['id']) - 1)
        # print(data)
        for row_names in Card.row_names:
            print(row_names)
            print(row_names + '_Card_' + str(card_num) + '_Row_' + str(i))
            # Time for some shitty checks

            if data[row_names] == "":
                print('NULL')
                set_value(f'{row_names}_Card_{card_num}_Row_{i}', 'NULL')

            elif row_names == "rarity":
                set_value(f'{row_names}_Card_{card_num}_Row_{i}', rarity[data[row_names]])

            elif row_names == "element":
                set_value(f'{row_names}_Card_{card_num}_Row_{i}', element[data[row_names]])

            elif row_names in ["link_skill1_id", "link_skill2_id", "link_skill3_id", "link_skill4_id", "link_skill5_id", "link_skill6_id", "link_skill7_id"]:
                set_value(f'{row_names}_Card_{card_num}_Row_{i}', str(data[row_names]) + ': ' + str(Card_Table_Combos.link_skill_dict[int(data[row_names])]))
                # print(Card_Table_Combos.link_skill_dict[data[row_names]])

            else:
                set_value(f'{row_names}_Card_{card_num}_Row_{i}', data[row_names])

    
    # configure_item(f'Main_Card_Tab_{card}', label=Card_Checks.card_names[0][0])
        
    # Delete_Items(f'Card_Separator_{card_num}')            
    # add_separator(tag=f'Card_Separator_{card_num}', parent=f'Card_Input_Tab_{card_num}')
    Widget_Aliases.tags_to_delete.append(f'Card_Separator_{card_num}')

########################################################################################################################################################################################################       
def Passive_Widgets():
    cards = Custom_Unit.card_number
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
             class_name=Passive_Skill, combo=True, combo_tag=Passive_Skill.row_names[2], combo_list=Efficacy_Values.combo_list, combo_column_name=Passive_Skill.column_names[2],
             table_width=1775, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=cards)
    
    
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
    
########################################################################################################################################################################################################
def Custom_Unit_Passive_Skill_Query(*, card=int, json_cards=0):
    card_id = grab_card_id()

    if not Card_Checks.json_data[json_cards]:
        data = read_json_from_zip(card_id)
    else:
        data = Card_Checks.json_data[json_cards]

    passive_name = data['passive_skill']['name']
    passive_desc = data['passive_skill']['itemized_description']
    passive_skills = data['passive_skill']['skills']
    

    if passive_name:

        Passive_Skill.rows = len(passive_skills)
        sss = Table_Inputs(table_name=f'Passive_Skill_Table_{card}', row_name=f'Passive_Skill_Table_Row_{card}', table_parent=f'Card_Input_Tab_{card}', use_child_window=False,
                class_name=Passive_Skill, combo=True, combo_tag=Passive_Skill.row_names[2], combo_list=Efficacy_Values.combo_list, combo_column_name=Passive_Skill.column_names[2],
                table_width=1775, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=card, table_before=f'Passive_Desc_Text_{card}')
        
        print(sss)

        set_item_height(f'Passive_Skill_Table_{card}', 24 * Passive_Skill.rows + 23)
        # set_item_height(f'Passive_Skill_Table_{card}', 47)
        set_value(f'Passive_Desc_Text_Input_{card}', passive_desc)

        for row, skill in enumerate(passive_skills):
            print(skill)
            set_value(f'Passive_name_Card_{card}_Row_{row}', passive_name)
            for key, value in skill.items():
                # print('Passive_' + key + '_Card_' + str(card) + '_Row_' + str(row))

                if value == '' and key != 'efficacy_values':
                    set_value('Passive_' + key + '_Card_' + str(card) + '_Row_' + str(row), 'NULL')
                    # Text_Resize('Passive_' + key + '_Card_' + str(card) + '_Row_' + str(row))

                elif key == 'efficacy_type':
                    set_value('Passive_' + key + '_Card_' + str(card) + '_Row_' + str(row), Efficacy_Values.eff_dict[int(value)])
                    # Text_Resize('Passive_' + key + '_Card_' + str(card) + '_Row_' + str(row))

                else:
                    set_value('Passive_' + key + '_Card_' + str(card) + '_Row_' + str(row), value)
                    # Text_Resize('Passive_' + key + '_Card_' + str(card) + '_Row_' + str(row))


        configure_item(f'Passive_Rows_in_Table_{card}', default_value=f'Rows: {len(passive_skills)}')
        
        widget_widths_list = []
        for row in range(Passive_Skill.rows):
            widget_widths = 0
            for column in range(len(Passive_Skill.row_names)):
                widget_widths += get_item_width(Passive_Skill.row_names[column] + '_Card_' + str(card) + '_Row_' + str(row))
            widget_widths_list.append(widget_widths)
        
        
        # Finding the max width out of all widgets
        max_width = 0
        for width in widget_widths_list:
            max_width = width
            if width > max_width:
                max_width = width


        # print(max_width)
        set_item_width(f'Passive_Skill_Table_{card}', max_width + 140)
        
        Resize_Table_Width(card, Passive_Skill, Passive_Skill.rows, f'Passive_Skill_Table_{card}')

########################################################################################################################################################################################################             
def Specials_Widgets():
    cards = Custom_Unit.card_number
    
    with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Button_Add_Group_Card_{cards}'):
        add_button(label='Add Super', tag=f'Specials_Button_Add_Card_{cards}', callback=Specials_Add, parent=f'Specials_Button_Add_Group_Card_{cards}')
        add_button(label='Del Super', tag=f'Specials_Button_Del_Card_{cards}', callback=Specials_Del, parent=f'Specials_Button_Add_Group_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Add_Group_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Add_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Del_Card_{cards}')

    for i in range(1):
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

        with group(tag=f'Card_Specials_Text_Group_Card_{cards}_{i}', parent=f'Specials_Tab_Card_{cards}', horizontal=True):
            add_text('Card Specials', color=(255,50,50), parent=f'Card_Specials_Text_Group_Card_{cards}_{i}', tag=f'Card_Specials_Text_Card_{cards}_{i}')
            add_checkbox(label='Ex Super', default_value=False, tag=f'Ex_Super_Checkbox_Card_{cards}_{i}', callback=Ex_Super_Callback, parent=f'Card_Specials_Text_Group_Card_{cards}_{i}')
            add_combo(['When Super', 'When Additional', 'When Crit'], tag=f'Ex_Super_Combo_Card_{cards}_{i}', callback=Ex_Super_Combo_Callback,parent=f'Card_Specials_Text_Group_Card_{cards}_{i}', default_value='When Super', show=False, width=120)
            add_combo(['10','20','30','40','50', '60', '70', '80', '90', '100'], tag=f'Ex_Super_Combo2_Card_{cards}_{i}', callback=Ex_Super_Combo_Callback,parent=f'Card_Specials_Text_Group_Card_{cards}_{i}', default_value='60', show=False, width=50)
            add_input_text(tag=f'Card_Specials_BGM_Text_Card_{cards}_{i}', width=50, callback=Ex_Super_Combo_Callback, default_value='69', show=False, parent=f'Card_Specials_Text_Group_Card_{cards}_{i}')
            Widget_Aliases.tags_to_delete.append(f'Card_Specials_Text_Card_{cards}_{i}')
            
        Card_Specials.rows = 2
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
        Widget_Aliases.tags_to_delete.append(f'Ex_Super_Checkbox_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Ex_Super_Combo_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Card_Specials_Text_Group_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Ex_Super_Combo2_Card_{cards}_{i}')
        Widget_Aliases.tags_to_delete.append(f'Card_Specials_BGM_Text_Card_{cards}_{i}')
            
        Specials.rows = 1
        with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Table_Group_Card_{cards}_{i}'):
            Specials_tags = Table_Inputs(table_name=f'Specials_Card_{cards}_{i}', row_name=f'Specials_Table_Row_Card_{cards}_{i}', class_name=Specials,
                         used_in_loop=True, loop_number=i, use_child_window=True, child_parent=f'Specials_Table_Group_Card_{cards}_{i}', child_tag=f'Specials_Child_Window_Card_{cards}_{i}',
                         table_height=90, table_width=1134, child_height=87, child_width=1139, combo=True, combo_tag=Specials.row_names[1], combo_list=Efficacy_Values.combo_list,
                         transformation=True, transformation_card_num=cards, child_before=f'Specials_Group_Card_{cards}_{i}')
                
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
        ### Had to placed down here as it was interrupting the group f'Specials_Group_Card_{cards}_{i}' 
        
        add_separator(parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Separator_Card_{cards}_{i}')
        
        Widget_Aliases.tags_to_delete.append(f'Specials_Separator_Card_{cards}_{i}')
        
########################################################################################################################################################################################################

def Custom_Unit_Specials_Query(*, card=int, json_cards=0):
    cards = card
#
    if not Card_Checks.json_data[json_cards]:
        data = read_json_from_zip(card_id)
    else:
        data = Card_Checks.json_data[json_cards]

    card_id_1 = grab_card_id()
    cardID0 = str(card_id_1[:-1]) + '0'

    # Card_Checks.special_set_ids is a list of special set id lists Ex. [[XX, XX], [XX], [X, XX, X]]
    special_sets = data['special_sets']
    specials = data['specials']
    card_specials = data['card_specials']
    card_specials_base_card = read_json_from_zip(cardID0)['card_specials']
    special_set_ids = [key for key in data['special_sets']]
    card_special_ids = [key for key in data['card_specials']]
    card_specials_base_card_ids = [key for key in card_specials_base_card]
    num_of_special_sets = len(special_sets)








    Card_Specials.skill_rows.clear()
    Special_Set.skill_rows.clear()
    Specials.skill_rows.clear()

    Delete_Items([f'Specials_Button_Add_Group_Card_{cards}', f'Specials_Button_Add_Card_{cards}', f'Specials_Button_Del_Card_{cards}'])

    with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Button_Add_Group_Card_{cards}'):
        add_button(label='Add Super', tag=f'Specials_Button_Add_Card_{cards}', callback=Specials_Add, parent=f'Specials_Button_Add_Group_Card_{cards}')
        add_button(label='Del Super', tag=f'Specials_Button_Del_Card_{cards}', callback=Specials_Del, parent=f'Specials_Button_Add_Group_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Add_Group_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Add_Card_{cards}')
        Widget_Aliases.tags_to_delete.append(f'Specials_Button_Del_Card_{cards}')

    for i in range(num_of_special_sets):


        # Only setting the Specials rows to a different value as Card_Specials and Special_Set will always be the same num of rows.
        Specials.rows = len(specials[special_set_ids[i]])

        rows_to_check = [f'Special#_Text_Card_{cards}_{i}',f'Special_Name_Text_Card_{cards}_{i}',f'Special_Set_Name_Input_Card_{cards}_{i}',f'Special_Aim_Target_Text_Card_{cards}_{i}',f'Special_Set_Aim_Target_Input_Card_{cards}_{i}',f'Special_Desc_Text_Card_{cards}_{i}',f'Special_Set_Desc_Input_Card_{cards}_{i}',f'Special_Increase_Rate_Text_Card_{cards}_{i}',
                     f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}',f'Special_Cond_Text_Card_{cards}_{i}',f'Special_Set_Cond_Input_Card_{cards}_{i}',f'Special_Level_Bonus_Text_Card_{cards}_{i}',f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}',f'Card_Specials_Text_Card_{cards}_{i}',f'Special_Skills_Text_Card_{cards}_{i}',f'Specials_Separator_Card_{cards}_{i}',
                     f'Special_Set_Group_Card_{cards}_1_{i}', f'Special_Set_Group_Card_{cards}_2_{i}', f'Special_Set_Group_Card_{cards}_3_{i}', f'Specials_Table_Group_Card_{cards}_{i}', f'Specials_Aim_Target_Group_Card_{cards}_{i}',
                     f'Special_Aim_Target_Text_Card_{cards}_{i}',f'Special_Set_Aim_Target_Input_Card_{cards}_{i}',f'Specials_Increase_Rate_Group_Card_{cards}_{i}',f'Special_Increase_Rate_Text_Card_{cards}_{i}',
                     f'Special_Set_Increase_Rate_Input_Card_{cards}_{i}', f'Specials_Level_Bonus_Group_Card_{cards}_{i}', f'Special_Level_Bonus_Text_Card_{cards}_{i}', f'Special_Set_Level_Bonus_Input_Card_{cards}_{i}',
                     f'Specials_Button_Separtor_Card_{cards}_{i}', f'Special_Skills_Button_Group_Card_{cards}_{i}', f'Special_Skills_Text_Card_{cards}_{i}',
                     f'Ex_Super_Checkbox_Card_{cards}_{i}', f'Ex_Super_Combo_Card_{cards}_{i}', f'Card_Specials_Text_Group_Card_{cards}_{i}', f'Ex_Super_Combo2_Card_{cards}_{i}',
                     f'Card_Specials_BGM_Text_Card_{cards}_{i}']

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


        with group(tag=f'Card_Specials_Text_Group_Card_{cards}_{i}', parent=f'Specials_Tab_Card_{cards}', horizontal=True):
            add_text('Card Specials', color=(255,50,50), parent=f'Card_Specials_Text_Group_Card_{cards}_{i}', tag=f'Card_Specials_Text_Card_{cards}_{i}')
            add_checkbox(label='Ex Super', default_value=False, tag=f'Ex_Super_Checkbox_Card_{cards}_{i}', callback=Ex_Super_Callback, parent=f'Card_Specials_Text_Group_Card_{cards}_{i}')
            add_combo(['When Super', 'When Additional', 'When Crit'], tag=f'Ex_Super_Combo_Card_{cards}_{i}', callback=Ex_Super_Combo_Callback,parent=f'Card_Specials_Text_Group_Card_{cards}_{i}', default_value='When Super', show=False, width=125)
            add_combo(['10','20','30','40','50', '60', '70', '80', '90', '100'], tag=f'Ex_Super_Combo2_Card_{cards}_{i}', callback=Ex_Super_Combo_Callback,parent=f'Card_Specials_Text_Group_Card_{cards}_{i}', default_value='60', show=False, width=70)
            add_input_text(tag=f'Card_Specials_BGM_Text_Card_{cards}_{i}', width=50, callback=Ex_Super_Combo_Callback, default_value='69', show=False, parent=f'Card_Specials_Text_Group_Card_{cards}_{i}')

        Widget_Aliases.tags_to_delete.append(f'Card_Specials_Text_Card_{cards}_{i}')
        CS_tags = Table_Inputs(table_name=f'Card_Specials_Card_{cards}_{i}', row_name=f'Card_Specials_Table_Row_Card_{cards}_{i}', class_name=Card_Specials,
                             used_in_loop=True, loop_number=i, use_child_window=False, table_parent=f'Specials_Tab_Card_{cards}', table_height=67, table_width=1150,
                             row_width=75, table_policy=mvTable_SizingStretchSame, transformation=True, transformation_card_num=cards)

        set_item_height(f'Card_Specials_Card_{cards}_{i}', (24 * len(card_specials) * 2) + 23)

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

        with group(horizontal=True, parent=f'Specials_Tab_Card_{cards}', tag=f'Specials_Table_Group_Card_{cards}_{i}'):
            Specials_tags = Table_Inputs(table_name=f'Specials_Card_{cards}_{i}', row_name=f'Specials_Table_Row_Card_{cards}_{i}', class_name=Specials,
                                     used_in_loop=True, loop_number=i, use_child_window=True, child_parent=f'Specials_Table_Group_Card_{cards}_{i}', child_tag=f'Specials_Child_Window_Card_{cards}_{i}',
                                     table_height=90, table_width=1134, child_height=87, child_width=1139, combo=True, combo_tag=Specials.row_names[1], combo_list=Efficacy_Values.combo_list,
                                     transformation=True, transformation_card_num=cards)
            # print(Specials_tags)

            set_item_height(f'Specials_Card_{cards}_{i}', (24 * len(specials[special_set_ids[i]])) + 23)
            set_item_height(f'Specials_Child_Window_Card_{cards}_{i}', (25 * len(specials[special_set_ids[i]])) + 38)

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
        if specials[special_set_ids[i]]:
            if not len(specials[special_set_ids[i]]):
                for row_names in range(len(Specials.row_names)):
                    set_value(Specials.row_names[row_names] + '_Card_' + str(cards) + '_Row_' + str(i) + '0', 'NULL')

            for tag in range(len(specials[special_set_ids[i]])):
                list_of_special_skills = specials[special_set_ids[i]]

                # print(list_of_special_skills)
                for key, value in list_of_special_skills[tag].items():
                    if f'Specials_{key}' in Specials.row_names:
                        # print(f'Specials_{key}')
                        # print(key, value)

                        if value == '':
                            set_value(f'Specials_{key}' + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), 'NULL')
                        elif f'Specials_{key}' == Specials.row_names[1]:
                                # print(eff_dict[Passive_Skill.query_values[i][z]])
                                set_value(f'Specials_{key}' + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), Efficacy_Values.eff_dict[int(value)])
                                # Text_Resize(Specials.row_names[row_names] + str(i) + str(tag))
                        else:
                            # print(Specials.row_names[row_names] + str(cards) + str(i) + str(tag))
                            set_value(f'Specials_{key}' + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), value)
        # Card Specials
        ########################################################################################################
        # FIXME: Fix this garbage, it needs to properly grab the correct card specials for both base card and main card.
        for tag in range(2):
            base_card_specials = card_specials_base_card[card_specials_base_card_ids[i]]
            main_card_specials = card_specials[card_special_ids[i]]

            # print(f"skill {i} - tag {tag}")
            # print(base_card_specials)
            temp_dict = {0 : base_card_specials, 1 : main_card_specials}


            # print(base_card_specials)

            # for key, value in card_specials_base_card[card_specials_base_card_ids[tag]].items():
            #     # print(Card_Specials.row_names[row_names] + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag))
            #     if f'CS_{key}' in Card_Specials.row_names:
            #         if value == '':
            #             set_value(f'CS_{key}' + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), 'NULL')
            #         else:
            #             set_value(f'CS_{key}' + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), value)

            for key, value in card_specials[card_special_ids[i]].items():
                # print(Card_Specials.row_names[row_names] + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag))
                if tag == 0:
                    if f'CS_{key}' in Card_Specials.row_names:
                        if value == '':
                            set_value(f'CS_{key}' + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), 'NULL')
                        elif key == 'view_id':
                            set_value(f'CS_{key}' + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), str(int(value) - 1))
                        else:
                            set_value(f'CS_{key}' + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), value)
                else:
                    if f'CS_{key}' in Card_Specials.row_names:
                        if value == '':
                            set_value(f'CS_{key}' + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), 'NULL')
                        else:
                            set_value(f'CS_{key}' + '_Card_' + str(cards) + '_Row_' + str(i) + str(tag), value)

        # Special_Sets
        ########################################################################################################
        set = special_sets[special_set_ids[i]][0]
        set_value(f'Special_Set_Name_Input_Card_{cards}_{i}', set['name'].replace('\n', ''))
        Text_Resize(f'Special_Set_Name_Input_Card_{cards}_{i}')
        set_value(f'Special_Set_Desc_Input_Card_{cards}_{i}', set['description'].replace('\n', ''))
        Text_Resize(f'Special_Set_Desc_Input_Card_{cards}_{i}')

        if not set['causality_description']:
            set_value(f'Special_Set_Cond_Input_Card_{cards}_{i}', 'NULL')
            Text_Resize(f'Special_Set_Cond_Input_Card_{cards}_{i}')
        #
        # # If the list index is empty
        # elif not Card_Checks.special_set_conditions[0][i]:
        #     set_value(f'Special_Set_Cond_Input_Card_{cards}_{i}', 'NULL')
        #     Text_Resize(f'Special_Set_Cond_Input_Card_{cards}_{i}')
        #
        else:
            # print(Card_Checks.special_set_conditions[cards])
            set_value(f'Special_Set_Cond_Input_Card_{cards}_{i}', set['causality_description'].replace('\n', ''))
            Text_Resize(f'Special_Set_Cond_Input_Card_{cards}_{i}')

        for tag in range(len(special_sets)):
            # print(f"Special_Set_aim_target" + '_Card_' + str(cards) + '_' + str(i))
            set_value(f"Special_Set_Aim_Target_Input" + '_Card_' + str(cards) + '_' + str(i), set['aim_target'])
            set_value(f"Special_Set_Increase_Rate_Input" + '_Card_' + str(cards) + '_' + str(i), set['increase_rate'])
            set_value(f"Special_Set_Level_Bonus_Input" + '_Card_' + str(cards) + '_' + str(i), set['lv_bonus'])

    Specials.last_rows = num_of_special_sets
        # print(len(specials_fetch))
            
########################################################################################################################################################################################################        
def Active_Skill_Widgets(card):
    
    
    # print(card)
    if does_alias_exist(f'Active_Skill_Text_Card_{card}'):
        Delete_Items([f'Active_Skill_Text_Card_{card}', f'Active_Skill_Group_1_Card_{card}', f'Active_Skill_Group_2_Card_{card}', f'Active_Skill_Name_Text_Card_{card}', 
                     f'Active_Name_Card_{card}', f'Active_Skill_Group_3_Card_{card}', f'Active_Skill_Desc_Text_Card_{card}', f'Active_Desc_Card_{card}', f'Active_Skill_Group_4_Card_{card}',
                    f'Active_Skill_Cond_Text_Card_{card}', f'Active_Cond_Card_{card}', f'Active_Skill_Separator_Card_{card}', f'Active_Skills_Group_Card_{card}', f'Active_Skills_Text_Card_{card}',
                    f'Active_Skills_Button_Add_Card_{card}', f'Active_Skills_Button_Del_Card_{card}', f'Custom_Unit_Ultimate_Special_Checkbox_{card}'])
                     
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

    ttt = Table_Inputs(table_name=f'Active_Skill_Set_Card_{card}', row_name=f'Active_Skill_Set_Row_Card_{card}_', class_name=Active_Skill_Set,
                use_child_window=False, table_parent=f'Active_Skill_Card_{card}', table_height=47, table_width=755, transformation=True, transformation_card_num=card)

    with group(horizontal=True, tag=f'Active_Skills_Group_Card_{card}', parent=f'Active_Skill_Card_{card}'):
        add_text('Active Skills', tag=f'Active_Skills_Text_Card_{card}', color=(255,50,50), parent=f'Active_Skills_Group_Card_{card}')
        add_button(label='Add Skill', tag=f'Active_Skills_Button_Add_Card_{card}', parent=f'Active_Skills_Group_Card_{card}', callback=Active_Skill_Add)
        add_button(label='Del Skill', tag=f'Active_Skills_Button_Del_Card_{card}', parent=f'Active_Skills_Group_Card_{card}', callback=Active_Skill_Del)
    Widget_Aliases.tags_to_delete.append(f'Active_Skills_Group_Card_{card}')
    Widget_Aliases.tags_to_delete.append(f'Active_Skills_Text_Card_{card}')
    Widget_Aliases.tags_to_delete.append(f'Active_Skills_Button_Add_Card_{card}')
    Widget_Aliases.tags_to_delete.append(f'Active_Skills_Button_Del_Card_{card}')
    
    Active_Skill.rows = 1
    sss = Table_Inputs(table_name=f'Active_Skill_Table_Card_{card}', row_name=f'Active_Skill_Row_Card_{card}_', class_name=Active_Skill,
                        use_child_window=False, table_parent=f'Active_Skill_Card_{card}', table_height=80, table_width=1132,
                        combo=True, combo_list=Efficacy_Values.combo_list, combo_tag=Active_Skill.row_names[3], transformation=True, transformation_card_num=card)
            
    set_item_height(f'Active_Skill_Table_Card_{card}', (24 * Active_Skill.rows + 23))
    
    add_checkbox(label='Ultimate Special', callback=Custom_Unit_Ultimate_Special_Checkbox, tag=f'Custom_Unit_Ultimate_Special_Checkbox_{card}', parent=f'Active_Skill_Card_{card}')
    configure_item(f'Active_Skill_Card_{card}', show=True)

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
    Active_Skill.tags_to_delete.append(f'Custom_Unit_Ultimate_Special_Checkbox_{card}')

def Ultimate_Special_Widgets(card):
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
            add_input_text(tag=Active_Skill.ultimate_names[z] + '_Card_' + str(card), default_value='', hint=Active_Skill.ultimate_hints[z], width=String_Length.length[0], callback=Text_Resize, parent=f'Ultimate_Special_Group_Card_{card}')
            Widget_Aliases.tags_to_delete.append(Active_Skill.ultimate_hints[z] + '_Card_' + str(card) + '_Text')
            Widget_Aliases.tags_to_delete.append(Active_Skill.ultimate_names[z] + '_Card_' + str(card))

########################################################################################################################################################################################################      
def Custom_Unit_Active_Skill_Query(*, card=int, json_cards=0):
    card = card

    if not Card_Checks.json_data[json_cards]:
        data = read_json_from_zip(card_id)
    else:
        data = Card_Checks.json_data[json_cards]

    if 'active_skill' in data:
        active_skill = data['active_skill']
        active_skill_set = data['active_skill_set']

    # if json_cards in Card_Checks.active_skill_ids:
        Active_Skill_Widgets(card)
        # for key, value in Card_Checks.active_skill_ids.items():
        for i in range(1):
            Active_Skill.rows = len(active_skill)



            ttt = Table_Inputs(table_name=f'Active_Skill_Set_Card_{card}', row_name=f'Active_Skill_Set_Row_Card_{card}_', class_name=Active_Skill_Set,
                                use_child_window=False, table_parent=f'Active_Skill_Card_{card}', table_height=47, table_width=755, transformation=True, transformation_card_num=card)
            # print(ttt)


            Delete_Items([f'Active_Skills_Group_Card_{card}', f'Active_Skills_Text_Card_{card}', f'Active_Skills_Button_Add_Card_{card}', f'Active_Skills_Button_Del_Card_{card}', f'Custom_Unit_Ultimate_Special_Checkbox_{card}'])
            with group(horizontal=True, tag=f'Active_Skills_Group_Card_{card}', parent=f'Active_Skill_Card_{card}'):
                add_text('Active Skills', tag=f'Active_Skills_Text_Card_{card}', color=(255,50,50), parent=f'Active_Skills_Group_Card_{card}')
                add_button(label='Add Skill', tag=f'Active_Skills_Button_Add_Card_{card}', parent=f'Active_Skills_Group_Card_{card}', callback=Active_Skill_Add)
                add_button(label='Del Skill', tag=f'Active_Skills_Button_Del_Card_{card}', parent=f'Active_Skills_Group_Card_{card}', callback=Active_Skill_Del)
            Widget_Aliases.tags_to_delete.append(f'Active_Skills_Group_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skills_Text_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skills_Button_Add_Card_{card}')
            Widget_Aliases.tags_to_delete.append(f'Active_Skills_Button_Del_Card_{card}')

            sss = Table_Inputs(table_name=f'Active_Skill_Table_Card_{card}', row_name=f'Active_Skill_Row_Card_{card}_', class_name=Active_Skill,
                                use_child_window=False, table_parent=f'Active_Skill_Card_{card}', table_height=80, table_width=1132,
                                combo=True, combo_list=Efficacy_Values.combo_list, combo_tag=Active_Skill.row_names[3], transformation=True, transformation_card_num=card)

            add_checkbox(label='Ultimate Special', callback=Custom_Unit_Ultimate_Special_Checkbox, tag=f'Custom_Unit_Ultimate_Special_Checkbox_{card}', parent=f'Active_Skill_Card_{card}')

            # print(sss)
            if 'ultimate_special' in data:
                ultimate_special = data['ultimate_special']

                set_value(f'Custom_Unit_Ultimate_Special_Checkbox_{card}', True)

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
                        add_input_text(tag=Active_Skill.ultimate_names[z] + '_Card_' + str(card), default_value='', hint=Active_Skill.ultimate_hints[z], width=String_Length.length[0], callback=Text_Resize, parent=f'Ultimate_Special_Group_Card_{card}')
                        Widget_Aliases.tags_to_delete.append(Active_Skill.ultimate_hints[z] + '_Card_' + str(card) + '_Text')
                        Widget_Aliases.tags_to_delete.append(Active_Skill.ultimate_names[z] + '_Card_' + str(card))


                for key, value in ultimate_special.items():
                    # print("ultimate hit")
                    if key in Active_Skill.ultimate_names:
                        # print("Ultimate key hit")
                        set_value(key + '_Card_' + str(card), value)

                # for o in range(len(Active_Skill.ultimate_names)):
                #     set_value(Active_Skill.ultimate_names[o] + '_Card_' + str(card), ultimate_special[0][o])
                #     Text_Resize(Active_Skill.ultimate_names[o] + '_Card_' + str(card))



            # Table_Inputs(table_name='Active_Skill_Table_Card_0', row_name='Active_Skill_Table_Row_', parent='Active_Skill_Child_Window', class_name=Active_Skill)
            # Active_Skill_Inputs()
            Active_Skill.last_rows = len(active_skill)
            # active_skill_set_id = get_value('CardID1')

            set_item_height(f'Active_Skill_Table_Card_{card}', (24 * len(active_skill)) + 23)

            for i in range(len(active_skill)):
                for key, value in active_skill[i].items():
                    if value == '':
                        set_value(key + '_Card_' + str(card) + '_Row_' + str(i), 'NULL')

                    elif key == Active_Skill.row_names[3]:
                        set_value(key + '_Card_' + str(card) + '_Row_' + str(i), Efficacy_Values.eff_dict[int(value)])

                    else:
                        set_value(key + '_Card_' + str(card) + '_Row_' + str(i), value)

                    # set_value(Active_Skill.row_names[0] + str(i), active_skill_set_id)


            for key, value in active_skill_set.items():
                # JSON file has more keys than row names, so we need to check if they exist
                if f"Active_Skill_Set_{key}" in Active_Skill_Set.row_names:
                    print(f"Active_Skill_Set_{key}")
                    if value == '':
                        set_value(f'Active_Skill_Set_{key}' + '_Card_' + str(card) + '_Row_' + '0', 'NULL')
                    else:
                        set_value(f'Active_Skill_Set_{key}' + '_Card_' + str(card) + '_Row_' + '0', value)


            set_value(f'Active_Name_Card_{card}', active_skill_set['name'])
            set_value(f'Active_Desc_Card_{card}', active_skill_set['effect_description'].replace('\n', ''))
            set_value(f'Active_Cond_Card_{card}', active_skill_set['condition_description'].replace('\n', ''))
            Text_Resize(f'Active_Name_Card_{card}')
            Text_Resize(f'Active_Desc_Card_{card}')
            Text_Resize(f'Active_Cond_Card_{card}')

            configure_item(f'Active_Skill_Card_{card}', show=True)
            set_value(f'Custom_Unit_Active_Skill_Checkbox_{card}', True)

########################################################################################################################################################################################################
def Standby_Skill_Widgets(card):
    standby_skill = 0
    Delete_Items([f'Standby_Skill_Set_Text_{card}_{standby_skill}', f'Standby_Skill_Set_Group_1_{card}_{standby_skill}', f'Standby_Skill_Name_Text_{card}_{standby_skill}', 
                  f'Standby_Set_Name_Input_Text_{card}_{standby_skill}', f'Standby_Skill_Set_Group_2_{card}_{standby_skill}', f'Standby_Skill_Desc_Text_{card}_{standby_skill}', 
                  f'Standby_Set_Desc_Input_Text_{card}_{standby_skill}', f'Standby_Skill_Set_Group_3_{card}_{standby_skill}', f'Standby_Skill_Cond_Text_{card}_{standby_skill}', 
                  f'Standby_Set_Cond_Input_Text_{card}_{standby_skill}', f'Standby_Skill_Set_Separator_{card}_{standby_skill}', f'Standby_Skill_Text_{card}_{standby_skill}'])
    
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
                
    add_separator(tag=f'Standby_Skill_Set_Separator_{card}_{standby_skill}', parent=f'Standby_Skill_{card}')
    add_text('Standby Skill', color=(255,50,50), parent=f'Standby_Skill_{card}', tag=f'Standby_Skill_Text_{card}_{standby_skill}')
                
    ttt = Table_Inputs(table_name=f'Standby_Skill_Set_Table_{card}_{standby_skill}', row_name=f'Standby_Skill_Set_Table_Row_{card}_{standby_skill}', table_parent=f'Standby_Skill_{card}', use_child_window=False, 
                class_name=Standby_Skill_Set, table_width=500, table_height=49, row_width=85, freeze_rows=1, table_policy=mvTable_SizingStretchSame, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=card)
            
    Standby_Skill.rows = 1
    Table_Inputs(table_name=f'Standby_Skill_Table_{card}_{standby_skill}', row_name=f'Standby_Skill_Table_Row_{card}_{standby_skill}', table_parent=f'Standby_Skill_{card}', use_child_window=False, 
                class_name=Standby_Skill, table_width=825, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=card)

    set_item_height(f'Standby_Skill_Table_{card}_{standby_skill}', (24 * Standby_Skill.rows) + 23)
    configure_item(f'Standby_Skill_{card}', show=True)

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
def Custom_Unit_Standby_Skill_Query(*, card=int, json_cards=0):
    card = card

    if not Card_Checks.json_data[json_cards]:
        data = read_json_from_zip(card_id)
    else:
        data = Card_Checks.json_data[json_cards]
    
    # if Card_Checks.standby_skill_ids.get(json_cards, None):
    if 'standby_skills' in data:

        # standby_skill_set [dict]
        standby_skill_set = data['standby_skill_set']
        # standby_skills [dict, dict, dict]
        standby_skills = data['standby_skills']
        standby_name = data['standby_skill_set']['name']
        standby_desc = data['standby_skill_set']['effect_description']
        standby_cond = data['standby_skill_set']['condition_description']

    # if len(Card_Checks.standby_skill_cards) > 0 and Card_Checks.standby_skill_cards[0]:
        Standby_Skill_Widgets(card)
        
        for skills in range(1):
            Standby_Skill_Widgets(card=card)

            ttt = Table_Inputs(table_name=f'Standby_Skill_Set_Table_{card}_{skills}', row_name=f'Standby_Skill_Set_Table_Row_{card}_{skills}', table_parent=f'Standby_Skill_{card}', use_child_window=False,
                        class_name=Standby_Skill_Set, table_width=500, table_height=49, row_width=85, freeze_rows=1, table_policy=mvTable_SizingStretchSame, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=skills)
            print(ttt)
            Standby_Skill.rows = len(standby_skills)
            ttt = Table_Inputs(table_name=f'Standby_Skill_Table_{card}_{skills}', row_name=f'Standby_Skill_Table_Row_{card}_{skills}', table_parent=f'Standby_Skill_{card}', use_child_window=False,
                        class_name=Standby_Skill, table_width=825, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=skills)
            # print(ttt)
            set_item_height(f'Standby_Skill_Table_{card}_{skills}', (24 * len(standby_skills)) + 23)


            for key, value in standby_skill_set.items():
                if f'Standby_Set_{key}' in Standby_Skill_Set.row_names:
                    print(f'Standby_Set_{key}' + '_Card_' + str(card) + '_Row_' + str(skills))
                    set_value(f'Standby_Set_{key}' + '_Card_' + str(card) + '_Row_' + str(skills) + '0', value)
            set_value(f'Standby_Set_Name_Input_Text_{card}_{skills}', standby_name)
            set_value(f'Standby_Set_Desc_Input_Text_{card}_{skills}', standby_desc.replace('\n', ''))
            set_value(f'Standby_Set_Cond_Input_Text_{card}_{skills}', standby_cond.replace('\n', ''))
            Text_Resize(f'Standby_Set_Name_Input_Text_{card}_{skills}')
            Text_Resize(f'Standby_Set_Desc_Input_Text_{card}_{skills}')
            Text_Resize(f'Standby_Set_Cond_Input_Text_{card}_{skills}')
            # Text_Resize(f'Standby_Set_causality_conditions' + '_Card_' + str(card) + '_Row_' + str(skills) + '0')


            for i in range(len(standby_skills)):
                for key, value in standby_skills[i].items():
                    print(f'Standby_Skill_{key}' + '_Card_' + str(card) + '_Row_' + str(skills) + str(i))
                    if value is '':
                        set_value(f'Standby_Skill_{key}' + '_Card_' + str(card) + '_Row_' + str(skills) + str(i), 'NULL')
                        # Text_Resize(f'Standby_Skill_{key}' + '_Card_' + str(card) + '_Row_' + str(skills) + str(i))
                    # ### row_names[6] is efficacy values
                    # elif Standby_Skill.row_names[z] == Standby_Skill.row_names[6]:
                    #
                    #     if get_value(Standby_Skill.row_names[4] + '_Card_' + str(card) + '_Row_' + str(standby_skills) + str(i)) == '103':
                    #         efficacy_values = ast.literal_eval(standby_skill_fetch[i][z])
                    #         efficacy_values[0] = int(str(efficacy_values[0]).replace(str(efficacy_values[0])[1], '3'))
                    #         efficacy_values[2] = int(efficacy_values[0])
                    #         set_value(Standby_Skill.row_names[z] + '_Card_' + str(card) + '_Row_' + str(standby_skills) + str(i), efficacy_values)
                    #         print(efficacy_values)
                    #     else:
                    #         set_value(Standby_Skill.row_names[z] + '_Card_' + str(card) + '_Row_' + str(standby_skills) + str(i), standby_skill_fetch[i][z])
                    
                    else:
                        set_value(f'Standby_Skill_{key}' + '_Card_' + str(card) + '_Row_' + str(skills) + str(i), value)
                        # Text_Resize(f'Standby_Skill_{key}' + '_Card_' + str(card) + '_Row_' + str(skills) + str(i))
                        
        configure_item(f'Standby_Skill_{card}', show=True)
        set_value(f'Custom_Unit_Standby_Skill_Checkbox_{card}', True)
            
########################################################################################################################################################################################################   
def Custom_Unit_Finish_Skill_Set_Widgets(card, *, finish_skills=1):
    
    for finish_skill in range(finish_skills):
        print(finish_skill)
        Delete_Items(f'Finish_Skill_Set_Text_{card}_{finish_skill}')
        add_text('Finish Skill Set', color=(255,50,50), parent=f'Finish_Skill_{card}', tag=f'Finish_Skill_Set_Text_{card}_{finish_skill}')


        Delete_Items(f'Finish_Skill_Set_Group_{card}_{finish_skill}')
        with group(horizontal=True, parent=f'Finish_Skill_{card}', tag=f'Finish_Skill_Set_Group_{card}_{finish_skill}'):
        
            Delete_Items(f'Finish_Skill_Set_Name_{card}_{finish_skill}')
            Delete_Items(f'Finish_Set_Name_{card}_{finish_skill}')

            add_text('Name:', color=(255, 174, 26), tag=f'Finish_Skill_Set_Name_{card}_{finish_skill}', parent=f'Finish_Skill_Set_Group_{card}_{finish_skill}')
            add_input_text(default_value='', hint='Name', width=String_Length.length[0], tag=f'Finish_Set_Name_{card}_{finish_skill}', parent=f'Finish_Skill_Set_Group_{card}_{finish_skill}')

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
                
        ttt = Table_Inputs(table_name=f'Finish_Skill_Set_Table_{card}_{finish_skill}', row_name=f'Finish_Skill_Set_Table_Row_{card}_{finish_skill}', table_parent=f'Finish_Skill_{card}', use_child_window=False, 
                    class_name=Finish_Skill_Set, table_width=927, table_height=47, row_width=80, freeze_rows=1, loop_number=finish_skill, used_in_loop=True, table_policy=mvTable_SizingFixedFit,
                    transformation=True, transformation_card_num=card)
        Delete_Items(f'Finish_Skill_Skill_Text_{card}_{finish_skill}')
        add_text('Finish Skill', tag=f'Finish_Skill_Skill_Text_{card}_{finish_skill}', color=(255,50,50), parent=f'Finish_Skill_{card}')
        Widget_Aliases.tags_to_delete.append(f'Finish_Skill_Skill_Text_{card}_{finish_skill}')
                
        ### Same logic from Finish Skill Set Table applies to these aliases.
        Finish_Skill.rows = 1
        sss = Table_Inputs(table_name=f'Finish_Skill_Table_{card}_{finish_skill}', row_name=f'Finish_Skill_Table_Row_{card}_{finish_skill}', table_parent=f'Finish_Skill_{card}', use_child_window=False, 
                    class_name=Finish_Skill, table_width=836, row_width=82, table_height=114, freeze_rows=1, loop_number=finish_skill, used_in_loop=True, transformation=True, transformation_card_num=card)
                
        set_item_height(f'Finish_Skill_Table_{card}_{finish_skill}', (24 * Finish_Skill.rows) + 23)
    configure_item(f'Finish_Skill_{card}', show=True)
    
########################################################################################################################################################################################################
def Custom_Unit_Finish_Skill_Query(*, card=int, json_cards=0):
    from . standby_finish import Finish_Skill_Set_Widgets
    cards = card

    if not Card_Checks.json_data[json_cards]:
        data = read_json_from_zip(card_id)
    else:
        data = Card_Checks.json_data[json_cards]
    
    ### Number of cards returned from Dokkan Wiki
    
    ### Dictionary in download.py that set dictionary values of True or False based on a unit having a finish skill. 
    if 'finish_skill_set' in data:

        finish_skill_set = data['finish_skill_set']
        finish_skills = data['finish_skills']
        finish_name = [v["name"] for v in finish_skill_set.values()]
        finish_desc = [v["effect_description"] for v in finish_skill_set.values()]
        finish_cond = [v["condition_description"] for v in finish_skill_set.values()]
        finish_skill_ids = [key for key in finish_skills.keys()]
    # if Card_Checks.finish_skill_ids.get(json_cards, None):
    # if len(Card_Checks.finish_skill_cards) > 0 and Card_Checks.finish_skill_cards[0]:
        
        
        for skills in range(len(finish_skill_set)):
            Finish_Skill_Set_Widgets(z=cards, finish_skills=skills)
            Finish_Skill.rows = len(finish_skills[finish_skill_ids[skills]])

            ### Finish_Set_View_ID_Card_1_Row_10  Row_1 would be the finish skill number, then the 0 after that is the row number.
            ttt = Table_Inputs(table_name=f'Finish_Skill_Set_Table_{cards}_{skills}', row_name=f'Finish_Skill_Set_Table_Row_{cards}_{skills}', table_parent=f'Finish_Skill_{cards}', use_child_window=False,
                        class_name=Finish_Skill_Set, table_width=927, table_height=47, row_width=80, freeze_rows=1, loop_number=skills, used_in_loop=True, table_policy=mvTable_SizingFixedFit,
                        transformation=True, transformation_card_num=cards)

            # print(ttt)
            Delete_Items(f'Finish_Skill_Skill_Text_{cards}_{skills}')
            add_text('Finish Skill', tag=f'Finish_Skill_Skill_Text_{cards}_{skills}', color=(255,50,50), parent=f'Finish_Skill_{cards}')
            Widget_Aliases.tags_to_delete.append(f'Finish_Skill_Skill_Text_{cards}_{skills}')
            
            Finish_Skill.rows = len(finish_skills[finish_skill_ids[skills]])
            ### Same logic from Finish Skill Set Table applies to these aliases.
            sss = Table_Inputs(table_name=f'Finish_Skill_Table_{cards}_{skills}', row_name=f'Finish_Skill_Table_Row_{cards}_{skills}', table_parent=f'Finish_Skill_{cards}', use_child_window=False,
                        class_name=Finish_Skill, table_width=836, row_width=82, table_height=114, freeze_rows=1, loop_number=skills, used_in_loop=True, transformation=True, transformation_card_num=cards)
            # print(sss)

            Finish_Skill.last_rows = (len(finish_skills[finish_skill_ids[skills]]))
            set_item_height(f'Finish_Skill_Table_{cards}_{skills}', (24 * Finish_Skill.rows) + 23)
            

            i = 0
            for key, value in finish_skill_set[finish_skill_ids[skills]].items():
                if f"Finish_Set_{key}" in Finish_Skill_Set.row_names:
                    # print(f"Finish_Set_{key}" + '_Card_' + str(cards) + '_Row_' + str(skills) + str(i))
                    if value == '':
                        set_value(f"Finish_Set_{key}" + '_Card_' + str(cards) + '_Row_' + str(skills) + str(i), 'NULL')
                    else:
                        set_value(f"Finish_Set_{key}" + '_Card_' + str(cards) + '_Row_' + str(skills) + str(i), value)

                # set_value(f"Finish_Set_dialog_label" + '_Card_' + str(cards) + '_Row_' + str(skills) + str(i), 'NULL')

                # Absolute dogshit hack to make this work
                if f'Finish_Set_{key}' == 'Finish_Set_special_view_id':
                    i += 1


                    
            # set_value(Finish_Skill_Set.row_names[6] + '_Card_' + str(cards) + '_Row_' + str(skills) + '0', int(get_value(f'id_Card_{cards}_Row_0')) + skills)
            # print(Card_Checks.finish_skill_names)
            set_value(f'Finish_Set_Name_{cards}_{skills}', finish_name[skills])
            set_value(f'Finish_Set_Desc_{cards}_{skills}', finish_desc[skills].replace('\n', ''))
            set_value(f'Finish_Set_Cond_{cards}_{skills}', finish_cond[skills].replace('\n', ''))
            Text_Resize(f'Finish_Set_Name_{cards}_{skills}')
            Text_Resize(f'Finish_Set_Desc_{cards}_{skills}')
            Text_Resize(f'Finish_Set_Cond_{cards}_{skills}')

            for j in range(len(finish_skills[finish_skill_ids[skills]])):
                # print(finish_skills[finish_skill_ids[skills]][j])
                for key, value in finish_skills[finish_skill_ids[skills]][j].items():

                    if f'Finish_Skill_{key}' in Finish_Skill.row_names:
                        # print(f'Finish_Skill_{key}' + '_Card_' + str(cards) + '_Row_' + str(skills) + str(j))
                        if value == '':
                            set_value(f'Finish_Skill_{key}' + '_Card_' + str(cards) + '_Row_' + str(skills) + str(j), 'NULL')
                        else:
                            set_value(f'Finish_Skill_{key}' + '_Card_' + str(cards) + '_Row_' + str(skills) + str(j), value)


            Widget_Aliases.tags_to_delete.append(f'Finish_Skill_Separator_{cards}_{skills}')
            add_separator(tag=f'Finish_Skill_Separator_{cards}_{skills}', parent=f'Finish_Skill_{cards}')
            configure_item(f'Finish_Skill_{cards}', show=True)
            set_value(f'Custom_Unit_Finish_Skill_Checkbox_{card}', True)

########################################################################################################################################################################################################
def Dokkan_Field_Widgets(card, *, fields=1):
    ### In case a unit comes out with more than 1 dokkan field
    # for card in range(len(Card_Checks.card_ids)):
        # for field in range(len(Card_Checks.dokkan_field_cards)):

    
    for field in range(fields):
        Delete_Items([f'Dokkan_Field_Text_{card}_{field}', f'Dokkan_Field_Name_Text_Group_{card}_{field}', f'Dokkan_Field_Name_Text_{card}_{field}', 
                     f'Dokkan_Field_Name_Input_Text_{card}_{field}', f'Dokkan_Field_Desc_Text_Group_{card}_{field}', f'Dokkan_Field_Desc_Text_{card}_{field}', 
                     f'Dokkan_Field_Desc_Input_Text_{card}_{field}', f'Dokkan_Field_Resource_Text_Group_{card}_{field}', f'Dokkan_Field_Resource_Text_{card}_{field}', 
                     f'Dokkan_Field_Resource_ID_{card}_{field}', f'Dokkan_Field_Separtor_1_{card}_{field}', f'Dokkan_Field_Checkbox_Group_{card}_{field}', 
                     f'Link_to_Active_Button_{card}_{field}', f'Link_to_Passive_Button_{card}_{field}', f'Dokkan_Field_Separtor_2_{card}_{field}'])
        
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
                
        add_separator(tag=f'Dokkan_Field_Separtor_2_{card}_{field}', parent=f'Dokkan_Field_{card}')
                
        Dokkan_Field.rows = 1
        t = Table_Inputs(table_name=f'Dokkan_Field_Table_{card}_{field}', row_name=f'Dokkan_Field_Table_Row_{card}_{field}', table_parent=f'Dokkan_Field_{card}', use_child_window=False, 
                    class_name=Dokkan_Field, table_width=1100, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=field, table_policy=mvTable_SizingFixedFit)
                
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
                
########################################################################################################################################################################################################
def Custom_Unit_Dokkan_Field_Query(*, card=int, json_cards=0):
    card = card

    if not Card_Checks.json_data[json_cards]:
        data = read_json_from_zip(card_id)
    else:
        data = Card_Checks.json_data[json_cards]

    if 'dokkan_field' in data:
        domain_field = data['dokkan_field']
        domain_skills = domain_field['skills']
        field_type = domain_field['skill_type']
        domain_name = domain_field['name']
        domain_desc = domain_field['description']
        domain_resource = domain_field['resource_id']



        configure_item(f'Dokkan_Field_{card}', show=True)
        set_value(f'Custom_Unit_Dokkan_Field_Checkbox_{card}', True)
        Dokkan_Field_Widgets(card, fields=1)
        ### Number of dokkan fields on said card (I think it will always be one)
        for dokkan_field in range(1):
            
            if field_type == 'Active':
                set_value(f'Link_to_Active_Button_{card}_{dokkan_field}', True)

            if field_type == 'Passive':
                set_value(f'Link_to_Passive_Button_{card}_{dokkan_field}', True)
                
            
            Dokkan_Field.rows = len(domain_skills)
            t = Table_Inputs(table_name=f'Dokkan_Field_Table_{card}_{dokkan_field}', row_name=f'Dokkan_Field_Table_Row_{card}_{dokkan_field}', table_parent=f'Dokkan_Field_{card}', use_child_window=False, 
                        class_name=Dokkan_Field, table_width=1100, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=dokkan_field, table_policy=mvTable_SizingFixedFit)
            # print(t)
            
            set_value(f'Dokkan_Field_Name_Input_Text_{card}_{dokkan_field}', domain_name)
            set_value(f'Dokkan_Field_Desc_Input_Text_{card}_{dokkan_field}', domain_desc)
            Resize_Description(f'Dokkan_Field_Desc_Input_Text_{card}_{dokkan_field}', domain_desc)
            set_value(f'Dokkan_Field_Resource_ID_{card}_{dokkan_field}', domain_resource)
            Text_Resize(f'Dokkan_Field_Name_Input_Text_{card}_{dokkan_field}')
            Text_Resize(f'Dokkan_Field_Desc_Input_Text_{card}_{dokkan_field}')
            Text_Resize(f'Dokkan_Field_Resource_ID_{card}_{dokkan_field}')
            
            for row in range(len(domain_skills)):
                for key, value in domain_skills[row].items():
                    if f'DF_{key}' in Dokkan_Field.row_names:
                        if value == '':
                            set_value(f'DF_{key}' + '_Card_' + str(card) + '_Row_0' + str(row), 'NULL')
                        elif f'DF_{key}' == Dokkan_Field.row_names[10]:
                            set_value(f'DF_{key}' + '_Card_' + str(card) + '_Row_0' + str(row), value)
                            Text_Resize(f'DF_{key}' + '_Card_' + str(card) + '_Row_0' + str(row))
                        else:
                            set_value(f'DF_{key}' + '_Card_' + str(card) + '_Row_0' + str(row), value)
                        
                    
            set_item_height(f'Dokkan_Field_Table_{card}_{dokkan_field}', (24 * len(domain_skills)) + 23)
            
            widget_widths_list = []
            for row in range(len(domain_skills)):
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
            set_item_width(f'Dokkan_Field_Table_{card}_{dokkan_field}', max_width + 100)

########################################################################################################################################################################################################
def Battle_Params_Widgets(card):
    add_text('Transformation Information', tag=f'Transformation_Information_Text_{card}', color=(255,50,50), parent=f'Battle_Params_{card}')
    
    Transformation_Descriptions.rows = 1
    skill_type_combo_list = ['Active Skill', 'Passive Skill', 'Standby Skill', 'Finish Skill']
    tt = Table_Combo_Inputs(table_name=f'Transformation_Descriptions_Table_{card}', row_name=f'Transformation_Descriptions_Table_Row_{card}', table_parent=f'Battle_Params_{card}', 
                       class_name=Transformation_Descriptions, table_width=600, row_width=82, table_height=45, freeze_rows=1, table_policy=mvTable_SizingFixedFit,
                       combo_columns=[0], combo=True, combo_list=[skill_type_combo_list], transformation_card_num=card)
        
    add_separator(tag=f'Transformation_Descriptions_Table_Separator_{card}', parent=f'Battle_Params_{card}')
    combo_list = ['Transformation', 'Standby/Finish', 'Rage', 'Giant']
    with group(horizontal=True, tag=f'Battle_Params_Group_{card}', parent=f'Battle_Params_{card}'):
        add_text('Battle Params', tag=f'Battle_Params_Text_{card}', color=(255,50,50))
        add_combo(combo_list, tag=f'Battle_Param_Preset_Combo_{card}', width=String_Length.length[9], default_value='Presets', callback=Battle_Param_Presets)
        add_text('(?)', tag='Battle_Params_Hints')
        with tooltip('Battle_Params_Hints'):
            add_text('                                                             Rage & Giant Params')
            add_text('--------------------------------------------------------------------------------------------------------------------------------------------------------')
            add_text('idx 7 = The Effect Pack ID of the animated card icon that plays on the bottom right of the screen')
            add_text('idx 8 = The Effect Pack ID of the Initial Effect Pack; played upon Rage/Giant transformation')
            add_text('idx 9 = The Effect Pack ID of the Continued Effect Pack; played in between turns')
            add_text('idx 10 = The Effect Pack ID of the Reverse Effect Pack; played upon reverting back to previous form')
        
        
    
    Widget_Aliases.tags_to_delete.append(f'Transformation_Information_Text_{card}')
    Widget_Aliases.tags_to_delete.append(f'Transformation_Descriptions_Table_Separator_{card}')
    Widget_Aliases.tags_to_delete.append(f'Battle_Params_Text_{card}')
    Widget_Aliases.tags_to_delete.append(f'Battle_Param_Preset_Combo_{card}')
    
    # Battle Param Section
    ######################################################################################################################################################################################
    param_num = 0
    # Battle_Params.rows = 1
    # ttt = Table_Combo_Inputs(table_name=f'Battle_Params_Table_{card}_{param_num}', row_name=f'Battle_Params_Table_Row_{card}_{param_num}', table_parent=f'Battle_Params_{card}', 
                    # class_name=Battle_Params, table_width=270, row_width=82, freeze_rows=1, transformation_card_num=card, loop_number=param_num, used_in_loop=True, table_policy=mvTable_SizingFixedFit)
    # Resize_Table(f'Battle_Params_Table_{card}_{param_num}', Battle_Params.rows)
    configure_item(f'Battle_Params_{card}', show=True)
    

########################################################################################################################################################################################################
def Custom_Unit_Battle_Params_Information(*, card=int, json_cards=0):
    card = card
    battle_params_dictionary = Card_Checks.battle_params
    print(battle_params_dictionary)
    
    if battle_params_dictionary.get(json_cards, None):
    # if battle_params_dictionary:
        # if battle_params_dictionary[json_cards]:
        Delete_Items([f'Transformation_Information_Text_{card}', f'Transformation_Descriptions_Table_Separator_{card}', f'Battle_Params_Text_{card}'])
        add_text('Transformation Information', tag=f'Transformation_Information_Text_{card}', color=(255,50,50), parent=f'Battle_Params_{card}')


        skill_type_combo_list = ['Active Skill', 'Passive Skill', 'Standby Skill', 'Finish Skill']
        tt = Table_Combo_Inputs(table_name=f'Transformation_Descriptions_Table_{card}', row_name=f'Transformation_Descriptions_Table_Row_{card}', table_parent=f'Battle_Params_{card}', 
                            class_name=Transformation_Descriptions, table_width=600, row_width=82, table_height=45, freeze_rows=1, table_policy=mvTable_SizingFixedFit,
                            combo_columns=[0], combo=True, combo_list=[skill_type_combo_list], transformation_card_num=card)
        # print(tt)
        set_value(Transformation_Descriptions.row_names[1] + '_Card_' + str(card) + '_Row_0', Card_Checks.transformation_descriptions[0].replace('\n', ''))
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
        for key, value in battle_params_dictionary[0].items():
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
        
        set_value(f'Custom_Unit_Battle_Params_Checkbox_{card}', True)

########################################################################################################################################################################################################
def Leader_Skill_Widgets(card):
    # def Leader_Preset_Resize(tag_id):
        # text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIAL.ttf')
        # set_item_width(tag_id, text_width + 27)
    
    leader_options = ['Element Type', 'Extreme Class', 'Super Class', 'All Types', '1 Category', '1 Category & 1 Element', '2 Categories', '2 Categories & 1 Extra', '2 Categories & 2 Extra', '3 Categories & 2 Extra', '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)']
    leader_categories = Leader_Skill_Info.cat_list
    # for i in range(len(Leader_Skill_Info.tags_to_remove)):
        # Delete_Items(Leader_Skill_Info.tags_to_remove[i])
    Delete_Items([f'Leader_Skill_Widgets_Group_{card}_1', f'Leader_Skill_Widgets_Group_{card}_2', f'Leader_Skill_Text_{card}', f'Leader_Skill_Preset_List_{card}', f'Leader_Efficacy_Value_Changer_{card}', 
                  f'Leader_Efficacy_Value_Changer_Text_{card}', f'Leader_Efficacy_Value_Changer_Tooltip_{card}', f'Leader_Name_Text_Input_{card}', f'Leader_Desc_Text_Input_{card}'])    

    with group(horizontal=True, tag=f'Leader_Skill_Widgets_Group_{card}_1', parent=f'Leader_Skill_{card}'):
        add_text('Leader Skill', tag=f'Leader_Skill_Text_{card}', color=(255,50,50), parent=f'Leader_Skill_Widgets_Group_{card}_1')


        add_combo(leader_options, default_value='Presets', tag=f'Leader_Skill_Preset_List_{card}', width=String_Length.length[9], callback=Leader_Combo, parent=f'Leader_Skill_Widgets_Group_{card}_1')
        # Leader_Preset_Resize(f'Leader_Skill_Preset_List_{card}')
        
        add_combo(leader_categories, default_value='Categories', tag=f'Leader_Skill_Category_Selection_{card}_0', width=String_Length.length[11], callback=Leader_Cat_Selection, parent=f'Leader_Skill_Widgets_Group_{card}_1')
        # set_value(f'Leader_Skill_Category_Selection_{combo}', json_dict[f'Card {card + 1}']['Leader Skill']['Categories'][combo])
        # Leader_Preset_Resize(f'Leader_Skill_Category_Selection_{card}_0')


    with group(horizontal=True, parent=f'Leader_Skill_{card}', tag=f'Leader_Skill_Widgets_Group_{card}_2'):
        add_input_text(default_value='', hint='XXX%', width=String_Length.length[0], callback=Leader_Efficacy_Value_Changer, tag=f'Leader_Efficacy_Value_Changer_{card}', parent=f'Leader_Skill_Widgets_Group_{card}_2')

        add_text('%', tag=f'Leader_Efficacy_Value_Changer_Text_{card}', parent=f'Leader_Skill_Widgets_Group_{card}_2')

        with tooltip(f'Leader_Efficacy_Value_Changer_Text_{card}', tag=f'Leader_Efficacy_Value_Changer_Tooltip_{card}'):
            add_text('Type what percent you want the leader skill to use')

    add_input_text(default_value='', tag=f'Leader_Name_Text_Input_{card}',hint='Name', width=String_Length.length[0], callback=Leader_Resize, parent=f'Leader_Skill_{card}')
    add_input_text(default_value='', tag=f'Leader_Desc_Text_Input_{card}',hint='Description', width=265, callback=Resize_Widget, parent=f'Leader_Skill_{card}', multiline=True)

    Leader_Skill_Info.rows = 1
    Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                    use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=66, table_width=867)
    set_item_height(f'Leader_Skill_Table_{card}', (24 * (Leader_Skill_Info.rows)) + 23)
    configure_item(f'Leader_Skill_{card}', show=True)
    
    
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Widgets_Group_{card}_1')    
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Widgets_Group_{card}_2')    
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Text_{card}')        
    Widget_Aliases.tags_to_delete.append(f'Leader_Skill_Preset_List_{card}')        
    Widget_Aliases.tags_to_delete.append(f'Leader_Name_Text_Input_{card}')        
    Widget_Aliases.tags_to_delete.append(f'Leader_Desc_Text_Input_{card}')   
    Widget_Aliases.tags_to_delete.append(f'Leader_Efficacy_Value_Changer_{card}')   
    Widget_Aliases.tags_to_delete.append(f'Leader_Efficacy_Value_Changer_Text_{card}')   
    Widget_Aliases.tags_to_delete.append(f'Leader_Efficacy_Value_Changer_Tooltip_{card}')   
    
########################################################################################################################################################################################################
def Custom_Unit_Leader_Skill_Query(*, card=0):
    try:
        card = card

        if not Card_Checks.json_data[0]:
            data = load_JSON(f'jsons/{card_id}.json')
        else:
            data = Card_Checks.json_data[0]

        leader_skill = data['leader_skill']
        leader_skill_id = leader_skill['id']
        leader_skill_name = leader_skill['name']
        leader_skill_description = leader_skill['description']
        leader_skills_data : list[dict[str, str]] = leader_skill['skills']

        set_value(f'Custom_Unit_Leader_Skill_Checkbox_{card}', True)
        # Add a set_value for leader skill rows

        
        # Removes any lingering rows should there be a preset selected upon query
        # for i in range(Leader_Skill_Info.rows):
            # if does_alias_exist(f'l_exec_timing_type_{i}'):
                # for z in range(len(Leader_Skill_Info.input_text_widgets)):
                    # delete_item(Leader_Skill_Info.input_text_widgets[z] + str(i))
        # set_value('Leader_Skill_Preset_List_0', 'Presets')
        # set_item_width('Leader_Skill_Preset_List_0', String_Length.length[9])
        
        if card != 0:
            Leader_Skill_Widgets(card)
        Leader_Skill_Info.rows = len(leader_skills_data)
        Leader_Skill_tags = Table_Inputs(table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info,
                        use_child_window=False, table_parent=f'Leader_Skill_{card}', transformation=True, transformation_card_num=card, table_height=66, table_width=753)
        # print(Leader_Skill_tags)
        
        Leader_Skill_Set_Values(leader_skills_data, card=card)

        set_value(f'Leader_Name_Text_Input_{card}', leader_skill_name)
        set_value(f'Leader_Desc_Text_Input_{card}', leader_skill_description)
        width, height = get_text_size(f'Leader_Desc_Text_Input_{card}', font='fonts/ARIAL.tff')
        newline_count = leader_skill_description.count('\n')
        # if newline_count == 0:
        # set_item_height(f'Leader_Desc_Text_Input_{card}', 16.5)
        # else:
        set_item_height(f'Leader_Desc_Text_Input_{card}', 14.5 * newline_count + 20)

        Text_Resize(f'Leader_Name_Text_Input_{card}')
        Text_Resize(f'Leader_Desc_Text_Input_{card}')


        # set_value('Leader_Skill_Rows', len(leader_info))
        set_item_height(f'Leader_Skill_Table_{card}', (24 * len(leader_skills_data)) + 23)
        
        # Part of the category combo callbacks. Grabbing the index of the matching categories strings, as the list is in a specific order. Ex. "DB Saga" Category ID isn't 0 but it's index is.
        category_index_list = []
        leader_skill_description = get_value(f'Leader_Desc_Text_Input_{card}')
        category_combos = Row_Checker(f'Leader_Skill_Category_Selection_{card}_')
        # print(category_combos)
        
        matches = re.findall(r'"(.*?)"', leader_skill_description)
        for z in range(len(matches)):
            category_index_list.append(next((i for i, category in enumerate(Leader_Skill_Info.cat_list) if matches[z] in category), None))
        
        if len(matches) > 5:
            matches = list(set(matches))
            ### Set to 6 just so the bottom section works correctly
            category_combos = 6
        # print(matches)
        for t in range(len(matches) - 1):
            add_combo(Leader_Skill_Info.cat_list, default_value='Categories', tag=f'Leader_Skill_Category_Selection_{card}_{t + 1}', width=String_Length.length[11], callback=Leader_Cat_Selection, parent=f'Leader_Skill_Widgets_Group_{card}_1')
            bind_item_font(f'Leader_Skill_Category_Selection_{card}_{t + 1}', font='fonts/ARIALBD.ttf')
            
        for i in range(len(matches)):
            # print(Leader_Skill_Info.cat_list[category_index_list[i]])
            set_value(f'Leader_Skill_Category_Selection_{card}_{i}', Leader_Skill_Info.cat_list[category_index_list[i]])
            Text_Resize(f'Leader_Skill_Category_Selection_{card}_{i}')
        
        def Reset_Sub_Target_Rows():
            for i in range(Leader_Skill_Info.rows):
                set_value(Leader_Skill_Info.row_names[3] + '_Card_' + str(card) + '_Row_' + str(i), '0')
        
        if Card_Checks.leader_skill_type == '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)':
            add_combo(['Extreme Class', 'Super Class'], default_value='Extreme Class', tag=f'Leader_Skill_Category_Selection_{card}_5', width=String_Length.length[11], callback=Leader_Cat_Selection, parent=f'Leader_Skill_Widgets_Group_{card}_1')
            
            if 'Super Class' in get_value(f'Leader_Desc_Text_Input_{card}'):
                set_value(f'Leader_Skill_Category_Selection_{card}_5', 'Super Class')
            else:
                set_value(f'Leader_Skill_Category_Selection_{card}_5', 'Extreme Class')
                
            set_value(f'Leader_Skill_Preset_List_{card}', '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            Text_Resize(f'Leader_Skill_Category_Selection_{card}_5')
            
        elif Card_Checks.leader_skill_type == '3 Categories & 2 Extra':
            set_value(f'Leader_Skill_Preset_List_{card}', '3 Categories & 2 Extra')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            
        elif Card_Checks.leader_skill_type == '2 Categories & 2 Extra':
            set_value(f'Leader_Skill_Preset_List_{card}', '2 Categories & 2 Extra')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            
        elif Card_Checks.leader_skill_type == '2 Categories & 1 Extra':
            set_value(f'Leader_Skill_Preset_List_{card}', '2 Categories & 1 Extra')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            
        elif Card_Checks.leader_skill_type == '2 Categories':
            set_value(f'Leader_Skill_Preset_List_{card}', '2 Categories')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            
        elif Card_Checks.leader_skill_type == '1 Category & 1 Element':
            set_value(f'Leader_Skill_Preset_List_{card}', '1 Category & 1 Element')
            if does_alias_exist(Leader_Skill_Info.row_names[3] + str(card) + '4'):
                set_value(Leader_Skill_Info.row_names[3] + '_Card_' + str(card) + '_Row_' + '4', '0')
            combo = ['Super AGL (4096)', 'Super TEQ (8192)', 'Super INT (16384)', 'Super STR (32768)', 'Super PHY (65536)', 'Extreme AGL (131072)', 'Extreme TEQ (262144)', 'Extreme INT (524288)', 'Extreme STR (1048576)', 'Extreme PHY (2097512)','AGL (0)', 'TEQ (1)', 'INT (2)', 'STR (3)', 'PHY (4)']
            result_dict = {re.search(r'\((\d+)\)', item).group(1): item for item in combo}
            element_bitset = ast.literal_eval(get_value(Leader_Skill_Info.row_names[5] + '_Card_' + str(card) + '_Row_' + '0'))[0]
            Leader_Create_Combos(custom_combo=combo, num_of_combos=2, custom_combo_default_value='INT (2)',custom_combo_num=[2], custom_combo_callback=Leader_Ki_Selection)
            
            ### Getting the first category and setting the category combo to it.
            extracted_text = re.findall(r'"([^"]*)"', get_value(f'Leader_Desc_Text_Input_{card}'))

            # Print the extracted text
            for text in extracted_text:
                text = text
            index_value = ''
            
            for items in range(len(Leader_Skill_Info.cat_list)):
                if text in Leader_Skill_Info.cat_list[items]:
                    index_value = Leader_Skill_Info.cat_list[items]
                    break
                
            ### Getting Efficacy_Values from leader skill, converting to a list to grab the first index,
            ### then setting it to the combo value later using result_dict
            element_type = get_value(Leader_Skill_Info.row_names[5] + '_Card_' + str(card) + '_Row_' + '2')
            element_type_list = ast.literal_eval(element_type)
            element_type = element_type_list[0]
            
            
            set_value(f'Leader_Skill_Category_Selection_{card}_0', index_value)
            Text_Resize(f'Leader_Skill_Category_Selection_{card}_0')
            try:
                set_value(f'Leader_Skill_Category_Selection_{card}_1', result_dict[str(element_type)])
            except KeyError:
                set_value('log_1', 'Leader Skill Not a Preset, can ignore or modify the leader skill')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            Text_Resize(f'Leader_Skill_Category_Selection_{card}_1')
            
        elif Card_Checks.leader_skill_type == '1 Category':
            set_value(f'Leader_Skill_Preset_List_{card}', '1 Category')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            
        elif Card_Checks.leader_skill_type == 'Super Class':
            set_value(f'Leader_Skill_Preset_List_{card}', 'Super Class')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            Reset_Sub_Target_Rows()
            Delete_Items(f'Leader_Skill_Category_Selection_{card}_0')
            
        elif Card_Checks.leader_skill_type == 'Extreme Class':
            set_value(f'Leader_Skill_Preset_List_{card}', 'Extreme Class')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            Reset_Sub_Target_Rows()
            Delete_Items(f'Leader_Skill_Category_Selection_{card}_0')
            
        ### Uses ast to turn the efficacy values into a list, then checks the first index; being the element bitset
        elif Card_Checks.leader_skill_type == 'Element Type':
            set_value(f'Leader_Skill_Preset_List_{card}', 'Element Type')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            Reset_Sub_Target_Rows()
            combo = ['AGL (0)', 'TEQ (1)', 'INT (2)', 'STR (3)', 'PHY (4)', 'Super AGL (4096)', 'Super TEQ (8192)', 'Super INT (16384)', 'Super STR (32768)', 'Super PHY (65536)', 'Extreme AGL (131072)', 'Extreme TEQ (262144)', 'Extreme INT (524288)', 'Extreme STR (1048576)', 'Extreme PHY (2097512)']
            # result_dict = {re.search(r'\((\d+)\)', item).group(1): item for item in combo}
            # element_bitset = ast.literal_eval(get_value(Leader_Skill_Info.row_names[5] + '_Card_' + str(card) + '_Row_' + '0'))[0]
            Delete_Items(f'Leader_Skill_Category_Selection_{card}_0')
            add_combo(combo, default_value='TEQ', tag=f'Leader_Skill_Category_Selection_{card}_0', width=String_Length.length[11], callback=Leader_Ki_Selection, parent=f'Leader_Skill_Widgets_Group_{card}_1')
            set_value(f'Leader_Skill_Category_Selection_{card}_0', Card_Checks.leader_skill_element_type)
            Text_Resize(f'Leader_Skill_Category_Selection_{card}_0')
            
        else: ### All Types
            set_value(f'Leader_Skill_Preset_List_{card}', 'All Types')
            Text_Resize(f'Leader_Skill_Preset_List_{card}')
            Reset_Sub_Target_Rows()
            
        for i in range(6):
            if does_alias_exist(f'Leader_Skill_Category_Selection_{card}_{i}'):
                width, height = get_text_size(get_value(f'Leader_Skill_Category_Selection_{card}_{i}'), font='fonts/ARIAL.ttf')
                set_item_width(f'Leader_Skill_Category_Selection_{card}_{i}', width + 28)
                
        Text_Resize_2(f'Leader_Skill_Preset_List_{card}')
        Resize_Table_Width(card, Leader_Skill_Info, Leader_Skill_Info.rows, f'Leader_Skill_Table_{card}')

        # Shitty fix to replace any 0 causality conditions with NULL to prevent crashes in game
        for i in range(Leader_Skill_Info.rows):
            if get_value(f'l_causality_conditions_Card_{card}_Row_{i}') == '0':
                set_value(f'l_causality_conditions_Card_{card}_Row_{i}', 'NULL')

    except Exception as e:
        log_data = Traceback_Logging(e)
        
        with open('error_log.txt', 'w') as file:
            file.write(f'Exception Type: {log_data}')
        set_value('log_1', 'Error when querying Leader Skill, error_log.txt created with more information\nMay require manually modifying parts of the Leader Skill')

########################################################################################################################################################################################################                  
def Widgets_Combined():
    Custom_Unit_Card_Thumb_Display()
    Card_Widgets()
    Passive_Widgets()
    Specials_Widgets()
    if Custom_Unit.card_number == 0:
        Leader_Skill_Widgets('0')
    
########################################################################################################################################################################################################
    
def Custom_Unit_Hide_Tabs():
    configure_item('Active_Skill_Card_0', show=False)
    configure_item('Standby_Skill_0', show=False)
    configure_item('Finish_Skill_0', show=False)
    configure_item('Dokkan_Field_0', show=False)
    configure_item('Battle_Params_0', show=False)

def Set_Main_Card_ID(sender, data):
    print(sender)
    set_value('Card ID', data)
########################################################################################################################################################################################################                  
def Custom_Unit_Selectables(*, card=0):
    Delete_Items([f'Custom_Selectables_Group_{card}', f'Selectable_Child_Window_{card}', f'Custom_Unit_Leader_Skill_Checkbox_{card}', f'Custom_Unit_Active_Skill_Checkbox_{card}',
                  f'Custom_Unit_Standby_Skill_Checkbox_{card}', f'Custom_Unit_Finish_Skill_Checkbox_{card}', f'Custom_Unit_Dokkan_Field_Checkbox_{card}', f'Custom_Unit_Battle_Params_Checkbox_{card}'])
    
    with group(tag=f'Custom_Selectables_Group_{card}', horizontal=True, parent=f'Custom_Unit_Checkbox_Group_Horizontal_False_{card}'):

        with child_window(label='Selectable_Child_Window', tag=f'Selectable_Child_Window_{card}', width=95, height=156, parent=f'Card_Input_Image_Widget_Group_{card}'):
            if card == 0:
                add_selectable(label='Leader Skill', callback=Custom_Unit_Leader_Skill_Checkbox, tag=f'Custom_Unit_Leader_Skill_Checkbox_{card}', width=80, default_value=True)
            else:
                add_selectable(label='Leader Skill', callback=Custom_Unit_Leader_Skill_Checkbox, tag=f'Custom_Unit_Leader_Skill_Checkbox_{card}', width=80, default_value=False)
            add_selectable(label='Active Skill', callback=Custom_Unit_Active_Skill_Checkbox, tag=f'Custom_Unit_Active_Skill_Checkbox_{card}', width=80)
            add_selectable(label='Standby Skill', callback=Custom_Unit_Standby_Skill_Checkbox, tag=f'Custom_Unit_Standby_Skill_Checkbox_{card}', width=80)
            add_selectable(label='Finish Skill', callback=Custom_Unit_Finish_Skill_Checkbox, tag=f'Custom_Unit_Finish_Skill_Checkbox_{card}', width=80)
            add_selectable(label='Dokkan Field', callback=Custom_Unit_Dokkan_Field_Checkbox, tag=f'Custom_Unit_Dokkan_Field_Checkbox_{card}', width=80)
            add_selectable(label='Battle Params', callback=Custom_Unit_Battle_Params_Checkbox, tag=f'Custom_Unit_Battle_Params_Checkbox_{card}', width=80)
            add_selectable(label='Effect Packs', callback=Custom_Unit_Effect_Packs_Checkbox, tag=f'Custom_Unit_Effect_Packs_Checkbox_{card}', width=80)
            add_selectable(label='Special Views', callback=Custom_Unit_Special_Views_Checkbox, tag=f'Custom_Unit_Special_Views_Checkbox_{card}', width=80)
        bind_item_theme(f'Selectable_Child_Window_{card}','Custom_Unit_Selectable_Theme')
        Widget_Aliases.tags_to_delete.append(f'Selectable_Child_Window_{card}')
        Widget_Aliases.tags_to_delete.append(f'Custom_Unit_Leader_Skill_Checkbox_{card}')
        Widget_Aliases.tags_to_delete.append(f'Custom_Unit_Active_Skill_Checkbox_{card}')
        Widget_Aliases.tags_to_delete.append(f'Custom_Unit_Standby_Skill_Checkbox_{card}')
        Widget_Aliases.tags_to_delete.append(f'Custom_Unit_Finish_Skill_Checkbox_{card}')
        Widget_Aliases.tags_to_delete.append(f'Custom_Unit_Dokkan_Field_Checkbox_{card}')
        Widget_Aliases.tags_to_delete.append(f'Custom_Unit_Battle_Params_Checkbox_{card}')
        Widget_Aliases.tags_to_delete.append(f'Custom_Unit_Effect_Packs_Checkbox_{card}')
    if card > 0:
        with group(horizontal=False, tag=f'Custom_Query_Widget_Group_{card}', parent=f'Custom_Unit_Checkbox_Group_Horizontal_True_{card}'):
            add_input_text(tag=f'Custom_Query_Text_Input_{card}', width=90, callback=Set_Main_Card_ID)
            add_button(label='Custom Query', tag=f'Custom_Query_Button_{card}', callback=Custom_Query_Window)
        
        

        
    if card > 0:
        set_item_height(f'Selectable_Child_Window_{card}', 156)

########################################################################################################################################################################################################
def Custom_Unit_Leader_Skill_Checkbox(app_data, data):
    card = Table_ID(app_data)
    tags_to_delete = [f'Leader_Skill_Widgets_Group_{card}_1', f'Leader_Skill_Widgets_Group_{card}_2',f'Leader_Efficacy_Value_Changer_Tooltip_{card}', f'Leader_Efficacy_Value_Changer_Text_{card}',
                      f'Leader_Efficacy_Value_Changer_{card}',  f'Leader_Skill_Text_{card}', f'Leader_Skill_Preset_List_{card}', f'Leader_Name_Text_Input_{card}', f'Leader_Desc_Text_Input_{card}']
    if data:
        Leader_Skill_Widgets(card)
    else:
        Delete_Items(tags_to_delete)
        Delete_Table(card, table_name=f'Leader_Skill_Table_{card}', row_name=f'Leader_Skill_Row_{card}_', class_name=Leader_Skill_Info)
        configure_item(f'Leader_Skill_{card}', show=False)

########################################################################################################################################################################################################
def Custom_Unit_Ultimate_Special_Checkbox(app_data, data):
    card = Table_ID(app_data)
    if data:
        Ultimate_Special_Widgets(card)
    else:
        Delete_Items(f'Ultimate_Special_Separator_Card_{card}')
        Delete_Items(f'Ultimate_Special_Text_Card_{card}')
        Delete_Items(f'Ultimate_Special_Group_Card_{card}')
        for u in range(len(Active_Skill.ultimate_names)):
            Delete_Items(Active_Skill.ultimate_hints[u] + '_Card_' + str(card) + '_Text')
            Delete_Items(Active_Skill.ultimate_names[u] + '_Card_' + str(card))

########################################################################################################################################################################################################
def Custom_Unit_Active_Skill_Checkbox(app_data, data):
    card = Table_ID(app_data)
    
    tags_to_delete = [f'Active_Skill_Text_Card_{card}', f'Active_Skill_Name_Text_Card_{card}', f'Active_Skill_Desc_Text_Card_{card}', f'Active_Skill_Cond_Text_Card_{card}',
                      f'Active_Name_Card_{card}', f'Active_Desc_Card_{card}', f'Active_Cond_Card_{card}', f'Active_Skill_Separator_Card_{card}', f'Active_Skill_Group_1_Card_{card}',
                      f'Active_Skill_Group_2_Card_{card}', f'Active_Skill_Group_3_Card_{card}', f'Active_Skill_Group_4_Card_{card}', f'Active_Skill_Text_Card_{card}',
                      f'Active_Skill_Name_Text_Card_{card}', f'Active_Skill_Desc_Text_Card_{card}', f'Active_Skill_Cond_Text_Card_{card}', f'Active_Name_Card_{card}',
                      f'Active_Desc_Card_{card}', f'Active_Cond_Card_{card}', f'Active_Skill_Separator_Card_{card}', f'Active_Skill_Group_1_Card_{card}',
                      f'Active_Skill_Group_2_Card_{card}', f'Active_Skill_Group_3_Card_{card}', f'Active_Skill_Group_4_Card_{card}', f'Active_Skills_Group_Card_{card}',
                      f'Active_Skills_Text_Card_{card}', f'Active_Skills_Button_Add_Card_{card}', f'Active_Skills_Button_Del_Card_{card}']
    if data:
        Active_Skill_Widgets(card)
    else:
        Delete_Items(tags_to_delete)
        Delete_Items(f'Custom_Unit_Ultimate_Special_Checkbox_{card}')
        Delete_Table(card, table_name=f'Active_Skill_Table_Card_{card}', row_name=f'Active_Skill_Set_Row_Card_{card}_', class_name=Active_Skill)
        Delete_Table(card, table_name=f'Active_Skill_Set_Card_{card}', row_name=f'Active_Skill_Row_Card_{card}_', class_name=Active_Skill_Set)
        configure_item(f'Active_Skill_Card_{card}', show=False)
        
########################################################################################################################################################################################################
def Custom_Unit_Standby_Skill_Checkbox(app_data, data):
    card = Table_ID(app_data)
    tags_to_delete = [f'Standby_Skill_Set_Text_{card}_0', f'Standby_Skill_Set_Group_1_{card}_0', f'Standby_Skill_Name_Text_{card}_0', f'Standby_Set_Name_Input_Text_{card}_0',
                      f'Standby_Skill_Set_Group_2_{card}_0', f'Standby_Skill_Desc_Text_{card}_0', f'Standby_Set_Desc_Input_Text_{card}_0', f'Standby_Skill_Set_Group_3_{card}_0',
                      f'Standby_Skill_Cond_Text_{card}_0', f'Standby_Set_Cond_Input_Text_{card}_0', f'Standby_Skill_Set_Separator_{card}_0', f'Standby_Skill_Text_{card}_0']
    
    if data:
        Standby_Skill_Widgets(card)
    else:
        Delete_Items(tags_to_delete)
        Delete_Table(card, table_name=f'Standby_Skill_Set_Table_{card}_0', row_name=f'Standby_Skill_Set_Table_Row_{card}_0', class_name=Standby_Skill_Set)
        Delete_Table(card, table_name=f'Standby_Skill_Table_{card}_0', row_name=f'Standby_Skill_Table_Row_{card}_0', class_name=Standby_Skill)
        configure_item(f'Standby_Skill_{card}', show=False)

########################################################################################################################################################################################################      
def Custom_Unit_Finish_Skill_Checkbox(app_data, data):
    card = Table_ID(app_data)
    tags_to_delete = [f'Finish_Skill_Set_Text_{card}_0', f'Finish_Skill_Set_Group_{card}_0', f'Finish_Skill_Set_Name_{card}_0', f'Finish_Set_Name_{card}_0',
                      f'Finish_Skill_Desc_Group_{card}_0', f'Finish_Skill_Set_Desc_{card}_0', f'Finish_Set_Desc_{card}_0', f'Finish_Skill_Cond_Group_{card}_0',
                      f'Finish_Skill_Set_Cond_{card}_0', f'Finish_Set_Cond_{card}_0', f'Finish_Skill_Skill_Text_{card}_0']
    
    if data:
        Custom_Unit_Finish_Skill_Set_Widgets(card)
    else:
        Delete_Items(tags_to_delete)
        Delete_Table(card, table_name=f'Finish_Skill_Set_Table_{card}_0', row_name=f'Finish_Skill_Set_Table_Row_{card}_0', class_name=Finish_Skill_Set)
        Delete_Table(card, table_name=f'Finish_Skill_Table_{card}_0', row_name=f'Finish_Skill_Table_Row_{card}_0', class_name=Finish_Skill)
        configure_item(f'Finish_Skill_{card}', show=False)

########################################################################################################################################################################################################
def Custom_Unit_Dokkan_Field_Checkbox(app_data, data):
    card = Table_ID(app_data)
    tags_to_delete = [f'Dokkan_Field_Text_{card}_0', f'Dokkan_Field_Name_Input_Text_{card}_0', f'Dokkan_Field_Desc_Input_Text_{card}_0', f'Dokkan_Field_Resource_ID_{card}_0',
                      f'Dokkan_Field_Name_Text_Group_{card}_0', f'Dokkan_Field_Desc_Text_Group_{card}_0', f'Dokkan_Field_Resource_Text_Group_{card}_0', f'Dokkan_Field_Name_Text_{card}_0',
                      f'Dokkan_Field_Desc_Text_{card}_0', f'Dokkan_Field_Resource_Text_{card}_0', f'Dokkan_Field_Checkbox_Group_{card}_0', f'Link_to_Active_Button_{card}_0',
                      f'Link_to_Passive_Button_{card}_0', f'Dokkan_Field_Separtor_2_{card}_0', f'Dokkan_Field_Separtor_1_{card}_0']
                     
    if data:
        Dokkan_Field_Widgets(card)
    else:
        Delete_Items(tags_to_delete)
        Delete_Table(card, table_name=f'Dokkan_Field_Table_{card}_0', row_name=f'Dokkan_Field_Table_Row_{card}_0', class_name=Dokkan_Field)
        configure_item(f'Dokkan_Field_{card}', show=False)
        
########################################################################################################################################################################################################
def Custom_Unit_Battle_Params_Checkbox(app_data, data):
    card = Table_ID(app_data)
    tags_to_delete = [f'Transformation_Information_Text_{card}', f'Transformation_Descriptions_Table_Separator_{card}', f'Battle_Params_Text_{card}']
                     
    if data:
        Battle_Params_Widgets(card)
    else:
        Delete_Items(tags_to_delete)
        Delete_Table(card, table_name=f'Transformation_Descriptions_Table_{card}', row_name=f'Transformation_Descriptions_Table_Row_{card}', class_name=Transformation_Descriptions)
        Delete_Table(card, table_name=f'Battle_Params_Table_{card}_0', row_name=f'Battle_Params_Table_Row_{card}_0', class_name=Battle_Params)
        configure_item(f'Battle_Params_{card}', show=False)
         
########################################################################################################################################################################################################
def Custom_Unit_Effect_Packs_Checkbox(app_data, data):
    card = Table_ID(app_data)
                     
    if data:
        Effect_Packs_Widgets(card)
    else:
        Delete_Table(card, table_name=f'Effect_Packs_Table_{card}', row_name=f'Effect_Packs_Table_Row_{card}', class_name=Effect_Pack)
        configure_item(f'Effect_Packs_{card}', show=False)
         
########################################################################################################################################################################################################
def Custom_Unit_Special_Views_Checkbox(app_data, data):
    card = Table_ID(app_data)
                     
    if data:
        Special_View_Widgets(card)
    else:
        Delete_Table(card, table_name=f'Special_Views_Table_{card}', row_name=f'Special_Views_Table_Row_{card}', class_name=Special_Views)
        configure_item(f'Special_Views_{card}', show=False)
         
