from tkinter import Tk, Label, Entry, Button

class Window:
    def __init__(self, master):
        self.master = master
        
        self.id_label = Label(master, text="id")
        self.id_entry = Entry(master)
        
        self.price_label = Label(master, text="price")
        self.price_entry = Entry(master)
        
        self.asd_label = Label(master, text="asd")
        self.asd_entry = Entry(master)
        
        self.uff_label = Label(master, text="uff")
        self.uff_entry = Entry(master)
        
        self.submit_button = Button(master, text="Submit")
        self.close_button = Button(master, text="Close", command=master.quit)
        self.__init_pos()
    def __init_pos(self):
        
        self.id_label.pack()
        self.id_entry.pack()
        
        self.price_label.pack()
        self.price_entry.pack()
        
        self.asd_label.pack()
        self.asd_entry.pack()
        
        self.uff_label.pack()
        self.uff_entry.pack()
        
        self.submit_button.pack()
        self.close_button.pack()

root = Tk()

window = Window(root)
root.mainloop()