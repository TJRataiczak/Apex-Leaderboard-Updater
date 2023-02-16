class Player:
    def __init__(self, name, place):
        self.name = name
        self.placings = [place]
        self.wins = 0
        self.top_finish = 0
        self.entered_events = 0
        self.top_finish_percentage = 0
        self.win_percentage = 0
    
    def add_placing(self, new_placing):
        self.placings.append(new_placing)
    
    def update_stats(self):
        self.wins = self.placings.count(1)
        for finish in [1,2,3,4,5,6,7,8]:
            self.top_finish += self.placings.count(finish)
        self.entered_events = len(self.placings)
        self.win_percentage = self.wins / self.entered_events
        self.top_finish_percentage = self.top_finish / self.entered_events

import gspread
import gspread_dataframe as gd
from gspread_formatting import *
import pandas as pd

NORMAL_FORMAT = CellFormat(horizontalAlignment='CENTER')
gc = gspread.service_account(filename = 'apex-gaming-leaderboard-6c333513634d.json')

gsheet = gc.open_by_key('10FIaM2SmoGZZIODEm5acRNNmiIrPl4seuyfKIjtDPkQ')
all_worksheets = gsheet.worksheets()

all_players = {}

for worksheet in all_worksheets:
    if worksheet.title == 'Leaderboard':
        print("Skipping Leaderboard Sheet")
    else:
        for record in worksheet.get_all_records():
            if record['Name'] in all_players:
                all_players[record['Name']].add_placing(record['Rank'])
            else:
                all_players[record['Name']] = Player(record['Name'], record['Rank'])

player_name = []
player_wins = []
player_top_finish = []
player_events_entered = []
player_win_percentage = []
player_top_finish_percentage = []

for person in all_players:
    all_players[person].update_stats()
    player_name.append(all_players[person].name)
    player_wins.append(all_players[person].wins)
    player_events_entered.append(all_players[person].entered_events)
    player_top_finish.append(all_players[person].top_finish)
    player_win_percentage.append(all_players[person].win_percentage)
    player_top_finish_percentage.append(all_players[person].top_finish_percentage)

df_dict = {'Name': player_name,
            'Wins': player_wins,
            'Top 8s': player_top_finish,
            'Entered': player_events_entered, 
            'Win %': player_win_percentage,
            'Top 8 %': player_top_finish_percentage}

df = pd.DataFrame(df_dict)

gsheet = gc.open_by_key('1NV8DwCtsU6zazcElTmhIX6nhrNX4vXBNiwwh1LujYek')

gd.set_with_dataframe(gsheet.sheet1, df.sort_values(by=['Top 8s', 'Wins'], ascending=[False, False]))

format_cell_range(gsheet.sheet1, 'A:F', NORMAL_FORMAT)