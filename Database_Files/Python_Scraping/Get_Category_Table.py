import csv
import glob
import os
import re

stats_offensive_list = ['Overall Offense','Poss + Assists','Play Types','Offense Including Passes','During Pass Out Situations',
'During Trapping Situations','Shot Attempt - Half Court','Catch and Shoot - Half Court','Dribble Jumper - Half Court',
'Jump Shot Range - half court','Drive Direction (ISO Situations)','Isolation - Derived Offense',' Isolation',
' ISO - Defense Commits',' Post-Up - Derived Offense',' Post-Up','Post-Up - Defense Commits','Post-Up - Hard Double Team',
'P&R - Derived Offense',' P&R Ball Handler','P&R BH - Defense Commits Info',' P&R Ball Handler - Traps',' P&R Roll Man',
'Spot-Up',' Off Screen','Hand Off','Cut','Offensive Rebounds (put backs)','Transition','Miscellaneous']

stats_defensive_list = ['Overall Defense']

category_table_combos = []
category_table_combo = []
category_id = 1

for i in range(len(stats_offensive_list)):
	category_table_combo = [category_id,stats_offensive_list[i]]
	category_id = category_id + 1
	category_table_combos.append(category_table_combo)

for m in range(len(stats_defensive_list)):
	category_table_combo = [category_id,stats_defensive_list[m]]
	category_table_combos.append(category_table_combo)
	category_id = category_id + 1

directory = 'C:/Users/lchen/Desktop/Category/'
if not os.path.exists(directory):
	os.makedirs(directory)
	with open(directory+'Category.csv','w', newline = '') as ft:
		a = csv.writer(ft,delimiter = ',')
		for n in range(len(category_table_combos)):
			a.writerow(category_table_combos[n])
	