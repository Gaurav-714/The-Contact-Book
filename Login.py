from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3
import Home

class LoginWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Login")
        self.geometry("400x250")

        # For Interface Heading Frame... 
        style = Style()
        style.configure('Header.TFrame', background='grey')

        header_frame = Frame(self, style = 'Header.TFrame')
        header_frame.pack(fill = X)

        # For Interface Heading Label...
        style.configure('Header.TLabel', font='Times 30 bold',
                            background='grey', foreground='white')
        header_label = Label(header_frame, text="The  Contact  Book",
                              style = 'Header.TLabel')
        header_label.pack(pady = 15)

        # For Main Content...
        style.configure('Content.TFrame', background = 'grey')
        content_frame = Frame(self, style = 'Content.TFrame')
        content_frame.pack(fill = BOTH, expand = TRUE)

        # For Login Frame Inside Then Main Frame...
        login_frame = Frame(content_frame, style = 'Content.TFrame')
        login_frame.place(relx = .5, rely = .4, anchor = CENTER) 
        
        style.configure('Login.TLabel', font = 'Times 15 bold', background = 'grey', foreground = 'white')

        # For USERNAME Entry...
        username_label = Label(login_frame, text = "Username : ", style = 'Login.TLabel')
        username_label.grid(row = 0, column = 0)
        self.username_entry = Entry(login_frame, width = 25, font = 'Times 10', foreground = 'grey')
        self.username_entry.grid(row = 0, column = 1, pady = 10)
        
        # For PASSWORD Entry...
        password_label = Label(login_frame, text = "Password : ", style = 'Login.TLabel')
        password_label.grid(row = 1, column = 0)
        self.password_entry = Entry(login_frame, width = 25, show = "*", font = 'Times 10', foreground = 'grey')
        self.password_entry.grid(row = 1, column = 1, pady = 10)
            
        # For LOGIN BUTTON...
        style.configure('Login.TButton', foreground = 'grey', font = 'Times 12 bold', width = 10)
        login_button = Button(login_frame, text = "Login", style = 'Login.TButton',
                                command = self.login_button_click)
        login_button.grid(row = 2, column = 1, pady = 10)

        login_button.bind('<Return>', self.login_button_click) # Button will also work on pressing 'ENTER KEY'


    def login_button_click(self, event = None):
        con = sqlite3.connect('The-Contact-Book//Contacts.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM LoginInfo WHERE Username = ? AND Password = ?",
                    (self.username_entry.get(),self.password_entry.get()))
        row = cur.fetchone()
        if row is not None: # Will Execute When Username & Password Is Correct
            self.destroy() # To Close Login Window When The Login In Successfull
            Home.HomeWindow() # To Open Home Window When The Login In Successfull
        else: # Will Execute When Username & Password Is Incorrect
            messagebox.showinfo("Error Messsage","Incorrect Username or Password")



if __name__ == "__main__":
    
    lw = LoginWindow()
    lw.mainloop() # To Open Window 