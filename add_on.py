class PackageCatalog:
    def __init__(self):
        self.packagelist = []
        
    def add_package(self,package):
        if isinstance(package,Package):
            self.packagelist.append(package)
        else:
            raise TypeError("invalite paramiter")

class Package:
    def __init__(self,type,price):
        self._type = type
        self._price = price
    
    def get_package(self):
        pass
    
    @property
    def package_type(self):
        return self._type
    
class Extraservice:
    def __init__(self,fasttrack,insurance,lounge):
        self._fasttrack = fasttrack
        self._insurance = insurance
        self._lounge = lounge
    
    def get_extraservice():
        pass

class SpecialAssistance:
    def __init__(self,deaf,blind,monk,nun,wheelchair,alonekid):
        self._deaf = deaf
        self._blind = blind
        self._monk = monk
        self._nun = nun
        self._wheelchair = wheelchair
        self._alonekid = alonekid

    def get_specialassistance():
        pass

class Baggage:
    def __init__(self,extra_bag):
        self._extra_bag = extra_bag
    
    def get_baggage():
        pass

        
class Meal:
    def __init__(self,meal_type,meal_amout):
        self._meal_type = meal_type
        self._meal_amount = meal_amout
    
    def get_meal():
        pass

class SpecialBaggage:
    def __init__(self,special_bag):
        self._special_bag = special_bag
    
    def get_specialbaggage():
        pass
    
