import tkinter as tk
import requests
from tkinter import messagebox

API_ENDPOINT1 = "http://127.0.0.1:8000/select_origin"
API_ENDPOINT2 = "http://127.0.0.1:8000/select_destination"
API_ENDPOINT3 = "http://127.0.0.1:8000/select_date"
API_ENDPOINT4 = "http://127.0.0.1:8000/select_flight"
API_ENDPOINT5 = "http://127.0.0.1:8000/flight_detail/"
API_ENDPOINT6 = "http://127.0.0.1:8000/package_detail/"

data = {
        "Origin airport":"",
        "Destination airport":"",
        "Date depart":"",
        "Flight name":"",
        "Package name":"",
        "Adult":0,
        "Chlid":0,
        "Infant":0
        }

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack(side = "top",fill = "both",expand = True)
        
        self.framelist = []
        self.framelist.append(SelectOriginAirport(window,self))
        self.framelist.append(SelectDestinationAirport(window,self))
        self.framelist.append(SelectDate(window,self))
        self.framelist.append(SelectFlight(window,self))
        self.framelist[3].forget()

    def oap_submit(self,airport):
        data["Origin airport"] = airport
        endpoint2_response = requests.post(API_ENDPOINT2,json=data)
        if endpoint2_response.ok:
            airport_data = endpoint2_response.json()
            self.framelist[1].airport_list.clear()
            if airport_data["Destination airport list"] == []:
                self.framelist[1].airport_list.append("-")
            else:
                for airport in airport_data["Destination airport list"]:
                    self.framelist[1].airport_list.append(airport)
            tk.OptionMenu(self.framelist[1],self.framelist[1].selectDAP,*self.framelist[1].airport_list).grid(row=0,column=2,columnspan=2)
        return
    
    def dap_submit(self,airport):
        data["Destination airport"] = airport
        endpoint3_reponse = requests.post(API_ENDPOINT3,json=data)
        if endpoint3_reponse.ok:
            date_data = endpoint3_reponse.json()
            self.framelist[2].date_list.clear()
            if date_data["Date list"] == []:
                self.framelist[2].date_list.append("-")
            else:
                for date in date_data["Date list"]:
                    self.framelist[2].date_list.append(date)
            tk.OptionMenu(self.framelist[2],self.framelist[2].selectdate,*self.framelist[2].date_list).grid(row=0,column=3,columnspan=2)
        return
    
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
            data["Chlid"] = child
            data["Infant"] = infant
            endpoint4_response = requests.post(API_ENDPOINT4,json=data)
            if endpoint4_response.ok:
                response_data = endpoint4_response.json()
                if response_data["Flight data"] == []:
                    messagebox.showinfo("Error","Flight not found")
                else:
                    flight_list = []
                    package_list = []

                    for flight in response_data["Flight data"]:
                        flight_list.append(flight[0])
                    for package in response_data["Package data"]:
                        package_list.append(package)
                    
                    self.framelist[3].select_flight.set("Select flight")
                    self.framelist[3].select_package.set("Select package")
                    tk.OptionMenu(self.framelist[3],self.framelist[3].select_flight,*flight_list).grid(row=0,column=1)
                    tk.OptionMenu(self.framelist[3],self.framelist[3].select_package,*package_list).grid(row=0,column=3)
                    tk.Label(self.framelist[3],text = "Select flight").grid(row=0,column=0)
                    tk.Label(self.framelist[3],text = "Select package").grid(row=0,column=2)
                    tk.Button(self.framelist[3],text="Submit").grid(row=0,column=4)
                    tk.Button(self.framelist[3],text="Back",command= lambda: self.back_to_search()).grid(row=0,column=5)

                    for flight_data in response_data["Flight data"]:
                        tk.Button(self.framelist[3],text=str(flight_data[0]+" "+flight_data[1]+" "+flight_data[2]),command= lambda name = flight_data[0]: self.flight_detail(name)).grid(row=row,column=0)
                        for key, value in flight_data[3].items():
                            tk.Button(self.framelist[3],text=str(key+" "+str(value)),command= lambda name = key: self.package_detail(name)).grid(row=row,column=column)
                            column += 1
                        column = 1
                        row += 1

                    self.framelist[0].forget()
                    self.framelist[1].forget()
                    self.framelist[2].forget()
                    self.framelist[3].tkraise()
                    self.framelist[3].pack(padx = 100, pady = 50)
    
    def flight_detail(self,flight_name):
        response = requests.post(str(API_ENDPOINT5+flight_name),json=data)
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
        return
    
    def package_detail(self,package_name):
        response = requests.get(str(API_ENDPOINT6+package_name))
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

    def back_to_search(self):
        for widjet in self.framelist[3].winfo_children():
            widjet.destroy()
        self.framelist[3].forget()
        self.framelist[0].tkraise()
        self.framelist[0].pack(padx = 100, pady = 50)
        self.framelist[1].tkraise()
        self.framelist[1].pack(padx = 100, pady = 50)
        self.framelist[2].tkraise()
        self.framelist[2].pack(padx = 100, pady = 50)

class SelectOriginAirport(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        endpoint1_response = requests.get(API_ENDPOINT1)
        airport_data = endpoint1_response.json()

        self.selectOAP = tk.StringVar(self)
        self.selectOAP.set("Select airport")
        self.airport_list = []
        for airport in airport_data["Origin airport list"]:
            self.airport_list.append(airport)
        
        tk.Label(self, text = "Select origin airport").grid(row=0,column=0,columnspan=2)
        tk.OptionMenu(self,self.selectOAP,*self.airport_list).grid(row=0,column=2,columnspan=2)
        tk.Button(self,text="Submit",command= lambda: controller.oap_submit(self.selectOAP.get())).grid(row=0,column=4,columnspan=2)
        self.pack(padx = 100, pady = 10)


class SelectDestinationAirport(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.airport_list = ["-"]
        self.selectDAP = tk.StringVar(self)
        self.selectDAP.set("Select airport")

        tk.Label(self, text = "Select Destination airport").grid(row=0,column=0,columnspan=2)
        tk.OptionMenu(self,self.selectDAP,*self.airport_list).grid(row=0,column=2,columnspan=2)
        tk.Button(self,text="Submit",command= lambda: controller.dap_submit(self.selectDAP.get())).grid(row=0,column=4,columnspan=2)
        self.pack(padx = 100, pady = 10)

class SelectDate(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.date_list = ["-"]
        self.selectdate = tk.StringVar(self)
        self.adult = tk.IntVar(self)
        self.child = tk.IntVar(self)
        self.infant = tk.IntVar(self)
        self.selectdate.set("Select Date")

        tk.Label(self, text = "Select Date").grid(row=0,column=0,columnspan=3)
        tk.OptionMenu(self,self.selectdate,*self.date_list).grid(row=0,column=3,columnspan=2)
        tk.Label(self, text = "Adult").grid(row=1,column=0)
        tk.Entry(self,textvariable=self.adult,width=3,justify="left").grid(row=1,column=1)
        tk.Label(self, text = "Child").grid(row=1,column=2)
        tk.Entry(self,textvariable=self.child,width=3,justify="left").grid(row=1,column=3)
        tk.Label(self, text = "Infant").grid(row=1,column=4)
        tk.Entry(self,textvariable=self.infant,width=3,justify="left").grid(row=1,column=5)
        tk.Button(self,text="Search",command= lambda: controller.date_submit(self.selectdate.get(),self.adult.get(),self.child.get(),self.infant.get())).grid(row=2,column=2,columnspan=2)
        self.pack(padx = 100, pady = 10)
class SelectFlight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.select_flight = tk.StringVar(self)
        self.select_package = tk.StringVar(self)
        self.pack(padx = 100, pady = 10)

app = Application()
app.mainloop()



