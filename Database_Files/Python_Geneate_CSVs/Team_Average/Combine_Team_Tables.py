# automatically convert txt to csv
import re
import csv
import os
import fileinput
import pandas as pd 

# stats_offensive_list = ['Shot Attempt - Half Court']

stats_offensive_list = ['Overall Offense','Play Types','Offense Including Passes','During Pass Out Situations',
'During Trapping Situations','Catch and Shoot - Half Court','Dribble Jumper - Half Court',
'Jump Shot Range - half court']

# stats_defensive_list = ['Shot Attempt - Half Court']


stats_defensive_list = ['Overall Defense','Play Types','Offense Including Passes','During Pass Out Situations','During Trapping Situations',
'Catch and Shoot - Half Court','Dribble Jumper - Half Court','Jump Shot Range - half court']
# print(len(stats_offensive_list))

def append_team_table(school_name):
 
	file_needed_1  = open("C:/Users/lchen/Desktop/Teams_Raw_Data1/"+school_name+'_'+'Offensive'+".txt","r")

	file_needed_2  = open("C:/Users/lchen/Desktop/Teams_Raw_Data1/"+school_name+'_'+'Defensive'+".txt","r")
	



	for m in range(len(stats_offensive_list)):


		in_table = False
		in_row = False
		in_columns = False
		end_of_table = False

		in_columns_sign = re.compile(r'([^\t])')
		in_rows_sign = re.compile(r'([\t])')
		end_of_table_sign = re.compile(r'^\s*$')
		
		row_1 =[]
		columns_1 = []
		format_id = 1
		for line in file_needed_1:
			if(in_table and end_of_table):
				break
			else:
				in_columns = bool(in_columns_sign.search(line))
			
				#print("in_columns: "+str(in_columns))

				in_row = bool(in_rows_sign.search(line))
			
				#print("in_row: "+str(in_row))

				end_of_table = bool(end_of_table_sign.search(line))

				#print("end_of_table: "+str(end_of_table))
				#print("in_table: " +str(in_table)+'\n')


				if(in_table and in_columns and in_row==False and line.count(' ')<=1):
					columns_1.append(line.strip())
				elif(in_table and in_columns and in_row == True and line.count('\t')>=1):
					# player_name,format_id,stats_offensive_list[m],line.strip().split('\t')
					
					one_row = [school_name,format_id,stats_offensive_list[m]]
					the_rest_columns = line.strip().split('\t')
					one_row.extend(the_rest_columns)
					row_1.append(one_row)	

				elif(in_table and end_of_table):
					break
				elif(line.strip() == stats_offensive_list[m].strip()):
					in_table = True
					columns_1.append(line.rstrip())

		# print(row_1)
		# print(len(row_1))
		directory = 'C:/Users/lchen/Desktop/Chenjie_New_Team_Tables/'
		if not os.path.exists(directory):
			os.makedirs(directory)
		with open('C:/Users/lchen/Desktop/Chenjie_New_Team_Tables/combined_team_tables.csv','a', newline = '') as ft:
			a = csv.writer(ft,delimiter = ',')
			# a.writerow(columns_1)  ---- we don't need columns' names here
			a.writerows(row_1)
	

	for n in range(len(stats_defensive_list)):

		in_table = False
		in_row = False
		in_columns = False
		end_of_table = False

		in_columns_sign = re.compile(r'([^\t])')
		in_rows_sign = re.compile(r'([\t])')
		end_of_table_sign = re.compile(r'^\s*$')

		row_2 =[]
		columns_2 = []
		format_id = 2

		for line in file_needed_2:
			if(in_table and end_of_table):
				break
			else:
				in_columns = bool(in_columns_sign.search(line))
			
				#print("in_columns: "+str(in_columns))

				in_row = bool(in_rows_sign.search(line))
			
				#print("in_row: "+str(in_row))

				end_of_table = bool(end_of_table_sign.search(line))

				#print("end_of_table: "+str(end_of_table))
				#print("in_table: " +str(in_table)+'\n')


				if(in_table and in_columns and in_row==False and line.count(' ')<=1):
					columns_2.append(line.strip())
				elif(in_table and in_columns and in_row == True and line.count('\t')>=1):
					# player_name, format_id, category_name, element_name

					one_row = [school_name,format_id,stats_defensive_list[n]]
					the_rest_columns = line.strip().split('\t')
					one_row.extend(the_rest_columns)
					row_2.append(one_row)

				elif(in_table and end_of_table):
					break
				elif(line.strip() == stats_defensive_list[n].strip()):
					in_table = True
					columns_2.append(line.rstrip())

		
			directory = 'C:/Users/lchen/Desktop/Chenjie_New_Team_Tables/'
		if not os.path.exists(directory):
			os.makedirs(directory)
		with open('C:/Users/lchen/Desktop/Chenjie_New_Team_Tables/combined_team_tables.csv','a', newline = '') as ft:
			a = csv.writer(ft,delimiter = ',')
			# a.writerow(columns_1)  ---- we don't need columns' names here
			a.writerows(row_2)