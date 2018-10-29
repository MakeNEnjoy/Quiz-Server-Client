from tkinter import *

Questionfont = ('arial', 20, 'bold')
Answerfont = ('arial', 30)
Namefont = ('arial', 20)

class GueEy:

	def __init__(self, Args):
		self.question_id = 0
		self.Args = Args
		self.root = Tk()
		self.root.title("Quiz")
		self.label_username = Label(self.root, text="User: " +
		                       Args['user'], font=Namefont)
		self.label_username.grid(row=0, column=0, sticky='w')

		self.label_score = Label(self.root, text="Score: " +
		                       str(Args['score']), font=Namefont)
		self.label_score.grid(row=1, column=0, sticky='w')

		self.label_question = Label(
			self.root, text=Args['question'][self.question_id], font=Questionfont)
		self.label_question.grid(row=2, column=1, columnspan=2)

		self.Button_a = Button(self.root, text=Args['answer_a'][self.question_id],
					font=Answerfont, command=lambda:  self.Click_Answer(0))
		self.Button_a.grid(row=3, column=1, sticky=N+S+E+W)

		self.Button_b = Button(self.root, text=Args['answer_b'][self.question_id],
                    font=Answerfont, command=lambda: self.Click_Answer(1))
		self.Button_b.grid(row=3, column=2, sticky=N+S+E+W)

		self.Button_c = Button(self.root, text=Args['answer_c'][self.question_id],
                    font=Answerfont, command=lambda: self.Click_Answer(2))
		self.Button_c.grid(row=4, column=1, sticky=N+S+E+W)

		self.Button_d = Button(self.root, text=Args['answer_d'][self.question_id],
                    font=Answerfont, command=lambda: self.Click_Answer(3))
		self.Button_d.grid(row=4, column=2, sticky=N+S+E+W)

		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_columnconfigure(3, weight=1)

	def Click_Answer(self, answer):
		if(self.Args["correct_answer"][self.question_id] == answer):
			self.Args['score'] += 1
		self.update_question()
	
	def update_question(self):
		self.question_id += 1
		if(self.question_id == len(self.Args['question'])):
			self.root.destroy()
			return
		self.label_score['text'] = "Score: " + str(self.Args['score'])
		self.label_question['text'] = self.Args['question'][self.question_id]
		self.Button_a['text'] = self.Args['answer_a'][self.question_id]
		self.Button_b['text'] = self.Args['answer_b'][self.question_id]
		self.Button_c['text'] = self.Args['answer_c'][self.question_id]
		self.Button_d['text'] = self.Args['answer_d'][self.question_id]

		

def display(Args):
	root = GueEy(Args)

	root.root.geometry("1280x720")

	root.root.mainloop()
	return root.Args['score']
