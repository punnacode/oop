import tkinter as tk
import requests
from tkinter import messagebox

API_LOGIN = "http://127.0.0.1:8000/login"
API_CREATE_FLIGHT = "http://127.0.0.1:8000/flight"
API_CREATE_FLIGHT_INSTANCE = "http://127.0.0.1:8000/flight_instance"
API_EDIT_FLIGHT_INSTANCE = "http://127.0.0.1:8000/edit_flight_instance"
API_CANCEL_FLIGHT_INSTANCE = "http://127.0.0.1:8000/cancel_flight_instance"
API_CHANGE_SEAT = "http://127.0.0.1:8000/change_seat"
API_ADD_PROMOTION = "http://127.0.0.1:8000/add_promotion"
API_OAP = "http://127.0.0.1:8000/select_origin"
API_DAP = "http://127.0.0.1:8000/select_destination"
API_DATE = "http://127.0.0.1:8000/select_date"
API_SELECT_FLIGHT = "http://127.0.0.1:8000/select_flight"
API_FLIGHT_DETAIL = "http://127.0.0.1:8000/flight_detail/"
API_PACKAGE_DETAIL = "http://127.0.0.1:8000/package_detail/"
API_CREATE_BOOKING = "http://127.0.0.1:8000/create_booking"
API_INTER_CHECK = "http://127.0.0.1:8000/inter_status"
API_TITLE = "http://127.0.0.1:8000/passenger_title/"
API_PASSENGER = "http://127.0.0.1:8000/passengers"
API_ADULT_LIST = "http://127.0.0.1:8000/passenger_adult_list"
API_CHILD_LIST = "http://127.0.0.1:8000/passenger_child_list"
API_SEAT = "http://127.0.0.1:8000/select_seat/"
API_ADD_ON = "http://127.0.0.1:8000/select_add_on"
API_CREATE_TICKET = "http://127.0.0.1:8000/creat_ticket/"
API_TICKET_SUMMARY = "http://127.0.0.1:8000/ticket_summary"
API_SUM_PRICE = "http://127.0.0.1:8000/sum_price"
API_PROMOTION = "http://127.0.0.1:8000/add_promotion_code"
API_PAYMENT_TYPE = "http://127.0.0.1:8000/get_payment_type"
API_QR_CODE = "http://127.0.0.1:8000/qr_code_payment"
API_CREDIT_CARD = "http://127.0.0.1:8000/credit_card_payment"
API_COUNTER = "http://127.0.0.1:8000/counter_payment"
API_DEL_BOOKING = "http://127.0.0.1:8000/del_booking"

admin = {
        "Username":"",
        "Password":"",
        }

data = {
        "Origin airport":"",
        "Destination airport":"",
        "Date depart":"",
        "Flight name":"",
        "Package name":"",
        "Adult":0,
        "Child":0,
        "Infant":0,
        "Booking ID":0
        }

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack(side = "top",fill = "both",expand = True)

        self.frames = {}
        self.frames[StartMenu] = StartMenu(window,self)
        self.frames[StartMenu].pack(padx = 100, pady = 50)
        self.frames[AdminLoginPage] = AdminLoginPage(window,self)
        self.frames[AdminLoginPage].forget()
        self.frames[AdminPage] = AdminPage(window,self)
        self.frames[AdminPage].forget()
        self.frames[SearchFlight] = SearchFlight(window,self)
        self.frames[SearchFlight].forget()
        self.frames[SelectFlight] = SelectFlight(window)
        self.frames[SelectFlight].forget()
        self.frames[PassengerInfo] = PassengerInfo(window)
        self.frames[PassengerInfo].forget()
        self.frames[SelectAddOn] = SelectAddOn(window,self)
        self.frames[SelectAddOn].forget()
        self.frames[PaymentSummary] = PaymentSummary(window,self)
        self.frames[PaymentSummary].forget()
        self.frames[QRPayment] = QRPayment(window,self)
        self.frames[QRPayment].forget()
        self.frames[CounterServicePayment] = CounterServicePayment(window,self)
        self.frames[CounterServicePayment].forget()
        self.frames[CreditPayment] = CreditPayment(window,self)
        self.frames[CreditPayment].forget()
        self.frames[ShowTicket] = ShowTicket(window)
        self.frames[ShowTicket].forget()

    def login_page(self):
        self.frames[StartMenu].forget()
        self.frames[AdminLoginPage].tkraise()
        self.frames[AdminLoginPage].pack(padx = 100, pady = 50)

    def login(self):
        payload = {
        "Username": self.frames[AdminLoginPage].username.get(),
        "Password": self.frames[AdminLoginPage].password.get()
        }
        response = requests.post(API_LOGIN,json=payload)
        if response.ok:
            if response.json()["result"] == "LOGIN SUCCESSFULLY":
                admin["Username"] = self.frames[AdminLoginPage].username.get()
                admin["Password"] = self.frames[AdminLoginPage].password.get()
                self.frames[AdminLoginPage].forget()
                self.frames[AdminPage].tkraise()
                self.frames[AdminPage].pack(padx = 100, pady = 50)
            else:
                messagebox.showerror("Login","Incorrect username or password")

    def inter_select(self):
        print(self.frames[AdminPage].international.get())

    def create_flight(self):
        payload = {
                    "Username":admin["Username"],
                    "Password":admin["Password"],
                    "Name": self.frames[AdminPage].name.get(),
                    "Flight Duration": self.frames[AdminPage].duration.get(),
                    "International":self.frames[AdminPage].international.get(),
                    "Depart Airport": self.frames[AdminPage].depart.get(),
                    "Arrive Airport": self.frames[AdminPage].arrive.get()
                    }
        response = requests.post(API_CREATE_FLIGHT,json=payload)
        if response.ok:
            print(response.json())
        else:
            print("Error")

    def create_flight_instance(self):
        payload = {
            "Username":admin["Username"],
            "Password":admin["Password"],
            "Depart Airport": self.frames[AdminPage].depart_airport.get(),
            "Flight": self.frames[AdminPage].flight.get(),
            "Date": self.frames[AdminPage].date.get(),
            "Time Depart": self.frames[AdminPage].time_depart.get(),
            "Time Arrive": self.frames[AdminPage].time_arrive.get(),
            "Aircraft": self.frames[AdminPage].aircraft.get(),
            "Price": self.frames[AdminPage].price.get()
        }
        response = requests.post(API_CREATE_FLIGHT_INSTANCE,json=payload)
        if response.ok:
            print(response.json())
        else:
            print("Error")

    def edit_flight_instance(self):
        payload = {
                    "Username":admin["Username"],
                    "Password":admin["Password"],
                    "Depart Airport": self.frames[AdminPage].depfedit.get(),
                    "Date": self.frames[AdminPage].datefedit.get(),
                    "Flight": self.frames[AdminPage].flightfedit.get(),
                    "Edit Date": self.frames[AdminPage].edit_date.get(),
                    "Edit Time Depart": self.frames[AdminPage].edit_time_depart.get(),
                    "Edit Time Arrive": self.frames[AdminPage].edit_time_arrive.get(),
                    "Edit Price": self.frames[AdminPage].edit_price.get()
                    }
        response = requests.put(API_EDIT_FLIGHT_INSTANCE,json=payload)
        if response.ok:
            print(response.json())
        else:
            print("Error")

    def cancel_flight_instance(self):
        payload = {
                    "Username":admin["Username"],
                    "Password":admin["Password"],
                    "Depart Airport": self.frames[AdminPage].depfcancel.get(),
                    "Date": self.frames[AdminPage].datefcancel.get(),
                    "Flight": self.frames[AdminPage].flightfcancel.get(),
                    "Seat": self.frames[AdminPage].edit_date.get(),
                    }
        response = requests.delete(API_CANCEL_FLIGHT_INSTANCE,json=payload)
        if response.ok:
            print(response.json())
        else:
            print("Error")

    def change_seat(self):
        payload = {
                    "Username":admin["Username"],
                    "Password":admin["Password"],
                    "Booking ID": self.frames[AdminPage].booking_id.get(),
                    "Date": self.frames[AdminPage].date_departfseat.get(),
                    "Flight": self.frames[AdminPage].flightfseat.get(),
                    "Seat":self.frames[AdminPage].seat.get(),
                    "Change to:": self.frames[AdminPage].edit_seat.get()
                    }
        response = requests.put(API_CHANGE_SEAT,json=payload)
        if response.ok:
            print(response.json())
        else:
            print("Error")

    def add_promotion(self):
        payload = {
                    "Username":admin["Username"],
                    "Password":admin["Password"],
                    "Promotion Code": self.frames[AdminPage].promotion_code.get(),
                    "Discount": self.frames[AdminPage].discount.get()
                    }    
        response = requests.post(API_ADD_PROMOTION,json=payload)
        if response.ok:
            print(response.json())
        else:
            print("Error")

    def search_page(self):
        response = requests.get(API_OAP)
        airport_data = response.json()
        menu = self.frames[SearchFlight].oap_om["menu"]
        menu.delete(0, "end")
        self.frames[SearchFlight].OAP_list.clear()
        for airport in airport_data["Origin airport list"]:
            self.frames[SearchFlight].OAP_list.append(airport)
            menu.add_command(label=airport, command=lambda value=airport: self.frames[SearchFlight].selectOAP.set(value))

        self.frames[StartMenu].forget()
        self.frames[SearchFlight].tkraise()
        self.frames[SearchFlight].pack(padx = 100, pady = 50)

    def oap_submit(self,airport):
        data["Origin airport"] = airport
        response = requests.post(API_DAP,json=data)
        if response.ok:
            airport_data = response.json()
            menu = self.frames[SearchFlight].dap_om["menu"]
            menu.delete(0, "end")
            self.frames[SearchFlight].DAP_list.clear()
            if airport_data["Destination airport list"] == []:
                self.frames[SearchFlight].DAP_list.append("-")
                menu.add_command(label="-", command=lambda value="-": self.frames[SearchFlight].selectDAP.set(value))
            else:
                for airport in airport_data["Destination airport list"]:
                    self.frames[SearchFlight].DAP_list.append(airport)
                    menu.add_command(label=airport, command=lambda value=airport: self.frames[SearchFlight].selectDAP.set(value))
    
    def dap_submit(self,airport):
        data["Destination airport"] = airport
        reponse = requests.post(API_DATE,json=data)
        if reponse.ok:
            date_data = reponse.json()
            menu = self.frames[SearchFlight].date_om["menu"]
            menu.delete(0, "end")
            self.frames[SearchFlight].date_list.clear()
            if date_data["Date list"] == []:
                self.frames[SearchFlight].date_list.append("-")
                menu.add_command(label="-", command=lambda value="-": self.frames[SearchFlight].selectdate.set(value))
            else:
                for date in date_data["Date list"]:
                    self.frames[SearchFlight].date_list.append(date)
                    menu.add_command(label=date, command=lambda value=date: self.frames[SearchFlight].selectdate.set(value))

    def date_submit(self,date,adult,child,infant):
        row = 1
        column = 1

        if not isinstance(adult,int) or not isinstance(child,int) or not isinstance(infant,int):
            messagebox.showinfo("Error","Please enter amout of passenger")
        elif adult <= 0:
            messagebox.showinfo("Error","Require at least 1 adult")
        elif infant > adult:
            messagebox.showinfo("Error","Rrequire 1 adult for every each infant")
        elif adult + child + infant > 9:
            messagebox.showinfo("Error","Maximum passenger is 9")
        else:
            data["Date depart"] = date
            data["Adult"] = adult
            data["Child"] = child
            data["Infant"] = infant
            response = requests.post(API_SELECT_FLIGHT,json=data)
            if response.ok:
                response_data = response.json()
                if response_data["Flight data"] == []:
                    messagebox.showinfo("Error","Flight not found")
                else:
                    self.frames[SelectFlight].flight_list.clear()
                    self.frames[SelectFlight].package_list.clear()

                    for flight in response_data["Flight data"]:
                        self.frames[SelectFlight].flight_list.append(flight[0])
                    for package in response_data["Package data"]:
                        self.frames[SelectFlight].package_list.append(package)

                    self.frames[SelectFlight].select_flight.set("Select flight")
                    self.frames[SelectFlight].select_package.set("Select package")
                    tk.OptionMenu(self.frames[SelectFlight],self.frames[SelectFlight].select_flight,*self.frames[SelectFlight].flight_list).grid(row=0,column=1)
                    tk.OptionMenu(self.frames[SelectFlight],self.frames[SelectFlight].select_package,*self.frames[SelectFlight].package_list).grid(row=0,column=3)
                    tk.Label(self.frames[SelectFlight],text = "Select flight").grid(row=0,column=0)
                    tk.Label(self.frames[SelectFlight],text = "Select package").grid(row=0,column=2)
                    tk.Button(self.frames[SelectFlight],text="Submit",command= lambda: self.flight_submit(str(self.frames[SelectFlight].select_flight.get()),str(self.frames[SelectFlight].select_package.get()),data["Adult"],data["Child"],data["Infant"])).grid(row=0,column=4)
                    tk.Button(self.frames[SelectFlight],text="Back",command= lambda: self.back_to_search(SelectFlight)).grid(row=0,column=5)

                    for flight_data in response_data["Flight data"]:
                        tk.Button(self.frames[SelectFlight],text=str(flight_data[0]+" Departure"+flight_data[1]+" Arrival"+flight_data[2]),command= lambda name = flight_data[0]: self.flight_detail(name)).grid(row=row,column=0)
                        for key, value in flight_data[3].items():
                            tk.Button(self.frames[SelectFlight],text=str(key+" "+str(value)),command= lambda name = key: self.package_detail(name)).grid(row=row,column=column)
                            column += 1
                        column = 1
                        row += 1

                    self.frames[SearchFlight].forget()
                    self.frames[SelectFlight].tkraise()
                    self.frames[SelectFlight].pack(padx = 100, pady = 50)

    def flight_detail(self,flight_name):
        response = requests.post(str(API_FLIGHT_DETAIL+flight_name),json=data)
        if response.ok:
            flight_data = response.json()
            flight_detail = str("Flight name: " + flight_data["Name"] + "\n"
                                "Aircraft name: " + flight_data["Aircraft"] + "\n"
                                "Origin Airport: " + flight_data["Origin Airport"] + "\n"
                                "Destination Airport: " + flight_data["Destination Airport"] + "\n"
                                "Flight Duration: " + str(flight_data["Flight Duration"]) + " minute\n"
                                "Time Depart: " + flight_data["Time Depart"] + "\n"
                                "Time Arrive: " + flight_data["Time Arrive"] + "\n"
                                "Date Depart: " + flight_data["Date Depart"] + "\n"
                                )
            messagebox.showinfo("Flight detail",flight_detail)

    def package_detail(self,package_name):
        response = requests.get(str(API_PACKAGE_DETAIL+package_name))
        package_data = response.json()
        bagage = str("Bagage: " + str(package_data[package_name]["Bagage"]) + " kg\n")
        if package_data[package_name]["Meal"] == None:
            meal = ""
        else:
            meal = str("Meal amount: "+ str(package_data[package_name]["Meal"])  + "\n")
        if package_data[package_name]["Extra service"] == []:
            extraservice = ""
        else:
            extraservice = str("Extraservice: " + ", ".join(package_data[package_name]["Extra service"]) + "\n")
        messagebox.showinfo("Package detail",str(package_name + " package\n" + bagage + meal + extraservice))
        return

    def back_to_search(self,f):
        for widjet in self.frames[SelectFlight].winfo_children():
            widjet.destroy()

        data["Origin airport"] = ""
        data["Destination airport"] = ""
        data["Date depart"] = ""
        data["Flight name"] = ""
        data["Package name"] = ""
        data["Adult"] = 0
        data["Child"] = 0
        data["Infant"] = 0
        data["Booking ID"] = 0

        self.frames[SearchFlight].selectOAP.set("Select airport")
        self.frames[SearchFlight].selectDAP.set("Select airport")
        self.frames[SearchFlight].selectdate.set("Select Date")
        self.frames[SearchFlight].adult.set(0)
        self.frames[SearchFlight].child.set(0)
        self.frames[SearchFlight].infant.set(0)

        dap_menu = self.frames[SearchFlight].dap_om["menu"]
        dap_menu.delete(0, "end")
        self.frames[SearchFlight].DAP_list.clear()
        self.frames[SearchFlight].DAP_list.append("-")
        dap_menu.add_command(label="-", command=lambda value="-": self.frames[SearchFlight].selectDAP.set(value))

        date_menu = self.frames[SearchFlight].date_om["menu"]
        date_menu.delete(0, "end")
        self.frames[SearchFlight].date_list.clear()
        self.frames[SearchFlight].date_list.append("-")
        date_menu.add_command(label="-", command=lambda value="-": self.frames[SearchFlight].selectdate.set(value))

        self.frames[f].forget()
        self.frames[SearchFlight].tkraise()
        self.frames[SearchFlight].pack(padx = 100, pady = 50)

    def back_to_select_flight(self):
        row = 1
        column = 1

        requests.post(API_DEL_BOOKING,json=data)

        for widjet in self.frames[PassengerInfo].winfo_children():
            widjet.destroy()

        data["Booking ID"] = 0
        data["Flight name"] = ""
        data["Package name"] = ""

        response = requests.post(API_SELECT_FLIGHT,json=data)
        if response.ok:
            response_data = response.json()
            if response_data["Flight data"] == []:
                messagebox.showinfo("Error","Flight not found")
            else:
                self.frames[SelectFlight].flight_list.clear()
                self.frames[SelectFlight].package_list.clear()

                for flight in response_data["Flight data"]:
                    self.frames[SelectFlight].flight_list.append(flight[0])
                for package in response_data["Package data"]:
                    self.frames[SelectFlight].package_list.append(package)

                self.frames[SelectFlight].select_flight.set("Select flight")
                self.frames[SelectFlight].select_package.set("Select package")
                tk.OptionMenu(self.frames[SelectFlight],self.frames[SelectFlight].select_flight,*self.frames[SelectFlight].flight_list).grid(row=0,column=1)
                tk.OptionMenu(self.frames[SelectFlight],self.frames[SelectFlight].select_package,*self.frames[SelectFlight].package_list).grid(row=0,column=3)
                tk.Label(self.frames[SelectFlight],text = "Select flight").grid(row=0,column=0)
                tk.Label(self.frames[SelectFlight],text = "Select package").grid(row=0,column=2)
                tk.Button(self.frames[SelectFlight],text="Submit",command= lambda: self.flight_submit(str(self.frames[SelectFlight].select_flight.get()),str(self.frames[SelectFlight].select_package.get()),data["Adult"],data["Child"],data["Infant"])).grid(row=0,column=4)
                tk.Button(self.frames[SelectFlight],text="Back",command= lambda: self.back_to_search(SelectFlight)).grid(row=0,column=5)

                for flight_data in response_data["Flight data"]:
                    tk.Button(self.frames[SelectFlight],text=str(flight_data[0]+" Departure"+flight_data[1]+" Arrival"+flight_data[2]),command= lambda name = flight_data[0]: self.flight_detail(name)).grid(row=row,column=0)
                    for key, value in flight_data[3].items():
                        tk.Button(self.frames[SelectFlight],text=str(key+" "+str(value)),command= lambda name = key: self.package_detail(name)).grid(row=row,column=column)
                        column += 1
                    column = 1
                    row += 1

                self.frames[PassengerInfo].forget()
                self.frames[SelectFlight].tkraise()
                self.frames[SelectFlight].pack(padx = 100, pady = 50)

    def back_to_passenger(self):
        requests.post(API_DEL_BOOKING,json=data)

        for widjet in self.frames[PassengerInfo].winfo_children():
                    widjet.destroy()

        data["Booking ID"] = 0
        response = requests.post(API_CREATE_BOOKING,json=data)
        if response.ok:
            data["Booking ID"] = response.json()["Booking ID"]

            self.frames[PassengerInfo].adult_num = data["Adult"]
            self.frames[PassengerInfo].child_num = data["Child"]
            self.frames[PassengerInfo].infant_num = data["Infant"]

            self.frames[PassengerInfo].adult_num -= 1
            self.frames[PassengerInfo].select_passenger_type.set("ADULT")
            title_list = requests.get(str(API_TITLE + "ADULT")).json()
            title_om = tk.OptionMenu(self.frames[PassengerInfo],self.frames[PassengerInfo].select_passenger_title,*title_list)
            title_om.config(width=10)
            title_om.grid(row=1,column=1)

            tk.Label(self.frames[PassengerInfo],text=str("Adult : " + str(data["Adult"] - self.frames[PassengerInfo].adult_num))).grid(row=0,column=0,padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[PassengerInfo], text="Title :").grid(row=1, column=0,padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[PassengerInfo], text="Name :").grid(row=2, column=0,padx=10, ipady=5, sticky='E')
            tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].name, width=12, justify="left").grid(row=2, column=1, padx=10)
            tk.Label(self.frames[PassengerInfo], text="Last Name :").grid(row=3, column=0,padx=10, ipady=5, sticky='E')
            tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].last_name, width=12, justify="left").grid(row=3, column=1, padx=10)
            tk.Label(self.frames[PassengerInfo], text="Date of birth  :").grid(row=4, column=0,padx=10, ipady=5, sticky='E')
            tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].date_of_birth, width=12, justify="left").grid(row=4, column=1, padx=10)
            tk.Label(self.frames[PassengerInfo], text="Phone Number  :").grid(row=5, column=0,padx=10, ipady=5, sticky='E')
            tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].phon_number, width=12, justify="left").grid(row=5, column=1, padx=10)
            tk.Label(self.frames[PassengerInfo], text="Email  :").grid(row=6, column=0,padx=10, ipady=5, sticky='E')
            tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].email, width=12, justify="left").grid(row=6, column=1, padx=10)            

            #inter = True
            inter = requests.post(API_INTER_CHECK,json=data)
            if inter == True:
                tk.Label(self.frames[PassengerInfo], text="Nationality :").grid(row=7, column=0,padx=10, ipady=5, sticky='E')
                tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].national, width=12, justify="left").grid(row=7, column=1, padx=10)
                tk.Label(self.frames[PassengerInfo], text="Country ressidence :").grid(row=8, column=0,padx=10, ipady=5, sticky='E')
                tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].country_residence, width=12, justify="left").grid(row=8, column=1, padx=10)
                tk.Label(self.frames[PassengerInfo], text="Passport number :").grid(row=9, column=0,padx=10, ipady=5, sticky='E')
                tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].passport_number, width=12, justify="left").grid(row=9, column=1, padx=10)
                tk.Label(self.frames[PassengerInfo], text="Issued by :").grid(row=10, column=0,padx=10, ipady=5, sticky='E')
                tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].issued_by, width=12, justify="left").grid(row=10, column=1, padx=10)
                tk.Label(self.frames[PassengerInfo], text="Passport exp date :").grid(row=11, column=0,padx=10, ipady=5, sticky='E')
                tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].passport_exp_date, width=12, justify="left").grid(row=11, column=1, padx=10)

            tk.Button(self.frames[PassengerInfo],text="Next", bg="green",command= lambda: self.next_passenger()).grid(row=12,column=0, ipadx=10, ipady=5)
            tk.Button(self.frames[PassengerInfo],text="Back", bg="green",command= lambda: self.back_to_select_flight()).grid(row=12,column=1, ipadx=10, ipady=5)

            self.frames[SelectAddOn].forget()
            self.frames[PassengerInfo].tkraise()
            self.frames[PassengerInfo].pack(padx = 100, pady = 50)

    def flight_submit(self,flight_name,package_name,adult,child,infant):
        data["Flight name"] = flight_name
        data["Package name"] = package_name
        print(data["Flight name"],data["Package name"])
        response = requests.post(API_CREATE_BOOKING,json=data)
        if response.ok:
            data["Booking ID"] = response.json()["Booking ID"]
            self.frames[PassengerInfo].adult_num = adult
            self.frames[PassengerInfo].child_num = child
            self.frames[PassengerInfo].infant_num = infant

            self.frames[PassengerInfo].adult_num -= 1
            self.frames[PassengerInfo].select_passenger_type.set("ADULT")
            title_list = requests.get(str(API_TITLE + "ADULT")).json()
            title_om = tk.OptionMenu(self.frames[PassengerInfo],self.frames[PassengerInfo].select_passenger_title,*title_list)
            title_om.config(width=10)
            title_om.grid(row=1,column=1)

            tk.Label(self.frames[PassengerInfo],text=str("Adult : " + str(data["Adult"] - self.frames[PassengerInfo].adult_num))).grid(row=0,column=0,padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[PassengerInfo], text="Title :").grid(row=1, column=0,padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[PassengerInfo], text="Name :").grid(row=2, column=0,padx=10, ipady=5, sticky='E')
            tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].name, width=12, justify="left").grid(row=2, column=1, padx=10)
            tk.Label(self.frames[PassengerInfo], text="Last Name :").grid(row=3, column=0,padx=10, ipady=5, sticky='E')
            tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].last_name, width=12, justify="left").grid(row=3, column=1, padx=10)
            tk.Label(self.frames[PassengerInfo], text="Date of birth  :").grid(row=4, column=0,padx=10, ipady=5, sticky='E')
            tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].date_of_birth, width=12, justify="left").grid(row=4, column=1, padx=10)
            tk.Label(self.frames[PassengerInfo], text="Phone Number  :").grid(row=5, column=0,padx=10, ipady=5, sticky='E')
            tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].phon_number, width=12, justify="left").grid(row=5, column=1, padx=10)
            tk.Label(self.frames[PassengerInfo], text="Email  :").grid(row=6, column=0,padx=10, ipady=5, sticky='E')
            tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].email, width=12, justify="left").grid(row=6, column=1, padx=10)            

            #inter = True
            inter = requests.post(API_INTER_CHECK,json=data)
            if inter == True:
                tk.Label(self.frames[PassengerInfo], text="Nationality :").grid(row=7, column=0,padx=10, ipady=5, sticky='E')
                tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].national, width=12, justify="left").grid(row=7, column=1, padx=10)
                tk.Label(self.frames[PassengerInfo], text="Country ressidence :").grid(row=8, column=0,padx=10, ipady=5, sticky='E')
                tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].country_residence, width=12, justify="left").grid(row=8, column=1, padx=10)
                tk.Label(self.frames[PassengerInfo], text="Passport number :").grid(row=9, column=0,padx=10, ipady=5, sticky='E')
                tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].passport_number, width=12, justify="left").grid(row=9, column=1, padx=10)
                tk.Label(self.frames[PassengerInfo], text="Issued by :").grid(row=10, column=0,padx=10, ipady=5, sticky='E')
                tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].issued_by, width=12, justify="left").grid(row=10, column=1, padx=10)
                tk.Label(self.frames[PassengerInfo], text="Passport exp date :").grid(row=11, column=0,padx=10, ipady=5, sticky='E')
                tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].passport_exp_date, width=12, justify="left").grid(row=11, column=1, padx=10)

            tk.Button(self.frames[PassengerInfo],text="Next", bg="green",command= lambda: self.next_passenger()).grid(row=12,column=0, ipadx=10, ipady=5)
            tk.Button(self.frames[PassengerInfo],text="Back", bg="green",command= lambda: self.back_to_select_flight()).grid(row=12,column=1, ipadx=10, ipady=5)

            self.frames[SelectFlight].forget()
            self.frames[PassengerInfo].tkraise()
            self.frames[PassengerInfo].pack(padx = 100, pady = 50)

    def next_passenger(self):
            inter = requests.post(API_INTER_CHECK,json=data).json()
            if self.frames[PassengerInfo].name.get() == "" and self.frames[PassengerInfo].last_name.get() == "" and self.frames[PassengerInfo].date_of_birth.get() == "":
                messagebox.showerror("Error","Please enter infomation")
                return
            elif data["Adult"] - 1 == self.frames[PassengerInfo].adult_num and self.frames[PassengerInfo].phon_number.get() == "" and self.frames[PassengerInfo].email.get() == "":
                messagebox.showerror("Error","Please enter infomation")
                return 
            elif inter == True and self.frames[PassengerInfo].national.get() == "" and self.frames[PassengerInfo].country_residence.get() == "" and self.frames[PassengerInfo].passport_number.get() == "" and self.frames[PassengerInfo].issued_by.get() == "" and self.frames[PassengerInfo].passport_exp_date.get() == "":
                messagebox.showerror("Error","Please enter infomation")
                return
            elif self.frames[PassengerInfo].select_passenger_type.get() == "INFANT" and self.frames[PassengerInfo].select_adult_list.get() == "":
                messagebox.showerror("Error","Please enter infomation")
                return
            payload = {
                        "name": self.frames[PassengerInfo].name.get(), 
                        "last_name": self.frames[PassengerInfo].last_name.get(),
                        "date_of_birth": self.frames[PassengerInfo].date_of_birth.get(),
                        "phone_number": self.frames[PassengerInfo].phon_number.get(),
                        "email": self.frames[PassengerInfo].email.get(),
                        "national": self.frames[PassengerInfo].national.get(),
                        "country_residence": self.frames[PassengerInfo].country_residence.get(),
                        "passport_number": self.frames[PassengerInfo].passport_number.get(),
                        "issued_by": self.frames[PassengerInfo].issued_by.get(),
                        "passport_exp_date": self.frames[PassengerInfo].passport_exp_date.get(),
                        "parent": self.frames[PassengerInfo].select_adult_list.get(),
                        "Origin airport": data["Origin airport"],
                        "Date depart": data["Date depart"],
                        "Flight name": data["Flight name"],
                        'Booking ID': data["Booking ID"]
                        }
            response = requests.post(str(API_PASSENGER+'/'+self.frames[PassengerInfo].select_passenger_type.get()+'/'+self.frames[PassengerInfo].select_passenger_title.get()),json=payload)
            if response.ok:

                for widjet in self.frames[PassengerInfo].winfo_children():
                    widjet.destroy()

                self.frames[PassengerInfo].select_passenger_title.set('')
                self.frames[PassengerInfo].name.set('')
                self.frames[PassengerInfo].last_name.set('')
                self.frames[PassengerInfo].date_of_birth.set('')
                self.frames[PassengerInfo].phon_number.set('')
                self.frames[PassengerInfo].email.set('')
                self.frames[PassengerInfo].national.set('')
                self.frames[PassengerInfo].country_residence.set('')
                self.frames[PassengerInfo].passport_number.set('')
                self.frames[PassengerInfo].issued_by.set('')
                self.frames[PassengerInfo].passport_exp_date.set('')

                if self.frames[PassengerInfo].infant_num > 0 or self.frames[PassengerInfo].child_num > 0 or self.frames[PassengerInfo].adult_num > 0:
                    tk.Label(self.frames[PassengerInfo], text="Title :").grid(row=1, column=0,padx=10, ipady=5, sticky='E')
                    tk.Label(self.frames[PassengerInfo], text="Name :").grid(row=2, column=0,padx=10, ipady=5, sticky='E')
                    tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].name, width=12, justify="left").grid(row=2, column=1, padx=10)
                    tk.Label(self.frames[PassengerInfo], text="Last Name :").grid(row=3, column=0,padx=10, ipady=5, sticky='E')
                    tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].last_name, width=12, justify="left").grid(row=3, column=1, padx=10)
                    tk.Label(self.frames[PassengerInfo], text="Date of birth  :").grid(row=4, column=0,padx=10, ipady=5, sticky='E')
                    tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].date_of_birth, width=12, justify="left").grid(row=4, column=1, padx=10)
            
                    if inter == True:
                        tk.Label(self.frames[PassengerInfo], text="Nationality :").grid(row=5, column=0,padx=10, ipady=5, sticky='E')
                        tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].national, width=12, justify="left").grid(row=5, column=1, padx=10)
                        tk.Label(self.frames[PassengerInfo], text="Country ressidence :").grid(row=6, column=0,padx=10, ipady=5, sticky='E')
                        tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].country_residence, width=12, justify="left").grid(row=6, column=1, padx=10)
                        tk.Label(self.frames[PassengerInfo], text="Passport number :").grid(row=7, column=0,padx=10, ipady=5, sticky='E')
                        tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].passport_number, width=12, justify="left").grid(row=7, column=1, padx=10)
                        tk.Label(self.frames[PassengerInfo], text="Issued by :").grid(row=8, column=0,padx=10, ipady=5, sticky='E')
                        tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].issued_by, width=12, justify="left").grid(row=8, column=1, padx=10)
                        tk.Label(self.frames[PassengerInfo], text="Passport exp date :").grid(row=9, column=0,padx=10, ipady=5, sticky='E')
                        tk.Entry(self.frames[PassengerInfo], textvariable=self.frames[PassengerInfo].passport_exp_date, width=12, justify="left").grid(row=9, column=1, padx=10)
                    tk.Button(self.frames[PassengerInfo],text="Next", bg="green",command= lambda: self.next_passenger()).grid(row=13,column=0, ipadx=10, ipady=5)
                    tk.Button(self.frames[PassengerInfo],text="Back", bg="green",command= lambda: self.back_to_select_flight()).grid(row=13,column=1, ipadx=10, ipady=5)
                else:
                    self.finish_passenger(data["Adult"],data["Child"])

                if self.frames[PassengerInfo].adult_num > 0:
                    self.frames[PassengerInfo].adult_num -= 1
                    self.frames[PassengerInfo].select_passenger_type.set("ADULT")
                    title_list = requests.get(str(API_TITLE + "ADULT")).json()
                    title_om = tk.OptionMenu(self.frames[PassengerInfo],self.frames[PassengerInfo].select_passenger_title,*title_list)
                    title_om.config(width=10)
                    title_om.grid(row=1,column=1)
                    tk.Label(self.frames[PassengerInfo],text=str("Adult : " + str(data["Adult"] - self.frames[PassengerInfo].adult_num))).grid(row=0,column=0,padx=10, ipady=5, sticky='E')
                elif self.frames[PassengerInfo].child_num > 0:
                    self.frames[PassengerInfo].child_num -= 1
                    self.frames[PassengerInfo].select_passenger_type.set("CHILD")
                    title_list = requests.get(str(API_TITLE + "CHILD")).json()
                    title_om = tk.OptionMenu(self.frames[PassengerInfo],self.frames[PassengerInfo].select_passenger_title,*title_list)
                    title_om.config(width=10)
                    title_om.grid(row=1,column=1)
                    tk.Label(self.frames[PassengerInfo],text=str("Child : " + str(data["Child"] - self.frames[PassengerInfo].child_num))).grid(row=0,column=0,padx=10, ipady=5, sticky='E')
                elif self.frames[PassengerInfo].infant_num > 0:
                    self.frames[PassengerInfo].infant_num -= 1
                    self.frames[PassengerInfo].select_passenger_type.set("INFANT")
                    title_list = requests.get(str(API_TITLE + "INFANT")).json()
                    title_om = tk.OptionMenu(self.frames[PassengerInfo],self.frames[PassengerInfo].select_passenger_title,*title_list)
                    title_om.config(width=10)
                    title_om.grid(row=1,column=1)
                    tk.Label(self.frames[PassengerInfo], text="Parent :").grid(row=12, column=0,padx=10, ipady=5, sticky='E')
                    adult_list = requests.post(API_ADULT_LIST,json=data).json()
                    adult_list_om = tk.OptionMenu(self.frames[PassengerInfo],self.frames[PassengerInfo].select_adult_list,*adult_list)
                    adult_list_om.config(width=10)
                    adult_list_om.grid(row=12,column=1)
                    tk.Label(self.frames[PassengerInfo],text=str("Infant : " + str(data["Infant"] - self.frames[PassengerInfo].infant_num))).grid(row=0,column=0,padx=10, ipady=5, sticky='E')

    def finish_passenger(self,adult,child):

        self.frames[SelectAddOn].adult_num = adult
        self.frames[SelectAddOn].child_num = child

        if (self.frames[SelectAddOn].adult_num == 1 and self.frames[SelectAddOn].child_num == 0) or (self.frames[SelectAddOn].adult_num == 0 and self.frames[SelectAddOn].child_num == 1):
                self.frames[SelectAddOn].button.config(text = "confirm",command = lambda : self.finish_add_on())

        adult_list = requests.post(str(API_ADULT_LIST),json=data).json()
        self.frames[SelectAddOn].name_passenger.set(str(adult_list[data["Adult"] - self.frames[SelectAddOn].adult_num]))
        self.frames[SelectAddOn].name.config(text= "Passenger name: " + str(adult_list[data["Adult"] - self.frames[SelectAddOn].adult_num]))
        self.frames[SelectAddOn].adult_num -=1

        add_on = requests.post(str(API_ADD_ON),json=data)
        tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["extra service"][0])).grid(row=4, column=0, padx=10, ipady=5, sticky='E')
        tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["extra service"][1])).grid(row=4, column=3, padx=10, ipady=5, sticky='E')
        tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["extra service"][2])).grid(row=4, column=6, padx=10, ipady=5, sticky='E')
        tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][0])).grid(row=6, column=0, padx=10, ipady=5, sticky='E')
        tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][1])).grid(row=6, column=3, padx=10, ipady=5, sticky='E')
        tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][2])).grid(row=6, column=6, padx=10, ipady=5, sticky='E')
        tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][3])).grid(row=7, column=0, padx=10, ipady=5, sticky='E')
        tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][4])).grid(row=7, column=3, padx=10, ipady=5, sticky='E')
        tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][5])).grid(row=7, column=6, padx=10, ipady=5, sticky='E')

        seat_list = requests.post(str(API_SEAT+data["Flight name"]),json=data)
        for i in seat_list.json()['Seat']:
            st = str(str(i[0])+" "+str(i[1])+" "+str(i[2]))
            self.frames[SelectAddOn].seat_list.append(st)
        seat_menu = self.frames[SelectAddOn].seat_om["menu"]
        seat_menu.delete(0, "end")
        for seat in self.frames[SelectAddOn].seat_list:
            seat_menu.add_command(label=seat, command=lambda value=seat: self.frames[SelectAddOn].select_seat.set(value))
        self.frames[SelectAddOn].select_seat.set("Please select")

        self.frames[SelectAddOn].FastTrack.set(add_on.json()['package'][0][0]['_fasttrack']) 
        self.frames[SelectAddOn].Insurance.set(add_on.json()['package'][0][0]['_insurance'])
        self.frames[SelectAddOn].Lounge.set(add_on.json()['package'][0][0]['_lounge'])

        self.frames[SelectAddOn].Deaf.set(add_on.json()['package'][0][1]['_deaf'])
        self.frames[SelectAddOn].Blind.set(add_on.json()['package'][0][1]['_blind'])
        self.frames[SelectAddOn].Monk.set(add_on.json()['package'][0][1]['_monk']) 
        self.frames[SelectAddOn].Nun.set(add_on.json()['package'][0][1]['_nun']) 
        self.frames[SelectAddOn].Wheelchair.set(add_on.json()['package'][0][1]['_wheelchair']) 
        self.frames[SelectAddOn].Alone_kid.set(add_on.json()['package'][0][1]['_alonekid'])

        self.frames[SelectAddOn].baggage.set(add_on.json()['package'][0][2]['_extra_bag']) 

        self.frames[SelectAddOn].meal.set(add_on.json()['meal'][0])
        meal_menu = self.frames[SelectAddOn].meal_type_om["menu"]
        meal_menu.delete(0, "end")
        for meal in add_on.json()['meal']:
            meal_menu.add_command(label=meal, command=lambda value=meal: self.frames[SelectAddOn].meal.set(value))
        self.frames[SelectAddOn].meal_amount.set(add_on.json()['package'][0][3]['_meal_amount'])

        self.frames[SelectAddOn].Special_baggage.set(self.frames[SelectAddOn].special_baggage_list[0])

        self.frames[PassengerInfo].forget()
        self.frames[SelectAddOn].tkraise()
        self.frames[SelectAddOn].pack(padx = 100, pady = 50)

    def next_add_on(self):
        payload = {
                    "Booking ID": data['Booking ID'],
                    "Origin airport":data['Origin airport'],
                    "Destination airport":data['Destination airport'],
                    "Date depart":data['Date depart'],
                    "select_seat": self.frames[SelectAddOn].select_seat.get(),
                    "FastTrack": self.frames[SelectAddOn].FastTrack.get(),
                    "Insurance": self.frames[SelectAddOn].Insurance.get(),
                    "Lounge": self.frames[SelectAddOn].Lounge.get(),
                    "Deaf": self.frames[SelectAddOn].Deaf.get(),
                    "Blind": self.frames[SelectAddOn].Blind.get(),
                    "Nun": self.frames[SelectAddOn].Nun.get(),
                    "Monk": self.frames[SelectAddOn].Monk.get(),
                    "Wheelchair": self.frames[SelectAddOn].Wheelchair.get(),
                    "Alone_kid": self.frames[SelectAddOn].Alone_kid.get(),
                    "baggage": self.frames[SelectAddOn].baggage.get(),
                    "meal": self.frames[SelectAddOn].meal.get(),
                    "meal_amount" : self.frames[SelectAddOn].meal_amount.get(),
                    "Special_baggage": self.frames[SelectAddOn].Special_baggage.get(),
                    "Name" : self.frames[SelectAddOn].name_passenger.get()
                    }
        response = requests.post(str(API_CREATE_TICKET+data["Flight name"]),json=payload)
        if response.ok:
            if (self.frames[SelectAddOn].adult_num == 1 and self.frames[SelectAddOn].child_num == 0) or (self.frames[SelectAddOn].adult_num == 0 and self.frames[SelectAddOn].child_num == 1):
                self.frames[SelectAddOn].button.config(text = "confirm",command = lambda : self.finish_add_on())

            if self.frames[SelectAddOn].adult_num > 0:
                adult_list = requests.post(str(API_ADULT_LIST),json=data).json()
                self.frames[SelectAddOn].name_passenger.set(str(adult_list[data["Adult"] - self.frames[SelectAddOn].adult_num]))
                self.frames[SelectAddOn].name.config(text= "Passenger name: " + str(adult_list[data["Adult"] - self.frames[SelectAddOn].adult_num]))
                self.frames[SelectAddOn].adult_num -=1
            elif self.frames[SelectAddOn].child_num > 0:
                child_list = requests.post(str(API_CHILD_LIST),json=data).json()
                self.frames[SelectAddOn].name_passenger.set(str(child_list[data["Child"] - self.frames[SelectAddOn].child_num]))
                self.frames[SelectAddOn].name.config(text= "Passenger name: " + str(child_list[data["Child"] - self.frames[SelectAddOn].child_num]))
                self.frames[SelectAddOn].child_num -=1
            
            add_on = requests.post(str(API_ADD_ON),json=data)
            tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["extra service"][0])).grid(row=4, column=0, padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["extra service"][1])).grid(row=4, column=3, padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["extra service"][2])).grid(row=4, column=6, padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][0])).grid(row=6, column=0, padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][1])).grid(row=6, column=3, padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][2])).grid(row=6, column=6, padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][3])).grid(row=7, column=0, padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][4])).grid(row=7, column=3, padx=10, ipady=5, sticky='E')
            tk.Label(self.frames[SelectAddOn], text=str(add_on.json()["special assistance"][5])).grid(row=7, column=6, padx=10, ipady=5, sticky='E')

            for seat in self.frames[SelectAddOn].seat_list:
                if seat == self.frames[SelectAddOn].select_seat.get():
                    print("del")
                    self.frames[SelectAddOn].seat_list.remove(seat)
                    break
            seat_menu = self.frames[SelectAddOn].seat_om["menu"]
            seat_menu.delete(0, "end")
            for seat in self.frames[SelectAddOn].seat_list:
                seat_menu.add_command(label=seat, command=lambda value=seat: self.frames[SelectAddOn].select_seat.set(value))
                self.frames[SelectAddOn].select_seat.set("Please select")

            self.frames[SelectAddOn].FastTrack.set(add_on.json()['package'][0][0]['_fasttrack']) 
            self.frames[SelectAddOn].Insurance.set(add_on.json()['package'][0][0]['_insurance'])
            self.frames[SelectAddOn].Lounge.set(add_on.json()['package'][0][0]['_lounge'])

            self.frames[SelectAddOn].Deaf.set(add_on.json()['package'][0][1]['_deaf'])
            self.frames[SelectAddOn].Blind.set(add_on.json()['package'][0][1]['_blind'])
            self.frames[SelectAddOn].Monk.set(add_on.json()['package'][0][1]['_monk']) 
            self.frames[SelectAddOn].Nun.set(add_on.json()['package'][0][1]['_nun']) 
            self.frames[SelectAddOn].Wheelchair.set(add_on.json()['package'][0][1]['_wheelchair']) 
            self.frames[SelectAddOn].Alone_kid.set(add_on.json()['package'][0][1]['_alonekid'])

            self.frames[SelectAddOn].baggage.set(add_on.json()['package'][0][2]['_extra_bag']) 

            self.frames[SelectAddOn].meal.set(add_on.json()['meal'][0])

            self.frames[SelectAddOn].Special_baggage.set(self.frames[SelectAddOn].special_baggage_list[0])
    
    def finish_add_on(self):
        payload = {
                    "Booking ID": data['Booking ID'],
                    "Origin airport":data['Origin airport'],
                    "Destination airport":data['Destination airport'],
                    "Date depart":data['Date depart'],
                    "select_seat": self.frames[SelectAddOn].select_seat.get(),
                    "FastTrack": self.frames[SelectAddOn].FastTrack.get(),
                    "Insurance": self.frames[SelectAddOn].Insurance.get(),
                    "Lounge": self.frames[SelectAddOn].Lounge.get(),
                    "Deaf": self.frames[SelectAddOn].Deaf.get(),
                    "Blind": self.frames[SelectAddOn].Blind.get(),
                    "Nun": self.frames[SelectAddOn].Nun.get(),
                    "Monk": self.frames[SelectAddOn].Monk.get(),
                    "Wheelchair": self.frames[SelectAddOn].Wheelchair.get(),
                    "Alone_kid": self.frames[SelectAddOn].Alone_kid.get(),
                    "baggage": self.frames[SelectAddOn].baggage.get(),
                    "meal": self.frames[SelectAddOn].meal.get(),
                    "meal_amount" : self.frames[SelectAddOn].meal_amount.get(),
                    "Special_baggage": self.frames[SelectAddOn].Special_baggage.get(),
                    "Name" : self.frames[SelectAddOn].name_passenger.get()
                    } 
        response = requests.post(str(API_CREATE_TICKET+data["Flight name"]),json=payload)
        if response.ok:
            row = 1
            ticket_summary = requests.post(API_TICKET_SUMMARY,json=data).json()
            for ticket in ticket_summary:
                for key,value in ticket.items():
                    tk.Label(self.frames[PaymentSummary],text=str(key+" "+value)).grid(row=row,column=0, sticky='W')
                    row += 1
            
            sum_price = requests.post(API_SUM_PRICE,json=data).json()
            tk.Label(self.frames[PaymentSummary],text="Payment info").grid(row=0,column=0, sticky='E')
            tk.Label(self.frames[PaymentSummary],text="Adult price: " + str(sum_price["Flight price"][0]) + "Baht").grid(row=1,column=1, sticky='E')
            tk.Label(self.frames[PaymentSummary],text="Child price: " + str(sum_price["Flight price"][1]) + "Baht").grid(row=2,column=1, sticky='E')
            tk.Label(self.frames[PaymentSummary],text="Infant price: " + str(sum_price["Flight price"][2]) + "Baht").grid(row=3,column=1, sticky='E')

            tk.Label(self.frames[PaymentSummary],text="Seat price: " + str(sum_price["Seat price"]) + "Baht").grid(row=4,column=1, sticky='E')
            tk.Label(self.frames[PaymentSummary],text="Add on price: " + str(sum_price["Add on price"]) + "Baht").grid(row=5,column=1, sticky='E')
            self.frames[PaymentSummary].total_price.config(text = "Total price: " + str(sum_price["Total price"]) + "Baht")

            payment_type = requests.get(API_PAYMENT_TYPE).json()
            tk.OptionMenu(self.frames[PaymentSummary],self.frames[PaymentSummary].payment_type,*payment_type).grid(row=8, column=1)

            self.frames[SelectAddOn].forget()
            self.frames[PaymentSummary].tkraise()
            self.frames[PaymentSummary].pack(padx = 100, pady = 50)

    def submit_code(self,promotion_code):
        payload = { 
                    "Origin airport" : data["Origin airport"],
                    "Date depart" : data["Date depart"],
                    "Flight name" : data["Flight name"],
                    "Booking ID" : data["Booking ID"],
                    "Promotion code" : promotion_code
                    }
        response = requests.post(API_PROMOTION,json=payload)
        if response.ok:
            if response.json() == "Not Found":
                messagebox.showerror("Add promotion",response.json())
            elif response.json() == "Can only use 1 code":
                messagebox.showerror("Add promotion",response.json())
            else:
                self.frames[PaymentSummary].total_price.config(text = "Total price: " + str(response.json()) + "Baht")

    def submit_payment_type(self,payment_type):
        payment_type_list = requests.get(API_PAYMENT_TYPE).json()
        if payment_type == payment_type_list[0]:
            self.frames[PaymentSummary].forget()
            self.frames[CreditPayment].tkraise()
            self.frames[CreditPayment].pack(padx = 100, pady = 50)
        elif payment_type == payment_type_list[1]:
            self.frames[PaymentSummary].forget()
            self.frames[QRPayment].tkraise()
            self.frames[QRPayment].pack(padx = 100, pady = 50)
        elif payment_type == payment_type_list[2]:
            self.frames[PaymentSummary].forget()
            self.frames[CounterServicePayment].tkraise()
            self.frames[CounterServicePayment].pack(padx = 100, pady = 50)
        else:
            messagebox.showerror("Error","Please select payment type")

    def qr_submit(self):
        payload = { 
                    "Origin airport" : data["Origin airport"],
                    "Date depart" : data["Date depart"],
                    "Flight name" : data["Flight name"],
                    "Booking ID" : data["Booking ID"],
                    "Phone number" : self.frames[QRPayment].phone_number.get()
                    }
        response = requests.post(API_QR_CODE,json=payload)
        if response.ok:
            self.frames[QRPayment].forget()
            self.show_ticket()
    
    def credit_submit(self):
        payload = { 
                    "Origin airport" : data["Origin airport"],
                    "Date depart" : data["Date depart"],
                    "Flight name" : data["Flight name"],
                    "Booking ID" : data["Booking ID"],
                    "Card number" : self.frames[CreditPayment].card_number.get(),
                    "Expired date" : self.frames[CreditPayment].expired_date.get(),
                    "Card holder" : self.frames[CreditPayment].card_holder.get(),
                    "CCV" : self.frames[CreditPayment].ccv.get()
                    }
        response = requests.post(API_CREDIT_CARD,json=payload)
        if response.ok:
            self.frames[CreditPayment].forget()
            self.show_ticket()
    
    def counter_submit(self):
        payload = { 
                    "Origin airport" : data["Origin airport"],
                    "Date depart" : data["Date depart"],
                    "Flight name" : data["Flight name"],
                    "Booking ID" : data["Booking ID"],
                    "Phone number" : self.frames[CounterServicePayment].phone_number.get()
                    }
        response = requests.post(API_COUNTER,json=payload)
        if response.ok:
            self.frames[CounterServicePayment].forget()
            self.show_ticket()

    def show_ticket(self):
        tk.Label(self.frames[ShowTicket],text="Booking ID: "+ str(data["Booking ID"])).grid(row=0,column=0)

        response = requests.post(str(API_FLIGHT_DETAIL+data["Flight name"]),json=data)
        if response.ok:
            flight_data = response.json()
            flight_detail = str("Flight name: " + flight_data["Name"] + "  " + "Origin Airport: " + flight_data["Origin Airport"] + "  " + "Time Depart: " + flight_data["Time Depart"] + "\n" +
                                "Aircraft name: " + flight_data["Aircraft"] + "  " + "Destination Airport: " + flight_data["Destination Airport"] + "  " + "Time Arrive: " + flight_data["Time Arrive"] + "\n" +
                                "Flight Duration: " + str(flight_data["Flight Duration"]) + " minute  " + "Date Depart: " + flight_data["Date Depart"] + "\n")
            tk.Label(self.frames[ShowTicket],text=flight_detail).grid(row=1,column=0)
        
        ticket_summary = requests.post(API_TICKET_SUMMARY,json=data).json()
        passenger_list = []
        for ticket in ticket_summary:
            key_list = []
            for key in ticket.keys():
                key_list.append(key)
            passenger_list.append(key_list[0])
        passenger_str = ",".join(passenger_list)

        tk.Label(self.frames[ShowTicket],text="Passenger list").grid(row=2,column=0)
        tk.Label(self.frames[ShowTicket],text=passenger_str).grid(row=3,column=0)
        tk.Label(self.frames[ShowTicket],text="Check-in airport counter").grid(row=4,column=0)
        tk.Label(self.frames[ShowTicket],text="Please refer to the booking number and prepare a valid").grid(row=5,column=0)
        tk.Label(self.frames[ShowTicket],text="photo ID ready for varification upon check-in.").grid(row=6,column=0)
        tk.Label(self.frames[ShowTicket],text="Check-in counter opens: 2 hours before flight departure").grid(row=7,column=0)
        tk.Label(self.frames[ShowTicket],text="Check-in counter closes: 30 minutes before flight departure").grid(row=8,column=0)
        self.frames[ShowTicket].tkraise()
        self.frames[ShowTicket].pack(padx = 100, pady = 50)

class StartMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.adminlogin = tk.Button(self,text="Admin login", bg="green",command= lambda: controller.login_page())
        self.adminlogin.grid(row=0,column=0, ipadx=10, ipady=5)
        self.flight_book = tk.Button(self,text="Booking ticket", bg="green",command= lambda: controller.search_page())
        self.flight_book.grid(row=1,column=0, ipadx=5, ipady=5)

        self.pack(padx = 100, pady = 10)

class AdminLoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.username_lable = tk.Label(self, text = "Username: ").grid(row=0,column=0, padx=10, ipady=5, sticky='E')
        self.username_entry = tk.Entry(self, textvariable=self.username, width=12, justify="left").grid(row=0, column=1, padx=10)
        self.username_lable = tk.Label(self, text = "Password: ").grid(row=1,column=0, padx=10, ipady=5, sticky='E')
        self.username_entry = tk.Entry(self, textvariable=self.password, width=12, justify="left").grid(row=1, column=1, padx=10)
        self.username_entry = tk.Button(self, text=" LOGIN ", bg="green", command= lambda: controller.login()).grid(row=2, column=0, columnspan=2)      

        self.pack(padx = 100, pady = 10)

class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # create flight
        self.name = tk.StringVar()
        self.duration = tk.IntVar()
        self.depart = tk.StringVar()
        self.arrive = tk.StringVar()
        self.international = tk.BooleanVar()

        tk.Label(self, text = "Name: ").grid(row=0,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.name, width=12, justify="left").grid(row=0, column=1, padx=10)
        tk.Label(self, text = "Flight Duration").grid(row=1,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.duration, width=12, justify="left").grid(row=1, column=1, padx=10)
        self.showIndicator = True
        tk.Label(self, text = "International").grid(row=2,column=0, padx=10, ipady=5, sticky='E')
        tk.Radiobutton(self,text="True",value=1,variable=self.international,indicatoron=self.showIndicator,command=lambda: controller.inter_select()).grid(row=2, column=1, padx=10)
        tk.Radiobutton(self,text="False",value=0,variable=self.international,indicatoron=self.showIndicator,command=lambda: controller.inter_select()).grid(row=2, column=2, padx=10)
        tk.Label(self, text = "Depart Airport").grid(row=3,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.depart, width=12, justify="left").grid(row=3, column=1, padx=10)
        tk.Label(self, text = "Arrive Airport").grid(row=4,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.arrive, width=12, justify="left").grid(row=4, column=1, padx=10)
        tk.Button(self, text=" SUBMIT ", bg="green",command=lambda: controller.create_flight()).grid(row=5, column=0, columnspan=2)

        #create flight instance
        self.flight = tk.StringVar()
        self.date = tk.StringVar()
        self.time_depart = tk.StringVar()
        self.time_arrive = tk.StringVar()
        self.aircraft = tk.StringVar()
        self.depart_airport = tk.StringVar()
        self.price = tk.DoubleVar()

        tk.Label(self, text = "Depart Airport").grid(row=6,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.depart_airport, width=12, justify="left").grid(row=6, column=1, padx=10)
        tk.Label(self, text = "Flight ").grid(row=7,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.flight, width=12, justify="left").grid(row=7, column=1, padx=10)
        tk.Label(self, text = "Date").grid(row=8,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.date, width=12, justify="left").grid(row=8, column=1, padx=10)
        tk.Label(self, text = "Time Depart").grid(row=9,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.time_depart, width=12, justify="left").grid(row=9, column=1, padx=10)
        tk.Label(self, text = "Time Arrive").grid(row=10,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.time_arrive, width=12, justify="left").grid(row=10, column=1, padx=10)
        tk.Label(self, text = "Aircraft").grid(row=11,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.aircraft, width=12, justify="left").grid(row=11, column=1, padx=10)
        tk.Label(self, text = "Price").grid(row=12,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.price, width=12, justify="left").grid(row=12, column=1, padx=10)
        tk.Button(self, text=" SUBMIT ", bg="green", command=lambda: controller.create_flight_instance()).grid(row=13, column=0, columnspan=2)   

        #edit flight instance
        self.depfedit = tk.StringVar()
        self.datefedit = tk.StringVar()
        self.flightfedit = tk.StringVar()
        self.edit_date = tk.StringVar()
        self.edit_time_depart = tk.StringVar()
        self.edit_time_arrive = tk.StringVar()
        self.edit_price = tk.DoubleVar()

        tk.Label(self, text = "Depart Airport").grid(row=0,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.depfedit, width=12, justify="left").grid(row=0, column=4, padx=10)
        tk.Label(self, text = "Date ").grid(row=1,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.datefedit, width=12, justify="left").grid(row=1, column=4, padx=10)
        tk.Label(self, text = "Flight").grid(row=2,column=3, padx=18, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.flightfedit, width=12, justify="left").grid(row=2, column=4, padx=10)
        tk.Label(self, text = "Edit Date").grid(row=3,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.edit_date, width=12, justify="left").grid(row=3, column=4, padx=10)
        tk.Label(self, text = "Edit Time Depart").grid(row=4,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.edit_time_depart, width=12, justify="left").grid(row=4, column=4, padx=10)
        tk.Label(self, text = "Edit Time Arrive").grid(row=5,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.edit_time_arrive, width=12, justify="left").grid(row=5, column=4, padx=10)
        tk.Label(self, text = "Edit Price").grid(row=6,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.edit_price, width=12, justify="left").grid(row=6, column=4, padx=10)
        tk.Button(self, text=" EDIT ", bg="green", command=lambda: controller.edit_flight_instance()).grid(row=7, column=3, columnspan=2)

        #cancel flight instance
        self.depfcancel = tk.StringVar()
        self.datefcancel = tk.StringVar()
        self.flightfcancel = tk.StringVar()

        tk.Label(self, text = "Depart Airport").grid(row=8,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.depfcancel, width=12, justify="left").grid(row=8, column=4, padx=10)
        tk.Label(self, text = "Date ").grid(row=9,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.datefcancel, width=12, justify="left").grid(row=9, column=4, padx=10)
        tk.Label(self, text = "Flight").grid(row=10,column=3, padx=18, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.flightfcancel, width=12, justify="left").grid(row=10, column=4, padx=10)
        tk.Button(self, text=" Cancel ", bg="green", command=lambda: controller.cancel_flight_instance()).grid(row=11, column=3, columnspan=2)

        #change seat
        self.booking_id = tk.StringVar()
        self.depart_airportfseat = tk.StringVar()
        self.date_departfseat = tk.StringVar()
        self.flightfseat = tk.StringVar()
        self.seat = tk.StringVar()
        self.edit_seat = tk.StringVar()

        tk.Label(self, text = "Booking ID").grid(row=12,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.booking_id, width=12, justify="left").grid(row=12, column=4, padx=10)
        tk.Label(self, text = "Depart Airport").grid(row=13,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.depart_airportfseat, width=12, justify="left").grid(row=13, column=4, padx=10)
        tk.Label(self, text = "Date").grid(row=14,column=3, padx=18, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.date_departfseat, width=12, justify="left").grid(row=14, column=4, padx=10)
        tk.Label(self, text = "Flight").grid(row=15,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.flightfseat, width=12, justify="left").grid(row=15, column=4, padx=10)
        tk.Label(self, text = "Seat").grid(row=16,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.seat, width=12, justify="left").grid(row=16, column=4, padx=10)
        tk.Label(self, text = "Edit Seat").grid(row=17,column=3, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.edit_seat, width=12, justify="left").grid(row=17, column=4, padx=10)
        tk.Button(self, text=" Submit ", bg="green", command=lambda: controller.change_seat()).grid(row=18, column=3, columnspan=2)

        #add promotion
        self.promotion_code = tk.StringVar()
        self.discount = tk.IntVar()

        tk.Label(self, text = "Promotion Code").grid(row=14,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.depfedit, width=12, justify="left").grid(row=14, column=1, padx=10)
        tk.Label(self, text = "Discount").grid(row=15,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self, textvariable=self.datefedit, width=12, justify="left").grid(row=15, column=1, padx=10)
        tk.Button(self, text=" Submit ", bg="green", command=lambda: controller.add_promotion(self)).grid(row=16, column=0, columnspan=2)

        self.pack(padx = 100, pady = 10)

class SearchFlight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #select origin airport
        self.OAP_list = ["-"]
        self.selectOAP = tk.StringVar(self)
        self.selectOAP.set("Select airport")

        tk.Label(self, text = "Select origin airport").grid(row=0,column=0,columnspan=2, padx=10, ipady=5, sticky='W')
        self.oap_om = tk.OptionMenu(self,self.selectOAP,*self.OAP_list)
        self.oap_om.grid(row=0,column=2,columnspan=2)
        tk.Button(self,text="Submit", bg="green",command= lambda: controller.oap_submit(self.selectOAP.get())).grid(row=0,column=4,columnspan=2)

        #select destination airport
        self.DAP_list = ["-"]
        self.selectDAP = tk.StringVar(self)
        self.selectDAP.set("Select airport")

        tk.Label(self, text = "Select Destination airport").grid(row=1,column=0,columnspan=2, padx=10, ipady=5, sticky='W')
        self.dap_om = tk.OptionMenu(self,self.selectDAP,*self.DAP_list)
        self.dap_om.grid(row=1,column=2,columnspan=2)
        tk.Button(self,text="Submit", bg="green",command= lambda: controller.dap_submit(self.selectDAP.get())).grid(row=1,column=4,columnspan=2)

        #select date
        self.date_list = ["-"]
        self.selectdate = tk.StringVar(self)
        self.selectdate.set("Select Date")
        self.adult = tk.IntVar(self)
        self.child = tk.IntVar(self)
        self.infant = tk.IntVar(self)

        tk.Label(self, text = "Select Date").grid(row=2,column=0,columnspan=2, padx=10, ipady=5, sticky='W')
        self.date_om = tk.OptionMenu(self,self.selectdate,*self.date_list)
        self.date_om.grid(row=2,column=2,columnspan=2, sticky='W')
        tk.Label(self, text = "Adult").grid(row=3,column=0, padx=10, ipady=5, sticky='E')
        tk.Entry(self,textvariable=self.adult,width=3,justify="left").grid(row=3,column=1, sticky='W')
        tk.Label(self, text = "Child").grid(row=3,column=2, sticky='E')
        tk.Entry(self,textvariable=self.child,width=3,justify="left").grid(row=3,column=3, sticky='W')
        tk.Label(self, text = "Infant").grid(row=3,column=4, sticky='E')
        tk.Entry(self,textvariable=self.infant,width=3,justify="left").grid(row=3,column=5, sticky='W')
        tk.Button(self,text="Search", bg="green",command= lambda: controller.date_submit(self.selectdate.get(),self.adult.get(),self.child.get(),self.infant.get())).grid(row=4,column=2,columnspan=2)
        self.pack(padx = 100, pady = 10)

class SelectFlight(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.flight_list = ["-"]
        self.package_list = ["-"]
        self.select_flight = tk.StringVar(self)
        self.select_package = tk.StringVar(self)
        
        self.pack(padx = 100, pady = 10)

class PassengerInfo(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.adult_num = 0
        self.child_num = 0
        self.infant_num = 0

        self.select_passenger_type = tk.StringVar()
        self.select_passenger_title = tk.StringVar()
        self.select_adult_list = tk.StringVar()
        self.name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.date_of_birth = tk.StringVar()

        self.phon_number = tk.StringVar()
        self.phon_number.set("")
        self.email = tk.StringVar()
        self.email.set("")
        self.national = tk.StringVar()
        self.national.set("")
        self.country_residence = tk.StringVar()
        self.country_residence.set("")
        self.passport_number = tk.StringVar()
        self.passport_number.set("")
        self.issued_by = tk.StringVar()
        self.issued_by.set("")
        self.passport_exp_date = tk.StringVar()
        self.passport_exp_date.set("")

class SelectAddOn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.adult_num = 0
        self.child_num = 0

        self.name_passenger = tk.StringVar()
        self.select_seat = tk.StringVar()
        self.FastTrack = tk.IntVar()
        self.Insurance = tk.IntVar()
        self.Lounge = tk.IntVar()
        self.Monk = tk.IntVar()
        self.Blind = tk.IntVar()
        self.Deaf = tk.IntVar()
        self.Nun = tk.IntVar()
        self.Wheelchair = tk.IntVar()
        self.Alone_kid = tk.IntVar()
        self.baggage = tk.IntVar()
        self.meal = tk.StringVar()
        self.meal_amount = tk.IntVar()
        self.Special_baggage = tk.StringVar()

        self.meal_number = [1,2,3]
        self.baggage_size = [7,15,20,25,30]
        self.special_baggage_list = ['No selection','Bicycle',20 ,25 ,30 ]
        self.seat_list = []
        self.showIndicator = True

        self.name = tk.Label(self, text="")
        self.name.grid(row=0, column=0, padx=10, ipady=5, sticky='E')

        tk.Label(self, text="Select seat").grid(row=1, column=0, padx=10, ipady=5, sticky='E')
        self.seat_om = tk.OptionMenu(self,self.select_seat,"")
        self.seat_om.config(width=15)
        self.seat_om.grid(row=1,column=1)

        tk.Label(self, text="Select add on").grid(row=2, column=0, padx=10, ipady=5, sticky='E')
        tk.Label(self, text="Extra service").grid(row=3, column=0, padx=10, ipady=5, sticky='E')
        tk.Radiobutton(self, text="on",value=1,variable=self.FastTrack,indicatoron=self.showIndicator).grid(row=4, column=1, padx=10, ipady=5)
        tk.Radiobutton(self, text="off",value=0,variable=self.FastTrack,indicatoron=self.showIndicator).grid(row=4, column=2, padx=10, ipady=5)
        tk.Radiobutton(self, text="on",value=1,variable=self.Insurance,indicatoron=self.showIndicator).grid(row=4, column=4, padx=10, ipady=5)
        tk.Radiobutton(self, text="off",value=0,variable=self.Insurance,indicatoron=self.showIndicator).grid(row=4, column=5, padx=10, ipady=5)
        tk.Radiobutton(self, text="on",value=1,variable=self.Lounge,indicatoron=self.showIndicator).grid(row=4, column=7, padx=10, ipady=5)
        tk.Radiobutton(self, text="off",value=0,variable=self.Lounge,indicatoron=self.showIndicator).grid(row=4, column=8, padx=10, ipady=5)

        tk.Label(self, text="Special assistance").grid(row=5, column=0, padx=10, ipady=5, sticky='E')
        tk.Radiobutton(self, text="on",value=1,variable=self.Deaf,indicatoron=self.showIndicator).grid(row=6, column=1, padx=10, ipady=5)
        tk.Radiobutton(self, text="off",value=0,variable=self.Deaf,indicatoron=self.showIndicator).grid(row=6, column=2, padx=10, ipady=5)
        tk.Radiobutton(self, text="on",value=1,variable=self.Blind,indicatoron=self.showIndicator).grid(row=6, column=4, padx=10, ipady=5)
        tk.Radiobutton(self, text="off",value=0,variable=self.Blind,indicatoron=self.showIndicator).grid(row=6, column=5, padx=10, ipady=5)
        tk.Radiobutton(self, text="on",value=1,variable=self.Monk,indicatoron=self.showIndicator).grid(row=6, column=7, padx=10, ipady=5)
        tk.Radiobutton(self, text="off",value=0,variable=self.Monk,indicatoron=self.showIndicator).grid(row=6, column=8, padx=10, ipady=5)
        tk.Radiobutton(self, text="on",value=1,variable=self.Nun,indicatoron=self.showIndicator).grid(row=7, column=1, padx=10, ipady=5)
        tk.Radiobutton(self, text="off",value=0,variable=self.Nun,indicatoron=self.showIndicator).grid(row=7, column=2, padx=10, ipady=5)
        tk.Radiobutton(self, text="on",value=1,variable=self.Wheelchair,indicatoron=self.showIndicator).grid(row=7, column=4, padx=10, ipady=5)
        tk.Radiobutton(self, text="off",value=0,variable=self.Wheelchair,indicatoron=self.showIndicator).grid(row=7, column=5, padx=10, ipady=5)
        tk.Radiobutton(self, text="on",value=1,variable=self.Alone_kid,indicatoron=self.showIndicator).grid(row=7, column=7, padx=10, ipady=5)
        tk.Radiobutton(self, text="off",value=0,variable=self.Alone_kid,indicatoron=self.showIndicator).grid(row=7, column=8, padx=10, ipady=5)

        tk.Label(self, text="Baggage").grid(row=8, column=0, padx=10, ipady=5, sticky='E')
        self.bagage_om = tk.OptionMenu(self,self.baggage,*self.baggage_size)
        self.bagage_om.config(width=15)
        self.bagage_om.grid(row=8,column=1)

        tk.Label(self, text="Meal").grid(row=9, column=0, padx=10, ipady=5, sticky='E')
        self.meal_type_om = tk.OptionMenu(self,self.meal,"")
        self.meal_type_om.config(width=15)
        self.meal_type_om.grid(row=9,column=1)

        tk.Label(self, text="Amount").grid(row=9, column=2, padx=10, ipady=5, sticky='E')
        self.meal_amount_om = tk.OptionMenu(self,self.meal_amount,*self.meal_number)
        self.meal_amount_om.config(width=15)
        self.meal_amount_om.grid(row=9,column=3)

        tk.Label(self, text="Special baggage").grid(row=10, column=0, padx=10, ipady=5, sticky='E')
        self.special_baggage_om = tk.OptionMenu(self,self.Special_baggage,*self.special_baggage_list)
        self.special_baggage_om.config(width=15)
        self.special_baggage_om.grid(row=10,column=1)

        self.button = tk.Button(self, text="Next",bg="green", command= lambda: controller.next_add_on())
        self.button.grid(row=11, column=3, columnspan=2)
        tk.Button(self, text="Back",bg="green", command= lambda: controller.back_to_passenger()).grid(row=11, column=2)

class PaymentSummary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.total_price = tk.Label(self,text="")
        self.total_price.grid(row=6,column=1, sticky='E')
        self.promotion_code = tk.StringVar()
        self.payment_type = tk.StringVar()
        self.payment_type.set("Plaese select")
        tk.Entry(self, textvariable=self.promotion_code, width=12).grid(row=7, column=1, padx=10)
        tk.Button(self,text= "Add code",command=lambda: controller.submit_code(self.promotion_code.get())).grid(row=7, column=2, sticky='E')
        tk.Button(self,text= "Submit",command=lambda: controller.submit_payment_type(self.payment_type.get())).grid(row=8, column=2, sticky='E')

        self.pack(padx = 100, pady = 10)

class QRPayment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.phone_number = tk.StringVar()

        tk.Label(self,text="1. Key *481*111# Press Call on your Mobile Phone").grid(row=0,column=0,columnspan=2)
        tk.Label(self,text="2. Receive Notification SMS").grid(row=1,column=0,columnspan=2)
        tk.Label(self,text="3. Fill up Mobile Phone No. from Step 1 on below box to confirm SMS").grid(row=2,column=0,columnspan=2)
        tk.Label(self,text="4. Open your Mobile Banking Application to Scan QR Payment").grid(row=3,column=0,columnspan=2)
        tk.Entry(self,textvariable=self.phone_number,width=12).grid(row=4,column=0, sticky='E')
        tk.Button(self,text="Submit",command= lambda: controller.qr_submit()).grid(row=4,column=1, sticky='W')
        self.photo = tk.PhotoImage(file="qrcode.png")
        tk.Button(self, image=self.photo,borderwidth=0).grid(row=5,column=0,columnspan=2)

        self.pack(padx = 100, pady = 10)

class CounterServicePayment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.phone_number = tk.StringVar()

        tk.Label(self,text="1. Key *481*111# Press Call on your Mobile Phone").grid(row=0,column=0,columnspan=2)
        tk.Label(self,text="2. Receive Notification SMS").grid(row=1,column=0,columnspan=2)
        tk.Label(self,text="3. Fill up Mobile Phone No. from Step 1 on below box to confirm SMS").grid(row=2,column=0,columnspan=2)
        tk.Entry(self,textvariable=self.phone_number,width=12).grid(row=3,column=0, sticky='E')
        tk.Button(self,text="Submit",command= lambda: controller.counter_submit()).grid(row=3,column=1, sticky='W')

        self.pack(padx = 100, pady = 10)

class CreditPayment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.card_number = tk.IntVar()
        self.expired_date = tk.StringVar()
        self.card_holder = tk.StringVar()
        self.ccv = tk.IntVar()

        tk.Label(self,text="Card number: ").grid(row=0,column=0)
        tk.Label(self,text="Expired date: ").grid(row=1,column=0)
        tk.Label(self,text="Card holder name: ").grid(row=2,column=0)
        tk.Label(self,text="ccv: ").grid(row=3,column=0)
        tk.Entry(self,textvariable=self.card_number,width=12).grid(row=0,column=1)
        tk.Entry(self,textvariable=self.expired_date,width=12).grid(row=1,column=1)
        tk.Entry(self,textvariable=self.card_holder,width=12).grid(row=2,column=1)
        tk.Entry(self,textvariable=self.ccv,width=12).grid(row=3,column=1)
        tk.Button(self,text="Submit",command= lambda: controller.credit_submit()).grid(row=4,column=0,columnspan=2)

        self.pack(padx = 100, pady = 10)

class ShowTicket(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

app = Application()
app.mainloop()

