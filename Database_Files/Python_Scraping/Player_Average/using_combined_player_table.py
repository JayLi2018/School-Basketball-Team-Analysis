from Combine_Players_Tables import append_player_table

Albion = [ 'Adam_Davis', 'Aquavius_Burks', 'Arshawn_Parker', 'Austin_Thompson', 'Caden_Ebeling', 'Corey_Wheeler',
	'Dylan_Bennett', 'Jamezell_Davis_Jr', 'Jaylen_Fordham', 'Juwan_Perry', 'Nathaniel_Collins', 'Nathan_Kellum', 
	'Ojani_Echevarria', 'Quinton_Armstrong', 'Robert_Ryan', 'Ryan_Lowe']

Carthage = [ 'Adam_Radcliffe', 'Brad_Kruse', 'Brad_Perry', 'Brett_Czerak', 'Dan_Messina',
	'Derek_Mason_II', 'Dimitrije_Kastratovic', 'Jacob_Polglase', 'Jordan_Thomas', 'Jordan_Vedder', 'Kamal_Shasi', 
	'Kienan_Baltimore', 'Mike_Canady', 'Sean_Johnson', 'Steve_Leazer', 'Tj_Best' ]

Chicago = [ 'Brennan_Mcdaniel', 'Cole_Schmitz', 'Collin_Barthel', 'Dominic_Laravie', 'Ezra_Swell', 'Jake_Berhorst',
	'Jake_Fenlon', 'Jordan_Baum', 'Justin_Jackson', 'Louis_Mehaffey', 'Mattia_Colangelo', 'Max_Jacobs', 'Noah_Karras', 
	'Porter_Veach', 'Ryan_Jacobsen', 'Ryan_Shearmire', 'Sam_Sustacek' ]

CornellCollege = [ 'Austin_Dyer', 'Brad_Hund', 'Carron_Watt', 'Cody_Carter', 'Cooper_Kabela', 
'Corey_Davis', 'Craig_Engle', 'Dylan_Murdock', 'Eric_Medenblik', 'Jan_Siegien', 'Jon_Anderson', 
'Jordan_Heien', 'Jordan_Venters', 'Kameron_Williams', 'Keegan_Van_Kooten', 'Michael_Drew', 'Michael_Fiorito', 'Scott_Gasik']

Dominican = [ 'Andrew_Wojcik', 'Antonio_Amoah', 'Arrin_Westbrook', 'Connor_Dartt', 'Dennis_Handy', 'Domenic_Aiello', 'Isaac_Moore',
	'Jackson_Smith', 'Jonny_Woolf', 'Marin_Bandalo', 'Nick_LaVere', 'Rory_Cunningham', 'Sean_Ek', 'Tim_Robertson']

East_West = [ 'Adonis_Bell', 'Ahmad_Eshftari', 'Amare_Thurman', 'Anthony_Bonney', 'Brian_Ashberry', 
'Carl_Moore', 'Cortland_Gillespie', 'Demarques_Turner', 'Eric_Spencer', 'Jeremy_Hargrove', 'Kinsley_Shaw',
	'Manny_Coleman', 'Markus_Johnson', 'Patrick_Rucker', 'Roland_Watkins', 'Scherone_Clarke', 'Sherman_Brown', 'Sherman_Carter', 'Stanley_Thomas']

Fontbonne = [ 'Anthony_Loper', 'Brian_Wacha', 'Erich_Schark', 'Garrett_Goodnight', 'Jack_Lake', 'Jacob_Mueller', 'Jahmad_Wilburn', 
'James_Wiggins', 'Jared_Woodcock', 'Kalin_Mitchell', 'Kris_Mccann', 'Logan_KelleyWolff', 'Luke_Darst', 'Luke_Deline', 'Maguire_Scheer', 
'Noah_Coddington', 'Thomas_Ritter', 'Tristan_Baker']

Knox = [ 'Aaron_Crose', 'Alik_Airapetyan', 'Blake_Godbold', 'Bryce_Wilkinson', 'Danny_Serrano', 
'Deryk_Ruple', 'Dj_Lewis', 'Eric_Pillath', 'Eric_Thompson', 'Garrett_Stone', 'Ikenna_Ozor', 'Jacob_Kampf',
	'Jeremiah_Horton', 'John_Tsahageas', 'Jonathan_Damota', 'Marko_Protic', 'Sean_Pollock', 'Tyre_Dukes']

MoodyBible = [ 'Aaron_Brown', 'David_Arabis', 'Jacob_Kim', 'Jeremiah_Ransom', 'Jonah_Wilson', 'Jonathan_Raub', 'Joseph_Shidler',
	'Joshua_Wedeven', 'Kent_Hinrichsen', 'Keynan_Carter', 'Levi_Miller', 'Mitchell_Giedd', 'Zachary_Daniels' ]

MSOE = [ 'Anthony_Bartman', 'Bailey_Mcdaniel', 'Brian_Dorn', 'David_Llorente', 'Eddie_Harwick', 'Gabe_Wear', 
'Jake_Gebert', 'Jason_Palesse', 'Josh_Herzog', 'Lennart_Rieckmann', 'Luke_Nelson', 'Matthew_Kirmse', 
'Matt_Powers', 'Nolan_Henton', 'Sammy_Linn', 'Tegan_Miles', 'Travis_Ballard']

Roosevelt = [ 'Adam_Alexander', 'Andre_Raiford_Jr.', 'Carson_Hughes', 'Chandler_Fuzak', 'Grant_Gibson', 
'Jake_Asquini', 'Jake_Ludwig', 'Jordan_Radcliff', 'Joshua_Dillingham', 'Kevin_Day', 'Kyle_Bumbalough', 'Tariq_Archibald', 'Tomas_Cutts']

Wabash = [ 'Alex_Eberhard', 'Ben_Stachowski', 'Blake_Miller', 'Colten_Garland', 'Conner_Brens',
	'Connor_Rotterman', 'Dalton_Vachon', 'Duncan_Roy', 'Harrison_Hallstrom', 'Jack_Davidson', 'Logan_White',
		'Matt_Chinn', 'Max_Flinchum', 'Max_Kurkowski', 'Parker_Manges', 'Rhett_Helt', 'Ronald_Ryan', 'Zach_Anderson']

Wheaton = [ 'Aston_Francis', 'Cade_Alioth', 'Gavin_Hawkins', 'Jack_Bennett', 'Jay_Spencer', 'Kobe_Eichelberger',
	'Luke_Peters', 'Mark_Champion', 'Reagan_Jones', 'Ricky_Samuelson', 'Spencer_Peterson', 'Trevor_Gunter', 'Tyrel_Derrick', 'Zack_Kvam', 'Zac_Holman']

Kalamazoo = [ 'Alex_Dykema', 'Andrew_Sheckell', 'Ben_Reiter', 'Brennen_Buszka', 'Charlie_Carson', 'Dan_Black', 
'Jack_Smith', 'Jarnard_Smith', 'Jeremiah_Vincent', 'Jimmy_Paprocki', 'Jordan_Currie', 'KaLeif_Gaines', 'Merritt_Hamann',
	'Owen_Jozefowicz', 'Roger_Hood', 'Tanner_Blyly', 'Thomas_Cook' ]

NorthPark = [ 'Aaron_Reed', 'Antonio_Gardner', 'Billy_Kirby', 'Cardell_Simmons', 'Colin_Lake', 
'Dyron_Woods', 'Isaiah_Webster', 'Jack_Gurvey', 'Jarrod_Coleman', 'Jason_Hines', 'Jelani_Sankey', 
'Jonathon_Mcdonald', 'Josh_Washburn', 'Khalen_Davis', 'Matt_Mohr', 'Matt_Szuba', 'Quinn_Williams', 
'Raysean_Jones', 'Scott_Olsen', 'Toby_Marek', 'Vegard_Tangen']

UWPlatteville = [ 'Alex_Ranney', 'Carter_Voelker', 'Clay_Gerds', 'Cole_Hake', 'Colin_Connelly', 'Colin_Kramper',
	'Dan_Lowe', 'Drew_Gunnink', 'Grayson_Knowlton', 'Harold_Fay', 'Jake_Showalter', 'Justin_Jarvensivu', 'Justin_Stovall', 
	'Matt_Oestrich', 'Nathan_Cokenour', 'Quentin_Shields', 'Robert_Duax', 'Tanner_Hudziak']

OlivetCollege = [ 'Aaron_Washington', 'Angus_Bennett', 'Blake_Siersma', 'Brent_Davis', 'Chase_Brocker',
'Delbert_Redfield', 'Diangelo_Carlton', 'Eldridge_Mason', 'Griffin_Lewis', 'Jalen_Adams', 'John_Mcadoo', 
'Kylen_Brown', 'Mike_Williams', 'Quintin_Way', 'Sirafino_Davis']

Rose_Hulman = [ 'Charlie_Aimone', 'David_Saadatnezhadi', 'Eli_Combs', 'Jacob_Back', 'John_Czarnecki',
	'Joshua_Richey', 'JT_Whitaker', 'Kyle_Steckel', 'Luke_Callahan', 'Michael_Lake', 'Nick_McGrail',
		'Ryuji_Aoki', 'Stephen_Schueth', 'Taylor_Heil', 'Trey_Sykes']

GustavusAdolphus = ['Austin_Goetz', 'Brandon_Snoberger', 'Charlie_Krambeer', 'CJ_Woda', 'Jason_Faul', 
'Kelsey_Thomas', 'Leif_Engen', 'Peter_Lundquist', 'Riley_Sharbono', 'Sam_DuBois', 'Schuyler_Thompson', 
	'Spencer_Tollefson', 'Vannis_Smith', 'Zach_Bloemker']

Illinois_Tech = [ 'Anthony_Mosley', 'Brett_Ott', 'Brinden_Carlson', 'Calvin_Schmitz', 'Capriest_Gardner',
	'Jake_Digiorgio', 'Jake_Bruns', 'Jason_Morris', 'Kohl_Linder', 'Malik_Howze', 'Max_Hisatake', 'Parker_Joncus', 'Quentin_Forberg']

School_List = []
School_List.extend(['Albion', 'Carthage', 'Chicago', 'CornellCollege', 'Dominican', 'East_West', 'Fontbonne',
	'Knox', 'MoodyBible', 'MSOE', 'Roosevelt', 'Wabash', 'Wheaton', 'Kalamazoo', 'NorthPark', 'UWPlatteville',
	'OlivetCollege', 'Rose_Hulman', 'GustavusAdolphus', 'Illinois_Tech'])

# number_of_players = 0
# number_of_players =len(Albion)+len(Carthage)+len(Chicago)+len(CornellCollege)+len(Dominican)+len(East_West)+len(Knox)+len(MoodyBible)+len(MSOE)+len(Roosevelt)+len(Wabash)+len(Wheaton)+len(Fontbonne)+len(Kalamazoo)+len(NorthPark)+len(UWPlatteville)+len(OlivetCollege)+len(Rose_Hulman)+len(GustavusAdolphus)+len(Illinois_Tech)
# print('number_of_players: '+str(number_of_players))

print('1')
for m in range(len(Albion)):
	append_player_table('Albion',Albion[m])
print('2')
for m in range(len(Carthage)):
	append_player_table('Carthage',Carthage[m])		
print('3')
for m in range(len(Chicago)):
	append_player_table('Chicago',Chicago[m])
print('4')
for m in range(len(CornellCollege)):
	append_player_table('CornellCollege',CornellCollege[m])
print('5')
for m in range(len(Dominican)):
	append_player_table('Dominican',Dominican[m])
print('6')
for m in range(len(East_West)):
	append_player_table('East_West',East_West[m])		
print('7')
for m in range(len(Knox)):
	append_player_table('Knox',Knox[m])
print('8')
for m in range(len(MoodyBible)):
	append_player_table('MoodyBible',MoodyBible[m])
print('9')
for m in range(len(MSOE)):
	append_player_table('MSOE',MSOE[m])
print('10')
for m in range(len(Roosevelt)):
	append_player_table('Roosevelt',Roosevelt[m])		
print('11')
for m in range(len(Wabash)):
	append_player_table('Wabash',Wabash[m])
print('12')
for m in range(len(Wheaton)):
	append_player_table('Wheaton',Wheaton[m])
print('13')
for m in range(len(Fontbonne)):
	append_player_table('Fontbonne',Fontbonne[m])
print('14')
for m in range(len(Kalamazoo)):
	append_player_table('Kalamazoo',Kalamazoo[m])
print('15')
for m in range(len(NorthPark)):
	append_player_table('NorthPark',NorthPark[m])
print('16')
for m in range(len(UWPlatteville)):
	append_player_table('UWPlatteville',UWPlatteville[m])
print('17')
for m in range(len(OlivetCollege)):
	append_player_table('OlivetCollege',OlivetCollege[m])
print('18')
for m in range(len(Rose_Hulman)):
	append_player_table('Rose_Hulman',Rose_Hulman[m])
print('19')
for m in range(len(GustavusAdolphus)):
	append_player_table('GustavusAdolphus',GustavusAdolphus[m])
print('20')
for m in range(len(Illinois_Tech)):
	append_player_table('Illinois_Tech',Illinois_Tech[m])

