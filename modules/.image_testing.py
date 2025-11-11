import sqlite3
from pathlib import Path
import os
from configparser import ConfigParser

def Home_Path():
    home_path = str(Path.home())
    return home_path

#################################################################################################################################################################################################################################################################

def Config_Path():
    Config_Path = str(Path.home()) + '/Unit Creation Tool' + '/config.ini'
    return Config_Path

#################################################################################################################################################################################################################################################################

def Config_Exists():
    Exists = os.path.exists(Config_Path())
    return Exists

#################################################################################################################################################################################################################################################################

def Config():
    config = ConfigParser()
    return config

#################################################################################################################################################################################################################################################################

def Config_Read():
    config = Config()
    config.read(Config_Path())
    return config


# config = Config_Read()
# con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)    
# cur = con.cursor()

# final_values = []
# card_unique_info_set_ids = []
# card_unique_infos_names = []
# card_unique_infos_set_lists = []
# card_unique_infos_set_card_names_lists = []

# ### Gets the card_unique_info_set_ids
# query = f'SELECT card_unique_info_set_id FROM card_unique_info_set_relations'
# cur.execute(query, (), )
# values = cur.fetchall()
# for tuple in range(len(values)):
#     final_values.append(['NULL' if values[tuple][z] is None else values[tuple][z] for z in range(len(values[tuple]))])


# for item in final_values:
#     if item not in card_unique_info_set_ids and item[0] != 0:
#         card_unique_info_set_ids.append(item)
# #########################################################################################################################
# ### Gets the card_unique_infos
# for set in range(len(card_unique_info_set_ids)):
#     query = f'SELECT name FROM card_unique_infos WHERE id = {str(card_unique_info_set_ids[set][0])}'
#     cur.execute(query, (), )
#     values = cur.fetchall()
#     # print(values)
#     for tuple in range(len(values)):
#         card_unique_infos_names.append(['NULL' if values[tuple][z] is None else values[tuple][z] for z in range(len(values[tuple]))])

# #########################################################################################################################
# ### Gets all of the character's card_unique_info_ids using the card_unique_info_set_ids
# for set in range(len(card_unique_info_set_ids)):
#     query = f'SELECT card_unique_info_id FROM card_unique_info_set_relations WHERE card_unique_info_set_id = {str(card_unique_info_set_ids[set][0])}'
#     cur.execute(query, (), )
#     values = cur.fetchall()
#     # print(values)
#     # for tuple in range(len(values)):
#     card_unique_infos_set_lists.append(values)
    
# card_unique_infos_set_lists = [[item[0] for item in sublist] for sublist in card_unique_infos_set_lists]

# ### Gets the names for the card_unique_info_set_ids
# for set in range(len(card_unique_infos_set_lists)):
#     means_to_an_end = []
#     for unique_info_id in card_unique_infos_set_lists[set]:
#         query = f'SELECT name FROM card_unique_infos WHERE id = {str(unique_info_id)}'
#         cur.execute(query, (), )
#         values = cur.fetchall()
#         # print(values)
#         # for tuple in range(len(values)):
#         means_to_an_end.append(['NULL' if values[tuple][z] is None else values[tuple][z] for z in range(len(values[tuple]))])
#     card_unique_infos_set_card_names_lists.append(means_to_an_end)
    
    

# # card_unique_infos_set_card_names = {card_unique_infos_names[i]: }

# ### Create a list of character names based on the first index of each list in order to get the first card name of the card_unique_infos_set
# card_unique_infos_first_name_list = []
# for list in range(len(card_unique_infos_set_card_names_lists)):
#     card_unique_infos_first_name_list.append(card_unique_infos_set_card_names_lists[list][0])

# final_card_unique_infos_name_sets = []
# ### Create a list format for all of the card names in a set
# for set_of_names in range(len(card_unique_infos_set_card_names_lists)):
#     means_to_an_end = []
#     for name in card_unique_infos_set_card_names_lists[set_of_names]:
#         means_to_an_end.append(name[0])
#     final_card_unique_infos_name_sets.append(means_to_an_end)
    
# # print(final_card_unique_infos_name_sets[0])

# card_unique_infos_name_dict = {card_unique_infos_first_name_list[i][0]: final_card_unique_infos_name_sets[i] for i in range(len(card_unique_infos_set_card_names_lists))}

# print(card_unique_infos_name_dict)



















from dearpygui.dearpygui import *
import cv2
import numpy as np

# def Animation():
    # 
    # pass

original_image = cv2.imread('logo/Yellow_Light.png')
# angle = 0


# Function to update the rotated image in the GUI
def Animation(sender):
    angle = 0
    angle += 1  # Increment the rotation angle
    if angle >= 360:
        angle = 0  # Reset angle to 0 after a full rotation

    # Calculate the rotation matrix
    center = (original_image.shape[1] // 2, original_image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Apply the rotation to the image
    rotated_image = cv2.warpAffine(original_image, rotation_matrix, (original_image.shape[1], original_image.shape[0]))

    # Update the image in the GUI
    print(get_value('Yellow_Light'))
    set_value('Yellow_Light', rotated_image.tobytes())

create_context()
# show_debug()
# show_style_editor()
show_imgui_demo()
# show_font_manager()
create_viewport(title='Unit Creation SQL Tool', width=1300 - 300, height=1300 - 300, x_pos=0, y_pos=0, clear_color=(0, 0, 0, 255))
set_viewport_vsync(True)

with window(label='Test Window', width=700, height=700, tag='Test_Window'):
    add_button(label='Play Animation', callback=Animation, tag='Animation_Button')
    
    with texture_registry():
        
        width, height, channels, data = load_image('logo/Placeholder.png')
        add_dynamic_texture(width=width, height=height, default_value=data, tag=f'Placeholder')
        
        width, height, channels, data = load_image('logo/Custom_Border_Background_INT.png')
        add_dynamic_texture(width=width, height=height, default_value=data, tag=f'Custom_Border_Background_INT')
        
        width, height, channels, data = load_image('logo/card_1026430_thumb.png')
        add_dynamic_texture(width=width, height=height, default_value=data, tag=f'card_1026430_thumb')
        
        width, height, channels, data = load_image('logo/Custom_Border_Border_AGL.png')
        add_dynamic_texture(width=width, height=height, default_value=data, tag=f'Custom_Border_Border_AGL')
        
        width, height, channels, data = load_image('logo/Yellow_Light.png')
        add_dynamic_texture(width=width, height=height, default_value=data, tag=f'Yellow_Light')
        
        width, height, channels, data = load_image('logo/Red_Lightning.png')
        add_dynamic_texture(width=width, height=height, default_value=data, tag=f'Red_Lightning')
        
        width, height, channels, data = load_image('logo/Yellow_Lightning.png')
        add_dynamic_texture(width=width, height=height, default_value=data, tag=f'Yellow_Lightning')
        


    
    add_image('Placeholder', parent='Test_Window', tag='Placeholder_Image')
    position = get_item_pos('Placeholder_Image')
    add_image('Custom_Border_Background_INT', parent='Test_Window', tag='Background_Image', pos=[0,0])
    add_image('Yellow_Light', parent='Test_Window', tag='Yellow_Light_Image', pos=[55,40])
    # add_image('Red_Lightning', parent='Test_Window', tag='Red_Lightning_image', pos=[60,0])
    # add_image('Yellow_Lightning', parent='Test_Window', tag='Yellow_Lightning_image', pos=[60,0])
    add_image('card_1026430_thumb', parent='Test_Window', tag='Card_Thumb', pos=[0,0])
    add_image('Custom_Border_Border_AGL', parent='Test_Window', tag='Border', pos=[0,0])
    

    # Define the rotation angle and rotation center

    
    setup_dearpygui()
    show_viewport(minimized=True)
    # time.sleep(1)
    
    set_primary_window('Test_Window', True)
    # show_viewport(maximized=True)
    start_dearpygui()
    

    #this replaces, start_dearpygui()
    
    # colors = []
    # for i in range(250):
    #     colors.append(i)
    #     colors.append(i / 3)
    #     colors.append(i * 3)
    # while is_dearpygui_running():
    #     #plop things in here if they need to be constantly updated
    #     print('this will run every frame')
    #     set_value('Card_Name_Display_0', color)
    #     configure_item('Card_Name_Display_0', color=(colors, colors, colors))
    #     render_dearpygui_frame()

    destroy_context()