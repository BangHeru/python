"""
from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)

E1.pack(side = RIGHT)

top.mainloop()

"""

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.var1 =  tk.Text(self,bd=2)#  tk.Entry(bd=2)
        self.var1.pack(side="left")

        self.var2 = tk.Entry(bd=2)
        self.var2.pack(side="right")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World (click me)"
        self.hi_there["command"] = self.say_hi()
        self.hi_there.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def jumlah(self):
        #var1 = int(val1)
        #var2 = int(val2)
        print("val1 + val2")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()



