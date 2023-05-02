class Ticket:
    def __init__(self, flight, passenger, seatbook, extraservice, baggage, meal, specialbaggage,specialAssistance) :
        self._flight = flight
        self._seatbook = seatbook
        self._passenger = passenger
        self._extraservice = extraservice
        self._baggage = baggage
        self._meal = meal
        self._specialbaggage = specialbaggage
        self._specialAssistance = specialAssistance

    def get_ticket():
        pass

    def get_seat_book(self):
        return self._seatbook
    
    def get_meal(self):
        return self.meal
    
    def sum_price(self,package):
        package_detail = package.get_package_detail()
        add_on_price = {}
        if self._passenger.type != "INFANT":
            if package_detail["Bagage"] < self._baggage.extra_bag:
                if package_detail["Bagage"] == 7:
                    bagage_price = ((self._baggage.extra_bag - 15)*10) + 450
                else:
                    bagage_price = ((self._baggage.extra_bag - package_detail["Bagage"])*10) + 100
                add_on_price["Bagage"] = bagage_price
            if self._meal.meal_amount > 0:
                if package_detail["Meal"] != None:
                    meal_price = (self._meal.meal_amount - package_detail["Meal"]) * 150
                else:
                    meal_price = self._meal.meal_amount * 150
                add_on_price["Meal"] = meal_price
            if self._specialbaggage.special_bag != "No selection":
                if self._specialbaggage.special_bag == "Bicycle":
                    sp_bagage_price = 500
                else:
                    sp_bagage_price = ((int(self._specialbaggage.special_bag) - 20)*100) + 500
                add_on_price["Special Bagage"] = sp_bagage_price
            if self._extraservice.get_detail() != []:
                extraservice_price = 0
                for extraservice in self._extraservice.get_detail():
                    if extraservice not in package_detail["Extra service"]:
                        extraservice_price += 150
                add_on_price["Extra service"] = extraservice_price
        return add_on_price

    @property    
    def passenger(self):
        return self._passenger
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
    @property
    def seatbook(self):
        return self._seatbook
    @seatbook.setter
    def seatbook(self,new_seatbook):
        self._seatbook = new_seatbook