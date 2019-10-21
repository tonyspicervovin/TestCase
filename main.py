import requests
import sys
from route import getroute

def main():

    URL = "http://svc.metrotransit.org/NexTrip/17953?format=json"

    fun = sys.argv[0]
    print(fun)
    routeTest = "4 - New Brighton - Johnson St - Bryant Av - Southtown"
    directionTest = "north"
    stopTest = "Hennepin Ave and 36th St "

    getroute(routeTest)

    data = requests.get(URL)









if __name__ == '__main__':
        main()