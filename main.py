import pandas as pd

class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    def add_points(self, points):
        self.points = self.points + points


all_players = {}

xl = pd.ExcelFile('Apex Gaming Season 2 Leaderboard.xlsx')

all_sheets = xl.sheet_names

for current_sheet in all_sheets:
    if current_sheet != 'Leaderboard':
        first_event = xl.parse(current_sheet, usecols=('Rank', 'Name', 'Points'))
        for player in zip(first_event['Name'], first_event["Points"]):
            current_player = all_players.get(player[0])
            print(player)
            if current_player != None:
                all_players[player[0]].add_points(player[1])
            else:
                all_players[player[0]] = Player(player[0], player[1])

print(all_players['Maxx Turner'].points)