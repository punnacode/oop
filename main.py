import airport,flight

AirportCatalog = airport.AirportCatalog()
AirportA = airport.Airport("AirportA")
AirportCatalog.add_airport(AirportA)
AirportB = airport.Airport("AirportB")
AirportCatalog.add_airport(AirportB)
dd405 = flight.Flight("DD405",90,False,AirportA,AirportB)
AirportA.add_flight(dd405)
dd406 = flight.Flight("DD406",90,False,AirportA,AirportB)
AirportA.add_flight(dd406)
AirportA.create_flight_instance(dd405,"2023/05/18","18.30","20.00")
AirportA.create_flight_instance(dd405,"2023/05/19","20.30","22.00")

##Search Flight
airport_list = AirportCatalog.get_list_airport()
for i in airport_list:
    print(i.name)
depart_airport = airport_list[int(input())-1]

arrive_airport_list = depart_airport.get_arrive_airport_list()
for i in arrive_airport_list:
    print(i.name)
arrive_airport = arrive_airport_list[int(input())-1]

date_list = depart_airport.get_date_list(arrive_airport)
for i in date_list:
    print(i)
date_depart = date_list[int(input())-1]




