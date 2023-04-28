from typing import Union

from fastapi import FastAPI
from airport import Airport,AirportCatalog,Aircraft
from add_on import PackageCatalog,Package
from aircraft import SeatType, AircraftCatalog,SeatBook
from enum import Enum
from admin import Admin, Adminlist
from flight import Flight
from ticket import Ticket,TicketCatalog
from booking import Booking
from Passenger import Passenger

## Airport instance 
airportcatalog = AirportCatalog()
AirportA = Airport("AirportA")
airportcatalog.add_airport(AirportA)
AirportB = Airport("AirportB")
airportcatalog.add_airport(AirportB)

#Admin instance
adminlist = Adminlist()
AdminA = Admin("bob", "wowza567")
AdminB = Admin("ton", "zuzu234")
adminlist.add_admin(AdminA)
adminlist.add_admin(AdminB)
selected_flight = []

## Aircraft instance
aircraftcatalog = AircraftCatalog()
dm254 = Aircraft("DM254")
aircraftcatalog.add_aircraft(dm254)
## Flight instance
AdminA.create_flight("DD405",90,False,AirportA,AirportB,)
AdminA.create_flight("DD406",90,False,AirportA,AirportB)

## FlightInstance instance
AdminA.create_flight_instance(AirportA,"DD405","2023-04-01","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance(AirportA,"DD405","2023-05-18","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance(AirportA,"DD405","2023-05-19","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance(AirportA,"DD406","2023-05-18","20.30","22.00",dm254,1000.00)

## Package instance
packagecatalog = PackageCatalog()
packagecatalog.create_package("Normal",0.00,False,False,False,7,0)
packagecatalog.create_package("X-tra",500.00,False,False,False,15,1)
packagecatalog.create_package("Max",1000.00,True,True,True,30,1)
## AircraftSeat instance
dm254.create_seat(1,"A",SeatType.NORMAL)
dm254.create_seat(10,"B",SeatType.PREMIUM)

#flight instance dummy
airport_list = airportcatalog.airport_list
depart_airport = airport_list[0]
arrive_airport_list = depart_airport.get_arrive_airport_list()
arrive_airport = arrive_airport_list[0]
date_list = depart_airport.get_date_list(arrive_airport)
date_depart = date_list[0]
flight_instance_list = depart_airport.get_flight_instance_list(arrive_airport,date_depart)
package_list = packagecatalog.get_list_package()
flight_instance  = flight_instance_list[0]
package = package_list[0]
package.get_package_detail()

#booking
bookingA = Booking(flight_instance,package,1,0,0)
A = Passenger("ADULT","MR","HELP","ME","25-09-69","Thai","Thai","102485","Thailand","2088-02-10","1A")
Aseat = SeatBook(1,"A","NORMAL",True)
ticketA = Ticket("DD405",dm254,A,"1A",True,False,False,False,False)
#A.create_booking("1","0887567894",)

#payment = booking.create_payment()

#Ticket
ticketcatalog = TicketCatalog()

app = FastAPI()

admin_list = adminlist.get_list_admin()
airport_list = airportcatalog.airport_list
aircraft_list = aircraftcatalog.get_list_aircraft()
ticket_list = ticketcatalog.get_list_ticket()

"""
flights =[
        {
        "Name":"DD405",
        "Flight Duration":90,
        "International":0,
        "Depart Airport":"AirportA",
        "Arrive Airport":"AirportB"
        }
]

flight_instances = [
    {"Flight":"DD405",
     "Date":"2023-04-01",
     "Time Depart":"18.30",
     "Time Arrive":"20.00",
     "Aircraft":"dm254",
     "Price":1000.00}
]
"""

@app.get("/")
def read_root():
    return {"Hello": "Teacher"}


@app.post("/login")
async def login(admin:dict):
    username = admin["Username"]
    password = admin["Password"]
    status = adminlist.check(username,password)
    if status:
        return {"LOGIN SUCCESSFULLY"}
    else:
        return{"LOGIN UNSUCCESSFULLY"}
            
@app.post("/flight",tags=['Flights'])
async def create_flight(flight:dict):
    username = flight["Username"]
    password = flight["Password"] 
    name = flight["Name"]
    flight_duration = flight["Flight Duration"]
    international = bool(flight["International"])
    depart_airport = flight["Depart Airport"]
    arrive_airport = flight["Arrive Airport"]

    print(type(international))
    
    for depa in airport_list:
        if depart_airport == depa._name:
            break 
    
    for arra in airport_list:
        if arrive_airport == arra._name:
            break 

    status = adminlist.check(username,password)
    if status:
        depa.create_flight(name,flight_duration,international,depa,arra)
        return {"flight is Added!"}
    else:
        return{"Cannot Add FlightInstance"}

@app.post("/flight_instance",tags=['Flight_Instances'])
async def create_flight_instance(flight_instance : dict):
    username = flight_instance["Username"]
    password = flight_instance["Password"]
    depart_airport = flight_instance["Depart Airport"]
    flight = flight_instance["Flight"]
    date = flight_instance["Date"]
    time_depart = flight_instance["Time Depart"]
    time_arrive = flight_instance["Time Arrive"]
    aircraft = flight_instance["Aircraft"]
    price = flight_instance["Price"]

    for ac in aircraft_list:
        if aircraft == ac._name:
            break 
    
    for depa in airport_list:
        if depart_airport == depa._name:
            break 
    
    status = adminlist.check(username,password)
    if status:
        depa.create_flight_instance(flight,date,time_depart,time_arrive,ac,price)
        return {"flight instance is Added!"}
    else:
        return{"Cannot Add FlightInstance"}


@app.put("/edit_flight_instance",tags=['Flight_Instances'])
async def edit_flight_instance(flight_instance:dict):
    username = flight_instance["Username"]
    password = flight_instance["Password"]
    depart_airport = flight_instance["Depart Airport"]
    date_depart = flight_instance["Date"]
    flight = flight_instance["Flight"]
    edit_date = flight_instance["Edit Date"]
    edit_time_depart = flight_instance["Edit Time Depart"]
    edit_time_arrive = flight_instance["Edit Time Arrive"]
    edit_price = flight_instance["Edit Price"]
    flightins = airportcatalog.search_flight_instance(depart_airport,date_depart,flight)
    
    for depa in airport_list:
        if depart_airport == depa._name:
            break
    
    status = adminlist.check(username,password)
    admin = adminlist.login(username,password) 
    if status:
        admin.edit_flight_instance(flightins,edit_date,edit_time_depart,edit_time_arrive,edit_price)
        return{"Edit Successfully"}


@app.delete("/cancel_flight_instance",tags=['Flight_Instances'])
async def delete_flight_instance(flight_instance:dict):
    username = flight_instance["Username"]
    password = flight_instance["Password"]
    depart_airport = flight_instance["Depart Airport"]
    date_depart = flight_instance["Date"]
    flight = flight_instance["Flight"]
    flightins = airportcatalog.search_flight_instance(depart_airport,date_depart,flight)

    status = adminlist.check(username,password)
    admin = adminlist.login(username,password)
    if status:
        admin.cancel_flight_instance(flightins)
        return{"Promotion is Added!"}
    
@app.put("/change_seat",tags=["Seat"])
async def change_seat(data:dict):
    username = data["Username"]
    password = data["Password"]
    booking_id = data["Booking ID"]
    depart_airport = data["Depart Airport"]
    date_depart = data["Date"]
    flight = data["Flight"]
    seat = data["Seat"]
    edit_seat = data["Edit Seat"]
    booking = airportcatalog.search_booking(depart_airport,date_depart,flight,booking_id)
    ticket = booking.search_ticket(flight,seat)

    status = adminlist.check(username,password)
    admin = adminlist.login(username,password)
    if status:
        admin.change_seat(booking,ticket,seat,edit_seat)
        return{"Change Successfully"}
    
@app.post("add_promotion",tags=["Promotion"])
async def add_promotion(data:dict):
    username = data["Username"]
    password = data["Password"]
    promotion_code = data["Promotion Code"]
    discount = data["Discount"]

    status = adminlist.check(username,password)
    admin = adminlist.login(username,password)
    if status:
        admin.change_seat(promotion_code,discount)
        return{"Change Successfully"}