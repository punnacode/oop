class Ticket:
    def __init__(self, flight, passenger, extraservice, baggage, meal, specialbaggage,specialAssistance) :
        self._flight = flight
        self._passenger = passenger
        self.extraservice = extraservice
        self.baggage = baggage
        self.meal = meal
        self.specialbaggage = specialbaggage
        self.specialAssistance = specialAssistance

    def __str__(self):
        pass
    

