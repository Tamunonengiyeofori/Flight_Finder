import os 
from dotenv import load_dotenv
load_dotenv()
import requests
from datetime import datetime


api_key = os.getenv("FLIGHT_SEARCH_KEY")
tequila_endpoint = "https://tequila-api.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{tequila_endpoint}/locations/query"
        query = {
           "term": city_name , 
           "location_types" : "city"
        }
        headers = {
            "apikey": api_key
        }
        
        response = requests.get(url=location_endpoint, params=query, headers=headers)
        result = response.json()["locations"]
        country_code = result[0]["code"]
        return country_code
    
    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        
        search_endpoint = f"{tequila_endpoint}/v2/search"
        headers = {
            "apikey" , api_key
        }
        
        query = {
            "fly_from": origin_city_code ,
            "fly_to": destination_city_code , 
            "date_from": from_time.strftime("%d/%m/%Y") , 
            "date_to": to_time.strftime("%d/%m/%Y") , 
            "nights_in_dist_from": 7 , 
            "nights_in_dist_to": 28 , 
            "flight_type": "round" , 
            "one_for_city": 1 ,
            "max_stopovers": 0 , 
            "currency": "NGN"
        }
        
        response = requests.get(url=search_endpoint, 
                                headers=headers, 
                                params=query)
        print(response.status_code)
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {self.get_destination_code}.")
            return None
        
        flight_data = FlightData(price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0] , 
            return_date = data["route"][1]["local_departure"].split("T")[0])
        
        print(f"{flight_data.destination_city}: #{flight_data.price}")
        print(response.text)
        return flight_data
        
        
        
            