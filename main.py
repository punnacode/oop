from airport import Airport,AirportCatalog,Aircraft
from add_on import PackageCatalog,Package,MealType,Meal,Extraservice,SpecialAssistance,Baggage,SpecialBaggage
from aircraft import SeatType,SeatBook
from enum import Enum
from booking import Booking
from Passenger import Passenger,PassengerType,TitleType
from payment import Payment,PaymentStatus,PaymentType
from ticket import Ticket
import random

# Airport instance 
airportcatalog = AirportCatalog()
AirportA = Airport("AirportA")
airportcatalog.add_airport(AirportA)
AirportB = Airport("AirportB")
airportcatalog.add_airport(AirportB)
## Aircraft instance
dm254 = Aircraft("DM254")
## Flight instance
AirportA.create_flight("DD405",90,False,AirportA,AirportB)
AirportA.create_flight("DD406",90,False,AirportA,AirportB)


## FlightInstance instance
AirportA.create_flight_instance("DD405","2023-04-01","18.30","20.00",dm254,1000.00)
AirportA.create_flight_instance("DD405","2023-05-18","18.30","20.00",dm254,1000.00)
AirportA.create_flight_instance("DD405","2023-05-19","18.30","20.00",dm254,1000.00)
AirportA.create_flight_instance("DD406","2023-05-18","20.30","22.00",dm254,1000.00)
## Package instance
packagecatalog = PackageCatalog()
packagecatalog.create_package("Normal",0.00,False,False,False,7,0)
packagecatalog.create_package("X-tra",500.00,False,False,False,15,1)
packagecatalog.create_package("Max",1000.00,True,True,True,30,1)
## AircraftSeat instance
# dm254.create_seat(1,"A",SeatType.NORMAL)
# dm254.create_seat(10,"B",SeatType.PREMIUM)
for i in range(1,6):
    for j in range(97,100):
        if i<3 :
            dm254.create_seat(i,chr(j),SeatType.NORMAL)
        elif i>=3 and i<5 :
            dm254.create_seat(i,chr(j),SeatType.FRONTROW)
        else:
            dm254.create_seat(i,chr(j),SeatType.PREMIUM)

#Search Flight(Ton)
#  input depart airport
airport_list = airportcatalog.airport_list()
for i in airport_list:
    print(i.name)
depart_airport = airport_list[int(input())-1]
##  End point
##  input arrive airport
arrive_airport_list = depart_airport.get_arrive_airport_list()
for i in arrive_airport_list:
    print(i.name)
arrive_airport = arrive_airport_list[int(input())-1]
##  End point
##  input date
date_list = depart_airport.get_date_list(arrive_airport)
for i in date_list:
    print(i)

date_depart = date_list[int(input())-1]
adult_amount = int(input("Amount of adult:"))
kid_amount = int(input("Amount of kid:"))
infant_amount = int(input("Amount of infant:"))
##  End point

#Select FlightInstance(Ton)
#  show FlightInstance,Package
flight_instance_list = depart_airport.get_flight_instance_list(arrive_airport,date_depart)
for i in range(len(flight_instance_list)):
    print(flight_instance_list[i].name , flight_instance_list[i].time_depart , flight_instance_list[i].time_arrive)
    package_list = packagecatalog.get_list_package()
    for j in package_list:
        print(j.name, j.sum_price(flight_instance_list[i]))
flight_instance  = flight_instance_list[int(input())-1]
package = package_list[int(input())-1]
##  End point
##  show FlightInstance detail
print(flight_instance)
## End point
## show Package datail
package.get_package_detail()
## End point

#input passenger and Show seat/Select seat
aircraft_seat = flight_instance.aircraft.get_seat(flight_instance)
print("------------------Passenger-------------------")
adult_list = []
kid_list = []
infant_list = []
seat_book = []

for i in range(adult_amount):
    print(f'Adult{i+1}:')
    
    #show seat    
    for j in aircraft_seat:
        print(f'{j.seat_row}{j.seat_column}->{j.seat_type}   ',end=' ')
        if j.seat_column == aircraft_seat[-1].seat_column:
            print('\n',end='')
    #select seat
    seat = aircraft_seat[int(input("select seat:"))-1]
    print(seat.seat_row,seat.seat_column,seat.seat_type)
    seat_book.append(SeatBook(False,seat.seat_row,seat.seat_column,seat.seat_type))
    
    print(list(TitleType(k).name for k in range(0,7)))
    adult_list.append(Passenger(PassengerType.ADULT.name,TitleType(int(input("select adult title:"))-1).name,input("first name:"),input("last name:"),input("birth date:"),input("national:"),input("country resident:"),input("passport number:"),input("issued by:"),input("passport exp date:"),seat))
    if i == 0:
        phone_number = str(input("phone number:"))
        email = str(input("email:"))

for i in range(kid_amount):
    print(f'Kid{i+1}:')
    
    for j in aircraft_seat:
        print(f'{j.seat_row}{j.seat_column}->{j.seat_type}   ',end=' ')
        if j.seat_column == aircraft_seat[-1].seat_column:
            print('\n',end='')
    seat = aircraft_seat[int(input("select seat:"))-1]
    seat_book.append(SeatBook(False,seat.seat_row,seat.seat_column,seat.seat_type))
    
    print(list(TitleType(k).name for k in range(0,7)))
    kid_list.append(Passenger(PassengerType.CHILD.name,TitleType(int(input("select child Title:"))-1).name,input("first name:"),input("last name:"),input("birth date:"),input("national:"),input("country resident:"),input("passport number:"),input("issued by:"),input("passport exp date:"),seat))

for i in range(infant_amount):
    print(f'Infant{i+1}:')
    
    for adult in adult_list:
        print(f'{adult_list.index(adult)+1}. {adult.name}')
    select_parent = int(input("Select parent:"))-1
        
    print(list(TitleType(k).name for k in range(0,7)))
    infant_list.append(Passenger(PassengerType.INFANT.name,TitleType(int(input("select infant title:"))-1).name,input("first name:"),input("last name:"),input("birth date:"),input("national:"),input("country resident:"),input("passport number:"),input("issued by:"),input("passport exp date:"),adult_list[select_parent].seat))

    adult_list[select_parent].add_parent(infant_list[i])

#combine passsenger
passenger_list = adult_list+kid_list+infant_list


# #setup passenger
# PassengerA = Passenger(PassengerType.ADULT.name,TitleType.MR.name,"BOB","OK","25/09/46","Thai","Thailand","65010971","B","25/01/69")
# PassengerB = Passenger(PassengerType.INFANT.name,TitleType.MISS.name,"M","OK","25/12/48","Thai","Thailand","65010999","B","25/02/69")
# PassengerC = Passenger(PassengerType.INFANT.name,TitleType.MSTR.name,"BB","OK","25/12/60","Thai","Thailand","65010009","B","25/02/69")

# #test add_parent
# PassengerA.add_parent(PassengerB)
# PassengerA.add_parent(PassengerC)

# #show member
# Member_of_parent = PassengerA.parent
# for i,member in enumerate(Member_of_parent):
#     print(f"Member{i+1}:")
#     print(member)

# setup booking
id_of_booking = random.randrange(0,10000)
num_of_passenger = kid_amount+infant_amount+adult_amount
package_type = package.name
BookingA = adult_list[0].create_booking(id_of_booking,num_of_passenger,phone_number,email,seat_book,False,package_type,passenger_list)

#select add on 
for i in range(adult_amount):
    print(f'Adult:{i+1}')
    for meal in MealType:
        print (meal.name)
    meal = Meal(MealType(int(input("select meal :"))),int(input("meal amout :")))
    for extraservice in Extraservice.extraservice_dict.values():
        print (extraservice)
    extraservice = Extraservice(bool(input("FastTrack :")),bool(input("Insurance :")),bool(input("Lounge :"))) 
    for specialAssistance in SpecialAssistance.special_assistance_dict.values():
        print(specialAssistance)   
    specialAssistance = SpecialAssistance(bool(input("deaf :")),bool(input("blind :")),bool(input("monk :")),bool(input("nun :")),bool(input("wheelchair :")),bool(input("alonekid :")))
    baggage = Baggage(bool(input("extra bag :")))
    specialbaggage = SpecialBaggage(input("specail baggae :"))
    BookingA.create_ticket(flight_instance.name, adult_list[i].seat, adult_list[i].name, seat_book, extraservice, baggage, meal, specialbaggage ,specialAssistance)

for i in range(kid_amount):
    print(f'Adult:{i+1}')
    for meal in MealType:
        print (meal.name)
    meal = Meal(MealType(int(input("select meal :"))),int(input("meal amout :")))
    for extraservice in Extraservice.extraservice_dict.values():
        print (extraservice)
    extraservice = Extraservice(bool(input("FastTrack :")),bool(input("Insurance :")),bool(input("Lounge :"))) 
    for specialAssistance in SpecialAssistance.special_assistance_dict.values():
        print(specialAssistance)   
    specialAssistance = SpecialAssistance(bool(input("deaf :")),bool(input("blind :")),bool(input("monk :")),bool(input("nun :")),bool(input("wheelchair :")),bool(input("alonekid :")))
    baggage = Baggage(bool(input("extra bag :")))
    specialbaggage = SpecialBaggage(input("specail baggae :"))
    BookingA.create_ticket(flight_instance.name, kid_list[i].seat, kid_list[i].name, seat_book, extraservice, baggage, meal, specialbaggage ,specialAssistance)


# payment
paymentA = Payment(PaymentType.QRCODE.name,1,id_of_booking,num_of_passenger,None,False)
payment_status = paymentA.payment_status
flight_instance.add_booking(BookingA)


