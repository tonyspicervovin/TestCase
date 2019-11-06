import re
import requests
from datetime import datetime, timedelta


def get_next_bus(route_id, direction_id, stop_id, now):

    URL = f"https://svc.metrotransit.org/NexTrip/{route_id}/{direction_id}/{stop_id}?format=json"

    data = requests.get(URL).json()

    # pulling bus information for route at stop going direction
    try:
        arrival_time = data[0]["DepartureTime"]
    except IndexError:
        print("No more buses leaving today")
        quit()
            
    # accessing departure time
    date_dif_in_minutes = process_time_to_minutes(arrival_time, now)
    return date_dif_in_minutes

def process_time_to_minutes(arrival_time, now):

    temp = re.findall(r'\d+', arrival_time)
    res = list(map(int, temp))
    time_code = int(res[0] / 1000)
    # extracting 13 digit unix timestamp and changing it to seconds
    thing = datetime.utcfromtimestamp(time_code) - timedelta(hours=6)
    # subtracting 6 hours to get current local time
    date_dif = (thing - now).seconds

    # difference between dates in seconds
    date_dif_in_minutes = int(date_dif / 60)
    # difference between dates in minutes rounded down
    # i round down because I prefer lsto underestimate the time until
    # the next bus in this case
    return date_dif_in_minutes






