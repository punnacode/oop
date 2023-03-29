from aircraft import Aircraft

from booking import Booking

from datetime import date

class Flight:
    def __init__(self,name,flight_duration,international,depart_airport,arrive_airport):
        self._name = name
        self._flight_duration = flight_duration
        self._international = international
        self._depart_airport = depart_airport
        self._arrive_airport = arrive_airport
    
    @property
    def name(self):
        return self._name
    @property
    def flight_duration(self):
        return self._flight_duration
    @property
    def international(self):
        return self._international
    @property
    def depart_airport(self):
        return self._depart_airport
    @property
    def arrive_airport(self):
        return self._arrive_airport

class FlightInstance(Flight):
    day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    def __init__(self,name,flight_duration,international,depart_airport,arrive_airport,date_depart,time_arrive,time_depart,aircraft,price):
        super().__init__(name,flight_duration,international,depart_airport,arrive_airport)
        self._date_depart = date_depart
        self._time_arrive = time_arrive
        self._time_depart = time_depart
        self._aircraft = aircraft
        self._price = price
        self._booking = []

        

        self.day_in_month

    
    @property
    def date_depart(self):
        return self._date_depart
    @property
    def time_arrive(self):
        return self._time_arrive
    @property
    def time_depart(self):
        return self._time_depart
    @property
    def price(self):
        return self._price
    @property
    def aircraft(self):
        return self._aircraft

    def __str__(self):
        return f'Flight Detail\nName: {self.name}\nAircraft: {self.aircraft.name}\nOrigin Airport: {self.depart_airport.name}\nDestination Airport: {self.arrive_airport.name}\nFlight Duration: {self.flight_duration} minute\nTime Depart: {self.time_depart}\nTime Arrive: {self.time_arrive}\nDate Depart: {self.date_depart}'    

    def get_price(self):
        days = self.date_diff(str(date.today()),self.date_depart)
        if days > 30:
            return self.price
        else:
            return round(float(self.price*(1.02**(31-days))), 2)

    def get_seat__book_detail():
        pass

    def get_filght_info():
        pass

    def change_seat(aircraft_seat):
        pass


    def add_booking(self,booking):
        if booking.payment_status == True:
            self._booking.append(booking)
        else:
            raise TypeError("please check payment status")

    
    ## Date difference system
    def is_leap(self,year):
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            return 29
        else:
            return 28

    def day_of_year(self,day,month,year):
        self.day_in_month[2] = self.is_leap(year)
        num = sum(self.day_in_month[x] for x in range(month)) + day
        return num

    def day_in_year(self,year):
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            return 366
        else:
            return 365

    def month_date_call(self,month,year):
        self.day_in_month[2] = self.is_leap(year)
        return self.day_in_month[month]

    def date_diff(self,date1,date2):
        date_1 = [int(date) for date in date1.split("-")]
        date_2 = [int(date) for date in date2.split("-")]
        if date_1[1] > 12 or date_1[1] < 1 or date_2[1] > 12 or date_2[1] < 1:
            raise ValueError("Incorrect Month Value")
        if date_1[2] > self.month_date_call(date_1[1],date_1[0]) or date_2[2] > self.month_date_call(date_2[1],date_2[0]):
            raise ValueError("Incorrect Day Value")
        year_list = sum(self.day_in_year(year) for year in range(date_1[0],date_2[0])) + self.day_of_year(date_2[2],date_2[1],date_2[0]) - self.day_of_year(date_1[2],date_1[1],date_1[0]) + 1
        return(year_list)

   
   



