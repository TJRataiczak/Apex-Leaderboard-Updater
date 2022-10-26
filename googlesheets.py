import gspread
from oauth2client.service_account import ServiceAccountCredentials

gc = gspread.service_account(filename = 'apex-gaming-leaderboard-6c333513634d.json')

gsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1xaPFDqGpuA0t77mZ6CKpcEmaFoBC6klrS6pumivjlV4/edit#gid=0')
mydata = gsheet.sheet1.get_all_records()

print(mydata)