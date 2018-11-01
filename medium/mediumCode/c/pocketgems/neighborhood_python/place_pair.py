"""
A data object that holds the placeName and its latlng information.
"""
from lat_lng import LatLng


class PlacePair:

  def __init__(self, place_name, lat_lng):
    self.place_name = place_name
    self.lat_lng = lat_lng

  def __str__(self):
    return "PlacePair<" + self.place_name + "," + str(self.lat_lng) + ">"

  __repr__ = __str__

  def __hash__(self):
    return hash(self.place_name) + hash(self.lat_lng)

  def __eq__(self, object):
    if (isinstance(object, PlacePair) and
        object.place_name == self.place_name and
        object.lat_lng == self.lat_lng):
      return True
    return False
