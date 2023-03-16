class Promotion:
    def __init__(self, promotion_code, discount):
        self._promotion_code = promotion_code
        self._discount = discount

class PromotionCatalog:
    def __init__(self,promotionlist):
        self._promotion_list = promotionlist