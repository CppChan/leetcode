import heapq
class Solution(object):
  def ksort(self, array, k):
  	list = []
  	for i in range(k+1):
  		list.append(array[i])
  	queue = heapq.heapify(list)
  	j = 0
  	for i in range(k+1, len(array)):
  		array[j]=heapq.heappop(list)
  		heapq.heappush(list,array[i])
  		j+=1
  	while len(list)>0:
  		array[j]= heapq.heappop(list)
  		j+=1
  	return array


if __name__ == "__main__":
	s = Solution()
	print s.ksort([6,5,4,3,2,1],4)

#maintain a size k heap, and each time pop a element into the previous array