import heapq
class tuple(object):
	def __init__(self, letter, time):
		self.letter = letter
		self.time = time
	def __cmp__(self,other):
		return -cmp(self.time, other.time)
class Solution(object):
  def topKFrequent(self, combo, k):
  	dic = {}
  	for i in range(len(combo)):
  		if combo[i] not in dic:
  			dic[combo[i]]=tuple(combo[i], 1)
  		else:
  			dic[combo[i]].time+=1
  	heap = []
  	for item in dic.iteritems():
  		heap.append(item[1])
  	heapq.heapify(heap)
  	res = []
  	for j in range(k):
  		if len(heap)==0:
  			break
  		res.append(heapq.heappop(heap).letter)
  	return res