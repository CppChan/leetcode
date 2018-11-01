"""PlaceData object
"""
from lat_lng import LatLng


class PlaceData:

  def __init__(self, place_name, lat_lng, address, price_level, rating):
    self.place_name = place_name
    self.lat_lng = lat_lng
    # a String of the # and street name. eg "1 Main St."
    self.address = address
    # an int representing the number of dollar signs (1-4)
    self.price_level = price_level
    # rating returns a double representing the number of stars (1-5)
    self.rating = rating

  def __str__(self):
    return "PlaceData {" + self.place_name + ": " + str(self.lat_lng) + "}"

  __repr__ = __str__
