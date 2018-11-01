import time
from image_server import ImageServer
from lat_lng import LatLng
from neighborhood import Neighborhood
from place_data_server import PlaceDataServer


class Runner:

  def run(self):
    place_data_server = PlaceDataServer()
    try:
      place_data_server.initialize_server("place_data.csv")
    except IOError as pds_io_exception:
      print("Exception thrown populating PDS data: %s" % pds_io_exception)

    image_server = ImageServer()
    try:
      image_server.initialize_server("image_data.csv")
    except IOError as is_io_exception:
      print("Exception thrown populating IS data: %s" % is_io_exception)

    neighborhood = Neighborhood(place_data_server, image_server)

    while True:
      print("~~~~~~~~~~~A new Server is running.!!")
      places_found = place_data_server.get_place_data_from_name("Starbucks")
      for place in places_found:
        print("***: %s" % place)
      print("***: %s" % place_data_server.get_place_data(
          "Starbucks", LatLng(100, -200)))
      print("***: %s" % image_server.get_image_for_place(
          "Starbucks", LatLng(100, -200)))
      print("*** get_nearby_places: %s" % place_data_server.get_nearby_places(
          LatLng(100, -200), 2))
      print("*** get_places: %s" % neighborhood.get_places(LatLng(100, -200), 1))

      # Feel free to add more print statements here in order to test your code
      # and see how things are working.
      time.sleep(11)


if __name__ == "__main__":
  try:
    Runner().run()
  except KeyboardInterrupt:
    print("~~~~~~~~~~~Server stops.")
