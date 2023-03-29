from enum import Enum
class PassengerType(Enum):
    ADULT,CHILD,INFANT = range(0,3)

class TitleType(Enum):
    MR,MONK,MRS,MISS,MSTR,BOY,GIRL = range(0,7)

class MealType(Enum):
    MENUONE,MENUTWO,MENUTHREE,MENUFOUR,MENUFIVE = range(0,5)

class Passenger:
    def __init__(self,type,title,name,last_name,date_of_birth,country_residence,passport_number,issued_by,passport_exp_date):
        self._type = type
        self._title = title
        self._name = name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._country_residence = country_residence
        self._passport_number = passport_number
        self._issued_by = issued_by
        self._passport_exp_date = passport_exp_date
        self.parent = []

    def add_parent(self):
        pass
    
    def create_booking(self):
        pass
        
