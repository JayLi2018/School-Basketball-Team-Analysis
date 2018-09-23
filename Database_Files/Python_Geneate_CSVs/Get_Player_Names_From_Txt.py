#use this program to get all the players name in text files

import glob
import os
import re
import csv

# directory format  = 'C:/Users/lchen/Desktop/school_raw_data/'+school_name+'/'

# school_name_list = ['Albion','Carthage','Chicago','CornellCollege','Dominican','East_West','Fontbonne','Knox','MoodyBible','MSOE',
# 'Roosevelt','Wabash','Wheaton','Kalamazoo','NorthPark','UWPlatteville','OlivetCollege','Rose_Hulman','GustavusAdolphus','Illinois Tech']

school_name_list = ['Trine']


player_name_list = []
player_and_ID_pairs = []

for m in range(len(school_name_list)):
	print('\''+school_name_list[m]+'\',',end =' ')

for i in range(len(school_name_list)):
	os.chdir('C:/Users/lchen/Desktop/Player_Raw_Data/'+school_name_list[i]+'/')
	print(school_name_list[i]+' = [',end = ' ')
	for file in glob.glob("*.txt"):
		filename = str(file)
		try:
			found = re.search('(.*)_Offensive',filename).group(1)
			print('\''+found+'\',',end = ' ')
			player_name_list.append(found)
		except AttributeError:
			found = ''
	print(']')

#this is first player's id
# player_id = 1

# for m in range(len(player_name_list)):	
# 	player_and_ID_pair = [player_name_list[m],player_id]
# 	player_and_ID_pairs.append(player_and_ID_pair)
# 	player_id = player_id+1

# directory = 'C:/Users/lchen/Desktop/Player/'
# if not os.path.exists(directory):
# 	os.makedirs(directory)
# 	with open(directory+'player.csv','w', newline = '') as ft:
# 		a = csv.writer(ft,delimiter = ',')
# 		for n in range(len(player_and_ID_pairs)):
# 			a.writerow(player_and_ID_pairs[n])


		









		

			

