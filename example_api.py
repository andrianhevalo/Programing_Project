import urllib.request
import json


def geocode(location):
    key = 'AIzaSyBY2Z626Q1jbvJQF7kDywQI0WAbYYd49Dc'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' \
        + urllib.request.quote(location) + '&types=geocode&key=' + key
    r = urllib.request.urlopen(url)
    r = json.loads(r.read().decode('utf-8'))
    if r["status"] != "OK":
        pass
    else:
        lat = r['results'][0]['geometry']['location']["lat"]
        lng = r['results'][0]['geometry']['location']["lng"]
    return lat, lng


def search_place(lat, lng, radius, types):
    lst = []
    key = 'AIzaSyDZxcGpO0if3u223oqs5iQkrHekcjD-LXU'
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(lat) + ',' + str(lng) + \
          '&radius=' + str(radius) + '&types=' + types + '&key=' + key
    r = urllib.request.urlopen(url)
    r = json.loads(r.read().decode('utf-8'))
    if r["status"] != "OK":
        pass
    else:
        for place in r['results']:
            lst.append(place['name'])
    return lst


def main():
    location = 'Lviv'
    radius = '1000'
    types = 'food'
    print('location: ', location)
    print('radius: ', radius)
    print('type: ', types)
    lat, lng = geocode(location)
    print(search_place(lat, lng, radius, types))


main()