from airport import Airport,AirportCatalog,Aircraft
from add_on import PackageCatalog,Package,MealType,Meal,Extraservice,SpecialAssistance,Baggage,SpecialBaggage
from aircraft import SeatType,SeatBook
from enum import Enum
from booking import Booking
from Passenger import Passenger,PassengerType,TitleType
from payment import Payment,PaymentStatus,PaymentType
from ticket import Ticket
import random
from fastapi import FastAPI
from admin import Adminlist,Admin

app = FastAPI()
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
## Aircraft instance
dm254 = Aircraft("DM254")
## Flight instance
AdminA.create_flight("DD405",90,False,AirportA,AirportB,)
AdminA.create_flight("DD406",90,False,AirportA,AirportB)
## FlightInstance instance
AdminA.create_flight_instance("DD405","2023-04-20","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance("DD405","2023-05-18","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance("DD405","2023-05-19","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance("DD406","2023-05-18","20.30","22.00",dm254,1500.00)
## Package instance
packagecatalog = PackageCatalog()
packagecatalog.create_package("Normal",0.00,False,False,False,7,0)
packagecatalog.create_package("X-tra",500.00,False,False,False,15,1)
packagecatalog.create_package("Max",1000.00,True,True,True,30,1)
#booking 
flight_instance = airportcatalog.search_flight_instance("AirportA","2023-05-18","DD405")
normal_package = packagecatalog.get_package("Normal")
xtra_package = packagecatalog.get_package("X-tra")
max_package = packagecatalog.get_package("Max")
booking_id1 = flight_instance.create_booking(flight_instance,normal_package,1,0,0)
booking_id2 = flight_instance.create_booking(flight_instance,xtra_package,1,1,0)
booking_id3 = flight_instance.create_booking(flight_instance,max_package,1,0,1)

"""
{
    "Origin airport":"AirportA",
    "Destination airport":"AirportB",
    "Date depart":"2023-05-18",
    "Flight name":"DD405",
    "Package name":"Max"
}
"""
for i in range(1,6):
    for j in range(97,100):
        if i<3 :
            dm254.create_seat(i,chr(j),SeatType.NORMAL)
        elif i>=3 and i<5 :
            dm254.create_seat(i,chr(j),SeatType.FRONTROW)
        else:
            dm254.create_seat(i,chr(j),SeatType.PREMIUM)

@app.get("/")
def read_root():
    return {"Welcome": "to the Hell"}

@app.post("/select_seat/{flight_name}")
async def select_seat(flight_name: str,data: dict):
    st = []
    flight_instance = airportcatalog.search_flight_instance(data["Origin airport"],data["Date depart"],flight_name)
    aircraft_seat = flight_instance.aircraft.get_seat(flight_instance)
    for i in aircraft_seat:
        st.append([i.seat_row,i.seat_column,i.seat_type.name])
    return  {
                "Seat":st
            }

@app.post("/select_add_on")
async def select_add_on(data:dict):
    extraservice =[]
    specialAssistance = []
    meal = []
    default = []

    for i in MealType:
        meal.append(i.name)
    for i in Extraservice.extraservice_dict.values():
        extraservice.append(i)
    for i in SpecialAssistance.special_assistance_dict.values():
        specialAssistance.append(i)
    
    package = packagecatalog.get_package(data['Package name'])
    default.append([package.get_extra_service(),package.get_special_assistance(),package.get_baggage(),package.get_meal(),package.get_special_baggage()])
    return  {
                "package" : default,
                "extra service" : extraservice,
                "special assistance" : specialAssistance,
                "baggage" : package.get_baggage(),
                "meal" : meal,
                "special baggage" : package.get_special_baggage()
            }

@app.post("/creat_ticket/{flight_name}")
async def creat_ticket(flight_name: str,data:dict):
    flight_instance = airportcatalog.search_flight_instance(data["Origin airport"],data["Date depart"],flight_name)
    passenger = 1
    seat = data['select_seat'].split(" ")
    print(seat)
    seatbook = SeatBook(False,seat[0],seat[1],seat[2])
    extraservice = Extraservice(bool(data['FastTrack']),bool(data['Insurance']),bool(data['Lounge']))
    baggage = Baggage(bool(data['baggage']))
    meal = Meal(data['meal'],data['meal_amount'])
    specialbaggage = SpecialBaggage(data['Special_baggage'])
    specialAssistance = SpecialAssistance(bool(data['Deaf']),bool(data['Blind']),bool(data['Nun']),bool(data['Monk']),bool(data['Wheelchair']),bool(data['Alone_kid']))
    booking = flight_instance.get_booking(data['Booking ID'])
    print(data['Booking ID'])
    # booking.create_ticket(flight_instance,passenger,seatbook, extraservice, baggage, meal, specialbaggage,specialAssistance)
    # booking.add_book_seat(seatbook)
    return{'message':'complete'}