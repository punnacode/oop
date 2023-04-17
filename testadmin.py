from airport import Airport,AirportCatalog,Aircraft
from add_on import PackageCatalog,Package
from aircraft import SeatType
from enum import Enum
from admin import Admin, Adminlist

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
dm254 = Aircraft("DM254")
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

#Log in
admin_list = adminlist.get_list_admin()
username = str(input())
password = str(input())
for i in admin_list:
    print(i._username)
    if username == i._username and password == i._password:
        print("Log in successfully")
        break
    else: 
        print("Log in unsuccessfully")

##Search Flight
##  input depart airport
airport_list = airportcatalog.airport_list()
for i in airport_list:
    print(i.name)
depart_airport = airport_list[int(input())-1]
##  input arrive airport
arrive_airport_list = depart_airport.get_arrive_airport_list()
for i in arrive_airport_list:
    print(i.name)
arrive_airport = arrive_airport_list[int(input())-1]

##  input date
date_list = depart_airport.get_date_list(arrive_airport)
for i in date_list:
    print(i)
date_depart = date_list[int(input())-1]

##Select FlightInstance
##  show FlightInstance
flight_instance_list = depart_airport.get_flight_instance_list(arrive_airport,date_depart)
for i in flight_instance_list:
    print(i.name , i.time_depart , i.time_arrive)
flight = flight_instance_list[int(input())-1]

print(flight)

#Edit FlightInstance
print("TYPE 1 for edit date depart / 2 for edit time depart / 3 for edit time arrive / 4 for edit price / 5 for cancel flight")
x = int(input())
if x==1:
    print("New date depart: ")
    edit_date_depart = str(input())
    Admin.edit_flight_instance(flight, edit_date_depart, flight.time_arrive, flight.time_depart, flight.price)
if x==2:
    print("New time depart: ")
    edit_time_depart = str(input())
    Admin.edit_flight_instance(flight, flight.date_depart, flight.time_arrive, edit_time_depart, flight.price)
if x==3:
    print("New time arrive: ")
    edit_time_arrive = str(input())
    Admin.edit_flight_instance(flight, flight.date_depart, edit_time_arrive, flight.time_depart, flight.price)
if x==4:
    print("New price: ")
    edit_price = str(input())
    Admin.edit_flight_instance(flight, flight.date_depart, flight.time_arrive, flight.time_depart, edit_price)
if x==5:
    edit_time_arrive = str(input())
    Admin.cancel_flight_instance(flight)

print(flight)
