from tkinter import Tk, Label, Entry, Button

class Window:
    def __init__(self, master):
        self.master = master
        
        self.id_label = Label(master, text="id")
        self.id_entry = Entry(master)
        
        self.name_pers_label = Label(master, text="name_pers")
        self.name_pers_entry = Entry(master)
        
        self.ages_all_label = Label(master, text="ages_all")
        self.ages_all_entry = Entry(master)
        
        self.hobby_label = Label(master, text="hobby")
        self.hobby_entry = Entry(master)
        
        self.heh_label = Label(master, text="heh")
        self.heh_entry = Entry(master)
        
        self.submit_button = Button(master, text="Submit")
        self.close_button = Button(master, text="Close", command=master.quit)
        self.__init_pos()
    def __init_pos(self):
        
        self.id_label.pack()
        self.id_entry.pack()
        
        self.name_pers_label.pack()
        self.name_pers_entry.pack()
        
        self.ages_all_label.pack()
        self.ages_all_entry.pack()
        
        self.hobby_label.pack()
        self.hobby_entry.pack()
        
        self.heh_label.pack()
        self.heh_entry.pack()
        
        self.submit_button.pack()
        self.close_button.pack()

root = Tk()

window = Window(root)
root.mainloop()