from fastapi import FastAPI
from airport import Airport,AirportCatalog
from aircraft import Aircraft,SeatType
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

@app.get("/") #Check
def read_root():
    return {"Welcome": "to the Hell"}

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
