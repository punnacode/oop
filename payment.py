from enum import Enum
from promotion import PromotionCatalog

class Payment:
    def __init__(self,id,payment_status):
        self._id = id
        self._booking = None
        self._payment_status = payment_status
        self._promotion_code = None
        self._payment_type = None
        self._payment_total = None

    def add_payment_type(self,payment_type):
        self._payment_type = payment_type
    
    def add_booking(self,booking):
        self._booking = booking
    
    def add_promotion_code(self,promotion):
        if self._promotion_code == None:
            self._promotion_code = promotion
            return round(float(self._payment_total - self._promotion_code.discount),2)
        else:
            return "Can only use 1 code"
        
        
    def sum_price(self):
        price_dict = {}
        price_dict["Flight price"] = self._booking.flight_sum_price()
        price_dict["Seat price"] = round(float(sum(self._booking.seat_sum_price())),2)
        price_dict["Add on price"] = round(float(sum(self._booking.add_on_sum_price())),2)
        price_dict["Total price"] = round(float(sum(self._booking.flight_sum_price()) + sum(self._booking.seat_sum_price()) + sum(self._booking.add_on_sum_price())),2)
        self._payment_total = round(float(sum(self._booking.flight_sum_price()) + sum(self._booking.seat_sum_price()) + sum(self._booking.add_on_sum_price())),2)
        return price_dict
        
    @property
    def payment_status(self):
        return self._payment_status
    @property
    def promotion_code(self):
        return self._promotion_code
    @promotion_code.setter
    def promotion_code(self,new_promotion_code):
        self._promotion_code = new_promotion_code
    @property
    def payment_total(self):
        return self._payment_total
    @payment_total.setter
    def payment_total(self,new_payment_total):
        self._payment_total = new_payment_total
    
class CreditCardPayment(Payment):
    def __init__(self,id,payment_status,card_number,expired_date,card_holder,cvv):
        Payment.__init__(self,id,payment_status)
        self._card_number = card_number
        self._expired_date = expired_date
        self._card_holder = card_holder
        self._cvv = cvv

class SMSVerifyPayment(Payment):
    def __init__(self,id,payment_status,phone_number):
        Payment.__init__(self,id,payment_status)
        self._phone_number = phone_number

class PaymentType(Enum):
    CREDITCARD: int = 1
    QRCODE: int = 2
    COUNTER: int = 3

class PaymentStatus(Enum):
    WAITING: int = 1
    CANCEL: int = 2
    COMPLETE: int = 3
