from tkinter import Tk, Label, Entry, Button

class Window:
    def __init__(self, master):
        self.master = master
        self.label = Label(master, text="Unesi ime")
        self.entry = Entry(master)
        self.add_button = Button(master, text="Ok", command=self.click_ok)
        self.close_button = Button(master, text="Close", command=master.quit)
        self.__init_pos()
    def __init_pos(self):
        row, column = 0, 0
        self.label.grid(row=0, column=0)
        self.entry.grid(row=1, column=0)
        self.add_button.grid(row=2, column=0)
        self.close_button.grid(row=3, column=0)
    def click_ok(self):
        pass
root = Tk()

window = Window(root)
root.mainloop()
