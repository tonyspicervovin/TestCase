import requests

def getDirection(routeID, direction):
    URL = f"http://svc.metrotransit.org/NexTrip/directions/{routeID}?format=json"

    data = requests.get(URL).json()
    print(direction)
    if direction.lower == "south" or "southbound":
        print("its south")
        for item in data:
            if item['Text'] == "SOUTHBOUND":
                return item['Value']

    if direction.lower == "north" or "northbound":
        print("its north")
        for item in data:
            if item['Text'] == "NORTHBOUND":
                return item['Value']





