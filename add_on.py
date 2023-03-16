class PackageCatalog:
    def __init__(self,packagelist):
        self.packagelist = packagelist

class Package:
    def __init__(self,type,price):
        self._type = type
        self._price = price
    
    def get_extraservice():
        pass
    
    def get_baggage():
        pass
    
    def get_meal():
        pass
    
    def get_specialbaggage():
        pass
    
    def get_specialassistance():
        pass
   
class Extraservice:
    def __init__(self,fasttrack,insurance,lounge):
        self._fasttrack = fasttrack
        self._insurance = insurance
        self._lounge = lounge

class SpecialAssistance:
    def __init__(self,deaf,blind,monk,nun,wheelchair,alonekid):
        self._deaf = deaf
        self._blind = blind
        self._monk = monk
        self._nun = nun
        self._wheelchair = wheelchair
        self._alonekid = alonekid

class Baggage:
    def __init__(self,extra_bag):
        self._extra_bag = extra_bag
        
class Meal:
    def __init__(self,meal_type,meal_amout):
        self._meal_type = meal_type
        self._meal_amount = meal_amout

class SpecialBaggage:
    def __init__(self,special_bag):
        self._special_bag = special_bag
