from tkinter import *

Questionfont = ('arial', 40, 'bold')
Answerfont = ('arial', 30)
Namefont = ('arial', 20)

class GueEy:

	def __init__(self, users):
		self.users = users
		self.question_id = 0
		self.root = Tk()
		self.root.title("Quiz")
		self.label_question = Label(
			self.root, text="Name Select", font=Questionfont)
		self.label_question.grid(row=1, column=1, columnspan=2)

		self.label_username = Label(
			self.root, text="Username:", font=Answerfont)
		self.label_username.grid(row=2, column=1)

		self.User_username = StringVar()

		self.input_username = Entry(self.root, font=Answerfont, textvariable=self.User_username)
		self.input_username.grid(row=2, column=2)

		self.btn_submit = Button(self.root, text="Submit", command= self.confirm, font=Namefont)
		self.btn_submit.grid(row=3, column=1, columnspan=2)

		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_columnconfigure(3, weight=1)
		self.root.grid_rowconfigure(0, weight=1)
		self.root.grid_rowconfigure(4, weight=1)

	def confirm(self):
		global username
		user = self.User_username.get()
		if(user not in self.users):
			username = user
			self.root.destroy()
			return
		else:
			self.label_question['text'] = 'User Already Exists!'
		

def ask_for_username(users):
	root = GueEy(users)

	root.root.geometry("1280x720")

	root.root.mainloop()
	return username