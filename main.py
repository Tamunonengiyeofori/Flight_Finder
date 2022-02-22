#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import timedelta, datetime
from data_manager import DataManager
# create an instance of the data manager class
data_manager = DataManager()

from flight_search import FlightSearch
# create an instance of the flight_search class
flight_search = FlightSearch()

# from flight_data import FlightData
# flight_data = FlightData()

# store all the search data in a variable sheet_data
sheet_data = data_manager.get_all_data()

for row in sheet_data:
   if row["iataCode"] == "":
       row["iataCode"] = flight_search.get_destination_code(row["city"])
       
data_manager.destination_data = sheet_data
data_manager.update_destination_code()

time_tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=(6 * 30))

ORIGIN_CITY_IATA = "LOS"
for city in sheet_data:
    flight_search.search_flights(ORIGIN_CITY_IATA , 
                                 city["iataCode"] , 
                                 from_time=time_tomorrow , 
                                 to_time= six_months_from_now
                                 )
        
print(sheet_data)
    
    
    
    











