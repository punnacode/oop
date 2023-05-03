class System:
    def __init__(self):
        self._airport_list = []
        self._flight_list = []
        self._flight_instance_list = []
    
    @property
    def airport_list(self):
        return self._airport_list
    @property
    def flight_list(self):
        return self._flight_list
    @property
    def flight_instance_list(self):
        return self._flight_instance_list
    
    def add_airport(self,airport):
        if isinstance(airport,Airport):
            self._airport_list.append(airport)

    def search_arrive_airport_list(self,origin_airport):
        arrive_airport_list = []
        for i in self._flight_list:
            if i.depart_airport.name == origin_airport:
                arrive_airport_list.append(i.arrive_airport)
        return arrive_airport_list
            
    def search_date_list(self,origin_airport,destination_airport):
        data_list = []
        for i in self._flight_instance_list:
            if i.arrive_airport.name == destination_airport and i.depart_airport.name == origin_airport:
                data_list.append(i.date_depart)
        return data_list
    
    def search_flight_instance_list(self,origin_airport,destination_airport,date_depart):
        flight_instance_list = []
        for i in self._flight_instance_list:
            if i.arrive_airport.name == destination_airport and i.depart_airport.name == origin_airport and i.date_depart == date_depart:
                flight_instance_list.append(i)
        return flight_instance_list
            
    def search_flight_instance(self,date_depart,flight_name):
        for i in self._flight_instance_list:
            if i.date_depart == date_depart and i.name == flight_name:
                return i
            
    def search_airport(self,airport):
        for i in self.airport_list:
            if i.name == airport:
                return i
            
    def search_booking(self,date_depart,flight_name,booking_id):
        flight_instance = self.search_flight_instance(date_depart,flight_name)
        return flight_instance.get_booking(booking_id)

class Airport:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name