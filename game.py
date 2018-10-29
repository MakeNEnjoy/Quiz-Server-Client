class game:
    def __init__(self, display, question_sheet, user_sheet):
        self.display = display
        self.question_sheet = question_sheet
        self.user_sheet = user_sheet

    def get_new_question(self, user):
        questions = self.question_sheet.col_values(2)[1:]
        choices = {
            'a': self.question_sheet.col_values(3)[1:],
            'b': self.question_sheet.col_values(4)[1:],
            'c': self.question_sheet.col_values(5)[1:],
            'd': self.question_sheet.col_values(6)[1:]}
        labels = self.question_sheet.col_values(7)[1:]

        questions = {
            "question": questions,
            "answer_a": choices['a'],
            "answer_b": choices['b'],
            "answer_c": choices['c'],
            "answer_d": choices['d'],
            "correct_answer":  list(map(int, labels)),
            "user": user,
            "score": 0
        }
        return questions

    def store_user_data(self, score, user):
        row = [user, score]
        self.user_sheet.insert_row(row, 2)

    def generate_username(self):
        users = self.user_sheet.col_values(1)[1:]
        return self.display(users)
