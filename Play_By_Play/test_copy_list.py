import re
from BBall_Classes import Player, Lineup

# in_possesion_first_half = re.compile(r'\b[A-Z]+\b\t\b1\b')
# in_possesion_second_half = re.compile(r'\b[A-Z]+\b\t\b2\b')
# in_possesion_ot = re.compile(r'\b[A-Z]+\b\t\b3\b')
timer = re.compile(r'([0-9][0-9])\:([0-5][0-9])')

file_needed  = open('C:/Users/lchen/Desktop/Play-By-Play/test_if_right.txt',"r")

lines = []

for line in file_needed:
	lines.append(line)

starting_time = 20
current_time = starting_time
time_interval = 0
unusual_interval = 0
unusual_time = 0
# for line in lines:
# 	print("first half "+str(bool(in_possesion_first_half.search(line))))
# 	print("second half" +str(bool(in_possesion_second_half.search(line))))
# 	print("over time "+str(bool(in_possesion_ot.search(line))))


current_lineup  = Lineup()

for line in lines:
	if(bool(timer.search(line))==False):
		continue
	else:
		if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
			time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
			if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
				current_lineup.Min = current_lineup.Min + time_interval
				unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
			print('unusual interval:'+str(time_interval))

		elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
			time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
			current_lineup.Min = current_lineup.Min + time_interval
			current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

		elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
			continue
print(current_lineup.Min)





		
