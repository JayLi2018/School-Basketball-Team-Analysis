# Create Top3_Offensive_Contributions

CREATE VIEW Offensive_Top3_Contributions AS 
with offensive_contribution as
(
SELECT t.team_id,t.team_name,p.player_name,f.format_name, c.category_name,
e.element_name, (pa.ppp * pa.percentage_of_time) as Off_contribution
FROM team t, player p, player_average pa, category c, format f, element e
WHERE t.team_id = p.team_id AND p.player_id = pa.player_id AND c.category_id = pa.category_id AND f.format_id = pa.format_id
AND e.element_id = pa.element_id AND f.format_name = 'Offensive' AND c.category_name = 'Play Types' 
AND pa.ppp * pa.percentage_of_time is not null AND pa.ppp * pa.percentage_of_time!= 0
AND e.element_name != 'Miscellaneous'
)
select *
FROM 
(
SELECT oc.team_id,oc.team_name,oc.player_name,oc.format_name, oc.category_name,
oc.element_name,oc.off_contribution, dense_rank() OVER (partition by oc.team_id,oc.team_name,oc.player_name,oc.format_name ORDER BY Off_contribution DESC) as ranking FROM
offensive_contribution oc
) a
WHERE a.ranking <=3;

CREATE VIEW Defensive_Top3_Contributions AS 
with offensive_contribution as
(
SELECT t.team_id,t.team_name,p.player_name,f.format_name, c.category_name,
e.element_name, (pa.ppp * pa.percentage_of_time) as Off_contribution
FROM team t, player p, player_average pa, category c, format f, element e
WHERE t.team_id = p.team_id AND p.player_id = pa.player_id AND c.category_id = pa.category_id AND f.format_id = pa.format_id
AND e.element_id = pa.element_id AND f.format_name = 'Offensive' AND c.category_name = 'Play Types' 
AND pa.ppp * pa.percentage_of_time is not null AND pa.ppp * pa.percentage_of_time!= 0
AND e.element_name != 'Miscellaneous'
)
select *
FROM 
(
SELECT oc.team_id,oc.team_name,oc.player_name,oc.format_name, oc.category_name,
oc.element_name,oc.off_contribution, dense_rank() OVER (partition by oc.team_id,oc.team_name,oc.player_name,oc.format_name ORDER BY Off_contribution DESC) as ranking FROM
offensive_contribution oc
) a
WHERE a.ranking <=3;


