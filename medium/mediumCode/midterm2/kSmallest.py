import heapq

class Solution(object):
	def kSmallest(self, array, k):
		res = []
		if len(array)<k:
			return res
		else:
			heapq.heapify(array)
			for i in xrange(k):
				res.append(heapq.heappop(array))
		return res

if __name__ == "__main__":
    s = Solution()
    print s.kSmallest([3,2,4,6,1],3)
