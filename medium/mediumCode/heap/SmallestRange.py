import heapq
class tuple(object):
	def __init__(self, i, j, val):
		self.i = i
		self.j = j
		self.val = val
	def __cmp__(self,other):
		return cmp(self.val, other.val)
class Solution(object):
  def smallestRange(self, arrays):
  	maxval = -float('inf')
  	list = []
  	for i in range(len(arrays)):
  		list.append(tuple(i,0, arrays[i][0]))
  		maxval = max(maxval, arrays[i][0])
  	heapq.heapify(list)
  	res = [-float('inf'), maxval]
  	while True:
  		minval = heapq.heappop(list)
  		if maxval-minval.val<res[1]-res[0]: res[0],res[1]=minval.val, maxval
  		if minval.j==len(arrays[minval.i])-1:
  			break
  		heapq.heappush(list, tuple(minval.i, minval.j+1, arrays[minval.i][minval.j+1]))
  		maxval = max(maxval,arrays[minval.i][minval.j+1])
  	return res