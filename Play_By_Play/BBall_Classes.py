class Player():
    """" A player's performance in a game"""


    
    def __init__(self,Name,all_players = None):
        """Initialize attributes to describe a player"""
        self.Name = Name
        
        self.all_players = {'Anthony Mosley':0,            #used to document to whom this player pass to
           'Jake Digiorgio':0,
           'Parker Joncus':0,
           'Max Hisatake':0,
           'Malik Howze':0,
           'Quentin Forberg':0,
           'Jake Bruns':0,
           'Jason Morris':0,
           'Calvin Schmitz':0,
           'Capriest Gardner':0, 
           'Brett Ott':0,
           'Brinden Carlson':0,
           'Kohl Linder':0}
        
        self.Pts = 0
        self.FGA = 0  # field_goal_attempts
        self.FGM = 0  # field_goal_made
        self.FGm = 0  # field_goal_miss
        self.Two_FGA = 0  # field_goal_attempts
        self.Two_FGM = 0  # field_goal_made
        self.Two_FGm = 0  # field_goal_miss
        self.Three_FGA = 0  # 3_field_goal_attempts
        self.Three_FGM = 0
        self.Three_FGm = 0
        self.DefReb = 0  # defensive reb
        self.OffReb = 0  # offensive reb
        self.TtlReb = 0  # total reb
        self.FTA = 0
        self.FTm = 0
        self.FTM = 0
        self.Ast = 0
        self.Stl = 0

                   
    def pass_to(self,teammate):
        # print(self.Name +'\'s Passing history:\n')
        for key in self.all_players: 
            if(teammate == key):
                self.all_players[key] = self.all_players[key] +1 
        # for k,v in self.all_players.items():
        #     print( str(k) +' : '+str(v))
        # print('\n')

class Lineup():

    def __init__(self):
        self.Min = 0
        self.Lineup_Score = 0
        self.Oppo_Score = 0
        self.Oppo_FGA = 0  # field_goal_attempts
        self.Oppo_FGM = 0  # field_goal_made
        self.Oppo_FGm = 0  # field_goal_miss
        self.Oppo_Two_FGA = 0  # field_goal_attempts
        self.Oppo_Two_FGM = 0  # field_goal_made
        self.Oppo_Two_FGm = 0  # field_goal_miss
        self.Oppo_Three_FGA = 0  # 3_field_goal_attempts
        self.Oppo_Three_FGM = 0
        self.Oppo_Three_FGm = 0
        self.Oppo_DefReb = 0  # defensive reb
        self.Oppo_OffReb = 0  # offensive reb
        self.Oppo_TtlReb = 0  # total reb
        self.Oppo_FTA = 0
        self.Oppo_FTm = 0
        self.Oppo_FTM = 0
        self.Oppo_Ast = 0
        self.Oppo_Stl = 0