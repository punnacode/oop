from airport import Airport,AirportCatalog,Aircraft
from add_on import PackageCatalog,Package
from aircraft import SeatType, SeatBook, AircraftSeat
from enum import Enum
from admin import Admin, Adminlist
from Passenger import Passenger, PassengerType, TitleType
from payment import Payment, PaymentType

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
for i in range(1,6):
    for j in range(97,100):
        if i<3 :
            dm254.create_seat(i,chr(j),SeatType.NORMAL)
        elif i>=3 and i<5 :
            dm254.create_seat(i,chr(j),SeatType.FRONTROW)
        else:
            dm254.create_seat(i,chr(j),SeatType.PREMIUM)

#setup passenger
PassengerA = Passenger(PassengerType.ADULT.name,TitleType.MR.name,"BOB","OK","25/09/46","Thai","Thailand","65010971","B","25/01/69","1A")
PassengerB = Passenger(PassengerType.INFANT.name,TitleType.MISS.name,"M","OK","25/12/48","Thai","Thailand","65010999","B","25/02/69","1B")
PassengerC = Passenger(PassengerType.INFANT.name,TitleType.MSTR.name,"BB","OK","25/12/60","Thai","Thailand","65010009","B","25/02/69","1C")

#Log in
admin_list = adminlist.get_list_admin()
username = str(input())
password = str(input())
for i in admin_list:
    if username == i._username and password == i._password:
        print("Log in successfully")
        break
    else: 
        print("Log in unsuccessfully")
        break

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

flight_instance = flight_instance_list[int(input())-1]


print(flight_instance)


#Edit FlightInstance
print("TYPE 1 for edit date depart / 2 for edit time depart / 3 for edit time arrive / 4 for edit price / 5 for cancel flight")
x = int(input())
if x==1:
    print("New date depart: ")
    edit_date_depart = str(input())
    Admin.edit_flight_instance(flight_instance, edit_date_depart, flight_instance.time_arrive, flight_instance.time_depart, flight_instance.price)
if x==2:
    print("New time depart: ")
    edit_time_depart = str(input())
    Admin.edit_flight_instance(flight_instance, flight_instance.date_depart, flight_instance.time_arrive, edit_time_depart, flight_instance.price)
if x==3:
    print("New time arrive: ")
    edit_time_arrive = str(input())
    Admin.edit_flight_instance(flight_instance, flight_instance.date_depart, edit_time_arrive, flight_instance.time_depart, flight_instance.price)
if x==4:
    print("New price: ")
    edit_price = str(input())
    Admin.edit_flight_instance(flight_instance, flight_instance.date_depart, flight_instance.time_arrive, flight_instance.time_depart, edit_price)
if x==5:
    edit_time_arrive = str(input())
    Admin.cancel_flight_instance(flight_instance)

print(flight_instance)

#show seat  
aircraft_seat = flight_instance.aircraft.get_seat(flight_instance)
for j in aircraft_seat:
    print(f'{j.seat_row}{j.seat_column}->{j.seat_type}   ',end=' ')
    if j.seat_column == aircraft_seat[-1].seat_column:
        print('\n',end='')
#select seat
seat = aircraft_seat[int(input("select seat:"))-1]
print(seat.seat_row,seat.seat_column,seat.seat_type)

#change seat
edit_seat = aircraft_seat[int(input("change to:"))-1]
Admin.change_seat(seat,edit_seat)
print(edit_seat.seat_row,edit_seat.seat_column,edit_seat.seat_type)
