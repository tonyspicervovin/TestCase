from route import get_route
from direction import get_direction
from stop import get_stop
from nextBus import get_next_bus
import sys


def get_uri():

    route_test = "METRO Blue Line"
    direction_test = "north"
    stop_test = "Target Field Station Platform 1"

    route_id = get_route(route_test)
    if route_id is None:
        sys.exit(route_test+" is not a valid route")
    print(route_id)

    direction_id = get_direction(route_id, direction_test)
    if direction_id is None:
        sys.exit(route_test + " does not run " + direction_test)
    print(direction_id)

    stop_id = get_stop(route_id, direction_id, stop_test)
    if stop_id is None:
        sys.exit(stop_test + " is not along " + route_test + " going " + direction_test)

    get_next_bus(route_id, direction_id, stop_id)


