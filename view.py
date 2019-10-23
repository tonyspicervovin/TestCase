from route import get_route
from direction import get_direction
from stop import get_stop
from nextBus import get_next_bus
import sys


def get_uri(bus_route, stop_name, bus_direction):

    route_test = "METRO Blue Line"
    direction_test = "north"
    stop_test = "Target Field Station Platform 1"

    route_id = get_route(bus_route)
    if route_id is None:
        sys.exit(bus_route+" is not a valid route")
    print(route_id)

    direction_id = get_direction(route_id, bus_direction)
    if direction_id is None:
        sys.exit(bus_route + " does not run " + bus_direction)
    print(direction_id)

    stop_id = get_stop(route_id, direction_id, stop_name)
    if stop_id is None:
        sys.exit(stop_name + " is not along " + bus_route + " going " + bus_direction)

    get_next_bus(route_id, direction_id, stop_id)


