import pandas as pd 

# line_ups = pd.read_csv("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Line_Ups_Info/combined_line_ups_info.csv")
# line_ups_info = pd.read_csv("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Line_Ups/combined_line_ups.csv")
combined = pd.read_csv("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/info_lineup_combined.csv")
player_id= pd.read_csv("C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/player_id.csv")

# combined  = pd.merge(line_ups,line_ups_info,on = ['Game_ID','Session_ID','LineUp_ID','Game_Status_ID'])

# print(combined.head())

# combined.to_csv('info_lineup_combined.csv')

combine_player_id = pd.merge(combined,player_id, on = 'Player_Name')
combine_player_id.to_csv("final_version.csv")