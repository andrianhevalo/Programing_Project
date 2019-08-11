from json import load
from urllib.request import urlopen


class Place:
    """
    A class for place representation
    """

    KEY = "AIzaSyAfA_-78_dtaELR1iEs4OIhz7clxATWFhA"

    def __init__(self, place_id):
        """

        :param place_id:
        """

        url = 'https://maps.googleapis.com/maps/api/place/' \
              'details/json?placeid=' \
              + place_id + '&key=' + Place.KEY
        r = urlopen(url)
        r = load(r)
        r = r['result']
        name = r['name']
        location = ",".join([x['long_name'] for x in r['address_components']])
        rating = r['rating']
        open_now = r["opening_hours"]['open_now']
        phone = r['formatted_phone_number']
        reviews = r['reviews']
        web_page = r['website']
        self.name, self.location, self.rating = name, location, rating
        self.open_now, self.number, self.reviews = open_now, phone, reviews
        self.web_page = web_page

