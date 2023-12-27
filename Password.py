from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3

class ChangePasswordFrame(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        style = Style()
        style.configure('TFrame', background = 'white')
        style.configure('TLabel', background = 'white',
                        font = 'Times 18 bold', foreground = 'grey')
        style.configure('TButton',width = 15,font = 'Times 14 bold',foreground = 'grey')

        self.place(relx = .5, rely = .3, anchor = CENTER)

        old_password_label = Label(self, text = "Old Password : ")
        old_password_label.grid(row = 0, column = 0, sticky = E)
        
        self.old_password_entry = Entry(self, width = 25, font = 'Times 15', foreground = 'grey')
        self.old_password_entry.grid(row = 0, column = 1, padx = 10, pady = 10,
                                     ipadx = 5, ipady = 5)
        
        new_password_label = Label(self, text = "New Password : ")
        new_password_label.grid(row = 1, column = 0, sticky = E)
        
        self.new_password_entry = Entry(self, width = 25, font = 'Times 15', foreground = 'grey')
        self.new_password_entry.grid(row = 1, column = 1, padx = 10, pady = 10,
                               ipadx = 5, ipady = 5)
        
        confirm_password_label = Label(self, text = "Confirm Password : ")
        confirm_password_label.grid(row = 2, column = 0, sticky = E)
        
        self.confirm_password_entry = Entry(self, width = 25, font = 'Times 15', foreground = 'grey')
        self.confirm_password_entry.grid(row = 2, column = 1, padx = 10, pady = 10,
                                   ipadx = 5, ipady = 5)

        change_Password_button = Button(self,text = "Change Password",style = 'TButton',
                                        width = 16, command = self.change_Password_click)
        change_Password_button.grid(row = 3, column = 1, padx = 10, pady = 10,
                                    ipadx = 5, ipady = 5)

    def change_Password_click(self):
        con = sqlite3.connect('The-Contact-Book//Contacts.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM LoginInfo WHERE Password = ?",
                    (self.old_password_entry.get(),)) # -> Here the 'Comma' tells that its a 'Tuple'
        record = cur.fetchone()                                  
        if record is not None:
            if self.new_password_entry.get() == self.confirm_password_entry.get():
                cur.execute("UPDATE LoginInfo SET Password = ? WHERE Password = ?",
                            (self.new_password_entry.get(),self.old_password_entry.get()))
                con.commit()
                messagebox.showinfo("Success Message","Password Is Changed Successfully")
            else:
                messagebox.showerror("Error Message","New & Confrim Passwords Didn't Matched")
        else:
            messagebox.showerror("Error Message", "Incorrect Old Password")