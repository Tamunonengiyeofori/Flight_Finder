# import os
# from pprint import pprint
# from dotenv import load_dotenv
import requests
from data_manager import DataManager
# from datetime import datetime, timedelta
# load_dotenv()

# def search_flights(origin_city_code, destination_city_code, from_time, to_time):
#     api_key = os.getenv("FLIGHT_SEARCH_KEY")
#     tequila_endpoint = "https://tequila-api.kiwi.com"
#     search_endpoint = f"{tequila_endpoint}/v2/search"
    
#     header = {
#             "apikey" : api_key
#         }
        
#     query = {
#             "fly_from": origin_city_code ,
#             "fly_to": destination_city_code , 
#             "date_from": from_time.strftime("%d/%m/%Y") , 
#             "date_to": to_time.strftime("%d/%m/%Y") , 
#             "flight_type": "round" , 
#             "one_for_city": 0 , 
#             "curr": "NGN"
#         }

#     response = requests.get(url=search_endpoint , params=query , headers=header)
#     print(response.raise_for_status)
#     # print(response.text)
#     pprint(response.json()["data"])
    
    
# tomorrow = datetime.now() + timedelta(days=1)
# two_days_time = datetime.now() + timedelta(days=3)

# search_flights("PHC" , "LOS" , tomorrow , two_days_time)

# # print(f"{tomorrow} and {two_days_time}")

user_data = DataManager()
user_data.get_customer_details()