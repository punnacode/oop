from enum import Enum
from flight import FlightInstance
class PackageCatalog:
    def __init__(self):

        self._packagelist = []

    def create_package(self,name,price,fasttrack,insurance,lounge,extra_bag,meal_amout):
        if isinstance(fasttrack,bool) and isinstance(insurance,bool) and isinstance(lounge,bool):
            extra_service = Extraservice(fasttrack,insurance,lounge)
        else:
            raise TypeError("Parameter type not correct")
        special_assistance = SpecialAssistance(False,False,False,False,False,False)
        if isinstance(extra_bag,int):
            baggage = Baggage(extra_bag)
        else:
            raise TypeError("Parameter type not correct")
        if isinstance(meal_amout,int):
            meal = Meal(MealType.NONE,meal_amout)
        else:
            raise TypeError("Parameter type not correct")
        special_baggage = SpecialBaggage("")

        if isinstance(name,str) and isinstance(price,float):
            self._packagelist.append(Package(name,price,extra_service,special_assistance,baggage,meal,special_baggage))
        else:
            raise TypeError("Parameter type not correct")
    
    def get_list_package(self):
        return self._packagelist
    
    def get_package(self,package_name):
        for package in self._packagelist:
            if package.name == package_name:
                return package


class Package:
    def __init__(self,name,price,extra_service,special_assistance,baggage,meal,special_baggage):
        self._name = name
        self._price = price
        self._extra_service = extra_service
        self._special_assistance = special_assistance
        self._baggage = baggage
        self._meal = meal
        self._special_baggage = special_baggage
    @property
    def name(self):
        return self._name
        
    def get_extra_service(self):
        return self._extra_service
    
    def get_special_assistance(self):
        return self._special_assistance
    
    def get_baggage(self):
        return self._baggage
    
    def get_meal(self):
        return self._meal
    
    def get_special_baggage(self):
        return self._special_baggage
    

    def sum_price(self,flight):
        if isinstance(flight,FlightInstance):
            return round(self._price + flight.get_price(),2)
        else:
            raise TypeError("Parameter type not correct")
    
    def get_package_detail(self):
        return {"Bagage": self._baggage.get_detail(),"Meal": self._meal.get_detail(),"Extra service": self._extra_service.get_detail()}
    
    
    
class Extraservice:
    extraservice_dict = {1:"FastTrack",2:"Insurance",3:"Lounge"} 

    def __init__(self,fasttrack,insurance,lounge):
        self._fasttrack = fasttrack
        self._insurance = insurance
        self._lounge = lounge
        self.extraservice_dict

    def get_detail(self):
        i = 1
        extraservice_list = []
        for value in self.__dict__.values():
            if value == True:
                extraservice_list.append(self.extraservice_dict[i])
            i += 1
        return extraservice_list


class SpecialAssistance:
    special_assistance_dict = {1:"Deaf",2:"Blind",3:"Monk",4:"Nun",5:"Wheelchair",6:"Alone kid"}

    def __init__(self,deaf,blind,monk,nun,wheelchair,alonekid):
        self._deaf = deaf
        self._blind = blind
        self._monk = monk
        self._nun = nun
        self._wheelchair = wheelchair
        self._alonekid = alonekid
        self.special_assistance_dict
     
    def get_detail(self):
        i = 1
        specialassitance_list = [] 
        for value in self.__dict__.values():
            if value == True:
                specialassitance_list.append(self.special_assistance_dict[i])
            i += 1
        return specialassitance_list

    def get_specialassistance():
        pass

class Baggage:
    def __init__(self,extra_bag):
        self._extra_bag = extra_bag
    
    def get_detail(self):
        if self._extra_bag != 0:
            return self._extra_bag
        return
    
    def get_baggage():
        pass

        
class Meal:
    def __init__(self,meal_type,meal_amout):
        self._meal_amount = meal_amout
        self._meal_type = meal_type
    
    def get_detail(self):
        if self._meal_amount > 0 and self._meal_type.value == 0:
            return self._meal_amount
        elif self._meal_amount > 0:
            return [self._meal_amount,self._meal_type.name]
        return
    
    def get_meal():
        pass

class MealType(Enum):
    NONE : int = 0
    MENUONE : int = 1
    MENUTWO : int = 2
    MENUTHREE : int = 3
    MENUFOUR : int = 4
    MENUFIVE : int = 5

class SpecialBaggage:
    def __init__(self,special_bag):
        self._special_bag = special_bag
    
    def get_detail(self):
        return self._special_bag

    def get_specialbaggage():
        pass
    