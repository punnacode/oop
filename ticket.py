class Ticket:
    def __init__(self, flight, passenger, seatbook, extraservice, baggage, meal, specialbaggage,specialAssistance) :
        self._flight = flight
        self.seatbook = seatbook
        self._passenger = passenger
        self.extraservice = extraservice
        self.baggage = baggage
        self.meal = meal
        self.specialbaggage = specialbaggage
        self.specialAssistance = specialAssistance

    def get_ticket():
        pass

    def get_seat_book(self):
        return self.seatbook
    
    def get_meal(self):
        return self.meal


