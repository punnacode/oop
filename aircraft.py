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
    @property
    def name(self):
        return self._name
    @property
    def seat_list(self):
        return self._seat_list
    
    def get_seat(self,flight):
        available_seat = []
        seat_book_list = flight.get_seatbook_list()
        seat_check = False
        if not seat_book_list:
            return self._seat_list
        else:
            for seat in self._seat_list:
                for bookseat in seat_book_list:
                    if seat not in available_seat and (seat.seat_row == bookseat.row and seat.seat_column == bookseat.column):
                        seat_check = True
                if seat_check == False:
                    available_seat.append(seat)
                seat_check = False
            return available_seat

class AircraftSeat:
    def __init__(self,seat_row,seat_column,seat_type):
        self._seat_row = seat_row
        self._seat_column = seat_column
        self._seat_type = seat_type
    
    def get_seat_detail():
        pass
    
    @property
    def seat_row(self):
        return self._seat_row
    @property
    def seat_column(self):
        return self._seat_column
    @property
    def seat_type(self):
        return self._seat_type
    
class SeatBook(AircraftSeat):
    def __init__(self,seat_booked,seat_row,seat_column,seat_type):
        AircraftSeat.__init__(self,seat_row,seat_column,seat_type)
        self._seat_booked = seat_booked
        
    @property
    def seat_booked(self):
        return self._seat_booked
    
    @property
    def row(self):
        return self._seat_row
    
    @property
    def column(self):
        return self._seat_column
    @property
    def type(self):
        return self._seat_type

class SeatType(Enum):
    NORMAL  : int = 100
    PREMIUM : int = 200
    FRONTROW: int = 300

class AircraftCatalog:
    def __init__(self):
        self._aircraft_list = []

    def add_aircraft(self,aircraft):
        if isinstance(aircraft,Aircraft):
            self._aircraft_list.append(aircraft)
            
    def get_list_aircraft(self):
        return self._aircraft_list
         
