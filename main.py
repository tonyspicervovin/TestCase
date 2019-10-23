
import sys
from view import get_uri


def main():

    if len(sys.argv) != 4:
        print("Enter a route, stop and direction")

    program_name = sys.argv[0]
    bus_route = sys.argv[1]
    stop_name = sys.argv[2]
    bus_direction = sys.argv[3]

    get_uri(bus_route, stop_name, bus_direction)


if __name__ == '__main__':
        main()