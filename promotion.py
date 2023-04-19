class PromotionCatalog:
    def __init__(self):
        self._promotion_list =[] 
    
    def create_promotion(self,promotion_code,discount):
        if isinstance(promotion_code,int) and isinstance(discount,int):
            self._promotion_list.append(Promotion(promotion_code,discount))
        else:
            raise TypeError("Parameter type not correct")
    
    @property
    def get_promotion_list(self):
        return self._promotion_list
class Promotion:
    def __init__(self, promotion_code, discount):
        self._promotion_code = promotion_code
        self._discount = discount

    @property
    def promotion_code(self):
        return self._promotion_code
    
    @property
    def discount(self):
        return self._discount

    