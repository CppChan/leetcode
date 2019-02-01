class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.pre = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.head, self.tail = Node('a', 'a'), Node('b', 'b')
        self.head.next = self.tail
        self.tail.pre = self.head
        self.dic = {}

    def get(self, key):
        if key not in self.dic: return -1
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
            self.dic.__delitem__(key)
        temp = Node(key, value)
        self.add(temp)
        self.dic[key] = temp
        if len(self.dic) > self.capacity:
            delNode = self.head.next
            self.remove(delNode)
            self.dic.__delitem__(delNode.key)

    def remove(self, node): #remove from the head
        p, n = node.pre, node.next
        p.next = n
        n.pre = p

    def add(self, node):#put it to the tail
        p = self.tail.pre
        self.tail.pre = node
        node.next = self.tail
        p.next = node
        node.pre = p