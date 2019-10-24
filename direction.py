import requests


def get_direction(routeID, direction):

    URL = f"http://svc.metrotransit.org/NexTrip/directions/{routeID}?format=json"

    data = requests.get(URL).json()
    direction = direction.lower()
    print(direction)
    if direction == "south":
        print("its south")
        for item in data:
            if item['Text'] == "SOUTHBOUND":
                return item['Value']

    if direction == "north":
        print("its north")
        for item in data:
            if item['Text'] == "NORTHBOUND":
                return item['Value']

    if direction == "east":
        print("its east")
        for item in data:
            if item['Text'] == "EASTBOUND":
                return item['Value']

    if direction == "west":
        print("its west")
        for item in data:
            if item['Text'] == "WESTBOUND":
                return item['Value']







