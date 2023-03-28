from aircraft import Aircraft
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
    def __init__(self,name,flight_duration,international,depart_airport,arrive_airport,date_depart,time_arrive,time_depart,aircraft):
        super().__init__(name,flight_duration,international,depart_airport,arrive_airport)
        self._date_depart = date_depart
        self._time_arrive = time_arrive
        self._time_depart = time_depart
        self._aircraft = aircraft
        self._booking = []
    
    @property
    def date_depart(self):
        return self._date_depart
    @property
    def time_arrive(self):
        return self._time_arrive
    @property
    def time_depart(self):
        return self._time_depart    

    @property
    def aircarft(self):
        return self._aircraft

    def get_seat__book_detail():
        pass

    def get_filght_info():
        pass

    def change_seat(aircraft_seat):
        pass
