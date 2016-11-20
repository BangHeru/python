import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        BTN = tk.Button(self, text="BUTTON", font=LARGE_FONT)
        BTN.pack(pady=50, padx=50)
        i = list([(i) for i in range(5)])
        y = 20
        x = 100
        for x in i:
            label2 = tk.Label(self, text=x, font=LARGE_FONT)
            label2.pack(pady=20, padx=100)
            y += 1

app = SeaofBTCapp()
app.mainloop()