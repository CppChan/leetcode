"""Finds the nearest places in the neighborhood.
"""

from complete_place_data import CompletePlaceData


class Neighborhood:

  def __init__(self, place_server, image_server):
    self.place_server = place_server
    self.image_server = image_server

  def get_places(self, lat_lng, max_results):
    # TODO: implement to return a list of CompletePlaceData

    place_list = self.place_server.get_nearby_places(lat_lng, max_results)#first get nearby place
    complete_pd_list = []#use to store complete place data
    for i in range(len(place_list)):
      pd = place_list[i]
      url = self.image_server.get_image_for_place(pd.place_name, pd.lat_lng)
      complete_pd_list.append(CompletePlaceData(pd, url))
    return complete_pd_list