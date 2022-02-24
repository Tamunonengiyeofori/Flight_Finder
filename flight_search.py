import os 
from dotenv import load_dotenv

from flight_data import FlightData
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
        header = {
            "apikey" : api_key
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
            "curr": "NGN"
        }
        
        response = requests.get(url=search_endpoint, headers=header, params=query)
        print(response.text)
        print(response.status_code)
        
        try:
            data = response.json() # to change add => data = response.json()["data"][0] and delete price and city variables under data variable
            price = data["data"][0]["conversion"]["NGN"]
            city = data["data"][0]["cityTo"]
            print(f"{city}: #{price}")
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None 
            
        # to change to former version for flight data class remove ["data"][0] from each argument
        flight_data = FlightData(
            price=data["data"][0]["price"],
            origin_city=data["data"][0]["route"][0]["cityFrom"],
            origin_airport=data["data"][0]["route"][0]["flyFrom"],
            destination_city=data["data"][0]["route"][0]["cityTo"],
            destination_airport=data["data"][0]["route"][0]["flyTo"],
            out_date=data["data"][0]["route"][0]["local_departure"].split("T")[0] , 
            return_date = data["data"][0]["route"][1]["local_departure"].split("T")[0])
     
        
        # print(f"{flight_data.destination_city}: #{flight_data.price}")
        print(response.text)
        return flight_data
        
        
        
        
