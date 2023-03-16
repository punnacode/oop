class AirportCatalog:
    def __init__(self):
        self._airport = []
    def add_airport(self,airport):
        if isinstance(airport,Airport):
            self._airport.append(airport)
    def get_list_airport(self):
        return self._airport

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
    def get_flight_list(self):
        return self._flight_list
    def get_flight_instance_list(self):
        return self._flight_instance_list