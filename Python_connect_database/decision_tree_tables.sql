    WITH Stat1 as (
    SELECT p1.player_name as player_name,p1.player_id as player_id, pa1.percentage_of_time as PR_Ball_Handler
    FROM player p1,player_average pa1, format f1, category c1, element e1
    WHERE p1.player_id = pa1.player_id AND f1.format_id = pa1.format_id 
    AND f1.format_name= 'Offensive' AND c1.category_id = pa1.category_id
    AND c1.category_name = 'Play Types' AND e1.element_id = pa1.element_id
    AND e1.element_name = 'P&R Ball Handler' 
    ),
        Stat2 as (
    SELECT p2.player_name as player_name,p2.player_id as player_id, pa2.percentage_of_time as Transition
    FROM player p2,player_average pa2, format f2, category c2, element e2
    WHERE p2.player_id = pa2.player_id AND f2.format_id = pa2.format_id 
    AND f2.format_name= 'Offensive' AND c2.category_id = pa2.category_id
    AND c2.category_name = 'Play Types' AND e2.element_id = pa2.element_id
    AND e2.element_name = 'Transition' 
    ),
        Stat3 as (
    SELECT p3.player_name as player_name,p3.player_id as player_id, pa3.percentage_of_time as Isolation
    FROM player p3,player_average pa3, format f3, category c3, element e3
    WHERE p3.player_id = pa3.player_id AND f3.format_id = pa3.format_id 
    AND f3.format_name= 'Offensive' AND c3.category_id = pa3.category_id
    AND c3.category_name = 'Play Types' AND e3.element_id = pa3.element_id
    AND e3.element_name = 'Isolation' 
    ),
        Stat4 as (
    SELECT p4.player_name as player_name,p4.player_id as player_id, pa4.percentage_of_time as Spot_Up
    FROM player p4,player_average pa4, format f4, category c4, element e4
    WHERE p4.player_id = pa4.player_id AND f4.format_id = pa4.format_id 
    AND f4.format_name= 'Offensive' AND c4.category_id = pa4.category_id
    AND c4.category_name = 'Play Types' AND e4.element_id = pa4.element_id
    AND e4.element_name = 'Spot Up' 
    ),
        Stat5 as (
    SELECT p5.player_name as player_name,p5.player_id as player_id, pa5.percentage_of_time as Hand_Off
    FROM player p5,player_average pa5, format f5, category c5, element e5
    WHERE p5.player_id = pa5.player_id AND f5.format_id = pa5.format_id 
    AND f5.format_name= 'Offensive' AND c5.category_id = pa5.category_id
    AND c5.category_name = 'Play Types' AND e5.element_id = pa5.element_id
    AND e5.element_name = 'Hand Off' 
    ),
        Stat6 as (
    SELECT p6.player_name as player_name,p6.player_id as player_id, pa6.percentage_of_time as Offensive_Rebounds
    FROM player p6,player_average pa6, format f6, category c6, element e6
    WHERE p6.player_id = pa6.player_id AND f6.format_id = pa6.format_id 
    AND f6.format_name= 'Offensive' AND c6.category_id = pa6.category_id
    AND c6.category_name = 'Play Types' AND e6.element_id = pa6.element_id
    AND e6.element_name = 'Offensive Rebounds (put backs)' 
    ),
        Stat7 as (
    SELECT p7.player_name as player_name,p7.player_id as player_id, pa7.percentage_of_time as Off_Screen
    FROM player p7,player_average pa7, format f7, category c7, element e7
    WHERE p7.player_id = pa7.player_id AND f7.format_id = pa7.format_id 
    AND f7.format_name= 'Offensive' AND c7.category_id = pa7.category_id
    AND c7.category_name = 'Play Types' AND e7.element_id = pa7.element_id
    AND e7.element_name = 'Off Screen' 
    ),
        Stat8 as (
    SELECT p8.player_name as player_name,p8.player_id as player_id, pa8.percentage_of_time as Cut
    FROM player p8,player_average pa8, format f8, category c8, element e8
    WHERE p8.player_id = pa8.player_id AND f8.format_id = pa8.format_id 
    AND f8.format_name= 'Offensive' AND c8.category_id = pa8.category_id
    AND c8.category_name = 'Play Types' AND e8.element_id = pa8.element_id
    AND e8.element_name = 'Cut' 
    ), 
        Stat9 as (
    SELECT p9.player_name as player_name,p9.player_id as player_id, pa9.percentage_of_time as Post_Up
    FROM player p9,player_average pa9, format f9, category c9, element e9
    WHERE p9.player_id = pa9.player_id AND f9.format_id = pa9.format_id 
    AND f9.format_name= 'Offensive' AND c9.category_id = pa9.category_id
    AND c9.category_name = 'Play Types' AND e9.element_id = pa9.element_id
    AND e9.element_name = 'Post-Up' 
    ),
        Stat10 as (
    SELECT p10.player_name as player_name,p10.player_id as player_id, pa10.percentage_of_time as PR_Roll_Man
    FROM player p10,player_average pa10, format f10, category c10, element e10
    WHERE p10.player_id = pa10.player_id AND f10.format_id = pa10.format_id 
    AND f10.format_name= 'Offensive' AND c10.category_id = pa10.category_id
    AND c10.category_name = 'Play Types' AND e10.element_id = pa10.element_id
    AND e10.element_name = 'P&R Roll Man' 
    ),
        Stat11 as (
    SELECT p11.player_name as player_name,p11.player_id as player_id, pa11.percentage_of_time as Miscellaneous
    FROM player p11,player_average pa11, format f11, category c11, element e11
    WHERE p11.player_id = pa11.player_id AND f11.format_id = pa11.format_id 
    AND f11.format_name= 'Offensive' AND c11.category_id = pa11.category_id
    AND c11.category_name = 'Play Types' AND e11.element_id = pa11.element_id
    AND e11.element_name = 'Miscellaneous' 
    )

    Select Stat1.*,Stat2.Transition,Stat3.Isolation,Stat4.Spot_Up,Stat5.Hand_Off,
    Stat6.Offensive_Rebounds,Stat7.Off_Screen,Stat8.Cut,
    Stat9.Post_Up,Stat10.PR_Roll_Man,Stat11.Miscellaneous
    FROM Stat1,Stat2,Stat3,Stat4,Stat5,Stat6,Stat7,Stat8,Stat9,Stat10,Stat11
    WHERE 
    Stat1.player_id = Stat2.player_id AND Stat1.player_id = Stat3.player_id AND 
    Stat1.player_id = Stat4.player_id AND Stat1.player_id = Stat5.player_id AND
    Stat1.player_id = Stat6.player_id AND Stat1.player_id = Stat7.player_id AND
    Stat1.player_id = Stat8.player_id AND Stat1.player_id = Stat9.player_id AND 
    Stat1.player_id = Stat10.player_id AND Stat1.player_id = Stat11.player_id AND

    Stat2.player_id = Stat3.player_id AND Stat2.player_id = Stat4.player_id AND 
    Stat2.player_id = Stat5.player_id AND Stat2.player_id = Stat6.player_id AND 
    Stat2.player_id = Stat7.player_id AND Stat2.player_id = Stat8.player_id AND 
    Stat2.player_id = Stat9.player_id AND Stat2.player_id = Stat10.player_id AND 
    Stat2.player_id = Stat11.player_id AND

    Stat3.player_id = Stat4.player_id AND Stat3.player_id = Stat5.player_id AND
    Stat3.player_id = Stat6.player_id AND Stat3.player_id = Stat7.player_id AND 
    Stat3.player_id = Stat8.player_id AND Stat3.player_id = Stat9.player_id AND 
    Stat3.player_id = Stat10.player_id AND Stat3.player_id = Stat11.player_id AND

    Stat4.player_id = Stat5.player_id AND Stat4.player_id = Stat6.player_id AND 
    Stat4.player_id = Stat7.player_id AND Stat4.player_id = Stat8.player_id AND
    Stat4.player_id = Stat9.player_id AND Stat4.player_id = Stat10.player_id AND
    Stat4.player_id = Stat11.player_id AND

    Stat5.player_id = Stat6.player_id AND Stat5.player_id = Stat7.player_id AND 
    Stat5.player_id = Stat8.player_id AND Stat5.player_id = Stat9.player_id AND
    Stat5.player_id = Stat10.player_id AND Stat5.player_id = Stat11.player_id AND

    Stat6.player_id = Stat7.player_id AND Stat6.player_id = Stat8.player_id AND 
    Stat6.player_id = Stat9.player_id AND Stat6.player_id = Stat10.player_id AND
    Stat6.player_id = Stat11.player_id AND

    Stat7.player_id = Stat8.player_id AND Stat7.player_id = Stat9.player_id AND 
    Stat7.player_id = Stat10.player_id AND Stat7.player_id = Stat11.player_id AND

    Stat8.player_id = Stat9.player_id AND Stat8.player_id = Stat10.player_id AND
    Stat8.player_id = Stat11.player_id AND

    Stat9.player_id = Stat10.player_id AND Stat9.player_id = Stat11.player_id AND

    Stat10.player_id = Stat11.player_id