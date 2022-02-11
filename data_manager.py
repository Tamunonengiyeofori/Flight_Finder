import requests
# import pretty print => pprint to format json
from pprint import pprint

class DataManager():
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/ab979ccaa314203fa44ba15da940809e/flightDeals/prices"
        
        
    def get_all_data(self):
        self.response = requests.get(url=self.sheety_endpoint)
        return pprint(self.response.json()["prices"])
    
        