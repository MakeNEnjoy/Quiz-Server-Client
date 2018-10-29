from tkinter import *

Questionfont = ('arial', 50, 'bold')
Answerfont = ('arial', 30)
Namefont = ('arial', 20)

class Window(Frame):


	def __init__(self, master=None):

		# parameters that you want to send through the Frame class.
		Frame.__init__(self, master)

		# reference to the master widget, which is the tk window
		self.master = master

		# with that, we want to then run init_window, which doesn't yet exist
		self.init_window()

	# Creation of init_window
	def init_window(self):

		# changing the title of our master widget
		self.master.title("GUI")

		# allowing the widget to take the full space of the root window
		
		question = Label(self, text="What is the answer to 1 + 1")
		question.grid(row=0,column=1)

		quitButton = Button(self, text="Exit", command=self.client_exit)
		quitButton.grid(row=0, column=0)

		AButton = Button(self, text="Greet", command=self.client_greet, width=50)

		# placing the button on my window
		AButton.place(x=640, y=360)
		root.grid_columnconfigure(0, minsize=500)

	def client_exit(self):
		self.text['text'] = 'Bye'

	def client_greet(self):
		self.text = Label(self, text="Hello World")
		self.text.place(x=640, y=160)


root = Tk()

# size of the window
root.geometry("1280x720")

app = Window(root)
root.mainloop()
