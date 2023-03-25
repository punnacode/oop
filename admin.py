from promotion import PromotionCatalog

class Admin:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def edit_flight_instance():
        pass

    def create_flight_instance():
        pass

    def add_promotion(self,promotion_code,discount):
        if isinstance(promotion_code,str) and isinstance(discount,int) :
                PromotionCatalog._promotion_list.append((promotion_code,discount))
        else:
            raise TypeError("Parameter type is not correct")
