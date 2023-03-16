from enum import Enum

class Aircraft:
    def __init__(self,name):
        self._name = name
    
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

class SeatType(Enum):
    Normal  : int = 1
    Premium : int = 2
    Frontrow: int = 3
         