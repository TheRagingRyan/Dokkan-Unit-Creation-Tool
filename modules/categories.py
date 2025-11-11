from dearpygui.dearpygui import *
import re
import requests
from . configs import Config_Read
from . classes import Leader_Skill_Info, Custom_Unit, Card_Checks


# Categories Activated
class Categories_Activated:
        
        Cats = []
        card_categories_dict = {}
        
def Table_ID(app_data):
    Table_Number = ''
    for char in reversed(app_data):
            if char.isdigit():
                Table_Number += char
            else:
                break
    return Table_Number

def Grab_Tag_Numbers(tag_id):
    """Takes a string and grabs all the numbers from it

    Args:
        tag_id (str): String with numbers

    Returns:
        str: Every number from the string
    """
    number = ''
    for char in tag_id:
            if char.isdigit():
                    number += char
    return number

def Grab_GLB_Categories():
        url = f'https://dokkan.wiki/api/categories'
        response = requests.get(url)
        data = response.json()
        cat_list = [data[i]['name'] + ' ' + '(' + str(data[i]['id']) + ')' for i in range(len(data))]
        
        return cat_list
                
def Category_jp_id_List():
        import ast
        config_info = Config_Read()
        jp_categories_id_list = config_info.get('JP_Categories', 'categories')
        jp_categories_id_list = ast.literal_eval(jp_categories_id_list)
        
        return jp_categories_id_list

def Category_Sub_Window():
        with window(label='Category Window', width=600, height=1015, pos=[0,0], tag='Category_Window'):
                bind_item_font('Category_Window', 'Arial_Font')
                Card_Categories_Window()

def Show_Category_Window(data, app_data):
        pass

def Card_Categories_Wiki(*, card=0, json_cards=0):
        # cat_list = [re.search(r'\((\d+)\)', text).group(1) for text in Leader_Skill_Info.cat_list]
        
        Clear_Categories(card)
        json_data = Card_Checks.json_data[json_cards]
        
        for i in range(len(json_data['categories'])):
                category = json_data['categories'][i]['id']
                if does_alias_exist(f'Category_Card_{card}_{category}_left'):
                        configure_item(f'Category_Card_{card}_{category}_left', texture_tag=f'Category_{category}_on')
                        set_value(f'Image_State_Check_{category}', 1)
                elif does_alias_exist(f'Category_Card_{card}_{category}_right'):
                        configure_item(f'Category_Card_{card}_{category}_right', texture_tag=f'Category_{category}_on')
                        set_value(f'Image_State_Check_{category}', 1)
                if json_data['categories'][i]['id'] not in Categories_Activated.card_categories_dict[int(card)]:
                        Categories_Activated.card_categories_dict[int(card)].append(json_data['categories'][i]['id'])
        
        print('Categories: ' + str(Categories_Activated.card_categories_dict))
        
def Button_Test(app_data):
        print(app_data)
        card = None
        cat_num = ''
        for char in app_data:
                if char.isdigit():
                        card = int(char)
                        break
                
        cat_string = app_data.replace(f'Category_Card_{card}', '')
        cat_num = Grab_Tag_Numbers(cat_string)
        
                        
        Cat_Icons_Activated = Categories_Activated.Cats
                 
        state = get_value(f'Image_State_Check_{cat_num}')
        
        if state == 0:
                configure_item(app_data, texture_tag=f'Category_{cat_num}_on')
                set_value(f'Image_State_Check_{cat_num}', 1)
                if card in Categories_Activated.card_categories_dict:
                        if cat_num not in Categories_Activated.card_categories_dict[card]:
                                Categories_Activated.card_categories_dict[card].append(int(cat_num))
                                
        elif state == 1:
                configure_item(app_data, texture_tag=f'Category_{cat_num}_off')
                set_value(f'Image_State_Check_{cat_num}', 0)
                Categories_Activated.card_categories_dict[card].remove(int(cat_num))
        
        print(Categories_Activated.card_categories_dict)
        
        Categories_Activated.Cats = Cat_Icons_Activated

def Load_Category_Images():
        jp_categories_id_list = Category_jp_id_List() 
        with texture_registry():
                for i in range(len(jp_categories_id_list)):
                        try:
                                width, height, channels, data = load_image(f'categories/Category_{jp_categories_id_list[i]}_off.png')
                        except TypeError:
                                print(f'categories/Category_{jp_categories_id_list[i]}_off.png not found')

                        try:
                                add_dynamic_texture(width, height, default_value=data, tag=f'Category_{jp_categories_id_list[i]}_off')
                        except TypeError:
                                print(f'categories/Category_{jp_categories_id_list[i]}_off.png not found')

                        try:
                                width, height, channels, data = load_image(f'categories/Category_{jp_categories_id_list[i]}_on.png')
                        except TypeError:
                                print(f'categories/Category_{jp_categories_id_list[i]}_on.png not found')

                        try:
                                add_dynamic_texture(width, height, default_value=data, tag=f'Category_{jp_categories_id_list[i]}_on')
                        except TypeError:
                                print(f'categories/Category_{jp_categories_id_list[i]}_on.png not found') 
                                
def Create_Category_Images(*, card=0):
        jp_categories_id_list = Category_jp_id_List() 
        
        # testy = 0
        # for i in range(int(len(jp_categories_id_list) / 2)):
                # Delete_Items(f'Card_Category_Pair_{i}')
                # Delete_Items(f'Category_Card_{card}_{jp_categories_id_list[testy]}_left')
                # testy += 1
                # Delete_Items(f'Category_Card_{card}_{jp_categories_id_list[testy]}_right')
                # testy += 1
        Categories_Activated.card_categories_dict[card] = []
        test = 0
        for i in range(int(len(jp_categories_id_list) / 2)):
                with group(tag=f'Card_Category_Pair_Card_{card}_{i}', horizontal=True):

                        add_image_button(f'Category_{jp_categories_id_list[test]}_off', callback=Button_Test, tag=f'Category_Card_{card}_{jp_categories_id_list[test]}_left')
                        bind_item_theme(f'Category_Card_{card}_{jp_categories_id_list[test]}_left', 'Category_Button_Theme')
                        test += 1
                        add_image_button(f'Category_{jp_categories_id_list[test]}_off', callback=Button_Test, tag=f'Category_Card_{card}_{jp_categories_id_list[test]}_right')
                        bind_item_theme(f'Category_Card_{card}_{jp_categories_id_list[test]}_right', 'Category_Button_Theme')
                        test += 1

def Create_New_Category_Tab():
        card = Custom_Unit.card_number
        card_name = f'Unit {card + 1}'
        if Card_Checks.card_names:
                card_name = Card_Checks.card_names[0][0]

def Add_All_Categories(tag_id):
        card = Table_ID(tag_id)
        cat_list = [re.search(r'\((\d+)\)', text).group(1) for text in Leader_Skill_Info.cat_list]
        Categories_Activated.card_categories_dict[int(card)].clear()
        
        for cat in cat_list:
                if does_alias_exist(f'Category_Card_{card}_{cat}_left'):
                        configure_item(f'Category_Card_{card}_{cat}_left', texture_tag=f'Category_{cat}_on')
                        set_value(f'Image_State_Check_{cat}', 1)
                elif does_alias_exist(f'Category_Card_{card}_{cat}_right'):
                        configure_item(f'Category_Card_{card}_{cat}_right', texture_tag=f'Category_{cat}_on')
                        set_value(f'Image_State_Check_{cat}', 1)
                Categories_Activated.card_categories_dict[int(card)].append(cat)
        
# Clear categories before adding new ones. Meant to delete existing categories of previous queries    
def Clear_Categories(card):
        cat_list = [re.search(r'\((\d+)\)', text).group(1) for text in Leader_Skill_Info.cat_list]
        Categories_Activated.card_categories_dict[int(card)].clear()
        for cat in cat_list:
                if does_alias_exist(f'Category_Card_{card}_{cat}_left'):
                        configure_item(f'Category_Card_{card}_{cat}_left', texture_tag=f'Category_{cat}_off')
                        set_value(f'Image_State_Check_{cat}', 0)
                elif does_alias_exist(f'Category_Card_{card}_{cat}_right'):
                        configure_item(f'Category_Card_{card}_{cat}_right', texture_tag=f'Category_{cat}_off')
                        set_value(f'Image_State_Check_{cat}', 0)
        
        
                
def Card_Categories_Window(*, card=0):
        #Height near passive 370
        jp_categories_id_list = Category_jp_id_List() 
        def remove(tag):
                if does_alias_exist(tag):
                        remove_alias(tag)
                
        check = ['Category_Window', 'card_categories_child_window', 'cat_icons']
        testy = 0
        for i in range(int(len(jp_categories_id_list) / 2)):
                remove(f'Card_Category_Pair_Card_{card}_{i}')
                remove(f'Category_{jp_categories_id_list[testy]}_left')
                testy += 1
                remove(f'Category_{jp_categories_id_list[testy]}_right')
                testy += 1
        # print(remove_list)
        for value in check:
                if does_alias_exist(value):
                        remove_alias(value)
                        
                        
        # Delete_Items('Card_Categories_Tab_Bar')
        with group(tag=f'Categories_Buttons_Group_{card}', horizontal=True):
                add_button(label='Add All', tag=f'Add_All_Categories_Button_{card}', callback=Add_All_Categories)
                add_button(label='Clear', tag=f'Clear_Categories_Button_{card}', callback=Clear_Categories)
        
        with child_window(tag=f'card_categories_child_window_{card}', width=600, height=985):
                bind_item_font(f'card_categories_child_window_{card}', 'Arial_Font')
                # with tab_bar(tag=f'Card_Categories_Tab_Bar'):
                # for i in range(Custom_Unit.card_number + 1):
                                # with tab(tag=f'Card_Categories_Tab_{i}', label=f'Card {i + 1}'):
                with group(tag=f'cat_icons_{card}_{i}', show=True):
                        # print(jp_categories_id_list)
                        # num = len(jp_categories_id_list) // 2
                        # first_half = jp_categories_id_list[:num]
                        # second_half = jp_categories_id_list[num:]
                        Create_Category_Images(card=card)
                        # add_combo(tag=f'cat_card_category_id{i}',items=categories_name_list, width=200, default_value='Pick a Category')
                        # add_input_text(tag=f'cat_num{i}', hint='Num', default_value=i + 1)


# def Category_Icon_Download():
#         import json
#         #Grabbing Categories from dokkan wiki so it can automatically grab the newest categories
#         url = "https://dokkan.wiki/api/categories"

#         response = requests.request("GET", url)
#         global_data = response.json()
#         global_categories_id_dict = {}
#         global_categories_name_dict = {}
#         global_categories_id_list = []
#         global_categories_leader_skill_list = []
#         for item in global_data:
#             global_categories_id_dict[item['id']] = item['name']
#             global_categories_name_dict[item['name']] = item['id']
#             global_categories_id_list.append(item['id'])
#             global_categories_leader_skill_list.append(item['name'] + ' (' + str(item['id']) + ')')
#         # print(global_categories_leader_skill_list)

        
#                 # print(categories_name_list)
#         url = 'https://jpn.dokkan.wiki/api/categories'
#         response = requests.get(url)
#         jp_data = response.json()
#         jp_categories_id_list = []
#         for item in jp_data:
#                 jp_categories_id_list.append(item['id'])
#                 # print(jp_categories_id_list)

#         Category_Downloads(global_categories_id_list, jp_categories_id_list)


#         jp_categories_id_list = json.dumps(jp_categories_id_list)
#         global_categories_leader_skill_list = json.dumps(global_categories_leader_skill_list)


#         database_path = easygui.fileopenbox('Please select your decrypted database')

#         if not os.path.exists(str(Home_Path()) + '/Unit Creation Tool'):
#                 os.makedirs(str(Home_Path()) + '/Unit Creation Tool')
        
#         config = ConfigParser()
                
#         if 'JP_Categories' in config:
#                 config.remove_section('JP_Categories')
#         if 'GLB_Categories' in config:
#                 config.remove_section('GLB_Categories')
        
#         config.add_section('JP_Categories')
#         config.add_section('GLB_Categories')
#         config.set('DEFAULT', 'database_path', database_path)
#         config.set('JP_Categories', 'categories', jp_categories_id_list)
#         config.set('GLB_Categories', 'categories list', global_categories_leader_skill_list)

#         conf_path = str(Home_Path()) + '/Unit Creation Tool/config.ini'
        
#         with open(conf_path, 'w') as f:
#             config.write(f)
#         # def Category_global_id_List():
#                 # return global_categories_id_list