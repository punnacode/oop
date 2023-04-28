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
        if payment_type != '':
            self._payment_type = payment_type
            return True
        return False
    
    def add_booking(self,booking):
        self._booking = booking
    
    def add_promotion_code(self,promotion):
        self._promotion_code = promotion
        return self._promotion_code
        
        
    def sum_price(self):
        print(self._promotion_code)
        print(sum(self._booking.flight_sum_price()))
        print(sum(self._booking.seat_sum_price()))
        print(sum(self._booking.add_on_sum_price()))
        self._payment_total = (sum(self._booking.flight_sum_price())+sum(self._booking.seat_sum_price())+sum(self._booking.add_on_sum_price()))-self._promotion_code.discount
        return self._payment_total
        
    @property
    def payment_status(self):
        return self._payment_status
    
    def to_dict(self):
        payment_dict = {
            "id": self._id,
            "booking": self._booking.to_dict() if self._booking else None,
            "payment_status": self._payment_status,
            "promotion_code": self._promotion_code,
            "payment_type": self._payment_type,
            "payment_total": self._payment_total,
        }
        return payment_dict
class PaymentType(Enum):
    CREDITCARD: int = 1
    COUNTER: int = 2
    QRCODE: int = 3
    LINEPAY: int = 4
    UNIONPAY: int = 5
    AIRPAY: int =6

class PaymentStatus(Enum):
    WAITING: int = 1
    CANCEL: int = 2
    COMPLETE: int = 3
