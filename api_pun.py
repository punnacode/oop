from typing import Union

from fastapi import FastAPI
from airport import Airport,AirportCatalog,Aircraft
from add_on import PackageCatalog,Package
from aircraft import SeatType, AircraftCatalog
from enum import Enum
from admin import Admin, Adminlist
from flight import Flight

## Airport instance 
airportcatalog = AirportCatalog()
AirportA = Airport("AirportA")
airportcatalog.add_airport(AirportA)
AirportB = Airport("AirportB")
airportcatalog.add_airport(AirportB)

#Admin instance
adminlist = Adminlist()
AdminA = Admin("bob", "wowza567",AirportA)
AdminB = Admin("ton", "zuzu234",AirportB)
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
AdminA.create_flight_instance("DD405","2023-04-01","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance("DD405","2023-05-18","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance("DD405","2023-05-19","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance("DD406","2023-05-18","20.30","22.00",dm254,1000.00)

## Package instance
packagecatalog = PackageCatalog()
packagecatalog.create_package("Normal",0.00,False,False,False,7,0)
packagecatalog.create_package("X-tra",500.00,False,False,False,15,1)
packagecatalog.create_package("Max",1000.00,True,True,True,30,1)
## AircraftSeat instance
dm254.create_seat(1,"A",SeatType.NORMAL)
dm254.create_seat(10,"B",SeatType.PREMIUM)
app = FastAPI()

admin_list = adminlist.get_list_admin()
airport_list = airportcatalog.get_list_airport()
aircraft_list = aircraftcatalog.get_list_aircraft()

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

@app.get("/")
def read_root():
    return {"Hello": "Teacher"}


@app.post("/login")
async def login(admin:dict):
    username = admin["Username"]
    password = admin["Password"]
    adminlist.login(username,password)
    return {"Login Success"}
            
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

    admin = adminlist.login(username,password)
    admin.create_flight(name,flight_duration,international,depa,arra)
    
    return {"flight is Added!"}

@app.post("/flight_instance",tags=['Flight_Instances'])
async def create_flight_instance(flight_instance : dict):
    username = flight_instance["Username"]
    password = flight_instance["Password"]
    flight = flight_instance["Flight"]
    date = flight_instance["Date"]
    time_depart = flight_instance["Time Depart"]
    time_arrive = flight_instance["Time Arrive"]
    aircraft = flight_instance["Aircraft"]
    price = flight_instance["Price"]

    for ac in aircraft_list:
        if aircraft == ac._name:
            break 
    
    admin = adminlist.login(username,password)
    admin.create_flight_instance(flight,date,time_depart,time_arrive,ac,price)

    return {"flight instance is Added!"}

@app.post("/edit_flight_instance",tags=['Flight_Instances'])
async def edit_flight_instance(data:dict):
   pass

@app.delete("/flight_instance/{flight_name}",tags=['Flight_Instances'])
async def delete_flight_instance(flight_name:str,date_depart:str,time_depart:str):
    for flight_instance in flight_instances:
        if (str(flight_instance["Flight"])) == flight_name and (str(flight_instance["Date Depart"])) == date_depart and (str(flight_instance["Time Depart"])) == time_depart :
            flight_instances.remove(flight_instance)
            return{f"flight instance {flight_name} in {date_depart} with {time_depart} has been removed"}
    return{f"This flight instance {flight_name} in {date_depart} with {time_depart} is not found"}
