from dearpygui.dearpygui import *
from . classes import Active_Skill, Active_Skill_Set, Causality, Dokkan_Field, Finish_Skill_Set, Finish_Skill, Leader_Skill_Info, Card_Specials, Special_Set, Specials, Standby_Skill_Set, Standby_Skill, Passive_Skill, Widget_Aliases
from . categories import Grab_GLB_Categories
import traceback
from . configs import Home_Path, Config_Path, Config
import os
from json import load as json_load
import zipfile
from PIL import Image
from io import BytesIO



def Table_Inputs(*, table_name='', table_width=1190, table_height=200, row_name='', row_width=99, class_name=None, freeze_columns=0, freeze_rows=0, 
                    child_parent='', child_tag='', child_width=1200, child_height=200, use_child_window=True, combo=False, combo_tag='', combo_list=[],
                    combo_column_name=str, used_in_loop=False, loop_number=int, table_parent=str, table_policy=mvTable_SizingFixedFit, transformation=False, 
                    transformation_card_num=int, child_before='', table_before=''):
    
    
    list_of_inputs = []
    table_row_final_inputs = []
    list_of_inputs.clear()
    if not transformation:
        if use_child_window:
        
            if does_alias_exist(child_tag):
                delete_item(child_tag)
            if does_alias_exist(table_name):
                delete_item(table_name)

            # if isinstance(class_name.last_rows, list):
            #     for rows in len(class_name.last_rows):
            #         for last_rows in range(class_name.last_rows[rows]):

            #             for u in range(len(class_name.row_names)):
            #                 if does_alias_exist(class_name.row_names[u] + str(last_rows)):
            #                     delete_item(class_name.row_names[u] + str(last_rows))
            #                 if used_in_loop:
            #                     if does_alias_exist(class_name.row_names[u] + str(loop_number) + str(last_rows)):
            #                         delete_item(class_name.row_names[u] + str(loop_number) + str(last_rows))
            else:
                for last_rows in range(class_name.last_rows):

                    for u in range(len(class_name.row_names)):
                        if does_alias_exist(class_name.row_names[u] + '0' + str(last_rows)):
                            delete_item(class_name.row_names[u] + '0' + str(last_rows))
                        if used_in_loop:
                            if does_alias_exist(class_name.row_names[u] + '0' + str(loop_number) + str(last_rows)):
                                delete_item(class_name.row_names[u] + '0' + str(loop_number) + str(last_rows))

                with child_window(tag=child_tag, width=child_width, height=child_height, parent=child_parent, horizontal_scrollbar=False, before=child_before):
                    Widget_Aliases.tags_to_delete.append(child_tag)
                    list_of_inputs.append(child_tag)

                    with table(tag=table_name, width=table_width, height=table_height, resizable=True, freeze_rows=freeze_rows, freeze_columns=freeze_columns, header_row=True, policy=table_policy, scrollX=True, scrollY=True):
                        Widget_Aliases.tags_to_delete.append(table_name)
                        list_of_inputs.append(table_name)
                        list_of_inputs.append(table_name)
                        for i in range(len(class_name.row_names)):
                            if combo and class_name.column_names[i] == combo_column_name:
                                add_table_column(label=class_name.column_names[i], init_width_or_weight=150)

                            else:
                                add_table_column(label=class_name.column_names[i])
                        for o in range(class_name.rows):
                            with table_row(tag=row_name + str(o)):
                                Widget_Aliases.tags_to_delete.append(row_name + str(o))
                                list_of_inputs.append(row_name + str(o))
                                pass
                            
                        for z in range(class_name.rows):
                            table_row_inputs = []
                            for t in range(len(class_name.row_names)):
                                # The last number is always 0
                                # print(str(z))
                                # print(class_name.row_names[t] + str(z))
                                if combo and class_name.row_names[t] == combo_tag:
                                    if used_in_loop:
                                        add_combo(tag=class_name.row_names[t] + '0' + str(loop_number) + str(z), items=combo_list, default_value=combo_list[0], width=149, parent=row_name + str(z))
                                        Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                                        list_of_inputs.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                                        table_row_inputs.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                                    else:
                                        add_combo(tag=class_name.row_names[t] + '0' + str(z), items=combo_list, default_value=combo_list[0], width=149, parent=row_name + str(z))
                                        Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '0' + str(z))
                                        list_of_inputs.append(class_name.row_names[t] + '0' + str(z))
                                        table_row_inputs.append(class_name.row_names[t] + '0' + str(z))

                                else:
                                    if used_in_loop:
                                        add_input_text(tag=class_name.row_names[t] + '0' + str(loop_number) + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                                        Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                                        list_of_inputs.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                                        table_row_inputs.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                                    else:
                                        add_input_text(tag=class_name.row_names[t] + '0' + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                                        Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '0' + str(z))
                                        list_of_inputs.append(class_name.row_names[t] + '0' + str(z))
                                        table_row_inputs.append(class_name.row_names[t] + '0' + str(z))
                            table_row_final_inputs.append(table_row_inputs)

                            # with tooltip(class_name.row_names[t] + str(z)):
                                # add_text(class_name.column_names[t] + str(z))
        else:

            if does_alias_exist(child_tag):
                delete_item(child_tag)
            if does_alias_exist(table_name):
                delete_item(table_name)
            for last_rows in range(class_name.last_rows):

                for u in range(len(class_name.row_names)):
                    if does_alias_exist(class_name.row_names[u] + '0' + str(last_rows)):
                        delete_item(class_name.row_names[u] + '0' + str(last_rows))
                    if used_in_loop:
                        if does_alias_exist(class_name.row_names[u] + '0' + str(loop_number) + str(last_rows)):
                            delete_item(class_name.row_names[u] + '0' + str(loop_number) + str(last_rows))

            with table(tag=table_name, width=table_width, height=table_height, resizable=True, freeze_rows=freeze_rows, freeze_columns=freeze_columns, header_row=True, policy=table_policy, parent=table_parent, scrollX=True, scrollY=True, before=table_before):
                Widget_Aliases.tags_to_delete.append(table_name)
                list_of_inputs.append(table_name)
                for i in range(len(class_name.row_names)):
                    if combo and class_name.column_names[i] == combo_column_name:
                        add_table_column(label=class_name.column_names[i], tag=table_name + class_name.column_names[i], init_width_or_weight=150)
                        Widget_Aliases.tags_to_delete.append(table_name + class_name.column_names[i])
                        list_of_inputs.append(table_name + class_name.column_names[i])
                    else:
                        add_table_column(label=class_name.column_names[i], tag=table_name + class_name.column_names[i])
                        Widget_Aliases.tags_to_delete.append(table_name + class_name.column_names[i])
                        list_of_inputs.append(table_name + class_name.column_names[i])
                for o in range(class_name.rows):
                    with table_row(tag=row_name + str(o)):
                        Widget_Aliases.tags_to_delete.append(row_name + str(o))
                        list_of_inputs.append(row_name + str(o))
                    
                for z in range(class_name.rows):
                    table_row_inputs = []
                    for t in range(len(class_name.row_names)):
                        # The last number is always 0
                        # print(str(z))
                        # print(class_name.row_names[t] + str(z))
                        if combo and class_name.row_names[t] == combo_tag:
                            if used_in_loop:
                                add_combo(tag=class_name.row_names[t] + '0' + str(loop_number) + str(z), items=combo_list, default_value=combo_list[0], width=149, parent=row_name + str(z))
                                Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                                list_of_inputs.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                                table_row_inputs.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                            else:
                                add_combo(tag=class_name.row_names[t] + '0' + str(z), items=combo_list, default_value=combo_list[0], width=149, parent=row_name + str(z))
                                Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '0' + str(z))
                                list_of_inputs.append(class_name.row_names[t] + '0' + str(z))
                                table_row_inputs.append(class_name.row_names[t] + '0' + str(z))

                        else:
                            if used_in_loop:
                                add_input_text(tag=class_name.row_names[t] + '0' + str(loop_number) + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                                Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                                list_of_inputs.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                                table_row_inputs.append(class_name.row_names[t] + '0' + str(loop_number) + str(z))
                            else:
                                add_input_text(tag=class_name.row_names[t] + '0' + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                                Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '0' + str(z))
                                list_of_inputs.append(class_name.row_names[t] + '0' + str(z))
                                table_row_inputs.append(class_name.row_names[t] + '0' + str(z))
                    table_row_final_inputs.append(table_row_inputs)

                    # with tooltip(class_name.row_names[t] + str(z)):
                        # add_text(class_name.column_names[t] + str(z))
    else:
        if use_child_window:
        
            if does_alias_exist(child_tag):
                delete_item(child_tag)
            if does_alias_exist(table_name):
                delete_item(table_name)

            # if isinstance(class_name.last_rows, list):
            #     for rows in len(class_name.last_rows):
            #         for last_rows in range(class_name.last_rows[rows]):

            #             for u in range(len(class_name.row_names)):
            #                 if does_alias_exist(class_name.row_names[u] + str(last_rows)):
            #                     delete_item(class_name.row_names[u] + str(last_rows))
            #                 if used_in_loop:
            #                     if does_alias_exist(class_name.row_names[u] + str(loop_number) + str(last_rows)):
            #                         delete_item(class_name.row_names[u] + str(loop_number) + str(last_rows))
            else:
                for last_rows in range(class_name.last_rows):

                    for u in range(len(class_name.row_names)):
                        if does_alias_exist(class_name.row_names[u] + str(transformation_card_num) + str(last_rows)):
                            delete_item(class_name.row_names[u] + str(transformation_card_num) + str(last_rows))
                        if used_in_loop:
                            if does_alias_exist(class_name.row_names[u] + str(transformation_card_num) + str(loop_number) + str(last_rows)):
                                delete_item(class_name.row_names[u] + str(transformation_card_num) + str(loop_number) + str(last_rows))

                with child_window(tag=child_tag, width=child_width, height=child_height, parent=child_parent, horizontal_scrollbar=False, before=child_before):
                    Widget_Aliases.tags_to_delete.append(child_tag)
                    list_of_inputs.append(child_tag)

                    with table(tag=table_name, width=table_width, height=table_height, resizable=True, freeze_rows=freeze_rows, freeze_columns=freeze_columns, header_row=True, policy=table_policy, scrollX=True, scrollY=True):
                        Widget_Aliases.tags_to_delete.append(table_name)
                        list_of_inputs.append(table_name)
                        for i in range(len(class_name.row_names)):
                            if combo and class_name.column_names[i] == combo_column_name:
                                add_table_column(label=class_name.column_names[i], init_width_or_weight=150)

                            else:
                                add_table_column(label=class_name.column_names[i])
                        for o in range(class_name.rows):
                            with table_row(tag=row_name + str(o)):
                                Widget_Aliases.tags_to_delete.append(row_name + str(o))
                                list_of_inputs.append(row_name + str(o))
                            
                        for z in range(class_name.rows):
                            table_row_inputs = []
                            for t in range(len(class_name.row_names)):
                                # The last number is always 0
                                # print(str(z))
                                # print(class_name.row_names[t] + str(z))
                                if combo and class_name.row_names[t] == combo_tag:
                                    if used_in_loop:
                                        add_combo(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z), items=combo_list, default_value=combo_list[0], width=149, parent=row_name + str(z))
                                        Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                                        list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                                        table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                                    else:
                                        add_combo(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z), items=combo_list, default_value=combo_list[0], width=149, parent=row_name + str(z))
                                        Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                                        list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                                        table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))

                                else:
                                    if used_in_loop:
                                        add_input_text(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                                        Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                                        list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                                        table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                                    else:
                                        add_input_text(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                                        Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                                        list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                                        table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                            table_row_final_inputs.append(table_row_inputs)

                            # with tooltip(class_name.row_names[t] + str(z)):
                                # add_text(class_name.column_names[t] + str(z))
        else:

            if does_alias_exist(child_tag):
                delete_item(child_tag)
            if does_alias_exist(table_name):
                delete_item(table_name)
            for last_rows in range(class_name.last_rows):

                for u in range(len(class_name.row_names)):
                    if does_alias_exist(class_name.row_names[u] + str(transformation_card_num) + str(last_rows)):
                        delete_item(class_name.row_names[u] + str(transformation_card_num) + str(last_rows))
                    if used_in_loop:
                        if does_alias_exist(class_name.row_names[u] + str(transformation_card_num) + str(loop_number) + str(last_rows)):
                            delete_item(class_name.row_names[u] + str(transformation_card_num) + str(loop_number) + str(last_rows))

            with table(tag=table_name, width=table_width, height=table_height, resizable=True, freeze_rows=freeze_rows, freeze_columns=freeze_columns, header_row=True, policy=table_policy, parent=table_parent, scrollX=True, scrollY=True, before=table_before):
                Widget_Aliases.tags_to_delete.append(table_name)
                list_of_inputs.append(table_name)
                for i in range(len(class_name.row_names)):
                    if combo and class_name.column_names[i] == combo_column_name:
                        add_table_column(label=class_name.column_names[i], tag=table_name + class_name.column_names[i], init_width_or_weight=150)
                        Widget_Aliases.tags_to_delete.append(table_name + class_name.column_names[i])
                        list_of_inputs.append(table_name + class_name.column_names[i])
                    else:
                        add_table_column(label=class_name.column_names[i], tag=table_name + class_name.column_names[i])
                        Widget_Aliases.tags_to_delete.append(table_name + class_name.column_names[i])
                        list_of_inputs.append(table_name + class_name.column_names[i])
                        
                for o in range(class_name.rows):
                    with table_row(tag=row_name + str(o)):
                        Widget_Aliases.tags_to_delete.append(row_name + str(o))
                        list_of_inputs.append(row_name + str(o))
                        pass
                    
                for z in range(class_name.rows):
                    table_row_inputs = []
                    for t in range(len(class_name.row_names)):
                        # The last number is always 0
                        # print(str(z))
                        # print(class_name.row_names[t] + str(z))
                        if combo and class_name.row_names[t] == combo_tag:
                            if used_in_loop:
                                add_combo(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z), items=combo_list, default_value=combo_list[0], width=149, parent=row_name + str(z))
                                Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                                list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                                table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                            else:
                                add_combo(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z), items=combo_list, default_value=combo_list[0], width=149, parent=row_name + str(z))
                                Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                                list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                                table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))

                        else:
                            if used_in_loop:
                                add_input_text(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                                Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                                list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                                table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                            else:
                                add_input_text(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                                Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                                list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                                table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                    table_row_final_inputs.append(table_row_inputs)
        class_name.table_row_tags.append(table_row_final_inputs)

                    # with tooltip(class_name.row_names[t] + str(z)):
                        # add_text(class_name.column_names[t] + str(z))
    return list_of_inputs, table_row_final_inputs


def Table_Combo_Inputs(*, table_name='', table_width=1190, table_height=200, row_name='', row_width=99, class_name=None, freeze_columns=0, freeze_rows=0, 
                    child_tag='', combo=False, combo_list={}, used_in_loop=False, loop_number=int, table_parent=str, 
                    table_policy=mvTable_SizingFixedFit, transformation_card_num=int, combo_columns=[], callback_columns=[], callback={}):
    
    list_of_inputs = []
    table_row_final_inputs = []
    if does_alias_exist(child_tag):
        delete_item(child_tag)
    if does_alias_exist(table_name):
        delete_item(table_name)
    for last_rows in range(class_name.last_rows):

        for u in range(len(class_name.row_names)):
            if does_alias_exist(class_name.row_names[u] + str(transformation_card_num) + str(last_rows)):
                delete_item(class_name.row_names[u] + str(transformation_card_num) + str(last_rows))
            if used_in_loop:
                if does_alias_exist(class_name.row_names[u] + str(transformation_card_num) + str(loop_number) + str(last_rows)):
                    delete_item(class_name.row_names[u] + str(transformation_card_num) + str(loop_number) + str(last_rows))

    with table(tag=table_name, width=table_width, height=table_height, resizable=True, freeze_rows=freeze_rows, freeze_columns=freeze_columns, header_row=True, policy=table_policy, parent=table_parent, scrollX=True, scrollY=True):
        Widget_Aliases.tags_to_delete.append(table_name)
        list_of_inputs.append(table_name)
        for i in range(len(class_name.row_names)):
            if i in combo_columns:
                add_table_column(label=class_name.column_names[i], tag=table_name + class_name.column_names[i], init_width_or_weight=150)
                Widget_Aliases.tags_to_delete.append(table_name + class_name.column_names[i])
                list_of_inputs.append(table_name + class_name.column_names[i])
            else:
                add_table_column(label=class_name.column_names[i], tag=table_name + class_name.column_names[i])
                Widget_Aliases.tags_to_delete.append(table_name + class_name.column_names[i])
                list_of_inputs.append(table_name + class_name.column_names[i])
                
        for o in range(class_name.rows):
            with table_row(tag=row_name + str(o)):
                Widget_Aliases.tags_to_delete.append(row_name + str(o))
                list_of_inputs.append(row_name + str(o))
                pass
            
        for z in range(class_name.rows):
            table_row_inputs = []
            for t in range(len(class_name.row_names)):
                # The last number is always 0
                # print(str(z))
                # print(class_name.row_names[t] + str(z))
                ### Option to add combos
                if t in combo_columns:
                    if t in callback_columns:
                        # print(f'combo: {t}')
                        if used_in_loop:
                            add_combo(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z), items=combo_list[t], default_value=combo_list[t][0], width=149, parent=row_name + str(z), callback=callback[t])
                            Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                            list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                            table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                        else:
                            add_combo(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z), items=combo_list[t], default_value=combo_list[t][0], width=149, parent=row_name + str(z), callback=callback[t])
                            Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                            list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                            table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                    else:
                        if used_in_loop:
                            add_combo(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z), items=combo_list[t], default_value=combo_list[t][0], width=149, parent=row_name + str(z))
                            Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                            list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                            table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                        else:
                            add_combo(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z), items=combo_list[t], default_value=combo_list[t][0], width=149, parent=row_name + str(z))
                            Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                            list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                            table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                else:
                    if t in callback_columns:
                        if used_in_loop:
                            add_input_text(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z), callback=callback[t])
                            Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                            list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                            table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                        else:
                            add_input_text(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z), callback=callback[t])
                            Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                            list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                            table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                    else:
                        if used_in_loop:
                            add_input_text(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                            Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                            list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                            table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(loop_number) + str(z))
                        else:
                            add_input_text(tag=class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z), hint=class_name.column_names[t], default_value='', width=row_width, parent=row_name + str(z))
                            Widget_Aliases.tags_to_delete.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                            list_of_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                            table_row_inputs.append(class_name.row_names[t] + '_Card_' + str(transformation_card_num) + '_Row_' + str(z))
                        
    class_name.table_row_tags.append(table_row_final_inputs)
    return list_of_inputs


def Delete_Items(tag_id):
    
    if isinstance(tag_id, list):
        for i in range(len(tag_id)):
            if does_alias_exist(tag_id[i]):
                delete_item(tag_id[i])
                
    elif does_alias_exist(tag_id):
        delete_item(tag_id)

    
def Text_Resize(tag_id):
    text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIAL.ttf')
    set_item_width(tag_id, text_width + 7)
    
def Text_Resize_2(tag_id):
    text_width, text_height = get_text_size(get_value(tag_id), font='fonts/ARIAL.ttf')
    set_item_width(tag_id, text_width + 25)
    
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

# Uses the tag id returned through app_data to deduce the table number.
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
                    

def Get_Card_Number(app_data):
    import re
    match = re.search(r'\d+', app_data)
    if match:
        return match.group()
    else:
        return ''

# Returns the number of cards in the program
def Card_Checker():
    cards = 0
    while True:
        if does_alias_exist(f'Main_Card_Tab_{cards}'):
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

def Thumb_Display(card_num, state):
    # set_value(f'Card_Name_Display_{card_num}', 'Card Name')
    configure_item(f'Placeholder_Image_{card_num}', show=state)
    configure_item(f'Custom_Border_Thumb_Background_{card_num}', show=state)
    configure_item(f'card_thumb_display_{card_num}', show=state)
    configure_item(f'Custom_Border_Thumb_Border_{card_num}', show=state)
    
    
def Value_Grabber(*, class_name, tag_id=str, skill_rows=1, combo=False, combo_tag=None):
    import re
    values = []
    num_of_cards = Card_Checker()
    
    for cards in range(num_of_cards):
        for rows in range(skill_rows):
            if combo:
                values.append([re.sub(r'\D', '', get_value(tag_id)) if tag_id == combo_tag else get_value(tag_id) for i in range(len(class_name.row_names))])
            else:
                values.append([get_value(tag_id) for i in range(len(class_name.row_names))])
                
def Get_Max_Table_Row_Width(table_class, Number_of_Rows):
    widget_widths_list = []
    for row in range(Number_of_Rows):
        widget_widths = 0
        for column in range(len(table_class.row_names)):
            widget_widths += get_item_width(table_class.row_names[column] + str(row))
        widget_widths_list.append(widget_widths)
        
    
        
    # Finding the max width out of all widgets
    max_width = 0
    for width in widget_widths_list:
        max_width = width
        if width > max_width:
            max_width = width
                

        
    return max_width

def Get_Transfromation_Table_Max_Width(tag_to_check):
    widget_widths_list = []
    for row in range(1):
        widget_widths = 0
        widget_widths += get_item_width(tag_to_check)
    widget_widths_list.append(widget_widths)

def Resize_Table(table_name, rows):
    set_item_height(table_name, 24 * rows + 20)


###############################
### Alias Checking Function ###
###############################

### Will need to modify when Custom Units section gets added.
def Check_Skill(skill, card_number):
    """Takes a skill name and checks if it exists

    Args:
        skill (str): 'Leader Skill', 'Active Skill', 'Standby Skill', 'Finish Skill', 'Battle Params'
    
    Returns:
        state (bool):
    """
    ### This will only be a thing for Custom Units, so commenting out for now
    # if skill == 'Leader Skill':
        # state = does_alias_exist('')
        # pass
    if skill == 'Active Skill':
        state = does_alias_exist(f'Active_Skill_Text_Card_{card_number}')
    
    elif skill == 'Standby Skill':
        state = does_alias_exist(f'Standby_Skill_Set_Text_{card_number}_0')
    
    elif skill == 'Finish Skill':
        state = does_alias_exist(f'Finish_Skill_Set_Text_{card_number}_0')
    
    elif skill == 'Battle Params':
        state = does_alias_exist(f'Transformation_Information_Text_{card_number}_0')
    
    return state

#################################################################################################

def Clear_Class_Tags_List():
    Active_Skill.table_row_tags.clear()
    Active_Skill_Set.table_row_tags.clear()
    Causality.table_row_tags.clear()
    Dokkan_Field.table_row_tags.clear()
    Finish_Skill_Set.table_row_tags.clear()
    Finish_Skill.table_row_tags.clear()
    Leader_Skill_Info.table_row_tags.clear()
    Card_Specials.table_row_tags.clear()
    Special_Set.table_row_tags.clear()
    Specials.table_row_tags.clear()
    Standby_Skill_Set.table_row_tags.clear()
    Standby_Skill.table_row_tags.clear()
    Passive_Skill.table_row_tags.clear()
    
def Delete_Table(card, table_name, row_name, class_name):
    Delete_Items(table_name)
    for rows in range(Row_Checker(class_name.row_names[0] + '_Card_' + str(card) + '_Row_' )):
        delete_item(row_name + str(rows))
        for i in range(len(class_name.row_names)):
            delete_item(class_name.row_names[i] + '_Card_' + str(card) + '_Row_' + str(rows))
            
            
def Traceback_Logging(exception):
    ### Get the exception information
    exc_type = type(exception).__name__
    exc_value = str(exception)
    
    # Get the traceback information
    exc_traceback = exception.__traceback__
    tb_info = traceback.extract_tb(exc_traceback)
    line_number = tb_info[-1][1]
    
    log_data = f'Type: {exc_type}\nValue: {exc_value}\nLine: {line_number}'
    
    return log_data


def Config_AIO():
    import re
    home_path = Home_Path()
    conf_path = Config_Path()
    config_exist = os.path.exists(conf_path)
    print(conf_path)
    if not config_exist:
        if not os.path.exists('config/'):
            os.makedirs('config/')
        config = Config()
        
        # Database_Path = easygui.fileopenbox('Please select your decrypted database')
        Database_Path = 'database/database.db'
        cat_list = Grab_GLB_Categories()
        
        jp_cat_list = [re.search(r'\((\d+)\)', text).group(1) for text in cat_list]
        jp_cat_list = [int(item) for item in jp_cat_list]
        
        config['DEFAULT'] = {
            'discord_presence' : False,
            'database_path' : str(Database_Path),
            'module_check' : False
        }
        
        config['JP_Categories'] = {
            'categories' : jp_cat_list
        }
        
        # config['GLB_Categories'] = {
            # 'categories_list' : cat_list
        # }
        
        with open(conf_path, 'w') as f:
            config.write(f)
            
def Allow_Use_Check() -> bool:
    import requests

    url = "https://raw.githubusercontent.com/TheRagingRyan/Dokkan-Modding-Tools/main/Allow%20Use.txt"

    querystring = {"token":"GHSAT0AAAAAACHRSB7NRRPLI5Z3E57C3V26ZJUJBVA"}

    payload = ""
    headers = {"User-Agent": "Insomnia/2023.5.6"}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    check = True
    if response.text == 'False':
        check = False
    
    return check

def Dokkan_Wiki():
    import webbrowser
    
    url = 'https://dokkan.wiki/cards'
    webbrowser.open(url)
    
    
def Resize_Table_Width(card, class_name, rows, table_name):
    columns_max_widths = {}
    
    for column in range(len(class_name.row_names)):
        columns_max_widths[column] = get_item_width(class_name.row_names[column] + '_Card_' + str(card) + '_Row_0')
        for row in range(rows):
            width = get_text_size(get_value(class_name.row_names[column] + '_Card_' + str(card) + '_Row_' + str(row)), font='fonts/ARIAL.tff')[0]
            
            if width > columns_max_widths[column]:
                columns_max_widths[column] = width
                
    # All column widths added up + 60 = perfect table width
    table_width = 0
    for key, value in columns_max_widths.items():
        table_width += value + 9
    
    
    # if class_name == Passive_Skill:
        # table_width += 130
    # else:
        # table_width += 60
    
    set_item_width(table_name, table_width)
    for column in range(len(class_name.row_names)):
        for row in range(rows):
            set_item_width(class_name.row_names[column] + '_Card_' + str(card) + '_Row_' + str(row), columns_max_widths[column])


def load_JSON(file_path):

    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json_load(json_file)

    return data

def grab_card_id() -> str:
    return get_value('Custom_Query_Text_Input_0')

def read_json_from_zip(card_id: str) -> dict:
    with zipfile.ZipFile('jsons/jsons.zip', 'r') as zip_ref:
        with zip_ref.open(f'{card_id}.json') as json_file:
            return json_load(json_file)

def read_png_from_zip(card_id: str):
    with zipfile.ZipFile('thumbs/thumb.zip', 'r') as zip_ref:
        with zip_ref.open(f'card_{card_id}_thumb.png') as img_file:
            image_data = img_file.read()
            image = Image.open(BytesIO(image_data))
            return image