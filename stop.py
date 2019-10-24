import requests
import sys


def get_stop(route_id, direction_id, stop):

    URL = f"https://svc.metrotransit.org/NexTrip/stops/{route_id}/{direction_id}?format=json"

    data = requests.get(URL).json()

    for item in data:

        if stop == item["Text"].strip():
            #comparing stop arg string with stop text, removing whitespace
            route_code = item["Value"]
            print(route_code)
            if route_code is None:
                print("Invalid Stop")
                quit()
            return route_code





