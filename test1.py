from tkinter import *
from tkinter.ttk import *
root = Tk()
root.geometry('200x100')
class Application(Frame):
    def say_hi(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        self = Button(root, text='Quit', fg= "red", command=self.quit).pack({"side": "left"})
        self.QUIT = Button(self)

"""        self.QUIT["text"] = "Quit"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.QUIT["parent"] = "root"
        self.hi_there["text"] = "Hello",
        self.hi_there["fg"] = "blue"
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})
"""
def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()