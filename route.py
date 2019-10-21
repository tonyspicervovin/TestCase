import requests


def getroute(route):
    URL = "http://svc.metrotransit.org/NexTrip/routes?format=json"

    data = requests.get(URL)


    for item in data:
        print(item)
        ##print(item[0]['Description'])
        print("\n")





