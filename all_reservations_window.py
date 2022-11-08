import tkinter
from tkinter import *
from tkinter.ttk import Treeview
import mysql.connector
import tkinter.messagebox


class ArchivePage:

    def __init__(self, master):
        self.master = master
        self.master.geometry("1300x650")
        self.master.config(bg="#42b3f5")

        self.title_label = Label(master, text=" *****HOTEL SKY ", font=('Ariel', 14, "bold"), bg="#42b3f5",
                                 fg="white")
        self.title_label.place(x=450, y=30, width=250, height=50)

        self.button = Button(master, text="Search", font=("Ariel", 10, "bold"), command=self.search_client)
        self.button.place(x=20, y=90, width=200, height=30)

        self.entry = Entry(master)
        self.entry.place(x=260, y=90, width=200, height=30)
        self.entry.insert(0, "   by Client Id")

        label_f = LabelFrame(master, text="All Rooms Archives ")
        label_f.place(x=20, y=150, width=1250, height=450)

        self.treeview = Treeview(label_f, columns=(1, 2, 3, 4, 5, 6), show="headings")
        self.treeview.heading(1, text="Client Id")
        self.treeview.heading(2, text="Client Name")
        self.treeview.heading(3, text="Client Address")
        self.treeview.heading(4, text="Room Nr")
        self.treeview.heading(5, text="Check-in-date")
        self.treeview.heading(6, text="Check-out-date")
        self.treeview.place(x=20, y=0, width=1200, height=400)
        self.treeview.bind("<Double-1>", self.archive)

        self.scrollbar = Scrollbar(label_f, orient="vertical", command=self.treeview.yview)  # y axe
        self.scrollbar.pack(side=LEFT, fill="y")
        self.treeview.configure(yscrollcommand=self.scrollbar.set())

    # double-click the table
    # we get all the client's reservations from database and show the results in the treeview
    def archive(self, event):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
        cursor = mydb.cursor()

        query = "Select * from clients "
        cursor.execute(query)
        result = cursor.fetchall()

        for i in result:
            self.treeview.insert("", "end", values=i)

    # Search button
    # we search the reservations by client id
    # we get from database the reservation resulted and show it in to the treeview
    def search_client(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
        cursor = mydb.cursor()

        client_id = self.entry.get()
        if client_id == "   by Client Id":
            tkinter.messagebox.showinfo(message="Enter the Client's Id ")
        else:
            query = "Select * from clients where clientID= '" + client_id + "' order by checkIn";
            cursor.execute(query)
            result = cursor.fetchall()
            self.treeview.delete(*self.treeview.get_children())  # deletes all records af the table
        for i in result:
            self.treeview.insert("", "end", values=i)
