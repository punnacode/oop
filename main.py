from airport import Airport,AirportCatalog,Aircraft
from add_on import PackageCatalog,Package
from aircraft import SeatType
from enum import Enum

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
dm254.create_seat(1,"A",SeatType.Normal)
dm254.create_seat(10,"B",SeatType.Premium)

##Search Flight(Ton)
##  input depart airport
airport_list = airportcatalog.get_list_airport()
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

##Select FlightInstance(Ton)
##  show FlightInstance
flight_instance_list = depart_airport.get_flight_instance_list(arrive_airport,date_depart)
for i in flight_instance_list:
    print(i.name , i.time_depart , i.time_arrive)
flight = flight_instance_list[int(input())-1]

##  show FlightInstance detail
print(flight)
print("")

## show Package
package_list = packagecatalog.get_list_package()
for i in package_list:
    print(i.name, i.sum_price(flight))
package = package_list[int(input())-1]

## show Package datail
package.get_package_detail()

##Show seat
aircraft_seat = flight.aircraft.get_seat()
for i in aircraft_seat:
    print(i.seat_row,i.seat_column,i.seat_type)



