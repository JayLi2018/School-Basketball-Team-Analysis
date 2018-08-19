import re
import os


timer = re.compile(r'([0-9][0-9])\:([0-5][0-9])')

def get_time(line):
	match = timer.search(line)
	if match:
		return float(match.group(1))+float(match.group(2))/60

for n in range(19,20):
	print('we are doing '+ str(n)+' th file!')
	file_needed_1 = open('C:/Users/lchen/Desktop/Games_Play_By_Play/'+str(n)+'-'+'1.txt',"r")
	file_needed_2 = open('C:/Users/lchen/Desktop/Games_Play_By_Play/'+str(n)+'-'+'2.txt',"r")
	the_file = open('C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Raw_Data/'+str(n)+'.txt',"a")

	lines_1 = []

	for line in file_needed_1:
		if(bool(timer.search(line)) == True):
			lines_1.append(line)

	for line in lines_1:
		get_time(line)

	lines_1.sort(key = get_time,reverse =True)


	for line in lines_1:
		the_file.write("%s" %line)

	the_file = open('C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Raw_Data/'+str(n)+'.txt',"a")
	lines_2 = []

	for line in file_needed_2:
		if(bool(timer.search(line)) == True):
			lines_2.append(line)

	for line in lines_2:
		get_time(line)

	lines_2.sort(key = get_time,reverse =True)


	for line in lines_2:
		the_file.write("%s" %line)

	directory ='C:/Users/lchen/Desktop/Games_Play_By_Play/'+str(n)+'-'+'3.txt' #check if there was a overtime
	if os.path.exists(directory):
		file_needed_3 = open('C:/Users/lchen/Desktop/Games_Play_By_Play/'+str(n)+'-'+'3.txt','r')
		the_file = open('C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Raw_Data/'+str(n)+'.txt',"a")
		lines_3 = []

		for line in file_needed_3:
			if(bool(timer.search(line)) == True):
				lines_3.append(line)

		for line in lines_3:
			get_time(line)

		lines_3.sort(key = get_time,reverse =True)


		for line in lines_3:
			the_file.write("%s" %line)







