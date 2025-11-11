

# z = []

# for i in range(10):
#     z.append(i)
# print(z)


# category_names = {1 : 'Fusion', 2 : 'Shadow Dragon Saga'}
# category_ids = []
# for key in category_names:
    # category_ids.append(key) 
    # 
# print(category_ids)


# import requests
# import re

# url = "https://dokkaninfo.com/api/cards/1023491"

# headers = {
#     "cookie": "dokkan_info_session=crx5FaLVQVw7oii5DWElRANXj44MLcImbMSGWUKv; _ga=GA1.1.1458656178.1681267656; usprivacy=1---; ad_clicker=false; _pbjs_userid_consent_data=3524755945110770; _sharedid=1e1e1111-5ce4-4c07-baa4-88cc94c560a0; _pw_fingerprint=^%^2213385e395a3c5df402166b6eede8dddb^%^22; panoramaId_expiry=1681872457220; _cc_id=e2b0784f33dfb19c9e9a4def98e9f410; panoramaId=7482201e983324cfd65ab53ef54716d53938c7a494fe04e1259351efbd87adfb; __gads=ID=1508ab73a72266b2:T=1681267659:S=ALNI_MZZzTmsIgtacEIffWWmEnTzo8lLYg; __gpi=UID=00000bddc1a68bd9:T=1681267659:RT=1681267659:S=ALNI_MbvNEoXYWhg4o7isYaVejGSqqvaUQ; cto_bundle=jopUel9Xelc2MkZmRTZSNlJNZkNNbEFjdmNtTHdRWEpiQmVjUCUyQjhzYTF3S3FhV21CTyUyQlozaFBtdEZLeWhrWFZqSjRPV3VaYThVUjB3djBHTnpIWXVtdDk5RjRad1ZXaFdBRkNmcVFpemZwVk04JTJCNnF3S29kNXljd2VueFMlMkJrYTRwZ3ljdW5QVkVoSmElMkJFRXFrN0FGOXg1JTJCJTJCdyUzRCUzRA; FCNEC=^%^5B^%^5B^%^22AKsRol9Q4vxPhUk1d7BN6QyD1R38Ml1HfaITrKLkBUNGRCotm0jHF4FwbECuJsnveVq2MgoNkgoI7qwYuh24pbwE8BZmE5nx7RNqk2C5FxD9AM_udmPxxs6HHjvOGmTsn1ZzLegHzwSvQxqPJrIvDRcH1By228-RHw^%^3D^%^3D^%^22^%^5D^%^2Cnull^%^2C^%^5B^%^5D^%^5D; _ga_P752HZBXS3=GS1.1.1681276219.2.0.1681276257.0.0.0; XSRF-TOKEN=eyJpdiI6ImdqK1BYTjN6aHl6MDV3VUd4R3RaS0E9PSIsInZhbHVlIjoiYVFFNENOUHRyL3k5QXdqOFBrS2xFZUgyUUdYMUxTckVQQWZ4STVqUXdiRXpwVE5RQ3R3Q1h4bktPNUtUTHJRRHlFRVUxdVRBaGVENFNEY25TRFU5Q3picld2VEVqRi9nMjBBQU5DaXB6Q3QrYk8yd05JK2g0dlI3b1Y0MmNYclkiLCJtYWMiOiIyMTk5Yzk1N2FjY2M3YTA0YjRhNDgzMzYyYzhhNmU2YWYwZDYyODUxYTQ1Njk4ZmQ2ZjE5ODI3NmMxNTQzZGVjIiwidGFnIjoiIn0^%^3D",
#     "authority": "dokkaninfo.com",
#     "accept": "*/*",
#     "accept-language": "en-US,en;q=0.9",
#     "content-type": "application/json",
#     "referer": "https://dokkaninfo.com/cards/1026421",
#     "sec-ch-ua": "^\^Chromium^^;v=^\^112^^, ^\^Microsoft",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "^\^Windows^^",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-site": "same-origin",
#     "x-csrf-token": "60aUFeE0z1pQLHtE8fWJg1cix3Woyj9i9qRhVNNE"
# }

# response = requests.request("GET", url, headers=headers)
# data = response.json()

# text = data['passive_skill_description']
# input_text = text.replace('\r', '').replace('\n', '')
# # print(text)    





# def replace_whitespace(text):
#     # modified_text = re.sub(r"(.{55}) {2}", r"\1\n", text)
#     modified_text = re.sub(r"(.{55}) ", r"\1 ' || char(10) ||\n'", text)
#     return modified_text

# # Example usage:
# # input_text = data['passive_skill_description']

# output_text = replace_whitespace(input_text)
# output_text = '\'' + output_text + '\''
# print(output_text)



# asset_directory = ['assets', 'assets/character', 'assets/character/card', 'assets/character/card/ja']
# for i in range(len(asset_directory)):
#     print(i)
    
# card_id_0 = '1024730'
# card_id_0 = str(card_id_0[:-1]) + '1'
# print(card_id_0)
############################################################################################################################
# import requests
# from bs4 import BeautifulSoup as bs

# url = "https://dokkan.wiki/api/cards/1020311" # card_id_0

# response = requests.request("GET", url)
# response_card_json = response.json()
# active_skill_view_id = response_card_json['card']['active_skill_view_id']

# url = 'https://dokkan.wiki/api/lua/4/7725' # active_skill_view_id
# response = requests.request("GET", url)
# response_effect_pack_json = response.json()

# effect_pack_id = []
# effect_pack_id = response_effect_pack_json['effects']
# effect_pack_id = effect_pack_id[0]
# effect_pack_id = effect_pack_id['effect_pack_id']


# url = 'https://dokkan.wiki/api/effect_packs/156667' # effect_pack_id
# response = requests.request("GET", url)
# response_effect_pack_name_json = response.json()
# response_effect_pack_name = response_effect_pack_name_json['pack_name']

# url = f'https://dokkan.wiki/assets/global/en/ingame/battle/sp_effect/{response_effect_pack_name}/en/{response_effect_pack_name}.lwf'
# import requests


    # url = 'https://ishin-global.aktsk.com/ping'

# url = 'https://ishin-production.aktsk.jp/ping'
# # we send an ancient version code that is valid.
# headers = {
#     'X-Platform': 'android',
#     'X-ClientVersion': '1.0.0',
#     'X-Language': 'en',
#     'X-UserID': '////'
# }
# r = requests.get(url, data=None, headers=headers)
# # store our requested data into a variable as json.
# store = r.json()

# url = store['ping_info']['host']
# port = store['ping_info']['port_str']

# print(store)
# test = ['A', 'B', "C"]
# test_dict = {'name' : test}
# print(test_dict['name'][0])

# eff_name = {1 : 'ATK', 2 : 'DEF'}
# eff_id = []
# for key in eff_name:
#     eff_id.append(key)
# print(eff_id)
# for i in range(15):
#     print(i)
# print(len('Fist, Fist, Body, Explosion, Light'))
# test = 'Fist, Fist, Body, Explosion, Light'
# print(test)
# print(len(test))
# test = test.replace(' ', '-')
# print(test)
# print(len(test))



# value = 1
# EZA = None
# CU = None
# if value == 1:
#     EZA = True
    
# if value == 2:
#     CU = True
    
# test =  [f'\n\t\t-- Optimal Awakening Growths'
# f'\n\t\t-- INSERT INTO optimal_awakening_growths ("id", "optimal_awakening_grow_type", "step", "lv_max", "skill_lv_max", "passive_skill_set_id", "leader_skill_set_id")'
# f'\n\t\t-- VALUES '
# f'\n\t\t-- (CardID1, CardID1, 7, 140, 15, CardID1, CardID1);'
# f'\n\t\t-- (CardID1, CardID1, 3, 150, 25, CardID1, CardID1);']

# test = str(test[0])
# if EZA is True:
#     test = test.replace('\n\t\t-- Optimal Awakening Growths', '')
#     test = test.replace('\n\t\t-- VALUES ', '')
#     test = test.replace('\n\t\t-- INSERT INTO optimal_awakening_growths ("id", "optimal_awakening_grow_type", "step", "lv_max", "skill_lv_max", "passive_skill_set_id", "leader_skill_set_id")', '')
#     test = test.replace('\n\t\t-- (CardID1, CardID1, 7, 140, 15, CardID1, CardID1);','')
#     test = test.replace('\n\t\t-- (CardID1, CardID1, 3, 150, 25, CardID1, CardID1);','')
# print(test)
# print(test[0])

# p_name = 'Never-ending Disaster '
# p_name_length = len(p_name)
# if p_name[:p_name_length] == ' ':
#     p_name[:-1]
# else:
#     pass
# print(p_name)

# text = "Ki +3, ATK & DEF +180%;\nAn additional ATK & DEF +30% per attack\nperformed (Up to 120%);\nLaunches an additional attack with a medium chance\nfor it to be a Super Attack;\nRecover 20% HP at the end of the turn if this character\nreceives an attack;\nGreat chance to nullify melee based Super Attacks"

# lines = text.split("\n")  # Split the text into separate lines

# formatted_lines = []
# for i, line in enumerate(lines):
#     if i < len(lines) - 1:
#         formatted_lines.append("\'" + line + " \' || char(10) ||")  # Append ' || char(10) ||' to each line except the last one
#     else:
#         formatted_lines.append('\'' + line)  # Keep the last line unchanged

# formatted_text = "\n".join(formatted_lines)  # Join the modified lines back together

# print(formatted_text)


# print(formatted_text)
# import re

# def add_newlines(text, max_line_length):
#     pattern = r"(?<=\s.{" + str(max_line_length - 1) + r"}\s)"
#     new_text = re.sub(pattern, '\n', text)
#     return new_text

# # Example usage
# text = '''Ki +3, ATK & DEF +180%;
# An additional ATK & DEF +30% per attack
# performed (Up to 120%); Launches an
# additional attack with a medium chance
# for it to be a Super Attack; Recover 20%
# HP at the end of the turn if this character
# receives an attack; Great chance to nullify
# melee based Super Attacks'''

# max_line_length = 55
# result = add_newlines(text, max_line_length)
# print(result)



# from passive import str_length

# length = str_length()

# print(length.str_length[0])

# import requests
# from PIL import Image
# import io

# url = "https://dokkan.wiki/api/categories"

# response = requests.request("GET", url)
# data = response.json()
# categories_id = {}
# categories_name = {}
# categories_name_list = []
# for item in data:
#     categories_id[item['id']] = item['name']
#     categories_name[item['name']] = item['id']

# for i in range(len(categories_id)):
#     categories_name_list.append(categories_id[i + 1])

    
# # selection = categories_list[9]
# print(categories_name[categories_name_list[0]])

# import requests
# from PIL import Image
# import io

# url = 'https://dokkaninfo.com/assets/japan/character/thumb/card_1025870_thumb.png'
# response = requests.get(url)
# image_data = response.content

# image_stream = io.BytesIO(image_data)
# image = Image.open(image_stream)
# image_list = list(image.getdata())

# texture_data = []
# for i in range(len(image_list)):
#     texture_data.append(image_list[i] / 255.0)

# print(texture_data)


# print(texture_data)

# for i in range(len(texture_data)):
    # if image_list[i] == 0.0392156862745098:
        # print(i)
# print(image_list[38796] / 255)
# print(texture_data)

# import requests
# from PIL import Image
# import io

# url = 'https://dokkaninfo.com/assets/japan/character/thumb/card_1025870_thumb.png'
# response = requests.get(url)
# image_data = response.content

# image_stream = io.BytesIO(image_data)
# image = Image.open(image_stream)
# image_list = list(image.getdata())

# # Convert values to the range of 0.0 - 1.0
# image_list_normalized = [val / 255.0 for val in image_list]

# print(image_list_normalized)


# import dearpygui.dearpygui as dpg

# # Callback function for button click
# def button_callback(sender, app_data):
#     print("Button clicked!")

# # Create a window and add UI elements
# with dpg.create_context():
#     dpg.create_window()

#     # Load the image
#     image_path = "path/to/image.png"
#     image_handle = dpg.add_static_texture(dpg.load_texture(image_path))

#     # Create a button
#     button_id = dpg.add_button(label="Button",
#                               callback=button_callback,
#                               width=100,
#                               height=100)

#     # Set the button image
#     dpg.set_button_image(button_id, image_handle)

#     # Run the Dear PyGui event loop
#     dpg.create_context()
#     dpg.show_toolbars()

# jp_text = '自身の登場時、1度だけ登場時演出が発動し、 7ターンの間、知気玉を虹気玉に変化させる'

# with open('test.txt', 'w', encoding='utf-8') as f:
#     filedata = jp_text
#     # print(filedata)
#     # filedata.encode('utf-8', errors='ignore')
#     f.write(filedata)

# print(jp_text)





def Table_Inputs(*, table_name='', table_width=1190, table_height=200, row_name='', row_width=99, class_name=None, parent='', combo=False, combo_tag='', combo_list=[], child_tag='', child_parent='', use_child_window=False):
    
    
    list_of_inputs = []
    list_of_inputs.clear()
    if does_alias_exist(table_name):
        delete_item(table_name)
    for last_rows in range(class_name.last_rows):
        
        for u in range(len(class_name.row_names)):
            if does_alias_exist(class_name.row_names[u] + str(last_rows)):
                delete_item(class_name.row_names[u] + str(last_rows))
    with table(tag=table_name, width=table_width, height=table_height, resizable=True, header_row=True, parent=parent, scrollX=True, scrollY=True, policy=mvTable_SizingFixedFit):
        for i in range(len(class_name.row_names)):
            add_table_column(label=class_name.column_names[i], tag=class_name.column_names[i])
        for o in range(class_name.rows):
            with table_row(tag=row_name + str(o)):
                pass
            
        for z in range(class_name.rows):
            for t in range(len(class_name.row_names)):
                
                if combo and class_name.row_names[t] == combo_tag:
                    add_combo(tag=class_name.row_names[t] + str(z), items=combo_list, default_value=combo_list[0], width=row_width, parent=row_name + str(z))
                    list_of_inputs.append(class_name.row_names[t] + str(z))
                else:
                    add_text(class_name.row_names[t], tag=class_name.row_names[t] + '_Text_' + str(z), parent=row_name + str(z))
                    add_input_text(tag=class_name.row_names[t] + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                    list_of_inputs.append(class_name.row_names[t] + str(z))
            # with tooltip(class_name.row_names[t] + str(z)):
                # add_text(class_name.column_names[t] + str(z))
    return list_of_inputs

# This works for sets with name, desc, cond like Finish Skill Set
def Set_Table(*, table_name='', table_width=1000, table_height=100, parent='', class_name=''):
    
    with table(tag=table_name, width=table_width, height=table_height, resizable=True, header_row=False, parent=parent, scrollX=True, scrollY=True, policy=mvTable_SizingFixedFit, no_host_extendX=True):
        for column in range(3):
            
            add_table_column(tag=table_name + class_name.column_names[column])
        for i in range(len(class_name.column_names)):
            with table_row(tag=table_name + class_name.row_names[i]):
                add_text(class_name.column_names[i])
                add_input_text(tag=class_name.column_names[i], width=200, callback=Text_Resize)
                add_selectable(label=f'Test{i}', width=50)
        
# def Table_Inputs(*, table_name='', table_width=1190, table_height=200, row_name='', row_width=99, class_name=None, 
#                     child_parent='', child_tag='', child_width=1200, child_height=200, use_child_window=True, combo=False, combo_tag='', combo_list=[],
#                     used_in_loop=False, loop_number=int):
    
    
#     list_of_inputs = []
#     list_of_inputs.clear()


#     if does_alias_exist(child_tag):
#         delete_item(child_tag)
#     if does_alias_exist(table_name):
#         delete_item(table_name)
#     for last_rows in range(class_name.last_rows):

#         for u in range(len(class_name.row_names)):
#             if does_alias_exist(class_name.row_names[u] + str(last_rows)):
#                 delete_item(class_name.row_names[u] + str(last_rows))
#             if used_in_loop:
#                 if does_alias_exist(class_name.row_names[u] + str(loop_number) + str(last_rows)):
#                     delete_item(class_name.row_names[u] + str(loop_number) + str(last_rows))
#         with child_window(tag=child_tag, width=child_width, height=child_height, parent=child_parent):

#             with table(tag=table_name, width=table_width, height=table_height, resizable=True, freeze_rows=False, freeze_columns=True, header_row=True, policy=mvTable_SizingStretchProp, scrollX=True, scrollY=True):
#                 for i in range(len(class_name.row_names)):
#                     add_table_column(label=class_name.column_names[i], width_stretch=True)
#                 for o in range(class_name.rows):
#                     with table_row(tag=row_name + str(o)):
#                         pass
                    
#                 for z in range(class_name.rows):
#                     for t in range(len(class_name.row_names)):
#                         # The last number is always 0
#                         # print(str(z))
#                         # print(class_name.row_names[t] + str(z))
#                         if combo and class_name.row_names[t] == combo_tag:
#                             if used_in_loop:
#                                 add_combo(tag=class_name.row_names[t] + str(loop_number) + str(z), items=combo_list, default_value=combo_list[0], width=row_width, parent=row_name + str(z))
#                                 list_of_inputs.append(class_name.row_names[t] + str(loop_number) + str(z))
#                             else:
#                                 add_combo(tag=class_name.row_names[t] + str(z), items=combo_list, default_value=combo_list[0], width=row_width, parent=row_name + str(z))
#                                 list_of_inputs.append(class_name.row_names[t] + str(z))

#                         else:
#                             if used_in_loop:
#                                 add_input_text(tag=class_name.row_names[t] + str(loop_number) + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
#                                 list_of_inputs.append(class_name.row_names[t] + str(loop_number) + str(z))
#                             else:
#                                 add_input_text(tag=class_name.row_names[t] + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
#                                 list_of_inputs.append(class_name.row_names[t] + str(z))

#                     # with tooltip(class_name.row_names[t] + str(z)):
#                         # add_text(class_name.column_names[t] + str(z))

class Efficacy_Values:
    eff_dict = {1 : '1 - ATK', 
                2 : '2 - DEF', 
                3 : '3 - ATK & DEF', 
                4 : '4 - Heal HP', 
                5 : '5 - Ki',
                8 : '8 - Ghost Usher', 
                9 : '9 - Stun', 
                11 : '11 - Attack Order', 
                12 : '12 - Pain Attack', 
                13 : '13 - DR', 
                16 : '16 - Element Type ATK', 
                17 : '17 - Element Type DEF', 
                18 : '18 - Element Type ATK & DEF', 
                19 : '19 - Element Type HP', 
                20 : '20 - Element Type Ki', 
                21 : '21 - Recovery', 
                22 : '22 - Condition Heal', 
                24 : '24 - Guard Break', 
                26 : '26 - Absorb Special Energy', 
                27 : '27 - Resist Special Damage', 
                28 : '28 - Absorb Deal Damage', 
                34 : '34 - Dokkan Gauge Bonus', 
                35 : '35 - Heal Bonus', 
                36 : '36 - Special Bonus', 
                37 : '37 - Energy Bonus', 
                38 : '38 - Link Skill Bonus', 
                39 : '39 - Element Type Energy Bonus', 
                40 : '40 - Element Type Linkage Bonus', 
                43 : '43 - HP ATK', 
                44 : '44 - Element Type HP ATK', 
                46 : '46 - Passive Probability Bonus', 
                47 : '47 - Disable enemy\'s guard', 
                48 : '48 - Seal', 
                50 : '50 - Immune to Neg. Effects', 
                51 : '51 - Energy Ball Color', 
                52 : '52 - Survive K.O Attacks', 
                53 : '53 - Ignore Enemy Defense', 
                54 : '54 - Invalid Combination Attack Bonus', 
                55 : '55 - Target DEF & Self ATK', 
                56 : '56 - Target DEF & Self DEF', 
                57 : '57 - Target DEF & Self Ki', 
                58 : '58 - Energy Ball Heal', 
                59 : '59 - Energy Ball Proportional ATK', 
                60 : '60 - Energy Ball Proportional DEF', 
                61 : '61 - Energy Ball Proportional ATK & DEF', 
                63 : '63 - Special Energy Cost', 
                64 : '64 - Element Type Energy Ball Proportional ATK', 
                65 : '65 - Element Type Energy Ball Proportional DEF', 
                66 : '66 - Element Type Energy Ball Proportional ATK DEF', 
                67 : '67 - Energy Ball Color Bitpattern', 
                68 : '68 - Energy Ball Proportional Bitpattern', 
                69 : '69 - Energy Ball Color Specify Random', 
                70 : '70 - Energy Ball Color Specify Random Without Obstacles', 
                71 : '71 - HP Range ATK', 
                72 : '72 - HP Range DEF', 
                73 : '73 - HP Range ATK DEF', 
                74 : '74 - HP Range Ball Heal', 
                75 : '75 - Disable Swap', # Immune to Locking?
                76 : '76 - ATK Super Effective', 
                77 : '77 - Reset Ball Color', 
                78 : '78 - Guard', 
                79 : '79 - Rage Transformation', 
                80 : '80 - Counter Attack', 
                81 : '81 - Additional Attack', # From folder [lua] > [ab_script] > [attack_counter] > cXXXX.lua
                82 : '82 - Element Type HP ATK DEF', 
                83 : '83 - Element Type Energy Bitpattern', 
                84 : '84 - Sacrifice HP', 
                85 : '85 - Step Extra Attack', 
                86 : '86 - Special ATK Rate', 
                87 : '87 - Element Type Attack Coef', 
                88 : '88 - Element Type Defense Coef', 
                89 : '89 - Element Type Attack Defense Coef', 
                90 : '90 - Critical Attack', 
                91 : '91 - Dodge', 
                92 : '92 - Always Hit', 
                93 : '93 - Element Type Bitpattern HP', # For Leader Skills
                94 : '94 - Immune to Stun', 
                95 : '95 - Dodge Counter Attack', 
                96 : '96 - Ki Sphere Additional Point', 
                97 : '97 - Super Nullification', # From folder [lua] > [ab_script] > [ab_sys] > cXXXX.lua
                98 : '98 - Incremental Param', 
                99 : '99 - Immune to Status Down', 
                100 : '100 - Invalidate Astute', 
                101 : '101 - Forsee Super Attacks', 
                102 : '102 - Metamorphic Probability Count Limit', # For Leader Skills
                103 : '103 - Transformation',
                104 : '104 - HP ATK DEF', # For Leader Skills 
                105 : '105 - ???',
                106 : '106 - ???',
                107 : '107 - ???',
                108 : '108 - ???',
                109 : '109 - Revive', 
                110 : '110 - Passive Reset', 
                111 : '111 - Disable Action', 
                112 : '112 - ???', 
                113 : '113 - ???', 
                114 : '114 - ???', 
                115 : '115 - ???', 
                116 : '116 - ???', 
                117 : '117 - ???', 
                118 : '118 - ???', 
                119 : '119 - Nullify Super' ,
                120 : '120 - Counter Attack' 
                }
    # Any eff with a '???' is to prevent KeyErrors, I'll have to figure out what some of these eff do.

    combo_list = [value for value in eff_dict.values()]
    
def Widget_Value_Grabber(*, class_name, combo=False, combo_tag=None):
    import re
    values = []
    num_of_cards = Card_Checker()
    
    for cards in range(num_of_cards):
        
        # if multiple_skills:
            # for z in range(skill_rows):
                # for x in range(class_name.skill_rows[z]):
                    # if combo:
                        # values.append([re.sub(r'\D', '', get_value(class_name.row_names[i] + '_Card_' + str(cards) + '_Row_' + str(x))) if class_name.row_names[i] == combo_tag else get_value(class_name.row_names[i] +'_Card_' + str(z) + '_Row_' + str(x)) for i in range(len(class_name.row_names))])
                    # else:
                        # values.append([get_value(class_name.row_names[i] + '_Card_' + str(cards) + '_Row_' + str(x)) for i in range(len(class_name.row_names))])
        # else:
        skill_rows = Row_Checker(class_name.row_names[0] + '_Card_' + str(cards) + '_Row_')
        for rows in range(skill_rows):
            if combo:
                values.append([re.sub(r'\D', '', get_value(class_name.row_names[i] + '_Card_' + str(cards) + '_Row_' + str(rows))) if class_name.row_names[i] == combo_tag else get_value(class_name.row_names[i] + '_Card_' + str(cards) + '_Row_' + str(rows)) for i in range(len(class_name.row_names))])
            else:
                values.append([get_value(class_name.row_names[i] + '_Card_' + str(cards) + '_Row_' + str(rows)) for i in range(len(class_name.row_names))])
                        
    

    return values

# Returns the number of cards in the program
def Card_Checker():
    cards = 0
    while True:
        if does_alias_exist(f'Main_Card_Tab_Bar_{cards}'):
            cards += 1
        else:
            break
    return cards
    
    
# Will check how many rows exist in a table, just provide the the tag up until the row number. Row # is included in the function. 
def Row_Checker(tag_id):
    Rows = 0
    while True:
        if does_alias_exist(tag_id + str(Rows)):
            Rows += 1
                # print(Rows)
        else:
            break
    return Rows

from configs import Config_Read
from dearpygui.dearpygui import *
import sqlite3
from configparser import ConfigParser
from pathlib import Path

class Passive_Skill:
        row_names = ['Passive_Name', 'Passive_Desc', 'Passive_Cond']
        # query_row_names = ['Name', 'Desc', 'Cond']
        column_names = ['Name', 'Desc', 'Cond']
        query_values = []
        query_values_formatted = []
        rows = 4
        last_rows = 4

create_context()
# show_debug()
show_imgui_demo()
# show_font_manager()
create_viewport(title='Unit Creation SQL Tool', width=1500, height=1000, x_pos=0, y_pos=0, clear_color=(153, 12, 0, 255))
setup_dearpygui()


with texture_registry():
    width, height, channels, data = load_image('logo/Custom_Border_Border_TEQ.png')
    add_dynamic_texture(width=250, height=250, default_value=data, tag='Custom_Border_Thumb_Border')
    width, height, channels, data = load_image('logo/Custom_Border_Background_TEQ.png')
    add_dynamic_texture(width=250, height=250, default_value=data, tag='Custom_Border_Thumb_Background')
    width, height, channels, data = load_image('logo/card_1026430_thumb.png')
    add_dynamic_texture(width=250, height=250, default_value=data, tag='card_thumb_0')
    
with font_registry():
    Arialbold_font = add_font('fonts/ARIALBD.ttf', size=14)
    
def Text_Resize(tag_id):
    text_width, text_height = get_text_size(get_value(tag_id))
    set_item_width(tag_id, text_width + 10)

def Delete_Items_Test_Button():
    test = []
    for i in range(10):
        test.append(f'Test_Input_{i}')
        
# def Click_Me():
    # x, y = get_item_pos('Custom_Border_Thumb_Tag_1')
    # 
    # configure_item('Custom_Border_Thumb_Tag_2', pos=(x - 3, y))
    # configure_item('Custom_Border_Thumb_Tag_3', pos=(x, y))
    
    

with window(label='Main Window', width=1800, height=1400, pos=[0,0], tag='Unit Creation SQL Tool Main Window', show=True):
    with tab_bar(label=f'XXX', tag=f'Main_Tab_Bar'):
        with tab(label=f'Card',tag=f'Card', parent=f'Main_Tab_Bar'):
            with tab_bar(label=f'XX', tag=f'Tab_Bar1_'):
            
                with tab(label=f'Passive Skill', tag=f'Passive_Skill', parent=f'Tab_Bar1_'):
                    # add_button(label='Click Me', tag='Move_Image_Button', callback=Click_Me)
                    add_text(default_value='', tag='Test_Text', show=False)
                    bind_item_font('Test_Text', Arialbold_font)
                    # add_image('Custom_Border_Thumb_Background', tag='Custom_Border_Thumb_Tag_1')
                    # add_image('card_thumb_0', tag='Custom_Border_Thumb_Tag_2')
                    # add_image('Custom_Border_Thumb_Border', tag='Custom_Border_Thumb_Tag_3')
                    dictionary = {'AGL' : 1 , 'TEQ' : 2, 'INT' : 4, 'STR' : 8, 'PHY' : 16}
                    items = [value for key, value in dictionary.items()]
                    add_selectable(tag='test_selectable', width=100)

                    # configure_item('Custom_Border_Thumb_Tag_1')
                    
                    pass
    # with child_window(label='gay', width=800, height=500):
        
with tab(label='Card 2', tag='Card_Tab', parent='Main_Tab_Bar'):
    pass
    with tab_bar(label=f'Passive Skill', tag=f'Passive_Skill_1', parent=f'Card_Tab'):
        pass
        with tab(label=f'Passive Skill', tag=f'Passive_Skill_2', parent=f'Card_Tab1'):
            pass
        pass
    
# sss = Table_Inputs(table_name='Passive_Skill_Table', row_name='Passive_Skill_Table_Row_', class_name=Passive_Skill,child_tag='Child_Window_',
                #    combo_list=Efficacy_Values.combo_list, table_width=1380, row_width=82, 
                #    parent='Unit Creation SQL Tool Main Window')

Set_Table(table_name='Passive_Skill_Table', class_name=Passive_Skill,
            table_width=1380, table_height=82, parent='Unit Creation SQL Tool Main Window')

class Passive_Skill:
        row_names = ['Passive_Name', 'Passive_Exec_Timing_Type', 'Passive_Efficacy_Type', 'Passive_Target_Type', 'Passive_Sub_Target_Type_Set_ID', 'Passive_Passive_Skill_Effect_ID', 'Passive_Calc_Option', 'Passive_Turn', 'Passive_Is_Once', 'Passive_Probability', 'Passive_Causality_Conditions', 'Passive_Eff_Val1', 'Passive_Eff_Val2', 'Passive_Eff_Val3', 'Passive_Eff_Values']
        query_row_names = ['Passive_Exec_Timing_Type', 'Passive_Efficacy_Type', 'Passive_Target_Type', 'Passive_Sub_Target_Type_Set_ID', 'Passive_Passive_Skill_Effect_ID', 'Passive_Calc_Option', 'Passive_Turn', 'Passive_Is_Once', 'Passive_Probability', 'Passive_Causality_Conditions', 'Passive_Eff_Val1', 'Passive_Eff_Val2', 'Passive_Eff_Val3', 'Passive_Eff_Values']
        column_names = ['Name', 'Exec Timing', 'Eff Type', 'Target Type', 'Sub Target Set', 'PSE ID', 'Calc Option', 'Turn(s)', 'Is Once', 'Prob', 'Causality', 'Eff Val1', 'Eff Val2', 'Eff Val3', 'Eff Values']
        previous_row_values = []
        query_values = []
        query_values_formatted = []
        rows = 0
        last_rows = 0

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

config = Config_Read()

con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
# con.row_factory = lambda cursor, row: row
cur = con.cursor()


cur.execute("SELECT passive_skill_id FROM passive_skill_set_relations WHERE passive_skill_set_id = " + '3353')
Passive_IDs = cur.fetchall()

Passive_IDs = [item[0] for item in Passive_IDs]

Passive_Skill.rows = len(Passive_IDs)
  

# Always clear the list before appending to it. This is to prevent a second query from appending on top of old values
Passive_Skill.query_values.clear()
for i in range(len(Passive_IDs)):
    cur.execute('SELECT exec_timing_type,efficacy_type,target_type,sub_target_type_set_id,passive_skill_effect_id,calc_option,turn,is_once,probability,causality_conditions,eff_value1,eff_value2,eff_value3,efficacy_values FROM passive_skills WHERE id = ' + str(Passive_IDs[i]))
    Passive_Skills_Info = cur.fetchall()
    Passive_Skill.query_values.append(Passive_Skills_Info[0])
    
sss = Table_Inputs(table_name='Passive_Skill_Table', row_name='Passive_Skill_Table_Row_', class_name=Passive_Skill, combo=True,child_tag='Child_Window_', 
             combo_tag=Passive_Skill.row_names[2], combo_list=Efficacy_Values.combo_list, table_width=1380, row_width=82, 
             parent='Unit Creation SQL Tool Main Window')
for i in range(Passive_Skill.rows):
    set_value(Passive_Skill.row_names[0] + str(i), 'God-on-God Showdown')
    # Text_Resize(Passive_Skill.row_names[0] + str(i))
    for z in range(len(Passive_Skill.query_row_names)):
            # if Passive_Skill.row_names[z] == Passive_Skill.row_names[0]:
                    # set_value(Passive_Skill.row_names[0] + str(i), get_value('Passive_Name'))
                    
            if Passive_Skill.query_values[i][z] is None:
                    set_value(Passive_Skill.query_row_names[z] + str(i), 'NULL')
            else:
                    # Setting the Eff_Type combo list using the dictionary
                    if Passive_Skill.query_row_names[z] == Passive_Skill.query_row_names[1]:
                            # print(eff_dict[Passive_Skill.query_values[i][z]])
                            set_value(Passive_Skill.query_row_names[z] + str(i), Efficacy_Values.eff_dict[Passive_Skill.query_values[i][z]])
                            # Text_Resize(Passive_Skill.query_row_names[z] + str(i))
                    elif Passive_Skill.query_row_names[z] == Passive_Skill.query_row_names[9]:
                            set_value(Passive_Skill.query_row_names[z] + str(i), Passive_Skill.query_values[i][z])
                            # Text_Resize(Passive_Skill.query_row_names[z] + str(i))
                    # Every other value in passive  
                    else:
                            set_value(Passive_Skill.query_row_names[z] + str(i), Passive_Skill.query_values[i][z])
            configure_item(Passive_Skill.row_names[0] + str(i), show=False)
            configure_item(Passive_Skill.column_names[0], show=False)
            
    set_item_height('Passive_Skill_Table', (24 * len(Passive_IDs)) + 23)
                            
with group(horizontal=True, tag=f'Test_Group_1', parent=('Unit Creation SQL Tool Main Window')):                       
    for i in range(10):

        add_input_text(tag=f'Test_Input_{i}', default_value='')

# print(sss)


set_item_width(Passive_Skill.row_names[2] + '0', 125)
configure_item(Passive_Skill.column_names[0], init_width_or_weight=500)

for i in range(len(Passive_Skill.column_names)):
    print(Passive_Skill.row_names[i] + '0')
    print(get_item_width(Passive_Skill.row_names[i] + '0'))
print(get_item_width)
# values = Widget_Value_Grabber(Passive_Skill)
# print(sss)
# set_item_width('Passive_Efficacy_Type_8', 300)

# finish_skills_ID_tags = [f'Finish_Skill_ID_{i}' for i in range(5)]
# print(finish_skills_ID_tags)
    
show_viewport()
show_imgui_demo()
set_primary_window('Unit Creation SQL Tool Main Window', True)

start_dearpygui()
# while is_dearpygui_running():
    # render_dearpygui_frame()
    # print(get_item_pos('Custom_Border_Thumb_Tag'))
    # print(get_item_pos('Custom_Border_Thumb_Tag_1'))

# # # # # leader_combo_rows = {'Element Type' : 2, 'Extreme Class' : 2, 'Super Class' : 2, 'All Types' : 2, '1 Category' : 2, '1 Category & 1 Element' : 4, '2 Categories' : 4, '2 Categories & 1 Extra' : 6, '3 Categories & 2 Extra' : 12}

# # # # # print(leader_combo_rows[1])
# import requests

# def checkServers(ver):
#     if ver == 'gb':
#         url = 'https://ishin-global.aktsk.com/ping'
#     else:
#         url = 'https://ishin-production.aktsk.jp/ping'
#     # we send an ancient version code that is valid.
#     headers = {
#         'X-Platform': 'android',
#         'X-ClientVersion': '1.0.0',
#         'X-Language': 'en',
#         'X-UserID': '////'
#     }
#     r = requests.get(url, data=None, headers=headers)
#     # store our requested data into a variable as json.
#     store = r.json()
#     # if 'error' not in store:
#         # url = store['ping_info']['host']
#         # port = store['ping_info']['port_str']
#         # if ver == 'gb':
#             # gb_url = 'https://' + str(url)
#             # gb_port = str(port)
#         # else:
#             # jp_url = 'https://' + str(url)
#             # jp_port = str(port)
#         # return True
#     # else:
#         # print('[' + ver + ' server] ' + str(store['error']))
    
#     print(store['ping_info']['host'])
#     return False
    
    

# checkServers('gb')


# def database_download():
    
#     url = 'https://ishin-global.aktsk.com/client_assets/database'
    
#     headers = {
#         'User-Agent': 'Dalvik/2.1.0 (Linux; Android 7.0; SM-E7000)',
#         'Accept': '*/*',
#         'Authorization': cryption.mac('GET', '/client_assets/database'),
#         'Content-type': 'application/json',
#         'X-Platform': 'android',
#         'X-AssetVersion': '////',
#         'X-DatabaseVersion': '////',
#         'X-ClientVersion': '4.7.1-0cfca85464a68be2257af10e69257dfba116fa0f7315c6b930b4eec74f41a49f',
#         'X-Language': 'en',
#     }
    
# def mac(method, action):
#     # Creates Mac Authentication header string used when sending requests
#     # returns string

#     ts = str(int(round(time.time(), 0)))
#     nonce = ts + ':' + str(hashlib.md5(ts.encode()).hexdigest())
    
#     if config.client == 'global':
#         value = ts + '\n' + nonce + '\n' + method + '\n' + action + '\n' \
#             + config.gb_url.replace('https://', '') + '\n' + config.gb_port + '\n'
#     else:
#         value = ts + '\n' + nonce + '\n' + method + '\n' + action + '\n' \
#             + config.jp_url.replace('https://', '') + '\n' + config.jp_port + '\n'

#     hmac_hex_bin = hmac.new(config.secret.encode('utf-8'), value.encode('utf-8'), hashlib.sha256).digest()
#     mac = base64.b64encode(hmac_hex_bin).decode()
#     final = 'MAC ' + 'id=' + '"' + config.access_token + '"' + ' nonce=' + '"' \
#         + nonce + '"' + ' ts=' + '"' + ts + '"' + ' mac=' + '"' + mac + '"'
    
#     return final

# from classes import Database
    
# card_id = [2]
# select = 'dokkan_field_efficacy_set_id,exec_timing_type,efficacy_type,calc_option,turn,is_once,probability,eff_value1,eff_value2,eff_value3,efficacy_values,causality_conditions'
# Database = Database()

# test = Database.query(SELECT=select, FROM='dokkan_field_efficacies', WHERE='dokkan_field_efficacy_set_id', value=card_id)
# print(test)


# import pygame

# # Initialize pygame
# pygame.init()

# # Load a WAV audio file
# audio_file = r"C:\Users\rbero\OneDrive\Documents\GitHub\Dokkan-Modding-Tools\Custom Songs\.ImEating BGMs\[HD] One Piece OST - Franky Theme.wav"

# # Initialize the mixer module (for sound playback)
# pygame.mixer.init()

# # Load the audio file into a Sound object
# sound = pygame.mixer.Sound(audio_file)

# # Play the sound
# sound.play()

# # Wait for the sound to finish playing
# while pygame.mixer.get_busy():
#     pygame.time.delay(100)

# # Clean up
# pygame.quit()