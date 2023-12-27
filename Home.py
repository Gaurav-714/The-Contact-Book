from tkinter import *
from tkinter.ttk import *
import Login
import Password
import Contacts

class HomeWindow(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Home")
        self.state("zoom") # Window will occupy Full Screen

        style = Style()
        style.configure('Header.TFrame', background = 'grey')

        header_frame = Frame(self, style = 'Header.TFrame')
        header_frame.pack(fill = X)

        style.configure('Header.TLabel', font  = 'Times 50 bold',
                        background = 'grey', foreground = 'white')
        header_label = Label(header_frame, text = "The Contact Book",
                             style = 'Header.TLabel')
        header_label.pack(pady = 20)

        navigation_frame = Frame(self, style = 'Header.TFrame')
        navigation_frame.pack(side = LEFT, fill = Y) # Aligned To Left Side

        style.configure('Sidebar.TButton', background = 'grey', font = 'Times 16 bold',
                         width = 16, foreground = 'grey')

        manage_contacts_button = Button(navigation_frame, text = "Manage Contacts", style = 'Sidebar.TButton',
                                        command = self.manage_contacts_button_click)
        manage_contacts_button.pack(padx = 10, ipadx = 10, ipady = 10)

        change_Password_button = Button(navigation_frame, text  = "Change Password", style = 'Sidebar.TButton',
                                        command = self.change_password_button_click)
        change_Password_button.pack(padx = 10, pady = 10, ipadx = 10, ipady = 10)

        logout_button = Button(navigation_frame, text = "Logout",
                               style = 'Sidebar.TButton', command = self.logout_button_click)
        logout_button.pack(padx = 10, ipadx = 10, ipady = 10)

        style.configure('Navigation.TFrame', background = 'white')

        self.content_frame = Frame(self, style = 'Navigation.TFrame')
        self.content_frame.pack(fill = BOTH, expand = TRUE)
        
        Contacts.ManageContactsFrame(self.content_frame)


    def logout_button_click(self):
        self.destroy()
        Login.LoginWindow()


    def change_password_button_click(self): # In The Sidebar

        for inner_frame in self.content_frame.winfo_children():
        # Destroy all Frames inside the content_Frame one by one..
            inner_frame.destroy()

        Password.ChangePasswordFrame(self.content_frame)


    def manage_contacts_button_click(self):

        for inner_frame in self.content_frame.winfo_children(): # Get Collection of Frames inside 'content_frame'
        # Destroy all Frames inside the 'content_frame' one by one..
            inner_frame.destroy()

        Contacts.ManageContactsFrame(self.content_frame)