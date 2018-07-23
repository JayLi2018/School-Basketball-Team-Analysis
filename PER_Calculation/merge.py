import pandas as pd 

team_pace_factors = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/PER_calculations/pace_factors.csv')
filtered_player_raw_data = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/PER_calculations/filtered_player_raw_data.csv')

# player_over_5_games = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/PER_calculations/players_over_5_games.csv')
# Player_Raw_Data = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/PER_calculations/Player_Raw_Data.csv')

# merged_1 = pd.merge(player_over_5_games,Player_Raw_Data,on = 'player_name')
# merged_1.to_csv('filtered_player_raw_data.csv')

merged_2 = pd.merge(filtered_player_raw_data,team_pace_factors,on = 'team_name')
merged_2.to_csv('final_raw_data.csv')
