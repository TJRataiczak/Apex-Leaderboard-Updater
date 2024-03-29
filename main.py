class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.qualified = False
        self.highest_rank = 4000

    def add_points(self, more_points):
        self.points += more_points
    
    def update_qualification(self, qual):
        self.qualified = qual
    
    def update_highest_placing(self, rank):
        self.highest_rank = rank

import gspread
import gspread_dataframe as gd
from gspread_formatting import *
import pandas as pd

NORMAL_FORMAT = CellFormat(horizontalAlignment='CENTER')
gc = gspread.service_account(filename = 'apex-gaming-leaderboard-6c333513634d.json')

gsheet = gc.open_by_key('10FIaM2SmoGZZIODEm5acRNNmiIrPl4seuyfKIjtDPkQ')
all_worksheets = gsheet.worksheets()

all_players = {}

all_players['Randy Uebbing'] = Player('Randy Uebbing', 0)
all_players['Randy Uebbing'].update_qualification(True)


for worksheet in all_worksheets:
    if worksheet.title == 'Leaderboard':
        print("Skipping Leaderboard Sheet")
    else:
        ranks_qualified = [1,2]
        for record in worksheet.get_all_records():
            if record['Name'] in all_players:
                all_players[record['Name']].add_points(record['Leaderboard Points'])
            else:
                all_players[record['Name']] = Player(record['Name'], record['Leaderboard Points'])
            
            if record['Rank'] in ranks_qualified and all_players[record['Name']].qualified == True:
                for i in range(len(ranks_qualified)):
                    ranks_qualified[i] += 1
            elif record['Rank'] in ranks_qualified and all_players[record['Name']].qualified == False:
                all_players[record['Name']].update_qualification(True)
                ranks_qualified.remove(record['Rank'])
            
            if record['Rank'] < all_players[record['Name']].highest_rank:
                all_players[record['Name']].update_highest_placing(record['Rank'])

player_names = []
player_points = []
player_qualified = []
player_highest_placing = []

for person in all_players:
    player_names.append(all_players[person].name)
    player_points.append(all_players[person].points)
    player_qualified.append('Yes' if all_players[person].qualified == True else 'No')
    player_highest_placing.append(all_players[person].highest_rank)

df_dict = {'Name': player_names,
            'Points': player_points,
            'Qualified': player_qualified,
            'Highest Placing': player_highest_placing}

df = pd.DataFrame(df_dict)

gd.set_with_dataframe(gsheet.sheet1, df.sort_values(by=['Points', 'Highest Placing'], ascending=[False, True]), col=2)

format_cell_range(gsheet.sheet1, 'A:F', NORMAL_FORMAT)

player_names.sort()

for name in player_names:
    print(name)