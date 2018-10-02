import pandas as pd 

player_average = pd.read_csv('C:/Users/lchen/Desktop/School-Basketball-Team-Analysis/new_player_averages.csv')

category = pd.read_csv('C:/Users/lchen/Desktop/School-Basketball-Team-Analysis/Database_Files/Category_Table.csv')

element = pd.read_csv('C:/Users/lchen/Desktop/School-Basketball-Team-Analysis/Database_Files/Element_Table.csv')

new_players = pd.read_csv('C:/Users/lchen/Desktop/School-Basketball-Team-Analysis/Database_Files/Python_Geneate_CSVs/Player_Average/new_school_raw_data/new_player_table.csv')

# merge_pa_with_c = pd.merge(player_average,category, on = 'Category_Name')

# merge_pa_with_c.to_csv('Player_AVE_with_Category.csv')

# Player_AVE_with_Category = pd.read_csv('C:/Users/lchen/Desktop/School-Basketball-Team-Analysis/Database_Files/Player_AVE_with_Category.csv')

# Player_AVE_with_CE = pd.merge(Player_AVE_with_Category,element, on = 'Element_Name')

# Player_AVE_with_CE.to_csv('Player_AVE_with_CE.csv')

Player_AVE_with_CE = pd.read_csv('C:/Users/lchen/Desktop/School-Basketball-Team-Analysis/Database_Files/Player_AVE_with_CE.csv')

Final_format = pd.merge(Player_AVE_with_CE,new_players,on = 'Player_Name')

Final_format.to_csv('new_player_averages_final.csv')