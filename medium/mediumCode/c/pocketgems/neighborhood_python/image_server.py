""" Image Server (IS)"""

import csv
import time
from lat_lng import LatLng
from place_pair import PlacePair


class ImageServer:

  def __init__(self):
    self.image_urls = {}

  def get_image_for_place(self, place_name, lat_lng):
    try:
      time.sleep(1.1)  # DO NOT REMOVE
      # simulates time delay for IS being located far away from our users.
    except KeyboardInterrupt:
      print('~~~~~~~~~~~IS stops.')
    return self.image_urls.get(PlacePair(place_name, lat_lng))

  def initialize_server(self, file_name):
    with open(file_name, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for parsed_line in reader:
        self.add_image_to_server(parsed_line)

  def add_image_to_server(self, parsed_line):
    lat_lng = LatLng(float(parsed_line[1]), float(parsed_line[2]))
    self.image_urls[PlacePair(parsed_line[0], lat_lng)] = parsed_line[3]
