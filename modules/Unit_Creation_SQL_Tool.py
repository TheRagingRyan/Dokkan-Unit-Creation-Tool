from dearpygui.dearpygui import *
from . classes import Card_Checks, Card, Widget_Aliases, Themes, Custom_Unit, Handler_Key
from . configs import Database_Selector
from . download import Lua_Downloader
from . discord import Discord_Presence_Menu, Discord_Server
from modules import RPC
from . categories import  Category_jp_id_List, Load_Category_Images, Card_Categories_Window
from . causality import Causality_Creator
from . functions import Delete_Items, Thumb_Display, Clear_Class_Tags_List, Allow_Use_Check, Dokkan_Wiki, Table_ID
import pyautogui
from . specials import Specials_Widgets
from . Json_file import JSON_Save, JSON_Load
from . custom_unit import Export_as_SQL, download_callback, get_card_id, save_callback, Widgets_Combined, Custom_Unit_Selectables, Custom_Unit_Hide_Tabs, Custom_Query_Window, Thumb_Test, Set_Main_Card_ID, Card_Widgets, Passive_Widgets, Leader_Skill_Widgets, Main_Tab_Bar_Callback



    
############################################################################################################
################################################## MAIN ####################################################
############################################################################################################
def main():
    
    screen_width, screen_height = pyautogui.size()
    
    def Custom_Unit_Checkbox(sender, data):
        def Confirmation_Window_Callback(tag_id):
            tags_to_delete = ['Confirmation_Window', 'Confirmation_Text', 'Confirmation_Button_Yes', 'Confirmation_Button_No', 'Confirmation_Button_Group']
            if tag_id == 'Confirmation_Button_Yes':
                Delete_Items(tags_to_delete)
                if len(Widget_Aliases.tags_to_delete) > 0:
                    Delete_Items(Widget_Aliases.tags_to_delete)
                    Widget_Aliases.tags_to_delete.clear()
                    Clear_Class_Tags_List()
                set_value('Custom_Unit_0', False)
                
                    
            else:
                set_value('Custom_Unit_0', True)
                Delete_Items(tags_to_delete)
                
        log_1 = 'Custom Unit Selected'
        set_value('log_1', log_1)
        
        if get_value(Card.row_names[0] + '_Card_0_Row_0'):
            set_value('Custom_Unit_0', True)
            with window(label='Warning', width=235, height=100, tag='Confirmation_Window', pos=[250, 250]):
                add_text(tag='Confirmation_Text', default_value='Are you sure you want to continue?\n(Doing so will delete all data)', color=(255, 0, 0))
                with group(horizontal=True, tag='Confirmation_Button_Group'):
                    add_button(tag='Confirmation_Button_Yes',label='Yes', callback=Confirmation_Window_Callback)
                    add_button(tag='Confirmation_Button_No',label='No', callback=Confirmation_Window_Callback)
                    bind_item_theme('Confirmation_Button_Yes','Confirmation_Button_Yes_Theme')
                    bind_item_theme('Confirmation_Button_No','Confirmation_Button_No_Theme')
        else:
            # Wipes the GUI clean should there be widgets from previous queries
            if len(Widget_Aliases.tags_to_delete) > 0:
                Delete_Items(Widget_Aliases.tags_to_delete)
                Widget_Aliases.tags_to_delete.clear()
                Clear_Class_Tags_List()
            
        # Add stuff for Custom Units here
        if data:
            configure_item('Main_Card_Tab_0', label='Main Card')
            Thumb_Display('0', False)
            Card_Checks.card_ids.clear()
            Card_Checks.card_ids.append('0')
            add_tab_button(tag=f'Add_Card_Tab', label='+', parent='Main_Tab_Bar', callback=Main_Tab_Bar_Callback, trailing=True)
            Custom_Unit_Hide_Tabs()
            Custom_Unit_Selectables()
            Widgets_Combined()
        else:
            Delete_Items(f'Add_Card_Tab')
            
    #############################################################################################################
    create_context()
    # show_debug()
    # show_style_editor()
    # show_imgui_demo()
    # show_font_manager()
    create_viewport(title='Unit Creation SQL Tool', width=screen_width - 300, height=screen_height - 300, x_pos=0, y_pos=0, clear_color=(0, 0, 0, 255), vsync=True, small_icon='logo/logo.ico', large_icon='logo/logo.ico')
    # set_viewport_vsync(True)
    
    #############################################################################################################    
    with font_registry():
        Arial_font = add_font('fonts/ARIAL.ttf', size=14, tag='Arial_Font')
        Nishi_font = add_font('fonts/NishikiTeki-MVxaJ.ttf', size=14)
        Arialbold_font = add_font('fonts/ARIALBD.ttf', size=14)
        Arialbold_Card_Name = add_font('fonts/ARIALBD.ttf', size=24, tag='Arial_Bold_Font')
        Arial_font_pass_desc = add_font('fonts/ARIAL.ttf', size=16)

    #############################################################################################################
    jp_categories_id_list = Category_jp_id_List()
    # Come back an clean this up since I can just delete existing values or update them if the alias exists
    int_values = ['Passive_Row_Check', 'Card_Rarity', 'Number_Of_Special_Sets', 'card_categories_rows', 'Image_State_Check', 'Lua_alias_to_remove', 'Query_Index_Number']
    string_values = ['Special_View_IDs', 'CardID0', 'CardID1', 'CardName', 'Special_View_ID_1', 'Special_View_ID_2', 'Special_View_ID_3', 'Leader_Name', 'Leader_Desc', 
                     'Leader_Skill_ID', 'Active_Skill_Name', 'Active_Skill_Desc', 'Active_Skill_Cond', 'Standby_Skill_Set_Name', 'Standby_Skill_Set_Desc', 'Standby_Skill_Set_Cond',
                     'Ultimate_Special_ID', 'Standby_Skill_ID', 'Passive_Skill_ID', 'Passive_Desc', 'Passive_Name']
    bool_values = ['EZA_Check', 'Transformation_Check', 'Standby_Skill_Check', 'Finish_Skill_Check', 'Active_Skill_Check', 'Ultimate_Special_Check', 'Translation_Good']
    with value_registry():
        for i in range(len(int_values)):
            add_int_value(default_value=0, tag=int_values[i])
        for i in range(len(string_values)):
            add_string_value(default_value='', tag=string_values[i])
            
        #Check for card region
        add_bool_value(default_value=True, tag='ENG_Check')
        
        for i in range(len(bool_values)):
            add_bool_value(default_value=False, tag=bool_values[i])
        
        for i in range(len(jp_categories_id_list)):
            add_int_value(default_value=0, tag=f'Image_State_Check_{jp_categories_id_list[i]}')

    with texture_registry():
        width, height, channels, data = load_image('logo/Add_Image.png')
        add_dynamic_texture(width=250, height=250, default_value=data, tag='Placeholder_Image_Texture_0')
        # width, height, channels, data = load_image('logo/Add_Image.png')
        # add_dynamic_texture(width=250, height=250, default_value=data, tag='Add_Image_Texture_0')
        width, height, channels, data = load_image('logo/Custom_Border_Border_AGL.png')
        add_dynamic_texture(width=250, height=250, default_value=data, tag='Custom_Border_Thumb_Border_Texture_0')
        width, height, channels, data = load_image('logo/Custom_Border_Background_AGL.png')
        add_dynamic_texture(width=250, height=250, default_value=data, tag='Custom_Border_Thumb_Background_Texture_0')
        width, height, channels, data = load_image('logo/Placeholder.png')
        add_dynamic_texture(width=250, height=250, default_value=data, tag='Card_Thumb_Texture_0')
        width, height, channels, data = load_image('categories/Category_1_off.png')
        add_dynamic_texture(width=273, height=65, default_value=data, tag='button_test_image_off')
        width, height, channels, data = load_image('categories/Category_1_on.png')
        add_dynamic_texture(width=273, height=65, default_value=data, tag='button_test_image_on')
    Load_Category_Images()
    

    ############################################################################################################
    ################################################## Themes ##################################################
    ############################################################################################################

    with theme() as global_theme:

        with theme_component(mvAll):
            add_theme_color(mvThemeCol_FrameBg, (50, 50, 50), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_Text, (255, 215, 0), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_TextDisabled, (10, 10, 0, 20), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_TitleBgActive, (10, 10, 10), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_TabActive, (124,140,146,99), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_CheckMark, (255, 215, 0), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_TableHeaderBg, (0, 0, 0, 60), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_Button, (124,140,146,99), category=mvThemeCat_Core)

            add_theme_style(mvStyleVar_FrameRounding, 5, category=mvThemeCat_Core)   

        with theme_component(mvInputInt):
            add_theme_color(mvThemeCol_FrameBg, (37, 37, 37), category=mvThemeCat_Core)
            add_theme_style(mvStyleVar_FrameRounding, 5, category=mvThemeCat_Core)


    ############################################################################################################ 
    
    with theme(tag='Category_Button_Theme') as category_buttons:

        with theme_component(mvAll):

            add_theme_color(mvThemeCol_Button, (37, 37, 38), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_ButtonHovered, (37, 37, 38), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_ButtonActive, (37, 37, 38), category=mvThemeCat_Core)
        with theme_component(mvInputInt):
            add_theme_color(mvThemeCol_Text, (255, 174, 26), category=mvThemeCat_Core)
    Themes.Buttons = category_buttons

    ############################################################################################################
    with theme() as detected_skills:

        with theme_component(mvAll):

            add_theme_color(mvThemeCol_Tab, (51, 153, 63, 161), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_TabActive, (0, 200, 71, 68), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_TabHovered, (69, 81, 90, 103), category=mvThemeCat_Core)
    
    with theme(tag='Selectable_Theme'):
      with theme_component(mvAll):
            add_theme_color(mvThemeCol_Header, (37, 37, 38), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_HeaderActive, (37, 37, 38), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_HeaderHovered, (37, 37, 38, 0), category=mvThemeCat_Core)
            
    with theme(tag='Custom_Unit_Selectable_Theme'):
      with theme_component(mvAll):
            add_theme_color(mvThemeCol_Header, (255, 132, 0, 100), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_HeaderActive, (255, 174, 26), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_HeaderHovered, (255, 255, 255, 75), category=mvThemeCat_Core)
            
    with theme(tag='log_theme'):
      with theme_component(mvAll):
          add_theme_color(mvThemeCol_Text, (255, 174, 26), category=mvThemeCat_Core)
          
    with theme(tag='Confirmation_Button_Yes_Theme'):
      with theme_component(mvAll):
          add_theme_color(mvThemeCol_Text, (255, 0, 0), category=mvThemeCat_Core)
          
    with theme(tag='Confirmation_Button_No_Theme'):
      with theme_component(mvAll):
          add_theme_color(mvThemeCol_Text, (0, 255, 0), category=mvThemeCat_Core)
          
    with theme(tag='Red_Text'):
      with theme_component(mvAll):
          add_theme_color(mvThemeCol_Text, (255, 0, 0), category=mvThemeCat_Core)
        
    ############################################################################################################
    ### Handler functions
    def print_window_size(sender,user_data,app_data):


        window_size = user_data
        pos_x = window_size[3] / 70
        pos_y = window_size[1] - 75
        # set_item_pos('log_1',(pos_x, pos_y) )
        
    def handler_callback(sender, data):
        
        if Handler_Key.last_key == 17 and data == 83:
            JSON_Save()
        elif Handler_Key.last_key == 17 and data == 76:
            JSON_Load()
        Handler_Key.last_key = 0
        Handler_Key.last_key = data
        
    def Tab_Delete(data, sender):
        delete_item(sender[1])
        Custom_Unit.card_number -= 1
    
    with item_handler_registry(tag='Tab_Handler'):
        add_item_clicked_handler(button=mvMouseButton_Middle, callback=Tab_Delete)
        

    with item_handler_registry(tag='widget_handler') as handler:
        add_item_resize_handler(callback=print_window_size)
        
    with handler_registry():
        # add_key_press_handler(key=ord('S'), callback=JSON_Save)
        # add_key_press_handler(key=ord('L'), callback=JSON_Load)
        add_key_press_handler(callback=handler_callback)
        # add_mouse_click_handler(button=mvMouseButton_Middle, callback=Second_Tab_Bar_Callback)
    
    ###########################################################################################################
    ############################################# MAIN WINDOW #################################################
    ###########################################################################################################
    with window(label='Main Window', width=1920, height=1080, pos=[0,0], tag='Unit Creation SQL Tool Main Window'):

        set_viewport_resize_callback(callback=print_window_size, user_data='Main Window')
        
        bind_theme(global_theme)
        bind_font(Arial_font)
        with menu_bar():
            presence = False
            if RPC:
                presence = True
            
            with menu(tag='Menu_0', label='Menu'):
                add_menu_item(label='Database Selection', callback=Database_Selector, tag='Database_Selector_Button')
                add_menu_item(tag='Save_JSON_Menu', label='Save JSON', callback=JSON_Save, shortcut='(Ctrl+S)')
                add_menu_item(tag='Load_JSON_Menu', label='Load JSON', callback=JSON_Load, shortcut='(Ctrl+L)')
                add_menu_item(tag='Discord_Presence_Menu', label='Discord Presence', callback=Discord_Presence_Menu, check=True, default_value=presence)
                with tooltip('Discord_Presence_Menu'):
                    add_text('Requires a restart to see changes.\nShould you ever run the program and it hangs, it\'s because of this.\nSet to False in the config to fix.')
                
            # add_menu_item(label='Edit Categories', callback=Show_Category_Window, tag='Edit_Categories_Button', check=True)
            # with tooltip('Edit_Categories_Button'):
                # add_text('Pressing this button will open the "Category Selection" window')
            with menu(tag='Tool_Menu', label='Tools'):
                add_menu_item(label='Causality Creator', callback=Causality_Creator, tag='Causality_Creator_Button')
                with tooltip('Causality_Creator_Button'):
                    add_text("Pressing this button will open a window where causalities can be created")
                add_menu_item(label='Download Assets', callback=download_callback, tag='Down_Desc')
                
            add_menu_item(label='Dokkan Wiki', callback=Dokkan_Wiki, tag='Dokkan_Wiki')
            add_menu_item(label='Discord', tag='Discord', callback=Discord_Server)
            bind_item_theme('Discord', 'Red_Text')
            with tooltip('Discord'):
                add_text('Should you wish to report bugs, please join the discord to sumbit a report.')
            add_menu_item(label='(?)', tag='Menu_Hint')
            with tooltip('Menu_Hint'):
                add_text('Use middle mouse to delete tabs')
                

        with tab_bar(label='Don\'t Matter', tag='Main_Tab_Bar'):
            bind_item_font('Main_Tab_Bar', Arial_font)
            
            with tab(label='Main Card', tag='Main_Card_Tab_0'):
                # Widget_Aliases.tags_to_delete.append('Main_Card_Tab_0')
                add_tab_button(tag=f'Add_Card_Tab', label='+', parent='Main_Tab_Bar', callback=Main_Tab_Bar_Callback, trailing=True)
                bind_item_font('Main_Card_Tab_0', Arial_font)
                with tab_bar(label='Main Card Tab Bar', tag='Main_Card_Tab_Bar_0'):
                    bind_item_font('Main_Card_Tab_Bar_0', Arial_font)
                    
                    


            ###########################################################################################################
            ############################################# Card Input Tab ##############################################
            ###########################################################################################################

                    with tab(label='Card Input', tag='Card_Input_Tab_0'):
                        bind_item_font('Card_Input_Tab_0', Arial_font)
                        # Widget_Aliases.tags_to_delete.append('Card_Input_Tab_0')
                        add_text(default_value='', tag='Card_Name_Display_0', color=(255, 215, 0))
                        bind_item_font('Card_Name_Display_0', Arialbold_Card_Name)
                        with group(horizontal=True, parent='Card_Input_Tab_0'):
                            add_image('Placeholder_Image_Texture_0', tag='Placeholder_Image_0', pos=[8,110])
                            add_image('Custom_Border_Thumb_Background_Texture_0', tag='Custom_Border_Thumb_Background_0', show=False, pos=[8,110])
                            add_image('Card_Thumb_Texture_0', tag='card_thumb_display_0', show=False, pos=[8,110])
                            add_image('Custom_Border_Thumb_Border_Texture_0', tag='Custom_Border_Thumb_Border_0', show=False, pos=[8,110])
                        
                            add_spacer()
                            # with group(horizontal=True, tag=f'Custom_Unit_Checkbox_Group_Horizontal_False_0'):
                            Custom_Unit_Selectables(card=Custom_Unit.card_number)
                            # add_checkbox(label='Custom Unit', callback=Custom_Unit_Checkbox, tag='Custom_Unit_0')
                            # bind_item_font('Custom_Unit_0', font=Arialbold_font)
                            # with group(horizontal=False, tag=f'Custom_Unit_Checkbox_Group_Horizontal_True_0'):
                                # pass
                            
                            with group(horizontal=False, tag=f'Custom_Query_Widget_Group_0', parent=f'Custom_Unit_Checkbox_Group_Horizontal_True_0'):
                                add_input_text(tag=f'Custom_Query_Text_Input_0', width=90, callback=get_card_id)
                                add_button(label='Custom Query', tag=f'Custom_Query_Button_0', callback=Custom_Query_Window)
                                
                            # with group(horizontal=False):
                                # add_input_text(callback=get_card_id, tag='Card ID', hint='Card ID', width=95)
                                # bind_item_font('Card ID', font=Arial_font)
                                # add_button(label='Execute Query', callback=save_callback, tag='Execute_Query')
                                # bind_item_font('Execute_Query', font=Arial_font) 


                        
                            with group(horizontal=True):
                                with group(horizontal=False):
                                    with group(horizontal=True):
                                        add_input_text(hint='SQL name', tag='Filename', width=95)
                                        bind_item_font('Filename', Arial_font)
                                        add_input_text(hint='Card ID', tag='Card_ID_Lua', width=95)
                                        bind_item_font('Card_ID_Lua', Arial_font)

                                    with group(horizontal=True):
                                        add_button(label='Export as SQL', callback=Export_as_SQL, tag='Export as SQL button')
                                        bind_item_font('Export as SQL button', Arial_font) 

                                        add_button(label='Download Luas', callback=Lua_Downloader, tag='Download_Luas')
                                        bind_item_font('Download_Luas', Arial_font)
                                        
                            with group(horizontal=True, tag=f'Custom_Unit_Checkbox_Group_Horizontal_True_0'):
                                pass
                                with group(horizontal=False, tag=f'Custom_Unit_Checkbox_Group_Horizontal_False_0'):
                                    pass              
                                    
                            
                        add_selectable(tag=f'Add_Image_Placeholder_0', height=250, width=250, parent=f'Card_Input_Tab_0', pos=[10,100], callback=Thumb_Test)
                        
                        add_text('', tag='log_1', before='Main_Card_Separator_0')
                        bind_item_font('log_1', Arial_font)
                        bind_item_theme('log_1', 'log_theme')
                        
                        bind_item_theme(f'Add_Image_Placeholder_0','Selectable_Theme')
                        Widget_Aliases.tags_to_delete.append(f'Add_Image_Placeholder_0')
                        add_separator(tag='Main_Card_Separator_0')
                        
                        Card_Widgets()
                        Passive_Widgets()


                        with tooltip('Down_Desc'):

                            add_text('This will download assets such as Luas and effect packs', tag='Down_Desc_Tooltip')
                            bind_item_font('Down_Desc_Tooltip', Arial_font)

                        add_spacer()


            ###########################################################################################################
            ########################################## Specials Tab ###################################################
            ###########################################################################################################

                    with tab(label='Specials', tag='Specials_Tab_Card_0'):
                        Specials_Widgets()
                        bind_item_font('Specials_Tab_Card_0', Arial_font)

            ###############################################################################################################
                    with tab(label='Leader Skill', tag='Leader_Skill_0'):
                        Leader_Skill_Widgets(card=0)
                        bind_item_font('Leader_Skill_0', Arial_font)

            ###############################################################################################################
                    with tab(label='Active Skill', tag='Active_Skill_Card_0', show=False):
                        bind_item_font('Active_Skill_Card_0', Arial_font)
                        
            ###############################################################################################################
                    with tab(label='Standby Skill', tag='Standby_Skill_0', show=False):
                        bind_item_font('Standby_Skill_0', Arial_font)

            ###############################################################################################################
                    with tab(label='Finish Skill', tag='Finish_Skill_0', show=False):
                        bind_item_font('Finish_Skill_0', Arial_font)

            ###############################################################################################################
                    with tab(label='Dokkan Field', tag='Dokkan_Field_0', show=False):
                        bind_item_font('Dokkan_Field_0', Arial_font)
                        
            ###############################################################################################################
                    with tab(label='Battle Params', tag='Battle_Params_0', show=False):
                        pass
                    
            ###############################################################################################################
                    with tab(label='Categories', tag='Categories_0', show=True):
                        Card_Categories_Window()
                        pass
            ###############################################################################################################        
                    with tab(label='Effect Packs', tag=f'Effect_Packs_0', show=False):
                        pass
            ###############################################################################################################        
                    with tab(label='Special Views', tag=f'Special_Views_0', show=False):
                        pass
                    
    

    # show_style_editor()
    # time.sleep(1)
    setup_dearpygui()
    show_viewport(minimized=True)
    # time.sleep(1)
    
    set_primary_window('Unit Creation SQL Tool Main Window', True)
    # show_viewport(maximized=True)
    start_dearpygui()

    #this replaces, start_dearpygui()
    
    # while is_dearpygui_running():
    #     #plop things in here if they need to be constantly updated
        

    destroy_context()

# if __name__ == '__main__':
    # main()