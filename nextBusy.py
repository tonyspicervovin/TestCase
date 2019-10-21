import requests
import sys

def main():

    URL = "http://svc.metrotransit.org/NexTrip/17953?format=json"

    routeTest = "Route 4"
    directionTest = "Northbound"
    stopTest = "DeLaSalle High School"
    query = {'route': routeTest, 'direction':directionTest, 'stop': stopTest}
    data = requests.get(URL, params=query)





if __name__ == '__main__':
        main()