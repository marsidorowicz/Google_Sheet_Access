import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://googleapis.com/auth/drive']

cred = ServiceAccountCredentials.from_json_keyfile_name('E:\\Programowanie\sigma-nimbus-278206-2a5d066f5e22.json')

gs = gspread.authorize(cred)

kontr = gs.open('Kontrahenci').sheet1

rows = kontr.get()

for row in rows:
    if 'Patryk Semczuk' in row:
        print(row[0])