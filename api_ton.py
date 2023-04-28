from fastapi import FastAPI
from airport import Airport,AirportCatalog
from aircraft import Aircraft,SeatType,AircraftCatalog
from add_on import PackageCatalog,Meal,MealType,Baggage,SpecialBaggage,Extraservice,SpecialAssistance
from admin import Adminlist,Admin
from payment import Payment,PaymentStatus
from Passenger import Passenger

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
test_package = packagecatalog.get_package("Max")
## Test booking1
test_payment1 = Payment(PaymentStatus.COMPLETE)
test_booking_id1 = test_flight_instance.create_booking(test_payment1,test_flight_instance,test_package,1,1,0)
test_booking1 = airportcatalog.search_booking("AirportA","2023-05-18","DD405",test_booking_id1)
test_booking1.add_passenger(fake_passenger_1)
test_booking1.add_passenger(fake_passenger_2)
test_seat1 = test_booking1.create_seatbook(1,"a")
test_seat2 = test_booking1.create_seatbook(1,"b")
test_booking1.create_ticket(fake_passenger_1,test_seat1,test_extraservice,test_baggage,test_meal,test_specialbaggage,test_specialAssistance)
test_booking1.create_ticket(fake_passenger_2,test_seat2,test_extraservice,test_baggage,test_meal,test_specialbaggage,test_specialAssistance)
## Test booking2
test_payment2 = Payment(PaymentStatus.CANCEL)
test_booking_id2 = test_flight_instance.create_booking(test_payment2,test_flight_instance,test_package,1,0,1)
test_booking2 = airportcatalog.search_booking("AirportA","2023-05-18","DD405",test_booking_id2)
test_booking2.add_passenger(fake_passenger_3)
test_booking2.add_passenger(fake_passenger_4)
test_seat3 = test_booking2.create_seatbook(2,"a")
test_booking2.create_ticket(fake_passenger_3,test_seat3,test_extraservice,test_baggage,test_meal,test_specialbaggage,test_specialAssistance)

"""
Data for add flights 
{
    "Name":"DD405",
    "Flight Duration":90,
    "International":0,
    "Depart Airport":"AirportA",
    "Arrive Airport":"AirportB"
}

Data for add flight instances 
{
     Flight":"DD405",
     "Date":"2023-04-01",
     "Time Depart":"18.30",
     "Time Arrive":"20.00",
     "Aircraft":"dm254",
     "Price":1000.00
}

Data for booking flight
{
    "Origin airport":"AirportA",
    "Destination airport":"AirportB",
    "Date depart":"2023-05-18",
    "Flight name":"DD405",
    "Package name":"Max",
    "Adult":1,
    "Chlid":1,
    "Infant":1,
    "Booking ID":1
}
"""
@app.post("/login",tags=["admin"])
async def login(admin:dict):
    username = admin["Username"]
    password = admin["Password"]
    status = adminlist.check(username,password)
    if status:
        return {"LOGIN SUCCESSFULLY"}
    else:
        return{"LOGIN UNSUCCESSFULLY"}
    
@app.post("/flight",tags=["admin"])
async def create_flight(flight:dict):
    airport_list = airportcatalog.airport_list
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
    airport_list = airportcatalog.airport_list
    aircraft_list = aircraftcatalog.get_list_aircraft()
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
    airport_list = airportcatalog.airport_list
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
    
@app.delete("/cancel_flight_instance",tags=["admin"])
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
        return{"Cancel Successfully"}
    
@app.put("/change_seat",tags=["admin"])
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

@app.get("/select_origin",tags=["search flight"]) #Check
async def select_origin():
    airport_list = airportcatalog.airport_list
    oal = []
    for i in airport_list:
        oal.append(i.name)
    return {"Origin airport list": oal}

@app.post("/select_destination",tags=["search flight"]) #Check
async def select_destination(data: dict):
    arrive_airport_list = airportcatalog.search_arrive_airport_list(data["Origin airport"])
    dal = []
    for i in arrive_airport_list:
        dal.append(i.name)
    return {"Destination airport list":dal}

@app.post("/select_date",tags=["search flight"]) #Check
async def select_date(data: dict):
    date_list = airportcatalog.search_date_list(data["Origin airport"],data["Destination airport"])
    dl = []
    for i in date_list:
        dl.append(i)
    return {"Date list":dl}

@app.post("/select_flight",tags=["select flight"]) #Check
async def select_flight_instance(data: dict):
    pl = []
    fl = []
    flight_instance_list = airportcatalog.search_flight_instance_list(data["Origin airport"],data["Destination airport"],data["Date depart"])
    package_list = packagecatalog.get_list_package()
    for i in range(len(flight_instance_list)):
        pkl = {}
        for j in package_list:
            pkl[j.name]=flight_instance_list[i].sum_price(j)
        fl.append([flight_instance_list[i].name , flight_instance_list[i].time_depart , flight_instance_list[i].time_arrive,pkl])
    for i in package_list:
        pl.append(i.name)
    return {"Flight data":fl,"Package data":pl}

@app.post("/flight_detail/{flight_name}",tags=["flight detail"]) #Check
async def flight_detail(flight_name: str,data: dict):
    flight_instance = airportcatalog.search_flight_instance(data["Origin airport"],data["Date depart"],flight_name)
    return {
            "Name":flight_instance.name,
            "Aircraft":flight_instance.aircraft.name,
            "Origin Airport":flight_instance.depart_airport.name,
            "Destination Airport":flight_instance.arrive_airport.name,
            "Flight Duration":flight_instance.flight_duration,
            "Time Depart":flight_instance.time_depart,
            "Time Arrive":flight_instance.time_arrive,
            "Date Depart":flight_instance.date_depart
            }

@app.get("/package_detail/{package_name}",tags=["package detail"]) #Check
async def package_detail(package_name: str):
    package = packagecatalog.get_package(package_name)
    return {package_name: package.get_package_detail()}

@app.post("/create_booking",tags=["select flight"]) #Check
async def create_booking(data:dict):
    flight_instance = airportcatalog.search_flight_instance(data["Origin airport"],data["Date depart"],data["Flight name"])
    package = packagecatalog.get_package(data["Package name"])
    payment = Payment(PaymentStatus.WAITING)
    booking_id = flight_instance.create_booking(payment,flight_instance,package,data["Adult"],data["Chlid"],data["Infant"])
    return {"Booking ID": booking_id}
    
@app.post("/select_seat/{flight_name}",tags=["select add on"])
async def select_seat(flight_name: str,data: dict):
    st = []
    flight_instance = airportcatalog.search_flight_instance(data["Origin airport"],data["Date depart"],flight_name)
    aircraft_seat = flight_instance.aircraft.get_seat(flight_instance)
    for i in aircraft_seat:
        st.append([i.seat_row,i.seat_column,i.seat_type.name])
    return  {
                "Seat":st
            }

@app.post("/select_add_on",tags=["select add on"])
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

@app.post("/creat_ticket/{flight_name}",tags=["select add on"])
async def creat_ticket(flight_name: str,data:dict):
    passenger = 1
    extraservice = Extraservice(bool(data['FastTrack']),bool(data['Insurance']),bool(data['Lounge']))
    baggage = Baggage(bool(data['baggage']))
    meal = Meal(data['meal'],data['meal_amount'])
    specialbaggage = SpecialBaggage(data['Special_baggage'])
    specialAssistance = SpecialAssistance(bool(data['Deaf']),bool(data['Blind']),bool(data['Nun']),bool(data['Monk']),bool(data['Wheelchair']),bool(data['Alone_kid']))
    booking = airportcatalog.search_booking(data["Origin airport"],data["Date depart"],flight_name,data['Booking ID'])
    print(data['Booking ID'])
    seat = data['select_seat'].split(" ")
    print(seat)
    seatbook = booking.create_seatbook(seat[0],seat[1],)
    booking.create_ticket(passenger,seatbook, extraservice, baggage, meal, specialbaggage,specialAssistance)
    return{'message':'complete'}
