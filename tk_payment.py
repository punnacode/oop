# import tkinter as tk
from tkinter import *
import requests

def select_promotion():
    response = requests.get("http://127.0.0.1:8000/sum_price/"+select_promotion_code.get())
    if response.ok:
        data = response.json()
        Label(root, text=f'Total Price : {data}').grid(row=3, column=0, padx=10, ipady=5, sticky='W')

def show_detail():
    response = requests.get("http://127.0.0.1:8000/show_promotion_detail/"+select_promotion_code.get())
    if response.ok:
        data = response.json()
        Label(root, text=f'detail->{data}').grid(row=0, column=3, padx=10, ipady=5, sticky='E')
        
def submit():
    payload = {
        "payment_type":select_payment_type.get()
    }
    response = requests.post("http://127.0.0.1:8000/select_payment_type",json=payload)
    if response.ok:
        data = response.json()
        Label(root, text=f'{data}          ').grid(row=6, column=0, padx=10, ipady=5, sticky='W')
    
root = Tk()
root.option_add("*Font", "impact 18")
payment_type = requests.get("http://127.0.0.1:8000/get_payment_type")
select_payment_type = StringVar()
promotion = requests.get("http://127.0.0.1:8000/get_promotion_code")
select_promotion_code  = StringVar()
total_price = requests.get("http://127.0.0.1:8000/sum_price")

Label(root, text="Payment").grid(row=0, column=0, padx=10, ipady=5, sticky='W')

Label(root, text="Select Payment Type").grid(row=1, column=0, padx=10, ipady=5, sticky='W')
om1 = OptionMenu(root,select_payment_type,*payment_type.json())
om1.config(width=10)
om1.grid(row=1,column=1)

Button(root, text=" detail ", bg="green", command=show_detail).grid(row=2, column=2)
Button(root, text=" submit_promotion ", bg="green", command=select_promotion).grid(row=2, column=3)
Label(root, text="Select Promotion Code").grid(row=2, column=0, padx=10, ipady=5, sticky='W')
om2 = OptionMenu(root,select_promotion_code,*promotion.json())
om2.config(width=10)
om2.grid(row=2,column=1)

Button(root, text=" Submit ", bg="green", command=submit).grid(row=5, column=1)

root.mainloop()
