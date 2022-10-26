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
        for record in worksheet.get_all_records():
            if record['Name'] in all_players:
                all_players[record['Name']] += record['Leaderboard Points']
            else:
                all_players[record['Name']] = record['Leaderboard Points']

sorted_points = sorted(all_players.items(), key=lambda x: x[1], reverse=True)

df = pd.DataFrame(sorted_points, columns=['Name', 'Leaderboard Points'])

print(df)

gd.set_with_dataframe(gsheet.sheet1, df)