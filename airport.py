import flight
Flight = flight.Flight
FlightInstance = flight.FlightInstance
class AirportCatalog:
    def __init__(self):
        self._airport_list = []
    def add_airport(self,airport):
        if isinstance(airport,Airport):
            self._airport_list.append(airport)
    def get_list_airport(self):
        return self._airport_list
    def __str__(self):
        return str(self._airport_list)

class Airport:
    def __init__(self,name):
        self._name = name
        self._flight_list = []
        self._flight_instance_list = []
    def create_flight_instance():
        pass
    def edit_flight_instance():
        pass
    def cancel_flight_instance():
        pass
    def get_airport(self):
        return self._name
    
    def add_flight(self,flight):
        if isinstance(flight,Flight):
            self._flight_list.append(flight)

    def add_flight_instance(self,flight_instance):
        if isinstance(flight_instance,FlightInstance):
            self._flight_list.append(flight_instance)

    def get_arrive_airport_list(self):
        _arrive_airport_list = []
        for flight in self._flight_list:
            if flight._arrive_airport not in _arrive_airport_list:
                print(flight._arrive_airport)
                _arrive_airport_list.append(flight._arrive_airport)
        return _arrive_airport_list

    def get_flight_instance_list(self):
        return self._flight_instance_list
    