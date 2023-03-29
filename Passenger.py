from booking import Booking
from enum import Enum
class PassengerType(Enum):
    ADULT,CHILD,INFANT = range(0,3)

class TitleType(Enum):
    MR,MONK,MRS,MISS,MSTR,BOY,GIRL = range(0,7)

class MealType(Enum):
    MENUONE,MENUTWO,MENUTHREE,MENUFOUR,MENUFIVE = range(0,5)

class Passenger:
    num_passenger = 0
    def __init__(self,type,title,name,last_name,date_of_birth,nationality,country_residence,passport_number,issued_by,passport_exp_date):
        self._type = type
        self._title = title
        self._name = name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._nationality = nationality
        self._country_residence = country_residence
        self._passport_number = passport_number
        self._issued_by = issued_by
        self._passport_exp_date = passport_exp_date
        self.parent = []
        Passenger.num_passenger += 1

    def add_parent(self,passenger):
        if isinstance(passenger,Passenger) and passenger._type == "INFANT" and self._type != "INFANT" :
            self.parent.append(passenger)
        else:
            raise TypeError("Parameter type not correct")

    def __str__(self):
         return f"Type:{self._type}\nTiele:{self._title}\nName:{self._name}\nLastname:{self._last_name}\nbirthdate:{self._date_of_birth}\nnationality:{self._nationality}\nCountry_resident:{self._country_residence}\nPassportNum:{self._passport_number}\nIssuedBy:{self._issued_by}\nPassportexp:{self._passport_exp_date}\n"   
     
    def create_booking(self,id,phone_number,email,num_of_passenger,seat_booked,payment_status,package_type):
        if isinstance(seat_booked,bool) and isinstance(payment_status,str) and isinstance(package_type,str) :      
            print(f"{id}....{phone_number}....{email}....{num_of_passenger}....{seat_booked}....{payment_status}....{package_type}")
            Booking(id,phone_number,email,num_of_passenger,seat_booked,payment_status,package_type)

