from typing import Union

from fastapi import FastAPI
from airport import Airport,AirportCatalog
from aircraft import Aircraft,SeatType,AircraftCatalog
from add_on import PackageCatalog,Meal,MealType,Baggage,SpecialBaggage,Extraservice,SpecialAssistance
from admin import Adminlist,Admin
from payment import PaymentType,CreditCardPayment,SMSVerifyPayment,PaymentStatus
from Passenger import Passenger,TitleType
from promotion import PromotionCatalog

app = FastAPI()
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
## Aircraft instance
aircraftcatalog = AircraftCatalog()
dm254 = Aircraft("DM254")
aircraftcatalog.add_aircraft(dm254)
## Flight instance
AdminA.create_flight("DD405",90,False,AirportA,AirportB,)
AdminA.create_flight("DD406",90,False,AirportA,AirportB)
## FlightInstance instance
AdminA.create_flight_instance(AirportA,"DD405","2023-05-01","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance(AirportA,"DD405","2023-05-18","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance(AirportA,"DD405","2023-05-19","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance(AirportA,"DD406","2023-05-18","20.30","22.00",dm254,1500.00)
## Package instance
packagecatalog = PackageCatalog()
packagecatalog.create_package("Normal",0.00,False,False,False,7,0)
packagecatalog.create_package("X-tra",500.00,False,False,False,15,1)
packagecatalog.create_package("Max",1000.00,True,True,True,30,1)
## Promotion instance
promotioncatalog = PromotionCatalog()
promotioncatalog.create_promotion("1",100)
promotioncatalog.create_promotion("2",500)
promotioncatalog.create_promotion("3",1000)
## Aircraft seat
for i in range(1,6):
    for j in range(97,100):
        if i<3 :
            dm254.create_seat(i,chr(j),SeatType.NORMAL)
        elif i>=3 and i<5 :
            dm254.create_seat(i,chr(j),SeatType.FRONTROW)
        else:
            dm254.create_seat(i,chr(j),SeatType.PREMIUM)
## Test passenger
fake_passenger_1 = Passenger("ADULT","MR","Ron","Ku","2004-05-02")
fake_passenger_2 = Passenger("CHILD","MSTR","Nor","Ku","2012-05-02")
fake_passenger_3 = Passenger("ADULT","MR","Non","Ku","2003-05-02")
fake_passenger_4 = Passenger("INFANT","BOY","Ror","Ku","2022-05-02")
fake_passenger_3.add_parent(fake_passenger_4)
## Test add on
test_extraservice = Extraservice(True,True,False)
test_baggage = Baggage(20)
test_meal = Meal("Krapow",1)
test_specialbaggage = SpecialBaggage("No selection")
test_specialAssistance = SpecialAssistance(False,False,False,False,False,False)
## Test object
test_flight_instance = airportcatalog.search_flight_instance("AirportA","2023-05-18","DD405")
test_package1 = packagecatalog.get_package("Max")
test_package2 = packagecatalog.get_package("Normal")
## Test booking1
test_booking_id1 = test_flight_instance.create_booking(test_flight_instance,test_package1,1,1,0)
test_booking1 = airportcatalog.search_booking("AirportA","2023-05-18","DD405",test_booking_id1)
test_booking1.add_passenger(fake_passenger_1)
test_booking1.add_passenger(fake_passenger_2)
test_seat1 = test_booking1.create_seatbook(1,"a")
test_seat2 = test_booking1.create_seatbook(1,"b")
test_booking1.create_ticket(fake_passenger_1,test_seat1,test_extraservice,test_baggage,test_meal,test_specialbaggage,test_specialAssistance)
test_booking1.create_ticket(fake_passenger_2,test_seat2,test_extraservice,test_baggage,test_meal,test_specialbaggage,test_specialAssistance)
## Test booking2
test_booking_id2 = test_flight_instance.create_booking(test_flight_instance,test_package2,1,0,1)
test_booking2 = airportcatalog.search_booking("AirportA","2023-05-18","DD405",test_booking_id2)
test_booking2.add_passenger(fake_passenger_3)
test_booking2.add_passenger(fake_passenger_4)
test_seat3 = test_booking2.create_seatbook(2,"a")
test_booking2.create_ticket(fake_passenger_3,test_seat3,test_extraservice,test_baggage,test_meal,test_specialbaggage,test_specialAssistance)
test_booking2.create_ticket(fake_passenger_4,None,None,None,None,None,None)


admin_list = adminlist.get_list_admin()
airport_list = airportcatalog.airport_list
aircraft_list = aircraftcatalog.get_list_aircraft()

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


@app.post("/login",tags=["admin"])
async def login(admin:dict):
    username = admin["Username"]
    password = admin["Password"]
    status = adminlist.check(username,password)
    if status:
        return {"result":"LOGIN SUCCESSFULLY"}
    else:
        return{"result":"LOGIN UNSUCCESSFULLY"}
            
@app.post("/flight",tags=["admin"])
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

@app.post("/flight_instance",tags=["admin"])
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


@app.put("/edit_flight_instance",tags=["admin"])
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
    
    status = adminlist.check(username,password)
    admin = adminlist.login(username,password) 
    if status:
        admin.edit_flight_instance(flightins,edit_date,edit_time_depart,edit_time_arrive,edit_price)
        return{"Edit Successfully"}


@app.delete("/cancel_flight_instance",tags=["admin"])
async def delete_flight_instance(flight_instance:dict):
    #username = flight_instance["Username"]
    #password = flight_instance["Password"]
    depart_airport = flight_instance["Depart Airport"]
    date_depart = flight_instance["Date"]
    flight = flight_instance["Flight"]
    airport = airportcatalog.search_airport(depart_airport)
    flightins = airportcatalog.search_flight_instance(depart_airport,date_depart,flight)

    #status = adminlist.check(username,password)
    #admin = adminlist.login(username,password)
    #if status:
    AdminA.cancel_flight_instance(airport,flightins)
    return{"Cancel Successfully"}
    
@app.put("/change_seat",tags=["admin"])
async def change_seat(data:dict):
    username = data["Username"]
    password = data["Password"]
    booking_id = data["Booking ID"]
    depart_airport = data["Depart Airport"]
    date_depart = data["Date"]
    flight = data["Flight"]
    seat_row = data["Seat Row"]
    seat_column = data["Seat Column"]
    edit_seat_row = data["Edit Seat Row"]
    edit_seat_column = data["Edit Seat Column"]
    booking = airportcatalog.search_booking(depart_airport,date_depart,flight,booking_id)

    status = adminlist.check(username,password)
    admin = adminlist.login(username,password)
    if status:
        admin.change_seat(booking,seat_row,seat_column,edit_seat_row,edit_seat_column)
    return{"Change Successfully"}
    
@app.post("add_promotion",tags=["admin"])
async def add_promotion(data:dict):
    username = data["Username"]
    password = data["Password"]
    promotion_code = data["Promotion Code"]
    discount = data["Discount"]

    status = adminlist.check(username,password)
    admin = adminlist.login(username,password)
    if status:
        admin.change_seat(promotion_code,discount)
        return{"Promotion is Added!"}