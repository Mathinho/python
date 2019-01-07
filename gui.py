import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hallo Welt\n(einfach klicken)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.hi_there.config(height = "2", width = "100")

        self.quit = tk.Button(self, text="QUIT", fg="red", bg="yellow", command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.quit.config(height = "2", width = "100")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.master.title("Hallo Welt...")
app.master.geometry("640x480")
app.mainloop()