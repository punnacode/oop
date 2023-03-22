class Flight:
    def __init__(self,name,flight_duration,international,depart_airport,arrive_airport):
        self._name = name
        self._flight_duration = flight_duration
        self._international = international
        self._depart_airport = depart_airport
        self._arrive_airport = arrive_airport
    
    def get_flight():
        pass

class FlightInstance(Flight):
    def __init__(self,name,flight_duration,international,depart_airport,arrive_airport,date_depart,time_arrive,time_depart):
        super().__init__(name,flight_duration,international,depart_airport,arrive_airport)
        self._date_depart = date_depart
        self._time_arrive = time_arrive
        self._time_depart = time_depart
    

    def get_seat__book_detail():
        pass
    
    def get_date():
        pass

    def get_filght_info():
        pass

    def change_seat(aircraft_seat):
        pass
