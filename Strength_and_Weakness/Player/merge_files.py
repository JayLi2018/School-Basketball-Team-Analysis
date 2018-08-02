import pandas as pd 

adjustments = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/Strength_and_Weakness/Player/2.0/adjustments.csv')

offense = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/Strength_and_Weakness/Player/2.0/Offense.csv')

defense = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/Strength_and_Weakness/Player/2.0/Defense.csv')

# offense_adjust = pd.merge(adjustments,offense,on = 'team_name')

# offense_adjust.to_csv('Offense_Adjusted.csv')

offense_adjust = pd.merge(adjustments,defense,on = 'team_name')

offense_adjust.to_csv('Defense_Adjusted.csv')