# import tkinter as tk
from tkinter import *
import requests

API_ENDPOINT1 = "http://127.0.0.1:8000/set_num_of_passenger"
API_ENDPOINT2 = "http://127.0.0.1:8000/passengers"

def on_click():
    payload = {
        "num_adult": num_adult.get(),
        "num_kid": num_kid.get(),
        "num_infant": num_infant.get()
    }
    response = requests.post(API_ENDPOINT1,json=payload)
    if response.ok:
        data = response.json()
        print(data)

def on_click1():
    payload = {
        "name": name.get(), 
        "last_name": last_name.get(),
        "date_of_birth": date_of_birth.get(),
        "phone_number": phon_number.get(),
        "email": email.get(),
        "national":national.get(),
        "country_residence":country_residence.get(),
        "passport_number":passport_number.get(),
        "issued_by":issued_by.get(),
        "passport_exp_date":passport_exp_date.get(),
        "parent":select_adult_list.get()
        }
    
    print(select_adult_list.get())
    # print(API_ENDPOINT2+'/'+select_passenger_type.get()+'/'+select_passenger_title.get())
    response = requests.post(API_ENDPOINT2+'/'+select_passenger_type.get()+'/'+select_passenger_title.get(),json=payload)
    if response.ok:
        data = response.json()
        print(data)
        name.set('')
        last_name.set('')
        date_of_birth.set('')
        phon_number.set('')
        email.set('')
        national.set('')
        country_residence.set('')
        passport_number.set('')
        issued_by.set('')
        passport_exp_date.set('')

def get_adult():
    response = requests.get("http://127.0.0.1:8000/passenger_adult_list")
    if response.ok:
        option_list = response.json()
        om2["menu"].delete(0, "end")
        for option in option_list:
            om2["menu"].add_command( label=option,command=lambda value=option: select_adult_list.set(value)) 

def get_title():
    response = requests.get("http://127.0.0.1:8000/passenger_title"+"/"+select_passenger_type.get())
    if response.ok:
        option_list = response.json()
        om1["menu"].delete(0, "end")
        for option in option_list:
            om1["menu"].add_command(label=option,command=lambda value=option: select_passenger_title.set(value)) 

root = Tk()
root.option_add("*Font", "impact 18")
num_adult = StringVar()
num_kid = StringVar()
num_infant = StringVar()
isinter = requests.get("http://127.0.0.1:8000/inter_status")

passenger_type = requests.get("http://127.0.0.1:8000/passenger_type")
select_passenger_type = StringVar()
select_adult_list = StringVar()

select_passenger_title = StringVar()
name = StringVar()
last_name = StringVar()
date_of_birth = StringVar()
phon_number = StringVar()
email = StringVar()
national = StringVar()
country_residence = StringVar()
passport_number = StringVar()
issued_by = StringVar()
passport_exp_date = StringVar()

Label(root, text=f'Nataional:{str(isinter.json())}').grid(row=0, column=5, padx=10, ipady=5, sticky='E')
#input num passenger
Label(root, text="Adult num :").grid(row=0, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=num_adult, width=12, justify="left").grid(row=0, column=1, padx=10)
Label(root, text="Kid num :").grid(row=1, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=num_kid, width=12, justify="left").grid(row=1, column=1, padx=10)
Label(root, text="Infant num :").grid(row=2, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=num_infant, width=12, justify="left").grid(row=2, column=1, padx=10)
Button(root, text=" SUBMIT ", bg="green", command=on_click).grid(row=5, column=0, columnspan=2)


Button(root, text=" search_parent ", bg="green", command=get_adult).grid(row=14, column=2, columnspan=2)
Label(root, text="Select type").grid(row=7, column=0, padx=10, ipady=5, sticky='E')
om = OptionMenu(root,select_passenger_type,*passenger_type.json())
om.config(width=10)
om.grid(row=7,column=1)

Button(root, text=" submit_type ", bg="green", command=get_title).grid(row=7, column=2, columnspan=2)
Label(root, text="Title :").grid(row=8, column=0,padx=10, ipady=5, sticky='E')
om1 = OptionMenu(root,select_passenger_title,'')
om1.config(width=10)
om1.grid(row=8,column=1)

Button(root, text=" search_parent ", bg="green", command=get_adult).grid(row=14, column=2, columnspan=2)
Label(root, text="Parent :").grid(row=14, column=0,padx=10, ipady=5, sticky='E')
om2 = OptionMenu(root,select_adult_list,'')
om2.config(width=10)
om2.grid(row=14,column=1)

Label(root, text="Name :").grid(row=9, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=name, width=12, justify="left").grid(row=9, column=1, padx=10)
Label(root, text="Last Name :").grid(row=10, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=last_name, width=12, justify="left").grid(row=10, column=1, padx=10)
Label(root, text="DATE  :").grid(row=11, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=date_of_birth, width=12, justify="left").grid(row=11, column=1, padx=10)
Label(root, text="Phone Number  :").grid(row=12, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=phon_number, width=12, justify="left").grid(row=12, column=1, padx=10)
Label(root, text="Email  :").grid(row=13, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=email, width=12, justify="left").grid(row=13, column=1, padx=10)

Label(root, text="Nationality :").grid(row=9, column=4,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=national, width=12, justify="left").grid(row=9, column=5, padx=10)
Label(root, text="Country ressidence :").grid(row=10, column=4,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=country_residence, width=12, justify="left").grid(row=10, column=5, padx=10)
Label(root, text="Passport number :").grid(row=11, column=4,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=passport_number, width=12, justify="left").grid(row=11, column=5, padx=10)
Label(root, text="Issued by :").grid(row=12, column=4,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=issued_by, width=12, justify="left").grid(row=12, column=5, padx=10)
Label(root, text="Passport exp date :").grid(row=13, column=4,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=passport_exp_date, width=12, justify="left").grid(row=13, column=5, padx=10)

Button(root, text=" NEXT ", bg="green", command=on_click1).grid(row=15, column=1, columnspan=2)

root.mainloop()
