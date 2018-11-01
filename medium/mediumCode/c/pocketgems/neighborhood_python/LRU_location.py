
# implement a LRU to store some <location(lat_lng), CompletePlaceData> pair
from complete_place_data import CompletePlaceData
from lat_lng import LatLng

class loc_placedata:
    def __init__(self, lat_lng, c_place_data):
        self.k = lat_lng
        self.v = c_place_data
        self.next = None
        self.pre = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.head = loc_placedata('a', 'a')
        self.tail = loc_placedata('b', 'b')
        self.head.next = self.tail
        self.tail.pre = self.head

    def add(self, point):
        pre_list = self.tail.pre
        self.tail.pre = point
        point.next = self.tail
        point.pre = pre_list
        pre_list.next = point

    def remove(self, point):
        point.pre.next = point.next
        point.next.pre = point.pre

    def get(self, k):
        if k not in self.dic: return -1
        self.remove(self.dic[k])
        newNode = loc_placedata(k, self.dic[k].val)
        self.add(newNode)
        self.dic[k] = newNode
        return newNode.val

    def put(self, k, v):
        if k in self.dic:
            self.remove(self.dic[k])
        newNode = loc_placedata(k, v)
        self.add(newNode)
        self.dic[k] = newNode
        if len(self.dic) > self.capacity:
            delNode = self.head.next
            self.remove(delNode)
            self.dic.__delitem__(delNode.key)