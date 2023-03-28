from flight import Flight,FlightInstance
from aircraft import Aircraft
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

    @property
    def name(self):
        return self._name
    
    def create_flight(self,name,flight_duration,international,depart_airport,arrive_airport):
        if isinstance(name,str) and isinstance(flight_duration,int) and isinstance(international,bool) and isinstance(depart_airport,Airport) and isinstance(arrive_airport,Airport):
            self._flight_list.append(Flight(name,flight_duration,international,depart_airport,arrive_airport))
        else:
            raise TypeError("Parameter type not correct")

    def create_flight_instance(self,flight_name,date_depart,time_arrive,time_depart,aircraft):
        if isinstance(flight_name,str) and isinstance(date_depart,str) and isinstance(time_arrive,str) and isinstance(time_depart,str) and isinstance(aircraft,Aircraft):
            for f in self._flight_list:
                if f.name == flight_name:
                    flight = f
                    break
            self._flight_instance_list.append(FlightInstance(flight.name,flight.flight_duration,flight.international,flight.depart_airport,flight.arrive_airport,date_depart,time_arrive,time_depart,aircraft))
        else:
            raise TypeError("Parameter type not correct")
        
    def edit_flight_instance():
        pass
    def cancel_flight_instance():
        pass
    
    def get_arrive_airport_list(self):
        arrive_airport_list = []
        for flight in self._flight_list:
            if flight.arrive_airport not in arrive_airport_list:
                arrive_airport_list.append(flight.arrive_airport)
        return arrive_airport_list

    def get_date_list(self,arrive_airport):
        date_list = []
        for flight_instance in self._flight_instance_list:
            if flight_instance.arrive_airport == arrive_airport and flight_instance.date_depart not in date_list:
                date_list.append(flight_instance.date_depart)
        return date_list
    
    def get_flight_instance_list(self,arrive_airport,date_depart):
        flight_instance_list = []
        for flight_instance in self._flight_instance_list:
            if flight_instance.arrive_airport == arrive_airport and flight_instance.date_depart == date_depart and flight_instance not in flight_instance_list:
                flight_instance_list.append(flight_instance)
        return flight_instance_list
    