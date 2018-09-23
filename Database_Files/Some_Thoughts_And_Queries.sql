Evaluating whether a player is clutch or not,  on 'home court' or 'road court' 
# 1. calculating the average SSTs of each player of IIT
#Winning games

select p.player_name,ps.sst,tg1.game_name,ps.player_id,tg1.game_id,p.team_id,tg1.team_game_status_id from player_single_game ps, team_game tg1, team_game tg2 ,team t,player p
where tg1.game_id = tg2.game_id and tg1.game_id = ps.game_id 
and tg1.team_id = t.team_id and t.team_name = 'IllinoisTech' and p.team_id = t.team_id
and tg1.pts - tg2.pts >0 and ps.player_id = p.player_id
order by ps.game_id;

#Losing games
select p.player_name,ps.sst,tg1.game_name,ps.player_id,tg1.game_id,p.team_id,tg1.team_game_status_id from player_single_game ps, team_game tg1, team_game tg2 ,team t,player p
where tg1.game_id = tg2.game_id and tg1.game_id = ps.game_id 
and tg1.team_id = t.team_id and t.team_name = 'IllinoisTech' and p.team_id = t.team_id
and tg1.pts - tg2.pts <0 and ps.player_id = p.player_id
order by ps.game_id;

# 2. winning within 10 points on the home court

select p.player_name,ps.sst,tg1.game_name,ps.player_id,tg1.game_id,p.team_id from player_single_game ps, team_game tg1, team_game tg2 ,team t,player p
where tg1.game_id = tg2.game_id and tg1.team_game_status_id = 1 and tg1.game_id = ps.game_id 
and tg1.team_id = t.team_id and t.team_name = 'IllinoisTech' and p.team_id = t.team_id
and tg1.pts - tg2.pts >10 and  tg1.pts - tg2.pts<10 and ps.player_id = p.player_id
order by ps.sst

# 3. losing within 10 points on the home court
select p.player_name,ps.sst,tg1.game_name,ps.player_id,tg1.game_id,p.team_id from player_single_game ps, team_game tg1, team_game tg2 ,team t,player p
where tg1.game_id = tg2.game_id and tg1.team_game_status_id = 1 and tg1.game_id = ps.game_id 
and tg1.team_id = t.team_id and t.team_name = 'IllinoisTech' and p.team_id = t.team_id
and tg1.pts - tg2.pts <0 and  tg1.pts - tg2.pts>=-10 and ps.player_id = p.player_id
order by ps.sst

# 4. winning within 10 points as the guest
select p.player_name,ps.sst,tg1.game_name,ps.player_id,tg1.game_id,p.team_id from player_single_game ps, team_game tg1, team_game tg2 ,team t,player p
where tg1.game_id = tg2.game_id and tg1.team_game_status_id = 2 and tg1.game_id = ps.game_id 
and tg1.team_id = t.team_id and t.team_name = 'IllinoisTech' and p.team_id = t.team_id
and tg1.pts - tg2.pts >0 and  tg1.pts - tg2.pts<10 and ps.player_id = p.player_id
order by ps.sst

# 5. losing within 10 points as the guest
select p.player_name,ps.sst,tg1.game_name,ps.player_id,tg1.game_id,p.team_id from player_single_game ps, team_game tg1, team_game tg2 ,team t,player p
where tg1.game_id = tg2.game_id and tg1.team_game_status_id = 2 and tg1.game_id = ps.game_id 
and tg1.team_id = t.team_id and t.team_name = 'IllinoisTech' and p.team_id = t.team_id
and tg1.pts - tg2.pts <0 and  tg1.pts - tg2.pts>=-10 and ps.player_id = p.player_id
order by ps.sst

# compare the team's efficiency and the distribution of the ways they scored.
# Compare the overall ppp of each team and distribution of "Overall-halfcourt","Transition"

Select t.team_name,e.element_name,f.format_name,e.element_name, ta.ppp, ta.rank
from team_average ta, element e,category c, format f,team t
where ta.format_id = f.format_id and ta.category_id = c.category_id and ta.team_id = t.team_id
and ta.element_id = e.element_id and f.format_name = 'Offensive'
and c.category_name = 'Overall Offense' and e.element_name = 'Overall School';

Select t.team_name,e.element_name,f.format_name,e.element_name, ta.ppp,ta.percentage_of_time,ta.rank
from team_average ta, element e,category c, format f,team t
where ta.format_id = f.format_id and ta.category_id = c.category_id and ta.team_id = t.team_id
and ta.element_id = e.element_id and f.format_name = 'Offensive'
and c.category_name = 'Overall Offense' and e.element_name = 'Transition';

Select t.team_name,e.element_name,f.format_name,e.element_name, ta.ppp,ta.percentage_of_time, ta.rank
from team_average ta, element e,category c, format f,team t
where ta.format_id = f.format_id and ta.category_id = c.category_id and ta.team_id = t.team_id
and ta.element_id = e.element_id and f.format_name = 'Offensive'
and c.category_name = 'Overall Offense' and e.element_name = 'Overall Half Court';


# figure out what are the best ways of scoring for each player on certain teams
# By doing this,I thought it would be a good way to compare the difference between the ppp of the team and the ppp of a players offense types

select p.player_name,pa.poss,pa.field_goal_percentage,pa.percentage_of_time,pa.points,pa.ppp,e.element_name from player_average pa,element e,category c, format f,team t, player p
where 
(pa.format_id = f.format_id and pa.category_id = c.category_id and pa.element_id = e.element_id
and c.category_name = 'Overall Offense' and e.element_name = 'Player' and pa.player_id = p.player_id
and p.team_id  = t.team_id and t.team_name = 'IllinoisTech'
)
or
(pa.format_id = f.format_id and pa.category_id = c.category_id and pa.element_id = e.element_id
and c.category_name = 'Play Types' and pa.player_id = p.player_id
and p.team_id  = t.team_id and t.team_name = 'IllinoisTech'
)


# PER
Formula:
uPER = (1 / MP) *
[ 3P
 + (2/3) * AST
 + (2 - factor * (team_AST / team_FG)) * FG
 + (FT *0.5 * (1 + (1 - (team_AST / team_FG)) + (2/3) * (team_AST / team_FG)))
 - VOP * TOV - VOP * DRB% * (FGA - FG)
 - VOP * 0.44 * (0.44 + (0.56 * DRB%)) * (FTA - FT)
 + VOP * (1 - DRB%) * (TRB - ORB)
 + VOP * DRB% * ORB
 + VOP * STL
 + VOP * DRB% * BLK
 - PF * ((lg_FT / lg_PF) - 0.44 * (lg_FTA / lg_PF) * VOP) ] 

 factor = (2 / 3) - (0.5 * (lg_AST / lg_FG))	 / (2 * (lg_FG / lg_FT))
 VOP    = lg_PTS / (lg_FGA - lg_ORB + lg_TOV + 0.44 * lg_FTA)
 DRB%   = (lg_TRB - lg_ORB) / lg_TRB


PTS,3P,AST,turnover,FG,FT,FGA,STL,PF,FTA,TRB,ORB,DRB,BLK.
team_AST,team_FG

pace adjustment = lg_Pace / team_Pace
aPER = (pace adjustment) * uPER

Pace
Pace Factor: the formula is 40* ((Tm Poss + Opp Poss) / (2 * (Tm MP / 5)))

PER = aPER * (15 / lg_aPER)

 1) get info of possesions

get Tm_Poss
create view tm_poss as 
select t.team_id,t.team_name,ta.poss,
from team_average ta,format f,category c,element e, team t where
ta.format_id = f.format_id and ta.team_id = t.team_id and ta.category_id = c.category_id and ta.element_id = e.element_id
and f.format_name = 'Offensive' and c.category_name = 'Overall Offense' and e.element_name = 'Overall School'

get Opp_poss
create view Opp_poss as 
select t.team_id,t.team_name,ta.poss
from team_average ta,format f,category c,element e, team t where
ta.format_id = f.format_id and ta.team_id = t.team_id and ta.category_id = c.category_id and ta.element_id = e.element_id
and f.format_name = 'Defensive' and c.category_name = 'Overall Defense' and e.element_name = 'Overall School'

-- get team and opp poss
create view team_and_opp_poss as 
select tp.team_name, tp.team_id,tp.poss as team_poss,op.poss as opp_poss
from tm_poss tp, opp_poss op
where tp.team_id = op.team_id

-- get number of games played for each team
create view team_season_performance as
select distinct t.team_name,tg.season_win,tg.season_loss from team_game tg,team t
where t.team_id = tg.team_id

-- calculate team_average_poss and opp_average_poss
create view team_average_poss
select taop.team_name,(tsp.season_win+tsp.season_loss) as number_of_games,
(taop.team_poss::float)/(tsp.season_win+tsp.season_loss) as team_poss,
(taop.opp_poss::float)/(tsp.season_win+tsp.season_loss)as opp_poss
from team_and_opp_poss taop,team_season_performance tsp
where taop.team_name = tsp.team_name

-- calculate pace_factors	
create view pace_factors as 
select tap.team_name,(40 * ((tap.team_poss + tap.opp_poss) / (2 * (40*5 / 5)))) as pace_factor
from team_average_poss tap

set a filter to rule-out some "end of bench" players: only include players who played over 10 games in the last season
select t.team_name,p.player_name,tc.gp
from player p, team_cumulative tc,team t
where p.player_id = tc.player_id and t.team_id = p.team_id and tc.gp>=10

-- get league average pace_factor：lg_pace
select avg(pace_factor) from pace_factors;

league average pace: 


-- get player_stats : PTS,3P,AST,turnover,FG,FT,FGA,STL,PF,FTA,TRB,ORB,DRB,BLK.
create view per_player_raw_stats as 
select t.team_id,t.team_name,p.player_id,p.player_name,
round((tc.min)::numeric(5,2)/tc.gp,4) as mp,
round((tc.pts)::numeric(5,2)/tc.gp,4) as pts, 
round((tc.three_field_goals_made)::numeric(5,2)/tc.gp,4) as three_field_goals_made, 
round((tc.ast)::numeric(5,2)/tc.gp,4) as ast, round((tc.turnover)::numeric(5,2)/tc.gp,4) as to,
round((tc.field_goals_made)::numeric(5,2)/tc.gp,4) as fgm, round((tc.free_throw_made)::numeric(5,2)/tc.gp,4) as ft,
round((tc.field_goals_attempt)::numeric(5,2)/tc.gp,4) as fga,round((tc.stl)::numeric(5,2)/tc.gp,4) as stl,
round((tc.total_personal_fouls_commited)::numeric(5,2)/tc.gp,4) as pf,
round((tc.free_throw_attempts)::numeric(5,2)/tc.gp,4) as fta,
round((tc.ttlreb)::numeric(5,2)/tc.gp,4) as ttlreb ,round((tc.offreb)::numeric(5,2)/tc.gp,4) as offreb,
round((tc.defreb)::numeric(5,2)/tc.gp,4) as defreb,
round((tc.blk)::numeric(5,2)/tc.gp,4) as blk
from team t,player p,team_cumulative tc 
where t.team_id = tc.team_id and p.team_id = t.team_id and tc.player_id = p.player_id


# Another interesting topic I want to explore is to evaluate what kind of player someone is

-- 1)play types : what are the distributions of each kind of play and their average ppp compared with this player's average ppp
-- 2)find 2 best skills for a player and 1 potential promising skill
-- 3)filter: players who average 6 or more points are considered.

create view average_above_6 as
select t.team_name,p.player_id,p.player_name,(tc.pts::float)/tc.gp as average_pts 
from team_cumulative tc,team t,player p
where t.team_id = p.team_id and p.player_id = tc.player_id
and (tc.pts::float)/tc.gp >=6

create view average_ppp_of_good_scorer as
select t.team_name,aa6.player_name,pa.*
from team t,average_above_6 aa6,player_average pa,category c,element e,format f
where aa6.team_name= t.team_name and pa.player_id = aa6.player_id and pa.format_id = f.format_id and f.format_name = 'Offensive'
      and pa.category_id = c.category_id and c.category_name = 'Overall Offense'
	  and pa.element_id = e.element_id and e.element_name = 'Player'

create view strength_of_good_scorers as
select apogs.team_name,apogs.player_name,e.element_name,pa.percentage_of_time,pa.ppp,apogs.ppp as average_ppp,pa.field_goal_percentage
from average_ppp_of_good_scorer apogs,player_average pa,format f,category c,element e
where pa.player_id = apogs.player_id and pa.format_id = f.format_id and f.format_name = 'Offensive'
      and pa.category_id = c.category_id and c.category_name = 'Play Types'
	  and pa.element_id = e.element_id and pa.ppp >apogs.ppp
order by apogs.player_name DESC

create view weakness_of_good_scorers as
select apogs.team_name,apogs.player_name,e.element_name,pa.percentage_of_time,pa.ppp,apogs.ppp as average_ppp,pa.field_goal_percentage
from average_ppp_of_good_scorer apogs,player_average pa,format f,category c,element e
where pa.player_id = apogs.player_id and pa.format_id = f.format_id and f.format_name = 'Offensive'
      and pa.category_id = c.category_id and c.category_name = 'Play Types'
	  and pa.element_id = e.element_id and pa.ppp < apogs.ppp
order by apogs.player_name DESC

https://www.youtube.com/watch?v=nxcbuV0_WEM


#!!!!!! a prolem in database(fixed)
update team_game set average_free_throw_percentage = 0.556, total_ast = 13,total_personal_fouls_taken = 18,average_sst = 0.93,
total_3_field_goals_attempt = 17,total_free_throw_attempts = 27, total_and_one = 3, pts = 70,average_ast_to_ratio =0.76,
total_stlpos = 10, total_field_goals_made = 26, total_defreb = 28,total_2_field_goals_attempt = 41,average_adjusted_field_percentage = 0.474,
average_3_field_goal_percentage = 0.176,total_3_field_goals_missed = 14,total_personal_fouls_commited = 21,total_field_goals_missed = 32,
total_blk = 3, total_offreb = 17,total_3_field_goals_made = 3,average_2_field_goal_percentage = 0.561,average_sstexpts = 0.34,
total_turnover = 17, average_ppp = 0.8,total_stl = 4 ,total_ttlreb = 45,average_field_goal_percentage = 0.448,
total_field_goals_attempt = 58,total_2_field_goal_missed = 18,total_2_field_goals_made = 23,total_free_throw_missed = 12,total_free_throw_made =15
where game_id = 18 and team_id = 20


update team_game set average_free_throw_percentage = 0.667, total_ast = 8,total_personal_fouls_taken = 13,average_sst = 0.87,
total_3_field_goals_attempt = 27,total_free_throw_attempts = 21, total_and_one = 1, pts = 69,average_ast_to_ratio =0.8,
total_stlpos = 4, total_field_goals_made = 23, total_defreb = 20,total_2_field_goals_attempt = 30,average_adjusted_field_percentage = 0.482,
average_3_field_goal_percentage = 0.333,total_3_field_goals_missed = 18,total_personal_fouls_commited = 24,total_field_goals_missed = 34,
total_blk = 4, total_offreb = 7,total_3_field_goals_made = 9,average_2_field_goal_percentage = 0.467,average_sstexpts = 0.29,
total_turnover = 10, average_ppp = 0.9,total_stl = 	10,total_ttlreb = 27,average_field_goal_percentage = 0.404,
total_field_goals_attempt = 57,total_2_field_goal_missed = 16,total_2_field_goals_made = 14,total_free_throw_missed = 7,total_free_throw_made =14
where game_id = 18 and team_id = 18

# Evaluating teams
Evaluating teams to get the trends of the team

1.get the teams that IIT beaten

create view teams_iit_beaten as 
select t2.team_name, t2.team_id
from team_game tg1, team_game tg2, team t1, team t2
where tg1.game_id = tg2.game_id and t1.team_id = tg1.team_id and t2.team_id = tg2.team_id 
and t1.team_name = 'IllinoisTech' and t2.team_name !='IllinoisTech' and tg1.pts > tg2.pts

2.get the teams that IIT lost to

create view teams_iit_lost_to as 
select t2.team_name, t2.team_id
from team_game tg1, team_game tg2, team t1, team t2
where tg1.game_id = tg2.game_id and t1.team_id = tg1.team_id and t2.team_id = tg2.team_id 
and t1.team_name = 'IllinoisTech' and t2.team_name !='IllinoisTech' and tg1.pts < tg2.pts

3.average ppp for Offensive
create view average_offensive_overall_ppp_teams as
select t.team_name,ta.*
from team t,team_average ta,category c,element e,format f
where ta.team_id= t.team_id  and ta.format_id = f.format_id and f.format_name = 'Offensive'
      and ta.category_id = c.category_id and c.category_name = 'Overall Offense'
	  and ta.element_id = e.element_id and e.element_name = 'Overall School'

4.average ppp for Defensive
create view average_Defensive_overall_ppp_teams as
select t.team_name,ta.*
from team t,team_average ta,category c,element e,format f
where ta.team_id= t.team_id  and ta.format_id = f.format_id and f.format_name = 'Defensive'
      and ta.category_id = c.category_id and c.category_name = 'Overall Defense'
	  and ta.element_id = e.element_id and e.element_name = 'Overall School'

5.strength for Offensive 
create view offensive_strength_of_teams as
select t.team_name,e.element_name,ta.percentage_of_time,ta.ppp, aoopt.ppp as average_ppp,ta.field_goal_percentage
from team t,team_average ta,format f,category c,element e,average_Offensive_overall_ppp_teams aoopt
where ta.team_id = t.team_id and ta.team_id = aoopt.team_id and aoopt.team_id = t.team_id
      and ta.format_id = f.format_id and f.format_name = 'Offensive'
      and ta.category_id = c.category_id and c.category_name = 'Play Types'
	  and ta.element_id = e.element_id and ta.ppp >aoopt.ppp
order by aoopt.team_name DESC

6. weakness for Offensive
create view offensive_weakness_of_teams as
select t.team_name,e.element_name,ta.percentage_of_time,ta.ppp, aoopt.ppp as average_ppp,ta.field_goal_percentage
from team t,team_average ta,format f,category c,element e,average_Offensive_overall_ppp_teams aoopt
where ta.team_id = t.team_id and ta.team_id = aoopt.team_id and aoopt.team_id = t.team_id
      and ta.format_id = f.format_id and f.format_name = 'Offensive'
      and ta.category_id = c.category_id and c.category_name = 'Play Types'
	  and ta.element_id = e.element_id and ta.ppp < aoopt.ppp
order by aoopt.team_name DESC

7. strength for Defensive
create view Defensive_strength_of_teams as
select t.team_name,e.element_name,ta.percentage_of_time,ta.ppp, adopt.ppp as average_ppp,ta.field_goal_percentage
from team t,team_average ta,format f,category c,element e,average_Defensive_overall_ppp_teams adopt
where ta.team_id = t.team_id and ta.team_id = adopt.team_id and adopt.team_id = t.team_id
      and ta.format_id = f.format_id and f.format_name = 'Defensive'
      and ta.category_id = c.category_id and c.category_name = 'Play Types'
	  and ta.element_id = e.element_id and ta.ppp < adopt.ppp
order by adopt.team_name DESC

8. weakness for Defensive
create view Defensive_weakness_of_teams as
select t.team_name,e.element_name,ta.percentage_of_time,ta.ppp, adopt.ppp as average_ppp,ta.field_goal_percentage
from team t,team_average ta,format f,category c,element e,average_Defensive_overall_ppp_teams adopt
where ta.team_id = t.team_id and ta.team_id = adopt.team_id and adopt.team_id = t.team_id
      and ta.format_id = f.format_id and f.format_name = 'Defensive'
      and ta.category_id = c.category_id and c.category_name = 'Play Types'
	  and ta.element_id = e.element_id and ta.ppp > adopt.ppp
order by adopt.team_name DESC



## Try to find some correlations between game_results and opponent play_types

1.get score_difference
create view game_score_difference as
select t2.team_name,tg2.game_id,(tg1.pts-tg2.pts) as score_difference
from team t1, team t2, team_game tg1, team_game tg2
where t1.team_id = tg1.team_id and t2.team_id = tg2.team_id and t1.team_name = 'IllinoisTech'and tg1.game_id = tg2.game_id
and t2.team_name != 'IllinoisTech'
	

2. get the table of ppp of each type and score_difference in games
select t.team_name,f.format_name,e.element_name as play_type,ta.percentage_of_time,ta.ppp,gsd.score_difference
from team t,team_average ta,category c,element e,format f,game_score_difference gsd
where t.team_name = gsd.team_name and ta.team_id= t.team_id  and ta.format_id = f.format_id and f.format_name = 'Defensive'
      and ta.category_id = c.category_id and c.category_name = 'Play Types'
	  and ta.element_id = e.element_id 
order by e.element_name



## Find the percentage of possesions each player take from the team

1. create team_and_opp_poss view
create view team_and_opponet_poss as
select tap.*,t.team_id
from team_average_poss tap,team t
where tap.team_name = t.team_name



2.get player overall poss and team_avrage_poss
create view player_overall_and_team_avg_poss as
select taop.team_name, p.player_name, pa.poss as player_overall_poss, taop.team_poss as team_average_poss
from team_and_opponet_poss as taop, player p,player_average pa,category c, format f, element e
where p.player_id = pa.player_id and p.team_id = taop.team_id
and pa.format_id = f.format_id and f.format_name = 'Offensive'
and pa.category_id = c.category_id and c.category_name = 'Overall Offense'
and pa.element_id = e.element_id and e.element_name = 'Player'


3.get player number of games played
create view number_of_games_player_played as
select t.*,p.player_name,tc.gp
from team t, team_cumulative tc, player p
where t.team_id = tc.team_id and tc.player_id = p.player_id

4.get average player poss and team average poss
create view player_poss_in_team_poss as 
select nogpp.team_name,nogpp.player_name, (poatap.player_overall_poss::float)/nogpp.gp as player_average_poss, poatap.team_average_poss,
((poatap.player_overall_poss::float)/nogpp.gp)/poatap.team_average_poss as poss_ratio
from player_overall_and_team_avg_poss poatap, number_of_games_player_played nogpp
where poatap.player_name = nogpp.player_name


## update the player_strength_weakness

1. get avg(points),avg(minutes)

create view avg_pts_and_minutes as
select t.team_name,p.player_id,p.player_name,(tc.pts::float)/tc.gp as average_pts,(tc.Min::float)/tc.gp as average_minutes
from team_cumulative tc,team t,player p
where t.team_id = p.team_id and p.player_id = tc.player_id

2. get avg(overall_Offensive_ppp)
create view avg_pts_minutes_overallOffensivePPP as
select apam.*,pa.ppp as overall_average_ppp
from avg_pts_and_minutes apam,player_average pa,category c,element e,format f
where pa.player_id = apam.player_id and pa.format_id = f.format_id and f.format_name = 'Offensive'
      and pa.category_id = c.category_id and c.category_name = 'Overall Offense'
        and pa.element_id = e.element_id and e.element_name = 'Player'


3.offensive_strength_of_all_players
create view offensive_strength_of_all_players as
select apmo.*,e.element_name,pa.percentage_of_time,pa.ppp as type_ppp,pa.field_goal_percentage
from avg_pts_minutes_overallOffensivePPP apmo,player_average pa,format f,category c,element e
where pa.player_id = apmo.player_id and pa.format_id = f.format_id and f.format_name = 'Offensive'
      and pa.category_id = c.category_id and c.category_name = 'Play Types'
        and pa.element_id = e.element_id and pa.ppp >apmo.overall_average_ppp
order by apmo.player_name DESC

4.offensive_weakness_of_all_players
create view offensive_weakness_of_all_players as
select apmo.*,e.element_name,pa.percentage_of_time,pa.ppp as type_ppp,pa.field_goal_percentage
from avg_pts_minutes_overallOffensivePPP apmo,player_average pa,format f,category c,element e
where pa.player_id = apmo.player_id and pa.format_id = f.format_id and f.format_name = 'Offensive'
      and pa.category_id = c.category_id and c.category_name = 'Play Types'
        and pa.element_id = e.element_id and pa.ppp <apmo.overall_average_ppp
order by apmo.player_name DESC

5. get avg(overall_Defensive_ppp)
create view avg_pts_minutes_overallDefensivePPP as
select apam.*,pa.ppp as overall_average_ppp
from avg_pts_and_minutes apam,player_average pa,category c,element e,format f
where pa.player_id = apam.player_id and pa.format_id = f.format_id and f.format_name = 'Defensive'
      and pa.category_id = c.category_id and c.category_name = 'Overall Defense'
        and pa.element_id = e.element_id and e.element_name = 'Player'

6.Defensive_strength_of_all_players
create view Defensive_strength_of_all_players as
select apmo.*,e.element_name,pa.percentage_of_time,pa.ppp as type_ppp,pa.field_goal_percentage
from avg_pts_minutes_overallDefensivePPP apmo,player_average pa,format f,category c,element e
where pa.player_id = apmo.player_id and pa.format_id = f.format_id and f.format_name = 'Defensive'
      and pa.category_id = c.category_id and c.category_name = 'Play Types'
        and pa.element_id = e.element_id and pa.ppp < apmo.overall_average_ppp
order by apmo.player_name DESC

7.Defensive_weakness_of_all_players
create view offensive_weakness_of_all_players as
select apmo.*,e.element_name,pa.percentage_of_time,pa.ppp as type_ppp,pa.field_goal_percentage
from avg_pts_minutes_overallDefensivePPP apmo,player_average pa,format f,category c,element e
where pa.player_id = apmo.player_id and pa.format_id = f.format_id and f.format_name = 'Defensive'
      and pa.category_id = c.category_id and c.category_name = 'Play Types'
        and pa.element_id = e.element_id and pa.ppp >apmo.overall_average_ppp
order by apmo.player_name DESC


get play-by-play lineupinfo
select li.*, tg.game_name, p.player_name
from lineupinfo li, team_game tg, player p, session s
where li.session_id = s.session_id and li.player_id = p.player_id
and li.game_id = tg.game_id and li.game_status_id = tg.team_game_status_id


Best 5 :

1) field_goal_percentage
2) 3_point_field_goal_percentage
3) Rebound
4) free_throw_percentage
5) effective_field_goal_percentage
6) True_shooting_percentage

Stats we need :
FGA,3FGA,FGM,FGm,3FGM,3FGm,Min,DefReb,OffReb,TtlReb,FTA,FTm,FTM 
1.field_goal_attempts --> "Made","Miss"
2.3_point_field_goal_percentage --> "3 Point Attempt","Miss 3 Pts"，"Make 3 Pts","Long/3pt",
3.Rebound --> "Defensive Rebound","Offensive Rebound"
4.free_throw_percentage --> "Free Throw > Made", "Free Throw > Missed"


Plus/Minus 
1)Individual evaluation

select p.player_name, li.* 
from player p,lineupinfo li
where p.player_id  = li.player_id 
group by p.name 

player_single_game_plus/Minus:

create view single_player_single_game_plus_minus as
select p.player_name,tg.game_name,pm.* from
(select player_id,game_id,sum(plus_minus) as plus_minus,sum(min) as minutes_played 
 from lineupinfo group by player_id,game_id) as pm,player p,team_game tg
 where p.player_id = pm.player_id and tg.game_id = pm.game_id
 order by pm.game_id

combine with score difference:

select spsgpm.*,gsd.score_difference 
from game_score_difference gsd,single_player_single_game_plus_minus spsgpm
where spsgpm.game_id = gsd.game_id

player_overall
select p.player_name,pm.* from
(select player_id,sum(plus_minus) as plus_minus,sum(min) as minutes_played 
 from lineupinfo group by player_id) as pm,player p
 where p.player_id = pm.player_id


create a view for iit lineup cumulative info

create view iit_lineup_cumulative_info as
select game_id,session_id,lineup_id,game_status_id, sum(li.OffReb) as OffReb,sum(li.DefReb) as DefReb,	
sum(li.TtlReb) as TtlReb,sum(li.FGA) as FGA,sum(li.FGMade) as FGMade,
sum(li.FGmiss) as FGmiss,sum(li.Two_FGA) as Two_FGA, sum(Two_FGMade) as Two_FGMade,
sum(Two_FGmiss) as Two_FGmiss,sum(li.Three_FGA) as Three_FGA, sum(li.Three_FGMade) as Three_FGMade,
sum(li.Three_Fgmiss) as Three_Fgmiss, sum(li.Ast) as ast,sum(li.Stl) as stl, sum(li.FTA) as FTA,
sum(li.FTMade) as FTMade,sum(li.FTmiss) as FTmiss
from lineupinfo li
group by game_id,session_id,lineup_id,game_status_id
order by game_id,session_id,lineup_id,game_status_id


GET SQUADS INFO BASED ON 5 NAMES

select p1.player_name,p2.player_name,p3.player_name,p4.player_name,p5.player_name,sum(l_1.Min) as Min,sum(l_1.Lineup_Score) as Lineup_Score,
sum(l_1.Oppo_Score) as Oppo_Score,sum(l_1.plus_minus) as plus_minus,sum(ilci.OffReb) as OffReb,sum(ilci.DefReb) as DefReb,	
sum(ilci.TtlReb) as TtlReb,sum(ilci.FGA) as FGA,sum(ilci.FGMade) as FGMade,
sum(ilci.FGmiss) as FGmiss,sum(ilci.Two_FGA) as Two_FGA, sum(ilci.Two_FGMade) as Two_FGMade,
sum(ilci.Two_FGmiss) as Two_FGmiss,sum(ilci.Three_FGA) as Three_FGA, sum(ilci.Three_FGMade) as Three_FGMade,
sum(ilci.Three_Fgmiss) as Three_Fgmiss, sum(ilci.Ast) as ast,sum(ilci.Stl) as stl, sum(ilci.FTA) as FTA,
sum(ilci.FTMade) as FTMade,sum(ilci.FTmiss) as FTmiss,
sum(l_1.Oppo_FGA) as Oppo_FGA,
sum(l_1.Oppo_FGmade) as Oppo_FGmade,sum(l_1.Oppo_FGmiss) as Oppo_FGmiss,sum(l_1.Oppo_Two_FGA) Oppo_Two_FGA,sum(l_1.Oppo_Two_FGMade) Oppo_Two_FGMade,
sum(l_1.Oppo_Two_FGmiss) as Oppo_Two_FGmiss, sum(l_1.Oppo_Three_FGA) as Oppo_Three_FGA, sum(l_1.Oppo_Three_FGMade) as Oppo_Three_FGMade,
sum(l_1.Oppo_Three_FGmiss) as Oppo_Three_FGmiss,sum(l_1.Oppo_DefReb) as Oppo_DefReb, sum(l_1.Oppo_OffReb) as Oppo_OffReb,
sum(l_1.Oppo_TtlReb) as Oppo_TtlReb, sum(l_1.Oppo_FTA) as Oppo_FTA, sum(l_1.Oppo_FTmade) as Oppo_FTmade ,sum(l_1.Oppo_FTMiss) as Oppo_FTMiss,
sum(l_1.Oppo_Ast) as Oppo_Ast,sum(l_1.Oppo_Stl) as Oppo_Stl
from lineupinfo l_1, lineupinfo l_2, lineupinfo l_3, lineupinfo l_4, 
lineupinfo l_5, player p1,player p2,player p3,player p4, player p5,iit_lineup_cumulative_info ilci
where p1.player_id = l_1.player_id and p2.player_id = l_2.player_id and p3.player_id = l_3.player_id and p4.player_id = l_4.player_id and
p5.player_id = l_5.player_id
and l_1.game_id = l_2.game_id and l_1.game_id = l_3.game_id and l_1.game_id = l_4.game_id and l_1.game_id = l_5.game_id
and l_1.game_id = ilci.game_id
and l_1.session_id = l_2.session_id and l_1.session_id = l_3.session_id and l_1.session_id = l_4.session_id
and l_1.session_id = l_5.session_id and l_1.session_id = ilci.session_id
and l_1.lineup_id = l_2.lineup_id and l_1.lineup_id = l_3.lineup_id and 
l_1.lineup_id = l_4.lineup_id and l_1.lineup_id = l_5.lineup_id and l_1.lineup_id = ilci.lineup_id
and l_1.game_status_id = l_2.game_status_id and l_1.game_status_id = l_3.game_status_id and l_1.game_status_id = l_4.game_status_id and l_1.game_status_id = l_5.game_status_id 
group by p1.player_name,p2.player_name,p3.player_name,p4.player_name,p5.player_name




Some potential legit squads:




select p1.player_name,p2.player_name,p3.player_name,p4.player_name,p5.player_name,sum(l_1.Min) as Min,sum(l_1.Lineup_Score) as Lineup_Score,
sum(l_1.Oppo_Score) as Oppo_Score,sum(l_1.plus_minus) as plus_minus,sum(ilci.OffReb) as OffReb,sum(ilci.DefReb) as DefReb,	
sum(ilci.TtlReb) as TtlReb,sum(ilci.FGA) as FGA,sum(ilci.FGMade) as FGMade,
sum(ilci.FGmiss) as FGmiss,sum(ilci.Two_FGA) as Two_FGA, sum(ilci.Two_FGMade) as Two_FGMade,
sum(ilci.Two_FGmiss) as Two_FGmiss,sum(ilci.Three_FGA) as Three_FGA, sum(ilci.Three_FGMade) as Three_FGMade,
sum(ilci.Three_Fgmiss) as Three_Fgmiss, sum(ilci.Ast) as ast,sum(ilci.Stl) as stl, sum(ilci.FTA) as FTA,
sum(ilci.FTMade) as FTMade,sum(ilci.FTmiss) as FTmiss,
sum(l_1.Oppo_FGA) as Oppo_FGA,
sum(l_1.Oppo_FGmade) as Oppo_FGmade,sum(l_1.Oppo_FGmiss) as Oppo_FGmiss,sum(l_1.Oppo_Two_FGA) Oppo_Two_FGA,sum(l_1.Oppo_Two_FGMade) Oppo_Two_FGMade,
sum(l_1.Oppo_Two_FGmiss) as Oppo_Two_FGmiss, sum(l_1.Oppo_Three_FGA) as Oppo_Three_FGA, sum(l_1.Oppo_Three_FGMade) as Oppo_Three_FGMade,
sum(l_1.Oppo_Three_FGmiss) as Oppo_Three_FGmiss,sum(l_1.Oppo_DefReb) as Oppo_DefReb, sum(l_1.Oppo_OffReb) as Oppo_OffReb,
sum(l_1.Oppo_TtlReb) as Oppo_TtlReb, sum(l_1.Oppo_FTA) as Oppo_FTA, sum(l_1.Oppo_FTmade) as Oppo_FTmade ,sum(l_1.Oppo_FTMiss) as Oppo_FTMiss,
sum(l_1.Oppo_Ast) as Oppo_Ast,sum(l_1.Oppo_Stl) as Oppo_Stl
from lineupinfo l_1, lineupinfo l_2, lineupinfo l_3, lineupinfo l_4, 
lineupinfo l_5, player p1,player p2,player p3,player p4, player p5,iit_lineup_cumulative_info ilci
where p1.player_id = l_1.player_id and p2.player_id = l_2.player_id and p3.player_id = l_3.player_id and p4.player_id = l_4.player_id and
p5.player_id = l_5.player_id and
and p1.player_id != p2.player_id and p1.player_id != p3.player_id and p1.player_id != p4.player_id and p1.player_id != p5.player_id
and p2.player_id != p3.player_id and p2.player_id != p4.player_id and p2.player_id != p5.player_id 
and p3.player_id != p4.player_id and p3.player_id != p5.player_id
and p4.player_id != p5.player_id
and l_1.game_id = l_2.game_id and l_1.game_id = l_3.game_id and l_1.game_id = l_4.game_id and l_1.game_id = l_5.game_id
and l_1.game_id = ilci.game_id
and l_1.session_id = l_2.session_id and l_1.session_id = l_3.session_id and l_1.session_id = l_4.session_id
and l_1.session_id = l_5.session_id and l_1.session_id = ilci.session_id
and l_1.lineup_id = l_2.lineup_id and l_1.lineup_id = l_3.lineup_id and 
l_1.lineup_id = l_4.lineup_id and l_1.lineup_id = l_5.lineup_id and l_1.lineup_id = ilci.lineup_id
and l_1.game_status_id = l_2.game_status_id and l_1.game_status_id = l_3.game_status_id and l_1.game_status_id = l_4.game_status_id and l_1.game_status_id = l_5.game_status_id 
group by p1.player_name,p2.player_name,p3.player_name,p4.player_name,p5.player_name




9.23

1. add new school names and ids.

psql -h myhost -d database_name -U username

\copy team(Team_Name,Team_ID) from 'C:\Users\lchen\Desktop\School-Basketball-Team-Analysis\Database_Files\Python_Geneate_CSVs\New_Team_Table.csv' DELIMITER ','CSV HEADER;


2. add new player names and ids

\copy player(Player_Name,Player_ID,Team_ID) from 'C:\Users\lchen\Desktop\School-Basketball-Team-Analysis\Database_Files\Python_Geneate_CSVs\Player_Average\new_school_raw_data\new_player_table.csv' DELIMITER ','CSV HEADER;


3. add new team_cumulative 

copy Team_Cumulative(Team_Cumulative_ID,Team_ID,Player_ID,GP,Min,SST,SSTexPts,Pts,Ast,Turnover,Ast_To_Ratio,Stl,StlPos,Blk,TtlReb,OffReb,DefReb,Field_Goals_Attempt,Field_Goals_Made,Field_Goals_Missed,Field_Goal_Percentage,Adjusted_Field_Goal_Percentage,Two_Field_Goals_Attempt,Two_Field_Goals_Made,Two_Field_Goals_Missed,Two_Field_Goal_Percentage,Three_Field_Goals_Attempt,Three_Field_Goals_Made,Three_Field_Goals_Missed,Three_Field_Goal_Percentage,Free_Throw_Attempts,Free_Throw_Made,Free_Throw_Missed,Free_Throw_Percentage,And_One,Personal_Fouls_Taken,Total_Personal_Fouls_Commited)from 'C:/Users/lchen/Desktop/School-Basketball-Team-Analysis/Database_Files/Python_Geneate_CSVs/Team_Cumulative/NEW_team_cumulative.csv' DELIMITER ',' CSV HEADER NULL as '-';

















