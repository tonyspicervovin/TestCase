import requests


def get_route(route):
    route_id = get_routes(route)
    return route_id
    # Url to see all routes



def get_routes(route):

    URL = "http://svc.metrotransit.org/NexTrip/routes?format=json"

    # making call to api
    data = requests.get(URL).json()

    # searching return for a description matching
    for item in data:
        if route == item['Description']:
            route_id = item['Route']
            return route_id






