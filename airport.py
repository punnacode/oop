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

    @property
    def name(self):
        return self._name
    
    def create_flight(self,name,flight_duration,international,depart_airport,arrive_airport):
        if isinstance(name,str) and isinstance(flight_duration,int) and isinstance(international,bool) and isinstance(depart_airport,Airport) and isinstance(arrive_airport,Airport):
            self._flight_list.append(Flight(name,flight_duration,international,depart_airport,arrive_airport))
        else:
            raise TypeError("Parameter type not correct")

    def create_flight_instance(self,flight,date_depart,time_arrive,time_depart):
        if isinstance(flight,Flight) and isinstance(date_depart,str) and isinstance(time_arrive,str) and isinstance(time_depart,str):
            self._flight_instance_list.append(FlightInstance(flight.name,flight.flight_duration,flight.international,flight.depart_airport,flight.arrive_airport,date_depart,time_arrive,time_depart))
        else:
            raise TypeError("Parameter type not correct")
        
    def edit_flight_instance():
        pass
    def cancel_flight_instance():
        pass
    
    def get_arrive_airport_list(self):
        _arrive_airport_list = []
        for flight in self._flight_list:
            if flight.arrive_airport not in _arrive_airport_list:
                _arrive_airport_list.append(flight.arrive_airport)
        return _arrive_airport_list

    def get_date_list(self,arrive_airport):
        _date_list = []
        for flight_instance in self._flight_instance_list:
            if flight_instance.arrive_airport == arrive_airport and flight_instance.date_depart not in _date_list:
                _date_list.append(flight_instance.date_depart)
        return _date_list
    