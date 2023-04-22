from tkinter import *
from tkinter import messagebox
import requests

API_1 = "http://127.0.0.1:8000/select_seat/"
API_2 = "http://127.0.0.1:8000/select_add_on"
API_ENDPOINT1 = "http://127.0.0.1:8000/creat_ticket/"


data=   {
            "Origin airport":"AirportA",
            "Destination airport":"AirportB",
            "Date depart":"2023-05-18",
            "Flight name":"DD405",
            "Package name":"Max",
            "num_adult": 2,
            "num_kid": 1
        }



def on_click(data):
    print("on click")
    payload = {
        "Origin airport":data['Origin airport'],
        "Destination airport":data['Destination airport'],
        "Date depart":data['Date depart'],
        "select_seat": select_seat.get(),
        "FastTrack": FastTrack.get(),
        "Insurance": Insurance.get(),
        "Lounge": Lounge.get(),
        "Deaf": Deaf.get(),
        "Blind": Blind.get(),
        "Nun": Nun.get(),
        "Monk": Monk.get(),
        "Wheelchair": Wheelchair.get(),
        "Alone_kid": Alone_kid.get(),
        "baggage": baggage.get(),
        "meal": meal.get(),
        "meal_amount" : meal_amount.get(),
        "Special_baggage": Special_baggage.get()
    }
    
    response = requests.post(str(API_ENDPOINT1+data["Flight name"]),json=payload)
    if response.ok:
        global count
        global kidcount
        global name
        global button
        print(response.json())
        select_seat.set("") 
        FastTrack.set("")
        Insurance.set("") 
        Lounge.set("") 
        Monk.set("") 
        Blind.set("") 
        Deaf.set("") 
        Nun.set("") 
        Wheelchair.set("") 
        Alone_kid.set("") 
        baggage.set("") 
        meal.set("") 
        Special_baggage.set("") 
        if count+1 < int(data["num_adult"]):
            count+=1
            name.config(text= "Adult :" + str(count))

        elif count+1 == data['num_adult']:
                count+=1
                name.config(text= "Adult :" + str(count))
                if data['num_kid'] == 0:
                     button.config(text=" Confirm ", command= lambda: finish(data))
                #     Button(root, text=" Confirm ", command= finish(data)).grid(row=11, column=2, columnspan=2)

        elif count == data['num_adult'] and kidcount+1 < data['num_kid']:
                kidcount += 1
                name.config(text= "Kid :" + str(kidcount))
        
        elif count == data['num_adult'] and kidcount+1 == data['num_kid']:
                kidcount += 1
                name.config(text= "Kid :" + str(kidcount))
                button.config(text=" Confirm ", command= lambda:finish(data))
                

            
                


def finish(data):
    payload = {
        "Origin airport":data['Origin airport'],
        "Destination airport":data['Destination airport'],
        "Date depart":data['Date depart'],
        "select_seat": select_seat.get(),
        "FastTrack": FastTrack.get(),
        "Insurance": Insurance.get(),
        "Lounge": Lounge.get(),
        "Deaf": Deaf.get(),
        "Blind": Blind.get(),
        "Nun": Nun.get(),
        "Monk": Monk.get(),
        "Wheelchair": Wheelchair.get(),
        "Alone_kid": Alone_kid.get(),
        "baggage": baggage.get(),
        "meal": meal.get(),
        "meal_amount" : meal_amount.get(),
        "Special_baggage": Special_baggage.get()
    }
    response = requests.post(str(API_ENDPOINT1+data["Flight name"]),json=payload)
    if response.ok:
        print('finish')
        messagebox.showinfo("showinfo", "finish")
        


root = Tk()


seat = requests.post(str(API_1+data["Flight name"]),json=data)
add_on = requests.post(str(API_2),json=data)
seat_string = []
for i in seat.json()['Seat']:
    st = str(str(i[0])+" "+str(i[1])+" "+str(i[2]))
    seat_string.append(st)




select_seat = StringVar()
FastTrack = StringVar()
Insurance = StringVar()
Lounge = StringVar()
Monk = StringVar()
Blind = StringVar()
Deaf = StringVar()
Nun = StringVar()
Wheelchair = StringVar()
Alone_kid = StringVar()
baggage = IntVar()
meal = StringVar()
meal_amount = IntVar()
Special_baggage = StringVar()

number = [1,2,3,4,5,6,7,8,9]
baggage_size = [7,15,20,25,30]
special_baggage_list = ['No selection','Bicycle',20 ,25 ,30 ]
showIndicator = True
global count
count = 1
global kidcount
kidcount = 0

name = Label(root, text="Adult :" + str(count))
name.grid(row=0, column=0, padx=10, ipady=5, sticky='E')
    
Label(root, text="Select seat").grid(row=1, column=0, padx=10, ipady=5, sticky='E')
om = OptionMenu(root,select_seat,*seat_string)
om.config(width=15)
om.grid(row=1,column=1)

Label(root, text="Select add on").grid(row=2, column=0, padx=10, ipady=5, sticky='E')
Label(root, text="Extra service").grid(row=3, column=0, padx=10, ipady=5, sticky='E')

Label(root, text=str(add_on.json()["extra service"][0])).grid(row=4, column=0, padx=10, ipady=5, sticky='E')
Radiobutton(root, text="on",value=True,variable=FastTrack,indicatoron=showIndicator).grid(row=4, column=1, padx=10, ipady=5)
Radiobutton(root, text="off",value=False,variable=FastTrack,indicatoron=showIndicator).grid(row=4, column=2, padx=10, ipady=5)

Label(root, text=str(add_on.json()["extra service"][1])).grid(row=4, column=3, padx=10, ipady=5, sticky='E')
Radiobutton(root, text="on",value=True,variable=Insurance,indicatoron=showIndicator).grid(row=4, column=4, padx=10, ipady=5)
Radiobutton(root, text="off",value=False,variable=Insurance,indicatoron=showIndicator).grid(row=4, column=5, padx=10, ipady=5)

Label(root, text=str(add_on.json()["extra service"][2])).grid(row=4, column=6, padx=10, ipady=5, sticky='E')
Radiobutton(root, text="on",value=True,variable=Lounge,indicatoron=showIndicator).grid(row=4, column=7, padx=10, ipady=5)
Radiobutton(root, text="off",value=False,variable=Lounge,indicatoron=showIndicator).grid(row=4, column=8, padx=10, ipady=5)

Label(root, text="Special assistance").grid(row=5, column=0, padx=10, ipady=5, sticky='E')

Label(root, text=str(add_on.json()["special assistance"][0])).grid(row=6, column=0, padx=10, ipady=5, sticky='E')
Radiobutton(root, text="on",value=True,variable=Deaf,indicatoron=showIndicator).grid(row=6, column=1, padx=10, ipady=5)
Radiobutton(root, text="off",value=False,variable=Deaf,indicatoron=showIndicator).grid(row=6, column=2, padx=10, ipady=5)

Label(root, text=str(add_on.json()["special assistance"][1])).grid(row=6, column=3, padx=10, ipady=5, sticky='E')
Radiobutton(root, text="on",value=True,variable=Blind,indicatoron=showIndicator).grid(row=6, column=4, padx=10, ipady=5)
Radiobutton(root, text="off",value=False,variable=Blind,indicatoron=showIndicator).grid(row=6, column=5, padx=10, ipady=5)

Label(root, text=str(add_on.json()["special assistance"][2])).grid(row=6, column=6, padx=10, ipady=5, sticky='E')
Radiobutton(root, text="on",value=True,variable=Monk,indicatoron=showIndicator).grid(row=6, column=7, padx=10, ipady=5)
Radiobutton(root, text="off",value=False,variable=Monk,indicatoron=showIndicator).grid(row=6, column=8, padx=10, ipady=5)

Label(root, text=str(add_on.json()["special assistance"][3])).grid(row=7, column=0, padx=10, ipady=5, sticky='E')
Radiobutton(root, text="on",value=True,variable=Nun,indicatoron=showIndicator).grid(row=7, column=1, padx=10, ipady=5)
Radiobutton(root, text="off",value=False,variable=Nun,indicatoron=showIndicator).grid(row=7, column=2, padx=10, ipady=5)

Label(root, text=str(add_on.json()["special assistance"][4])).grid(row=7, column=3, padx=10, ipady=5, sticky='E')
Radiobutton(root, text="on",value=True,variable=Wheelchair,indicatoron=showIndicator).grid(row=7, column=4, padx=10, ipady=5)
Radiobutton(root, text="off",value=False,variable=Wheelchair,indicatoron=showIndicator).grid(row=7, column=5, padx=10, ipady=5)

Label(root, text=str(add_on.json()["special assistance"][5])).grid(row=7, column=6, padx=10, ipady=5, sticky='E')
Radiobutton(root, text="on",value=True,variable=Alone_kid,indicatoron=showIndicator).grid(row=7, column=7, padx=10, ipady=5)
Radiobutton(root, text="off",value=False,variable=Alone_kid,indicatoron=showIndicator).grid(row=7, column=8, padx=10, ipady=5)

Label(root, text="Baggage").grid(row=8, column=0, padx=10, ipady=5, sticky='E')
om = OptionMenu(root,baggage,*baggage_size)
om.config(width=15)
om.grid(row=8,column=1)

Label(root, text="Meal").grid(row=9, column=0, padx=10, ipady=5, sticky='E')
om = OptionMenu(root,meal,*add_on.json()['meal'])
om.config(width=15)
om.grid(row=9,column=1)

Label(root, text="Amount").grid(row=9, column=2, padx=10, ipady=5, sticky='E')
om = OptionMenu(root,meal_amount,*number)
om.config(width=15)
om.grid(row=9,column=3)

Label(root, text="Special baggage").grid(row=10, column=0, padx=10, ipady=5, sticky='E')
om = OptionMenu(root,Special_baggage,*special_baggage_list)
om.config(width=15)
om.grid(row=10,column=1)

button = Button(root, text=" Next ", command= lambda: on_click(data))
button.grid(row=11, column=2, columnspan=2)
if data['num_adult'] == 1 and  data['num_kid'] == 0:
    button.config(text = "confirm" , command = lambda : finish(data) )







root.mainloop()