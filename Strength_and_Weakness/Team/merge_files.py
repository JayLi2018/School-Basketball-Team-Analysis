import pandas as pd 

adjustments = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/Strength_and_Weakness/Team/2.0/adjustments.csv')

offense = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/Strength_and_Weakness/Team/2.0/Team_Offensive.csv')

defense = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/Strength_and_Weakness/Team/2.0/Team_Defensive.csv')

offense_adjust = pd.merge(adjustments,offense,on = 'team_name')

offense_adjust.to_csv('Offense_Adjusted.csv')

offense_adjust = pd.merge(adjustments,defense,on = 'team_name')

offense_adjust.to_csv('Defense_Adjusted.csv')

adjusted_teams = pd.read_csv('Adjusted_Teams_Weakness_Strength.csv')
score_difference = pd.read_csv('game_score_difference.csv')

final_version = pd.merge(adjusted_teams,score_difference,on = 'team_name')

final_version.to_csv('final_adjusted_team_weak_stren.csv')