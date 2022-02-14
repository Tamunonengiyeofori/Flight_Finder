import os 
from dotenv import load_dotenv
load_dotenv()
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self , city_name):
        self.api_key = os.getenv("FLIGHT_SEARCH_KEY")
        self.flight_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.query = {
           "term": city_name , 
           "location_types" : "city"
        }
        self.headers = {
            "apikey": self.api_key
        }
        
    def get_destination_code(self):
        self.response = requests.get(url=self.flight_endpoint, params=self.query)
        result = self.response.json()
        country_code = result["location"]
        return country_code
            