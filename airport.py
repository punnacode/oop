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

    def get_flight_list(self):
        return self._flight_list
    def get_flight_instance_list(self):
        return self._flight_instance_list
    