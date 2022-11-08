import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Treeview
import mysql.connector


class AvailabilityPage:

    def __init__(self, master):
        self.master = master
        self.master.geometry("700x650")
        self.master.config(bg="#42b3f5")

        self.title_label = Label(master, text="HOTEL SKY", font=("Ariel", 14, "bold"), fg="white", bg="#42b3f5")
        self.title_label.place(x=150, y=30, width=250, height=50)

        self.subtl_label = Label(master, text="Room Availability", font=("Ariel", 12, "bold"), fg="black", bg="#42b3f5")
        self.subtl_label.place(x=20, y=70, width=150, height=50)

        self.roomNr_label = Label(master, text="Room Nr", font=("Ariel", 10, "bold"), fg="black", bg="#42b3f5")
        self.roomNr_label.place(x=10, y=100, width=100, height=50)

        self.roomNr_entry = Entry(master)
        self.roomNr_entry.place(x=30, y=140, width=550, height=20)

        self.checkIn_label = Label(master, text="Check-in-date(yyyy-mm-dd)", font=("Ariel", 10, "bold"), fg="black",
                                   bg="#42b3f5")
        self.checkIn_label.place(x=30, y=160, width=180, height=20)

        self.checkIn_entry = Entry(master)
        self.checkIn_entry.place(x=30, y=180, width=550, height=20)

        self.checkRoom_Button = Button(master, text="Check Room", font=('Ariel', 10, "bold"), command=self.room_details)
        self.checkRoom_Button.place(x=30, y=210, width=275, height=30)

        label_f = LabelFrame(master, text="Room Details")
        label_f.place(x=30, y=260, width=600, height=300)

        self.treeview = Treeview(label_f, columns=(1, 2, 3), show="headings")  # acts like a table
        self.treeview.heading(1, text="Room Nr")
        self.treeview.heading(2, text="Check-in-date")
        self.treeview.heading(3, text="Check-out-date")
        self.treeview.pack()

    # Check Room button
    # we check in the database if the room is booked or not in the specified date
    # show the results in the treeview
    def room_details(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
        cursor = mydb.cursor()

        room_nr = self.roomNr_entry.get()
        check_in_date = self.checkIn_entry.get()
        if room_nr == "" or check_in_date == "":
            tkinter.messagebox.showinfo(message="Please enter the room number and check-in-date")
        else:
            query = "SELECT roomNr, checkIn,checkOut from clients where roomNr='" + room_nr + "' and checkIn>='" + \
                    check_in_date + "' or roomNr='" + room_nr + "' and checkOut>'" + check_in_date + \
                    "' order by checkIn";
            cursor.execute(query)
            result = cursor.fetchall()
            self.treeview.delete(*self.treeview.get_children())

            for i in result:
                self.treeview.insert("", "end", values=i)
