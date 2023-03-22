import airport,flight

AirportCatalog = airport.AirportCatalog()
AirportA = airport.Airport("AirportA")
AirportCatalog.add_airport(AirportA)
AirportB = airport.Airport("AirportB")
AirportCatalog.add_airport(AirportB)
dd405 = flight.Flight("DD405",90,False,AirportA,AirportB)
AirportA.add_flight(dd405)
dd405_20230518 = flight.FlightInstance("DD405",90,False,AirportA,AirportB,"2023/05/18","18.30","20.00")


airport_list = AirportCatalog.get_list_airport()
for i in airport_list:
    print(i._name)
depart_airport = airport_list[int(input())]

flight_list = depart_airport.get_flight_list()
