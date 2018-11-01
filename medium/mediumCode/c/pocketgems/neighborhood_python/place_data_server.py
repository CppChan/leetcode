"""
Place Data Server (PDS).
"""
from place_data import PlaceData
from place_pair import PlacePair
from lat_lng import LatLng
import csv


class PlaceDataServer:

  def __init__(self):
    self.places = {}

  def get_place_data_from_name(self, place_name):
    return self.places[place_name]

  def get_place_data(self, place_name, lat_lng):
    place_list = self.get_place_data_from_name(place_name)
    for place in place_list:
      if LatLng.get_distance(lat_lng, place.lat_lng) <= 1E-7:
        return place
    return None

  def get_nearby_places(self, lat_lng, max_results):
    # TODO: Fix this method
    places = self.places.items()
    PD_list = []#use to store candidate PlaceData instances
    for i in range(len(places)):
        place_list = places[i][1]
        for j in range(len(place_list)):
          PD_list.append(place_list[j])
    PD_distance = {}#compute distacne between target and candidate PlaceData, and put <k,v> pair<PlaceData, distance> into dictionary
    for k in range(len(PD_list)):
      PD_distance[PD_list[k]] = lat_lng.get_distance(lat_lng, PD_list[k])
    PD_distance = PD_distance.items()
    PD_distance.sort(key=lambda x: x[1])#sort the PlaceData based on distance between target and candidiate
    result = []
    for q in range(len(PD_distance)-1, max(len(PD_distance)-max_results, -1), -1):
      result.append(PD_distance[q][0])
    return result # it is final list of PlaceData


  def initialize_server(self, file_name):
    with open(file_name, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',', quotechar="'")
      for parsed_line in reader:
        self.add_place_data_to_server(parsed_line)

  def add_place_data_to_server(self, parsed_line):
    place_list = self.places.get(parsed_line[0], [])
    pd = PlaceData(parsed_line[0],
                   LatLng(float(parsed_line[1]), float(parsed_line[2])),
                   parsed_line[3], int(parsed_line[4]), float(parsed_line[5]))
    place_list.append(pd)
    self.places[parsed_line[0]] = place_list
