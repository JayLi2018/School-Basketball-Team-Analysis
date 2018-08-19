import re
import os
import csv
from BBall_Classes import Player,Lineup
import copy   # use "deep copy" here 

# def get_squads_stats():
def get_squads_stats(game_id):
    file_needed  = open('C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/Raw_Data/'+game_id+'.txt',"r")

    lines = []

    for line in file_needed:
        lines.append(line)

    in_possesion_first_half = re.compile(r'\b[A-Za-z]+\b\t\b1\b')
    in_possesion_second_half = re.compile(r'\b[A-Za-z]+\b\t\b2\b')
    in_possesion_ot = re.compile(r'\b[A-Za-z]+\b\t\b3\b')

    timer = re.compile(r'([0-9][0-9])\:([0-5][0-9])') # find timer
    off_reb = re.compile(r'Misc Stat > Offensive Rebound > (.*)') # off_reb.search(line).group(1)
    def_reb = re.compile(r'Misc Stat > Defensive Rebound > (.*)') # def_reb.search(line).group(1)
    shot_attempt = re.compile(r'Shot > (.*) > Any Type > ')
    two_made = re.compile(r'2 Point Attempt > Make 2 Pts')
    two_missed = re.compile(r'2 Point Attempt > Miss 2 Pts')
    three_made = re.compile(r' 3 Point Attempt > Make 3 Pts')
    three_miss = re.compile(r' 3 Point Attempt > Miss 3 Pts')
    freethrow_attempt = re.compile(r'Shot > (.*) > Free Throw >')
    freethrow_made = re.compile(r'Free Throw > Made')
    freethrow_miss= re.compile(r'Free Throw > Missed')
    assist = re.compile(r'Misc Stat > Assist > (.*)')
    steal = re.compile(r'Misc Stat > Steal > (.*)')
    player_movement_out = re.compile(r'Player Movement > Sub Out >.*> (.*)') #player_movement.search(line).group(1)
    player_movement_in = re.compile(r'Player Movement > Sub In > .*> (.*)')

    all_players = ['Anthony Mosley','Jake Digiorgio','Parker Joncus','Max Hisatake','Malik Howze','Quentin Forberg',
    'Jake Bruns','Jason Morris','Calvin Schmitz','Capriest Gardner','Brett Ott','Brinden Carlson','Kohl Linder']


    player_1 = Player('Anthony Mosley')
    player_2 = Player('Jake Digiorgio')
    player_3 = Player('Parker Joncus')
    player_4 = Player('Max Hisatake')
    player_5 = Player('Malik Howze')
    player_6 = Player('Quentin Forberg')
    player_7 = Player('Jake Bruns')
    player_8 = Player('Jason Morris')
    player_9 = Player('Calvin Schmitz')
    player_10 = Player('Capriest Gardner')
    player_11 = Player('Brett Ott')
    player_12 = Player('Brinden Carlson')
    player_13 = Player('Kohl Linder')

    player_objects = [player_1,player_2,player_3,player_4,player_5,player_6,player_7,player_8,player_9,player_10,player_11,player_12,player_13]

    
    # List of line-ups
    total_lineups = []

    first_half_lineups = []
    second_half_lineups = []
    overtime_lineups = []
    
    first_half_lineups_names = []
    second_half_lineups_names = []
    overtime_lineups_names = []

    
    half_time = 20
    starting_time = 20
    current_time =starting_time
    time_interval = 0
    unusual_interval = 0
    unusual_time = 0
    over_time = 5

     #starting lineups of each game:
     # 1: 1,2,3,4,5
     # 2: 2,4,5,7,9       messed up
     # 3: 2,3,4,7,9
     # 4: 2,3,4,7,9
     # 5: 1,2,3,4,10
     # 6: 1,2,3,4,11
     # 7: 1,2,3,4,5
     # 8: 1,2,3,4,5       messed up
     # 9: 1,2,3,4,5
     #10: 1,2,3,4,5
     #11: 1,2,3,4,5
     #12: 2,3,4,5,7
     #13: 2,3,4,6,7
     #14: 2,3,4,5,7
     #15: 1,2,3,4,5
     #16: 1,2,3,4,5       messed up
     #17: 1,2,3,4,5
     #18: 1,2,3,4,5
     #19: 1,2,3,4,5       messed up



    first_half_starting_lineup= [player_2,player_4,player_1,player_5,player_3] # this is the first line-up
    first_half_starting_lineup_names = ['Anthony Mosley','Jake Digiorgio','Parker Joncus','Max Hisatake','Malik Howze']
    first_half_lineups_names.append(first_half_starting_lineup_names)

    first_half_lineups.append(first_half_starting_lineup)
    
    second_half_starting_lineup= copy.deepcopy(first_half_starting_lineup)
    second_half_starting_lineup_names = ['Anthony Mosley','Jake Digiorgio','Parker Joncus','Max Hisatake','Malik Howze']
    second_half_lineups_names.append(second_half_starting_lineup_names)

    second_half_lineups.append(second_half_starting_lineup)


    overtime_starting_lineup= copy.deepcopy(first_half_starting_lineup) # this is the first line-up
    overtime_starting_lineup_names = ['Parker','Jake Digiorgio','Malik Howze','Max Hisatake','Anthony Mosley','Malik Howze']
    overtime_lineups_names.append(overtime_starting_lineup_names)

    overtime_lineups.append(overtime_starting_lineup)



    first_half_lineup_info = []
    second_half_lineup_info = []
    overtime_lineup_info = []
    
    final_first_half_lineup_info = []
    final_second_half_lineup_info = []
    final_overtime_lineup_info =[]

    first_half_lineup_info_1 = Lineup()
    second_half_lineup_info_1 = Lineup()
    overtime_lineup_info_1 = Lineup()
    

    first_half_lineup_info.append(first_half_lineup_info_1)
    second_half_lineup_info.append(second_half_lineup_info_1)
    overtime_lineup_info.append(overtime_lineup_info_1)
     
    current_lineup = first_half_starting_lineup
    current_lineup_info = first_half_lineup_info_1

    in_first_half = False
    in_second_half = False 
    in_ot = False
    in_one_possesion = False

    iit_poss = False
    made_shot_last_line = False    # check if there was an assist
    player_who_scored = None       # store the player who scored last possesion( besides free throws)
    first_half_time_left = None
    second_half_time_left = None
    overtime_left = None

    player_stats_match = False
    
    iit_sub_in = False
    iit_sub_out = False
    iit_sub_in_buffer = []  # handle situations where there are 2 consistant "sub in" or "sub out"
    iit_sub_out_buffer = []
    for line in lines:
        
        if(in_first_half ==True and (bool(player_movement_in.search(line))==True or bool(player_movement_out.search(line))==True)):

            if(bool(player_movement_in.search(line))==True):
                player = player_movement_in.search(line).group(1)

                if(player.strip() in all_players):
                    iit_sub_in = True
                    for n in player_objects:
                        if(n.Name == player):
                            player_in = Player(n.Name)
                            iit_sub_in_buffer.append(player_in)
                            
            if(bool(player_movement_out.search(line))==True):
                player =player_movement_out.search(line).group(1)

                if(player.strip() in all_players):
                    iit_sub_out = True
                    for n in player_objects:
                        if(n.Name == player):
                            player_out = Player(n.Name)
                            iit_sub_out_buffer.append(player_out)


            if(iit_sub_in == True and iit_sub_out == True):
                
                print("Substitution Timing: " + str(float(timer.search(line).group(1))+float(timer.search(line).group(2))/60))
                new_line_up = []
                new_line_up.append(iit_sub_in_buffer[-1])
                new_line_up_names = []
                new_line_up_names.append(iit_sub_in_buffer[-1].Name)
                print('Movement! '+ str(iit_sub_in_buffer[-1].Name)+' is in!' )
                iit_sub_in_buffer.pop(-1)
                

                
                # print('Current_lineup is:'+current_lineup[0].Name+' '+current_lineup[1].Name+' '+ current_lineup[2].Name+' '+ current_lineup[3].Name+' '+current_lineup[4].Name)
                last_player_in_buffer = iit_sub_out_buffer[-1]
                print(iit_sub_out_buffer[-1].Name+' is Out!')
                deep_copy_of_current_lineup = copy.deepcopy(current_lineup)
                print('Before movement the line-up is : '+current_lineup[0].Name+', '+current_lineup[1].Name+', '+current_lineup[2].Name+', '+current_lineup[3].Name+', '+current_lineup[4].Name+' ')
                for n in deep_copy_of_current_lineup:
                    if(n.Name == last_player_in_buffer.Name):
                        continue
                    else:
                        new_player = Player(n.Name)
                        new_line_up.append(new_player)
                        new_line_up_names.append(n.Name)
                print('new line up has '+str(len(new_line_up))+' Players!')
                iit_sub_out_buffer.pop(-1)

                print("New Lineup: ")
                for n in new_line_up:
                    print(n.Name)
                
                lineup_exists = False
                
                m = -1
                for n in first_half_lineups_names:
                    check = bool(set(n)==set(new_line_up_names))
                    m=m+1
                    if(check == True):
                        break
                    else:
                        continue
                if (check == True):
                    print("line-up EXISTS!")
                    current_lineup = first_half_lineups[m]
                    print("we are merging with the " + str(m) + "th Line up!" )
                    current_lineup_info = first_half_lineup_info[m]
                    lineup_exists = True

                elif(lineup_exists == False and len(iit_sub_out_buffer)==0 and len(iit_sub_in_buffer)==0):
                    print("Line-up doesnt Exist!")
                    current_lineup = new_line_up 
                    first_half_lineups.append(new_line_up)
                    first_half_lineups_names.append(new_line_up_names)
                    print('after appending new line - up names, we have '+str(len(first_half_lineups_names))+' different line-ups names !!!!!!!!!')
                    print(first_half_lineups_names)
                    new_line_up_info = Lineup()
                    current_lineup_info = new_line_up_info
                    first_half_lineup_info.append(new_line_up_info)
                else:
                    print('Shoot, it was just an tempo line up!')
                    if(len(first_half_lineup_info)==1):
                        current_lineup_info = first_half_lineup_info_1
                    else:
                        current_lineup = copy.deepcopy(new_line_up)
                        current_lineup_info = copy.deepcopy(new_line_up_info)
                
                print('sub in buffer has '+str(len(iit_sub_in_buffer))+' players')
                print('sub out buffer has '+str(len(iit_sub_out_buffer))+' players')
                print("\n\n\n")
                if(len(iit_sub_in_buffer)==0):
                    iit_sub_in = False
                if(len(iit_sub_out_buffer)==0):
                    iit_sub_out = False

        if(in_second_half ==True and (bool(player_movement_in.search(line))==True or bool(player_movement_out.search(line))==True)):

            if(bool(player_movement_in.search(line))==True):
                player =player_movement_in.search(line).group(1)

                if(player.strip() in all_players):
                    iit_sub_in = True
                    for n in player_objects:
                        if(n.Name == player):
                            player_in = Player(n.Name)
                            iit_sub_in_buffer.append(player_in)
                            
            if(bool(player_movement_out.search(line))==True):
                player =player_movement_out.search(line).group(1)

                if(player.strip() in all_players):
                    iit_sub_out = True
                    for n in player_objects:
                        if(n.Name == player):
                            player_out = Player(n.Name)
                            iit_sub_out_buffer.append(player_out)


            if(iit_sub_in == True and iit_sub_out == True):
                print("Substitution Timing: " + str(float(timer.search(line).group(1))+float(timer.search(line).group(2))/60))
                new_line_up = []
                new_line_up.append(iit_sub_in_buffer[-1])
                new_line_up_names = []
                new_line_up_names.append(iit_sub_in_buffer[-1].Name)
                print('Movement! '+ str(iit_sub_in_buffer[-1].Name)+' is in!' )
                iit_sub_in_buffer.pop(-1)
                

                
                # print('Current_lineup is:'+current_lineup[0].Name+' '+current_lineup[1].Name+' '+ current_lineup[2].Name+' '+ current_lineup[3].Name+' '+current_lineup[4].Name)
                last_player_in_buffer = iit_sub_out_buffer[-1]
                print(iit_sub_out_buffer[-1].Name+' is Out!')
                deep_copy_of_current_lineup = copy.deepcopy(current_lineup)
                print('Before movement the line-up is : '+current_lineup[0].Name+', '+current_lineup[1].Name+', '+current_lineup[2].Name+', '+current_lineup[3].Name+', '+current_lineup[4].Name+' ')
                for n in deep_copy_of_current_lineup:
                    if(n.Name == last_player_in_buffer.Name):
                        continue
                    else:
                        new_player = Player(n.Name)
                        new_line_up.append(new_player)
                        new_line_up_names.append(n.Name)
                print('new line up has '+str(len(new_line_up))+' Players!')
                iit_sub_out_buffer.pop(-1)

                print("New Lineup: ")
                for n in new_line_up:
                    print(n.Name)
                
                    
                lineup_exists = False
                
                m = -1
                for n in second_half_lineups_names:
                    check = bool(set(n)==set(new_line_up_names))
                    m=m+1
                    if(check == True):
                        break
                    else:
                        continue

                if (check == True):
                    print("line-up EXISTS!")
                    current_lineup = second_half_lineups[m]
                    current_lineup_info = second_half_lineup_info[m]
                    lineup_exists = True

                elif(lineup_exists == False and len(iit_sub_out_buffer)==0 and len(iit_sub_in_buffer)==0):
                    print("Line-up doesnt Exist!")
                    current_lineup = copy.copy(new_line_up) 
                    second_half_lineups.append(new_line_up)
                    second_half_lineups_names.append(new_line_up_names)
                    new_line_up_info = Lineup()
                    current_lineup_info = new_line_up_info
                    second_half_lineup_info.append(new_line_up_info)
                else:
                    print('Shoot, it was just an tempo line up!')
                    
                    if(len(first_half_lineup_info)==1):
                        current_lineup_info = first_half_lineup_info_1
                    else:
                        current_lineup = copy.deepcopy(new_line_up)
                        current_lineup_info = copy.deepcopy(new_line_up_info)

                if(len(iit_sub_in_buffer)==0):
                    iit_sub_in = False
                if(len(iit_sub_out_buffer)==0):
                    iit_sub_out = False



        if(in_ot ==True and (bool(player_movement_in.search(line))==True or bool(player_movement_out.search(line))==True)):
            print("Substitution Timing: " + str(float(timer.search(line).group(1))+float(timer.search(line).group(2))/60))
            if(bool(player_movement_in.search(line))==True):
                player =player_movement_in.search(line).group(1)

                if(player.strip() in all_players):
                    iit_sub_in = True
                    for n in player_objects:
                        if(n.Name == player):
                            player_in = Player(n.Name)
                            iit_sub_in_buffer.append(player_in)
                            
            if(bool(player_movement_out.search(line))==True):
                player =player_movement_out.search(line).group(1)

                if(player.strip() in all_players):
                    iit_sub_out = True
                    for n in player_objects:
                        if(n.Name == player):
                            player_out = Player(n.Name)
                            iit_sub_out_buffer.append(player_out)


            if(iit_sub_in == True and iit_sub_out == True):
                
                new_line_up = []
                new_line_up.append(iit_sub_in_buffer[-1])
                new_line_up_names = []
                new_line_up_names.append(iit_sub_in_buffer[-1].Name)
                print('Movement! '+ str(iit_sub_in_buffer[-1].Name)+' is in!' )
                iit_sub_in_buffer.pop(-1)
                

                
                # print('Current_lineup is:'+current_lineup[0].Name+' '+current_lineup[1].Name+' '+ current_lineup[2].Name+' '+ current_lineup[3].Name+' '+current_lineup[4].Name)
                last_player_in_buffer = iit_sub_out_buffer[-1]
                print(iit_sub_out_buffer[-1].Name+' is Out!')
                deep_copy_of_current_lineup = copy.deepcopy(current_lineup)
                print('Before movement the line-up is : '+current_lineup[0].Name+', '+current_lineup[1].Name+', '+current_lineup[2].Name+', '+current_lineup[3].Name+', '+current_lineup[4].Name+' ')
                for n in deep_copy_of_current_lineup:
                    if(n.Name == last_player_in_buffer.Name):
                        continue
                    else:
                        new_player = Player(n.Name)
                        new_line_up.append(new_player)
                        new_line_up_names.append(n.Name)
                print('new line up has '+str(len(new_line_up))+' Players!')
                iit_sub_out_buffer.pop(-1)

                print("New Lineup: ")
                for n in new_line_up:
                    print(n.Name)
                print("\n\n\n")
                    
                lineup_exists = False
                
                m = -1
                for n in overtime_lineups_names:
                    check = bool(set(n)==set(new_line_up_names))
                    m=m+1
                    if(check == True):
                        break
                    else:
                        continue

                if (check == True):
                    print("line-up EXISTS!")
                    current_lineup = overtime_lineups[m]
                    current_lineup_info = overtime_lineup_info[m]
                    lineup_exists = True

                elif(lineup_exists == False and len(iit_sub_out_buffer)==0 and len(iit_sub_in_buffer)==0):
                    print("Line-up doesnt Exist!")
                    current_lineup = copy.copy(new_line_up) 
                    overtime_lineups.append(new_line_up)
                    overtime_lineups_names.append(new_line_up_names)
                    new_line_up_info = Lineup()
                    current_lineup_info = new_line_up_info
                    overtime_lineup_info.append(new_line_up_info)

                else:
                    print('Shoot, it was just an tempo line up!')

                    if(len(first_half_lineup_info)==1):
                        current_lineup_info = first_half_lineup_info_1
                    else:
                        current_lineup = copy.deepcopy(new_line_up)
                        current_lineup_info = copy.deepcopy(new_line_up_info)


                if(len(iit_sub_in_buffer)==0):
                    iit_sub_in = False
                if(len(iit_sub_out_buffer)==0):
                    iit_sub_out = False


        if(bool(in_possesion_first_half.search(line))==True and bool(timer.search(line))==True):  # IIT possesion
            in_one_possesion= True
            in_first_half = True
            in_second_half = False 
            in_ot = False
            first_half_time_left = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60
            if(len(first_half_lineups) == 1):
                current_lineup = first_half_starting_lineup
                current_lineup_info = first_half_lineup_info_1
            if(current_lineup == first_half_starting_lineup and len(first_half_lineups)== 1):
                first_half_lineup_info_1.Min =half_time - first_half_time_left
                current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

        

        elif(bool(in_possesion_second_half.search(line))==True and bool(timer.search(line))==True):
            in_one_possesion= True
            in_first_half = False
            in_second_half = True
            in_ot = False
            second_half_time_left = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60
            if(len(second_half_lineups)==1):
                current_lineup = second_half_starting_lineup
                current_lineup_info = second_half_lineup_info_1
            if(current_lineup == second_half_starting_lineup and len(second_half_lineups)== 1):
                second_half_lineup_info_1.Min = half_time - second_half_time_left
                current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60
                
            
        elif(bool(in_possesion_ot.search(line))==True and bool(timer.search(line))==True):
            in_one_possesion= True
            in_first_half = False
            in_second_half = False
            in_ot = True
            overtime_time_left = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60
            if(len(overtime_lineups)==1):
                current_lineup = overtime_starting_lineup
                current_lineup_info = overtime_lineup_info_1
            if(current_lineup == overtime_starting_lineup and len(overtime_lineups)== 1):
                overtime_lineup_info_1.Min = over_time - overtime_time_left
                current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60
                

        if(in_one_possesion==True and bool(off_reb.search(line))==True):      # Offensive Reb
            # print('found a reb!')
            name_off_reb = off_reb.search(line).group(1)
            player_stats_match =False
            for p in current_lineup:
                if(p.Name == name_off_reb.strip()):
                    player_stats_match = True
                    p.OffReb = p.OffReb+1
                    p.TtlReb = p.TtlReb+1
                    break
            if(player_stats_match ==False):
                # print('Found an Opponent stat!!!!')
                current_lineup_info.Oppo_OffReb = current_lineup_info.Oppo_OffReb+1
                current_lineup_info.Oppo_TtlReb = current_lineup_info.Oppo_TtlReb+1

            if(bool(timer.search(line))==False):
                continue
            else:
                if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
                    time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
                    if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
                        current_lineup_info.Min = current_lineup_info.Min + time_interval
                        unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
                    print('unusual interval:'+str(time_interval))

                elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
                    time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
                    current_lineup_info.Min = current_lineup_info.Min + time_interval
                    current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

                elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
                    continue


        if(in_one_possesion==True and bool(def_reb.search(line))==True):   # Defensive Reb
            name_def_reb = def_reb.search(line).group(1) 
            player_stats_match =False
            for p in current_lineup:
                if(p.Name == name_def_reb.strip()):
                    player_stats_match = True
                    p.DefReb = p.DefReb+1
                    p.TtlReb = p.TtlReb+1
                    break
            if(player_stats_match == False):
                # print('Found an Opponent stat!!!!')
                current_lineup_info.Oppo_DefReb=current_lineup_info.Oppo_DefReb+1
                current_lineup_info.Oppo_TtlReb=current_lineup_info.Oppo_TtlReb+1
            
            if(bool(timer.search(line))==False):
                continue
            else:
                if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
                    time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
                    if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
                        current_lineup_info.Min = current_lineup_info.Min + time_interval
                        unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
                    print('unusual interval:'+str(time_interval))

                elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
                    time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
                    current_lineup_info.Min = current_lineup_info.Min + time_interval
                    current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

                elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
                    continue

        if(in_one_possesion==True and bool(shot_attempt.search(line))==True):  # Shot Attempts
            FGA = shot_attempt.search(line).group(1)
            player_stats_match =False
            if(bool(two_made.search(line))==True):
                for p in current_lineup:
                    if(p.Name == FGA.strip()):
                        player_stats_match = True
                        p.FGA= p.FGA+1
                        p.FGM = p.FGM+1
                        p.Two_FGA = p.Two_FGA +1
                        p.Two_FGM = p.Two_FGM +1
                        p.Pts = p.Pts +2
                        made_shot_last_line = True
                        player_who_scored = p.Name
                        current_lineup_info.Lineup_Score = current_lineup_info.Lineup_Score + 2
                        break 

                if(player_stats_match == False):
                    # print('Found an Opponent stat!!!!')
                    current_lineup_info.Oppo_FGA=current_lineup_info.Oppo_FGA+1
                    current_lineup_info.Oppo_FGM=current_lineup_info.Oppo_FGM+1
                    current_lineup_info.Oppo_Two_FGA =current_lineup_info.Oppo_Two_FGA+1
                    current_lineup_info.Oppo_Two_FGM =current_lineup_info.Oppo_Two_FGM+1
                    player_who_scored = FGA.strip()
                    current_lineup_info.Oppo_Score =current_lineup_info.Oppo_Score+2

                if(bool(timer.search(line))==False):
                    continue 
                else:   
                    if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
                        time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
                        if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
                            current_lineup_info.Min = current_lineup_info.Min + time_interval
                            unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
                        print('unusual interval:'+str(time_interval))

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
                        time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
                        current_lineup_info.Min = current_lineup_info.Min + time_interval
                        current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
                        continue

            elif(bool(two_missed.search(line))==True):
                player_stats_match =False
                for p in current_lineup:
                    if(p.Name == FGA.strip()):
                        player_stats_match = True
                        p.FGA= p.FGA+1
                        p.FGm = p.FGm+1
                        p.Two_FGA = p.Two_FGA +1
                        p.Two_FGm = p.Two_FGm +1
                        break
                if(player_stats_match == False):
                    # print('Found an Opponent stat!!!!')
                    current_lineup_info.Oppo_FGA = current_lineup_info.Oppo_FGA +1
                    current_lineup_info.Oppo_FGm = current_lineup_info.Oppo_FGm +1
                    current_lineup_info.Oppo_Two_FGm = current_lineup_info.Oppo_Two_FGm +1
                    current_lineup_info.Oppo_Two_FGA = current_lineup_info.Oppo_Two_FGA +1

                if(bool(timer.search(line))==False):
                    continue 
                else:   
                    if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
                        time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
                        if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
                            current_lineup_info.Min = current_lineup_info.Min + time_interval
                            unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
                        print('unusual interval:'+str(time_interval))

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
                        time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
                        current_lineup_info.Min = current_lineup_info.Min + time_interval
                        current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
                        continue


            elif(bool(three_made.search(line)) == True):
                player_stats_match =False
                for p in current_lineup:
                    if(p.Name == FGA.strip()):
                        player_stats_match = True
                        p.FGA= p.FGA+1
                        p.FGM = p.FGM+1
                        p.Three_FGA = p.Three_FGA +1
                        p.Three_FGM = p.Three_FGM +1
                        p.Pts = p.Pts +3
                        made_shot_last_line = True
                        current_lineup_info.Lineup_Score+=3
                        player_who_scored = p.Name
                        break

                if(player_stats_match == False):
                    # print('Found an Opponent stat!!!!')
                    current_lineup_info.Oppo_FGA = current_lineup_info.Oppo_FGA +1
                    current_lineup_info.Oppo_FGM = current_lineup_info.Oppo_FGM +1
                    current_lineup_info.Oppo_Three_FGA = current_lineup_info.Oppo_Three_FGA+1
                    current_lineup_info.Oppo_Three_FGM = current_lineup_info.Oppo_Three_FGM+1
                    player_who_scored = FGA.strip()
                    current_lineup_info.Oppo_Score = current_lineup_info.Oppo_Score + 3

                if(bool(timer.search(line))==False):
                    continue 
                else:   
                    if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
                        time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
                        if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
                            current_lineup_info.Min = current_lineup_info.Min + time_interval
                            unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
                        print('unusual interval:'+str(time_interval))

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
                        time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
                        current_lineup_info.Min = current_lineup_info.Min + time_interval
                        current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
                        continue

            elif(bool(three_miss.search(line)) == True):
                player_stats_match =False
                for p in current_lineup:
                    if(p.Name == FGA.strip()):
                        player_stats_match = True
                        p.FGA= p.FGA+1
                        p.FGm = p.FGm+1
                        p.Three_FGA = p.Three_FGA +1
                        p.Three_FGm = p.Three_FGm +1
                        break
                if(player_stats_match == False):
                    # print('Found an Opponent stat!!!!')
                    current_lineup_info.Oppo_FGA = current_lineup_info.Oppo_FGA + 1
                    current_lineup_info.Oppo_FGm = current_lineup_info.Oppo_FGm + 1
                    current_lineup_info.Oppo_Three_FGA= current_lineup_info.Oppo_Three_FGA +1
                    current_lineup_info.Oppo_Three_FGm= current_lineup_info.Oppo_Three_FGm +1

                if(bool(timer.search(line))==False):
                    continue 
                else:   
                    if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
                        time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
                        if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
                            current_lineup_info.Min = current_lineup_info.Min + time_interval
                            unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
                        print('unusual interval:'+str(time_interval))

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
                        time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
                        current_lineup_info.Min = current_lineup_info.Min + time_interval
                        current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
                        continue

        elif(in_one_possesion==True and bool(freethrow_attempt.search(line))==True):
            
            FT_attempt= freethrow_attempt.search(line).group(1)
            if(bool(freethrow_made.search(line)) == True):
                player_stats_match =False
                for p in current_lineup:
                    if(p.Name == FT_attempt.strip()):
                        player_stats_match = True
                        p.FTA= p.FTA+1
                        p.FTM= p.FTM+1
                        p.Pts = p.Pts+1
                        current_lineup_info.Lineup_Score+=1
                        break
                if(player_stats_match==False):
                    # print('Found an Opponent stat!!!!')
                    current_lineup_info.Oppo_FTA = current_lineup_info.Oppo_FTA +1
                    current_lineup_info.Oppo_FTM = current_lineup_info.Oppo_FTM+1
                    current_lineup_info.Oppo_Score =current_lineup_info.Oppo_Score + 1

                if(bool(timer.search(line))==False):
                    continue 
                else:   
                    if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
                        time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
                        if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
                            current_lineup_info.Min = current_lineup_info.Min + time_interval
                            unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
                        print('unusual interval:'+str(time_interval))

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
                        time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
                        current_lineup_info.Min = current_lineup_info.Min + time_interval
                        current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
                        continue

            if(bool(freethrow_miss.search(line)) == True):
                player_stats_match =False
                for p in current_lineup:
                    if(p.Name == FT_attempt.strip()):
                        player_stats_match =True
                        p.FTA= p.FTA+1
                        p.FTm= p.FTm+1
                        break
                if(player_stats_match ==False):
                    # print('Found an Opponent stat!!!!')
                    current_lineup_info.Oppo_FTA = current_lineup_info.Oppo_FTA +1
                    current_lineup_info.Oppo_FTm = current_lineup_info.Oppo_FTm +1

                if(bool(timer.search(line))==False):
                    continue 
                else:   
                    if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
                        time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
                        if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
                            current_lineup_info.Min = current_lineup_info.Min + time_interval
                            unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
                        print('unusual interval:'+str(time_interval))

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
                        time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
                        current_lineup_info.Min = current_lineup_info.Min + time_interval
                        current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

                    elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
                        continue

        elif(in_one_possesion==True and bool(assist.search(line))==True):
            assist_name = assist.search(line).group(1)
            player_stats_match =False
            for p in current_lineup:
                if(p.Name == assist_name.strip()):
                    player_stats_match = True
                    p.Ast = p.Ast+1
                    p.pass_to(player_who_scored)
                    break
            if(player_stats_match == False):
                # print('Found an Opponent stat!!!!')
                current_lineup_info.Oppo_Ast =current_lineup_info.Oppo_Ast+1

            if(bool(timer.search(line))==False):
                continue 
            else:   
                if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
                    time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
                    if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
                        current_lineup_info.Min = current_lineup_info.Min + time_interval
                        unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
                    print('unusual interval:'+str(time_interval))

                elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
                    time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
                    current_lineup_info.Min = current_lineup_info.Min + time_interval
                    current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

                elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
                    continue

        elif(in_one_possesion==True and bool(steal.search(line))==True):
            steal_name = steal.search(line).group(1)
            player_stats_match =False
            for p in current_lineup:
                if(p.Name == steal_name.strip()):
                    player_stats_match = True
                    p.Stl = p.Stl+1 
                    break
            if(player_stats_match == False):
                # print('Found an Opponent stat!!!!')
                current_lineup_info.Oppo_Stl+=1

            if(bool(timer.search(line))==False):
                continue 
            else:   
                if(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 > current_time)):
                    time_interval =float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 - current_time
                    if(float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 != unusual_time):
                        current_lineup_info.Min = current_lineup_info.Min + time_interval
                        unusual_time = float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60
                    print('unusual interval:'+str(time_interval))

                elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 < current_time)): 
                    time_interval = current_time - (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60)
                    current_lineup_info.Min = current_lineup_info.Min + time_interval
                    current_time = float(timer.search(line).group(1))+float(timer.search(line).group(2))/60

                elif(bool(timer.search(line)) == True and (float(timer.search(line).group(1)) + float(timer.search(line).group(2))/60 == current_time)):
                    continue

                        
        else:
            continue

    for n in first_half_lineup_info:
        if(n.Min == 0):
            continue
        else:
            final_first_half_lineup_info.append(n)

    for n in second_half_lineup_info:
        if(n.Min == 0):
            continue
        else:
            final_second_half_lineup_info.append(n)

    if(len(overtime_lineup_info)>0):
        for n in overtime_lineup_info:
             if(n.Min == 0):
                 continue
             else:
                 final_overtime_lineup_info.append(n)

     
    print('WE HAVE '+str(len(first_half_lineups)) +' DIFFERENT REAL LINE - UPS !!!\n\n\n')
    for n in first_half_lineups:
        for m in n:
            print(m.Name +' '+ str(m.Pts)+ " Pts  "+str(m.OffReb)+" OffReb  "+str(m.DefReb)+" DefReb  "+str(m.FGA)+" FGA  "+ str(m.FGM) +' FGM  '+ str(m.FGm)+" FGm  "+
                str(m.Two_FGA)+" 2FGA  "+str(m.Two_FGM)+" 2FGM  " + str(m.Three_FGA)+" 3FGA  " + str(m.Three_FGM)+" 3FGM  " +str(m.Three_FGm)+ ' 3FGm  ' + str(m.Ast)+' Ast  '+str(m.Stl)+' Stl  ')

        print('\n\n\n')

    print("End Of First HALF   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n")
    

    print('WE HAVE '+str(len(second_half_lineups)) +' DIFFERENT REAL LINE - UPS !!!\n\n\n')
    for n in second_half_lineups:
        for m in n:
            print(m.Name +' '+ str(m.Pts)+ " Pts  "+str(m.OffReb)+" OffReb  "+str(m.DefReb)+" DefReb  "+str(m.FGA)+" FGA  "+ str(m.FGM) +' FGM  '+ str(m.FGm)+" FGm  "+
                str(m.Two_FGA)+" 2FGA  "+str(m.Two_FGM)+" 2FGM  " + str(m.Three_FGA)+" 3FGA  " + str(m.Three_FGM)+" 3FGM  " +str(m.Three_FGm)+ ' 3FGm  ' + str(m.Ast)+' Ast  '+str(m.Stl)+' Stl  ')

        print('\n\n\n')

    
    print('WE HAVE '+str(len(overtime_lineups)) +' DIFFERENT REAL LINE - UPS !!!\n\n\n')
    for n in overtime_lineups:
        for m in n:
            print(m.Name +' '+ str(m.Pts)+ " Pts  "+str(m.OffReb)+" OffReb  "+str(m.DefReb)+" DefReb  "+str(m.FGA)+" FGA  "+ str(m.FGM) +' FGM  '+ str(m.FGm)+" FGm  "+
                str(m.Two_FGA)+" 2FGA  "+str(m.Two_FGM)+" 2FGM  " + str(m.Three_FGA)+" 3FGA  " + str(m.Three_FGM)+" 3FGM  " +str(m.Three_FGm)+ ' 3FGm  ' + str(m.Ast)+' Ast  '+str(m.Stl)+' Stl  ')
        print('\n\n\n')

    for n in first_half_lineups:
        for m in n:
            print(m.Name)
        print('\n\n')

    for n in second_half_lineups:
        for m in n:
            print(m.Name)
        print('\n\n')
    # print('Number of Lineup in overtime: '+ str(len(overtime_lineups)))
    for n in overtime_lineups:
        for m in n:
            print(m.Name)
        print('\n\n')

    print('Number of Lineup_info in first_half: '+ str(len(final_first_half_lineup_info)))
    for n in final_first_half_lineup_info:
        print(" Min = " + str(n.Min) + ", Lineup_Score = " + str(n.Lineup_Score) + ", Oppo_Score = " +str(n.Oppo_Score) + ", Oppo_FGA = "+ str(n.Oppo_FGA) + ", Oppo_FGM = "+str(n.Oppo_FGM) +
        ", Oppo_FGm = " + str(n.Oppo_FGm) + ", Oppo_Two_FGA = " + str(n.Oppo_Two_FGA) +", Oppo_Two_FGM = " + str(n.Oppo_Two_FGM) + ", Oppo_Two_FGm = " +str(n.Oppo_Two_FGm) +", Oppo_Three_FGA = " + str(n.Oppo_Three_FGA)+
        ", Oppo_Three_FGM = " + str(n.Oppo_Three_FGM) +", Oppo_Three_FGm = " + str(n.Oppo_Three_FGm) + ", Oppo_DefReb" + str(n.Oppo_DefReb) + ", Oppo_TtlReb = " + str(n.Oppo_TtlReb) +", Oppo_OffReb = " + str(n.Oppo_OffReb) +
        ", Oppo_FTA = " + str(n.Oppo_FTA) + ", Oppo_FTm " + str(n.Oppo_FTm) +", Oppo_FTM = " + str(n.Oppo_FTM) + ", Oppo_Ast = "+ str(n.Oppo_Ast) + ", Oppo_Stl = "+ str(n.Oppo_Stl))
        print('\n\n')

    print("End of 1 ST Half!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")

    print('Number of Lineup_info in second_half: '+ str(len(final_second_half_lineup_info)))
    for n in final_second_half_lineup_info:
        print(" Min = " + str(n.Min) + ", Lineup_Score = " + str(n.Lineup_Score) + ", Oppo_Score = " +str(n.Oppo_Score) + ", Oppo_FGA = "+ str(n.Oppo_FGA) + ", Oppo_FGM = "+str(n.Oppo_FGM) +
        ", Oppo_FGm = " + str(n.Oppo_FGm) + ", Oppo_Two_FGA = " + str(n.Oppo_Two_FGA) +", Oppo_Two_FGM = " + str(n.Oppo_Two_FGM) + ", Oppo_Two_FGm = " +str(n.Oppo_Two_FGm) +", Oppo_Three_FGA = " + str(n.Oppo_Three_FGA)+
        ", Oppo_Three_FGM = " + str(n.Oppo_Three_FGM) +", Oppo_Three_FGm = " + str(n.Oppo_Three_FGm) + ", Oppo_DefReb" + str(n.Oppo_DefReb) + ", Oppo_TtlReb = " + str(n.Oppo_TtlReb) +", Oppo_OffReb = " + str(n.Oppo_OffReb) +
        ", Oppo_FTA = " + str(n.Oppo_FTA) + ", Oppo_FTm " + str(n.Oppo_FTm) +", Oppo_FTM = " + str(n.Oppo_FTM) + ", Oppo_Ast = "+ str(n.Oppo_Ast) + ", Oppo_Stl = "+ str(n.Oppo_Stl))
        print('\n\n')

    print("End of 2 ND Half!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")
    
    print('Number of Lineup_info in overtime: '+ str(len(final_overtime_lineup_info)))
    for n in final_overtime_lineup_info:
        print(" Min = " + str(n.Min) + ", Lineup_Score = " + str(n.Lineup_Score) + ", Oppo_Score = " +str(n.Oppo_Score) + ", Oppo_FGA = "+ str(n.Oppo_FGA) + ", Oppo_FGM = "+str(n.Oppo_FGM) +
        ", Oppo_FGm = " + str(n.Oppo_FGm) + ", Oppo_Two_FGA = " + str(n.Oppo_Two_FGA) +", Oppo_Two_FGM = " + str(n.Oppo_Two_FGM) + ", Oppo_Two_FGm = " +str(n.Oppo_Two_FGm) +", Oppo_Three_FGA = " + str(n.Oppo_Three_FGA)+
        ", Oppo_Three_FGM = " + str(n.Oppo_Three_FGM) +", Oppo_Three_FGm = " + str(n.Oppo_Three_FGm) + ", Oppo_DefReb" + str(n.Oppo_DefReb) + ", Oppo_TtlReb = " + str(n.Oppo_TtlReb) +", Oppo_OffReb = " + str(n.Oppo_OffReb) +
        ", Oppo_FTA = " + str(n.Oppo_FTA) + ", Oppo_FTm " + str(n.Oppo_FTm) +", Oppo_FTM = " + str(n.Oppo_FTM) + ", Oppo_Ast = "+ str(n.Oppo_Ast) + ", Oppo_Stl = "+ str(n.Oppo_Stl))
        print('\n\n')


    


    index_of_lineup = 1
    
    first_half_index = 1
    second_half_index = 2
    overtime_index = 3
    
    rows_of_lineups = []
    rows_of_lineup_info  =[]
    rows_of_assists = []
    
    name_of_lineup_index =['Game_ID','Session_ID','LineUp_ID','Player_Name','Pts','OffReb','DefReb','TtlReb','FGA','FGM','FGm','Two_FGA','Two_FGM','Two_FGm','Three_FGA','Three_FGM','Three_FGm','Ast','Stl','FTA','FTM','FTm']
    name_of_lineup_info_index = ['Game_ID','Session_ID','LineUp_ID','Min','Lineup_Score','Oppo_Score','Oppo_FGA','Oppo_FGM','Oppo_FGm','Oppo_Two_FGA','Oppo_Two_FGM','Oppo_Two_FGm','Oppo_Three_FGA','Oppo_Three_FGM','Oppo_Three_FGm',
    'Oppo_DefReb','Oppo_OffReb','Oppo_TtlReb','Oppo_FTA','Oppo_FTm','Oppo_FTM','Oppo_Ast','Oppo_Stl']

    rows_of_lineups.append(name_of_lineup_index)
    for n in first_half_lineups:
        for m in n:
            player_row = [game_id,first_half_index,index_of_lineup,m.Name,m.Pts,m.OffReb,m.DefReb,m.TtlReb,m.FGA,m.FGM,m.FGm,m.Two_FGA,m.Two_FGM,m.Two_FGm,m.Three_FGA,m.Three_FGM,m.Three_FGm,m.Ast,m.Stl,m.FTA,m.FTM,m.FTm]
            rows_of_lineups.append(player_row)
        index_of_lineup +=1

    index_of_lineup = 1
    for n in second_half_lineups:
        for m in n:
            player_row =  [game_id,second_half_index,index_of_lineup,m.Name,m.Pts,m.OffReb,m.DefReb,m.TtlReb,m.FGA,m.FGM,m.FGm,m.Two_FGA,m.Two_FGM,m.Two_FGm,m.Three_FGA,m.Three_FGM,m.Three_FGm,m.Ast,m.Stl,m.FTA,m.FTM,m.FTm]
            rows_of_lineups.append(player_row)
        index_of_lineup +=1

    index_of_lineup = 1
    for n in overtime_lineups:
        for m in n:
            player_row =  [game_id,overtime_index,index_of_lineup,m.Name,m.Pts,m.OffReb,m.DefReb,m.TtlReb,m.FGA,m.FGM,m.FGm,m.Two_FGA,m.Two_FGM,m.Two_FGm,m.Three_FGA,m.Three_FGM,m.Three_FGm,m.Ast,m.Stl,m.FTA,m.FTM,m.FTm]
            rows_of_lineups.append(player_row)
        index_of_lineup +=1



    rows_of_lineup_info.append(name_of_lineup_info_index)
    index_of_lineup = 1
    for m in first_half_lineup_info:
        lineup_info_row = [game_id,first_half_index,index_of_lineup, m.Min, m.Lineup_Score, m.Oppo_Score ,m.Oppo_FGA, m.Oppo_FGM, m.Oppo_FGm, m.Oppo_Two_FGA, m.Oppo_Two_FGM, m.Oppo_Two_FGm,
        m.Oppo_Three_FGA, m.Oppo_Three_FGM, m.Oppo_Three_FGm, m.Oppo_DefReb, m.Oppo_OffReb, m.Oppo_TtlReb, m.Oppo_FTA, m.Oppo_FTm, m.Oppo_FTM, m.Oppo_Ast, m.Oppo_Stl]
        rows_of_lineup_info.append(lineup_info_row)
        index_of_lineup +=1

    index_of_lineup = 1
    for m in second_half_lineup_info:
        lineup_info_row = [game_id,second_half_index,index_of_lineup, m.Min, m.Lineup_Score, m.Oppo_Score ,m.Oppo_FGA, m.Oppo_FGM, m.Oppo_FGm, m.Oppo_Two_FGA, m.Oppo_Two_FGM, m.Oppo_Two_FGm,
        m.Oppo_Three_FGA, m.Oppo_Three_FGM, m.Oppo_Three_FGm, m.Oppo_DefReb, m.Oppo_OffReb, m.Oppo_TtlReb, m.Oppo_FTA, m.Oppo_FTm, m.Oppo_FTM, m.Oppo_Ast, m.Oppo_Stl]
        rows_of_lineup_info.append(lineup_info_row)
        index_of_lineup +=1

    index_of_lineup = 1
    for m in overtime_lineup_info:
        lineup_info_row = [game_id,overtime_index,index_of_lineup, m.Min, m.Lineup_Score, m.Oppo_Score ,m.Oppo_FGA, m.Oppo_FGM, m.Oppo_FGm, m.Oppo_Two_FGA, m.Oppo_Two_FGM, m.Oppo_Two_FGm,
        m.Oppo_Three_FGA, m.Oppo_Three_FGM, m.Oppo_Three_FGm, m.Oppo_DefReb, m.Oppo_OffReb, m.Oppo_TtlReb, m.Oppo_FTA, m.Oppo_FTm, m.Oppo_FTM, m.Oppo_Ast, m.Oppo_Stl]
        rows_of_lineup_info.append(lineup_info_row)
        index_of_lineup +=1


    



    directory = 'C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open('C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/player_lineups_'+game_id+'.csv','a', newline = '') as ft1:
        a = csv.writer(ft1,delimiter = ',')
        a.writerows(rows_of_lineups)

    with open('C:/Users/lchen/Desktop/Some_valuable_queries/Play_By_Play/LineUps/player_lineups_info_'+game_id+'.csv','a', newline = '') as ft2:
        b = csv.writer(ft2,delimiter = ',')
        b.writerows(rows_of_lineup_info)




         
        
        
        
        
        
        
        
        
        
        