import pandas as pd

all_players = {}

xl = pd.ExcelFile('Apex Gaming Season 2 Leaderboard.xlsx')

all_sheets = xl.sheet_names

for current_sheet in all_sheets:
    if current_sheet != 'Leaderboard':
        first_event = xl.parse(current_sheet, usecols=('Rank', 'Name', 'Points'))
        for player in zip(first_event['Name'], first_event["Points"]):
            if player[0] in all_players:
                all_players[player[0]] += player[1]
            else:
                all_players[player[0]] = player[1]

print(sorted(all_players.items(), key=lambda x: x[1], reverse=True))

print(len(all_players))