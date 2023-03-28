from enum import Enum

class Payment:
    def __init__(self, payment_type, payment_total, id, num_of_passenger,promotion_code,payment_status):
        self._payment_type = payment_type
        self._payment_status = payment_status
        self._payment_total = payment_total
        self._id = id
        self._num_of_passenger = num_of_passenger
        self._promotion_code = promotion_code

    def get_promotion(self):
        pass

    def update_price(self):
        pass
    
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
