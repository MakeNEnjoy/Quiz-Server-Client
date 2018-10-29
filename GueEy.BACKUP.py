from tkinter import *

Questionfont = ('arial', 50, 'bold')
Answerfont = ('arial', 30)
Namefont = ('arial', 10)

root = Tk()

label_username = Label(root, text="User: Make & Joy", font=Namefont)
label_username.grid(row=0, column=0, sticky='w')

label_username = Label(root, text="Score: over 9000", font=Namefont)
label_username.grid(row=1, column=0, sticky='w')

label_question = Label(
    root, text="What is the answer to 1 + 1?", font=Questionfont)
label_question.grid(row=2, column=1, columnspan=2)

Button_a = Button(root, text="4", font=Answerfont)
Button_a.grid(row=3, column=1, sticky=N+S+E+W)

Button_b = Button(root, text="2", font=Answerfont)
Button_b.grid(row=3, column=2, sticky=N+S+E+W)

Button_c = Button(root, text="8", font=Answerfont)
Button_c.grid(row=4, column=1, sticky=N+S+E+W)

Button_d = Button(root, text="3", font=Answerfont)
Button_d.grid(row=4, column=2, sticky=N+S+E+W)

#root.grid_columnconfigure(0, minsize=450)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(3, weight=1)

root.geometry("1280x720")

root.mainloop()
