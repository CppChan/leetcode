from collections import deque


class HitCounter(object):

    def __init__(self):
        self.queue = deque([])
        self.hitcount = 0
        self.lasthit = 0

    def hit(self, timestamp):
        if self.lasthit == timestamp:
            self.queue[-1][-1] += 1
            self.hitcount += 1
            return
        self.queue.append([timestamp, 1])
        self.lasthit = timestamp
        self.hitcount += 1
        while len(self.queue) > 0 and timestamp - self.queue[0][0] >= 300:#remember len(self.queue) > 0
            self.hitcount -= self.queue[0][1]
            self.queue.popleft()

    def getHits(self, timestamp):
        while len(self.queue) > 0 and timestamp - self.queue[0][0] >= 300: #here need to judge again
            self.hitcount -= self.queue[0][1]
            self.queue.popleft()
        return self.hitcount