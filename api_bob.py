from typing import Union,Optional
from fastapi import FastAPI
from promotion import PromotionCatalog
from airport import Airport,AirportCatalog,Aircraft
from payment import Payment,PaymentStatus,PaymentType
from add_on import PackageCatalog
from aircraft import SeatBook
from admin import Adminlist,Admin
from passenger import Passenger,TitleType,PassengerType
from booking import Booking

app = FastAPI()
airportcatalog = AirportCatalog()
AirportA = Airport("AirportA")
airportcatalog.add_airport(AirportA)
AirportB = Airport("AirportB")
airportcatalog.add_airport(AirportB)
#Admin instance
adminlist = Adminlist()
AdminA = Admin("bob", "wowza567",AirportA)
AdminB = Admin("ton", "zuzu234",AirportB)
adminlist.add_admin(AdminA)
adminlist.add_admin(AdminB)
## Aircraft instance
dm254 = Aircraft("DM254")
## Flight instance
AdminA.create_flight("DD405",90,False,AirportA,AirportB,)
AdminA.create_flight("DD406",90,False,AirportA,AirportB)
## FlightInstance instance
AdminA.create_flight_instance("DD405","2023-04-20","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance("DD405","2023-05-18","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance("DD405","2023-05-19","18.30","20.00",dm254,1000.00)
AdminA.create_flight_instance("DD406","2023-05-18","20.30","22.00",dm254,1500.00)
## Package instance
packagecatalog = PackageCatalog()
packagecatalog.create_package("Normal",0.00,False,False,False,7,0)
packagecatalog.create_package("X-tra",500.00,False,False,False,15,1)
packagecatalog.create_package("Max",1000.00,True,True,True,30,1)

promotioncatalog = PromotionCatalog()
promotioncatalog.create_promotion(1,100)
promotioncatalog.create_promotion(2,500)
promotioncatalog.create_promotion(3,1000)


#dummy flight instance---- 
airport_list = airportcatalog.airport_list
depart_airport = airport_list[0]
arrive_airport_list = depart_airport.get_arrive_airport_list()
arrive_airport = arrive_airport_list[0]
date_list = depart_airport.get_date_list(arrive_airport)
date_depart = date_list[0]
flight_instance_list = depart_airport.get_flight_instance_list(arrive_airport,date_depart)
package_list = packagecatalog.get_list_package()
flight_instance  = flight_instance_list[0]
package = package_list[0]
package.get_package_detail()
#--------

id_booking = 177013
#my part
booking = Booking(id_booking,flight_instance)
A = Passenger("ADULT","MR","HELP","ME","25-09-69")
Aseat = SeatBook(1,"A","NORMAL",True)
A.add_seat(Aseat)

payment = booking.create_payment()


"""
{
"num_adult":3,
"num_kid":0,
"num_infant":0
}

{
"title":"MR",
"name":"BOB",
"last_name":"AA",
"date_of_birth":"26-6-69",
"type":"ADULT"
}
"""

@app.get("/")
def read_root():
    return {"DAMN"}

@app.post("/set_num_of_passenger",tags=["num_of_passenger"])
async def set_num_of_passsenger(data:dict):      
    num_adult = int(data["num_adult"])
    num_kid = int(data["num_kid"])
    num_infant = int(data["num_infant"])
    if num_adult <= 0:
        return f'booking fail'
    passenger_num = booking.set_num_passenger(num_adult,num_kid,num_infant)
    return f'Adult_num:{passenger_num[0]},CHILD_num:{passenger_num[1]},INFANT_num:{passenger_num[2]}'  


@app.post("/passengers/{type_passenger}/{title_passenger}",tags=["passenger"])
async def enter_passenger(type_passenger:str,title_passenger:str,data:dict):
    name = data["name"]
    last_name = data["last_name"]
    date_of_birth = data["date_of_birth"]
    passenger_type = type_passenger
    phone_number = data["phone_number"]
    email = data["email"]
    national = data["national"]
    country_residence = data["country_residence"]
    passport_number = data["passport_number"]
    issued_by = data["issued_by"]
    passport_exp_date = data["passport_exp_date"]
    parent = data["parent"]
    
    if passenger_type == "ADULT" and title_passenger in [TitleType(i).name for i in range(0,3)]:
        if len(booking.get_adult_list) >= booking.adult_num:
            return {"message": "Maximum number of adult passenger reached."}
        if len(booking.passenger_list) == 0:
            if phone_number == '' or email == '':
                return {"message":"Invalid phone number and email"}
            if phone_number != '' and email != '':
                booking.main_passenger_info(phone_number,email)
        passenger = Passenger("ADULT",title_passenger,name,last_name,date_of_birth)
        if booking.flight_international_status and passenger.check_international_info(national,country_residence,passport_number,issued_by,passport_exp_date):
            passenger.add_international_info(national,country_residence,passport_number,issued_by,passport_exp_date)
        if booking.flight_international_status and not passenger.check_international_info(national,country_residence,passport_number,issued_by,passport_exp_date):
            return f'<message>:check your infomation-->international'
        booking.add_passenger(passenger)
            
    elif passenger_type == "CHILD" and title_passenger in [TitleType(i).name for i in range(3,5)]:        
        if len(booking.get_kid_list) >= booking.kid_num:
            return {"message": "Maximum number of kid passenger reached."}
        passenger = Passenger("CHILD",title_passenger,name,last_name,date_of_birth)
        if booking.flight_international_status and passenger.check_international_info(national,country_residence,passport_number,issued_by,passport_exp_date):
            passenger.add_international_info(national,country_residence,passport_number,issued_by,passport_exp_date)
        if booking.flight_international_status and not passenger.check_international_info(national,country_residence,passport_number,issued_by,passport_exp_date):
                return f'<message>:check your infomation-->international'
        booking.add_passenger(passenger)

    elif passenger_type == "INFANT" and title_passenger in [TitleType(i).name for i in range(5,7)]:
        if len(booking.get_infant_list) >= booking.infant_num:
            return {"message": "Maximum number of infant passenger reached."}    
        passenger = Passenger("INFANT",title_passenger,name,last_name,date_of_birth)
        if booking.flight_international_status and passenger.check_international_info(national,country_residence,passport_number,issued_by,passport_exp_date):
            passenger.add_international_info(national,country_residence,passport_number,issued_by,passport_exp_date)
        if booking.flight_international_status and not passenger.check_international_info(national,country_residence,passport_number,issued_by,passport_exp_date):
            return f'<message>:check your infomation-->international'
        
        for adult in booking.passenger_list:
            if adult.name == parent and parent != '':
                adult.add_parent(passenger)
                booking.add_passenger(passenger)
            if parent == '':
                return f'<message>:please select parent'
    else:
        return f'<message>:Invalid passenger type and title'
    
    return f'Passenger:{len(booking.passenger_list)} {passenger}'

@app.get("/inter_status")
async def get_inter_status():
    return booking.flight_international_status

@app.get("/passenger_adult_list" ,tags=["passenger"])
async def get_passenger_adult_list():
   return booking.get_adult_list

@app.get("/passenger_type" ,tags=["passenger"])
async def get_passenger_type():
    return [PassengerType(i).name for i in range(0,3)]

@app.get("/passenger_title/{type}",tags=["passenger"])
async def get_passenger_title(type:str):
    if type == "ADULT":
        return [TitleType(i).name for i in range(0,3)]
    if type == "CHILD":
        return [TitleType(i).name for i in range(3,5)]
    if type == "INFANT":
        return [TitleType(i).name for i in range(5,7)]

#payment
@app.get("/get_payment_type",tags=["payment"])
async def get_payment_type():
    return [PaymentType(i).name for i in range(1,7)]

@app.get("/get_promotion_code",tags=["payment"])
async def get_promotion_code():
    promotion_dict = {}
    for promotion in promotioncatalog.get_promotion_list:
        promotion_dict[promotion.promotion_code] = promotion.discount
    return promotion_dict

@app.post("/select_payment_type",tags=["payment"])
async def select_payment_type(payment_type:str):
    if payment.add_payment_type(payment_type):
        return "select payment type"
    else:
        return "<message>:Invalid payment type"

@app.post("/select_promotion_code",tags=["payment"])
async def select_promotion_code(promotion_name:int):
    for promotion in promotioncatalog.get_promotion_list:
        if promotion.promotion_code == promotion_name:
            payment.add_promotion_code(promotion)
            return f"select {promotion.promotion_code}-->{promotion.discount}"
    return "<message>:Invalid promotioncode"

@app.get("/sum_payment/{flight_price}/{extraservice_price}/{specialassistance_price}/{baggage_price}/{meal_price}/{special_price}")
async def sum_payment_price(flight_price:flight_instance,extraservice_price:int,specialassistance_price:int,meal_price:int,special_price:int):
    pass