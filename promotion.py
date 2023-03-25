class Promotion:
    def __init__(self, promotion_code, discount):
        self._promotion_code = promotion_code
        self._discount = discount

    @property
    def promotion_code(self):
        return self.promotion_code
    
    @property
    def discount(self):
        return self.discount

class PromotionCatalog:
    def __init__(self):
        self._promotion_list =[] 
    