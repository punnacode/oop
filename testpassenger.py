from Passenger import Passenger,PassengerType,TitleType
from aircraft import SeatBook,SeatType
from payment import Payment,PaymentStatus,PaymentType
from add_on import Package,PackageCatalog

#setup passenger
PassengerA = Passenger(PassengerType.ADULT.name,TitleType.MR.name,"BOB","OK","25/09/46","Thai","Thailand","65010971","B","25/01/69")
PassengerB = Passenger(PassengerType.CHILD.name,TitleType.MISS.name,"M","OK","25/12/48","Thai","Thailand","65010999","B","25/02/69")
PassengerC = Passenger(PassengerType.INFANT.name,TitleType.MSTR.name,"BB","OK","25/12/60","Thai","Thailand","65010009","B","25/02/69")

#test add_parent
#PassengerA.add_parent(PassengerB)
PassengerA.add_parent(PassengerC)

#show member
Member_of_parent = PassengerA.parent
for i,member in enumerate(Member_of_parent):
    print(f"Member{i+1}:")
    print(member)
    
#setup booking
id_of_booking = 69
num_of_passenger = Passenger.num_passenger
seatbookA = SeatBook(False,2,'A',SeatType.Frontrow.name)
seat_booked = seatbookA.seat_booked
paymentA = Payment(PaymentType.QRCODE.name,1,id_of_booking,num_of_passenger,None,PaymentStatus.WAITING.name)
payment_status = paymentA.payment_status
packageA = Package("D",5)
package_type = packageA.package_type
ticket_list = []

PassengerA.create_booking(id_of_booking,num_of_passenger,"0922513540","A@gmail.com",seat_booked,payment_status,package_type,ticket_list)