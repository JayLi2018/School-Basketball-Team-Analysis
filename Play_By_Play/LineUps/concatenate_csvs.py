import os

# fout=open("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Line_Ups/combined_line_ups.csv","a")
# # first file:
# for line in open("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Line_Ups/player_lineups_1.csv"):
#     fout.write(line)
# # now the rest:    
# for num in range(2,20):
# 	if not os.path.exists("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Line_Ups/player_lineups_"+str(num)+'.csv'):
# 		continue
# 	else:	
# 	    f = open("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Line_Ups/player_lineups_"+str(num)+'.csv')
# 	    f.__next__() # skip the header
# 	    for line in f:
# 	         fout.write(line)
# 	    f.close() # not really needed
# fout.close()

fout1=open("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Line_Ups_Info/combined_line_ups_info.csv","a")
# first file:
for line in open("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Line_Ups_Info/player_lineups_info_1.csv"):
    fout1.write(line)
# now the rest:    
for num in range(2,20):
	if not os.path.exists("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Line_Ups_Info/player_lineups_info_"+str(num)+'.csv'):
		continue
	else:	
	    f1= open("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Line_Ups_Info/player_lineups_info_"+str(num)+'.csv')
	    f1.__next__() # skip the header
	    for line in f1:
	         fout1.write(line)
	    f1.close() # not really needed
fout1.close()

