import heapq
class Solution(object):
  def heapsort(self, array):
  	if len(array) == 1: return array
  	for i in range(len(array)-1, -1,-1):
  		self.maxsiftdown(array, len(array), i)
  	n = len(array)
  	for i in range(len(array)-1, 0, -1):
  		array[0], array[i] = array[i], array[0]
  	 	n-=1
  	 	self.maxsiftdown(array, n, 0)
  	return array


  def maxsiftdown(self, array,n,i):
  	left = 2*i+1
  	right = 2*i+2
  	maxindex = i
  	if left<n and array[i]<array[left]:
  		maxindex = left
  	if right <n and array[maxindex]<array[right]:
  		maxindex = right
  	if maxindex!=i:
  		array[i], array[maxindex]= array[maxindex], array[i]
  		self.maxsiftdown(array, n, maxindex)


if __name__=="__main__":
    s = Solution()
    print s.heapsort([2,5,4,3,1,7,6])