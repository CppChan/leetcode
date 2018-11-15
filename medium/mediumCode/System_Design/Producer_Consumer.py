from collections import deque


class Data(object):
    def __init__(self, id):
        self.id = id


class Producer(object):

    def __init__(self, queue, count):
        self.queue = queue
        self.count = count

    def produce(self):
        self.count[0] += 1
        self.queue.append(Data(self.count[0]))


class Consumer(object):

    def __init__(self, queue, count):
        self.queue = queue
        self.count = count

    def consume(self):
        res = self.queue.popleft()
        print res.id


if __name__=="__main__":
    queue,count= deque([]),[0]
    p1 = Producer(queue, count)
    p2 = Producer(queue, count)
    p3 = Producer(queue, count)
    c1 = Consumer(queue, count)
    c2 = Consumer(queue, count)
    c3 = Consumer(queue, count)
    p1.produce()
    p2.produce()
    c1.consume()
    p3.produce()
    p2.produce()
    c2.consume()


