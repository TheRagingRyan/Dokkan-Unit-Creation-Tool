from dearpygui.dearpygui import *
from . configs import Config_Read
import sqlite3

    
class Widget_Aliases:
    tags_to_delete = []
    button_tags_to_delete = []
    
class Themes:
    Buttons = None
    
    
class Custom_Unit:
    card_number = 0
    card_id = None
    custom_execute_number = 0
    execute_all = False
    card_thumb_dict = {}
    json = False
    
class Handler_Key:
    last_key = 0
    
class Active_Skill:
    row_names = ['target_type', 'sub_target_type_set_id', 'calc_option', 'efficacy_type', 'eff_val1', 'eff_val2', 'eff_val3', 'efficacy_values', 'thumb_effect_id', 'effect_se_id']
    column_names = ['Target Type', 'Sub Target Set ID', 'Calc Option', 'Eff Type', 'Eff Val1', 'Eff Val2', 'Eff Val3', 'Eff Values', 'Thumb Effect ID', 'Effect SE ID']
    set_names = ['Active_Name_Card_0','Active_Turns','Active_Exec_Limit','Active_Causality','Active_Ultimate','Active_Special_View_ID','Active_BGM_ID']
    set_hints = ['Name', 'Turn(s)', 'Exec Limit', 'Causality', 'Ultimate Special ID', 'View ID', 'BGM ID']
    ultimate_names = ['name', 'description', 'increase_rate', 'aim_target']
    ultimate_hints = ['Name', 'Desc', 'Increase Rate', 'Aim Target']
    rows = 0
    last_rows = 0
    tags_to_delete = []
    table_row_tags = []
    
class Active_Skill_Set:
    row_names = ['Active_Skill_Set_turn', 'Active_Skill_Set_exec_limit', 'Active_Skill_Set_causality_conditions', 'Active_Skill_Set_ultimate_special_id', 'Active_Skill_Set_special_view_id', 'Active_Skill_Set_costume_special_view_id', 'Active_Skill_Set_bgm_id']
    column_names = ['Turn(s)', 'Exec Limit', 'Causality', 'Ult. Special ID', 'View ID', 'Costume View ID', 'BGM ID']
    rows = 1
    last_rows = 1
    table_row_tags = []
    
class Card:
    row_names = ['id', 'name', 'character_id', 'card_unique_info_id', 'cost', 'rarity', 'hp_init', 'hp_max', 'atk_init', 'atk_max', 'def_init', 'def_max', 'element', 'lv_max', 'skill_lv_max', 'grow_type', 'optimal_awakening_grow_type', 'price',
                    'exp_type', 'training_exp', 'special_motion', 'passive_skill_set_id', 'leader_skill_set_id', 'link_skill1_id', 'link_skill2_id', 'link_skill3_id', 'link_skill4_id', 'link_skill5_id', 'link_skill6_id', 'link_skill7_id', 
                    'eball_mod_min', 'eball_mod_num100', 'eball_mod_mid', 'eball_mod_mid_num', 'eball_mod_max', 'eball_mod_max_num', 'max_level_reward_id', 'max_level_reward_type', 'collectable_type', 'face_x', 'face_y', 'aura_id', 'aura_scale',
                    'aura_offset_x', 'aura_offset_y', 'is_aura_front', 'is_selling_only', 'awakening_number', 'resource_id', 'bg_effect_id', 'selling_exchange_point', 'awakening_element_type', 'potential_board_id']
    
    column_names = ['Card ID', 'Name', 'Character ID','Unique Info ID','Cost','Rarity','Hp Init','Hp Max','Atk Init','Atk Max','Def Init','Def Max','Element','Lv Max','Skill Lv Max','Grow Type','Opt. Awakening','Price',
                    'Exp Type','Training Exp','Special Motion','Passive Set ID','Leader Set ID','Link Skill1 ID','Link Skill2 ID','Link Skill3 ID','Link Skill4 ID','Link Skill5 ID','Link Skill6 ID','Link Skill7 ID',
                    'Eball Min','Eball Num100','Eball Mid','Eball Mid Num','Eball Max','Eball Max Num','Max Level Reward ID','Max Level Reward Type','Collectable Type','Face X','Face Y','Aura ID','Aura Scale',
                    'Aura Offset X','Aura Offset Y','Is Aura Front','Is Selling Only','Awakening Number','Resource ID','Bg Effect ID','Selling Exchange Point','Awakening Element Type','Potential Board ID']
    rows = 2
    last_rows = 2
    table_row_tags = []
    
class Causality:
    row_names = ['Causality_ID', 'Causality_Causality_Type', 'Causality_Cau_Val1', 'Causality_Cau_Val2', 'Causality_Cau_Val3']
    column_names = ['ID', 'Causality Type', 'Cau_Val1', 'Cau_Val2', 'Cau_Val3']
    rows = 1
    last_rows = 0
    causalities_list = []
    card_unique_info_set_names = {}
    causality_combo_list= ['(1) Is HP Over %','(2) Is HP Under %','(3) Ki Over #','(4) Ki Under #','(5) Past Turn #','(6) Deck Has Link Skill',
                           '(7) Enemy Has Link Skill','(8) Is ATK & DEF Over %','(9) Is ATK & DEF Under %','(10) Is HP Over % and Ki Above #',
                           '(11) Is HP Over % and Ki Below #','(12) Is HP Below % and Ki Above #','(13) Is HP Below % and Ki Below #',
                           '(14) Is First Slot','(15) Over # Enemies','(16) Under # Enemies','(17) Target Over HP %','(18) Target Under HP %',
                           '(19) Card Slot','(20) When Ki is above %','(21) When Ki is below %','(22) Character on team','(23) If # of links are active',
                           '(24) Hit Received','(25) Target Killed','(26) When HP is over % and has enough ki to super','(27) When HP is below % and has enough ki to super',
                           '(28) Checks if ID# element is on rotation','(29) Character is Enemy','(30) Check if Guarding','(31) When there are 3 or more enemy attacks',
                           '(32) When there is ID# type Ki on the field','(33) When HP is between % and %','(34) Category Card Present',
                           '(35) When the team consists of only X Class','(36) When HP is over % and battle has past turn #','(37) When HP is below % and battle has past turn #',
                           '(38) Enemy Status Effect','(39) When there is a X Class enemy','(40) Special Attack','(41) Character Name on team','(42) Ki Orbs Obtained',
                           '(43) Dodge Success','(44) Count Up','(45) Card is Name + Cat','(46) Type of Unit','(47) Revival Activated','(48) Super Attack Type',
                           '(49) When a (Super Type) is directed at the character','(51) Skill lasts for # turns from start of battle',
                           '(54) Starting from the turn in which the character\'s or an ally\'s Revival Skill is activated','(55) Starting from the # turn',
                           '(56) When normal attacks are directed at the character', '(58) Used with Dokkan Fields']
    
    table_row_tags = []
    
class Dokkan_Field:
    row_names = ['DF_exec_timing_type', 'DF_efficacy_type', 'DF_calc_option', 'DF_turn', 'DF_is_once', 'DF_probability', 'DF_eff_value1', 'DF_eff_value2', 'DF_eff_value3', 'DF_efficacy_values', 'DF_causality_conditions']
    column_names = ['Timing', 'Eff Type', 'Calc Option', 'Turn', 'Is Once', 'Prob', 'Eff Val1', 'Eff Val2', 'Eff Val3', 'Eff Values', 'Causality']
    rows = 0
    last_rows = 0
    table_row_tags = []
    
class Effect_Pack:
    row_names = ['EP_ID', 'EP_Category', 'EP_Name', 'EP_Pack_Name', 'EP_Scene_Name']
    column_names = ['ID', 'Category', 'Name', 'Pack Name', 'Scene Name']
    rows = 1
    last_rows = 0
    table_row_tags = []
    
class Finish_Skill_Set:
    row_names = ['Finish_Set_dialog_order', 'Finish_Set_dialog_images', 'Finish_Set_exec_timing_type', 'Finish_Set_exec_limit', 'Finish_Set_causality_conditions', 'Finish_Set_finish_special_id', 'Finish_Set_special_view_id', 'Finish_Set_costume_special_view_id', 'Finish_Set_bgm_id']
    column_names = ['Dialog Order', 'Dialog Images', 'Exec Timing', 'Exec Limit', 'Causality', 'Finish Special ID', 'View ID', 'Costume View ID', 'BGM ID']
    rows = 1
    last_rows = 1
    table_row_tags = []
    
class Finish_Skill:
    row_names = ['Finish_Skill_target_type', 'Finish_Skill_target_type_values', 'Finish_Skill_sub_target_type_set_id', 'Finish_Skill_turn', 'Finish_Skill_efficacy_type', 'Finish_Skill_calc_option', 'Finish_Skill_efficacy_values', 'Finish_Skill_thumb_effect_id', 'Finish_Skill_effect_se_id']
    column_names = ['Target Type', 'Target Values', 'Sub Target Set', 'Turn(s)', 'Eff Type', 'Calc Option', 'Eff Values', 'Thumb Effect ID', 'Effect SE ID']
    rows = 0
    last_rows = 0
    last_num_of_skills = 0
    table_row_tags = []
    
class Finish_Skill_Set_Test:
    row_names = ['Finish_Set_Name', 'Finish_Set_Desc', 'Finish_Set_Cond']
    column_names = ['Name', 'Desc', 'Cond']
    rows = 1
    last_rows = 1
    table_row_tags = []
    
class Leader_Skill_Info:
    import ast
    cat_list = ['DB Saga (34)', 'Saiyan Saga (86)', 'Planet Namek Saga (14)', 'Androids/Cell Saga (38)', 'Majin Buu Saga (9)',
                'Future Saga (19)', 'Universe Survival Saga (6)', 'Shadow Dragon Saga (2)', 'DAIMA (98)', 'Pure Saiyans (17)', 'Hybrid Saiyans (5)',
                'Earthlings (51)', 'Namekians (18)', 'Androids (21)', 'Artificial Life Forms (32)', "Goku's Family (30)", "Vegeta's Family (31)",
                'Wicked Bloodline (24)', 'Youth (33)', 'Peppy Gals (4)', 'Super Saiyans (36)', 'Super Saiyan 2 (45)', 'Super Saiyan 3 (12)',
                'Power Beyond Super Saiyan (84)', 'Fusion (1)', 'Potara (10)', 'Fused Fighters (85)', 'Giant Form (13)', 'Transformation Boost (23)',
                'Power Absorption (59)', 'Kamehameha (39)', 'Realm of Gods (8)', 'Full Power (20)', 'Giant Ape Power (60)', 'Majin Power (53)', 'Uncontrollable Power (94)',
                'Powerful Comeback (67)', 'Power of Wishes (90)', 'Demonic Power (93)', 'Miraculous Awakening (66)', 'Corroded Body and Mind (64)', 'Rapid Growth (54)',
                'Mastered Evolution (76)', 'Time Limit (75)', 'Final Trump Card (46)', 'Worthy Rivals (37)', 'Sworn Enemies (78)',
                'Joined Forces (28)', 'Bond of Parent and Child (87)', "Siblings' Bond (35)", 'Bond of Friendship (79)',
                'Bond of Master and Disciple (40)', 'Ginyu Force (15)', 'Team Bardock (49)', 'Universe 6 (27)',
                'Representatives of Universe 7 (22)', 'Universe 11 (56)', 'GT Heroes (72)', 'GT Bosses (73)', 'Super Heroes (88)', 'Super Bosses (92)',
                'Movie Heroes (29)', 'Movie Bosses (16)', 'Turtle School (65)', 'World Tournament (3)', 'Tournament Participants (91)' 'Earth-Bred Fighters (89)',
                'Low-Class Warrior (11)', 'Gifted Warriors (68)', 'Otherworld Warriors (44)', 'Resurrected Warriors (7)',
                'Space-Traveling Warriors (62)', 'Time Travelers (26)', 'Dragon Ball Seekers (25)', 'Successors (96)', 'Storied Figures (71)',
                'Legendary Existence (77)', 'Saviors (57)', 'Defenders of Justice (70)', 'Earth-Protecting Heroes (95)', 'Revenge (48)', 'Mission Execution (97)','Target: Goku (43)',
                'Terrifying Conquerors (41)', 'Inhuman Deeds (50)', 'Planetary Destruction (69)', 'Exploding Rage (47)',
                'Connected Hope (63)', 'Entrusted Will (81)', 'All-Out Struggle (55)', 'Battle of Wits (58)', 'Accelerated Battle (80)',
                'Battle of Fate (83)', 'Heavenly Events (74)', 'Special Pose (52)', 'Worldwide Chaos (82)', 'Crossover (61)',
                'Dragon Ball Heroes (42)']
    cat_list = sorted(cat_list)
    
    row_names = ['l_exec_timing_type', 'l_target_type', 'l_sub_target_type_set_id', 'l_causality_conditions', 'l_efficacy_type', 'l_efficacy_values', 'l_calc_option']
    column_names = ['Exec Timing', 'Target Type', 'Sub Target Set ID', 'Causality', 'Eff Type', 'Eff Values', 'Calc Option']
    input_text_widgets_hints = ['leader_skill_set_id', 'exec_timing_type', 'target_type', 'sub_target_type_set_id', 'causality_conditions', 'efficacy_type', 'efficacy_values', 'calc_option']
    leader_combo_rows = {'Element Type' : 2, 'Extreme Class' : 2, 'Super Class' : 2, 'All Types' : 2, '1 Category' : 2, '1 Category & 1 Element' : 4, '2 Categories' : 4, '2 Categories & 1 Extra' : 6, '2 Categories & 2 Extra' : 8, '3 Categories & 2 Extra' : 12, '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)' : 14}
    leader_sub_target_types_rows = {'1 Category' : 1, '1 Category & 1 Element' : 2, '2 Categories' : 3, '2 Categories & 1 Extra' : 8, '2 Categories & 2 Extra' : 15, '3 Categories & 2 Extra' : 27, '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)' : 30}
    leader_sub_target_types_sets_rows = {'1 Category' : 1, '1 Category & 1 Element' : 2, '2 Categories' : 2, '2 Categories & 1 Extra' : 4, '2 Categories & 2 Extra' : 6, '3 Categories & 2 Extra' : 9, '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)' : 10}
    leader_cat_combo_rows = {'Element Type' : 0, 'Extreme Class' : 0, 'Super Class' : 0, 'All Types' : 0, '1 Category' : 0, '1 Category & 1 Element' : 0, '2 Categories' : 1, '2 Categories & 1 Extra' : 2, '2 Categories & 2 Extra' : 3, '3 Categories & 2 Extra' : 4, '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)' : 4}
    leader_cat_combo_names = ['Element Type', 'Extreme Class', 'Super Class', 'All Types', '1 Category', '1 Category & 1 Element', '2 Categories', '2 Categories & 1 Extra', '2 Categories & 2 Extra', '3 Categories & 2 Extra', '3 Categories & 2 Extra & 1 Class (3 Categories Excluded)']
    # tags_to_remove = ['Leader_Skill_Widgets_Group_1','Leader_Skill_Text','Leader_Skill_Preset_List','Leader_Skill_Category_Selection_0','Leader_Skill_Widgets_Group_2','Leader_Efficacy_Value_Changer','Leader_Efficacy_Value_Changer_Text','Leader_Efficacy_Value_Changer_Tooltip','Leader_Skill_Widgets_Group_3','Leader_Name_Text_Input','Leader_Desc_Text_Input']
    last_cat_combo_selection = ''
    last_selection_groups = []
    last_selection_tags = []
    rows = 0
    last_rows = 0
    table_row_tags = []
    
class Card_Specials:
    row_names = ['CS_priority','CS_style','CS_lv_start','CS_eball_num_start','CS_view_id','CS_card_costume_condition_id','CS_special_bonus_id1','CS_special_bonus_lv1','CS_bonus_view_id1','CS_special_bonus_id2','CS_special_bonus_lv2','CS_bonus_view_id2','CS_causality_conditions','CS_special_asset_id']
    column_names = ['Priority','Style','Lv Start','Num Start','View ID','Cost Cond ID','Spec Bonus ID1','Spec Bonus Lv1','Bonus View ID1','Spec Bonus ID2','Spec Bonus Lv2','Bonus View ID2','Causality','Spec Asset ID']
    query_values = []
    # Card Specials is always 2 rows, putting it in the class for sake of consistent coding.
    rows = 2
    last_rows = 2
    skill_rows = []
    table_row_tags = []
    
class Special_Set:
    row_names = ['Special_Set_name','Special_Set_description','Special_Set_causality_description','Special_Set_aim_target','Special_Set_increase_rate','Special_Set_lv_bonus']
    column_names =  ['Name','Desc','Causality Desc','Aim Target','Inc Rate','Lv Bonus']
    query_tag_names = ['Special_Set_Aim_Target_Input','Special_Set_Increase_Rate_Input','Special_Set_Level_Bonus_Input']
    # Special Sets is always 1 row.
    query_values = []
    rows = 1
    last_rows = 1
    skill_rows = []
    table_row_tags = []
    
class Specials:
    row_names = ['Specials_type','Specials_efficacy_type','Specials_target_type','Specials_calc_option','Specials_turn','Specials_prob','Specials_causality_conditions','Specials_eff_value1','Specials_eff_value2','Specials_eff_value3']
    column_names = ['Type','Eff Type','Target Type','Calc Option','Turn','Prob','Causality','Eff Value1','Eff Value2','Eff Value3']
    query_values = []
    rows = 1
    last_rows = 0
    skill_rows = []
    table_row_tags = []

class Ex_Supers:
    data = {}
    
class Special_Views:
    row_names = ['SP_ID', 'SP_Script_Name', 'SP_Cut_In_Card_ID', 'SP_Special_Name_No', 'SP_Special_Motion', 'SP_Lite_Flicker_Rate', 'SP_Energy_Color', 'SP_Special_Category_ID']
    column_names = ['ID', 'Script Name', 'Cut In Card ID', 'Special Name No', 'Special Motion', 'Lite Flicker Rate', 'Energy Color', 'Special Category ID']
    rows = 1
    last_rows = 0
    table_row_tags = []
    
class Standby_Skill_Set:
    row_names = ['Standby_Set_exec_limit', 'Standby_Set_causality_conditions', 'Standby_Set_special_view_id', 'Standby_Set_costume_special_view_id', 'Standby_Set_bgm_id']
    column_names = ['Exec Limit', 'Causality', 'View ID', 'Costume View ID', 'BGM ID']
    rows = 1
    last_rows = 1
    table_row_tags = []
    
class Standby_Skill:
    row_names = ['Standby_Skill_target_type','Standby_Skill_target_type_values','Standby_Skill_sub_target_type_set_id','Standby_Skill_turn','Standby_Skill_efficacy_type','Standby_Skill_calc_option','Standby_Skill_efficacy_values','Standby_Skill_thumb_effect_id','Standby_Skill_effect_se_id']
    column_names = ['Target Type', 'Target Values', 'Sub Target ID', 'Turn', 'Eff Type', 'Calc Option', 'Eff Values', 'Thumb Effect ID', 'Effect SE ID']
    rows = 0
    last_rows = 0
    table_row_tags = []
    
class Passive_Skill:
        row_names = ['Passive_name', 'Passive_exec_timing_type', 'Passive_efficacy_type', 'Passive_target_type', 'Passive_sub_target_type_set_id', 'Passive_passive_skill_effect_id', 'Passive_calc_option', 'Passive_turn', 'Passive_is_once', 'Passive_probability', 'Passive_causality_conditions', 'Passive_eff_value1', 'Passive_eff_value2', 'Passive_eff_value3', 'Passive_efficacy_values']
        query_row_names = ['Passive_exec_timing_type', 'Passive_efficacy_type', 'Passive_target_type', 'Passive_sub_target_type_set_id', 'Passive_passive_skill_effect_id', 'Passive_calc_option', 'Passive_turn', 'Passive_is_once', 'Passive_probability', 'Passive_causality_conditions', 'Passive_eff_value1', 'Passive_eff_value2', 'Passive_eff_value3', 'Passive_efficacy_values']
        column_names = ['Name', 'Exec Timing', 'Eff Type', 'Target Type', 'Sub Target Set', 'PSE ID', 'Calc Option', 'Turn(s)', 'Is Once', 'Prob', 'Causality', 'Eff Val1', 'Eff Val2', 'Eff Val3', 'Eff Values']
        previous_row_values = []
        query_values = []
        query_values_formatted = []
        rows = 1
        last_rows = 0
        table_row_tags = []
        
class Battle_Params:
    row_names = ['param_no', 'idx', 'value']
    column_names = ['Param ID', 'idx', 'value']
    rows = 0
    last_rows = 0
    table_row_tags = []
    
class Transformation_Descriptions:
    row_names = ['skill_type', 'description']
    column_names = ['Skill Type', 'Desc']
    rows = 1
    last_rows = 0
    table_row_tags = []
        
        
def get_window_size(window):
    window_size = get_item_rect_size(window)
    return window

class Card_Table_Combos:
    rarity_combo = []
    element_combo = []
    element_dict = {}
    link_skill_combo = []
    potential_board_combo = []
    link_skill_dict = {}

    
    
class Database:
    
    """
    A class for interacting with Dokkan's Database
    
    Additional Info:
    query(*, columns, table, column_name, parameter, num_of_queries): Execute a query on the database; returns a list of values
    
    """
    
    def __init__(self):
        
        """
        Initializes the Database object.
        
        Database connection gets initialized for all methods of this class.
        Config location: 'home_path/Unit Creation Tool/config.ini
        """
        config = Config_Read()
        self.con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)    
        self.cur = self.con.cursor()
    
    def query(self, *, query='', value):
        """Queries the database

        Args:
            SELECT (str): All of the columns you want to search.
            FROM (str): Table to search in.
            WHERE (str): Column to search in.
            value (list): Value you are searching for.

        Returns:
            list: List of lists, Ex. [[X, X], [X, X]]
        """

        final_values = []
        if value:
            for i in range(len(value)):
                query = f'{query} ?'
                self.cur.execute(query, (str(value[i]), ))
                values = self.cur.fetchall()
                for tuple in range(len(values)):
                    final_values.append(['NULL' if values[tuple][z] is None else values[tuple][z] for z in range(len(values[tuple]))])
        else:
            query = f'{query}'
            self.cur.execute(query, (), )
            values = self.cur.fetchall()
            for tuple in range(len(values)):
                final_values.append(['NULL' if values[tuple][z] is None else values[tuple][z] for z in range(len(values[tuple]))])
        
        return final_values
    
    def execute_query(self, query, values=None):
        final_values = []

        if values:
            self.cur.execute(query, values)
        else:
            self.cur.execute(query)

        result = self.cur.fetchall()

        for row in result:
            final_values.append(['NULL' if value is None else value for value in row])

        return final_values
    

class Export:
    def __init__(self):
        pass
    
    def Create_RowIDs(self, num):
        """Creates Row IDs for SQL purposes

        Args:
            num (int): Used in a loop to create num amount of Row IDs

        Returns:
            list: List of Row IDs
            
        """
        
        Card_ID = int(get_value('id' + '_Card_' + '0' + '_Row_' + '1'))
        Row_IDs = []
        for i in range(num):
            Row_IDs.append(Card_ID + i)
            
        return Row_IDs
            
    def List_to_String(self, list_name):
        """Converts a (list) to a (str)

        Args:
            list_name (list)

        Returns:
            list_name (str)
        """
        list_name = ', '.join(map(str, list_name))
        
        return list_name
    
    def Add_Quotes(self, target, list_of_indexes):
        """Takes the target value and takes the values 
        from list_of_indexes, then adds qoutes around 
        those list locations for the sake of SQL formatting.
        Meant for use in the List_of_Values() method. 
        
        Args:
            target (list): list of export values.
            list_of_indexes (list): Specified index locations to implement quotes.
        """
        
        for index in range(len(list_of_indexes)):
            
            if target[list_of_indexes[index]] != 'NULL':
                target[list_of_indexes[index]] = f'\'{target[list_of_indexes[index]]}\''
                
            else:
                print(f'Export.Add_Quotes: {target[list_of_indexes[index]]} is NULL')
    
    
    def List_of_Values(self, tag_id, *, card=0, skill_number=0, Row=0, add_quotes=False, quote_indexes=[]):
        """Takes a tag id and gets the values from it's table.

        Args:
            tag_id (Class|str): Required
            card (int, optional): Card tag number. Defaults to 0.
            skill_number (int, optional): Skill tag number. Defaults to 0.
            Row (int, optional): Row of tag. Defaults to 0.

        Returns:
            str: Table Values as a string
        """
        
        if type(tag_id) == type:
            
            if get_value(tag_id.row_names[0] + '_Card_' + str(card) + '_Row_' + str(skill_number)):
                self.values = [get_value(tag_id.row_names[i] + '_Card_' + str(card) + '_Row_' + str(skill_number)) for i in range(len(tag_id.row_names))]
                if add_quotes:
                    self.Add_Quotes(self.values, quote_indexes)
                self.values = self.List_to_String(self.values)
                    
                
            elif get_value(tag_id.row_names[0] + '_Card_' + str(card) + '_Row_' + str(skill_number) + str(Row)):
                self.values = [get_value(tag_id.row_names[i] + '_Card_' + str(card) + '_Row_' + str(skill_number) + str(Row)) for i in range(len(tag_id.row_names))]
                if add_quotes:
                    self.Add_Quotes(self.values, quote_indexes)
                self.values = self.List_to_String(self.values)
                
            # Like in Standby Skill Set where there is only one row but can have multiple skiils. (Which is refected in the _Row_00 tag having a 0 for the skill number, then another 0 for the row number)    
            elif get_value(tag_id.row_names[0] + '_Card_' + str(card) + '_Row_00'):
                self.values = [get_value(tag_id.row_names[i] + '_Card_' + str(card) + '_Row_00') for i in range(len(tag_id.row_names))]
                if add_quotes:
                    self.Add_Quotes(self.values, quote_indexes)
                self.values = self.List_to_String(self.values)
        else:
            print('Not Found in Export.List_of_Values()')
            set_value('log', 'Not Found in Export.List_of_Values()')
            
        return self.values
    
class Card_Checks:
    json_data = {}
    number_of_cards = 1
    card_ids = []
    card0_data = {}
    card_specials_base_card = {}
    card_specials_main_card = {}
    card_names = []
    element_id = {}
    element_ids = {0 : 'AGL', 10 : 'AGL', 20 : 'AGL', 1 : 'TEQ', 11 : 'TEQ', 21 : 'TEQ', 2 : 'INT', 12 : 'INT', 22 : 'INT', 3 : 'STR', 13 : 'STR', 23 : 'STR', 4 : 'PHY', 14 : 'PHY', 24 : 'PHY'}
    battle_params = {}
    transformation_descriptions = {}
    passive_ids = []
    passive_names = []
    passive_descriptions = []
    special_set_ids = []
    special_set_names = []
    special_set_descriptions = []
    special_set_conditions = []
    leader_skill_id = None
    leader_skill_name = 'NULL'
    leader_skill_description = 'NULL'
    leader_skill_type = ''
    leader_skill_element_type = ''
    standby_skill_cards = {}
    standby_skill_ids = []
    standby_skill_names = []
    standby_skill_desc = []
    standby_skill_cond = []
    finish_skill_cards = {}
    finish_skill_ids = []
    finish_skill_names = []
    finish_skill_desc = []
    finish_skill_cond = []
    active_skill_ids = {}
    active_skill_name = {}
    active_skill_desc = {}
    active_skill_cond = {}
    ultimate_special_ids = {}
    dokkan_field_cards = {}
    dokkan_field_ids = []
    dokkan_field_names = []
    dokkan_field_desc = []
    dokkan_field_resource_ids = []
    json_unit_card_ids = []
    
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
                105 : '105 - Change Ki Sphere',
                106 : '106 - Potential Heal',
                107 : '107 - Delay (Stackable)',
                108 : '108 - Add Potential Skill',
                109 : '109 - Revive', 
                110 : '110 - Passive Reset', 
                111 : '111 - Disable Action', 
                112 : '112 - Immune to Attack Break', 
                113 : '113 - Threshold Damage', 
                114 : '114 - ???', 
                115 : '115 - Update Standby Mode', 
                116 : '116 - Charge Start', 
                117 : '117 - End Transformation', 
                118 : '118 - ATK Rate per Charge Count', 
                119 : '119 - Nullify Super' ,
                120 : '120 - Counter Attack',
                121 : '121 - ???',
                122 : '122 - Increased Received DMG',
                123 : '123 - ???',
                124 : '124 - ???',
                125 : '125 - ???',
                126 : '126 - ???',
                127 : '127 - ???',
                128 : '128 - ???',
                129 : '129 - ???',
                130 : '130 - ???',
                131 : '131 - Reversible Exchange',
                132 : '132 - ???',
                133 : '133 - ???'
                }
    # Any eff with a '???' is to prevent KeyErrors, I'll have to figure out what some of these eff do.

    combo_list = [value for value in eff_dict.values()]
    
class String_Length:
    
    length = {0 : 80,
    1 : 15,
    2 : 22,
    3 : 29,
    4 : 36,
    5 : 43,
    6 : 50,
    7 : 57,
    8 : 64,
    9 : 71,
    10 : 78,
    11 : 85,
    12 : 92,
    13 : 99,
    14 : 106,
    15 : 113,
    16 : 120,
    17 : 127,
    18 : 134,
    19 : 141,
    20 : 148,
    21 : 155,
    22 : 162,
    23 : 169,
    24 : 176,
    25 : 183,
    26 : 190,
    27 : 197,
    28 : 204,
    29 : 211,
    30 : 218,
    31 : 225,
    32 : 232,
    33 : 239,
    34 : 246,
    35 : 253,
    36 : 260,
    37 : 267,
    38 : 274,
    39 : 281,
    40 : 288,
    41 : 295,
    42 : 302,
    43 : 309,
    44 : 316,
    45 : 323,
    46 : 330,
    47 : 337,
    48 : 344,
    49 : 351,
    50 : 358,
    51 : 365,
    52 : 372,
    53 : 379,
    54 : 386,
    55 : 393,
    56 : 400,
    57 : 407,
    58 : 414,
    59 : 421,
    60 : 428,
    61 : 435,
    62 : 442,
    63 : 449,
    64 : 456,
    65 : 463,
    66 : 470,
    67 : 477,
    68 : 484,
    69 : 491,
    70 : 498
    }


