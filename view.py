from route import get_route
from direction import get_direction
from stop import get_stop
from nextBus import get_next_bus
from datetime import datetime


def get_uri(bus_route, stop_name, bus_direction):

    route_id = get_route(bus_route)
    # passing route to method in route.py
    if route_id is None:
        raise ValueError(bus_route+" is not a valid route")

        # if no route is found error message is printed and code exits

    direction_id = get_direction(route_id, bus_direction)
    # passing route id and direction to method in direction.py
    if direction_id is None:
        raise ValueError(bus_route + " does not run " + bus_direction)

        # if no direction is found error message is printed and code exits

    stop_id = get_stop(route_id, direction_id, stop_name)
    # passing route id direction id and stop string to method in stop.py
    if stop_id is None:
        raise ValueError(stop_name + " is not along " + bus_route + " going " + bus_direction)

        # if no stop is found error message is printed and code exits
    now = datetime.now()
    # current time
    minutes = get_next_bus(route_id, direction_id, stop_id, now)
    # finally if we have a proper route direction and stop id we call
    # method in nextBus.py with the arguments

    if minutes < 1:
        print("Less than a minute until next bus")
    else:
        print(str(minutes) + " minutes until next bus/rail")



