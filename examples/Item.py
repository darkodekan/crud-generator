from tkinter import Tk, Label, Entry, Button

class Window:
    def __init__(self, master):
        self.master = master
        
        self.id_label = Label(master, text="id")
        self.id_entry = Entry(master)
        
        self.name_label = Label(master, text="name")
        self.name_entry = Entry(master)
        
        self.price_label = Label(master, text="price")
        self.price_entry = Entry(master)
        
        self.customer_id_label = Label(master, text="customer_id")
        self.customer_id_entry = Entry(master)
        
        self.asd_label = Label(master, text="asd")
        self.asd_entry = Entry(master)
        
        self.submit_button = Button(master, text="Submit")
        self.close_button = Button(master, text="Close", command=master.quit)
        self.__init_pos()
    def __init_pos(self):
        
        self.id_label.pack()
        self.id_entry.pack()
        
        self.name_label.pack()
        self.name_entry.pack()
        
        self.price_label.pack()
        self.price_entry.pack()
        
        self.customer_id_label.pack()
        self.customer_id_entry.pack()
        
        self.asd_label.pack()
        self.asd_entry.pack()
        
        self.submit_button.pack()
        self.close_button.pack()

root = Tk()

window = Window(root)
root.mainloop()