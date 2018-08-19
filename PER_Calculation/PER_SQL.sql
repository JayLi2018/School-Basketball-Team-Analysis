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

-- calculate team_poss and opp_poss
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


