import get_player_table

stats_offensive_list = ['Overall Offense','Poss + Assists','Play Types','Offense Including Passes','During Pass Out Situations',
'During Trapping Situations','Shot Attempt - Half Court','Catch and Shoot - Half Court','Dribble Jumper - Half Court','Jump Shot Range - half court',
'Drive Direction (ISO Situations)','Isolation - Derived Offense',' Isolation',' ISO - Defense Commits',' Post-Up - Derived Offense',' Post-Up','Post-Up - Defense Commits',
'Post-Up - Hard Double Team','P&R - Derived Offense',' P&R Ball Handler','P&R BH - Defense Commits Info',' P&R Ball Handler - Traps',' P&R Roll Man',
'Spot-Up',' Off Screen','Hand Off','Cut','Offensive Rebounds (put backs)','Transition','Miscellaneous']

stats_defensive_list = ['Overall Defense','Play Types','Shot Attempt - Half Court',	'Catch and Shoot - Half Court','Dribble Jumper - Half Court',
'Jump Shot Range - half court','Drive Direction (ISO Situations)',' Isolation',' Post-Up',' P&R Ball Handler',' P&R Roll Man','Spot-Up',' Off Screen',
'Hand Off']

Carthage_Player_Name_List = ['Brad_Kruse','Adam_Radcliffe','Brad_Perry','Brett_Czerak','Dan_Messina','Derek_Mason_II','Dimitrije_Kastratovic',
'Jacob_Polglase','Jordan_Thomas','Jordan_Vedder','Kamal_Shasi','Kienan_Baltimore','Mike_Canady','Sean_Johnson','Steve_Leazer','Tj_Best']

Albion_Player_Name_List = ['Robert_Ryan','Corey_Wheeler','Arshawn_Parker','Jaylen_Fordham','Dylan_Bennett','Adam_Davis','Ryan_Lowe','Nathaniel_Collins','Aquavius_Burks','Caden_Ebeling',
'Ojani_Echevarria','Jamezell_Davis_Jr','Juwan_Perry','Austin_Thompson','Nathan_Kellum','Quinton_Armstrong']

Chicago_Player_Name_List = ['Jake_Fenlon','Ryan_Shearmire','Collin_Barthel','Ryan_Jacobsen','Justin_Jackson','Max_Jacobs','Noah_Karras',
'Cole_Schmitz','Mattia_Colangelo','Jake_Berhorst','Jordan_Baum','Sam_Sustacek','Dominic_Laravie','Louis_Mehaffey','Ezra_Swell','Brennan_Mcdaniel',
'Porter_Veach',]

CornellCollege_Player_Name_List = ['Brad_Hund','Corey_Davis','Dylan_Murdock','Austin_Dyer','Craig_Engle','Cody_Carter','Jan_Siegien',
'Jordan_Venters','Jon_Anderson','Keegan_Van_Kooten','Scott_Gasik','Cooper_Kabela','Jordan_Heien','Kameron_Williams','Michael_Drew','Michael_Fiorito',
'Carron_Watt','Eric_Medenblik']

Fontbonne_Player_Name_List = ['Jack_Lake','Kris_Mccann','Thomas_Ritter','James_Wiggins','Anthony_Loper','Logan_KelleyWolff','Erich_Schark',
'Jacob_Mueller','Jared_Woodcock','Tristan_Baker','Noah_Coddington','Kalin_Mitchell','Jahmad_Wilburn','Garrett_Goodnight','Luke_Deline',
'Brian_Wacha','Maguire_Scheer','Luke_Darst']

Knox_Player_Name_List = ['Dj_Lewis','Marko_Protic','Tyre_Dukes','Jonathan_Damota','Eric_Pillath','Jeremiah_Horton','Eric_Thompson','Alik_Airapetyan',
'Bryce_Wilkinson','Garrett_Stone','Jacob_Kampf','Deryk_Ruple','Blake_Godbold','Aaron_Crose','Ikenna_Ozor','Sean_Pollock','John_Tsahageas',
'Danny_Serrano']

Wabash_Player_Name_List = ['Duncan_Roy','Logan_White','Ronald_Ryan','Dalton_Vachon','Ben_Stachowski','Alex_Eberhard','Colten_Garland',
'Harrison_Hallstrom','Rhett_Helt','Jack_Davidson','Parker_Manges',' Zach_Anderson','Max_Kurkowski','Conner_Brens','Connor_Rotterman',
'Blake_Miller','Matt_Chinn','Max_Flinchum']




for p in range(len(Carthage_Player_Name_List)):
	for i in range(len(stats_offensive_list)):
		get_player_table.get_player_table('Carthage',Carthage_Player_Name_List[p].strip(),'Offensive',stats_offensive_list[i].strip())
	for m in range(len(stats_defensive_list)):
		get_player_table.get_player_table('Carthage',Carthage_Player_Name_List[p].strip(),'Defensive',stats_defensive_list[m].strip())

for p in range(len(Albion_Player_Name_List)):
	for i in range(len(stats_offensive_list)):
		get_player_table.get_player_table('Albion',Albion_Player_Name_List[p].strip(),'Offensive',stats_offensive_list[i].strip())
	for m in range(len(stats_defensive_list)):
		get_player_table.get_player_table('Albion',Albion_Player_Name_List[p].strip(),'Defensive',stats_defensive_list[m].strip())

for p in range(len(Chicago_Player_Name_List)):
	for i in range(len(stats_offensive_list)):
		get_player_table.get_player_table('Chicago',Chicago_Player_Name_List[p].strip(),'Offensive',stats_offensive_list[i].strip())
	for m in range(len(stats_defensive_list)):
		get_player_table.get_player_table('Chicago',Chicago_Player_Name_List[p].strip(),'Defensive',stats_defensive_list[m].strip())

for p in range(len(CornellCollege_Player_Name_List)):
	for i in range(len(stats_offensive_list)):
		get_player_table.get_player_table('CornellCollege',CornellCollege_Player_Name_List[p].strip(),'Offensive',stats_offensive_list[i].strip())
	for m in range(len(stats_defensive_list)):
		get_player_table.get_player_table('CornellCollege',CornellCollege_Player_Name_List[p].strip(),'Defensive',stats_defensive_list[m].strip())

for p in range(len(Fontbonne_Player_Name_List)):
	for i in range(len(stats_offensive_list)):
		get_player_table.get_player_table('Fontbonne',Fontbonne_Player_Name_List[p].strip(),'Offensive',stats_offensive_list[i].strip())
	for m in range(len(stats_defensive_list)):
		get_player_table.get_player_table('Fontbonne',Fontbonne_Player_Name_List[p].strip(),'Defensive',stats_defensive_list[m].strip())

for p in range(len(Knox_Player_Name_List)):
	for i in range(len(stats_offensive_list)):
		get_player_table.get_player_table('Knox',Knox_Player_Name_List[p].strip(),'Offensive',stats_offensive_list[i].strip())
	for m in range(len(stats_defensive_list)):
		get_player_table.get_player_table('Knox',Knox_Player_Name_List[p].strip(),'Defensive',stats_defensive_list[m].strip())

for p in range(len(Wabash_Player_Name_List)):
	for i in range(len(stats_offensive_list)):
		get_player_table.get_player_table('Wabash',Wabash_Player_Name_List[p].strip(),'Offensive',stats_offensive_list[i].strip())
	for m in range(len(stats_defensive_list)):
		get_player_table.get_player_table('Wabash',Wabash_Player_Name_List[p].strip(),'Defensive',stats_defensive_list[m].strip())