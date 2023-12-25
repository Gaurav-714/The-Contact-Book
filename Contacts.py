from tkinter import *
from tkinter.ttk import *

class ManageContactsFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        style = Style()
        style.configure('TFrame')
        style.configure('TLabel', font = 'Times 15 bold')
        style.configure('TButton', font = 'Times 15 bold')

        self.pack(fill = BOTH, expand = TRUE)

        contact_list_frame = Frame(self)
        contact_list_frame.place(relx = .5, rely = .5, anchor = CENTER)

        add_new_contact_button = Button(contact_list_frame, text = "Add New Contact")
        add_new_contact_button.grid(row = 0, column = 1)

        name_label = Label(contact_list_frame, text = "Name : ")
        name_label.grid(row = 1, column = 0)

        name_entry = Entry(contact_list_frame, font = 'Times 15', foreground = 'grey')
        name_entry.grid(row = 0, column = 1)