from airport import Airport,AirportCatalog,Aircraft
from add_on import PackageCatalog,Package
from aircraft import SeatType,SeatBook
from enum import Enum
from booking import Booking
from Passenger import Passenger,PassengerType,TitleType
from payment import Payment,PaymentStatus,PaymentType

## Airport instance 

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
dm254.create_seat(1,"A",SeatType.NORMAL)
dm254.create_seat(10,"B",SeatType.PREMIUM)


##Search Flight(Ton)
##  input depart airport
airport_list = airportcatalog.get_list_airport()
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

##Select FlightInstance(Ton)
##  show FlightInstance,Package
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

##Show seat
aircraft_seat = flight_instance.aircraft.get_seat()

for i in aircraft_seat:
    print(i.seat_row,i.seat_column,i.seat_type)
seat = aircraft_seat[int(input())-1]

#setup passenger
PassengerA = Passenger(PassengerType.ADULT.name,TitleType.MR.name,"BOB","OK","25/09/46","Thai","Thailand","65010971","B","25/01/69")
PassengerB = Passenger(PassengerType.INFANT.name,TitleType.MISS.name,"M","OK","25/12/48","Thai","Thailand","65010999","B","25/02/69")
PassengerC = Passenger(PassengerType.INFANT.name,TitleType.MSTR.name,"BB","OK","25/12/60","Thai","Thailand","65010009","B","25/02/69")

#test add_parent
PassengerA.add_parent(PassengerB)
PassengerA.add_parent(PassengerC)

#show member
Member_of_parent = PassengerA.parent
for i,member in enumerate(Member_of_parent):
    print(f"Member{i+1}:")
    print(member)
    
#setup booking
id_of_booking = 69
num_of_passenger = Passenger.num_passenger
seatbookA = SeatBook(False,2,'A',SeatType.FRONTROW.name)
seat_booked = seatbookA.seat_booked
paymentA = Payment(PaymentType.QRCODE.name,1,id_of_booking,num_of_passenger,None,False)
payment_status = paymentA.payment_status

package_type = package.name

BookingA = PassengerA.create_booking(id_of_booking,num_of_passenger,"0922513540","A@gmail.com",seat_booked,payment_status,package_type)
flight_instance.add_booking(BookingA)


