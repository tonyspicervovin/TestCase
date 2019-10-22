import requests


def get_route(route):

    # Url to see all routes
    URL = "http://svc.metrotransit.org/NexTrip/routes?format=json"

    #making call to api
    data = requests.get(URL).json()

    #searching return for a description matching
    for item in data:
        if route == item['Description']:
            route_id = item['Route']
            return route_id







