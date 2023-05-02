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
            
    def check(self,username,password):
        for i in self._admin_list:
            if username == i._username and password == i._password:
                return True
            else:
                return False

class Admin:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def create_flight(self,name,flight_duration,international,depart_airport,arrive_airport):
        if isinstance(name,str) and isinstance(flight_duration,int) and isinstance(international,bool) and isinstance(depart_airport,Airport) and isinstance(arrive_airport,Airport):
            depart_airport._flight_list.append(Flight(name,flight_duration,international,depart_airport,arrive_airport))
        else:
            raise TypeError("Parameter type not correct")

    def create_flight_instance(self,depart_airport,flight_name,date_depart,time_depart,time_arrive,aircraft,price):
        if isinstance(flight_name,str) and isinstance(date_depart,str) and isinstance(time_arrive,str) and isinstance(time_depart,str) and isinstance(aircraft,Aircraft) and isinstance(price,float) and isinstance(depart_airport,Airport):
            for f in depart_airport._flight_list:
                if f.name == flight_name:
                    flight = f
                    break
            flight.depart_airport._flight_instance_list.append(FlightInstance(flight.name,flight.flight_duration,flight.international,flight.depart_airport,flight.arrive_airport,date_depart,time_arrive,time_depart,aircraft,price))
        else:
            raise TypeError("Parameter type not correct")

    def edit_flight_instance(self,airport,flight_instance,edit_date_depart,edit_time_arrive,edit_time_depart,edit_price):
        flight_instance.date_depart = edit_date_depart
        flight_instance.time_arrive = edit_time_arrive
        flight_instance.time_depart = edit_time_depart
        flight_instance.price = edit_price

    def cancel_flight_instance(self,airport,flight_instance):
        airport.flight_instance_list.remove(flight_instance)

    def change_seat(self,booking,seat_row,seat_column,edit_seat_row,edit_seat_column):
        for seatbook in booking.seat_book:
            if seat_row == seatbook.seat_row and seat_column == seatbook.seat_column:
                break
        seat_list = booking._flight.aircraft.seat_list
        for i in seat_list:
            if edit_seat_row == i.seat_row and edit_seat_column == i.seat_column:
                break
        booking.seat_book.remove(seatbook)
        booking.seat_book.append(i)

        for ticket in booking.ticket:
            if seatbook == ticket.seatbook:
                break
        ticket.seatbook = i
        
        
    def add_promotion(self,promotion_code,discount):
        if isinstance(promotion_code,str) and isinstance(discount,int) :
                PromotionCatalog._promotion_list.append((promotion_code,discount))
        else:
            raise TypeError("Parameter type is not correct")
