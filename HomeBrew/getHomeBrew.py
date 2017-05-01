from Tkinter import *
import os
root = Tk()
l1 = Label(text = "Type your student number (smsd kids) or username for your mac")
l1.pack()
e1 = Entry()
e1.pack()
def create():
	name = str(e1.get())
	os.open("Users/" + name + "/usr/local",os.O_CREAT)
	os.rename()
b1 = Button(text = "Submit",command = lambda: create())
b1.pack()
print rubyFile
root.mainloop()
