import requests
# import pretty print => pprint to format json
from pprint import pprint

class DataManager():
    #This class is responsible for talking to the Google Sheet.
    SHEETY_ENDPOINT = "https://api.sheety.co/ab979ccaa314203fa44ba15da940809e/flightDeals/prices"

    def __init__(self):
        self.destination_data ={}
        
    def get_all_data(self):
        response = requests.get(url=self.sheety_endpoint)
        data = self.response.json()
        self.destination_data = data["prices"]
        return pprint(self.destination_data)
    
        