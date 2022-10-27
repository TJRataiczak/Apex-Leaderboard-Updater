class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.qualified = False

    def add_points(self, more_points):
        self.points += more_points
    
    def update_qualification(self, qual):
        self.qualified = qual

import gspread
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

gc = gspread.service_account(filename = 'apex-gaming-leaderboard-6c333513634d.json')

gsheet = gc.open_by_key('10FIaM2SmoGZZIODEm5acRNNmiIrPl4seuyfKIjtDPkQ')
all_worksheets = gsheet.worksheets()

all_players = {}


for worksheet in all_worksheets:
    if worksheet.title == 'Leaderboard':
        print("This is the Leaderboard")
    else:
        ranks_qualified = [1,2]
        for record in worksheet.get_all_records():
            if record['Name'] in all_players:
                all_players[record['Name']].add_points(record['Leaderboard Points'])
            else:
                all_players[record['Name']] = Player(record['Name'], record['Leaderboard Points'])
            
            if record['Rank'] in ranks_qualified and all_players[record['Name']].qualified == True:
                print("Qualified")
                for i in range(len(ranks_qualified)):
                    ranks_qualified[i] += 1
            elif record['Rank'] in ranks_qualified and all_players[record['Name']].qualified == False:
                print("Added Qualification")
                all_players[record['Name']].update_qualification(True)
                ranks_qualified.remove(record['Rank'])


sorted_players = sorted(all_players.items())

for person in sorted_players:
    # print(f"{sorted_players[person].name}: {sorted_players[person].qualified}")
    print(person)