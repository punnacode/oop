from enum import Enum
from promotion import PromotionCatalog
class Payment:
    def __init__(self,id,num_of_passenger,payment_status):
        self._id = id
        self._num_of_passenger = num_of_passenger
        self._payment_status = payment_status
        self._promotion_code = None
        self._payment_type = None
        self._payment_total = None

    def add_payment_type(self,payment_type):
        if payment_type != '':
            self._payment_type = payment_type
            return True
        return False
        
    def add_promotion_code(self,promotion):
        self._promotion_code = promotion

    def sum_price(self,flight,extraservice_price,specialassistance_price,baggage_price,meal_price,special_price):
        self._payment_total = flight+extraservice_price+specialassistance_price+baggage_price+meal_price+special_price-self._promotion_code.discount
        
    @property
    def payment_status(self):
        return self._payment_status
class PaymentType(Enum):
    CREDITCARD: int = 1
    COUNTER: int = 2
    QRCODE: int = 3
    LINEPAY: int = 4
    UNIONPAY: int = 5
    ALIPAY: int =6

class PaymentStatus(Enum):
    WAITING: int = 1
    CANCEL: int = 2
    COMPLETE: int = 3
