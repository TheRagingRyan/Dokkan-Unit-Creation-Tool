import sqlite3
from dearpygui.dearpygui import *
from . jp_translations import Translations
from . cards import String_Length
from . configs import Config_Read
from . functions import Table_Inputs, Delete_Items, Table_ID, Row_Checker
from . passive import Passive_Skill
from . classes import Efficacy_Values, Widget_Aliases, Card_Checks, Active_Skill, Active_Skill_Set

#################################################################################################################################################################################################################################################################
#################################################################################################################################################################################################################################################################    
#################################################################################################################################################################################################################################################################

def Text_Resize(tag_id):
    text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIAL.ttf')
    set_item_width(tag_id, text_width + 7)
    
#################################################################################################################################################################################################################################################################
    
def Active_Skill_Checkbox():
    add_checkbox(label='Active Skill',tag='Active_Skill_Checkbox_Card_0', default_value=False, parent='Active_Skill_Card_0', callback=Active_Skill_Checkbox_Widgets)
    Widget_Aliases.tags_to_delete.append('Active_Skill_Checkbox_Card_0')
    
#################################################################################################################################################################################################################################################################
def Active_Skill_Checkbox_Widgets(app_data):
    Delete_Items(Active_Skill.tags_to_delete)
    Active_Skill.tags_to_delete.clear()
    print(app_data)
    
    if get_value('Active_Skill_Checkbox_Card_0'):
        Active_Skill_Widgets()

        tags = Table_Inputs(table_name=f'Active_Skill_Set_Card_0', row_name=f'Active_Skill_Set_Row_', class_name=Active_Skill_Set,
                            use_child_window=False, table_parent='Active_Skill_Card_0', table_height=57, table_width=640)
        for tags in tags:
            Active_Skill.tags_to_delete.append(tags)

        with group(horizontal=True, tag='Active_Skills_Group_Card_0', parent='Active_Skill_Card_0'):
            add_text('Active Skills', tag='Active_Skills_Text_Card_0', color=(255,50,50), parent='Active_Skills_Group_Card_0')
            add_button(label='Add Skill', tag='Active_Skills_Button_Add_Card_0', parent='Active_Skills_Group_Card_0', callback=Active_Skill_Add)
            add_button(label='Del Skill', tag='Active_Skills_Button_Del_Card_0', parent='Active_Skills_Group_Card_0', callback=Active_Skill_Del)
        Widget_Aliases.tags_to_delete.append('Active_Skills_Group_Card_0')
        Widget_Aliases.tags_to_delete.append('Active_Skills_Text_Card_0')
        Widget_Aliases.tags_to_delete.append('Active_Skills_Button_Add_Card_0')
        Widget_Aliases.tags_to_delete.append('Active_Skills_Button_Del_Card_0')
        Active_Skill.tags_to_delete.append('Active_Skills_Group_Card_0')
        Active_Skill.tags_to_delete.append('Active_Skills_Text_Card_0')
        Active_Skill.tags_to_delete.append('Active_Skills_Button_Add_Card_0')
        Active_Skill.tags_to_delete.append('Active_Skills_Button_Del_Card_0')

        tags = Table_Inputs(table_name=f'Active_Skill_Table_Card_0', row_name=f'Active_Skill_Row_', class_name=Active_Skill,
                            use_child_window=False, table_parent='Active_Skill_Card_0', table_height=80, table_width=1132,
                            combo=True, combo_list=Efficacy_Values.combo_list, combo_tag=Active_Skill.row_names[3])
        for tags in tags:
            Active_Skill.tags_to_delete.append(tags)



        Delete_Items('Ultimate_Special_Separator')
        Delete_Items('Ultimate_Special_Text')
        Delete_Items('Ultimate_Special_Group')
        for u in range(len(Active_Skill.ultimate_names)):
            Delete_Items(Active_Skill.ultimate_hints[u] + '_Text')
            Delete_Items(Active_Skill.ultimate_names[u])

        add_separator(tag='Ultimate_Special_Separator', parent='Active_Skill_Card_0')
        add_text('Ultimate Special', color=(255,50,50), parent='Active_Skill_Card_0', tag='Ultimate_Special_Text')
        Widget_Aliases.tags_to_delete.append('Ultimate_Special_Separator')
        Widget_Aliases.tags_to_delete.append('Ultimate_Special_Text')
        Active_Skill.tags_to_delete.append('Ultimate_Special_Separator')
        Active_Skill.tags_to_delete.append('Ultimate_Special_Text')

        with group(horizontal=True, parent='Active_Skill_Card_0', tag='Ultimate_Special_Group'):
            for z in range(len(Active_Skill.ultimate_names)):
                add_text(Active_Skill.ultimate_hints[z] + ':', color=(255, 174, 26), parent='Ultimate_Special_Group', tag=Active_Skill.ultimate_hints[z] + '_Text')
                add_input_text(tag=Active_Skill.ultimate_names[z], default_value='', hint=Active_Skill.ultimate_hints[z], width=String_Length.length[0], callback=Text_Resize, parent='Ultimate_Special_Group')
                Widget_Aliases.tags_to_delete.append(Active_Skill.ultimate_hints[z] + '_Text')
                Widget_Aliases.tags_to_delete.append(Active_Skill.ultimate_names[z])
                Active_Skill.tags_to_delete.append(Active_Skill.ultimate_hints[z] + '_Text')
                Active_Skill.tags_to_delete.append(Active_Skill.ultimate_names[z])
                Active_Skill.tags_to_delete.append('Ultimate_Special_Group')
                
#################################################################################################################################################################################################################################################################

def Active_Skill_Widgets():
    
    for key, value in Card_Checks.active_skill_ids.items():
        # print(key)
        add_text('Active Skill Set', color=(255,50,50), tag=f'Active_Skill_Text_Card_{key}', parent=f'Active_Skill_Card_{key}')
        # with group(horizontal=True, tag=f'Active_Skill_Group'):
        with group(horizontal=True, parent=f'Active_Skill_Card_{key}', tag=f'Active_Skill_Group_1_Card_{key}'):

            with group(horizontal=True, parent=f'Active_Skill_Card_{key}', tag=f'Active_Skill_Group_2_Card_{key}'):
                add_text('Name:', color=(255, 174, 26), tag=f'Active_Skill_Name_Text_Card_{key}')
                add_input_text(tag=f'Active_Name_Card_{key}', default_value='', hint='Name', width=String_Length.length[0], callback=Text_Resize)

            with group(horizontal=True, parent=f'Active_Skill_Card_{key}', tag=f'Active_Skill_Group_3_Card_{key}'):
                add_text('Desc: ', color=(255, 174, 26), tag=f'Active_Skill_Desc_Text_Card_{key}')
                add_input_text(tag=f'Active_Desc_Card_{key}', default_value='', hint='Description', width=String_Length.length[0], callback=Text_Resize)

            with group(horizontal=True, parent=f'Active_Skill_Card_{key}', tag=f'Active_Skill_Group_4_Card_{key}'):
                add_text('Cond: ', color=(255, 174, 26), tag=f'Active_Skill_Cond_Text_Card_{key}')
                add_input_text(tag=f'Active_Cond_Card_{key}', default_value='', hint='Condition', width=String_Length.length[0], callback=Text_Resize)
        add_separator(tag=f'Active_Skill_Separator_Card_{key}', parent=f'Active_Skill_Card_{key}')

        Widget_Aliases.tags_to_delete.append(f'Active_Skill_Text_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skill_Name_Text_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skill_Desc_Text_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skill_Cond_Text_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Name_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Desc_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Cond_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skill_Separator_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skill_Group_1_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skill_Group_2_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skill_Group_3_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skill_Group_4_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Skill_Text_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Skill_Name_Text_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Skill_Desc_Text_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Skill_Cond_Text_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Name_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Desc_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Cond_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Skill_Separator_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Skill_Group_1_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Skill_Group_2_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Skill_Group_3_Card_{key}')
        Active_Skill.tags_to_delete.append(f'Active_Skill_Group_4_Card_{key}')
    
#################################################################################################################################################################################################################################################################
        
def Active_Skill_Query():
    config = Config_Read()
    
    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
    cur = con.cursor()
    
    print(Card_Checks.active_skill_ids)
    for key, value in Card_Checks.active_skill_ids.items():
    
        cur.execute('SELECT target_type,sub_target_type_set_id,calc_option,efficacy_type,eff_val1,eff_val2,eff_val3,efficacy_values,thumb_effect_id,effect_se_id FROM active_skills WHERE active_skill_set_id = ' + str(value))
        active_skills = cur.fetchall()

        cur.execute('SELECT turn,exec_limit,causality_conditions,ultimate_special_id,special_view_id,costume_special_view_id,bgm_id FROM active_skill_sets WHERE id = ' + str(value))
        active_skill_sets = cur.fetchall()


        if key in Card_Checks.ultimate_special_ids:
            cur.execute('SELECT name,description,increase_rate,aim_target FROM ultimate_specials WHERE id = ' + str(Card_Checks.ultimate_special_ids[key]))
            ultimate_special = cur.fetchall()



        Active_Skill.rows = len(active_skills)

        

        ttt = Table_Inputs(table_name=f'Active_Skill_Set_Card_{key}', row_name=f'Active_Skill_Set_Row_Card_{key}_', class_name=Active_Skill_Set,
                            use_child_window=False, table_parent=f'Active_Skill_Card_{key}', table_height=47, table_width=755, transformation=True, transformation_card_num=key)
        # print(ttt)
        
        
        
        with group(horizontal=True, tag=f'Active_Skills_Group_Card_{key}', parent=f'Active_Skill_Card_{key}'):
            add_text('Active Skills', tag=f'Active_Skills_Text_Card_{key}', color=(255,50,50), parent=f'Active_Skills_Group_Card_{key}')
            add_button(label='Add Skill', tag=f'Active_Skills_Button_Add_Card_{key}', parent=f'Active_Skills_Group_Card_{key}', callback=Active_Skill_Add)
            add_button(label='Del Skill', tag=f'Active_Skills_Button_Del_Card_{key}', parent=f'Active_Skills_Group_Card_{key}', callback=Active_Skill_Del)
        Widget_Aliases.tags_to_delete.append(f'Active_Skills_Group_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skills_Text_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skills_Button_Add_Card_{key}')
        Widget_Aliases.tags_to_delete.append(f'Active_Skills_Button_Del_Card_{key}')

        sss = Table_Inputs(table_name=f'Active_Skill_Table_Card_{key}', row_name=f'Active_Skill_Row_Card_{key}_', class_name=Active_Skill,
                            use_child_window=False, table_parent=f'Active_Skill_Card_{key}', table_height=80, table_width=1132,
                            combo=True, combo_list=Efficacy_Values.combo_list, combo_tag=Active_Skill.row_names[3], transformation=True, transformation_card_num=key)
        
        # print(sss)

        if key in Card_Checks.ultimate_special_ids:

            Delete_Items(f'Ultimate_Special_Separator_Card_{key}')
            Delete_Items(f'Ultimate_Special_Text_Card_{key}')
            Delete_Items(f'Ultimate_Special_Group_Card_{key}')
            for u in range(len(Active_Skill.ultimate_names)):
                Delete_Items(Active_Skill.ultimate_hints[u] + '_Card_' + str(key) + '_Text')
                Delete_Items(Active_Skill.ultimate_names[u] + '_Card_' + str(key))

            add_separator(tag=f'Ultimate_Special_Separator_Card_{key}', parent=f'Active_Skill_Card_{key}')
            add_text('Ultimate Special', color=(255,50,50), parent=f'Active_Skill_Card_{key}', tag=f'Ultimate_Special_Text_Card_{key}')
            Widget_Aliases.tags_to_delete.append(f'Ultimate_Special_Separator_Card_{key}')
            Widget_Aliases.tags_to_delete.append(f'Ultimate_Special_Text_Card_{key}')

            with group(horizontal=True, parent=f'Active_Skill_Card_{key}', tag=f'Ultimate_Special_Group_Card_{key}'):
                for z in range(len(Active_Skill.ultimate_names)):
                    add_text(Active_Skill.ultimate_hints[z] + ':', color=(255, 174, 26), parent=f'Ultimate_Special_Group_Card_{key}', tag=Active_Skill.ultimate_hints[z] + '_Card_' + str(key) + '_Text')
                    add_input_text(tag=Active_Skill.ultimate_names[z] + '_Card_' + str(key), default_value='', hint=Active_Skill.ultimate_hints[z], width=String_Length.length[0], callback=Text_Resize, parent=f'Ultimate_Special_Group_Card_{key}')
                    Widget_Aliases.tags_to_delete.append(Active_Skill.ultimate_hints[z] + '_Card_' + str(key) + '_Text')
                    Widget_Aliases.tags_to_delete.append(Active_Skill.ultimate_names[z] + '_Card_' + str(key))



            for o in range(len(Active_Skill.ultimate_names)):
                set_value(Active_Skill.ultimate_names[o] + '_Card_' + str(key), ultimate_special[0][o])
                Text_Resize(Active_Skill.ultimate_names[o] + '_Card_' + str(key))



        # Table_Inputs(table_name='Active_Skill_Table_Card_0', row_name='Active_Skill_Table_Row_', parent='Active_Skill_Child_Window', class_name=Active_Skill)
        # Active_Skill_Inputs()
        Active_Skill.last_rows = len(active_skills)
        # active_skill_set_id = get_value('CardID1')

        set_item_height(f'Active_Skill_Table_Card_{key}', (24 * len(active_skills)) + 23)
        
        for i in range(len(active_skills)):
            for z in range(10):
                if active_skills[i][z] is None:
                    set_value(Active_Skill.row_names[z] + '_Card_' + str(key) + '_Row_' + str(i), 'NULL')

                elif Active_Skill.row_names[z] == Active_Skill.row_names[3]:
                    set_value(Active_Skill.row_names[z] + '_Card_' + str(key) + '_Row_' + str(i), Efficacy_Values.eff_dict[active_skills[i][z]])

                else:
                    set_value(Active_Skill.row_names[z] + '_Card_' + str(key) + '_Row_' + str(i), active_skills[i][z])

                # set_value(Active_Skill.row_names[0] + str(i), active_skill_set_id)


        for y in range(len(Active_Skill_Set.row_names)):
            if active_skill_sets[0][y] is None:
                set_value(Active_Skill_Set.row_names[y] + '_Card_' + str(key) + '_Row_' + '0', 'NULL')
            else:
                set_value(Active_Skill_Set.row_names[y] + '_Card_' + str(key) + '_Row_' + '0', active_skill_sets[0][y])


        if get_value('ENG_Check'):
            set_value(f'Active_Name_Card_{key}', Card_Checks.active_skill_name[key])
            set_value(f'Active_Desc_Card_{key}', Card_Checks.active_skill_desc[key].replace('\n', ''))
            set_value(f'Active_Cond_Card_{key}', Card_Checks.active_skill_cond[key].replace('\n', ''))
            Text_Resize(f'Active_Name_Card_{key}')
            Text_Resize(f'Active_Desc_Card_{key}')
            Text_Resize(f'Active_Cond_Card_{key}')
        else:
            set_value(f'Active_Name_Card_{key}', Translations.Active_Skill_Name)
            set_value(f'Active_Desc_Card_{key}', Translations.Active_Skill_Description)
            set_value(f'Active_Cond_Card_{key}', Translations.Active_Skill_Conditions)
            Text_Resize(f'Active_Name_Card_{key}')
            Text_Resize(f'Active_Desc_Card_{key}')
            Text_Resize(f'Active_Cond_Card_{key}')
            
        configure_item(f'Active_Skill_Card_{key}', show=True)

# if get_value('ENG_Check'):
    # pass
# else:
    # pass
    
#################################################################################################################################################################################################################################################################
    
def Active_Skill_Add(app_data):
    Table_Number = Table_ID(app_data)
    Rows = Row_Checker(Active_Skill.row_names[0] + '_Card_' + str(Table_Number) + '_Row_')
    
    add_table_row(tag=f'Active_Skill_Row_Card_{Table_Number}_{Rows}', parent=f'Active_Skill_Table_Card_{Table_Number}')
    table_rows = []
    for i in range(len(Active_Skill.row_names)):
        # print(Active_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows))
        # Passive_Skill.row_names[2] is Efficacy Type
        if Active_Skill.row_names[i] == Active_Skill.row_names[3]:
                add_combo(tag=Active_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), items=Efficacy_Values.combo_list, width=149, parent=f'Active_Skill_Row_Card_{Table_Number}_{Rows}')
                set_value(Active_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), Efficacy_Values.combo_list[0])
        else:
                add_input_text(tag=Active_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows), hint=Active_Skill.column_names[i], width=99, default_value='', parent=f'Active_Skill_Row_Card_{Table_Number}_{Rows}')
        # table_row.append(Active_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows))
                    
    set_item_height(f'Active_Skill_Table_Card_{Table_Number}', (24 * (Rows + 1) + 23))
    Active_Skill.table_row_tags[int(Table_Number)].append(table_rows)

def Active_Skill_Del(app_data):
    Table_Number = Table_ID(app_data)
    Rows = Row_Checker(Active_Skill.row_names[0] + '_Card_' + str(Table_Number) + '_Row_')
    
    delete_item(f'Active_Skill_Row_Card_{Table_Number}_{Rows - 1}')
    
    if Rows > 1:
        for i in range(len(Active_Skill.row_names)):
            delete_item(Active_Skill.row_names[i] + '_Card_' + str(Table_Number) + '_Row_' + str(Rows - 1))
        set_item_height(f'Active_Skill_Table_Card_{Table_Number}', (24 * (Rows - 1) + 23))
        last_list_row = len(Passive_Skill.table_row_tags[int(Table_Number)])
        del Active_Skill.table_row_tags[int(Table_Number)][last_list_row - 1]
    else:
        pass