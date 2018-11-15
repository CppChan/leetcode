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


class Solution2(object):
	def heapsort2(self, input):
		for i in range((len(input)-1)/2-1,-1,-1):
			self.godown(input, i, len(input)-1)
		n = len(input)-1
		while n>0:
			input[0],input[n]=input[n],input[0]
			self.godown(input, 0, n-1)
			n-=1
		return input
	def godown(self, input, i,  end):
		largest = i
		if 2*i+1<=end:
			if input[i]<input[2*i+1]: largest = 2*i+1
		if 2*i+2<=end:
			if input[largest]<input[2*i+2]: largest = 2*i+2
		if largest == i:return
		input[i],input[largest]=input[largest],input[i]
		self.godown(input, largest, end)



if __name__=="__main__":
    s = Solution2()
    print s.heapsort2([2,5,4,3])