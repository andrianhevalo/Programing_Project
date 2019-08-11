import json
import json
import urllib.request


def distance(location_1, location_2, key):
    """
    This function finds the distance from point A to point B
    :param location_1:
    :param location_2:
    :param key:
    :return distance:
    """
    url = 'https://maps.googleapis.com/maps/api/distancematrix/' \
          'json?origins=' + location_1 + '&destinations=' + location_2 + \
          '&key=' + key
    r = urllib.request.urlopen(url)
    r = json.load(r)

    if r['status'] == 'OK':
        return r['rows'][0]['elements'][0]['distance']['text']
    return 0


def find_place(location, radius, tags, key):
    """
    This function finds places id information.
    :param location:
    :param radius:
    :param tags:
    :param key:
    :return place with ids:
    """
    places = []
    url = 'https://maps.googleapis.com/maps/api/place/radarsearch/json' \
          '?location=' + location + '&radius=' + radius + \
          '&type=' + tags + '&key=' + key
    r = urllib.request.urlopen(url)
    r = json.load(r)
    for place in r['results']:
        places.append(place['place_id'])

    return places


def intersection(list1, list2):
    """
    This function finds the intersection in two lists. The list1 is a list with
    places from point A within radius r and list2 is a list with places from B
    within radius r.
    :param list1:
    :param list2:
    :return list:
    """
    return [x for x in list1 if x in list2]


def geo_locating(address, key):
    """
    This function returns longitude and latitude from given address with a api
    key.
    :param address:
    :param key:
    :return longitude and latitude:
    """
    url = "https://maps.googleapis.com/maps/api/geocode/js" \
          "on?address={0}&key={1}".format(address, key)
    r = urllib.request.urlopen(url)
    r = json.load(r)
    return str(r['results'][0]['geometry']["location"]["lat"]) + \
        "," + str(r['results'][0]['geometry']["location"]["lng"])


def units_of_measurement(distance):
    """
    This function returns a distance in usual form without "km"
    :param distance:
    :return string - distance:
    """
    if distance[-2] + distance[-1] == "km":
        return distance[0] + "".join(list(distance)[len(distance)
                                                    - 4: len(distance) - 3]) \
               + "00"
    else:
        return "".join(list(distance)[0:len(distance) - 2])


def places_details(places_list, key):
    """
    This method finds the details from json file and appends them into the list
    :param places_list:
    :param key:
    :return all_place - list:
    """
    all_place = []
    for id in places_list:
        try:
            url = 'https://maps.googleapis.com/maps/api/place/' \
                  'details/json?placeid=' \
                  + id + '&key=' + key
            r = urllib.request.urlopen(url)
            r = json.load(r)
            r = r['result']
            all_place.append([r['name'], (r['geometry']['location']['lat'],
                                          r['geometry']['location']['lng']),
                              r['rating'],
                              r["opening_hours"]['open_now']])

        except:
            continue
    return all_place