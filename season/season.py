'''
---------- season.py ----------
Time    :  2022/05/04 01:16:39
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  File for the season class
'''

##### Imports #####
from nba_api.stats.endpoints import leagueseasonmatchups
from nba_api.stats.endpoints import leaguegamelog


# matchups = leagueseasonmatchups.LeagueSeasonMatchups()
# print(matchups.get_data_frames()[0].columns)
gamelog = leaguegamelog.LeagueGameLog(season='1984-85')
print(gamelog.get_data_frames()[0].head())
