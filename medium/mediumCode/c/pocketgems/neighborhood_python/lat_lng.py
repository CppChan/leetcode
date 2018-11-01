"""LatLng object.

Note that this design is not accurate to what latitude and longitude
definitionally mean, but can serve as a stand-in for a correct implementation.
"""
import math


class LatLng:

  def __init__(self, latitude, longitude):
    self.latitude = latitude
    self.longitude = longitude

  def get_distance(lat_lng_1, lat_lng_2):
    """Computes the euclidean distance between two "LatLng" pairs.

    This should be an ok approximation for LatLngs that are close enough
    together.
    """
    lat_dist = abs(lat_lng_2.latitude - lat_lng_1.latitude)
    lng_dist = abs(lat_lng_2.longitude - lat_lng_1.longitude)
    return math.sqrt(math.pow(lat_dist, 2) + math.pow(lng_dist, 2))

  def __str__(self):
    return "(" + str(self.latitude) + "," + str(self.longitude) + ")"

  __repr__ = __str__

  def __hash__(self):
    return int(self.latitude + self.longitude)

  def __eq__(self, object):
    if (isinstance(object, LatLng) and object.latitude == self.latitude and
        object.longitude == self.longitude):
      return True
    return False
