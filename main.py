#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import timedelta, datetime
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# create an instance of the data manager class
data_manager = DataManager()
# store all the search data in a variable sheet_data
sheet_data = data_manager.get_all_data()
# create an instance of the flight_search class
flight_search = FlightSearch()
# create an instance of the notification manager class
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"



if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
       
    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()

# Using datetime library and it's timedelta() method to calculate time for tomorrow and time range for six months
time_tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=(6 * 30))



# Loop through each city in the sheet_data list and search for flights
for city in sheet_data:
    flight = flight_search.search_flights(
        ORIGIN_CITY_IATA , 
        city["iataCode"] , 
        from_time=time_tomorrow , 
        to_time= six_months_from_now
        )
        
    if flight.price < city["lowestPrice"]:
        notification_manager.send_message(flight.price, 
                                          flight.origin_city,
                                          flight.origin_airport, 
                                          flight.destination_city,
                                          flight.destination_airport,
                                          flight.departure_date,
                                          flight.arrival_date)
        
    
    











