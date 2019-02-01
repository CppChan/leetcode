import heapq

class point(object):

	def __init__(self, x, y):
		self.x, self.y = x, y
	def __cmp__(self, other):
		return pow(other.x,2)+pow(other.y,2)-(pow(self.x,2)+pow(self.y,2))

class Solution(object):
	def knearest(self, points, k):
		pq = []
		heapq.heapify(pq)
		for p in points:
			heapq.heappush(pq, point(p[0], p[1]))
			if len(pq)>k: heapq.heappop(pq)
		return pq


s = Solution()
res = s.knearest([[3,4],[2,1],[2,2],[5,3]], 3)
i = 1