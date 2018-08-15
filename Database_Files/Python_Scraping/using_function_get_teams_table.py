import scrape_team_page

stats_offensive_list = ['Overall Offense','Play Types','Offense Including Passes','During Pass Out Situations','During Trapping Situations',
'Shot Attempt - Half Court','Catch and Shoot - Half Court','Dribble Jumper - Half Court','Jump Shot Range - half court',' Overall',
' Spot Up',' P&R Ball Handler',' Post-Up',' Transition',' Offensive Rebounds (put backs)',' Isolation',' Cut',' Off Screen',' Hand Off',
' P&R Roll Man',' Miscellaneous']

stats_defensive_list = ['Overall Defense','Play Types','Offense Including Passes','During Pass Out Situations','During Trapping Situations',
'Shot Attempt - Half Court','Catch and Shoot - Half Court','Dribble Jumper - Half Court','Jump Shot Range - half court',' Overall',
' Spot Up',' P&R Ball Handler',' Post-Up',' Off Screen',' Isolation',' P&R Roll Man',' Hand Off',]


print(len(stats_offensive_list))
print(len(stats_defensive_list))


for i in range(len(stats_offensive_list)):
	#scrape_team_page.get_team_table('Fontbonne','Offensive',stats_offensive_list[i].strip())
    #scrape_team_page.get_team_table('Albion','Offensive',stats_offensive_list[i].strip())
    #scrape_team_page.get_team_table('Carthage','Offensive',stats_offensive_list[i].strip())
    #scrape_team_page.get_team_table('Chicago','Offensive',stats_offensive_list[i].strip())
    #scrape_team_page.get_team_table('CornellCollege','Offensive',stats_offensive_list[i].strip())
    #scrape_team_page.get_team_table('Knox','Offensive',stats_offensive_list[i].strip())
    scrape_team_page.get_team_table('Wabash','Offensive',stats_offensive_list[i].strip())

for p in range(len(stats_defensive_list)):
	#scrape_team_page.get_team_table('Fontbonne','Defensive',stats_defensive_list[p].strip())
    #scrape_team_page.get_team_table('Albion','Defensive',stats_defensive_list[p].strip())
    #scrape_team_page.get_team_table('Carthage','Defensive',stats_defensive_list[p].strip())
    #scrape_team_page.get_team_table('Chicago','Defensive',stats_defensive_list[p].strip())
    #scrape_team_page.get_team_table('CornellCollege','Defensive',stats_defensive_list[p].strip())
    #scrape_team_page.get_team_table('Knox','Defensive',stats_defensive_list[p].strip())
    scrape_team_page.get_team_table('Wabash','Defensive',stats_defensive_list[p].strip())


#scrape_team_page.get_team_table('Fontbonne','Cumulative','Fontbonne Griffins')
#scrape_team_page.get_team_table('Fontbonne','Cumulative','Fontbonne Griffins_1')

#scrape_team_page.get_team_table('Albion','Cumulative','Albion Britons')
#scrape_team_page.get_team_table('Albion','Cumulative','Albion Britons_1')

#scrape_team_page.get_team_table('Carthage','Cumulative','Carthage Red Men')
#scrape_team_page.get_team_table('Carthage','Cumulative','Carthage Red Men_1')

#scrape_team_page.get_team_table('Chicago','Cumulative','Chicago Maroons')
#scrape_team_page.get_team_table('Chicago','Cumulative','Chicago Maroons_1')

#scrape_team_page.get_team_table('CornellCollege','Cumulative','Cornell College Rams')
#scrape_team_page.get_team_table('CornellCollege','Cumulative','Cornell College Rams_1')

#scrape_team_page.get_team_table('Knox','Cumulative','Knox')
#scrape_team_page.get_team_table('Knox','Cumulative','Knox_1')


scrape_team_page.get_team_table('Wabash','Cumulative','Wabash College Little Giants')
scrape_team_page.get_team_table('Wabash','Cumulative','Wabash College Little Giants_1')