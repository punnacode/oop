from fastapi import FastAPI
from airport import Airport,AirportCatalog,Aircraft
from add_on import PackageCatalog
from admin import Adminlist,Admin

app = FastAPI()
## Airport instance 
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

"""
{
    "Origin airport":"AirportA",
    "Destination airport":"AirportB",
    "Date depart":"2023-05-18",
    "Flight name":"DD405",
    "Package name":"Max"
}
"""

@app.get("/") #Check
def read_root():
    return {"Welcome": "to the Hell"}

@app.get("/select_origin") #Check
async def select_origin():
    airport_list = airportcatalog.airport_list
    oal = []
    for i in airport_list:
        oal.append(i.name)
    return {"Origin airport list": oal}

@app.post("/select_destination") #Check
async def select_destination(data: dict):
    arrive_airport_list = airportcatalog.search_arrive_airport_list(data["Origin airport"])
    dal = []
    for i in arrive_airport_list:
        dal.append(i.name)
    return {"Destination airport list":dal}

@app.post("/select_date") #Check
async def select_date(data: dict):
    date_list = airportcatalog.search_date_list(data["Origin airport"],data["Destination airport"])
    dl = []
    for i in date_list:
        dl.append(i)
    return {"Date list":dl}

@app.post("/select_flight") #Check
async def select_flight_instance(data: dict):
    pl = []
    fl = []
    flight_instance_list = airportcatalog.search_flight_instance_list(data["Origin airport"],data["Destination airport"],data["Date depart"])
    package_list = packagecatalog.get_list_package()
    for i in range(len(flight_instance_list)):
        pkl = {}
        for j in package_list:
            pkl[j.name]=j.sum_price(flight_instance_list[i])
        fl.append([flight_instance_list[i].name , flight_instance_list[i].time_depart , flight_instance_list[i].time_arrive,pkl])
    for i in package_list:
        pl.append(i.name)
    return {"Flight data":fl,"Package data":pl}

@app.post("/flight_detail/{flight_name}") #Check
async def flight_detail(flight_name: str,data: dict):
    flight_instance = airportcatalog.search_flight_instance(data["Origin airport"],data["Date depart"],flight_name)
    return {
            "Name":flight_instance.name,
            "Aircraft":flight_instance.aircraft.name,
            "Origin Airport":flight_instance.depart_airport.name,
            "Destination Airport":flight_instance.arrive_airport.name,
            "Flight Duration":flight_instance.flight_duration,
            "Time Depart":flight_instance.time_depart,
            "Time Arrive":flight_instance.time_arrive,
            "Date Depart":flight_instance.date_depart
            }

@app.get("/package_detail/{package_name}") #Check
async def package_detail(package_name: str):
    package = packagecatalog.get_package(package_name)
    return {package_name: package.get_package_detail()}

