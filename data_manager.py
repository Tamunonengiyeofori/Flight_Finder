import requests
# import pretty print => pprint to format json
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/80d6f782e639ee62e4871acc43892a3b/flightFinderFlightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/80d6f782e639ee62e4871acc43892a3b/flightFinderFlightDeals/users"

class DataManager():
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        
    def get_all_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                "iataCode" : city["iataCode"]
                }
            }
            
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}" , 
                json=new_data)
            print(response.status_code)
            print(response.text)
            
    def get_customer_details(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        # pprint(data)
        self.customer_data = data["users"]
        return self.customer_data
        
        
    