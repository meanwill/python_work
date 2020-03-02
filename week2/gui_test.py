#from tkinter import *
from tkinter import simpledialog,messagebox,Tk

windows = Tk()
name1 = simpledialog.askstring("Name","Enter your name")
messagebox.showinfo("info","Hello " + name1)
windows.mainloop()