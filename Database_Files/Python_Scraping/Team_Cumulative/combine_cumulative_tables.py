# automatically convert txt to csv
import re
import csv
import os
import pandas as pd 


def append_cumulative_table(school_name,school_id):
 
	file_needed_1  = open("C:/Users/lchen/Desktop/Basketball_Project_Archives/Cumulative_Raw_Data/"+school_id+".txt",'r')

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
				
				one_row = [school_id]
				the_rest_columns = line.strip().split('\t')
				one_row.extend(the_rest_columns)
				row_1.append(one_row)	

			elif(in_table and end_of_table):
				break
			elif(line.strip() == school_name.strip()):
				in_table = True
				columns_1.append(line.rstrip())

	# print(row_1)
	# print(len(row_1))
	directory = 'C:/Users/lchen/Desktop/'
	if not os.path.exists(directory):
		os.makedirs(directory)
	with open('C:/Users/lchen/Desktop/combined_team_tables.csv','a', newline = '') as ft:
		a = csv.writer(ft,delimiter = ',')
		# a.writerow(columns_1)  ---- we don't need columns' names here
		a.writerows(row_1)

	file_needed_1  = open("C:/Users/lchen/Desktop/Basketball_Project_Archives/Cumulative_Raw_Data/"+school_id+".txt",'r')

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
				
				one_row = [school_id]
				the_rest_columns = line.strip().split('\t')
				one_row.extend(the_rest_columns)
				row_1.append(one_row)	

			elif(in_table and end_of_table):
				break
			elif(line.strip() == school_name+'_1'):
				in_table = True
				columns_1.append(line.rstrip())

	# print(row_1)
	# print(len(row_1))
	directory = 'C:/Users/lchen/Desktop/'
	if not os.path.exists(directory):
		os.makedirs(directory)
	with open('C:/Users/lchen/Desktop/combined_team_tables.csv','a', newline = '') as ft:
		a = csv.writer(ft,delimiter = ',')
		# a.writerow(columns_1)  ---- we don't need columns' names here
		a.writerows(row_1)
