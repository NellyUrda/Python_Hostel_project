import tkinter.messagebox
from tkinter import *

autentification = {"jhon": '2345', "maria": '9876'}


class LoginPage:

    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.config(bg="#42b3f5")

        self.label = Label(master, text="WELCOME TO  *****HOSTEL  SKY ", font=("Ariel", 14, "bold"),
                           fg="white", bg="#42b3f5")
        self.label.place(x=120, y=50, width=310, height=70)

        self.login_label = Label(master, text="Login ", font=("Ariel", 13, "bold"),
                                 fg="Black", bg="#42b3f5")
        self.login_label.place(x=140, y=120, width=250, height=50)

        self.user_label = Label(master, text="Enter User Account", font=("Ariel", 10, "bold"),
                                fg="black", bg="#42b3f5")
        self.user_label.place(x=120, y=160, width=150, height=50)

        self.user_entry = Entry(master)
        self.user_entry.place(x=135, y=200, width=200, height=30)

        self.passwd_label = Label(master, text="Enter Password", font=("Ariel", 10, "bold"),
                                  fg="black", bg="#42b3f5")
        self.passwd_label.place(x=117, y=230, width=150, height=30)

        self.passwd_entry = Entry(master, show="*")
        self.passwd_entry.place(x=135, y=260, width=200, height=30)

        self.button = Button(master, text="Login", font=("Ariel", 10, "bold"), command=self.login)
        self.button.place(x=135, y=300, width=200, height=25)

    # Login button
    # verify if user and password match with pair key/value from dictionary
    def login(self):
        user_account = self.user_entry.get()
        password = self.passwd_entry.get()

        if user_account in autentification:
            if password == autentification[user_account]:
                self.master.withdraw()
                window = Tk()
                from reservation_window import ReservationPage
                ReservationPage(window)
            else:
                tkinter.messagebox.showinfo(message="Wrong Password")
        else:
            tkinter.messagebox.showinfo(message="Wrong Password or User Account")
