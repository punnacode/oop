class Flight:
    def __init__(self,name,flight_duration,international,depart_airport,arrive_airport):
        self._name = name
        self._flight_duration = flight_duration
        self._international = international
        self._depart_airport = depart_airport
        self._arrive_airport = arrive_airport
    
    @property
    def name(self):
        return self._name
    @property
    def flight_duration(self):
        return self._flight_duration
    @property
    def international(self):
        return self._international
    @property
    def depart_airport(self):
        return self._depart_airport
    @property
    def arrive_airport(self):
        return self._arrive_airport

class FlightInstance(Flight):
    def __init__(self,name,flight_duration,international,depart_airport,arrive_airport,date_depart,time_arrive,time_depart):
        super().__init__(name,flight_duration,international,depart_airport,arrive_airport)
        self._date_depart = date_depart
        self._time_arrive = time_arrive
        self._time_depart = time_depart
    

    def get_seat__book_detail():
        pass
    
    @property
    def date_depart(self):
        return self._date_depart

    def get_filght_info():
        pass

    def change_seat(aircraft_seat):
        pass
