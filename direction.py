import requests


def get_direction(routeID, direction):

    URL = f"http://svc.metrotransit.org/NexTrip/directions/{routeID}?format=json"

    data = requests.get(URL).json()
    direction = direction.lower()
    if direction == "south":
        for item in data:
            if item['Text'] == "SOUTHBOUND":
                return item['Value']

    if direction == "north":
        for item in data:
            if item['Text'] == "NORTHBOUND":
                return item['Value']

    if direction == "east":
        for item in data:
            if item['Text'] == "EASTBOUND":
                return item['Value']

    if direction == "west":
        for item in data:
            if item['Text'] == "WESTBOUND":
                return item['Value']







