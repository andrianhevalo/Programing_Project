from back_end.function import *
from back_end.map import Map

key = "AIzaSyAfA_-78_dtaELR1iEs4OIhz7clxATWFhA"


def main(location1, location2, type):
    """

    : param location1:
    : param location2:
    : param type:
    : return:
    """
    from time import time
    current = time()
    places = Map()
    radius = distance(location1, location2, key)
    coord1 = geo_locating(location1, key)
    coord2 = geo_locating(location2, key)
    radius = str(float(units_of_measurement(radius))*0.75)
    p1 = find_place(coord1, radius, type, key)
    p2 = find_place(coord2, radius, type, key)
    r = intersection(p1, p2)
    places.attractions(r)
    res = places.best_rated()
    print("The program conducted the map for {}".format(time() - current))
    return res

if __name__ == '__main__':
    main("RailwayStation,Lviv", "UCU,Lviv", "restaurant")
