from route import getroute
from direction import getDirection
from stop import getStop
from nextBus import getNextBus
import sys

def getUri():
    routeTest = "METRO Blue Line/."
    directionTest = "north"
    stopTest = "Target Field Station Platform 1"

    route_id = getroute(routeTest)
    if route_id is None:
        sys.exit(routeTest+" is not a valid route")
    print(route_id)

    direction_id = getDirection(route_id, directionTest)
    if direction_id is None:
        sys.exit(routeTest + " does not run " + directionTest)
    print(direction_id)

    stop_id = getStop(route_id, direction_id, stopTest)
    if stop_id is None:
        sys.exit(stopTest + " is not along " + routeTest + " going " + directionTest)

    getNextBus(route_id, direction_id, stop_id)


