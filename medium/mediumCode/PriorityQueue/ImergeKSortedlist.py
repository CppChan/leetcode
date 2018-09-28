import heapq
class tuple(object):
	def __init__(self, array, index):
		self.array = array
		self.index = index
	def __cmp(self, other):
		return cmp(self.array[self.index], other.array[other.index])

class Solution(object):
  def merge(self, arrayOfArrays):
  	res = []
  	queue = []
  	for i in range(len (arrayOfArrays)):
  		heapq.heappush(queue, tuple(arrayOfArrays[i], 0))
  	heapq.heapify(queue)
  	while queue:
  		temp = heapq.heappop(queue)
  		res.append(temp.array[temp.index])
  		if temp.index<len(temp.array)-1:
  			heapq.heappush(queue, tuple(temp.array, temp.index+1))
  	return res

if __name__ == "__main__":
    s= Solution()
    s.merge([[3],[1,2,3,4,5]])