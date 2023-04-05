class Booking:
    def __init__(self, id,phone_number,email, num_of_passenger, seat_booked, payment_status, package_type,passenger_list):
        self._id = id
        self._phone_number = phone_number
        self._email = email
        self._num_of_passenger = num_of_passenger
        self._seat_booked = seat_booked
        self._payment_status = payment_status
        self._package_type = package_type
        self._passenger_list = passenger_list

    def create_ticket():
        pass

    def get_book_seat():
        pass

    def add_seat_ticket():
        pass

    def create_seatbook():
        pass

    def add_addon():
        pass

    def sum_price():
        pass

    def create_payment():
        pass

    def update_booking_status():
        pass
    @property
    def payment_status(self):
        return self._payment_status