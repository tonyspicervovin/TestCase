import requests

def getNextBus(route_id, direction_id, stop_id):

    URL = f"https://svc.metrotransit.org/NexTrip/{route_id}/{direction_id}/{stop_id}?format=json"
    print(URL)
    data = requests.get(URL).json()

    print(data[0]["DepartureText"])

