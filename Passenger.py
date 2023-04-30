from enum import Enum
class PassengerType(Enum):
    ADULT,CHILD,INFANT = range(0,3)
class TitleType(Enum):
    MR,MRS,MONK,MISS,MSTR,BOY,GIRL = range(0,7)

class Passenger:
    def __init__(self,type,title,name,last_name,date_of_birth):
        self._type = type
        self._title = title
        self._name = name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._nationality = None
        self._country_residence = None
        self._passport_number = None
        self._issued_by = None
        self._passport_exp_date = None
        self._seat = None
        self.parent = []
        
    @property
    def name(self):
        return self._name
    
    @property
    def last_name(self):
        return self._last_name

    @property
    def title(self):
        return self._title
        
    @property
    def type(self):
        return self._type
    
    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    @property
    def seat(self):
        return self._seat
    
    def add_seat(self,seat):
        self._seat = seat
    
    def add_international_info(self,national,country_residence,passport_number,issued_by,passport_exp_date):
        self._nationality = national
        self._country_residence = country_residence
        self._passport_number = passport_number
        self._issued_by = issued_by
        self._passport_exp_date = passport_exp_date
            
    def check_international_info(self,national,country_residence,passport_number,issued_by,passport_exp_date):
        if national != '' and country_residence != '' and passport_number != '' and issued_by != '' and passport_exp_date != '':
            return True
        else:
            return False     
        
    def add_parent(self,passenger):
        if isinstance(passenger,Passenger) and passenger._type == "INFANT" and self._type != "INFANT" :
            self.parent.append(passenger)
        else:
            raise TypeError("Parameter type not correct")

    def __str__(self):
        passenger_str = f"\nType:{self._type}\nTitle:{self._title}\nName:{self._name}\nLastname:{self._last_name}\nbirthdate:{self._date_of_birth}"
        if self._country_residence != None and self._issued_by != None and self._nationality != None and self._passport_exp_date != None and self._passport_number != None:
            passenger_str += f"nationality:{self._nationality}\nCountry_resident:{self._country_residence}\nPassportNum:{self._passport_number}\nIssuedBy:{self._issued_by}\nPassportexp:{self._passport_exp_date}"
        return passenger_str

