from game import game
from spreadsheet import question_sheet, user_sheet
from GueEy import display
from getUsername import ask_for_username

env = game(ask_for_username, question_sheet, user_sheet)

username = env.generate_username()

questions = env.get_new_question(username)

score = display(questions)

env.store_user_data(score, username)