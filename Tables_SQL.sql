CREATE TABLE FORMAT
(
  Format_Name VARCHAR(100) NOT NULL,
  Format_ID INT NOT NULL,
  PRIMARY KEY (Format_ID)
);

CREATE TABLE CATEGORY
(
  Category_Name VARCHAR(100) NOT NULL,
  Category_ID INT NOT NULL,
  Category_Description VARCHAR(1000) NOT NULL,
  PRIMARY KEY (Category_ID)
);

CREATE TABLE ELEMENT
(
  Element_Name VARCHAR(100) NOT NULL,
  Element_ID INT NOT NULL,
  PRIMARY KEY (Element_ID)
);



CREATE TABLE TEAM
(
  Team_Name VARCHAR(100) NOT NULL,
  Team_ID INT NOT NULL,
  PRIMARY KEY (Team_ID)
);


CREATE TABLE PLAYER
(
  Player_ID INT NOT NULL,
  Player_Name VARCHAR(100) NOT NULL,
  Team_ID INT NOT NULL,
  PRIMARY KEY (Player_ID),
  FOREIGN KEY (Team_ID) REFERENCES TEAM(Team_ID)
);


CREATE TABLE PLAYER_AVERAGE
(
  Percent_Turnover FLOAT,
  Percentage_Of_Time FLOAT,
  PPP FLOAT,
  Field_Goals_Missed INT,
  Field_Goals_Attempt INT,
  Field_Goal_Percentage FLOAT,
  Adjusted_Field_Goal_Percentage FLOAT,
  Percent_Free_Throws FLOAT,
  Percent_Shooting_Foul FLOAT,
  Poss INT,
  Points INT,
  Rank FLOAT,
  Rating CHAR(30),
  Field_Goals_Made INT,
  Percent_Score FLOAT,
  Player_Average_Stats_ID INT NOT NULL,
  Category_ID INT NOT NULL,
  Element_ID INT NOT NULL,
  Format_ID INT NOT NULL,
  Player_ID INT NOT NULL,
  PRIMARY KEY (Player_Average_Stats_ID),
  FOREIGN KEY (Category_ID) REFERENCES CATEGORY(Category_ID),
  FOREIGN KEY (Element_ID) REFERENCES ELEMENT(Element_ID),
  FOREIGN KEY (Format_ID) REFERENCES FORMAT(Format_ID),
  FOREIGN KEY (Player_ID) REFERENCES PLAYER(Player_ID)
);

CREATE TABLE TEAM_AVERAGE
(
  Adjusted_Field_Goal_Percentage FLOAT,
  Field_Goal_Percentage FLOAT,
  Field_Goals_Attempt INT,
  Field_Goals_Made INT,
  Field_Goals_Missed INT,
  Rating CHAR(100),
  Rank FLOAT,
  PPP FLOAT,
  Points INT,
  Poss INT,
  Percentage_Of_Time FLOAT,
  Team_Average_Stats_ID INT NOT NULL,
  Percent_Shooting_Foul FLOAT,
  Percent_Free_Throws FLOAT,
  Percent_Turnover FLOAT,
  Percent_Score FLOAT,
  Team_ID INT NOT NULL,
  Format_ID INT NOT NULL,
  Category_ID INT NOT NULL,
  Element_ID INT NOT NULL,
  PRIMARY KEY (Team_Average_Stats_ID),
  FOREIGN KEY (Category_ID) REFERENCES CATEGORY(Category_ID),
  FOREIGN KEY (Element_ID) REFERENCES ELEMENT(Element_ID),
  FOREIGN KEY (Team_ID) REFERENCES TEAM(Team_ID)
);


CREATE TABLE TEAM_GAME_STATUS(
  Team_Game_Status_ID INT NOT NULL,
  TEAM_Game_Status_Name CHAR (10),
  PRIMARY KEY (Team_Game_Status_ID)
);

CREATE TABLE TEAM_GAME
(
  Average_Free_Throw_Percentage FLOAT NOT NULL,
  Total_Ast INT NOT NULL,
  Total_Personal_Fouls_Taken INT NOT NULL,
  Average_SST FLOAT NOT NULL,
  Game_Name VARCHAR(200) NOT NULL,
  Season_Loss INT NOT NULL,
  Total_3_Field_Goals_Attempt INT NOT NULL,
  Total_Free_Throw_Attempts INT NOT NULL,
  Total_And_One INT NOT NULL,
  First_Half INT NOT NULL,
  OT INT,
  Home_Win INT NOT NULL,
  Pts INT NOT NULL,
  Average_Ast_TO_Ratio FLOAT NOT NULL,
  Away_Win INT NOT NULL,
  Total_StlPos INT NOT NULL,
  Total_Field_Goals_Made INT NOT NULL,
  Total_DefReb INT NOT NULL,
  Total_2_Field_Goals_Attempt INT NOT NULL,
  Average_Adjusted_Field_Percentage FLOAT NOT NULL,
  Average_3_Field_Goal_Percentage FLOAT NOT NULL,
  Total_3_Field_Goals_Missed INT NOT NULL,
  Total_Personal_Fouls_Commited INT NOT NULL,
  Total_Min INT NOT NULL,
  Total_Field_Goals_Missed INT NOT NULL,
  Total_Blk INT NOT NULL,
  Total_OffReb INT NOT NULL,
  Total_3_Field_Goals_Made INT NOT NULL,
  Average_2_Field_Goal_Percentage FLOAT NOT NULL,
  Game_Date DATE NOT NULL,
  Game_ID INT NOT NULL,
  Second_Half INT NOT NULL,
  Away_Loss INT NOT NULL,
  Average_SSTexPts FLOAT NOT NULL,
  Total_Turnover INT NOT NULL,
  Average_PPP FLOAT NOT NULL,
  Total_Stl INT NOT NULL,
  Total_TtlReb INT NOT NULL,
  Average_Field_Goal_Percentage FLOAT NOT NULL,
  Total_Field_Goals_Attempt INT NOT NULL,
  Total_2_Field_Goal_Missed INT NOT NULL,
  Total_2_Field_Goals_Made INT NOT NULL,
  Total_Free_Throw_Missed INT NOT NULL,
  Total_Free_Throw_Made INT NOT NULL,
  Final_Points INT NOT NULL,
  Series_Win INT NOT NULL,
  Season_Win INT NOT NULL,
  Home_Loss INT NOT NULL,
  Team_ID INT NOT NULL,
  Team_Game_Status_ID INT NOT NULL,
  PRIMARY KEY (Game_ID,Team_Game_Status_ID),
  FOREIGN KEY (Team_Game_Status_ID) REFERENCES TEAM_GAME_STATUS(Team_Game_Status_ID),
  FOREIGN KEY (Team_ID) REFERENCES TEAM(Team_ID)
);

 CREATE TABLE  PLAYER_SINGLE_GAME(
  Player_Single_Game_ID INT NOT NULL,
  Player_ID INT NOT NULL,
  Team_ID INT NOT NULL,
  Team_Game_Status_ID INT NOT NULL,
  Game_ID INT NOT NULL,
  Min INT NOT NULL,
  SST FLOAT NOT NULL,
  SSTexPts FLOAT NOT NULL,
  Pts INT NOT NULL,
  PPP FLOAT,
  Ast INT NOT NULL,
  Turnover INT NOT NULL,
  Ast_To_Ratio FLOAT NOT NULL,
  stl INT NOT NULL,
  stlPos INT NOT NULL,
  Blk INT NOT NULL,
  TtlReb INT NOT NULL ,
  OffReb INT NOT NULL,
  DefReb INT NOT NULL,
  Field_Goals_Attempt INT NOT NULL,
  Field_Goals_Made INT NOT NULL,
  Field_Goals_Missed INT NOT NULL,
  Field_Goal_Percentage FLOAT,
  Adjusted_Field_Goal_Percentage FLOAT,
  Two_Field_Goals_Attempt INT NOT NULL,
  Two_Field_Goals_Made INT NOT NULL,
  Two_Field_Goals_Missed INT NOT NULL,
  Two_Field_Goal_Percentage FLOAT,
  Three_Field_Goals_Attempt INT NOT NULL,
  Three_Field_Goals_Made INT NOT NULL,
  Three_Field_Goals_Missed INT NOT NULL,
  Three_Field_Goal_Percentage FLOAT,
  Free_Throw_Attempts INT NOT NULL,
  Free_Throw_Made INT NOT NULL,
  Free_Throw_Missed INT NOT NULL,
  Free_Throw_Percentage FLOAT,
  And_One INT NOT NULL,
  Personal_Fouls_Taken INT NOT NULL,
  Total_Personal_Fouls_Commited INT NOT NULL,

  PRIMARY KEY(Player_Single_Game_ID),
  FOREIGN KEY(Player_ID) REFERENCES PLAYER(Player_ID),
   FOREIGN KEY(Game_ID,Team_Game_Status_ID) REFERENCES TEAM_GAME(Game_ID,Team_Game_Status_ID)
  )

copy category(Category_ID,Category_Name,Category_Description)
from 'D:\Final_Version_Tables\Category_Table.csv' DELIMITER ','CSV HEADER;

copy TEAM_GAME_STATUS(Team_Game_Status_ID,TEAM_Game_Status_Name) from 'D:\Final_Version_Tables\Team_Game_Status.csv' DELIMITER ',' CSV HEADER;

copy format(Format_ID,Format_Name)
from 'D:\Final_Version_Tables\Format_Table.csv' DELIMITER ','CSV HEADER;

copy element(Element_Name,Element_ID)
from 'D:\Final_Version_Tables\Element_Table.csv' DELIMITER ','CSV HEADER;

copy team(Team_ID,Team_Name)
from 'D:\Final_Version_Tables\Team_Table.csv' DELIMITER ','CSV HEADER;

copy player(Player_Name,Player_ID,Team_ID)
from 'D:\Final_Version_Tables\Player_Table.csv' DELIMITER ','CSV HEADER;


copy player_average(Player_Average_Stats_ID,Player_ID,Format_ID,Category_ID,Element_ID,Percentage_Of_Time,Poss,Points,PPP,Rank,Rating,Field_Goals_Missed,Field_Goals_Made,Field_Goals_Attempt,Field_Goal_Percentage,Adjusted_Field_Goal_Percentage,Percent_Turnover,Percent_Free_Throws,Percent_Shooting_Foul,Percent_Score)
from 'D:\Final_Version_Tables\Player_Average_Table.csv' DELIMITER ','CSV HEADER NULL AS '-';

copy team_average(Team_Average_Stats_ID,Team_ID,Format_ID,Category_ID,Element_ID,Percentage_Of_Time,Poss,Points,PPP,Rank,Rating,Field_Goals_Missed,Field_Goals_Made,Field_Goals_Attempt,Field_Goal_Percentage,Adjusted_Field_Goal_Percentage,Percent_Turnover,Percent_Free_Throws,Percent_Shooting_Foul,Percent_Score)                                                         
from 'D:\Final_Version_Tables\Team_Average_Table.csv' DELIMITER ','CSV HEADER NULL as '-';



copy team_game(Game_Date,Team_ID,Game_ID,Team_Game_Status_ID,Game_Name,Final_Points,First_Half,Second_Half,OT,Series_Win,Home_Win,Home_Loss,Away_Win,Away_Loss,Season_Win,Season_Loss,Total_Min,Average_SST, Average_SSTexPts,
Pts,Average_PPP,Total_Ast,Total_Turnover,Average_Ast_TO_Ratio,Total_Stl,Total_StlPos,Total_Blk,Total_TtlReb,Total_OffReb,Total_DefReb,Total_Field_Goals_Attempt,Total_Field_Goals_Made,
Total_Field_Goals_Missed,Average_Field_Goal_Percentage,Average_Adjusted_Field_Percentage,Total_2_Field_Goals_Attempt,Total_2_Field_Goals_Made,Total_2_Field_Goal_Missed,Average_2_Field_Goal_Percentage,
Total_3_Field_Goals_Attempt,Total_3_Field_Goals_Made,Total_3_Field_Goals_Missed,Average_3_Field_Goal_Percentage,Total_Free_Throw_Attempts,Total_Free_Throw_Made,Total_Free_Throw_Missed,
Average_Free_Throw_Percentage,Total_And_One,Total_Personal_Fouls_Taken,Total_Personal_Fouls_Commited)
from 'D:\Final_Version_Tables\Team_Game_Table.csv' DELIMITER ',' CSV HEADER;


copy PLAYER_SINGLE_GAME(Player_Single_Game_ID,Player_ID,Team_ID,Game_ID,Team_Game_Status_ID,Min,SST,SSTexPts,Pts,PPP,Ast,Turnover,Ast_To_Ratio,stl,
  stlPos,Blk,TtlReb,OffReb,DefReb,Field_Goals_Attempt,Field_Goals_Made,Field_Goals_Missed,Field_Goal_Percentage,Adjusted_Field_Goal_Percentage,
  Two_Field_Goals_Attempt,Two_Field_Goals_Made,Two_Field_Goals_Missed,Two_Field_Goal_Percentage,Three_Field_Goals_Attempt,Three_Field_Goals_Made,
  Three_Field_Goals_Missed,Three_Field_Goal_Percentage,Free_Throw_Attempts,Free_Throw_Made,Free_Throw_Missed,Free_Throw_Percentage,And_One,Personal_Fouls_Taken,Total_Personal_Fouls_Commited)
from 'C:\Users\lchen\Desktop\BBallDB_all_the_files\player_single_game_table.csv' DELIMITER ',' CSV HEADER NULL as '-';