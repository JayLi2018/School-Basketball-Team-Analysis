import pandas as pd 


offense_with_adjust_factor = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/Strength_and_Weakness/Team/2.0/Offense_Adjusted.csv')
deffense_with_adjust_factor = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/Strength_and_Weakness/Team/2.0/Defense_Adjusted.csv')

offensive = pd.DataFrame(offense_with_adjust_factor)
defensive = pd.DataFrame(deffense_with_adjust_factor)


offensive['Adjusted_Overall_Average_PPP'] = offensive['average_ppp']*offensive['off_adjustment_factor']

offensive['Adjusted_Type_PPP'] = offensive['type_ppp']*offensive['off_adjustment_factor']

offensive.to_csv('Offensive_Adjusted_Teams.csv')


defensive['Adjusted_Overall_Average_PPP'] = defensive['average_ppp']*defensive['def_adjustment_factor']

defensive['Adjusted_Type_PPP'] = defensive['type_ppp']*defensive['def_adjustment_factor']

defensive.to_csv('Defensive_Adjusted_Teams.csv')