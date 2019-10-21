from route import getroute
from direction import getDirection

def getUri():
    routeTest = "4 - New Brighton - Johnson St - Bryant Av - Southtown"
    directionTest = "north"
    stopTest = "Hennepin Ave and 36th St "

    routeID = getroute(routeTest)
    directionID = getDirection(routeID, directionTest)
    print(directionID)

    print(routeID)