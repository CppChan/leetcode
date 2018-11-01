class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.pre = None
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.head = Node('a', 'a')
        self.tail = Node('b', 'b')
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
        newNode = Node(k, self.dic[k].val)
        self.add(newNode)
        self.dic[k] = newNode
        return newNode.val

    def put(self, k, v):
        if k in self.dic:
            self.remove(self.dic[k])
        newNode = Node(k, v)
        self.add(newNode)
        self.dic[k] = newNode
        if len(self.dic) > self.capacity:
            delNode = self.head.next
            self.remove(delNode)
            self.dic.__delitem__(delNode.key)