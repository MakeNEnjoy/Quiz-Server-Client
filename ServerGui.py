from tkinter import *
from getTable import get_data

scoreboard = get_data()

Answerfont = ('arial', 20)
Questionfont = ('arial', 20, 'bold')

root = Tk()
root.title("Scoreboard")
b = Label(root, text="Usernames", font=Questionfont)
b.grid(row=0, column=0, sticky=N+S+E+W)
b = Label(root, text="Scores", font=Questionfont)
b.grid(row=0, column=1, sticky=N+S+E+W)

height = len(scoreboard['users'])

labels = [[],[]]

for i in range(1,height+1):

	labels[0].append(Label(root, text=scoreboard['users'][i-1], font=Questionfont))
	labels[0][-1].grid(row=i, column=0, sticky=N+S+E+W)

	labels[1].append(Label(root, text=scoreboard['scores'][i-1], font=Questionfont))
	labels[1][-1].grid(row=i, column=1, sticky=N+S+E+W)


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.geometry("1280x720")

def refresh():
	scoreboard = get_data()
	height = len(scoreboard['users'])
	[i.destroy() for i in labels[0]]
	[i.destroy() for i in labels[1]]

	for i in range(1, height+1):

		labels[0].append(
			Label(root, text=scoreboard['users'][i-1], font=Questionfont))
		labels[0][-1].grid(row=i, column=0, sticky=N+S+E+W)

		labels[1].append(
			Label(root, text=scoreboard['scores'][i-1], font=Questionfont))
		labels[1][-1].grid(row=i, column=1, sticky=N+S+E+W)

	root.after(5000, refresh)


root.after(1000, refresh)

mainloop()
print(labels)
