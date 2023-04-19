from promotion import PromotionCatalog
from airport import Airport, AirportCatalog
from aircraft import Aircraft, SeatBook
from flight import Flight, FlightInstance

class Adminlist:
    def __init__(self):
        self._admin_list = []
    
    def add_admin(self, admin):
        if isinstance(admin,Admin):
            self._admin_list.append(admin)
    def get_list_admin(self):
        return self._admin_list
    
    def login(self,username,password):
        for i in self._admin_list:
            if username == i._username and password == i._password:
                return i

class Admin:
    def __init__(self, username, password, admin_airport):
        self._username = username
        self._password = password
        self._admin_airport = admin_airport

    def create_flight(self,name,flight_duration,international,depart_airport,arrive_airport):
        if isinstance(name,str) and isinstance(flight_duration,int) and isinstance(international,bool) and isinstance(depart_airport,Airport) and isinstance(arrive_airport,Airport):
            self._admin_airport._flight_list.append(Flight(name,flight_duration,international,depart_airport,arrive_airport))
        else:
            raise TypeError("Parameter type not correct")

    def create_flight_instance(self,flight_name,date_depart,time_depart,time_arrive,aircraft,price):
        if isinstance(flight_name,str) and isinstance(date_depart,str) and isinstance(time_arrive,str) and isinstance(time_depart,str) and isinstance(aircraft,Aircraft) and isinstance(price,float):
            for f in self._admin_airport._flight_list:
                if f.name == flight_name:
                    flight = f
                    break
            self._admin_airport._flight_instance_list.append(FlightInstance(flight.name,flight.flight_duration,flight.international,flight.depart_airport,flight.arrive_airport,date_depart,time_arrive,time_depart,aircraft,price))
        else:
            raise TypeError("Parameter type not correct")

    def edit_flight_instance(flight_instance,edit_date_depart,edit_time_arrive,edit_time_depart,edit_price):
        flight_instance.date_depart = edit_date_depart
        flight_instance.time_arrive = edit_time_arrive
        flight_instance.time_depart = edit_time_depart
        flight_instance.price = edit_price

    def cancel_flight_instance(flight_instance):
        del flight_instance

    def change_seat(seat,edit_seat):
        SeatBook(True,seat.seat_row,seat.seat_column,seat.seat_type)
        SeatBook(False,edit_seat.seat_row,edit_seat.seat_column,edit_seat.seat_type)
        
    def add_promotion(self,promotion_code,discount):
        if isinstance(promotion_code,str) and isinstance(discount,int) :
                PromotionCatalog._promotion_list.append((promotion_code,discount))
        else:
            raise TypeError("Parameter type is not correct")
