from tkinter import *

Questionfont = ('arial', 50, 'bold')
Answerfont = ('arial', 30)
Namefont = ('arial', 20)

class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master

	def init_window(self, arguments):
		self.master.title("GUI")

		label_username = Label(self, text="User: " + arguments["user"], font=Namefont)
		label_username.grid(row=0, column=0, sticky='w')

		label_username = Label(self, text="Score: " + arguments["score"], font=Namefont)
		label_username.grid(row=1, column=0, sticky='w')

		label_question = Label(
			self, text=arguments["question"], font=Questionfont)
		label_question.grid(row=2, column=1, columnspan=2)

		Button_a = Button(self, text=arguments["answer_a"], font=Answerfont)
		Button_a.grid(row=3, column=1, sticky=N+S+E+W)

		Button_b = Button(self, text=arguments["answer_b"], font=Answerfont)
		Button_b.grid(row=3, column=2, sticky=N+S+E+W)

		Button_c = Button(self, text=arguments["answer_c"], font=Answerfont)
		Button_c.grid(row=4, column=1, sticky=N+S+E+W)

		Button_d = Button(self, text=arguments["answer_d"], font=Answerfont)
		Button_d.grid(row=4, column=2, sticky=N+S+E+W)

		#self.grid_columnconfigure(0, weight=1)
		#self.grid_columnconfigure(3, weight=1)


def display(arguments):
	root = Tk()

	root.geometry("1280x720")

	app = Window(root)
	app.init_window(arguments)

	root.mainloop()


questions = {
	"question": "how many?",
	"answer_a": "1",
	"answer_b": "2",
	"answer_c": "3",
	"answer_d": "4",
	"user": "rblx",
	"score": "10"
}

display(questions)
