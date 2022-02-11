class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_search_api = "https://tequila-api.kiwi.com/v2/search"
        self.search_parameters = {
            "fly_from": "" , 
            "flt_to": "" , 
            "dateFrom": "" , 
            "dateTo": ""
        }