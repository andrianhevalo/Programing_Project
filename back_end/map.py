from back_end.place import Place
from back_end.function import distance, geo_locating
from collections import defaultdict
from back_end.arrays import DynamicArray


class Map(object):
    """
    Implementation of Map abstract data type
    """
    #  API key
    KEY = "AIzaSyCTcwuB0Z2ygGSMPJhRlnUCPZFEyjU_CMA"

    def __init__(self):
        """
        Initializes ADT attributes.
        Creates a DynamicArray instance from arrays module
        : param None:
        : return None:
        """
        self.details = DynamicArray()
        self._size = 0

    def attractions(self, id_list):
        """
        This method gets a list of places id and appends to the dynamic array
        Place class instances with information taken from API.
        :param id_list:
        :return:
        """
        if not isinstance(id_list, list):
            raise ValueError("Must be list")
        assert id_list != [], "Empty list"
        for i in range(0, len(id_list)):
            try:
                self.details.append(Place(id_list[i]))
                self._size += 1
            except KeyError:
                pass

    def best_rated(self):
        """
        This method sorts the array according to the rating. From highest rated
        to lowest.
        : param None:
        : return None:
        """
        assert self.details != [], "Empty list"
        #  sorting
        return sorted(self.details, key=lambda x: x.rating,
                      reverse=True)

    def get_list(self):
        """
        This method returns a list of details.
        : param None:
        : return self.details:
        """
        return self.details

    def nearer_locations(self, coord1):
        """
        This method sorts the places in the road from the nearest to the
        furthest from A to B.
        : param None:
        : return d:
        """
        d = defaultdict()
        for place in range(0, self._size):
            place_coordinates = geo_locating(self.details[place].location,
                                             Map.KEY)
            d[self.details[place]] = place_coordinates
        return d

    def find_comments(self):
        """
        This method creates a default dictionary that contains user name as a
        key and comment information as a value.
        : param None:
        : return comments:
        """
        assert self._size != 0, "Empty list"
        comments = defaultdict()
        for comment in range(self._size):
            comments[self.details[comment]] = self.details[comment].reviews
        return comments

    def get_size(self):
        """
        This method returns a size of Dynamic Array
        : param None:
        : return self.size:
        """
        return self._size

    def find_website(self):
        """
        This method returns a default dictionary with Place instance as a key
        and web page of the cafe as a value
        : param None:
        : return web:
        """
        assert self._size != 0, "Empty list"
        web = defaultdict()
        for site in range(self._size):
            web[self.details[site]] = self.details[site].web_page
        return web

    def phone_number(self):
        """
        This method creates a dictionary with phones numbers
        : return numbers:
        """
        assert self._size != 0, "Empty list"
        numbers = defaultdict()
        for number in range(self._size):
            numbers[self.details[number]] = self.details[number].number
        return numbers