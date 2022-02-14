#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
# import pretty print => pprint to format json
from pprint import pprint
data_manager = DataManager()

sheet_data = data_manager.get_all_data()
for city in sheet_data:
    if city["iataCode"] == "":
        pass