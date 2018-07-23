import pandas as pd 


stats = pd.read_csv('C:/Users/lchen/Desktop/Some_valuable_queries/PER_calculations/final_raw_data.csv')
print(stats.head())
print(stats.columns)

													


lg= {
	'MP':14.88990073,
	'PTS':5.450290909,
	'3P':0.575527273,
	'AST':1.0128,
	'TO':1.089345455,	
	'FG':1.939672727,
	'FT':0.996072727,
	'FGA':4.507745455,
	'STL':0.469636364,
	'PF':1.418727273,
	'FTA':1.449381818,
	'TRB':2.5008,
	'ORB':0.669163636,
	'DRB':1.831781818,
	'BLK':0.207381818,
	'PACE':82.77368582
}

stats['factors'] = (2 / 3) - (0.5 * (lg.get('AST') / lg.get('FG'))) / (2 * lg.get('FG')/ lg.get('FT'))
 # factor =        (2 / 3) - (0.5 * (lg_AST        /       lg_FG)) / (2 * (lg_FG      /       lg_FT))
stats['VOP'] = lg.get('PTS') / (lg.get('FGA') - lg.get('ORB') + lg.get('TO') + 0.44 * lg.get('FTA'))
 # VOP       =        lg_PTS / (lg_FGA        -        lg_ORB + lg_TOV       + 0.44 * lg_FTA)
stats['DRB%'] = (lg.get('TRB') - lg.get('ORB')) / lg.get('TRB')
 # DRB%       = (lg_TRB        -        lg_ORB) / lg_TRB


stats['uPER'] =(1 / stats['MP']) *(stats['3P']+ (2/3) * stats['AST']+ (2 - stats['factors'] * (stats['team_ast'] / stats['team_fg'])) * stats['FG']+
 (stats['FT']*0.5 * (1 + (1 - stats['team_ast'] / stats['team_fg'])) + (2/3) * (stats['team_ast'] / stats['team_fg']))-
 stats['VOP'] * stats['TO'] - stats['VOP'] * stats['DRB%'] * (stats['FGA'] - stats['FG'])- 
 stats['VOP'] * 0.44 * (0.44 + (0.56 * stats['DRB%'])) * (stats['FTA'] - stats['FT'])+ 
 stats['VOP'] * (1 - stats['DRB%']) * (stats['TRB'] - stats['ORB'])+ 
 stats['VOP'] * stats['DRB%'] * stats['ORB']+ 
 stats['VOP'] * stats['STL']+ 
 stats['VOP'] * stats['DRB%'] * stats['BLK']-
stats['PF'] * ((lg.get('FT'))/ lg.get('PF')) - 0.44 * (lg.get('FTA')/ lg.get('PF')) * stats['VOP'])
            # ((lg_FT       /         lg_PF) - 0.44 * (lg_FTA       / lg_PF) * VOP)

stats['Pace_Adjustment'] =  lg.get('PACE')/ stats['pace_factor']

stats['aPER'] = stats['Pace_Adjustment'] * stats['uPER']
# league average aPER is calculated using player minutes played as the weights


total_minutes = 4094.7227

stats['aPER_Weights'] = stats['aPER']*stats['MP']/total_minutes

lg_aPER = 0.179484224

stats['PER'] = stats['aPER'] * (15 / lg_aPER)

stats.to_csv('PER.csv')