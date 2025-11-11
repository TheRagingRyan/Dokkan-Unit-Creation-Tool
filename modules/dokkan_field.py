from dearpygui.dearpygui import *
from . functions import Text_Resize, Table_Inputs, Get_Max_Table_Row_Width
from . classes import Card_Checks, Dokkan_Field, String_Length, Widget_Aliases, Database
from . leader import Resize_Description

# def Link_to_Active(tag_id, user_data):
    # print(tag_id)
    # link_to_passive_tag = tag_id.replace('Link_to_Active_Button_', 'Link_to_Passive_Button_')
    # set_value(link_to_passive_tag, False)
# 
# def Link_to_Passive(tag_id, user_data):
    # link_to_active_tag = tag_id.replace('Link_to_Passive_Button_', 'Link_to_Active_Button_')
    # set_value(link_to_active_tag, False)


def Dokkan_Field_Widgets(card, field):
    ### In case a unit comes out with more than 1 dokkan field
    # for card in range(len(Card_Checks.card_ids)):
        # for field in range(len(Card_Checks.dokkan_field_cards)):
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
            

        
Database = Database()
def Dokkan_Field_Query():
    query = f'SELECT exec_timing_type,efficacy_type,calc_option,turn,is_once,probability,eff_value1,eff_value2,eff_value3,efficacy_values,causality_conditions FROM dokkan_field_efficacies WHERE dokkan_field_efficacy_set_id = ?'
    for card in range(len(Card_Checks.card_ids)):
        if Card_Checks.dokkan_field_cards[card]:
            # print(Card_Checks.dokkan_field_ids)
            configure_item(f'Dokkan_Field_{card}', show=True)
            
            ### Number of dokkan fields on said card
            for dokkan_field in range(len(Card_Checks.dokkan_field_ids[card])):
                
                dokkan_field_efficacies = Database.execute_query(query, str(Card_Checks.dokkan_field_ids[card][dokkan_field]),)
                Dokkan_Field.rows = len(dokkan_field_efficacies)
                
                Dokkan_Field_Widgets(card, dokkan_field)
                
                ### Check for Dokkan Field Relation
                query = f'SELECT dokkan_field_id,active_skill_set_id FROM dokkan_field_active_skill_set_relations WHERE dokkan_field_id = ?'
                dokkan_field_active_relation = Database.execute_query(query, str(Card_Checks.dokkan_field_ids[card][dokkan_field]),)
                if dokkan_field_active_relation:
                    set_value(f'Link_to_Active_Button_{card}_{dokkan_field}', True)
                    
                query = f'SELECT dokkan_field_id,passive_skill_id FROM dokkan_field_passive_skill_relations WHERE dokkan_field_id = ?'
                dokkan_field_passive_relation = Database.execute_query(query, str(Card_Checks.dokkan_field_ids[card][dokkan_field]),)
                if dokkan_field_passive_relation:
                    Card_Checks.dokkan_field_ids[card][dokkan_field] in dokkan_field_passive_relation[0]
                    set_value(f'Link_to_Passive_Button_{card}_{dokkan_field}', True)
                    
                
                
                t = Table_Inputs(table_name=f'Dokkan_Field_Table_{card}_{dokkan_field}', row_name=f'Dokkan_Field_Table_Row_{card}_{dokkan_field}', table_parent=f'Dokkan_Field_{card}', use_child_window=False, 
                            class_name=Dokkan_Field, table_width=1100, row_width=82, freeze_rows=1, transformation=True, transformation_card_num=card, used_in_loop=True, loop_number=dokkan_field, table_policy=mvTable_SizingFixedFit)
                # print(t)
                
                set_value(f'Dokkan_Field_Name_Input_Text_{card}_{dokkan_field}', Card_Checks.dokkan_field_names[card][dokkan_field])
                set_value(f'Dokkan_Field_Desc_Input_Text_{card}_{dokkan_field}', Card_Checks.dokkan_field_desc[card][dokkan_field])
                Resize_Description(f'Dokkan_Field_Desc_Input_Text_{card}_{dokkan_field}', Card_Checks.dokkan_field_desc[card][dokkan_field])
                set_value(f'Dokkan_Field_Resource_ID_{card}_{dokkan_field}', Card_Checks.dokkan_field_resource_ids[card][dokkan_field])
                Text_Resize(f'Dokkan_Field_Name_Input_Text_{card}_{dokkan_field}')
                Text_Resize(f'Dokkan_Field_Desc_Input_Text_{card}_{dokkan_field}')
                Text_Resize(f'Dokkan_Field_Resource_ID_{card}_{dokkan_field}')
                
                for row in range(len(dokkan_field_efficacies)):
                    for value in range(len(dokkan_field_efficacies[row])):
                        if value is None:
                            set_value(Dokkan_Field.row_names[value] + '_Card_' + str(card) + '_Row_0' + str(row), 'NULL')
                        elif Dokkan_Field.row_names[value] == Dokkan_Field.row_names[10]:
                            set_value(Dokkan_Field.row_names[value] + '_Card_' + str(card) + '_Row_0' + str(row), dokkan_field_efficacies[row][value])
                            Text_Resize(Dokkan_Field.row_names[value] + '_Card_' + str(card) + '_Row_0' + str(row))
                        else:
                            set_value(Dokkan_Field.row_names[value] + '_Card_' + str(card) + '_Row_0' + str(row), dokkan_field_efficacies[row][value])
                            
                        
                set_item_height(f'Dokkan_Field_Table_{card}_{dokkan_field}', (24 * len(dokkan_field_efficacies)) + 23)
                
                widget_widths_list = []
                for row in range(len(dokkan_field_efficacies)):
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
                print(max_width)
                set_item_width(f'Dokkan_Field_Table_{card}_{dokkan_field}', max_width + 100)
                

        
                            