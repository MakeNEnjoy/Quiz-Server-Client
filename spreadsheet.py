import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

question_sheet = client.open('QuizMaster').sheet1
user_sheet = client.open('QuizMaster').get_worksheet(1)

'''
questions = sheet.get_all_records()
questions = sheet.row_values(2)
questions = sheet.col_values(2)
sheet.update_cell(2,2,'Hello World')
for i in range(2,4):
	print(sheet.cell(i,2).value)
'''
