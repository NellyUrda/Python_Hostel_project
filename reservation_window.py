from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox


class ReservationPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry('650x600')
        self.master.config(bg="#42b3f5")

        self.title_label = Label(master, text=" *****HOSTEL  SKY", fg="white", font=("Ariel", 14, 'bold'), bg="#42b3f5")
        self.title_label.place(x=150, y=30, width=250, height=50)

        self.res_label = Label(master, text="Reservation Details", fg="black", font=("Ariel", 12, 'bold'), bg="#42b3f5")
        self.res_label.place(x=15, y=80, width=200, height=50)

        self.client_id_label = Label(master, text="Client Id", fg="black", font=("Ariel", 10, 'bold'), bg="#42b3f5")
        self.client_id_label.place(x=15, y=120, width=100, height=20)

        self.client_id_entry = Entry(master)
        self.client_id_entry.place(x=30, y=145, width=500, height=20)

        self.client_name_label = Label(master, text="Client Name", fg="black", font=("Ariel", 10, 'bold'), bg="#42b3f5")
        self.client_name_label.place(x=20, y=170, width=100, height=20)

        self.client_name_entry = Entry(master)
        self.client_name_entry.place(x=30, y=190, width=500, height=20)

        self.client_adresse_label = Label(master, text="Client Adresse", fg="black", font=("Ariel", 10, 'bold'),
                                          bg="#42b3f5")
        self.client_adresse_label.place(x=30, y=210, width=100, height=20)

        self.client_adresse_entry = Entry(master)
        self.client_adresse_entry.place(x=30, y=230, width=500, height=20)

        self.roomtype_label = Label(master, text="Room Type", fg="black", font=("Ariel", 10, 'bold'),
                                    bg="#42b3f5")
        self.roomtype_label.place(x=25, y=250, width=100, height=20)

        rooms = ["single", "double", "double deluxe", "family"]
        self.combobox = ttk.Combobox(master, value=rooms)
        self.combobox.place(x=30, y=270, width=235, height=20)
        self.combobox.bind("<<ComboboxSelected>>", self.room_type)

        self.roomnr_label = Label(master, text="Room Nr", fg="black", font=("Ariel", 10, 'bold'),
                                  bg="#42b3f5")
        self.roomnr_label.place(x=290, y=250, width=80, height=20)

        self.roomnr_entry = Entry(master)
        self.roomnr_entry.place(x=290, y=270, width=115, height=20)

        self.room_price_label = Label(master, text="Room Price", fg="black", font=("Ariel", 10, 'bold'),
                                      bg="#42b3f5")
        self.room_price_label.place(x=420, y=250, width=80, height=20)

        self.room_price_entry = Entry(master)
        self.room_price_entry.place(x=415, y=270, width=115, height=20)

        self.checkin_label = Label(master, text="Check-in-date(yyyy-mm-dd)", fg="black", font=("Ariel", 10, 'bold'),
                                   bg="#42b3f5")
        self.checkin_label.place(x=35, y=290, width=170, height=20)

        self.checkin_entry = Entry(master)
        self.checkin_entry.place(x=30, y=310, width=235, height=20)

        self.checkout_label = Label(master, text="Check-out-date(yyyy-mm-dd)", fg="black", font=("Ariel", 10, 'bold'),
                                    bg="#42b3f5")
        self.checkout_label.place(x=265, y=290, width=235, height=20)

        self.checkout_entry = Entry(master)
        self.checkout_entry.place(x=295, y=310, width=235, height=20)

        self.nrnights_label = Label(master, text="Nr Nights", fg="black", font=("Ariel", 10, 'bold'),
                                    bg="#42b3f5")
        self.nrnights_label.place(x=25, y=330, width=100, height=20)

        self.nights_entry = Entry(master)
        self.nights_entry.place(x=30, y=350, width=235, height=20)

        self.roomav_button = Button(master, text="Check Room Availability", font=("Ariel", 10, "bold"),
                                    command=self.check_availability)
        self.roomav_button.place(x=30, y=390, width=235, height=30)

        self.price_button = Button(master, text="Total Price", font=("Ariel", 10, "bold"), command=self.price)
        self.price_button.place(x=30, y=430, width=235, height=30)

        self.book_button = Button(master, text="Book Room", font=("Ariel", 10, "bold"), command=self.book_room)
        self.book_button.place(x=300, y=430, width=235, height=30)

        self.all_reservations_button = Button(master, text="All Reservations", font=("Ariel", 10, "bold"),
                                              command=self.all_reservations)
        self.all_reservations_button.place(x=30, y=520, width=235, height=30)

        self.exit_button = Button(master, text="Close", font=("Ariel", 10, "bold"),
                                  bg="red", activebackground="red", command=exit)
        self.exit_button.place(x=30, y=560, width=100, height=30)

    # Combobox
    # when we select the room type , we take its number and price values from database
    # and put them in the entry boxes
    def room_type(self, event):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
        cursor = mydb.cursor()

        if self.combobox.get() == "single":
            query1 = "SELECT RoomNr FROM `rooms` WHERE RoomType ='single';"
            cursor.execute(query1)
            result1 = cursor.fetchone()
            self.roomnr_entry.delete(0, END)
            self.roomnr_entry.insert(0, result1)

            query2 = "SELECT RoomPrice from rooms where RoomType='single'"
            cursor.execute(query2)
            result2 = cursor.fetchone()
            self.room_price_entry.delete(0, END)
            self.room_price_entry.insert(0, result2)
        elif self.combobox.get() == "double":
            query1 = "SELECT RoomNr FROM `rooms` WHERE RoomType ='double';"
            cursor.execute(query1)
            result1 = cursor.fetchone()
            self.roomnr_entry.delete(0, END)
            self.roomnr_entry.insert(0, result1)

            query2 = "SELECT RoomPrice from rooms where RoomType='double'"
            cursor.execute(query2)
            result2 = cursor.fetchone()
            self.room_price_entry.delete(0, END)
            self.room_price_entry.insert(0, result2)
        elif self.combobox.get() == "double deluxe":
            query1 = "SELECT RoomNr FROM `rooms` WHERE RoomType ='double del';"
            cursor.execute(query1)
            result1 = cursor.fetchone()
            self.roomnr_entry.delete(0, END)
            self.roomnr_entry.insert(0, result1)

            query2 = "SELECT RoomPrice from rooms where RoomType='double del'"
            cursor.execute(query2)
            result2 = cursor.fetchone()
            self.room_price_entry.delete(0, END)
            self.room_price_entry.insert(0, result2)
        elif self.combobox.get() == "family":
            query1 = "SELECT RoomNr FROM `rooms` WHERE RoomType ='family';"
            cursor.execute(query1)
            result1 = cursor.fetchone()
            self.roomnr_entry.delete(0, END)
            self.roomnr_entry.insert(0, result1)

            query2 = "SELECT RoomPrice from rooms where RoomType='family'"
            cursor.execute(query2)
            result2 = cursor.fetchone()
            self.room_price_entry.delete(0, END)
            self.room_price_entry.insert(0, result2)

    # Check Room Availability button
    # opens room availability page were we check if a room is booked or not
    def check_availability(self):
        from room_availability_window import AvailabilityPage
        window = Tk()
        AvailabilityPage(window)

    # Total Price button
    # we calculate the total price for the client, nr of nights * room price
    def price(self):
        try:
            nr_nights = int(self.nights_entry.get())
            room_price = int(self.room_price_entry.get())
            total = nr_nights * room_price
            tkinter.messagebox.showinfo(message="Total to pay: " + str(total) + " euros ")
        except Exception:
            tkinter.messagebox.showinfo(message=" Choose the room type and then enter the number of nights ")

    # Book Room button
    # after all the fields are filled in, we book the room and save the changes in the database
    def book_room(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="hotel")
        cursor = mydb.cursor()

        client_id = self.client_id_entry.get()
        client_name = self.client_name_entry.get()
        client_address = self.client_adresse_entry.get()
        check_in = self.checkin_entry.get()
        check_out = self.checkout_entry.get()
        room_nr = self.roomnr_entry.get()

        if client_id == "" or client_name == "" or client_address == "" or check_in == "" or check_out == "" or room_nr == "":
            tkinter.messagebox.showinfo(message="You have to fill in all the fields")
        else:
            query = "INSERT INTO CLIENTS VALUES('" + client_id + "','" + client_name + "','" + client_address + "','" \
                    + room_nr + "','" + check_in + "','" + check_out + "')";
            cursor.execute(query)
            mydb.commit()  # to save the changes in the databases
            tkinter.messagebox.showinfo(message="Room successfully booked!!! ")

    # All Reservations button
    # opens the archive page with all the client's reservations
    def all_reservations(self):
        window = Tk()
        from all_reservations_window import ArchivePage
        ArchivePage(window)

