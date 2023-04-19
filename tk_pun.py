# import tkinter as tk
from tkinter import *
import requests

API_ENDPOINT1 = "http://127.0.0.1:8000/flight"
API_ENDPOINT2 = "http://127.0.0.1:8000/login"
API_ENDPOINT3 = "http://127.0.0.1:8000/flight_instance"

data = {
        "Username":"",
        "Password":""
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

def flight_instancebtn(data):
    print("on click")
    payload = {
        "Username":data["Username"],
        "Password":data["Password"],
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
        print("GG")
        data["Username"] = username.get()
        data["Password"] = password.get()

        print(response.json())

root = Tk()

name = StringVar()
duration = IntVar()
depart = StringVar()
arrive = StringVar()
international = BooleanVar()
username = StringVar()
password = StringVar()
flight = StringVar()
date = StringVar()
time_depart = StringVar()
time_arrive = StringVar()
aircraft = StringVar()
price = DoubleVar()

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
Button(root, text=" SUBMIT ", bg="green", command=lambda: flightbtn(data)).grid(row=8, column=0, columnspan=2)

showIndicator = True
Label(root, text = "International").grid(row=5,column=0, padx=10, ipady=5, sticky='E')
Radiobutton(root,text="True",value=1,variable=international,indicatoron=showIndicator,command=on_select).grid(row=5, column=1, padx=10)
Radiobutton(root,text="False",value=0,variable=international,indicatoron=showIndicator,command=on_select).grid(row=5, column=2, padx=10)

#Create Flight Instance
Label(root, text = "Flight ").grid(row=9,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=flight, width=12, justify="left").grid(row=9, column=1, padx=10)
Label(root, text = "Date").grid(row=10,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=date, width=12, justify="left").grid(row=10, column=1, padx=10)
Label(root, text = "Time Depart").grid(row=11,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=time_depart, width=12, justify="left").grid(row=11, column=1, padx=10)
Label(root, text = "Time Arrive").grid(row=12,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=time_arrive, width=12, justify="left").grid(row=12, column=1, padx=10)
Label(root, text = "Aircraft").grid(row=13,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=aircraft, width=12, justify="left").grid(row=13, column=1, padx=10)
Label(root, text = "Price").grid(row=14,column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=price, width=12, justify="left").grid(row=14, column=1, padx=10)
Button(root, text=" SUBMIT ", bg="green", command=lambda: flight_instancebtn(data)).grid(row=15, column=0, columnspan=2)

root.mainloop()