import os 
import requests
from dotenv import load_dotenv
from flight_data import FlightData
load_dotenv()



api_key = os.getenv("FLIGHT_SEARCH_KEY")
tequila_endpoint = "https://tequila-api.kiwi.com"

class FlightSearch:
    def __init__(self):
        pass
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{tequila_endpoint}/locations/query"
        
        headers = {"apikey": api_key}
        query = {
           "term": city_name , 
           "location_types" : "city"}
     
        
        
        response = requests.get(url=location_endpoint, params=query, headers=headers)
        result = response.json()["locations"]
        country_code = result[0]["code"]
        return country_code
    
    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        
        search_endpoint = f"{tequila_endpoint}/v2/search"
        headers = {"apikey" : api_key}
        
        query = {
            "fly_from": origin_city_code ,
            "fly_to": destination_city_code , 
            "date_from": from_time.strftime("%d/%m/%Y") , 
            "date_to": to_time.strftime("%d/%m/%Y") , 
            "nights_in_dst_from": 7 , 
            "nights_in_dst_to": 28 , 
            "flight_type": "round" , 
            "one_for_city": 1 ,
            "max_stopovers": 0 , 
            "curr": "USD"
        }
        
        response = requests.get(
            url=search_endpoint, 
            headers=headers, 
            params=query)
        
        # print(response.text)
        print(response.status_code)
        
        try:
            data = response.json()["data"][0] # to change add => data = response.json()["data"][0] and delete price and city variables under data variable
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None 
            
        # to change to former version for flight data class remove ["data"][0] from each argument
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            departure_date=data["route"][0]["local_departure"].split("T")[0] , 
            arrival_date = data["route"][1]["local_departure"].split("T")[0])
     
        
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        # print(response.text)
        return flight_data
        
        
        
        
