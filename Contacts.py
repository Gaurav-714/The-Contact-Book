from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import *

class ManageContactsFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        style = Style()
        style.configure('TFrame')
        style.configure('TLabel', font = 'Times 18 bold', foreground = 'grey')
        style.configure('TButton', font = 'Times 16 bold', foreground = 'grey', width = 17)

        style.configure('Treeview.Heading', font = 'Times 16 bold', foreground = 'grey')
        style.configure('Treeview', font = 'Times 13 bold', rowheight = 30, foreground = 'grey')
        
        self.pack(fill = BOTH, expand = TRUE)
        
        self.con = connect('The-Contact-Book//Contacts.db')
        self.cur = self.con.cursor()

        self.create_all_contacts_frame()


    def fill_contacts_treeview(self):
        for row in self.contacts_treeview.get_children(): # 'get_children' -> Returns Collection of Rows
            self.contacts_treeview.delete(row)

        records = self.cur.fetchall()
        for val in records:
            self.contacts_treeview.insert("", END, values = val)
            # 'END' -> Initial value will be '0' and it will Increase with every Iteration


    def create_all_contacts_frame(self):

        self.contact_list_frame = Frame(self)
        self.contact_list_frame.place(relx = .5, rely = .45, anchor = CENTER)

        add_new_contact_button = Button(self.contact_list_frame, text = "+ Add New Contact",
                                        command = self.add_new_contact_button_click)
        add_new_contact_button.grid(row = 0, column = 1, pady = 10, ipady = 5, sticky = E)

        name_label = Label(self.contact_list_frame, text = "Name :")
        name_label.grid(row = 1, column = 0)

        self.name_entry = Entry(self.contact_list_frame, font = 'Times 13', foreground = 'grey', width = 79)
        self.name_entry.grid(row = 1, column = 1, pady = 5, ipady = 3)
        self.name_entry.bind('<KeyRelease>', self.name_entry_key_release) # '< Non-Virtual Event >'

        self.contacts_treeview = Treeview(self.contact_list_frame, show = 'headings',
                                     columns = ('name','phone_no','email_id','city'),)
        
        self.contacts_treeview.heading('name', text = "Name", anchor = W)
        self.contacts_treeview.heading('phone_no', text = "Phone Number", anchor = W)
        self.contacts_treeview.heading('email_id', text = "Email Id", anchor = W)
        self.contacts_treeview.heading('city', text = "City", anchor = W)

        self.contacts_treeview.column('name', width = 200)
        self.contacts_treeview.column('phone_no', width = 170)
        self.contacts_treeview.column('email_id', width = 270)
        self.contacts_treeview.column('city', width = 150)

        # For Displaying The Contacts From Table To Window...
        self.cur.execute("SELECT * FROM Contacts")
        self.fill_contacts_treeview()
        
        self.contacts_treeview.grid(row = 2, column = 0, columnspan = 2, pady = 10)
        self.contacts_treeview.bind('<<TreeviewSelect>>',self.treeview_row_selection) # '<< Virtual Event >>'


    def add_new_contact_button_click(self):
        self.contact_list_frame.destroy()

        self.add_new_contact_frame = Frame()
        self.add_new_contact_frame.place(relx = .5, rely = .5, anchor = CENTER)

        name_label = Label(self.add_new_contact_frame, text = "Name : ", style = 'TLabel')
        name_label.grid(row = 0, column = 0, sticky = E)

        self.name_entry = Entry(self.add_new_contact_frame, font = 'Times 15', foreground = 'grey', width = 25)
        self.name_entry.grid(row = 0, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)

        phone_no_label = Label(self.add_new_contact_frame, text = "Phone No.: ", style = 'TLabel')
        phone_no_label.grid(row = 1, column = 0, sticky = E)

        self.phone_no_entry = Entry(self.add_new_contact_frame, font = 'Times 15', foreground = 'grey', width = 25)
        self.phone_no_entry.grid(row = 1, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)

        email_label = Label(self.add_new_contact_frame, text = "Email Id : ", style = 'TLabel')
        email_label.grid(row = 2, column = 0, sticky = E)
        
        self.email_entry = Entry(self.add_new_contact_frame, font = 'Times 15', foreground = 'grey', width = 25)
        self.email_entry.grid(row = 2, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        
        city_label = Label(self.add_new_contact_frame, text = "City : ", style = 'TLabel')
        city_label.grid(row = 3, column = 0, sticky = E)

        self.city_entry = Entry(self.add_new_contact_frame, font = 'Times 15', foreground = 'grey', width = 25)
        self.city_entry.grid(row = 3, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)  
        # Instead of 'Entry' we can use 'Combobox' (Dropdown Menu)
         

        save_button = Button(self.add_new_contact_frame, text = "Save", style = 'TButton',
                             command = self.save_button_click)
        save_button.grid(row = 4, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)


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
    

    def name_entry_key_release(self, event):

        self.cur.execute("SELECT * FROM Contacts WHERE Name LIKE ?",
                         ('%' + self.name_entry.get() + '%',))
        self.fill_contacts_treeview()
        
    def treeview_row_selection(self, event):

        record = self.contacts_treeview.item(self.contacts_treeview.selection())['values']
        # 'item' -> 'row' && 'selection' -> Brings Index Of Selected Row
        self.contact_list_frame.destroy()

        self.update_delete_contact_frame = Frame()
        self.update_delete_contact_frame.place(relx = .5, rely = .5, anchor = CENTER)

        name_label = Label(self.update_delete_contact_frame, text = "Name : ", style = 'TLabel')
        name_label.grid(row = 0, column = 0, sticky = E)

        self.name_entry = Entry(self.update_delete_contact_frame, font = 'Times 15', foreground = 'grey', width = 25)
        self.name_entry.grid(row = 0, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.name_entry.insert(END, record[0])
        self.old_name_entry = record[0] # To Save A Reference In Case User Wants To Change The 'Name' Also

        phone_no_label = Label(self.update_delete_contact_frame, text = "Phone No.: " ,style = 'TLabel')
        phone_no_label.grid(row = 1, column = 0, sticky = E)

        self.phone_no_entry = Entry(self.update_delete_contact_frame, font = 'Times 15', foreground = 'grey', width = 25)
        self.phone_no_entry.grid(row = 1, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.phone_no_entry.insert(END, record[1])

        email_label = Label(self.update_delete_contact_frame, text = "Email Id : ", style = 'TLabel')
        email_label.grid(row = 2, column = 0, sticky = E)

        self.email_entry = Entry(self.update_delete_contact_frame, font = 'Times 15', foreground = 'grey', width = 25)
        self.email_entry.grid(row = 2, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.email_entry.insert(END, record[2])

        city_label = Label(self.update_delete_contact_frame, text = "City : ", style = 'TLabel')
        city_label.grid(row = 3, column = 0, sticky = E)

        self.city_entry = Entry(self.update_delete_contact_frame, font = 'Times 15', foreground = 'grey', width = 25)
        self.city_entry.grid(row = 3, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.city_entry.insert(END, record[3])
        
        update_button = Button(self.update_delete_contact_frame, text = "Update", style = 'TButton',
                               command = self.update_button_click)
        update_button.grid(row = 4, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)

        delete_button = Button(self.update_delete_contact_frame, text = "Delete", style = 'TButton',
                               command = self.delete_button_click)
        delete_button.grid(row = 5, column = 1, padx = 10, pady = 10, ipadx = 5, ipady = 5)


    def update_button_click(self):

        self.cur.execute("UPDATE Contacts SET Name = ?, Phone_number = ?, Email_Id = ?, City = ? WHERE Name = ?",
                         (self.name_entry.get(), self.phone_no_entry.get(), self.email_entry.get(),self.city_entry.get(),
                          self.old_name_entry)) # 'Old_Name' -> To Check By Reference In Case User Wants To Change The 'Name' Also
        self.con.commit()
        messagebox.showinfo("Success Message","Contact Details Are Updated Successfully.")
        self.update_delete_contact_frame.destroy()
        self.create_all_contacts_frame()

    
    def delete_button_click(self):

        decision = messagebox.askquestion("Confirmation Message","Are You Sure !!\nYou Want To Delete This Record !!")
        if decision == 'yes':
            self.cur.execute("DELETE FROM Contacts WHERE Email_Id = ?",(self.name_entry.get(),))
            self.con.commit()
            messagebox.showinfo("Success Message","Contact Details Are Deleted Successfully.")
            self.update_delete_contact_frame.destroy()
            self.create_all_contacts_frame()

        self.update_delete_contact_frame.destroy()
        self.create_all_contacts_frame()

        
        
        