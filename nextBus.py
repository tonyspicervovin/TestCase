import requests
from datetime import datetime


def get_next_bus(route_id, direction_id, stop_id):

    URL = f"https://svc.metrotransit.org/NexTrip/{route_id}/{direction_id}/{stop_id}?format=json"
    print(URL)
    data = requests.get(URL).json()
    arrival_time = data[0]["DepartureText"]
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    print(arrival_time)
    FMT = '%H:%M'
    tdelta = datetime.strptime(arrival_time, FMT) - datetime.strptime(current_time, FMT)
    minutes_to_arrival = tdelta.seconds / 60
    print(f"{minutes_to_arrival:.0f} minutes")




