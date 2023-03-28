from enum import Enum

class Aircraft:
    def __init__(self,name):
        self._name = name
        self._seat_list = []
    
    def create_seat(self,row,column,seat_type):
        if isinstance(row,int) and isinstance(column,str) and isinstance(seat_type,SeatType):
            self._seat_list.append(AircraftSeat(row,column,seat_type))
        else:
            raise TypeError("Parameter type not correct")

    def get_seat():
        pass

    def update_seat():
        pass

class AircraftSeat:
    def __init__(self,seat_row,seat_column,seat_type):
        self._seat_row = seat_row
        self._seat_column = seat_column
        self._seat_type = seat_type
    
    def get_seat_detail():
        pass

class SeatBook(AircraftSeat):
    def __init__(self,seat_booked,seat_row,seat_column,seat_type):
        AircraftSeat.__init__(self,seat_row,seat_column,seat_type)
        self._seat_booked = seat_booked
        
    @property
    def seat_booked(self):
        return self._seat_booked

class SeatType(Enum):
    NORMAL  : int = 100
    PREMIUM : int = 200
    FRONTROW: int = 300
         