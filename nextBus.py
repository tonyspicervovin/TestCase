import re
import requests
from datetime import datetime, timedelta


def get_next_bus(route_id, direction_id, stop_id):

    URL = f"https://svc.metrotransit.org/NexTrip/{route_id}/{direction_id}/{stop_id}?format=json"
    print(URL)
    data = requests.get(URL).json()

    # pulling bus information for route at stop going direction
    arrival_time = data[0]["DepartureTime"]
    # accessing departure time
    now = datetime.now()
    # current time

    temp = re.findall(r'\d+', arrival_time)
    res = list(map(int, temp))
    time_code = int(res[0]/1000)
    # extracting 13 digit unix timestamp and changing it to seconds
    thing = datetime.utcfromtimestamp(time_code) - timedelta(hours=5)
    # subtracting 5 hours to get current local time
    date_dif =(thing-now).seconds
    # difference between dates in seconds
    date_dif_in_minutes = int(date_dif/60)
    # difference between dates in minutes rounded down
    # i round down because I prefer to underestimate the time until
    # the next bus in this case

    return date_dif_in_minutes









