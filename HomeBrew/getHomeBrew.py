#Made by Truman Raile / llTeeBombll
#It is not that complex, but I made it so...

from Tkinter import *
import os
import time
root = Tk()
l1 = Label(text = "Type your student number (smsd kids) or username for your mac")
l1.pack()
e1 = Entry()
e1.pack()
def create():
	name = str(e1.get())
	l1.config(text = "creating usr dir")
	os.open("Users/" + name + "/usr/local",os.O_CREAT)
	time.sleep(1)
	l1.config(text = "moving to folder")
	os.system("cd ~/Desktop/HomeBrew")
	os.system("echo YOUR_HOME = '" + name + "' >> install.rb")
	time.sleep(1)
	l1.config(text = "chmoding the install")
	os.system("chmod +x install.rb")
	time.sleep(1)
	l1.config(text = "installing...")
	os.system("./install.rb")
	time.sleep(1)
	l1.config(text = "editing ~/.profile and or ~/.bash_profile")
	time.sleep(1)
	os.system('echo export PATH="/usr/bin:/bin:/usr/sbin:/sbin" >> ~/.profile')
	os.system('echo export PATH="/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.profile')
	os.system('echo export PATH=/Users/'+ name + '/usr/local/bin:$PATH >> ~/.profile')
	l1.config(text = "updating brew")
	time.sleep(1)
	os.system("brew update")
	l1.config(text = "All done! Give your system 5-10 minutes to configure do not close the termianl you can corrupt brew (this is just a precaution)")
	time.sleep(1)
b1 = Button(text = "Submit",command = lambda: create())
b1.pack()
root.mainloop()
