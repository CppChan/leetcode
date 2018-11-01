"""
A single data class that holds all the information from PlaceData and the image url.
"""

class CompletePlaceData:
  # TODO: Implement

    def __init__(self, place_data, url):
      self.place_name = place_data.place_name
      self.lat_lng = place_data.lat_lng
      # a String of the # and street name. eg "1 Main St."
      self.address = place_data.address
      # an int representing the number of dollar signs (1-4)
      self.price_level = place_data.price_level
      # rating returns a double representing the number of stars (1-5)
      self.rating = place_data.rating
      self.image_url = url

    def __str__(self):
      return "PlaceData {" + self.place_name + ": " + str(self.lat_lng) + "}"

    __repr__ = __str__

