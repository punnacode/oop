from ticket import Ticket
from payment import PaymentStatus,Payment,PaymentType
class Booking:
    ID = 1
    def __init__(self,flight_instance,package,adult,child,infant):
        self._id = Booking.ID
        self._flight = flight_instance
        self._package = package
        self._adult_num = adult
        self._kid_num = child
        self._infant_num = infant
        self._phone_number = None 
        self._email = None
        self._passenger_list = []
        self._seat_book = []
        self._ticket = []

        Booking.ID +=1

    @property
    def id(self):
        return self._id
      
    @property
    def flight_international_status(self):
        return self._flight.international
    
    @property
    def payment_status(self):
        return self._payment_status
    @property
    def seat_book(self):
        return self._seat_book
    @property
    def ticket(self):
        return self._ticket
    
    @property
    def total_passenger_num(self):
        return self._adult_num+self._kid_num+self._infant_num
    
    @property
    def passenger_list(self):
        return self._passenger_list
    
    @property
    def get_adult_list(self):
        adult_list = []
        for passenger in self._passenger_list:
            if passenger.type == "ADULT":
                adult_list.append(passenger.name)
        return adult_list
    
    @property
    def get_kid_list(self):
        kid_list = []
        for passenger in self._passenger_list:
            if passenger.type == "CHILD":
                kid_list.append(passenger.name)
        return kid_list
    
    @property
    def get_infant_list(self):
        infant_list = []
        for passenger in self._passenger_list:
            if passenger.type == "INFANT":
                infant_list.append(passenger.name)
        return infant_list
        
    @property
    def adult_num(self):
        return self._adult_num

    @property
    def kid_num(self):
        return self._kid_num

    @property
    def infant_num(self):
        return self._infant_num

    def create_ticket(self, flight, aircraftseat, passenger, seatbook, extraservice, baggage, meal, specialbaggage,specialAssistance):
        self._ticket.append(Ticket(flight, aircraftseat, passenger, seatbook, extraservice, baggage, meal, specialbaggage,specialAssistance))

    def set_num_passenger(self,adult_num,kid_num,infant_num):
        self._adult_num = adult_num
        self._kid_num = kid_num
        self._infant_num = infant_num
        return [self._adult_num,self._kid_num,self._infant_num]
    
    def add_passenger(self,passenger):
        self._passenger_list.append(passenger)
        return self._passenger_list
        
    def main_passenger_info(self,phone_number,email):
        self._phone_number = phone_number
        self._email = email
    
    def create_payment(self):
        return Payment(self._id,len(self._passenger_list),PaymentStatus.WAITING.name)
    
    def add_seat_ticket():
        pass

    def create_seatbook():
        pass

    def add_addon():
        pass

    def sum_price():
        pass

    def update_booking_status():
        pass
