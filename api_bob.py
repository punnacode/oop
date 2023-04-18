from typing import Union,Optional
from fastapi import FastAPI
from airport import Airport,AirportCatalog,Aircraft
from add_on import PackageCatalog
from admin import Adminlist,Admin
from passenger import Passenger,TitleType,PassengerType
from booking import Booking

app = FastAPI()
booking = Booking()
booking.add_flight_instance(True)

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

