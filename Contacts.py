from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import *

class ManageContactsFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        style = Style()
        style.configure('TFrame')
        style.configure('TLabel', font = 'Times 16 bold', foreground = 'grey')
        style.configure('TButton', font = 'Times 16 bold', foreground = 'grey')

        style.configure('Treeview.Heading', font = 'Times 16 bold', foreground = 'grey')
        style.configure('Treeview', font = 'Times 13 bold', rowheight = 30, foreground = 'grey')
        
        self.pack(fill = BOTH, expand = TRUE)
        
        self.con = connect('The-Contact-Book//Contacts.db')
        self.cur = self.con.cursor()

        self.create_all_contacts_frame()


    def create_all_contacts_frame(self):

        self.contact_list_frame = Frame(self)
        self.contact_list_frame.place(relx = .5, rely = .45, anchor = CENTER)

        add_new_contact_button = Button(self.contact_list_frame, text = "+ Add New Contact",
                                        command = self.add_new_contact_button_click)
        add_new_contact_button.grid(row = 0, column = 1, pady = 10, sticky = E)

        name_label = Label(self.contact_list_frame, text = "Name :")
        name_label.grid(row = 1, column = 0)

        name_entry = Entry(self.contact_list_frame, font = 'Times 15', foreground = 'grey', width = 68)
        name_entry.grid(row = 1, column = 1, pady = 5)


        contacts_treeview = Treeview(self.contact_list_frame, show = 'headings',
                                     columns = ('name','phone_no','email_id','city'),)
        
        contacts_treeview.heading('name', text = "Name", anchor = W)
        contacts_treeview.heading('phone_no', text = "Phone Number", anchor = W)
        contacts_treeview.heading('email_id', text = "Email Id", anchor = W)
        contacts_treeview.heading('city', text = "City", anchor = W)

        contacts_treeview.column('name', width = 180)
        contacts_treeview.column('phone_no', width = 170)
        contacts_treeview.column('email_id', width = 250)
        contacts_treeview.column('city', width = 150)

        # For Displaying The Contacts From Table To Window...
        self.cur.execute("SELECT * FROM Contacts")
        records = self.cur.fetchall()
        for val in records:
            contacts_treeview.insert("", END, values = val)
            # 'END' -> Initial value will be '0' and it will Increase with every Iteration

        contacts_treeview.grid(row = 2, column = 0, columnspan = 2, pady = 10)


    def add_new_contact_button_click(self):
        self.contact_list_frame.destroy()

        self.add_new_contact_frame = Frame()
        self.add_new_contact_frame.place(relx = .5, rely = .5, anchor = CENTER)

        name_label = Label(self.add_new_contact_frame, text = "Name : ", style = 'TLabel')
        name_label.grid(row = 0, column = 0, sticky = E)

        self.name_entry = Entry(self.add_new_contact_frame)
        self.name_entry.grid(row = 0, column = 1)

        phone_no_label = Label(self.add_new_contact_frame, text = "Phone No.: ", style = 'TLabel')
        phone_no_label.grid(row = 1, column = 0, sticky = E)

        self.phone_no_entry = Entry(self.add_new_contact_frame)
        self.phone_no_entry.grid(row = 1, column = 1)

        email_label = Label(self.add_new_contact_frame, text = "Email Id : ", style = 'TLabel')
        email_label.grid(row = 2, column = 0, sticky = E)
        
        self.email_entry = Entry(self.add_new_contact_frame)
        self.email_entry.grid(row = 2, column = 1)
        
        city_label = Label(self.add_new_contact_frame, text = "City : ", style = 'TLabel')
        city_label.grid(row = 3, column = 0, sticky = E)

        self.city_entry = Entry(self.add_new_contact_frame) # Instead of 'Entry' we can use 'Combobox' (Dropdown Menu)
        self.city_entry.grid(row = 3, column = 1)           

        save_button = Button(self.add_new_contact_frame, text = "Save", style = 'TButton',
                             command = self.save_button_click)
        save_button.grid(row = 4, column = 1)


    def save_button_click(self):

        self.cur.execute("SELECT * FROM Contacts WHERE Phone_Number = ? OR Email_Id = ?", 
                         (self.phone_no_entry.get(),self.email_entry.get()))       
        
        record = self.cur.fetchone()
        if record is None:
            self.cur.execute("INSERT INTO Contacts (Name,Phone_Number,Email_Id,City) VALUES(?,?,?,?)",
                             (self.name_entry.get(),self.phone_no_entry.get(),self.email_entry.get(),self.city_entry.get()))
            self.con.commit()
            messagebox.showinfo("Success Message","Contact Details Added Successfully")
            
            self.add_new_contact_frame.destroy()
            self.create_all_contacts_frame() # To Go Back To The Home Page

        else:
            messagebox.showerror("Error Message","Contact Details Already Exist")
        

        

