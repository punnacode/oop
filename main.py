from airport import Airport,AirportCatalog,Aircraft
from aircraft import SeatType
from enum import Enum

airportcatalog = AirportCatalog()
AirportA = Airport("AirportA")
airportcatalog.add_airport(AirportA)
AirportB = Airport("AirportB")
airportcatalog.add_airport(AirportB)
dm254 = Aircraft("DM254")
AirportA.create_flight("DD405",90,False,AirportA,AirportB)
AirportA.create_flight("DD406",90,False,AirportA,AirportB)
AirportA.create_flight_instance("DD405","2023/05/18","18.30","20.00",dm254)
AirportA.create_flight_instance("DD405","2023/05/19","18.30","20.00",dm254)
AirportA.create_flight_instance("DD406","2023/05/18","20.30","22.00",dm254)
dm254.create_seat(1,"A",SeatType.Normal)
dm254.create_seat(10,"B",SeatType.Premium)

##Search Flight
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

##Select FlightInstance
##  show FlightInstance
flight_instance_list = depart_airport.get_flight_instance_list(arrive_airport,date_depart)
for i in flight_instance_list:
    print(i.name , i.time_depart , i.time_arrive)
flight = flight_instance_list[int(input())-1]

## show seat

aircraft_seat = flight.aircarft.get_seat()
for i in aircraft_seat:
    print(i.seat_row,i.seat_column,i.seat_type)



