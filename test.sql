-- Super Saiyan 3 Goku & Super Saiyan 2 Vegeta
	-- Cards
    	INSERT OR REPLACE INTO cards ("id", "name", "character_id", "card_unique_info_id", "cost", "rarity", "hp_init", "hp_max", "atk_init", "atk_max", "def_init", "def_max", "element", "lv_max", "skill_lv_max", "grow_type", "optimal_awakening_grow_type", "price", "exp_type", "training_exp", "special_motion", "passive_skill_set_id", "leader_skill_set_id", "link_skill1_id", "link_skill2_id", "link_skill3_id", "link_skill4_id", "link_skill5_id", "link_skill6_id", "link_skill7_id", "eball_mod_min", "eball_mod_num100", "eball_mod_mid", "eball_mod_mid_num", "eball_mod_max", "eball_mod_max_num", "max_level_reward_id", "max_level_reward_type", "collectable_type", "face_x", "face_y", "aura_id", "aura_scale", "aura_offset_x", "aura_offset_y", "is_aura_front", "is_selling_only", "awakening_number", "resource_id", "bg_effect_id", "selling_exchange_point", "awakening_element_type", "potential_board_id", "open_at", "created_at", "updated_at")
    	VALUES
		(1325730, 'Super Saiyan 3 Goku & Super Saiyan 2 Vegeta', 1315, 715, 77, 5, 5185, 17113, 4860, 16040, 2733, 9019, 14, 150, 20, 50, NULL, 50176, 25, 7980, 1, 3353, 102573, 22, 9, 29, 30, 97, 109, 125, 40, 3, 160, 12, 200, 24, 1, 1, 1, 336, 769, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, 1025730, 15000, 1, 24, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325731, 'Super Saiyan 3 Goku & Super Saiyan 2 Vegeta', 1315, 715, 77, 5, 5185, 17113, 4860, 16040, 2733, 9019, 14, 150, 20, 50, NULL, 50176, 25, 7980, 1, 3353, 102573, 22, 9, 29, 30, 97, 109, 125, 40, 3, 160, 12, 200, 24, 1, 1, 1, 336, 769, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, 1025730, 15000, 1, 24, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(4325740, 'Goku & Vegeta', 1316, 716, 77, 5, 5185, 17113, 4860, 16040, 2733, 9019, 14, 150, 20, 50, NULL, 50176, 25, 7980, 0, 3354, 102573, 22, 30, 34, 52, 97, 109, 125, 40, 3, 160, 12, 200, 24, 1, 1, 1, 336, 769, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, 4025740, 15000, 1, 24, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325741, 'Goku & Vegeta', 1316, 716, 77, 5, 5185, 17113, 4860, 16040, 2733, 9019, 14, 150, 20, 50, NULL, 50176, 25, 7980, 0, 3354, 102573, 22, 30, 34, 52, 97, 109, 125, 40, 3, 160, 12, 200, 24, 1, 1, 1, 336, 769, NULL, NULL, NULL, NULL, 0, 0, NULL, NULL, 4025740, 15000, 1, 24, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	-- Passive Skill (passive_skill_sets, passive_skill_effects, passive_skills, passive_skill_set_relations, transformation_descriptions)
    	INSERT OR REPLACE INTO passive_skill_sets ("id", "name", "itemized_description", "created_at", "updated_at")
    	VALUES
		(1325731, 'Full-Power Final Battle', 'ATK & DEF +200%; plus an additional ATK & DEF +50% when ' || char(10) ||
		'HP is 50% or more; plus an additional Ki +1 per Ki Sphere ' || char(10) ||
		'obtained and an additional DEF +100% as the 1st attacker ' || char(10) ||
		'in a turn; plus an additional Ki +2 per Ki Sphere obtained ' || char(10) ||
		'and an additional ATK +100% as the 2nd or 3rd attacker in ' || char(10) ||
		'a turn; launches an additional attack that has a great chance ' || char(10) ||
		'of becoming a Super Attack when Ki is 18 or more; launches ' || char(10) ||
		'an additional Super Attack when Ki is 24; Ki +1 and chance ' || char(10) ||
		'of performing a critical hit +10% (up to 50%) with each ' || char(10) ||
		'Super Attack performed', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(4325741, 'Keep the Hope Alive!', 'Unable to attack except when Finish Effect is activated; ' || char(10) ||
		'DEF +250%; guards all attacks and randomly changes Ki Spheres ' || char(10) ||
		'of a certain Type to Rainbow Ki Spheres for 4 turns from ' || char(10) ||
		'start of turn; reduces damage received by 8% per Ki Sphere ' || char(10) ||
		'obtained; ATK +500% when Finish Effect is activated', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO passive_skills ("id", "name", "description", "exec_timing_type", "efficacy_type", "target_type", "sub_target_type_set_id", "passive_skill_effect_id", "calc_option", "turn", "is_once", "probability", "causality_conditions", "eff_value1", "eff_value2", "eff_value3", "efficacy_values", "created_at", "updated_at")
    	VALUES
		(1325731, 'Full-Power Final Battle', '.', 1, 3, 1, 0, NULL, 2, 1, 0, 100, NULL, 200, 200, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325732, 'Full-Power Final Battle', '.', 1, 3, 1, 0, NULL, 2, 1, 0, 100, '{"source": "2128", "compiled": 2128}', 50, 50, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325733, 'Full-Power Final Battle', '.', 11, 2, 1, 0, NULL, 2, 1, 0, 100, '{"source": "2122", "compiled": 2122}', 100, 0, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325734, 'Full-Power Final Battle', '.', 15, 96, 1, 0, NULL, 0, 1, 0, 100, '{"source": "2122", "compiled": 2122}', 63, 1, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325735, 'Full-Power Final Battle', '.', 11, 1, 1, 0, NULL, 2, 1, 0, 100, '{"source": "2123|2124", "compiled": ["|", 2123, 2124]}', 100, 0, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325736, 'Full-Power Final Battle', '.', 15, 96, 1, 0, NULL, 0, 1, 0, 100, '{"source": "2123|2124", "compiled": ["|", 2123, 2124]}', 63, 2, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325737, 'Full-Power Final Battle', '.', 4, 81, 1, 0, NULL, 0, 1, 0, 100, '{"source": "2126", "compiled": 2126}', 0, 0, 70, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325738, 'Full-Power Final Battle', '.', 4, 81, 1, 0, NULL, 0, 1, 0, 100, '{"source": "2127", "compiled": 2127}', 0, 0, 100, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325739, 'Full-Power Final Battle', '.', 5, 98, 1, 0, NULL, 0, 99, 0, 100, '{"source": "2125", "compiled": 2125}', 1, 99, 5, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325740, 'Full-Power Final Battle', '.', 5, 98, 1, 0, NULL, 2, 99, 0, 100, '{"source": "2125", "compiled": 2125}', 10, 50, 2, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325741, 'Full-Power Final Battle', '.', 1, 13, 1, 0, NULL, 0, 1, 0, 100, NULL, 100, 0, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(4325741, 'Keep the Hope Alive!', '.', 1, 114, 1, 0, NULL, 0, 1, 0, 100, NULL, 0, 0, 0, '{"text": "守りの姿勢を取っている", "script_path": "lua/ab_script/ab_sys/cannot_attack.lua"}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325742, 'Keep the Hope Alive!', '.', 1, 2, 1, 0, NULL, 2, 1, 0, 100, NULL, 250, 0, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325743, 'Keep the Hope Alive!', '.', 1, 78, 1, 0, NULL, 0, 4, 1, 100, NULL, 0, 0, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325744, 'Keep the Hope Alive!', '.', 1, 67, 1, 0, NULL, 0, 4, 1, 100, NULL, 31, 32, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325745, 'Keep the Hope Alive!', '.', 1, 68, 1, 0, NULL, 2, 1, 0, 100, NULL, 63, 6, 8, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325746, 'Keep the Hope Alive!', '.', 4, 1, 1, 0, NULL, 2, 1, 0, 100, NULL, 500, 0, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325747, 'Keep the Hope Alive!', '.', 5, 110, 1, 0, NULL, 0, 1, 0, 100, NULL, 15, 12, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325748, 'Keep the Hope Alive!', '.', 5, 110, 1, 0, NULL, 0, 1, 0, 100, NULL, 15, 16, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325749, 'Keep the Hope Alive!', '.', 12, 117, 1, 0, NULL, 0, 1, 0, 100, '{"source": "2121", "compiled": 2121}', 0, 0, 0, '{}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO passive_skill_set_relations ("id", "passive_skill_set_id", "passive_skill_id", "created_at", "updated_at")
    	VALUES
		(1325731, 1325731, 1325731, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325732, 1325731, 1325732, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325733, 1325731, 1325733, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325734, 1325731, 1325734, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325735, 1325731, 1325735, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325736, 1325731, 1325736, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325737, 1325731, 1325737, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325738, 1325731, 1325738, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325739, 1325731, 1325739, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325740, 1325731, 1325740, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325741, 1325731, 1325741, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(4325741, 4325741, 4325741, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325742, 4325741, 4325742, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325743, 4325741, 4325743, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325744, 4325741, 4325744, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325745, 4325741, 4325745, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325746, 4325741, 4325746, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325747, 4325741, 4325747, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325748, 4325741, 4325748, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325749, 4325741, 4325749, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	-- Specials (card_specials, specials, special_sets, special_views)
    	INSERT OR REPLACE INTO card_specials ("id", "card_id", "special_set_id", "priority", "style", "lv_start", "eball_num_start", "view_id", "card_costume_condition_id", "special_bonus_id1", "special_bonus_lv1", "bonus_view_id1", "special_bonus_id2", "special_bonus_lv2", "bonus_view_id2", "causality_conditions", "special_asset_id", "created_at", "updated_at")
    	VALUES
		(1325731, 1325730, 1325731, 0, 'Normal', 0, 12, 11410, 0, 5, 20, 0, 0, 0, 0, NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325732, 1325731, 1325731, 0, 'Normal', 0, 12, 11411, 0, 5, 20, 0, 0, 0, 0, NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(1325733, 1325730, 1325732, 0, 'Hyper', 0, 18, 11412, 0, 5, 20, 0, 0, 0, 0, NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325734, 1325731, 1325732, 0, 'Hyper', 0, 18, 11413, 0, 5, 20, 0, 0, 0, 0, NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO special_sets ("id", "name", "description", "causality_description", "aim_target", "increase_rate", "lv_bonus", "is_inactive", "created_at", "updated_at")
    	VALUES
		(1325731, 'Cooperation Between Rivals', 'Raises DEF, raises ATK for 1 turn and causes colossal ' || char(10) ||
		'damage to enemy', 'NULL', 0, 200, 5, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(1325732, 'Full Power Energy Rush', 'Greatly raises DEF, greatly raises ATK for 1 turn ' || char(10) ||
		'and causes mega-colossal damage to enemy', 'NULL', 0, 250, 10, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO specials ("id", "special_set_id", "type", "efficacy_type", "target_type", "calc_option", "turn", "prob", "causality_conditions", "eff_value1", "eff_value2", "eff_value3", "created_at", "updated_at")
    	VALUES
		(1325731, 1325731, 'Special::NormalEfficacySpecial', 2, 1, 2, 99, 100, NULL, 30, 0, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325732, 1325731, 'Special::NormalEfficacySpecial', 1, 1, 2, 1, 100, NULL, 30, 0, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(1325733, 1325732, 'Special::NormalEfficacySpecial', 2, 1, 2, 99, 100, NULL, 50, 0, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325734, 1325732, 'Special::NormalEfficacySpecial', 1, 1, 2, 1, 100, NULL, 50, 0, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	-- Standby Skill
    	INSERT OR REPLACE INTO standby_skill_sets ("id", "name", "effect_description", "condition_description", "exec_limit", "causality_conditions", "special_view_id", "costume_special_view_id", "bgm_id", "created_at", "updated_at")
    	VALUES
		(1325730, 'Enters Standby Mode', 'Stands by for 5 turns, during which charge count ' || char(10) ||
		'increases by 1 per Ki Sphere obtained by allies', 'Can be activated when HP is 50% or less, or starting ' || char(10) ||
		'from the 4th turn from the start of battle if ' || char(10) ||
		'the character performs 4 or more attacks in battle ' || char(10) ||
		'(once only)', 1, '["|", ["&", ["not", ["type", 53, [0]]], ["type", 2, [50]]], ["&", ["not", ["type", 53, [0]]], ["type", 5, [3]], ["type", 44, [2, 4]]]]', 11583, 0, 232, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(1325731, 'Enters Standby Mode', 'Stands by for 5 turns, during which charge count ' || char(10) ||
		'increases by 1 per Ki Sphere obtained by allies', 'Can be activated when HP is 50% or less, or starting ' || char(10) ||
		'from the 4th turn from the start of battle if ' || char(10) ||
		'the character performs 4 or more attacks in battle ' || char(10) ||
		'(once only)', 1, '["|", ["&", ["not", ["type", 53, [0]]], ["type", 2, [50]]], ["&", ["not", ["type", 53, [0]]], ["type", 5, [3]], ["type", 44, [2, 4]]]]', 11583, 0, 232, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO standby_skills ("id", "standby_skill_set_id", "target_type", "target_type_values", "sub_target_type_set_id", "turn", "efficacy_type", "calc_option", "efficacy_values", "thumb_effect_id", "effect_se_id", "created_at", "updated_at")
    	VALUES
		(1325731, 1325730, 1, '{}', 0, 5, 115, NULL, '{"type": "charge", "is_active": true}', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325732, 1325730, 1, '{}', 0, 5, 116, NULL, '{"type": "energy_ball", "gauge_value": [39], "count_multiplier": 20, "max_effect_value": 6440}', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325733, 1325730, 1, '{}', 0, 1, 103, NULL, '[4325740, 0, 4325740]', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(1325734, 1325731, 1, '{}', 0, 5, 115, NULL, '{"type": "charge", "is_active": true}', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325735, 1325731, 1, '{}', 0, 5, 116, NULL, '{"type": "energy_ball", "gauge_value": [39], "count_multiplier": 20, "max_effect_value": 6440}', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325736, 1325731, 1, '{}', 0, 1, 103, NULL, '[4325741, 0, 4325741]', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO finish_skill_sets ("id", "name", "effect_description", "condition_description", "dialog_order", "dialog_images", "exec_timing_type", "exec_limit", "causality_conditions", "finish_special_id", "special_view_id", "costume_special_view_id", "bgm_id", "is_dialog_view_visible", "created_at", "updated_at")
    	VALUES
		(4325740, 'Spirit Bomb', 'Raises ATK by 15% temporarily per charge count ' || char(10) ||
		'and causes ultimate damage to enemy', 'Can be activated when charge count is 38 or less ' || char(10) ||
		'(once only)', 0, '{"bg": "com_chara_info_bg_blue.png", "label": "sp_atk_label_a_0004_a.png", "label_bg": "com_base_atk_blue.png"}', 0, 1, '["&", ["type", 55, [1]], ["<", ["type", 52], ["int", 39]]]', 4325740, 11585, 0, 233, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(4325741, 'Super Spirit Bomb', 'Raises ATK by 20% temporarily per charge count ' || char(10) ||
		'and causes super-ultimate damage to enemy', 'Can be activated when charge count is 39 or more ' || char(10) ||
		'(once only)', 10, '{"bg": "com_chara_info_bg_blue.png", "label": "sp_atk_label_a_0004_a.png", "label_bg": "com_base_atk_blue.png"}', 0, 1, '["&", ["type", 55, [1]], [">=", ["type", 52], ["int", 39]]]', 4325741, 11586, 0, 234, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

	-- Finish Skill
    	INSERT OR REPLACE INTO finish_skills ("id", "finish_skill_set_id", "target_type", "target_type_values", "sub_target_type_set_id", "turn", "efficacy_type", "calc_option", "efficacy_values", "thumb_effect_id", "effect_se_id", "created_at", "updated_at")
    	VALUES
		(4325740, 4325740, 1, '{}', 0, 1, 115, NULL, '{"type": "charge", "is_active": false}', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325741, 4325740, 1, '{}', 0, 1, 116, NULL, '{"is_active": false}', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325742, 4325740, 1, '{}', 0, 1, 117, NULL, '[0, 0, 0]', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325743, 4325740, 1, '{}', 0, 1, 118, NULL, '[15, 570, 0]', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(4325744, 4325741, 1, '{}', 0, 1, 115, NULL, '{"type": "charge", "is_active": false}', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325745, 4325741, 1, '{}', 0, 1, 116, NULL, '{"is_active": false}', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325746, 4325741, 1, '{}', 0, 1, 117, NULL, '[0, 0, 0]', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325747, 4325741, 1, '{}', 0, 1, 118, NULL, '[20, 6440, 0]', NULL, NULL, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO finish_specials ("id", "increase_rate", "aim_target", "created_at", "updated_at")
    	VALUES
		(4325740, 550, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325741, 750, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

	-- Standby/Finish Relations
    	INSERT OR REPLACE INTO card_standby_skill_set_relations ("id", "card_id", "standby_skill_set_id", "created_at", "updated_at")
		VALUES
		(1325730, 1325730, 1325730, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325731, 1325731, 1325731, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO card_finish_skill_set_relations ("id", "card_id", "finish_skill_set_id", "created_at", "updated_at")
    	VALUES
		(4325741, 4325741, 4325740, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325742, 4325741, 4325741, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO standby_skill_set_finish_skill_set_relations ("id", "standby_skill_set_id", "finish_skill_set_id", "created_at", "updated_at")
    	VALUES
		(4325741, 1325730, 4325740, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325742, 1325731, 4325740, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325743, 1325730, 4325741, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325744, 1325731, 4325741, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	-- Battle Params
    	INSERT OR REPLACE INTO battle_params ("id", "param_no", "idx", "value", "created_at", "updated_at")
    	VALUES
		(1325731, 1700, 0, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325732, 1700, 1, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325733, 1700, 2, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325734, 1700, 3, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325735, 1700, 4, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325736, 1700, 5, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325737, 1700, 6, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325738, 1700, 7, 23, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325739, 1700, 8, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(4325741, 1700, 0, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325742, 1700, 1, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325743, 1700, 2, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325744, 1700, 3, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325745, 1700, 4, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325746, 1700, 5, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325747, 1700, 6, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325748, 1700, 7, 23, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325749, 1700, 8, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	-- Leader Skill
    	INSERT OR REPLACE INTO leader_skill_sets ("id", "name", "description", "created_at", "updated_at")
    	VALUES
		(1325731, 'Universe''s Last Hope', '"Power of Wishes" or "Final Trump Card" Category ' || char(10) ||
		'Ki +3 and HP, ATK & DEF +170%, plus an additional ' || char(10) ||
		'HP, ATK & DEF +30% for characters who also belong ' || char(10) ||
		'to the "Connected Hope" or "Majin Buu Saga" Category', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(4325741, 'Universe''s Last Hope', '"Power of Wishes" or "Final Trump Card" Category ' || char(10) ||
		'Ki +3 and HP, ATK & DEF +170%, plus an additional ' || char(10) ||
		'HP, ATK & DEF +30% for characters who also belong ' || char(10) ||
		'to the "Connected Hope" or "Majin Buu Saga" Category', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO leader_skills ("id", "leader_skill_set_id", "exec_timing_type", "target_type", "sub_target_type_set_id", "causality_conditions", "efficacy_type", "efficacy_values", "calc_option", "created_at", "updated_at")
    	VALUES
		(1325731, 1325731, 1, 2, 342, NULL, 5, '[3, 0, 0]', 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325732, 1325731, 1, 2, 342, NULL, 82, '[31, 170, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325733, 1325731, 1, 2, 343, NULL, 5, '[3, 0, 0]', 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325734, 1325731, 1, 2, 343, NULL, 82, '[31, 170, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325735, 1325731, 1, 2, 344, NULL, 82, '[31, 30, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325736, 1325731, 1, 2, 345, NULL, 82, '[31, 30, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325737, 1325731, 1, 2, 346, NULL, 82, '[31, 30, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325738, 1325731, 1, 2, 347, NULL, 82, '[31, 30, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(4325741, 4325741, 1, 2, 342, NULL, 5, '[3, 0, 0]', 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325742, 4325741, 1, 2, 342, NULL, 82, '[31, 170, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325743, 4325741, 1, 2, 343, NULL, 5, '[3, 0, 0]', 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325744, 4325741, 1, 2, 343, NULL, 82, '[31, 170, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325745, 4325741, 1, 2, 344, NULL, 82, '[31, 30, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325746, 4325741, 1, 2, 345, NULL, 82, '[31, 30, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325747, 4325741, 1, 2, 346, NULL, 82, '[31, 30, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325748, 4325741, 1, 2, 347, NULL, 82, '[31, 30, 0]', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

	INSERT OR REPLACE INTO sub_target_types ("id", "sub_target_type_set_id", "target_value_type", "target_value", "created_at", "updated_at")
    	VALUES
		(1325731, 13257311, 1, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325732, 13257312, 2, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325733, 13257312, 1, 46, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325734, 13257313, 1, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325735, 13257313, 1, 63, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325736, 13257314, 1, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325737, 13257314, 2, 63, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325738, 13257314, 1, 9, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325739, 13257315, 2, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325740, 13257315, 1, 46, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325741, 13257315, 1, 63, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325742, 13257315, 2, 9, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325743, 13257316, 1, 46, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325744, 13257316, 2, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(1325745, 13257316, 1, 9, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),

		(4325741, 43257411, 1, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325742, 43257412, 2, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325743, 43257412, 1, 46, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325744, 43257413, 1, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325745, 43257413, 1, 63, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325746, 43257414, 1, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325747, 43257414, 2, 63, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325748, 43257414, 1, 9, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325749, 43257415, 2, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325750, 43257415, 1, 46, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325751, 43257415, 1, 63, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325752, 43257415, 2, 9, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325753, 43257416, 1, 46, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325754, 43257416, 2, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(4325755, 43257416, 1, 9, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

		INSERT OR REPLACE INTO sub_target_type_sets ("id", "created_at", "updated_at")
    	VALUES
		(13257311, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(13257312, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(13257313, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(13257314, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(13257315, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
		(13257316, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	-- Card Categories
    	INSERT OR REPLACE INTO card_card_categories (id, card_id, card_category_id, num, created_at, updated_at)
    	VALUES
		(1325730001,1325730,9,1, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730002,1325730,17,2, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730003,1325730,28,3, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730004,1325730,46,4, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730005,1325730,55,5, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730006,1325730,58,6, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730007,1325730,63,7, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730008,1325730,76,8, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730009,1325730,83,9, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730010,1325730,84,10, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730011,1325730,87,11, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325730012,1325730,90,12, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),

		(1325731001,1325731,9,1, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731002,1325731,17,2, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731003,1325731,28,3, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731004,1325731,46,4, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731005,1325731,55,5, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731006,1325731,58,6, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731007,1325731,63,7, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731008,1325731,76,8, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731009,1325731,83,9, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731010,1325731,84,10, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731011,1325731,87,11, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(1325731012,1325731,90,12, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),


		(4325740001,4325740,9,1, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740002,4325740,17,2, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740003,4325740,28,3, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740004,4325740,46,4, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740005,4325740,55,5, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740006,4325740,58,6, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740007,4325740,63,7, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740008,4325740,76,8, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740009,4325740,83,9, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740010,4325740,84,10, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740011,4325740,87,11, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325740012,4325740,90,12, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),

		(4325741001,4325741,9,1, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741002,4325741,17,2, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741003,4325741,28,3, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741004,4325741,46,4, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741005,4325741,55,5, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741006,4325741,58,6, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741007,4325741,63,7, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741008,4325741,76,8, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741009,4325741,83,9, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741010,4325741,84,10, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741011,4325741,87,11, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP),
		(4325741012,4325741,90,12, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
