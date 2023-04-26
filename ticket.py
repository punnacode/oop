class Ticket:
    def __init__(self, flight, aircraftseat, passenger, seatbook, extraservice, baggage, meal, specialbaggage,specialAssistance) :
        self._flight = flight
        self.seatbook = seatbook
        self._aircraft_seat = aircraftseat
        self._passenger = passenger
        self.extraservice = extraservice
        self.baggage = baggage
        self.meal = meal
        self.specialbaggage = specialbaggage
        self.specialAssistance = specialAssistance

    def get_ticket():
        pass
    
    @property    
    def flight(self):
        return self._flight

    @property
    def aircraft_seat(self):
        return self._aircraft_seat
    @aircraft_seat.setter
    def aircraft_seat(self,new_seat):
        if isinstance(new_seat, str):
            self._price = new_seat