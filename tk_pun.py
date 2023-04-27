# import tkinter as tk
from tkinter import *
import requests

API_ENDPOINT1 = "http://127.0.0.1:8000/flight"
API_ENDPOINT2 = "http://127.0.0.1:8000/login"
API_ENDPOINT3 = "http://127.0.0.1:8000/flight_instance"
API_ENDPOINT4 = "http://127.0.0.1:8000/edit_flight_instance"
API_ENDPOINT5 = "http://127.0.0.1:8000/cancel_flight_instance"
API_ENDPOINT6 = "http://127.0.0.1:8000/change_seat"
API_ENDPOINT7 = "http://127.0.0.1:8000/add_promotion"

admin = {
        "Username":"",
        "Password":"",
        }


def flightbtn(data):
    print("on click")
    payload = {
        "Username":data["Username"],
        "Password":data["Password"],
        "Name": name.get(),
        "Flight Duration": duration.get(),
        "International":international.get(),
        "Depart Airport": depart.get(),
        "Arrive Airport": arrive.get()
    }
    response = requests.post(API_ENDPOINT1,json=payload)
    if response.ok:
        data = response.json()
        print(data)
    else:
        print("Error")

def flight_instancebtn(data):
    print("on click")
    payload = {
        "Username":data["Username"],
        "Password":data["Password"],
        "Depart Airport": depart_airport.get(),
        "Flight": flight.get(),
        "Date": date.get(),
        "Time Depart":time_depart.get(),
        "Time Arrive": time_arrive.get(),
        "Aircraft": aircraft.get(),
        "Price": price.get()
    }
    response = requests.post(API_ENDPOINT3,json=payload)
    if response.ok:
        data = response.json()
        print(data)
    else:
        print("Error")

def on_select():
    print(international.get())

def loginbtn():
    print("on click")
    payload = {
        "Username": username.get(),
        "Password": password.get()
        }
    response = requests.post(API_ENDPOINT2,json=payload)
    if response.ok:
        admin["Username"] = username.get()
        admin["Password"] = password.get()

        print(response.json())

def editbtn(data):
    print("on click")
    payload = {
        "Username":data["Username"],
        "Password":data["Password"],
        "Depart Airport": depfedit.get(),
        "Date": datefedit.get(),
        "Flight": flightfedit.get(),
        "Edit Date":edit_date.get(),
        "Edit Time Depart": edit_time_depart.get(),
        "Edit Time Arrive": edit_time_arrive.get(),
        "Edit Price": edit_price.get()
    }
    response = requests.put(API_ENDPOINT4,json=payload)
    if response.ok:
        data = response.json()
        print(data)
    else:
        print("Error")

def cancelbtn(data):
    print("on click")
    payload = {
        "Username":data["Username"],
        "Password":data["Password"],
        "Depart Airport": depfcancel.get(),
        "Date": datefcancel.get(),
        "Flight": flightfcancel.get(),
        "Seat":edit_date.get(),
    }
    response = requests.delete(API_ENDPOINT5,json=payload)
    if response.ok:
        data = response.json()
        print(data)
    else:
        print("Error")

def changeseatbtn(data):
    print("on click")
    payload = {
        "Username":data["Username"],
        "Password":data["Password"],
        "Booking ID": booking_id.get(),
        "Date": date_departfseat.get(),
        "Flight": flightfseat.get(),
        "Seat":seat.get(),
        "Change to:":edit_seat.get()
    }
    response = requests.put(API_ENDPOINT6,json=payload)
    if response.ok:
        data = response.json()
        print(data)
    else:
        print("Error")

def add_promotionbtn(data):
    print("on click")
    payload = {
        "Username":data["Username"],
        "Password":data["Password"],
        "Promotion Code":promotion_code.get(),
        "Discount":discount.get()
        }    
    response = requests.post(API_ENDPOINT7,json=payload)
    if response.ok:
        data = response.json()
        print(data)


root = Tk()

# create flight
name = StringVar()
duration = IntVar()
depart = StringVar()
arrive = StringVar()
international = BooleanVar()
#login
username = StringVar()
password = StringVar()
#create flight instance
flight = StringVar()
date = StringVar()
time_depart = StringVar()
time_arrive = StringVar()
aircraft = StringVar()
depart_airport = StringVar()
price = DoubleVar()
#edit flight instance
depfedit = StringVar()
datefedit = StringVar()
flightfedit = StringVar()
edit_date = StringVar()
edit_time_depart = StringVar()
edit_time_arrive = StringVar()
edit_price = DoubleVar()
#cancel flight instance
depfcancel = StringVar()
datefcancel = StringVar()
flightfcancel = StringVar()
#change seat
booking_id = StringVar()
depart_airportfseat = StringVar()
date_departfseat = StringVar()
flightfseat = StringVar()
seat = StringVar()
edit_seat = StringVar()
#add promotion
promotion_code = StringVar()
discount = IntVar()

#Login
Label(root, text = "Username: ").grid(row=0,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=username, width=12, justify="left").grid(row=0, column=1, padx=10)
Label(root, text = "Password: ").grid(row=1,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=password, width=12, justify="left").grid(row=1, column=1, padx=10)
Button(root, text=" LOGIN ", bg="green", command=loginbtn).grid(row=2, column=0, columnspan=2)

#Create Flight
Label(root, text = "Name: ").grid(row=3,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=name, width=12, justify="left").grid(row=3, column=1, padx=10)
Label(root, text = "Flight Duration").grid(row=4,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=duration, width=12, justify="left").grid(row=4, column=1, padx=10)
Label(root, text = "Depart Airport").grid(row=6,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=depart, width=12, justify="left").grid(row=6, column=1, padx=10)
Label(root, text = "Arrive Airport").grid(row=7,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=arrive, width=12, justify="left").grid(row=7, column=1, padx=10)
Button(root, text=" SUBMIT ", bg="green", command=lambda: flightbtn(admin)).grid(row=8, column=0, columnspan=2)

showIndicator = True
Label(root, text = "International").grid(row=5,column=0, padx=10, ipady=5, sticky='E')
Radiobutton(root,text="True",value=1,variable=international,indicatoron=showIndicator,command=on_select).grid(row=5, column=1, padx=10)
Radiobutton(root,text="False",value=0,variable=international,indicatoron=showIndicator,command=on_select).grid(row=5, column=2, padx=10)

#Create Flight Instance
Label(root, text = "Depart Airport").grid(row=9,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=depart_airport, width=12, justify="left").grid(row=9, column=1, padx=10)
Label(root, text = "Flight ").grid(row=10,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=flight, width=12, justify="left").grid(row=10, column=1, padx=10)
Label(root, text = "Date").grid(row=11,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=date, width=12, justify="left").grid(row=11, column=1, padx=10)
Label(root, text = "Time Depart").grid(row=12,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=time_depart, width=12, justify="left").grid(row=12, column=1, padx=10)
Label(root, text = "Time Arrive").grid(row=13,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=time_arrive, width=12, justify="left").grid(row=13, column=1, padx=10)
Label(root, text = "Aircraft").grid(row=14,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=aircraft, width=12, justify="left").grid(row=14, column=1, padx=10)
Label(root, text = "Price").grid(row=15,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=price, width=12, justify="left").grid(row=15, column=1, padx=10)
Button(root, text=" SUBMIT ", bg="green", command=lambda: flight_instancebtn(admin)).grid(row=16, column=0, columnspan=2)

#Edit Flight Instance
Label(root, text = "Depart Airport").grid(row=0,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=depfedit, width=12, justify="left").grid(row=0, column=4, padx=10)
Label(root, text = "Date ").grid(row=1,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=datefedit, width=12, justify="left").grid(row=1, column=4, padx=10)
Label(root, text = "Flight").grid(row=2,column=3, padx=18, ipady=5, sticky='E')
Entry(root, textvariable=flightfedit, width=12, justify="left").grid(row=2, column=4, padx=10)
Label(root, text = "Edit Date").grid(row=3,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=edit_date, width=12, justify="left").grid(row=3, column=4, padx=10)
Label(root, text = "Edit Time Depart").grid(row=4,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=edit_time_depart, width=12, justify="left").grid(row=4, column=4, padx=10)
Label(root, text = "Edit Time Arrive").grid(row=5,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=edit_time_arrive, width=12, justify="left").grid(row=5, column=4, padx=10)
Label(root, text = "Edit Price").grid(row=6,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=edit_price, width=12, justify="left").grid(row=6, column=4, padx=10)
Button(root, text=" EDIT ", bg="green", command=lambda: editbtn(admin)).grid(row=7, column=3, columnspan=2)

#Cancel Flight Instance
Label(root, text = "Depart Airport").grid(row=8,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=depfcancel, width=12, justify="left").grid(row=8, column=4, padx=10)
Label(root, text = "Date ").grid(row=9,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=datefcancel, width=12, justify="left").grid(row=9, column=4, padx=10)
Label(root, text = "Flight").grid(row=10,column=3, padx=18, ipady=5, sticky='E')
Entry(root, textvariable=flightfcancel, width=12, justify="left").grid(row=10, column=4, padx=10)
Button(root, text=" Cancel ", bg="green", command=lambda: cancelbtn(admin)).grid(row=11, column=3, columnspan=2)

#Change Seat
Label(root, text = "Booking ID").grid(row=12,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=depfedit, width=12, justify="left").grid(row=12, column=4, padx=10)
Label(root, text = "Depart Airport").grid(row=13,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=datefedit, width=12, justify="left").grid(row=13, column=4, padx=10)
Label(root, text = "Date").grid(row=14,column=3, padx=18, ipady=5, sticky='E')
Entry(root, textvariable=flightfedit, width=12, justify="left").grid(row=14, column=4, padx=10)
Label(root, text = "Flight").grid(row=15,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=edit_date, width=12, justify="left").grid(row=15, column=4, padx=10)
Label(root, text = "Seat").grid(row=16,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=edit_time_depart, width=12, justify="left").grid(row=16, column=4, padx=10)
Label(root, text = "Edit Seat").grid(row=17,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=edit_time_arrive, width=12, justify="left").grid(row=17, column=4, padx=10)
Button(root, text=" Submit ", bg="green", command=lambda: changeseatbtn(admin)).grid(row=18, column=3, columnspan=2)

#Add Promotion
Label(root, text = "Promotion Code").grid(row=19,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=depfedit, width=12, justify="left").grid(row=19, column=4, padx=10)
Label(root, text = "Discount").grid(row=20,column=3, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=datefedit, width=12, justify="left").grid(row=20, column=4, padx=10)
Button(root, text=" Submit ", bg="green", command=lambda: add_promotionbtn(admin)).grid(row=21, column=3, columnspan=2)

root.mainloop()